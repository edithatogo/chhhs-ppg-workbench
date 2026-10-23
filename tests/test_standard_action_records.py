import copy
import hashlib
import json
from pathlib import Path
import unittest
from scripts.ppg_standard_action_records import records


class ActionRecords(unittest.TestCase):
    def setUp(self):
        self.frameworks = json.loads(Path('config/review-intelligence/frameworks-v1.json').read_text())
        self.supplement = json.loads(Path('config/review-intelligence/nsqhs2-standard6-actions-v1.json').read_text())
        self.raw = b'fictional source for offline contract test'
        self.supplement['sourceSha256'] = hashlib.sha256(self.raw).hexdigest()

    def test_actions_have_edition_parent_and_non_normative_source(self):
        r = records(self.frameworks, self.supplement, self.raw)
        self.assertEqual(len(r), 11)
        self.assertEqual(r[-1]['record']['RequirementCode'], '6.11')
        self.assertTrue(all(x['record']['ParentRequirementKey']=='nsqhs-2-2021-6' for x in r))
        self.assertTrue(all('Non-normative' in x['record']['RequirementText'] for x in r))

    def test_refuses_changed_source_duplicate_and_other_edition_parent(self):
        with self.assertRaises(ValueError): records(self.frameworks,self.supplement,b'changed')
        for change in ['duplicate', 'parent']:
            s=copy.deepcopy(self.supplement)
            if change=='duplicate': s['requirements'].append(s['requirements'][0])
            else: s['requirements'][0]['parentRequirementId']='nsqhs-3-draft-1'
            with self.assertRaises(ValueError): records(self.frameworks,s,self.raw)

    def test_clinical_governance_index_is_complete_and_separate_from_standard_six(self):
        s=json.loads(Path('config/review-intelligence/nsqhs2-standard1-actions-v1.json').read_text())
        s['sourceSha256']=hashlib.sha256(self.raw).hexdigest()
        rows=records(self.frameworks,s,self.raw)
        self.assertEqual([r['record']['RequirementCode'] for r in rows],
                         [f'1.{n:02d}' for n in range(1,34)])
        self.assertTrue(all(r['record']['ParentRequirementKey']=='nsqhs-2-2021-1' for r in rows))
        self.assertTrue(all(10<=r['pdfPage']<=16 and r['printedPage']==r['pdfPage']-4
                            for r in s['requirements']))
        six=records(self.frameworks,self.supplement,self.raw)
        self.assertFalse({r['record']['RequirementKey'] for r in rows}&
                         {r['record']['RequirementKey'] for r in six})

    def test_available_indexes_are_complete_with_no_cross_supplement_key_collision(self):
        keys=set()
        for standard,count in [(1,33),(2,14),(3,19),(4,15),(5,36),(6,11),(7,10),(8,13)]:
            s=json.loads(Path(f'config/review-intelligence/nsqhs2-standard{standard}-actions-v1.json').read_text())
            s['sourceSha256']=hashlib.sha256(self.raw).hexdigest()
            rows=records(self.frameworks,s,self.raw)
            self.assertEqual([r['record']['RequirementCode'] for r in rows],
                             [f'{standard}.{n:02d}' for n in range(1,count+1)])
            current={r['record']['RequirementKey'] for r in rows}
            self.assertFalse(keys&current);keys|=current
        self.assertEqual(len(keys),151)
