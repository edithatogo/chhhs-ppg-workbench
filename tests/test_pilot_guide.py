import json,unittest
from pathlib import Path
from scripts.ppg_pilot_guide import render


class PilotGuide(unittest.TestCase):
    def setUp(self):
        self.definition=json.loads(Path('config/review-intelligence/pilot-guide-v1.json').read_text())
        self.bindings={l['key']:'https://example.test/'+l['key'] for s in self.definition['sections'] for l in s['links']}
    def test_sections_links_and_authority_limits(self):
        value=render(self.definition,self.bindings)
        self.assertEqual(value.count('<h3>'),8)
        self.assertIn('not a live owner service',value)
        self.assertIn('requested V7 edition',value)
        self.assertIn('SourceText',value)
    def test_missing_unsafe_and_unescaped_links_refused(self):
        with self.assertRaises(ValueError):render(self.definition,{})
        self.bindings['workspace']='javascript:alert(1)'
        with self.assertRaises(ValueError):render(self.definition,self.bindings)
        self.bindings['workspace']='https://example.test/?x="quoted"&a=1'
        value=render(self.definition,self.bindings);self.assertIn('&quot;quoted&quot;&amp;',value)
