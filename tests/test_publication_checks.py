"""Offline integration checks using disposable Git repositories and synthetic data."""
from datetime import datetime, timezone
import json
import io
import os
import stat
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_publication as gate
import install_publication_hooks as hooks
import publish_github as publisher


def secret() -> str:
    # Deliberately assembled at runtime: never a real credential or tracked literal.
    return 'gh' + 'p_' + 'A7b9C2d4E6f8G0h1J3k5L7m9N2p4Q6r8S0t1'


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='ppg-gate-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'Fictional Gate Test')
        self.git('config', 'user.email', 'gate@example.invalid')
        self.git('config', 'commit.gpgsign', 'false')
        for name in gate.POLICY_FILES:
            self.write(name, (ROOT / name).read_text())
        self.write('README.md', 'Fictional repository.\n')
        self.git('add', '.')
        self.commit()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def commit(self):
        # Disposable synthetic repo only; no shared/user hooks run in these fixtures.
        self.git('-c', 'core.hooksPath=/dev/null', 'commit', '-qm', 'fictional test')

    def assert_refused(self, code, **kwargs):
        with self.assertRaisesRegex(gate.PublicationError, code):
            gate.check(self.root, **kwargs)

    def test_clean_complete_history_passes(self):
        self.assertEqual(gate.check(self.root)['mode'], 'history')

    def test_staged_secret_is_read_from_index_even_when_worktree_is_clean(self):
        self.write('sample.txt', 'access_token = "' + secret() + '"\n')
        self.git('add', 'sample.txt')
        self.write('sample.txt', 'Clean unstaged replacement.\n')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_deleted_historical_secret_still_blocks(self):
        self.write('sample.txt', 'access_token = "' + secret() + '"\n')
        self.git('add', 'sample.txt'); self.commit()
        self.git('rm', '-q', 'sample.txt'); self.commit()
        self.assert_refused('secret-or-binding-findings')

    def test_exact_fictional_hashes_pass_but_other_secret_in_same_file_fails(self):
        for name in ('proposal', 'report'):
            self.write(f'templates/identity-resolution/{name}.json',
                       (ROOT / f'templates/identity-resolution/{name}.json').read_text())
        self.git('add', 'templates')
        gate.check(self.root, mode='staged')
        self.commit()
        gate.check(self.root)
        path = self.root / 'templates/identity-resolution/proposal.json'
        value = json.loads(path.read_text()); value['access_token'] = secret()
        path.write_text(json.dumps(value, indent=2) + '\n')
        self.git('add', 'templates')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_inline_allow_comment_cannot_suppress_secret(self):
        self.write('sample.txt', 'access_token = "' + secret() + '" # gitleaks' + ':allow\n')
        self.git('add', 'sample.txt')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_renamed_fictional_hash_does_not_get_path_exception(self):
        self.write('nested/templates/identity-resolution/proposal.json',
                   (ROOT / 'templates/identity-resolution/proposal.json').read_text())
        self.git('add', 'nested')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_operational_binding_in_deleted_history_is_rejected(self):
        value = 'https://' + 'healthqld' + '.sharepoint.com/teams/FICTIONAL'
        self.write('sample.txt', value)
        self.git('add', 'sample.txt'); self.commit()
        self.git('rm', '-q', 'sample.txt'); self.commit()
        self.assert_refused('secret-or-binding-findings')

    def test_dataverse_url_in_deleted_history_is_rejected(self):
        self.write('sample.txt', 'https://' + 'fictional-org.crm6.dynamics.com/')
        self.git('add', 'sample.txt'); self.commit()
        self.git('rm', '-q', 'sample.txt'); self.commit()
        self.assert_refused('secret-or-binding-findings')

    def test_native_identifier_context_is_rejected_from_index(self):
        import uuid
        for label in ('candidate_environment_id', 'native_action_id', 'UniqueId', 'ETag'):
            with self.subTest(label=label):
                self.write('sample.txt', label + ': ' + str(uuid.uuid4()))
                self.git('add', 'sample.txt')
                self.write('sample.txt', 'Unstaged clean replacement')
                self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_deleted_native_identifier_still_blocks(self):
        import uuid
        self.write('sample.txt', 'native_flow_id: ' + str(uuid.uuid4()))
        self.git('add', 'sample.txt'); self.commit()
        self.git('rm', '-q', 'sample.txt'); self.commit()
        self.assert_refused('secret-or-binding-findings')

    def test_synthetic_uuid_exception_is_value_and_path_scoped(self):
        import uuid
        value = '11111111-' + '1111-4111-8111-111111111111'
        fixture = 'tests/test_ai_evaluation.py'
        self.write(fixture, "nativeUniqueId='" + value + "'\n")
        self.git('add', fixture)
        gate.check(self.root, mode='staged')
        self.write(fixture, "nativeUniqueId='" + str(uuid.uuid4()) + "'\n")
        self.git('add', fixture)
        self.assert_refused('secret-or-binding-findings', mode='staged')
        self.git('rm', '-q', '--cached', fixture)
        self.write('unreviewed.py', "nativeUniqueId='" + value + "'\n")
        self.git('add', 'unreviewed.py')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_unlabelled_public_identifier_and_placeholder_pass(self):
        import uuid
        self.write('sample.txt', 'Public specification: ' + str(uuid.uuid4()) +
                   '\nenvironment_id: <private binding>\n')
        self.git('add', 'sample.txt')
        gate.check(self.root, mode='staged')

    def test_operational_email_is_rejected(self):
        self.write('sample.txt', 'fictional.person@' + 'health.qld.gov.au')
        self.git('add', 'sample.txt')
        self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_private_paths_and_operational_document_types_are_rejected(self):
        for name in ('.local/receipt.json', 'deep/private/person.txt', 'policy.docx', '.env',
                     'binding.local.json', 'output.PDF'):
            with self.subTest(name=name):
                self.write(name, 'FICTIONAL')
                self.git('add', '-f', name)
                self.assert_refused('private-or-unsafe-path', mode='staged')
                self.git('reset', '-q', '--', name)

    def test_deleted_private_path_in_history_is_rejected(self):
        self.write('.local/receipt.json', '{}')
        self.git('add', '-f', '.local/receipt.json'); self.commit()
        self.git('rm', '-q', '.local/receipt.json'); self.commit()
        self.assert_refused('private-path-in-history')

    def test_symlink_and_binary_are_rejected(self):
        (self.root / 'linked.txt').symlink_to('/etc/hosts')
        self.git('add', 'linked.txt')
        self.assert_refused('unsupported-git-entry', mode='staged')
        self.git('reset', '-q', '--', 'linked.txt')
        (self.root / 'data.txt').write_bytes(b'FICTIONAL\0BINARY')
        self.git('add', 'data.txt')
        self.assert_refused('binary-tracked-artefact', mode='staged')

    def test_missing_scanner_and_wrong_version_fail_closed(self):
        with patch.object(gate.shutil, 'which', return_value=None):
            self.assert_refused('gitleaks-missing', mode='staged')
        with patch.object(gate, 'GITLEAKS_VERSION', '0.0.0'):
            self.assert_refused('gitleaks-version-mismatch', mode='staged')

    def test_missing_policy_and_shallow_history_fail_closed(self):
        path = self.root / '.gitleaks.toml'; path.unlink()
        self.assert_refused('scan-policy-missing')
        self.write('.gitleaks.toml', (ROOT / '.gitleaks.toml').read_text())
        oid = self.git('rev-parse', 'HEAD').decode().strip()
        (self.root / '.git/shallow').write_text(oid + '\n')
        self.assert_refused('shallow-history')

    def test_gitlinks_other_than_pinned_upstream_are_refused(self):
        oid = self.git('rev-parse', 'HEAD').decode().strip()
        self.git('update-index', '--add', '--cacheinfo', '160000,' + oid + ',unexpected-module')
        self.assert_refused('unsupported-git-entry', mode='staged')

    def test_ambient_config_cannot_disable_policy(self):
        self.write('sample.txt', 'access_token = "' + secret() + '"\n')
        self.git('add', 'sample.txt')
        with patch.dict(os.environ, {'GITLEAKS_CONFIG': '/does/not/exist',
                                    'GITLEAKS_CONFIG_TOML': 'title="empty"'}):
            self.assert_refused('secret-or-binding-findings', mode='staged')

    def test_unreferenced_pushed_commit_is_scanned(self):
        self.write('sample.txt', 'access_token = "' + secret() + '"\n')
        self.git('add', 'sample.txt'); self.commit()
        secret_oid = self.git('rev-parse', 'HEAD').decode().strip()
        self.git('reset', '--hard', '-q', 'HEAD~1')
        gate.check(self.root)
        refs = gate.pushed_refs('refs/heads/main ' + secret_oid + ' refs/heads/main ' + '0' * 40)
        self.assert_refused('secret-or-binding-findings', extra_refs=refs)

    def review_receipt(self):
        receipt = self.root / '.local/content-review.json'
        self.write('.local/content-review.json', json.dumps({
            'schemaVersion': 1, 'scope': 'all-reachable-history-and-head',
            'reviewedCommit': self.git('rev-parse', 'HEAD').decode().strip(),
            'reviewedTree': self.git('rev-parse', 'HEAD^{tree}').decode().strip(),
            'policySHA256': gate.policy_hash(self.root),
            'historySHA256': gate.history_hash(self.root), 'repository': 'example/fictional',
            'reviewer': 'Fictional test reviewer',
            'reviewedAtUtc': datetime.now(timezone.utc).isoformat(),
            'confidentialContentReviewed': True}))
        return receipt

    def test_review_is_required_and_bound_to_commit_policy_and_destination(self):
        with self.assertRaisesRegex(gate.PublicationError, 'review-required'):
            gate.verify_content_review(self.root, None, 'example/fictional')
        receipt = self.review_receipt()
        gate.verify_content_review(self.root, receipt, 'example/fictional')
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'other/fictional')
        self.write('README.md', 'New fictional revision')
        self.git('add', 'README.md'); self.commit()
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')
        receipt = self.review_receipt()
        self.write('.gitleaksignore', '# changed policy\n')
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')

    def test_review_visibility_is_explicit_and_bound(self):
        receipt = self.review_receipt()
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional', visibility='public')
        value = json.loads(receipt.read_text()); value['visibility'] = 'public'
        receipt.write_text(json.dumps(value))
        gate.verify_content_review(self.root, receipt, 'example/fictional', visibility='public')
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')

    def test_public_destination_must_match_reviewed_visibility_and_identity(self):
        for private, repo, accepted in [(False, 'example/fictional', True),
                                         (True, 'example/fictional', False),
                                         (False, 'example/other', False)]:
            result = subprocess.CompletedProcess([], 0, json.dumps({'nameWithOwner': repo, 'isPrivate': private}), '')
            with patch.object(gate.shutil, 'which', return_value='gh'), patch.object(gate.subprocess, 'run', return_value=result):
                if accepted:
                    gate.verify_destination('example/fictional', 'public')
                else:
                    with self.assertRaisesRegex(gate.PublicationError, 'destination-not-public'):
                        gate.verify_destination('example/fictional', 'public')

    def test_review_is_invalidated_by_new_branch_history_without_head_change(self):
        self.git('checkout', '-qb', 'other')
        self.write('branch.txt', 'Fictional branch')
        self.git('add', 'branch.txt'); self.commit()
        other = self.git('rev-parse', 'HEAD').decode().strip()
        self.git('checkout', '-q', 'main')
        self.git('branch', '-D', 'other')
        receipt = self.review_receipt()
        self.git('branch', 'other', other)
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')

    def test_gitleaks_success_without_history_is_refused(self):
        with tempfile.TemporaryDirectory() as d:
            report = Path(d) / 'report.json'; report.write_text('[]')
            result = subprocess.CompletedProcess([], 0, b'', b' ERR git failed\n0 commits scanned')
            with patch.object(gate.subprocess, 'run', return_value=result):
                with self.assertRaisesRegex(gate.PublicationError, 'incomplete-history'):
                    gate.scan('gitleaks', self.root, 'git', self.root, report)

    def test_invalid_review_and_nonprivate_receipt_are_refused(self):
        receipt = self.review_receipt(); value = json.loads(receipt.read_text())
        value['confidentialContentReviewed'] = False; receipt.write_text(json.dumps(value))
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')
        value['confidentialContentReviewed'] = 1; receipt.write_text(json.dumps(value))
        with self.assertRaisesRegex(gate.PublicationError, 'stale-or-invalid'):
            gate.verify_content_review(self.root, receipt, 'example/fictional')
        receipt = self.review_receipt()
        public = self.write('public-review.json', receipt.read_text())
        with self.assertRaisesRegex(gate.PublicationError, 'stay-private'):
            gate.verify_content_review(self.root, public, 'example/fictional')

    def test_installer_preserves_existing_hook_configuration(self):
        self.git('config', 'core.hooksPath', 'custom-hooks')
        with self.assertRaisesRegex(ValueError, 'retained'):
            hooks.install(self.root)
        self.assertEqual(self.git('config', '--get', 'core.hooksPath').strip(), b'custom-hooks')
        self.git('config', '--unset', 'core.hooksPath')
        hook = self.write('.git/hooks/pre-commit', '# existing hook')
        with self.assertRaisesRegex(ValueError, 'retained'):
            hooks.install(self.root)
        self.assertEqual(hook.read_text(), '# existing hook')

    def test_hooks_execute_and_block_synthetic_commit_and_push(self):
        shutil.copytree(ROOT / '.githooks', self.root / '.githooks')
        hooks.install(self.root)
        interpreter = self.root / '.venv/bin/python'
        interpreter.parent.mkdir(parents=True)
        interpreter.symlink_to(sys.executable)
        self.write('.python-version', '.'.join(map(str, sys.version_info[:3])))
        self.write('sample.txt', 'access_token = "' + secret() + '"\n')
        self.git('add', 'sample.txt')
        result = subprocess.run(['git', 'commit', '-qm', 'must fail'], cwd=self.root,
                                capture_output=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b'secret-or-binding-findings', result.stderr)
        self.assertNotIn(secret().encode(), result.stdout + result.stderr)
        self.commit()  # fixture enters history only in this disposable repository
        oid = self.git('rev-parse', 'HEAD').decode().strip()
        result = subprocess.run([str(self.root / '.githooks/pre-push')], cwd=self.root,
                                input=f'refs/heads/main {oid} refs/heads/main {"0" * 40}\n'.encode(),
                                capture_output=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b'secret-or-binding-findings', result.stderr)
        self.assertNotIn(secret().encode(), result.stdout + result.stderr)

    def test_hooks_refuse_missing_or_mismatched_repo_python(self):
        shutil.copytree(ROOT / '.githooks', self.root / '.githooks')
        result = subprocess.run([str(self.root / '.githooks/pre-commit')], cwd=self.root, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b'repo-local-python-required', result.stderr)
        interpreter = self.root / '.venv/bin/python'
        interpreter.parent.mkdir(parents=True)
        interpreter.symlink_to(sys.executable)
        self.write('.python-version', '3.14.0')  # Deliberate mismatch fixture.
        result = subprocess.run([str(self.root / '.githooks/pre-commit')], cwd=self.root, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(b'project-python-pin-mismatch', result.stderr)

    def test_pre_push_requires_review_before_destination_network_lookup(self):
        args = ['check_publication.py', '--mode', 'pre-push', '--remote-url',
                'https://github.com/example/fictional.git']
        oid = self.git('rev-parse', 'HEAD').decode().strip()
        data = f'refs/heads/main {oid} refs/heads/main {"0" * 40}\n'
        with patch.object(gate, 'ROOT', self.root), patch.object(gate, 'check', return_value={}), \
             patch.object(gate, 'verify_private_destination') as destination, \
             patch.object(sys, 'argv', args), patch.object(sys, 'stdin', io.StringIO(data)), \
             patch.dict(os.environ, {'PPG_CONTENT_REVIEW': str(self.root / '.local/missing.json')}), \
             patch.object(sys, 'stderr', io.StringIO()) as errors:
            self.assertEqual(gate.main(), 1)
            destination.assert_not_called()
            self.assertIn('review-required', errors.getvalue())

    def test_destination_is_exact_and_private(self):
        self.assertEqual(gate.repository_from_url('git@github.com:example/fictional.git'),
                         'example/fictional')
        with self.assertRaisesRegex(gate.PublicationError, 'unsupported-publication'):
            gate.repository_from_url('https://example.invalid/example/fictional')
        for value in ({'nameWithOwner': 'example/fictional', 'isPrivate': False},
                      {'nameWithOwner': 'example/other', 'isPrivate': True}):
            result = subprocess.CompletedProcess([], 0, json.dumps(value), '')
            with patch.object(gate.shutil, 'which', return_value='gh'), \
                 patch.object(gate.subprocess, 'run', return_value=result):
                with self.assertRaisesRegex(gate.PublicationError, 'destination-not-private'):
                    gate.verify_private_destination('example/fictional')

    def test_publisher_pins_reviewed_commit_and_does_not_force(self):
        head = self.git('rev-parse', 'HEAD').decode().strip()
        receipt = self.review_receipt()
        calls = []
        def simulated(*args, **kwargs):
            calls.append((args, kwargs))
            if args[:2] == ('git', 'rev-parse'):
                return head
            if args[:2] == ('git', 'branch'):
                return 'main'
            if args == ('git', 'remote'):
                return 'origin'
            if args[:3] == ('git', 'remote', 'get-url'):
                return 'https://github.com/example/fictional.git'
            if args[:3] == ('gh', 'api', 'user'):
                return 'example'
            if args[:3] == ('gh', 'repo', 'view'):
                return json.dumps({'nameWithOwner': 'example/fictional', 'isPrivate': True})
            if args[:2] == ('git', 'ls-remote'):
                return head + '\trefs/heads/main'
            return ''
        args = ['publish_github.py', '--repo', 'example/fictional', '--resume',
                '--content-review', str(receipt)]
        with patch.object(publisher, 'ROOT', self.root), patch.object(publisher, 'run', simulated), \
             patch.object(publisher, 'check', return_value={}), \
             patch.object(publisher.shutil, 'which', return_value='gh'), \
             patch.object(sys, 'argv', args), patch.object(sys, 'stdout', io.StringIO()):
            self.assertEqual(publisher.main(), 0)
        pushes = [(a, k) for a, k in calls if a[:2] == ('git', 'push')]
        self.assertEqual(len(pushes), 1)
        self.assertEqual(pushes[0][0], ('git', 'push', 'origin', head + ':refs/heads/main'))
        self.assertEqual(pushes[0][1]['env']['PPG_CONTENT_REVIEW'], str(receipt.resolve()))

    def test_publisher_public_mode_propagates_reviewed_visibility_to_hook(self):
        head = self.git('rev-parse', 'HEAD').decode().strip()
        receipt = self.review_receipt(); value = json.loads(receipt.read_text())
        value['visibility'] = 'public'; receipt.write_text(json.dumps(value))
        calls = []
        def simulated(*args, **kwargs):
            calls.append((args, kwargs))
            if args[:2] == ('git', 'rev-parse'): return head
            if args[:2] == ('git', 'branch'): return 'main'
            if args == ('git', 'remote'): return 'origin'
            if args[:3] == ('git', 'remote', 'get-url'): return 'https://github.com/example/fictional.git'
            if args[:3] == ('gh', 'api', 'user'): return 'example'
            if args[:3] == ('gh', 'repo', 'view'):
                return json.dumps({'nameWithOwner': 'example/fictional', 'isPrivate': False})
            if args[:2] == ('git', 'ls-remote'): return head + '\trefs/heads/main'
            return ''
        args = ['publish_github.py', '--repo', 'example/fictional', '--resume',
                '--visibility', 'public', '--content-review', str(receipt)]
        with patch.object(publisher, 'ROOT', self.root), patch.object(publisher, 'run', simulated), \
             patch.object(publisher, 'check', return_value={}), \
             patch.object(publisher.shutil, 'which', return_value='gh'), \
             patch.object(sys, 'argv', args), patch.object(sys, 'stdout', io.StringIO()):
            self.assertEqual(publisher.main(), 0)
        pushes = [(a, k) for a, k in calls if a[:2] == ('git', 'push')]
        self.assertEqual(pushes[0][0], ('git', 'push', 'origin', head + ':refs/heads/main'))
        self.assertEqual(pushes[0][1]['env']['PPG_PUBLICATION_VISIBILITY'], 'public')

    def test_mismatched_or_multiple_push_urls_are_refused(self):
        for urls in ('https://github.com/other/unreviewed.git',
                     'https://github.com/example/fictional.git\nhttps://github.com/other/unreviewed.git', ''):
            with patch.object(publisher, 'run', return_value=urls):
                with self.assertRaisesRegex(ValueError, 'Push destination differs'):
                    publisher.verify_push_url('example/fictional')

    def test_metadata_chunks_and_blob_reads_are_bounded(self):
        for i in range(36):
            self.write(f'fixtures/item-{i}.txt', 'Fictional text only')
        self.git('add', 'fixtures')
        original = subprocess.run
        metadata_calls = []
        def bounded(args, **kwargs):
            if args[:3] == ['git', 'cat-file', '--batch-check']:
                self.assertNotIn('input', kwargs)
                self.assertNotIn('capture_output', kwargs)
                for stream in ('stdin', 'stdout', 'stderr'):
                    self.assertTrue(stat.S_ISREG(os.fstat(kwargs[stream].fileno()).st_mode))
                request = kwargs['stdin'].read()
                kwargs['stdin'].seek(0)
                self.assertLessEqual(len(request.splitlines()), 32)
                self.assertEqual(kwargs['timeout'], 30)
                metadata_calls.append(args)
            if args[:3] == ['git', 'cat-file', 'blob']:
                self.assertNotIn('input', kwargs)
                self.assertEqual(kwargs['timeout'], 30)
            return original(args, **kwargs)
        with patch.object(gate.subprocess, 'run', side_effect=bounded):
            gate.check(self.root, mode='staged')
        self.assertEqual(len(metadata_calls), 2)

    def test_oversize_blob_is_refused_before_content_materialisation(self):
        self.write('large.txt', 'fictional oversized input')
        self.git('add', 'large.txt')
        with patch.object(gate, 'MAX_BLOB', 4):
            self.assert_refused('oversize-blob', mode='staged')

    def test_publisher_refuses_findings_before_any_github_call(self):
        def local_only(*args, **kwargs):
            if args[:2] == ('git', 'branch'):
                return 'main'
            if args[:2] == ('git', 'status'):
                return ''
            if args[0] == 'gh':
                self.fail('GitHub must not be called')
            return ''
        with patch.object(publisher, 'ROOT', self.root), patch.object(publisher, 'run', local_only), \
             patch.object(publisher, 'check', side_effect=gate.PublicationError('gitleaks-missing')), \
             patch.object(sys, 'argv', ['publish_github.py', '--dry-run']):
            with self.assertRaisesRegex(gate.PublicationError, 'gitleaks-missing'):
                publisher.main()

    def test_publisher_requires_review_before_any_github_call(self):
        def local_only(*args, **kwargs):
            if args[:2] == ('git', 'branch'):
                return 'main'
            if args[0] == 'gh':
                self.fail('GitHub must not be called')
            return ''
        with patch.object(publisher, 'ROOT', self.root), patch.object(publisher, 'run', local_only), \
             patch.object(publisher, 'check', return_value={}), \
             patch.object(sys, 'argv', ['publish_github.py']):
            with self.assertRaisesRegex(gate.PublicationError, 'review-required'):
                publisher.main()


if __name__ == '__main__':
    unittest.main()
