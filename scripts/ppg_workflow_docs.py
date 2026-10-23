#!/usr/bin/env python3
"""Validate and build the maintained workflow register and operator guide."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / 'docs/workflows/v1.0.0'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def release_directory(root, version):
    import re
    if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', version):
        raise ValueError('Use a numeric major.minor.patch release')
    return root / ('docs/workflows/v'+version)


def documented_workflows(register):
    return register['workflows'] + register.get('manualWorkflows', [])


def load_register(root=ROOT, version='1.0.0'):
    release = release_directory(root, version)
    register = json.loads((release / 'register.json').read_text())
    if register['release'] != version:
        raise ValueError('Release path and register version differ')
    manifest = json.loads((root / 'config/workspace-manifest.json').read_text())
    rows = register['workflows']
    ids = [row['id'] for row in rows]
    if len(ids) != len(set(ids)) or set(ids) != {c['key'] for c in manifest['capabilities']}:
        raise ValueError('Register must cover each current capability exactly once')
    documented = documented_workflows(register)
    import re
    all_ids = [row['id'] for row in documented]
    if len(all_ids) != len(set(all_ids)) or any(not re.fullmatch(r'[a-z0-9-]+', key) for key in all_ids):
        raise ValueError('Duplicate or unsafe documented workflow identity')
    for row in documented + register['lifecycleOperations'] + register['conditional']:
        ref = Path(row['instructions'])
        if ref.is_absolute() or '..' in ref.parts or not (root / ref).is_file():
            raise ValueError('Missing or unsafe workflow instruction reference')
    for row in documented:
        if row['version'] != register['release'] or not row['steps'] or not row['hold']:
            raise ValueError('Missing version, steps or failure/recovery path')
        if row['deployedDefinitionSHA256'] is not None:
            raise ValueError('Native deployment hashes require separate owner qualification')
        if row['diagram'] != f"docs/workflows/v{version}/{row['id']}.mmd":
            raise ValueError('Unexpected diagram reference')
    return register


def diagram(row):
    def label(value):
        return value.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    lines = ['flowchart TD', f'  start["{label(row["trigger"])}"]']
    prior = 'start'
    for i, step in enumerate(row['steps']):
        lines.append(f'  {prior} --> n{i}["{label(step)}"]')
        prior = f'n{i}'
    lines.extend([f'  {prior} --> output["{label(row["output"])}"]',
                  '  start -. "Missing, stale or conflicting evidence" .-> hold["Hold affected operation; preserve evidence; reconcile before retry"]'])
    if row['id'] == 'policy-lifecycle':
        lines.extend(['  n7 -. "Separate evidenced branch" .-> edition["Record replacement or withdrawal evidence; preserve issued history"]',
                      '  edition -. "Requires its own qualification; not proven by connected positive cycle" .-> hold'])
    return '\n'.join(lines)+'\n'


def dot_source(row):
    # The same ordered steps as the editable Mermaid; PNG is a reading aid.
    nodes = [('start', row['trigger'])] + [(f'n{i}', step) for i, step in enumerate(row['steps'])] + [('output', row['output'])]
    lines=['digraph workflow {','graph [rankdir=TB,bgcolor="white",pad="0.18",dpi=110];',
           'node [shape=box,style="rounded,filled",fillcolor="#eaf3fa",fontname="Arial",fontsize=11,margin="0.13,0.09"];',
           'edge [color="#45637d"];']
    for key, value in nodes:
        # Wrap prose without requiring a plotting runtime.
        import textwrap
        text='\n'.join(textwrap.wrap(value, 43))
        lines.append(f'{key} [label={json.dumps(text)}];')
    for (left,_),(right,_) in zip(nodes,nodes[1:]): lines.append(f'{left} -> {right};')
    lines += ['hold [label="Missing / stale / conflicting evidence\\nHold; preserve; reconcile before retry",fillcolor="#fff1d6"];',
              'start -> hold [style=dashed];']
    if row['id']=='policy-lifecycle':
        lines += ['edition [label="Separate replacement / withdrawal evidence\\nNot established by positive cycle",fillcolor="#fff1d6"];','n7 -> edition [style=dashed];','edition -> hold [style=dashed];']
    return '\n'.join(lines+['}'])


def page_tokens(value, origin):
    """Compare native HTML allowing same-origin relative URLs and void-tag syntax."""
    from html.parser import HTMLParser
    from urllib.parse import urljoin
    class Tokens(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.tokens=[]
        def handle_starttag(self, tag, attrs):
            normalized=[(key, urljoin(origin, item) if key in {'href','src'} and item else item) for key,item in attrs]
            self.tokens.append(('start',tag,tuple(sorted(normalized))))
        def handle_startendtag(self, tag, attrs):
            self.handle_starttag(tag,attrs)
            if tag not in {'img','br','hr','input','meta','link'}: self.handle_endtag(tag)
        def handle_endtag(self, tag):
            self.tokens.append(('end',tag))
        def handle_data(self, data):
            if data.strip(): self.tokens.append(('text',data))
        def handle_comment(self, data):
            self.tokens.append(('comment',data))
    parser=Tokens();parser.feed(value);parser.close()
    return parser.tokens


def build(root=ROOT, render=False, version='1.0.0'):
    register=load_register(root, version)
    release=release_directory(root,version)
    if (release/'release.json').exists():
        raise ValueError('Frozen release already exists; use --check or prepare a new version')
    baseline = register.get('currentBaseline', 'Current baseline: the connected fictional cycle reached closure and created a separate next review; exact replay created no duplicate case/request. This supersedes earlier positive-closure/next-review-unqualified statements only for that connected example. Replacement/withdrawal, production automation, and real policy authority require their own evidence.')
    limits = register.get('qualificationLimitations', 'Ordinary-user access and a second configuration remain unqualified.')
    md=['# PPG workflow operator guide', '', f'Version {register["release"]} — baseline {register["asOf"]}.', '',
        'Use the existing PPG workspace; no meeting or new channel is required. This guide describes available routes and their limits. It does not grant access, assign responsibility, issue policies or enable stopped pilots.', '',
        '## Start with the completed fictional example', '',
        'Open **PPG — Start Here → Completed fictional PPG walkthrough**. Inspect the closed review, its edited draft and case-filtered evidence, then the separate next review. Preserve these examples. Use fresh fictional references for another run and confirm current operation bindings with the lifecycle owner.', '',
        '## Versions and evidence', '',
        'This guide and register share release '+version+'. Git records source/document changes; the native page and downloaded files have separate SharePoint revisions. Local source hashes identify a snapshot, not the currently deployed flow. Deployed-definition evidence varies by workflow; consult its qualification and owner-scoped native receipts. Private runtime receipts retain exact tenant bindings and qualification evidence. '+limits, '',
        baseline, '',
        '## Workflow register', '', '| Workflow | Route | Qualification |', '|---|---|---|']
    escape=html.escape
    blocks=['<h2>PPG workflow operator guide — v'+version+'</h2>',
            '<p>Baseline: '+escape(register['asOf'])+'. Use the existing PPG workspace; no meeting or new channel is needed. Documentation does not grant access, assign responsibility, issue a policy or enable a stopped pilot.</p>',
            '<h3>Start with the completed fictional example</h3><p>Return to <a href="{{hub}}">PPG — Start Here</a> and choose Completed fictional PPG walkthrough. Inspect the closed review, edited draft and filtered evidence; then open the separate next review. Preserve those examples.</p>',
            '<h3>What is current</h3><p>'+escape(baseline)+' '+escape(limits)+'</p>',
            '<h3>Version and recovery</h3><p>Guide/register release '+version+'. SharePoint file/page revisions are separate from Git and deployed flow revisions. Consult each workflow qualification for its deployed-definition evidence; this guide does not establish the current state of other flows. Do not replace inputs or overwrite human edits on failure: preserve the operation reference and evidence, then reconcile through the owning route.</p>',
            '<p><a href="{{register}}">Download versioned workflow register</a> · <a href="{{guide}}">Download operator guide</a> · <a href="{{snapshot}}">Download release checksums</a></p>']
    for row in documented_workflows(register):
        md.append(f'| [{row["title"]}](#{row["id"]}) | {row["mode"]} | {row["qualification"]} |')
    for row in documented_workflows(register):
        (release/(row['id']+'.mmd')).write_text(diagram(row))
        if render:
            subprocess.run(['dot','-Tpng','-o',str(release/(row['id']+'.png'))],input=dot_source(row).encode(),check=True,capture_output=True)
        if not (release/(row['id']+'.png')).is_file():
            raise ValueError('Missing diagram image; build new release with --render')
        md += ['', f'<a id="{row["id"]}"></a>',f'## {row["title"]}', '',
               f'**Route:** {row["mode"]}. **Maintainer:** {row["owner"]}.', '',
               f'**Trigger:** {row["trigger"]}. **Inputs:** {row["inputs"]}.', '']
        md += [f'{i}. {step}.' for i,step in enumerate(row['steps'],1)]
        md += ['',f'**Output:** {row["output"]}.', '',f'**Hold/recovery:** {row["hold"]}', '',
               f'**Evidence:** {row["qualification"]}.', '',f'[Detailed instructions](../../../{row["instructions"]}) · [Editable diagram]({row["id"]}.mmd)', '',
               f'![{row["title"]} workflow]({row["id"]}.png)']
        blocks += [f'<h3>{escape(row["title"])}</h3>',f'<p><strong>Route:</strong> {escape(row["mode"])}. <strong>Maintainer:</strong> {escape(row["owner"])}.</p>',
                   f'<p><strong>Trigger:</strong> {escape(row["trigger"])}. <strong>Inputs:</strong> {escape(row["inputs"])}.</p>',
                   '<ol>'+''.join('<li>'+escape(step)+'</li>' for step in row['steps'])+'</ol>',
                   f'<p><strong>Output:</strong> {escape(row["output"])}. <strong>Evidence:</strong> {escape(row["qualification"])}.</p>',
                   f'<p><strong>Hold/recovery:</strong> {escape(row["hold"])}</p>',
                   '<p><img src="{{image:'+row['id']+'}}" alt="'+escape(row['title'])+' workflow diagram" /></p>']
    md += ['','## Lifecycle operation references','', '| Operation | Purpose and instructions |','|---|---|']
    for row in register['lifecycleOperations']:
        md.append(f'| {row["id"]} | [{row["purpose"]}](../../../{row["instructions"]}) |')
    md += ['','## Conditional capabilities','']
    blocks += ['<h3>Conditional capabilities</h3>']
    for row in register['conditional']:
        md += [f'- **{row["id"]}:** {row["status"]}. [Evidence](../../../{row["instructions"]}).']
        blocks += [f'<p><strong>{escape(row["id"])}:</strong> {escape(row["status"])}.</p>']
    md += ['','For historical qualification precedence and release maintenance, see [documentation baseline](../../workflow-documentation.md).','']
    (release/'operator-guide.md').write_text('\n'.join(md))
    (release/'operator-guide.html').write_text('\n'.join(blocks)+'\n')
    import re
    download = re.sub(r'\[([^\]]+)\]\(\.\./[^)]+\)', r'\1 (repository reference)', '\n'.join(md))
    (release/'operator-guide-download.md').write_text(download.rstrip()+'\n')
    paths=[release/'register.json',release/'operator-guide.md',release/'operator-guide.html',release/'operator-guide-download.md']
    paths += sorted(release.glob('*.mmd')) + sorted(release.glob('*.png'))
    paths += [root/row['instructions'] for row in documented_workflows(register)+register['lifecycleOperations']+register['conditional']]
    paths += [root/'docs/workflow-documentation.md',root/'config/workspace-manifest.json']
    snapshot={'release':register['release'],'baselineDate':register['asOf'],'snapshotScope':'Local documentation/diagram/instruction bytes; not deployed flow definitions or operational data',
              'files':{p.relative_to(root).as_posix():sha(p) for p in sorted(set(paths))},'nativeDeploymentVerified':False}
    (release/'release.json').write_text(json.dumps(snapshot,indent=2)+'\n')
    return register


def check_release(root=ROOT, version='1.0.0'):
    register=load_register(root,version)
    snapshot=json.loads((release_directory(root,version)/'release.json').read_text())
    drift=[]
    for name, expected in snapshot['files'].items():
        path=Path(name)
        if path.is_absolute() or '..' in path.parts or not (root/path).resolve().is_relative_to(root.resolve()):
            raise ValueError('Unsafe release snapshot reference')
        actual=sha(root/path) if (root/path).is_file() else None
        if actual!=expected:
            if name.startswith('docs/workflows/v'+version+'/') and name.endswith('.png') and actual is None:
                continue  # Native reading aids are generated, never committed as binary.
            if name.startswith('docs/workflows/v'+version+'/'):
                raise ValueError('Immutable release snapshot drift: '+name)
            drift.append(name)
    return register,drift


def render_images(root=ROOT, version='1.0.0'):
    register, _ = check_release(root,version)
    release=release_directory(root,version)
    snapshot=json.loads((release/'release.json').read_text())
    for row in documented_workflows(register):
        target=release/(row['id']+'.png')
        expected=snapshot['files'][target.relative_to(root).as_posix()]
        if target.exists():
            if sha(target)!=expected: raise ValueError('Existing reading aid differs; preserve it')
            continue
        result=subprocess.run(['dot','-Tpng'],input=dot_source(row).encode(),check=True,capture_output=True)
        if hashlib.sha256(result.stdout).hexdigest()!=expected:
            raise ValueError('Renderer bytes differ from published baseline; use native download or a new release')
        with target.open('xb') as stream: stream.write(result.stdout)
    return register


def reading_aid_pending(root, target):
    """Recognise only registered generated images whose text diagram is intact."""
    import re
    try:
        path=target.resolve().relative_to(root.resolve()).as_posix()
        match=re.fullmatch(r'docs/workflows/v([0-9]+\.[0-9]+\.[0-9]+)/([a-z0-9-]+)\.png',path)
        if not match: return False
        release=release_directory(root,match[1])
        snapshot=json.loads((release/'release.json').read_text())['files']
        source=target.with_suffix('.mmd')
        source_name=source.relative_to(root).as_posix()
        return (bool(re.fullmatch('[0-9a-f]{64}',snapshot[path]))
                and source.is_file() and sha(source)==snapshot[source_name])
    except (ValueError,KeyError,TypeError,OSError):
        return False


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--release',default='1.0.0',help='Maintained register version, e.g. 1.0.1')
    p.add_argument('--render',action='store_true',help='Render static PNG reading aids using installed Graphviz')
    p.add_argument('--render-images',action='store_true',help='Materialise missing untracked reading aids against frozen hashes; never overwrite')
    p.add_argument('--check',action='store_true',help='Verify frozen release checksums without modifying files')
    args=p.parse_args()
    if args.render_images:
        register=render_images(version=args.release)
        _,drift=check_release(version=args.release)
    elif args.check:
        register,drift=check_release(version=args.release)
    else:
        register=build(render=args.render,version=args.release)
        drift=[]
    print(json.dumps({'release':register['release'],'workflows':len(register['workflows']), 'manualWorkflows':len(register.get('manualWorkflows', [])), 'lifecycleOperations':len(register['lifecycleOperations']),'referencedInstructionDrift':len(drift),'unmaterialisedReadingAids':sum(not (release_directory(ROOT,args.release)/(row['id']+'.png')).exists() for row in documented_workflows(register)),'nativeDeploymentVerified':False}))



if __name__=='__main__': main()
