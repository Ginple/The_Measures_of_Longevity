"""Fail-closed checks for the current local software validator."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from run_validation import project_files, require_checks


class ValidationTests(unittest.TestCase):
    def test_explicit_failure_and_detail(self):
        require_checks({'ok': True})
        with self.assertRaisesRegex(RuntimeError, 'schema'):
            require_checks({'ok': True, 'schema': False})

    def test_optimized_interpreter_still_fails(self):
        code = ('import sys; sys.path.insert(0, sys.argv[1]); '
                'from run_validation import require_checks; '
                "require_checks({'integrity': False})")
        proc = subprocess.run([sys.executable, '-O', '-c', code, str(ROOT / 'scripts')],
                              capture_output=True, text=True, timeout=10)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn('integrity', proc.stderr)

    def test_prunes_local_environment_but_reports_real_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '.venv').mkdir()
            (root / '.venv' / 'generated.html').write_text('dependency')
            (root / 'notes').mkdir()
            (root / 'notes' / 'draft.htm').write_text('project')
            (root / 'notes' / 'visible.md').write_text('document')
            self.assertEqual([p.relative_to(root).as_posix() for p in project_files(root, {'.html', '.htm'})], ['notes/draft.htm'])
            self.assertEqual([p.relative_to(root).as_posix() for p in project_files(root, {'.md'})], ['notes/visible.md'])


if __name__ == '__main__':
    unittest.main()
