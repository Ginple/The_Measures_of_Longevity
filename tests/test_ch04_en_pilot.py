"""DEC-016 English ch4 pilot: bookkeeping checks, not scientific validation."""
from fractions import Fraction
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

PILOT = ROOT / 'knowledge_base/pilots/ch04_evidence_en'
spec = importlib.util.spec_from_file_location('ch04_en_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
d_spec = importlib.util.spec_from_file_location('ch04_denominators', PILOT / 'denominators.py')
denominators = importlib.util.module_from_spec(d_spec)
d_spec.loader.exec_module(denominators)


class Ch04EnglishPilotTest(unittest.TestCase):
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
        self.assertIn('A-CH4-EN', r['artifact_drift'])
        self.assertTrue(set(self.claims) <= set(r['stale_nodes']))

    def test_saved_synthetic_output_matches_script_and_hand_arithmetic(self):
        saved = json.loads((PILOT / 'evidence/DENOMINATORS_SYNTHETIC_output.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, json.loads(json.dumps(denominators.build())))
        rev = saved['reversal']
        # The reversal: better in each group, worse pooled.
        self.assertTrue(rev['new_better_in_each_group'])
        self.assertFalse(rev['new_better_overall'])
        self.assertEqual((rev['overall']['new']['recovered'], rev['overall']['old']['recovered']), (180 + 300, 520 + 80))
        # Independent arithmetic for 16 null readouts.
        self.assertEqual(saved['many_readouts']['chance_at_least_one_false_positive'],
                         f'{float(1 - Fraction(19, 20) ** 16):.2f}')
        # 191 reproduces the rounded percentages; 190 does not.
        for n, ok in ((191, True), (190, False)):
            got = all(f'{float(Fraction(100 * c, n)):.1f}' == p for c, p in saved['rounded_percentages']['observations'])
            self.assertEqual(got, ok)
        self.assertEqual(saved['rounded_percentages']['denominators_consistent'], [191])

    def test_records_excerpt_edit_stales_record_claims_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.copy_artifacts(tmp)
            p = Path(tmp) / builder.EV / 'PROJECT_RECORDS_excerpt.txt'
            p.write_text(p.read_text(encoding='utf-8').replace('| 105 | 59 | 164 |', '| 106 | 59 | 165 |'), encoding='utf-8')
            r = inspect_project(self.data, Path(tmp))
        self.assertIn('A-RECORDS', r['artifact_drift'])
        self.assertTrue({'CH4-EN-C004', 'CH4-EN-C005', 'CH4-EN-C007', 'CH4-EN-C010'} <= set(r['stale_nodes']))
        for cid in ('CH4-EN-C001', 'CH4-EN-C003', 'CH4-EN-C008', 'CH4-EN-C012'):
            self.assertNotIn(cid, r['stale_nodes'])

    def test_whole_ledger_and_audits_are_not_bound(self):
        paths = {a['path'] for a in self.data['artifacts']}
        for p in ('knowledge_base/CLAIM_LEDGER.md', 'knowledge_base/CALERIE_TEMPORAL_AUDIT_2026-11-27.md',
                  'knowledge_base/SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md'):
            self.assertNotIn(p, paths)

    def test_numbers_in_english_text_match_quoted_sources(self):
        for cid, token, eid, source_token in [
            ('CH4-EN-C001', 'aged 50 to 75 in Canada', 'E-M-MODEL', 'ages 50-75 years'),
            ('CH4-EN-C001', '2.1 to 6.0 percent of yearly screen-detected cancers', 'E-M-RANGE', '2.1%-6.0% of all yearly screen-detected cancers'),
            ('CH4-EN-C001', 'from 1 percent at 50 to over 10 percent', 'E-M-AGE', 'from 1% at age 50 to over 10%'),
            ('CH4-EN-C001', '15.9 to 77.6 percent', 'E-M-PPV', '15.9% to 77.6%'),
            ('CH4-EN-C001', '0.3 to 5.3 false positives', 'E-M-PPV', '0.3-5.3 false positives'),
            ('CH4-EN-C002', '180 of 200, 90.0 percent', 'E-SYN-REV', '"percent": "90.0"'),
            ('CH4-EN-C002', '520 of 600, 86.7 percent', 'E-SYN-REV', '"percent": "86.7"'),
            ('CH4-EN-C002', '480 of 800, 60.0 percent, against 600 of 800, 75.0 percent', 'E-SYN-REV', '"percent": "75.0"'),
            ('CH4-EN-C003', 'for fall 1973', 'E-B-AGG', 'for fall 1973'),
            ('CH4-EN-C004', 'In it, 220 adults', 'E-W-RAND', 'n = 220 adults'),
            ('CH4-EN-C004', '25 percent calorie restriction', 'E-W-RAND', '25% CR'),
            ('CH4-EN-C004', 'lists 128 people', 'E-R-CAL', '| 128 | 69 |'),
            ('CH4-EN-C004', '117 and 68', 'E-R-CAL', '| 117 | 68 |'),
            ('CH4-EN-C004', '105 and 59', 'E-R-CAL', '| 105 | 59 |'),
            ('CH4-EN-C005', 'reports 1,083 people aged 60 to 80', 'E-V-METH', 'n = 1,083'),
            ('CH4-EN-C005', 'average of 7.4 years', 'E-V-METH', 'average follow-up 7.4'),
            ('CH4-EN-C005', 'began with 1,671 participants', 'E-R-BASE', '1,671'),
            ('CH4-EN-C006', '854 participants contributed 2,047 observations', 'E-L-N', '854 participants contributed 2,047 observations'),
            ('CH4-EN-C006', 'grew by 14.9 percent a year', 'E-L-RATE', '14.9% annual increase'),
            ('CH4-EN-C006', 'a nonsignificant 6.3 percent', 'E-L-RATE', 'nonsignificant 6.3% increase'),
            ('CH4-EN-C006', 'P for interaction 0.13', 'E-L-RATE', 'Pinteraction = 0.13'),
            ('CH4-EN-C006', 'P=0.04', 'E-L-TET2', 'Pinteraction= 0.04'),
            ('CH4-EN-C007', 'database of 51 public and private', 'E-S-DB', '51 public and private'),
            ('CH4-EN-C007', 'calculated 16 prominent clocks', 'E-S-DB', '16 prominent epigenetic clocks'),
            ('CH4-EN-C008', 'randomised 71,122 people', 'E-GAL-N', '71,122 participants'),
            ('CH4-EN-C008', 'and 71,128 to have it stored', 'E-GAL-N', '71,128 to the control group'),
            ('CH4-EN-C008', 'among 12 prespecified types', 'E-GAL-END', 'among 12 prespecified types'),
            ('CH4-EN-C008', 'ratio 1.03, 95 percent confidence interval 0.92 to 1.14', 'E-GAL-PRIM', '1.03; 95% confidence interval [CI], 0.92 to 1.14'),
            ('CH4-EN-C008', 'ratio of 0.86 (0.74 to 1.00)', 'E-GAL-IV', '0.86 (95% CI, 0.74 to 1.00)'),
            ('CH4-EN-C010', 'only 191 is consistent', 'E-SYN-ROUND', '191'),
            ('CH4-EN-C010', 'its 10 pairs', 'E-R-X106', '10 组'),
            ('CH4-EN-C010', 'describes 190 people', 'E-R-X106', '正文写 190 人'),
            ('CH4-EN-C012', 'is 0.56', 'E-SYN-READ', '"chance_at_least_one_false_positive": "0.56"'),
        ]:
            with self.subTest(token=token):
                self.assertIn(token, self.claims[cid])
                self.assertIn(source_token, self.ev[eid])

    def test_owned_distinctions_and_guards(self):
        # Chapter 4 owns denominators, source families and replication as reading habits (VOL1).
        self.assertIn('built by this project with no real data', self.claims['CH4-EN-C002'])
        self.assertIn('insisting on denominators is pedantry', self.text)
        self.assertIn('But the denominator can reverse the direction itself.', self.text)
        self.assertIn('their agreement is not an independent replication', self.text)
        self.assertIn('Six authors appear on both papers.', self.claims['CH4-EN-C007'])
        self.assertIn('chapter 31 takes that up', self.text)
        self.assertIn('a microsimulation model, not a trial', self.claims['CH4-EN-C001'])
        self.assertIn('not a correction (X106)', self.claims['CH4-EN-C010'])
        lowered = self.text.lower()
        for banned in ('colchicine stops', 'colchicine prevents', 'proves that', 'you should be screened',
                       'one person in ten is harmed'):
            self.assertNotIn(banned, lowered)


if __name__ == '__main__':
    unittest.main()
