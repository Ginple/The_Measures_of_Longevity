"""Source binding and structure checks for the DEC-011 outline (software properties only)."""
from pathlib import Path
import importlib.util
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('outline_build', ROOT / 'books/manuscript/outline_build.py')
ob = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ob)


class OutlineSourceBinding(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'books/manuscript/outline_v1.json').read_text(encoding='utf-8'))

    def test_committed_files_are_in_sync_with_builder(self):
        js, md = ob.main(write=False)
        self.assertEqual(json.loads(js), self.data, 'outline_v1.json is stale: rerun outline_build.py')
        self.assertEqual(md, (ROOT / 'books/manuscript/OUTLINE_v1.md').read_text(encoding='utf-8'))

    def test_source_hash_line_and_title_bound(self):
        for key, src in self.data['sources'].items():
            self.assertEqual(ob.sha256(src['path']), src['sha256'], f'{key} corpus changed: review mapping')
            lines = (ROOT / src['path']).read_text(encoding='utf-8').splitlines()
            for cid, rec in self.data['inherited'].items():
                if cid.startswith(key):
                    self.assertEqual(lines[rec['line'] - 1], f"## {cid[3:]}｜{rec['title']}")

    def test_every_numbered_chapter_mapped_once_and_targets_valid(self):
        self.assertEqual(len(self.data['inherited']), 33 + 39)
        targets = {c['n'] for c in self.data['chapters']}
        self.assertEqual(sorted(targets), list(range(1, 34)))
        listed = [k for c in self.data['chapters'] for k in c['inherits']]
        self.assertEqual(sorted(listed), sorted(self.data['inherited']))
        self.assertTrue(all(v['to'] in targets for v in self.data['inherited'].values()))

    def test_parts_contiguous_and_volume_three_protected(self):
        ch = self.data['chapters']
        self.assertEqual([c['n'] for c in ch], list(range(1, 34)))
        self.assertGreaterEqual(sum(c['volume'] == 'Ⅲ' for c in ch) / len(ch), 0.28)
        self.assertEqual(len({c['part'] for c in ch}), 8)

    def test_front_back_matter_slots_do_not_change_chapters(self):
        # DEC-018: matter slots are positions only; they hold no inherited chapter and are not numbered chapters.
        matter = self.data['matter']
        self.assertEqual([m['position'] for m in matter if m['position'] == 'front'], ['front'])
        self.assertTrue({'B1', 'B2', 'B3', 'B4'} <= {m['id'] for m in matter})
        self.assertEqual(len({m['id'] for m in matter}), len(matter))
        self.assertTrue(all(m['title_en'] and m['title'] for m in matter))
        self.assertEqual(len(self.data['chapters']), 33)
        self.assertTrue(all(isinstance(v['to'], int) for v in self.data['inherited'].values()))
        # DEC-017: budgets are a balance reference, not a target.
        self.assertIn('DEC-017', self.data['budget_status'])
        md = (ROOT / 'books/manuscript/OUTLINE_v1.md').read_text(encoding='utf-8')
        self.assertNotIn('预算约', md)

    def test_mutations_are_detected(self):
        # A drifted title in a copied corpus, a dropped assignment and a duplicate heading must each fail.
        import shutil, tempfile
        with tempfile.TemporaryDirectory() as tmp:
            for src in self.data['sources'].values():
                dst = Path(tmp) / src['path']
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / src['path'], dst)
            v6 = Path(tmp) / self.data['sources']['V6']['path']
            v6.write_text(v6.read_text(encoding='utf-8').replace('## 01｜', '## 01｜（改）', 1), encoding='utf-8')
            old_root, ob.ROOT = ob.ROOT, Path(tmp)
            try:
                mutated = ob.build()
            finally:
                ob.ROOT = old_root
        self.assertNotEqual(mutated['sources']['V6']['sha256'], self.data['sources']['V6']['sha256'])
        self.assertNotEqual(mutated['inherited']['V6-01']['title'], self.data['inherited']['V6-01']['title'])
        saved = ob.ASSIGN['V7'].pop(33)
        try:
            with self.assertRaises(ValueError):
                ob.build()
        finally:
            ob.ASSIGN['V7'][33] = saved
        orig = ob.extract_headings
        ob.extract_headings = lambda p: (_ for _ in ()).throw(ValueError('duplicate numbered heading'))
        try:
            with self.assertRaises(ValueError):
                ob.build()
        finally:
            ob.extract_headings = orig


if __name__ == '__main__':
    unittest.main()
