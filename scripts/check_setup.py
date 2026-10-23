#!/usr/bin/env python3
"""Small, offline repository checks; does not claim tenant/clinical validation."""
from __future__ import annotations
import argparse
import configparser
import csv
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def git(*args: str) -> str:
    result = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True, check=True)
    return result.stdout.strip()

def dependency_metadata(conductor: Path, active: dict) -> dict:
    """Archived tracks remain dependencies; archival never changes acceptance."""
    combined = dict(active)
    for path in sorted((conductor / 'archive').glob('*/metadata.json')):
        value = json.loads(path.read_text())
        identity = path.parent.name
        if value.get('track_id') != identity or identity in combined:
            raise ValueError('ambiguous-or-invalid-archived-track-identity')
        combined[identity] = value
    return combined


def check(require_submodule: bool = False) -> tuple[list[str], list[str], list[str]]:
    passed: list[str] = []
    failed: list[str] = []
    pending: list[str] = []
    def record(label: str, condition: bool) -> None:
        (passed if condition else failed).append(label)
    required = ['AGENTS.md', 'README.md', 'CLAUDE.md', 'GEMINI.md', '.python-version',
        '.github/copilot-instructions.md', '.agents/skills/ppg-deliver/SKILL.md',
        'conductor/index.md', 'conductor/product.md', 'conductor/product-guidelines.md',
        'conductor/tech-stack.md', 'conductor/workflow.md', 'conductor/tracks.md',
        'conductor/handoff.md', 'conductor/decisions.md', 'conductor/execution-queue.md',
        'conductor/code_styleguides/general.md', 'conductor/conductor.lock.json',
        'conductor/setup-receipt.json', 'docs/roadmap.md', 'docs/source-manifest.json',
        'docs/operating-context.md', 'docs/source-ingestion.md', 'docs/tooling.md',
        'config/deployment.example.json', 'config/mvp-layout.json',
        'config/source-field-map.csv', 'templates/review-package.md',
        'templates/operation-receipt.json', 'scripts/bootstrap_conductor.py',
        'scripts/publish_github.py', '.gitmodules', '.gitignore']
    for name in required:
        record('file: '+name, (ROOT/name).is_file() and (ROOT/name).stat().st_size > 0)
    if failed:
        return passed, failed, pending
    python_pin = (ROOT/'.python-version').read_text().strip()
    record('project Python 3.15 patch pin', bool(re.fullmatch(r'3\.15\.\d+', python_pin)))
    record('actual Python matches project pin', '.'.join(map(str, sys.version_info[:3])) == python_pin and sys.version_info.releaselevel == 'final')
    record('repo-local Python environment', Path(sys.prefix).resolve() == (ROOT/'.venv').resolve())
    adapters = [(ROOT/n).read_text() for n in ['CLAUDE.md', 'GEMINI.md', '.github/copilot-instructions.md']]
    record('agent entry points use one instruction contract', len(set(adapters)) == 1)
    tracked = [n for n in git('ls-files').splitlines() if not n.startswith('.agents/plugins/conductor/')]
    json_files = [n for n in tracked if n.endswith('.json')]
    for name in json_files:
        try:
            json.loads((ROOT/name).read_text(encoding='utf-8'))
            record('JSON: '+name, True)
        except (ValueError, OSError):
            record('JSON: '+name, False)
    from ppg_workflow_docs import reading_aid_pending
    pending_images: set[str] = set()
    # Relative links are checked, not arbitrary inline paths or template variables.
    for name in tracked:
        if not name.endswith('.md'):
            continue
        text = (ROOT/name).read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            linked = (ROOT/name).parent/target
            if not linked.exists() and reading_aid_pending(ROOT, linked):
                pending_images.add(linked.resolve().relative_to(ROOT).as_posix())
            else:
                record(f'link: {name} -> {target}', linked.exists())
    if pending_images:
        pending.append(f'{len(pending_images)} generated workflow reading aids not materialised; native copies are separate, run ppg_workflow_docs.py --render-images for local copies')
    directories = sorted(p for p in (ROOT/'conductor/tracks').iterdir() if p.is_dir())
    registry = (ROOT/'conductor/tracks.md').read_text()
    metadata = {d.name: json.loads((d/'metadata.json').read_text())
                for d in directories if (d/'metadata.json').is_file()}
    dependencies_by_id = dependency_metadata(ROOT/'conductor', metadata)
    record('exactly four quick-win tracks',
           sum(bool(m.get('quick_win')) for m in metadata.values()) == 4)
    found = set()
    for directory in directories:
        for leaf in ['index.md','spec.md','plan.md','metadata.json']:
            record(f'track file: {directory.name}/{leaf}', (directory/leaf).is_file())
        if not (directory/'metadata.json').is_file() or not (directory/'plan.md').is_file():
            continue
        meta = json.loads((directory/'metadata.json').read_text())
        if meta.get('quick_win'):
            found.add(meta['quick_win'])
        record('track identity: '+directory.name, meta.get('track_id') == directory.name)
        record('registry entry: '+directory.name, './tracks/'+directory.name+'/' in registry)
        record('track status: '+directory.name, meta.get('status') in ['new','in_progress','completed','cancelled'])
        tasks = re.findall(r'^- \[([ ~x])\] ', (directory/'plan.md').read_text(), re.M)
        record('bounded task plan: '+directory.name, 1 <= len(tasks) <= 8)
        record('completion matches tasks: '+directory.name,
               meta.get('status') != 'completed' or all(t == 'x' for t in tasks))
        dependencies = meta.get('dependencies', [])
        record('known dependencies: '+directory.name,
               all(d in dependencies_by_id and d != directory.name for d in dependencies))
        if not meta.get('quick_win'):
            record('follow-on phase: '+directory.name, meta.get('phase') == 'follow_on')
            record('follow-on eligibility: '+directory.name,
                   meta.get('execution_eligibility') in ['ready', 'queued', 'eligibility_required'])
            record('follow-on next action: '+directory.name, bool(meta.get('next_action')))
            if meta.get('execution_eligibility') == 'ready':
                record('ready dependencies complete: '+directory.name,
                       all(dependencies_by_id.get(d, {}).get('status') == 'completed' for d in dependencies))
        if meta.get('quick_win') == 'QW2':
            record('QW2 not blocked by source automation', not any('qw3' in d.lower() for d in meta.get('dependencies',[])))
    record('quick-win set QW1–QW4', found == {'QW1','QW2','QW3','QW4'})
    def acyclic(track: str, trail: frozenset[str]) -> bool:
        if track in trail:
            return False
        return all(acyclic(d, trail | {track})
                   for d in dependencies_by_id.get(track, {}).get('dependencies', []) if d in dependencies_by_id)
    record('track dependencies are acyclic', all(acyclic(t, frozenset()) for t in metadata))
    record('roadmap has no implementation checklists', not re.search(r'^\s*- \[[ ~x]\]', (ROOT/'docs/roadmap.md').read_text(), re.M))
    with (ROOT/'config/source-field-map.csv').open(newline='',encoding='utf-8') as stream:
        rows=list(csv.DictReader(stream))
    record('all 25 ordered source mappings retained', [int(r['source_column']) for r in rows] == list(range(1,26)))
    audits=[r['mirror_field'] for r in rows if r['source_header']=='Audit Approach']
    record('both Audit Approach fields remain separate', audits == ['sourceAuditApproach1','sourceAuditApproach2'])
    record('core context remains bounded', sum(len((ROOT/n).read_text().split()) for n in required
        if n.startswith('conductor/') and n.endswith('.md')
        and n != 'conductor/execution-queue.md') < 3000)
    lock=json.loads((ROOT/'conductor/conductor.lock.json').read_text())
    subpath=lock['submodule_path']
    pin=lock['commit']
    modules=configparser.ConfigParser()
    modules.read(ROOT/'.gitmodules')
    record('upstream URL matches lock', modules.get(f'submodule "{subpath}"','url',fallback='') == lock['repository'])
    record('commit is a full SHA-1 pin', bool(re.fullmatch(r'[0-9a-f]{40}',pin)))
    entry=git('ls-files','--stage','--',subpath)
    record('genuine Git 160000 submodule pin', entry.split()[:2] == ['160000',pin])
    record('automatic tool updates disabled', lock.get('auto_update') is False)
    sub=ROOT/subpath
    if (sub/'.git').exists():
        head=subprocess.run(['git','-C',str(sub),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
        record('hydrated submodule HEAD matches pin',head == pin)
        manifest=json.loads((sub/'gemini-extension.json').read_text())
        record('hydrated tool manifest matches release',manifest.get('name')=='conductor' and manifest.get('version')=='0.4.1')
    else:
        message='Conductor gitlink verified; upstream checkout not materialised (run bootstrap on connected machine)'
        (failed if require_submodule else pending).append(message)
    forbidden_suffixes={'.xls','.xlsx','.xlsb','.xlsm','.msg','.eml','.pdf','.docx','.zip','.bundle','.pem','.pfx','.key'}
    record('no operational binary/source exports tracked',not any(Path(n).suffix.lower() in forbidden_suffixes or n.startswith(('.local/','private/','outputs/','receipts/')) for n in tracked))
    for key in ['source','destination']:
        binding=json.loads((ROOT/'config/deployment.example.json').read_text())[key]
        record('example binding unbound: '+key,all(v is None for v in binding.values()))
    secrets=re.compile(r'gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{25,}|https://healthqld\.sharepoint\.com', re.I)
    record('tracked project text contains no known token/tenant URL patterns',not any(secrets.search((ROOT/n).read_text(encoding='utf-8')) for n in tracked if (ROOT/n).is_file() and n != 'scripts/check_setup.py'))
    return passed,failed,pending

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-submodule',action='store_true',help='Fail until the pinned upstream checkout is present.')
    parser.add_argument('--json',action='store_true',help='Print a machine-readable report.')
    args=parser.parse_args()
    try:
        passed,failed,pending=check(args.require_submodule)
    except (OSError,ValueError,KeyError,subprocess.CalledProcessError) as exc:
        print('Setup check could not complete: '+str(exc),file=sys.stderr)
        return 2
    result={'scope':'local repository/context only','passed':len(passed),'failed':failed,'pending':pending,'checks':passed,'tenant_or_clinical_validation':False}
    if args.json:
        print(json.dumps(result,indent=2))
    else:
        print(f'{len(passed)} checks passed; {len(failed)} failed; {len(pending)} pending.')
        for label in failed: print('FAIL: '+label)
        for label in pending: print('PENDING: '+label)
        print('No Microsoft runtime or clinical-validation claim.')
    return 1 if failed else 0
if __name__=='__main__':
    raise SystemExit(main())
