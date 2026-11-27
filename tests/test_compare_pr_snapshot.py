import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('snapshot_compare', ROOT/'scripts/compare_pr_snapshot.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class SnapshotCompareTests(unittest.TestCase):
    def test_casefold_collision_without_filesystem_assumptions(self):
        self.assertEqual(mod.casefold_collisions(['X.txt', 'x.txt', 'other']), [['X.txt', 'x.txt']])

    def test_pinned_comparison(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            def g(*args):
                return subprocess.run(['git', '-C', td, *args], check=True, capture_output=True).stdout.decode().strip()
            g('init', '-q')
            g('config', 'user.email', 'test@example.invalid')
            g('config', 'user.name', 'Test')
            (root/'base.txt').write_text('base')
            g('add', '.'); g('commit', '-qm', 'base'); base = g('rev-parse', 'HEAD')
            (root/'base.txt').write_text('remote')
            (root/'X.txt').write_text('a')
            (root/'Y.txt').write_text('b')
            g('add', '.'); g('commit', '-qm', 'candidate'); head = g('rev-parse', 'HEAD')
            (root/'base.txt').write_text('local')
            (root/'X.txt').unlink()
            result = mod.compare(root, base, head)
            self.assertEqual(result['counts'], {'different': 1, 'identical': 1, 'local_absent': 1})
            self.assertEqual(result['casefold_collisions_in_snapshot'], [])
            self.assertEqual(result['snapshot_commit'], head)
            self.assertEqual((root/'base.txt').read_text(), 'local')

    def test_deleted_and_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            def g(*args):
                return subprocess.run(['git', '-C', td, *args], check=True, capture_output=True).stdout.decode().strip()
            g('init', '-q'); g('config', 'user.email', 'test@example.invalid'); g('config', 'user.name', 'Test')
            (root/'deleted').write_text('one'); g('add', '.'); g('commit', '-qm', 'base'); base = g('rev-parse', 'HEAD')
            (root/'deleted').unlink(); (root/'new').write_text('new')
            (root/'folder').mkdir(); (root/'folder'/'child').write_text('remote')
            g('add', '-A'); g('commit', '-qm', 'next'); head = g('rev-parse', 'HEAD')
            (root/'new').unlink(); (root/'new').symlink_to('/etc/passwd')
            (root/'folder'/'child').unlink(); (root/'folder').rmdir()
            (root/'folder').symlink_to('/etc')
            result = mod.compare(root, base, head)
            self.assertEqual(result['counts'], {'deleted_upstream': 1, 'local_symlink_not_read': 2})
            self.assertTrue(all(row['worktree_sha256'] is None for row in result['paths']))


if __name__ == '__main__':
    unittest.main()
