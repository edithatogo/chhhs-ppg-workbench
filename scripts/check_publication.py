#!/usr/bin/env python3
"""Fail closed on secret findings, private artefacts or incomplete scan scope.

Scan Git objects, never the working copy of a staged file. Reports contain only
redacted detector results and stay in a private temporary directory. Console output
contains counts/codes only. This is not general DLP or clinical approval.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
GITLEAKS_VERSION = '8.30.1'
POLICY_FILES = ('.gitleaks.toml', '.gitleaksignore', 'scripts/check_publication.py')
PRIVATE_PARTS = {'.local', 'private', 'outputs', 'receipts', '.venv', 'node_modules', '__pycache__'}
PRIVATE_SUFFIXES = {'.xls', '.xlsx', '.xlsb', '.xlsm', '.msg', '.eml', '.pdf', '.docx',
                    '.zip', '.bundle', '.pem', '.pfx', '.key', '.pyc'}
MAX_BLOB = 5 * 1024 * 1024
MAX_SNAPSHOT = 64 * 1024 * 1024


class PublicationError(ValueError):
    """A safe, non-sensitive failure code suitable for console output."""


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(['git', *args], cwd=root, capture_output=True, timeout=30)
    if result.returncode:
        raise PublicationError('git-read-failed')
    return result.stdout


def forbidden_path(name: str) -> bool:
    path = PurePosixPath(name)
    if (path.is_absolute() or '..' in path.parts or '\\' in name
            or any(ord(c) < 32 or ord(c) == 127 for c in name)):
        return True
    lower = name.lower()
    if any(p.lower() in PRIVATE_PARTS for p in path.parts):
        return True
    if path.name.lower().startswith('.env') and path.name != '.env.example':
        return True
    return lower.endswith('.local.json') or path.suffix.lower() in PRIVATE_SUFFIXES


def records(root: Path, revision: str | None) -> list[tuple[str, str, str]]:
    args = ('ls-tree', '-rz', '--full-tree', revision) if revision else ('ls-files', '--stage', '-z')
    found = []
    for row in git(root, *args).split(b'\0'):
        if not row:
            continue
        header, raw_name = row.split(b'\t', 1)
        mode, middle, last = header.decode('ascii').split()
        if not revision and last != '0':
            raise PublicationError('unmerged-index')
        oid = last if revision else middle
        name = raw_name.decode('utf-8', errors='strict')
        if forbidden_path(name):
            raise PublicationError('private-or-unsafe-path')
        if mode == '160000' and name == '.agents/plugins/conductor':
            # Existing pinned upstream gitlink; checked separately by check_setup.
            continue
        if mode not in ('100644', '100755'):
            raise PublicationError('unsupported-git-entry')
        found.append((mode, oid, name))
    return found


def snapshot(root: Path, revision: str | None, destination: Path) -> int:
    entries = records(root, revision)
    if not entries:
        return 0
    metadata = []
    # Git and Python were both observed blocked writing metadata pipes inside
    # a hook, even with bounded chunks. File-backed streams eliminate that
    # cyclic wait and let subprocess.run enforce its process timeout.
    for begin in range(0, len(entries), 32):
        chunk = entries[begin:begin + 32]
        request = ('\n'.join(oid for _, oid, _ in chunk) + '\n').encode()
        with tempfile.TemporaryFile() as source, tempfile.TemporaryFile() as output, \
                tempfile.TemporaryFile() as errors:
            source.write(request)
            source.seek(0)
            sizes = subprocess.run(['git', 'cat-file', '--batch-check'], cwd=root,
                                   stdin=source, stdout=output, stderr=errors, timeout=30)
            if sizes.returncode:
                raise PublicationError('git-blob-read-failed')
            output.seek(0)
            metadata.extend(output.read().splitlines())
    if len(metadata) != len(entries):
        raise PublicationError('incomplete-git-metadata')
    aggregate = 0
    for entry, row in zip(entries, metadata):
        observed, kind, raw_size = row.decode('ascii').split()
        size = int(raw_size)
        aggregate += size
        if (observed != entry[1] or kind != 'blob' or size > MAX_BLOB
                or aggregate > MAX_SNAPSHOT):
            raise PublicationError('unsupported-or-oversize-blob')
    # Read bounded individual blobs without an input pipe. The pre-commit check
    # must not deadlock while holding Git's shared index lock.
    for (_, oid, name), row in zip(entries, metadata):
        content = git(root, 'cat-file', 'blob', oid)
        if len(content) != int(row.decode('ascii').split()[2]):
            raise PublicationError('incomplete-git-blob')
        try:
            content.decode('utf-8')
        except UnicodeDecodeError as exc:
            raise PublicationError('non-text-tracked-artefact') from exc
        if b'\0' in content:
            raise PublicationError('binary-tracked-artefact')
        output = destination / name
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
    return len(entries)


def scanner() -> str:
    executable = shutil.which('gitleaks')
    if not executable:
        raise PublicationError('gitleaks-missing')
    result = subprocess.run([executable, 'version'], capture_output=True, text=True, timeout=20)
    if result.returncode or result.stdout.strip().removeprefix('v') != GITLEAKS_VERSION:
        raise PublicationError('gitleaks-version-mismatch')
    return executable


def scan(executable: str, root: Path, mode: str, target: Path,
         report: Path, extra_refs: tuple[str, ...] = ()) -> None:
    cmd = [executable, mode, '--config', str(root / '.gitleaks.toml'),
           '--gitleaks-ignore-path', str(root / '.gitleaksignore'),
           '--ignore-gitleaks-allow', '--redact', '--no-banner', '--no-color',
           '--max-decode-depth', '5', '--timeout', '120',
           '--report-format', 'json', '--report-path', str(report)]
    if mode == 'git':
        cmd += ['--log-opts', ' '.join(('--all', *extra_refs))]
    cmd.append('.' if mode == 'dir' else str(target))
    # Disallow ambient config/baseline variables from changing the policy.
    env = {k: v for k, v in os.environ.items() if not k.startswith('GITLEAKS_')}
    result = subprocess.run(cmd, cwd=target if mode == 'dir' else root,
                            capture_output=True, env=env, timeout=150)
    if result.returncode:
        if report.is_file():
            private = root / '.local' / 'publication-checks'
            private.mkdir(parents=True, exist_ok=True, mode=0o700)
            shutil.copyfile(report, private / (uuid.uuid4().hex + '.json'))
        raise PublicationError('secret-or-binding-findings' if result.returncode == 1
                               else 'gitleaks-execution-failed')
    if mode == 'git' and (b' ERR ' in result.stderr
                          or not re.search(rb'\b[1-9][0-9]* commits? scanned', result.stderr)):
        raise PublicationError('gitleaks-incomplete-history')
    if not report.is_file() or json.loads(report.read_text()) != []:
        raise PublicationError('missing-or-inconsistent-scan-report')


def check(root: Path = ROOT, *, mode: str = 'history',
          extra_refs: tuple[str, ...] = ()) -> dict:
    root = root.resolve()
    if mode not in ('staged', 'history'):
        raise PublicationError('invalid-scan-mode')
    for name in POLICY_FILES[:2]:
        if not (root / name).is_file() or (root / name).is_symlink():
            raise PublicationError('scan-policy-missing')
    executable = scanner()
    if mode == 'history':
        if git(root, 'rev-parse', '--is-shallow-repository').strip() != b'false':
            raise PublicationError('shallow-history')
        # Reject disallowed paths even if they were deleted from HEAD later.
        names = git(root, 'log', '--all', *extra_refs, '--format=', '--name-only',
                    '--no-renames', '--diff-filter=ACMR').decode('utf-8').splitlines()
        if any(forbidden_path(name) for name in names if name):
            raise PublicationError('private-path-in-history')
    with tempfile.TemporaryDirectory(prefix='ppg-publication-') as directory:
        work = Path(directory)
        revisions = [None] if mode == 'staged' else ['HEAD', *extra_refs]
        count = 0
        for i, revision in enumerate(dict.fromkeys(revisions)):
            target = work / str(i)
            target.mkdir()
            count += snapshot(root, revision, target)
            scan(executable, root, 'dir', target, work / f'tree-{i}.json')
        if mode == 'history':
            scan(executable, root, 'git', root, work / 'history.json', extra_refs)
    return {'mode': mode, 'filesChecked': count, 'gitleaksVersion': GITLEAKS_VERSION}


def policy_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for name in POLICY_FILES:
        digest.update(name.encode() + b'\0' + (root / name).read_bytes() + b'\0')
    return digest.hexdigest()


def history_hash(root: Path, extra_refs: tuple[str, ...] = ()) -> str:
    commits = sorted(git(root, 'rev-list', '--all', *extra_refs).splitlines())
    return hashlib.sha256(b'\n'.join(commits)).hexdigest()


def verify_content_review(root: Path, receipt: Path | None, repo: str,
                          extra_refs: tuple[str, ...] = (), *, visibility: str = 'private') -> None:
    """Require actual content review bound to exact commit/tree/policy/destination."""
    if receipt is not None and not receipt.is_absolute():
        receipt = root / receipt
    if receipt is None or not receipt.is_file():
        raise PublicationError('confidential-content-review-required')
    if receipt.is_symlink() or not receipt.resolve().is_relative_to((root / '.local').resolve()):
        raise PublicationError('review-receipt-must-stay-private')
    try:
        value = json.loads(receipt.read_text())
        reviewed_at = datetime.fromisoformat(value['reviewedAtUtc'].replace('Z', '+00:00'))
        if reviewed_at.utcoffset() is None or reviewed_at > datetime.now(timezone.utc):
            raise ValueError('date')
        expected = {
            'schemaVersion': 1,
            'scope': 'all-reachable-history-and-head',
            'reviewedCommit': git(root, 'rev-parse', 'HEAD').decode().strip(),
            'reviewedTree': git(root, 'rev-parse', 'HEAD^{tree}').decode().strip(),
            'policySHA256': policy_hash(root),
            'historySHA256': history_hash(root, extra_refs),
            'repository': repo,
            'confidentialContentReviewed': True,
        }
        if (visibility not in ('private', 'public')
                or value.get('visibility', 'private') != visibility
                or value.get('confidentialContentReviewed') is not True
                or any(value.get(k) != v for k, v in expected.items())):
            raise ValueError('scope')
        if not isinstance(value.get('reviewer'), str) or not value['reviewer'].strip():
            raise ValueError('reviewer')
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        raise PublicationError('content-review-stale-or-invalid') from exc


def pushed_refs(stream: str) -> tuple[str, ...]:
    result = []
    for line in stream.splitlines():
        parts = line.split()
        if len(parts) != 4 or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', parts[1]):
            raise PublicationError('invalid-pre-push-input')
        if set(parts[1]) != {'0'}:
            result.append(parts[1] + '^{commit}')
    return tuple(result)


def repository_from_url(url: str | None) -> str:
    match = re.fullmatch(r'(?:https://github\.com/|git@github\.com:)([A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+?)(?:\.git)?', url or '')
    if not match:
        raise PublicationError('unsupported-publication-destination')
    return match.group(1)


def verify_destination(repo: str, visibility: str = 'private') -> None:
    if visibility not in ('private', 'public'):
        raise PublicationError('invalid-publication-visibility')
    executable = shutil.which('gh')
    if not executable:
        raise PublicationError('github-cli-required-for-visibility-check')
    result = subprocess.run([executable, 'repo', 'view', repo, '--json', 'nameWithOwner,isPrivate'],
                            capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise PublicationError('github-destination-unverified')
    try:
        value = json.loads(result.stdout)
        if value.get('isPrivate') is not (visibility == 'private') or value.get('nameWithOwner', '').lower() != repo.lower():
            raise ValueError('destination')
    except (ValueError, AttributeError) as exc:
        raise PublicationError('github-destination-not-' + visibility) from exc


def verify_private_destination(repo: str) -> None:
    verify_destination(repo, 'private')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('staged', 'history', 'pre-push'), default='history')
    parser.add_argument('--remote-url', help='Supplied by the pre-push hook, not a new remote.')
    parser.add_argument('--visibility', choices=('private', 'public'),
                        default=os.environ.get('PPG_PUBLICATION_VISIBILITY', 'private'))
    args = parser.parse_args()
    try:
        refs = pushed_refs(sys.stdin.read()) if args.mode == 'pre-push' else ()
        result = check(mode='history' if args.mode == 'pre-push' else args.mode, extra_refs=refs)
        if args.mode == 'pre-push':
            repo = repository_from_url(args.remote_url)
            receipt = Path(os.environ.get('PPG_CONTENT_REVIEW', str(ROOT / '.local/publication-review.json')))
            verify_content_review(ROOT, receipt, repo, refs, visibility=args.visibility)
            if args.visibility == 'private':
                verify_private_destination(repo)
            else:
                verify_destination(repo, args.visibility)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (PublicationError, OSError, subprocess.TimeoutExpired, UnicodeError) as exc:
        code = str(exc) if isinstance(exc, PublicationError) else 'publication-check-error'
        print('Publication check refused: ' + code, file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
