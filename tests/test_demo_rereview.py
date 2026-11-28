"""2026-11-28 re-review of the seven stale demo drafts: bookkeeping checks, not scientific review."""
from pathlib import Path
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('demo_rereview_scan', ROOT / 'tools/demo_rereview_scan.py')
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)
REPORT = ROOT / 'review/DEMO_DRAFTS_REREVIEW_2026-11-28.md'

# Human judgement pinned at re-review: every chapter number each draft may cite (OUTLINE_v1 numbering,
# or an old number explicitly marked as old). A new reference fails until someone checks it.
EXPECTED_REFS = {
    'CH01_长寿的五个问题_示范稿.md': {1, 5, 15},
    'CH19_谁替谁维护_示范稿.md': {19, 21},
    'CH20_平均不等于及时_示范稿.md': {21, 22},
    'CH21_有余量却用不上_示范稿.md': {19, 22},
    'CH22_清除之后谁来接班_示范稿.md': {15, 19},
    'CH23_状态还在细胞换了吗_示范稿.md': {15, 17},
    'CH24_修好这一次还剩多少下一次_示范稿.md': {15},
}
# Watch-list hits judged at re-review: negations ("不是…首创", "不推断…延寿") or biology ("首次照射").
REVIEWED_WATCH = {
    'CH19_谁替谁维护_示范稿.md': {'延寿', '首次', '首创'},
    'CH20_平均不等于及时_示范稿.md': {'抗衰'},
    'CH22_清除之后谁来接班_示范稿.md': {'延寿'},
    'CH24_修好这一次还剩多少下一次_示范稿.md': {'首创', '首次'},
}


class DemoRereviewTest(unittest.TestCase):
    def setUp(self):
        self.data = scan.build()
        self.by_name = {Path(d['file']).name: d for d in self.data['drafts']}

    def test_receipt_in_sync(self):
        stored = json.loads(scan.OUT.read_text(encoding='utf-8'))
        self.assertEqual(stored, json.loads(json.dumps(self.data, ensure_ascii=False)))

    def test_every_draft_carries_note_and_review_status(self):
        report = REPORT.read_text(encoding='utf-8')
        for name, d in self.by_name.items():
            with self.subTest(name=name):
                self.assertTrue(d['has_rereview_note'])
                self.assertTrue(d['has_external_review_status'])
                self.assertIn(name, report)

    def test_chapter_references_match_reviewed_set(self):
        for name, d in self.by_name.items():
            with self.subTest(name=name):
                self.assertEqual({r['n'] for r in d['chapter_refs']}, EXPECTED_REFS[name])
                self.assertTrue(d['heading'].startswith('# 第一章') or f"第{d['outline_v1_chapter']}章" in d['heading'])

    def test_relative_pointer_only_where_still_true(self):
        # Only old ch20 (now 21) may say "next chapter": it points to space/access, which is new ch22.
        for name, d in self.by_name.items():
            with self.subTest(name=name):
                expected = 1 if name.startswith('CH20') else 0
                self.assertEqual(len(d['relative_refs']), expected)

    def test_watch_hits_were_reviewed_and_ledger_ids_exist(self):
        for name, d in self.by_name.items():
            with self.subTest(name=name):
                self.assertEqual({w['term'] for w in d['watch_terms']}, REVIEWED_WATCH.get(name, set()))
                self.assertNotIn('MISSING', d['ledger_ids'].values())

    def test_impact_record_marks_drafts_reviewed(self):
        impact = json.loads((ROOT / 'review/DEC011_DEC012_IMPACT_2026-11-27.json').read_text(encoding='utf-8'))
        states = {x['node']: x for x in impact['stale_queue']}
        for name in scan.DRAFTS:
            with self.subTest(name=name):
                node = states['books/manuscript/' + name]
                self.assertEqual(node['state_after_this_turn'], 'revised')
                self.assertIn('DEMO_DRAFTS_REREVIEW_2026-11-28', node['note'])


if __name__ == '__main__':
    unittest.main()
