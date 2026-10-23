import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from ppg_workflow_docs import ROOT, load_register, diagram, page_tokens, check_release, build, release_directory, reading_aid_pending, documented_workflows


class WorkflowDocumentationTests(unittest.TestCase):
    def test_successor_baseline_replaces_stale_default_and_escapes_html(self):
        register=load_register()
        register.update(currentBaseline='Fictional second configuration <qualified>',
                        qualificationLimitations='Ordinary-user execution deferred & unverified')
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);release=root/'docs/workflows/v1.0.0'
            release.mkdir(parents=True);(root/'config').mkdir()
            (root/'config/workspace-manifest.json').write_bytes((ROOT/'config/workspace-manifest.json').read_bytes())
            for row in documented_workflows(register)+register['lifecycleOperations']+register['conditional']:
                p=root/row['instructions'];p.parent.mkdir(parents=True,exist_ok=True);p.write_text('Fictional instructions')
            (root/'docs/workflow-documentation.md').write_text('Fictional baseline')
            for row in documented_workflows(register):
                (release/(row['id']+'.png')).write_bytes(b'fictional reading-aid fixture')
            (release/'register.json').write_text(json.dumps(register))
            build(root)
            page=(release/'operator-guide.html').read_text()
            self.assertIn('second configuration &lt;qualified&gt;',page)
            self.assertIn('deferred &amp; unverified',page)
            self.assertNotIn('second configuration remain unqualified',page)

    def test_complete_coverage_and_real_instruction_refs(self):
        register=load_register()
        self.assertEqual(len(register['workflows']),27)
        self.assertEqual(len(register['lifecycleOperations']),12)
        self.assertTrue(all(row['deployedDefinitionSHA256'] is None for row in register['workflows']))

    def test_missing_duplicate_or_invented_capability_refused(self):
        register=load_register()
        for kind in ('missing','duplicate','invented'):
            with tempfile.TemporaryDirectory() as directory:
                root=Path(directory);(root/'docs/workflows/v1.0.0').mkdir(parents=True);(root/'config').mkdir()
                current=copy.deepcopy(register)
                if kind=='missing': current['workflows'].pop()
                elif kind=='duplicate': current['workflows'].append(current['workflows'][0])
                else: current['workflows'][0]['id']='invented'
                (root/'docs/workflows/v1.0.0/register.json').write_text(json.dumps(current))
                (root/'config/workspace-manifest.json').write_bytes((ROOT/'config/workspace-manifest.json').read_bytes())
                with self.assertRaisesRegex(ValueError,'exactly once'): load_register(root)

    def test_manual_workflow_does_not_change_capability_coverage_or_allow_unsafe_ids(self):
        register=load_register()
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'docs/workflows/v1.0.0').mkdir(parents=True);(root/'config').mkdir()
            (root/'config/workspace-manifest.json').write_bytes((ROOT/'config/workspace-manifest.json').read_bytes())
            for row in register['workflows']+register['lifecycleOperations']+register['conditional']:
                target=root/row['instructions'];target.parent.mkdir(parents=True,exist_ok=True);target.write_text('Fictional instructions')
            manual=copy.deepcopy(register['workflows'][0]);manual.update(id='manual-transfer',diagram='docs/workflows/v1.0.0/manual-transfer.mmd')
            register['manualWorkflows']=[manual];path=root/'docs/workflows/v1.0.0/register.json'
            path.write_text(json.dumps(register));loaded=load_register(root)
            self.assertEqual(len(loaded['workflows']),27);self.assertEqual(len(documented_workflows(loaded)),28)
            for bad in ['workspace','../outside']:
                manual['id']=bad;path.write_text(json.dumps(register))
                with self.assertRaisesRegex(ValueError,'Duplicate or unsafe'):load_register(root)

    def test_ordered_steps_and_hold_branch_match_diagrams(self):
        for row in load_register()['workflows']:
            content=diagram(row)
            self.assertEqual((ROOT/row['diagram']).read_text(),content)
            for step in row['steps']: self.assertIn(step.replace('&','&amp;'),content)
            self.assertIn('reconcile before retry',content)

    def test_native_html_normalization_does_not_hide_target_or_text_changes(self):
        origin='https://example.invalid'
        original='<p><a href="https://example.invalid/guide">Guide</a><img src="/diagram.png" alt="Diagram" /></p>\n'
        native='<p><a href="/guide">Guide</a><img src="https://example.invalid/diagram.png" alt="Diagram"></p>'
        self.assertEqual(page_tokens(original,origin),page_tokens(native,origin))
        self.assertNotEqual(page_tokens(original,origin),page_tokens(native.replace('/guide','/wrong'),origin))
        self.assertNotEqual(page_tokens(original,origin),page_tokens(native.replace('>Guide<','>Changed<'),origin))

    def test_frozen_release_cannot_be_rebuilt_and_version_is_safe(self):
        with self.assertRaisesRegex(ValueError,'Frozen release'): build()
        with self.assertRaises(ValueError): release_directory(ROOT,'../../private')

    def test_immutable_corruption_refused_external_drift_reported(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            shutil.copytree(ROOT/'docs/workflows/v1.0.0',root/'docs/workflows/v1.0.0')
            (root/'config').mkdir()
            shutil.copy(ROOT/'config/workspace-manifest.json',root/'config/workspace-manifest.json')
            for row in load_register()['workflows']+load_register()['lifecycleOperations']+load_register()['conditional']:
                target=root/row['instructions']; target.parent.mkdir(parents=True,exist_ok=True); target.write_text('changed live instructions')
            register,drift=check_release(root)
            self.assertTrue(drift)
            (root/'docs/workflows/v1.0.0/workspace.mmd').write_text('corrupted release')
            with self.assertRaisesRegex(ValueError,'Immutable release'): check_release(root)

    def test_missing_binary_reading_aids_do_not_hide_missing_text_sources(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            shutil.copytree(ROOT/'docs/workflows/v1.0.0',root/'docs/workflows/v1.0.0',ignore=shutil.ignore_patterns('*.png'))
            (root/'config').mkdir()
            shutil.copy(ROOT/'config/workspace-manifest.json',root/'config/workspace-manifest.json')
            for row in load_register()['workflows']+load_register()['lifecycleOperations']+load_register()['conditional']:
                target=root/row['instructions']; target.parent.mkdir(parents=True,exist_ok=True); target.write_text('live instructions')
            check_release(root)
            (root/'docs/workflows/v1.0.0/workspace.mmd').unlink()
            with self.assertRaisesRegex(ValueError,'Immutable release'): check_release(root)

    def test_pending_reading_aid_requires_intact_registered_text_diagram(self):
        import shutil
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            shutil.copytree(ROOT/'docs/workflows/v1.0.0',root/'docs/workflows/v1.0.0',ignore=shutil.ignore_patterns('*.png'))
            target=root/'docs/workflows/v1.0.0/workspace.png'
            self.assertTrue(reading_aid_pending(root,target))
            self.assertFalse(reading_aid_pending(root,target.with_name('unknown.png')))
            target.with_suffix('.mmd').write_text('changed source')
            self.assertFalse(reading_aid_pending(root,target))
            self.assertFalse(reading_aid_pending(root,root/'outside.png'))

    def test_release_bytes_match_and_native_claims_absent(self):
        import hashlib
        release=ROOT/'docs/workflows/v1.0.0'
        snapshot=json.loads((release/'release.json').read_text())
        self.assertFalse(snapshot['nativeDeploymentVerified'])
        for name,expected in snapshot['files'].items():
            if name.startswith('docs/workflows/v1.0.0/') and (ROOT/name).exists():
                self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),expected,name)
            self.assertEqual(len(expected),64)
        check_release()
        html=(release/'operator-guide.html').read_text()
        self.assertEqual(html.count('{{image:'),27)
        self.assertIn('Ordinary-user access',html)
        download=(release/'operator-guide-download.md').read_text()
        self.assertNotIn('](../',download)

if __name__=='__main__': unittest.main()
