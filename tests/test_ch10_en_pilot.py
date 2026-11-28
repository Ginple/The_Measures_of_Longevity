"""DEC-016 English ch10 pilot: bookkeeping checks, not scientific validation."""
from pathlib import Path
import importlib.util
import json
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import inspect_project  # noqa: E402

PILOT = ROOT / 'knowledge_base/pilots/ch10_routes_en'
spec = importlib.util.spec_from_file_location('ch10_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Ch10EnglishPilotTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))
        self.claims = {c['id']: c['text'] for c in self.data['claims']}
        self.ev = {e['id']: e['text'] for e in self.data['evidence']}
        self.text = (ROOT / builder.EN_PATH).read_text(encoding='utf-8')

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

    def test_chapter_edit_makes_claims_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            with (Path(tmp) / builder.EN_PATH).open('a', encoding='utf-8') as f:
                f.write('\nAn unreviewed new sentence.\n')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-CH10-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_mouse_excerpt_edit_stales_mouse_claims_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'IMMUNE_SUPPORT_abstract.txt'
            p.write_text(p.read_text(encoding='utf-8').replace('did not breach', 'did breach'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-IMMUNE', r['artifact_drift'])
        self.assertTrue({'CH10-EN-C004', 'CH10-EN-C005'} <= set(r['stale_nodes']))
        for cid in ('CH10-EN-C001', 'CH10-EN-C002', 'CH10-EN-C003', 'CH10-EN-C006', 'CH10-EN-C008'):
            self.assertNotIn(cid, r['stale_nodes'])

    def test_capable_copy_matches_chapter_1_excerpt(self):
        ch1 = (ROOT / 'knowledge_base/pilots/ch01_measure_en/evidence/CAPABLE_abstract.txt').read_text(encoding='utf-8')
        mine = (PILOT / 'evidence/CAPABLE_abstract.txt').read_text(encoding='utf-8')
        self.assertEqual(mine.split('\n', 1)[1], ch1)

    def test_whole_ledger_is_not_bound(self):
        paths = {a['path'] for a in self.data['artifacts']}
        self.assertNotIn('knowledge_base/CLAIM_LEDGER.md', paths)
        ledger = (ROOT / 'knowledge_base/CLAIM_LEDGER.md').read_text(encoding='utf-8')
        for line in (PILOT / 'evidence/LEDGER_X15_X79_excerpt.txt').read_text(encoding='utf-8').splitlines():
            if line.startswith('| X'):
                self.assertIn(line, ledger, 'ledger row changed: re-copy and re-bind')

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH10-EN-C001', 'SPRINT trial, 9361 people', 'E-SP-METH', 'assigned 9361 persons'),
            ('CH10-EN-C001', 'below 120 mm Hg or below 140 mm Hg', 'E-SP-METH', 'less than 120 mm Hg'),
            ('CH10-EN-C001', '121.4 and 136.2 mm Hg', 'E-SP-BP', '121.4 mm Hg'),
            ('CH10-EN-C001', 'median of 3.26 years', 'E-SP-STOP', 'median follow-up of 3.26 years'),
            ('CH10-EN-C001', '1.65 percent a year against 2.19 percent, a hazard ratio of 0.75', 'E-SP-STOP', '1.65% per year vs. 2.19% per year; hazard ratio with intensive treatment, 0.75'),
            ('CH10-EN-C001', 'hazard ratio of 0.73', 'E-SP-MORT', 'hazard ratio, 0.73'),
            ('CH10-EN-C002', '100 people with moderate-to-severe knee osteoarthritis', 'E-KN-METH', '100 patients with moderate-to-severe knee osteoarthritis'),
            ('CH10-EN-C002', '32.5 points against 16.0, an adjusted difference of 15.8', 'E-KN-RES', '32.5 vs. 16.0; adjusted mean difference, 15.8'),
            ('CH10-EN-C002', '24 against 6', 'E-KN-AE', '24 vs. 6'),
            ('CH10-EN-C002', '13 of the people assigned to nonsurgical treatment, 26 percent', 'E-KN-CROSS', '13 patients (26%)'),
            ('CH10-EN-C003', 'aged 70 to 84', 'E-AC-METH', 'aged 70-84 years'),
            ('CH10-EN-C003', '(490 people)', 'E-AC-N', '490 (50%) to the hearing intervention'),
            ('CH10-EN-C003', '(487)', 'E-AC-N', '487 (50%)'),
            ('CH10-EN-C003', 'difference of 0.002 standard deviations (p=0.96)', 'E-AC-PRIM', 'difference 0·002'),
            ('CH10-EN-C006', '300 low-income adults aged 65 or older', 'E-CA-DES', '300 low-income community-dwelling adults'),
            ('CH10-EN-C006', 'up to 10 home visits over 5 months', 'E-CA-INT', 'up to 10 home visits over 5 months'),
            ('CH10-EN-C006', '30 percent lower in the CAPABLE group (relative risk 0.70)', 'E-CA-ADL', '30% reduction in ADL disability scores at 5 months (relative risk [RR], 0.70'),
            ('CH10-EN-C006', '17 percent reduction that was not statistically significant', 'E-CA-IADL', 'nonsignificant 17% reduction'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_owned_distinctions_and_guards(self):
        # Chapter 10 owns the routes and the two sources of durability (VOL2).
        for route in ('| Maintain |', '| Repair or clear |', '| Reset |', '| Replace |', '| Compensate |'):
            self.assertIn(route, self.text)
        self.assertIn('Durability has two sources', self.text)
        self.assertIn('A mouse study', self.claims['CH10-EN-C004'])
        self.assertIn('the thymus was not bypassed', self.claims['CH10-EN-C005'])
        self.assertIn('withdrew it', self.claims['CH10-EN-C008'])
        self.assertIn('That suggestion is a lead, not a result.', self.claims['CH10-EN-C003'])
        self.assertIn('chapter 20', self.text)
        lowered = self.text.lower()
        for banned in ('rejuvenates the immune system', 'young thymus was restored', 'proven safe', 'reverses aging',
                       'hearing aids prevent dementia', 'fills the gap', 'first framework'):
            self.assertNotIn(banned, lowered)
        # The withdrawn formula must not come back as an equation.
        self.assertIsNone(re.search(r'maintenance capacity\s*=', lowered))


if __name__ == '__main__':
    unittest.main()
