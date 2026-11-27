"""A standalone pilot must not pass if test discovery runs zero tests."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
REL = Path('knowledge_base/pilots/real_claims_001')


class PilotEmptySuiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'src', self.root / 'src', ignore=shutil.ignore_patterns('__pycache__'))
        self.pilot = self.root / REL
        shutil.copytree(ROOT / REL, self.pilot, ignore=shutil.ignore_patterns('__pycache__'))

    def run_pilot(self, *args, optimized=False):
        command = [sys.executable] + (['-O'] if optimized else []) + [str(self.pilot / 'scripts/validate.py'), *args]
        env = {**os.environ, 'PYTHONPATH': str(self.root / 'src')}
        return subprocess.run(command, cwd=self.pilot, env=env, capture_output=True, text=True, timeout=90)

    def test_zero_test_unit_and_full_checks_fail_closed(self):
        for path in (self.pilot / 'tests').glob('test*.py'):
            path.unlink()
        for optimized in (False, True):
            with self.subTest(optimized=optimized):
                unit = self.run_pilot('--unit-only', optimized=optimized)
                self.assertNotEqual(unit.returncode, 0, unit.stdout + unit.stderr)
                data = json.loads(unit.stdout)
                self.assertEqual(data['test_functions'], 0)
                self.assertFalse(data['passed'])
        full = self.run_pilot()
        self.assertNotEqual(full.returncode, 0, full.stdout + full.stderr)
        data = json.loads(full.stdout)
        self.assertEqual(data['unit_tests']['test_functions'], 0)
        self.assertFalse(data['portable_software_checks_passed'])

    def test_real_suite_is_not_empty(self):
        result = self.run_pilot('--unit-only')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertGreater(data['test_functions'], 0)
        self.assertTrue(data['passed'])


if __name__ == '__main__':
    unittest.main()
