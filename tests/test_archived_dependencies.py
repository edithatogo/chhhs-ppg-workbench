import json
from pathlib import Path
import tempfile
import unittest
from check_setup import dependency_metadata


class ArchivedDependencyTests(unittest.TestCase):
    def test_partial_archived_dependency_is_known_but_still_incomplete(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);p=root/'archive/fictional-track/metadata.json'
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'track_id':'fictional-track','status':'in_progress'}))
            result=dependency_metadata(root,{'consumer':{'status':'in_progress'}})
            self.assertIn('fictional-track',result)
            self.assertNotEqual(result['fictional-track']['status'],'completed')
            self.assertNotIn('unknown',result)

    def test_duplicate_or_mismatched_identity_is_not_silently_adopted(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);p=root/'archive/fictional-track/metadata.json'
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({'track_id':'fictional-track','status':'completed'}))
            with self.assertRaisesRegex(ValueError,'ambiguous-or-invalid'):
                dependency_metadata(root,{'fictional-track':{'status':'in_progress'}})
            p.write_text(json.dumps({'track_id':'wrong-track','status':'completed'}))
            with self.assertRaisesRegex(ValueError,'ambiguous-or-invalid'):
                dependency_metadata(root,{})
