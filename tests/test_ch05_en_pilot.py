"""DEC-016 English ch5 pilot: bookkeeping checks, not scientific or translation validation."""
from pathlib import Path
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import inspect_project  # noqa: E402

PILOT = ROOT / 'knowledge_base/pilots/ch05_measurement_contract_en'
spec = importlib.util.spec_from_file_location('ch05_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch05EnglishPilotTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))
        self.zh = json.loads((ROOT / 'knowledge_base/pilots/ch05_measurement_contract/project.json').read_text(encoding='utf-8'))

    def copy_artifacts(self, tmp):
        for art in self.data['artifacts']:
            dst = Path(tmp) / art['path']
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / art['path'], dst)

    def test_committed_record_is_clean_and_matches_builder(self):
        r = inspect_project(self.data, ROOT)
        self.assertTrue(r['schema_valid'])
        self.assertEqual(r['issues'], [])
        self.assertEqual(r['artifact_drift'], [])
        self.assertEqual(r['formal_release_record_check'], 'blocked')
        self.assertEqual(self.data['reviews'], [])
        self.assertEqual(self.data, builder.build(), 'project.json differs from builder: rebind deliberately')

    def test_same_evidence_and_state_as_chinese_pilot(self):
        zh_claims = {c['id']: c for c in self.zh['claims']}
        zh_ev = {e['id']: e['text'] for e in self.zh['evidence']}
        en_ev = {e['id']: e['text'] for e in self.data['evidence']}
        for c in self.data['claims']:
            z = zh_claims[c['id'].replace('-EN', '')]
            with self.subTest(claim=c['id']):
                self.assertEqual(c['context'], z['context'])
                self.assertEqual(c['assessment']['state'], z['assessment']['state'])
                self.assertEqual(c['evidence_ids'][:-1], z['evidence_ids'])
                self.assertEqual(c['evidence_ids'][-1], 'E-ZH-' + z['id'][4:])
                for eid in z['evidence_ids']:
                    self.assertEqual(en_ev[eid], zh_ev[eid])
                self.assertEqual(en_ev['E-ZH-' + z['id'][4:]], z['text'])

    def test_chinese_edit_makes_english_claims_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            zh_path = next(a['path'] for a in self.data['artifacts'] if a['id'] == 'A-CH5')
            with (Path(tmp) / zh_path).open('a', encoding='utf-8') as f:
                f.write('\n未审读的新增句子。\n')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-CH5', r['artifact_drift'])
        self.assertTrue({c['id'] for c in self.data['claims']} <= set(r['stale_nodes']))

    def test_english_edit_makes_english_claims_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            with (Path(tmp) / builder.EN_PATH).open('a', encoding='utf-8') as f:
                f.write('\nAn unreviewed new sentence.\n')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-CH5-EN', r['artifact_drift'])
        self.assertTrue({c['id'] for c in self.data['claims']} <= set(r['stale_nodes']))

    def test_numbers_in_english_text_match_quoted_sources(self):
        claims = {c['id']: c['text'] for c in self.data['claims']}
        ev = {e['id']: e['text'] for e in self.data['evidence']}
        for token, eid, source_token in [
            ('706 cases', 'E-GAL-COUNTS', '706 and 688'), ('1.03', 'E-GAL-IRR', '1.03 [0.92-1.14]'),
            ('17 months', 'E-GAL-FU', 'median of 17'), ('190 analyzable', 'E-WARM-190', '190 participants'),
            ('only 20 people', 'E-WARM-20', '(n = 20)'), ('57 missing', 'E-WARM-S3', 'n_miss_BL 57'),
            ('26 human intervention studies', 'E-YI-SCOPE', 'Twenty-six'),
        ]:
            with self.subTest(token=token):
                self.assertTrue(any(token in t for t in claims.values()))
                self.assertIn(source_token, ev[eid])


if __name__ == '__main__':
    unittest.main()
