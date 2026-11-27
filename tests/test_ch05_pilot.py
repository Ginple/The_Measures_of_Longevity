"""08_LINEAGE §7.2 single-chapter pilot (ch5): bookkeeping checks, not scientific validation."""
from pathlib import Path
import copy
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import claim_record_hash, inspect_project  # noqa: E402

PILOT = ROOT / 'knowledge_base/pilots/ch05_measurement_contract'
spec = importlib.util.spec_from_file_location('ch05_builder', PILOT / 'build_project.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def load():
    return json.loads((PILOT / 'project.json').read_text(encoding='utf-8'))


class Ch05PilotTest(unittest.TestCase):
    def setUp(self):
        self.data = load()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for art in self.data['artifacts']:
            dst = self.root / art['path']
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / art['path'], dst)

    def tearDown(self):
        self.tmp.cleanup()

    def reasons(self, result):
        return [i['reason'] for i in result['issues']]

    def test_committed_record_is_clean_and_matches_builder(self):
        r = inspect_project(self.data, ROOT)
        self.assertTrue(r['schema_valid'])
        self.assertEqual(r['issues'], [])
        self.assertEqual(r['artifact_drift'], [])
        self.assertEqual(self.data, builder.build(), 'project.json differs from builder: rebind deliberately')

    def test_release_stays_blocked_and_no_review_is_invented(self):
        r = inspect_project(self.data, ROOT)
        self.assertEqual(r['formal_release_record_check'], 'blocked')
        self.assertEqual(self.data['reviews'], [])
        self.assertEqual(r['scientific_truth'], 'not_computed')
        self.assertFalse(self.data['coverage']['human_inventory_complete'])
        self.assertEqual(self.data['coverage']['registered_claims'], len(self.data['claims']))

    def test_chapter_edit_outside_spans_makes_every_claim_stale(self):
        with (self.root / self.data['artifacts'][0]['path']).open('a', encoding='utf-8') as f:
            f.write('\n未审读的新增句子。\n')
        r = inspect_project(self.data, self.root)
        self.assertIn('A-CH5', r['artifact_drift'])
        self.assertTrue({c['id'] for c in self.data['claims']} <= set(r['stale_nodes']))

    def test_excerpt_edit_reaches_only_its_consumers(self):
        art = next(a for a in self.data['artifacts'] if a['id'] == 'A-GALLERI')
        with (self.root / art['path']).open('a', encoding='utf-8') as f:
            f.write('Later correction outside selected quotes.\n')
        r = inspect_project(self.data, self.root)
        self.assertIn('CH5-C004', r['stale_nodes'])
        for other in ('CH5-C001', 'CH5-C002', 'CH5-C003', 'CH5-C005'):
            self.assertNotIn(other, r['stale_nodes'])
        self.assertIn('CH5-C004', r['critical_unresolved'])

    def test_context_or_quote_change_invalidates_judgement(self):
        d = copy.deepcopy(self.data)
        d['claims'][3]['context']['population'] = 'all adults everywhere'
        self.assertIn('assessment_record_binding_mismatch', self.reasons(inspect_project(d, ROOT)))
        d = copy.deepcopy(self.data)
        d['evidence'][0]['text'] = 'An invented quote.\n'
        self.assertIn('exact_span_mismatch', self.reasons(inspect_project(d, ROOT)))

    def test_causal_upgrade_of_trial_report_not_licensed(self):
        d = copy.deepcopy(self.data)
        c = d['claims'][3]
        c['kind'] = 'causal'
        c['assessment']['record_sha256'] = claim_record_hash(c, {e['id']: e for e in d['evidence']})
        issues = inspect_project(d, ROOT)['issues']
        self.assertTrue(any(i['reason'] == 'required_dimension_not_supported'
                            and i.get('dimension') == 'causal_identification' for i in issues))

    def test_normative_rule_kept_unknown_and_lineage_bound_to_v7_06(self):
        c5 = next(c for c in self.data['claims'] if c['id'] == 'CH5-C005')
        self.assertEqual(c5['assessment']['state'], 'unknown')
        ev = {e['id']: e for e in self.data['evidence']}
        self.assertEqual(ev['E-V7-RULES']['artifact_id'], 'A-V7')
        outline = json.loads((ROOT / 'books/manuscript/outline_v1.json').read_text(encoding='utf-8'))
        v7_06 = outline['inherited']['V7-06']
        self.assertEqual(v7_06['to'], 5)
        self.assertLess(v7_06['line'], ev['E-V7-RULES']['lines_1based_halfopen'][0])

    def test_numbers_in_chapter_match_quoted_sources(self):
        claims = {c['id']: c['text'] for c in self.data['claims']}
        ev = {e['id']: e['text'] for e in self.data['evidence']}
        for chapter_token, eid, source_token in [
            ('706例', 'E-GAL-COUNTS', '706 and 688'), ('1.03', 'E-GAL-IRR', '1.03 [0.92-1.14]'),
            ('17个月', 'E-GAL-FU', 'median of 17'), ('190 名', 'E-WARM-190', '190 participants'),
            ('只有20人', 'E-WARM-20', '(n = 20)'), ('57个缺失', 'E-WARM-S3', 'n_miss_BL 57'),
            ('26 项', 'E-YI-SCOPE', 'Twenty-six'),
        ]:
            with self.subTest(token=chapter_token):
                self.assertTrue(any(chapter_token in t for t in claims.values()))
                self.assertIn(source_token, ev[eid])


if __name__ == '__main__':
    unittest.main()
