"""Installation smoke must not report success when subprocess results violate its contract."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

# Exercise the real main() in a separate optimized interpreter, with only pip,
# its metadata probe, and the installed CLI mocked. Do not touch the workspace.
HARNESS = r'''
import importlib.util, json, subprocess, sys
from unittest.mock import patch
spec = importlib.util.spec_from_file_location('smoke', sys.argv[1])
smoke = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smoke)
info, check = json.loads(sys.argv[2])
responses = iter(['install', 'probe', 'cli'])
target = None
def fake_run(args, **kwargs):
    global target
    step = next(responses)
    if step == 'install':
        target = args[args.index('--target')+1]
        return subprocess.CompletedProcess(args, 0, '', '')
    if step == 'probe':
        current = dict(info)
        current.setdefault('module_path', target + '/research_assurance/__init__.py')
        current.setdefault('distribution_path', target)
        return subprocess.CompletedProcess(args, 0, json.dumps(current), '')
    return subprocess.CompletedProcess(args, 0, json.dumps(check), '')
with patch.object(smoke.shutil, 'copytree'), patch.object(smoke.subprocess, 'run', side_effect=fake_run):
    smoke.main()
'''


class InstallSmokeContractTests(unittest.TestCase):
    def run_smoke(self, info, check):
        return subprocess.run(
            [sys.executable, '-O', '-c', HARNESS, str(ROOT / 'tools' / 'install_smoke.py'),
             json.dumps([info, check])], capture_output=True, text=True, timeout=20)

    def test_success_and_each_optimized_failure(self):
        info = {'module': '0.1.1', 'metadata': '0.1.1', 'schema': True}
        check = {'issues': [], 'formal_release_record_check': 'blocked'}
        success = self.run_smoke(info, check)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertTrue(json.loads(success.stdout)['local_no_deps_no_build_isolation_install_succeeded'])
        for bad_info, bad_check, message in [
            ({**info, 'module': '0.1.0'}, check, 'versions'),
            ({**info, 'metadata': '0.1.0'}, check, 'versions'),
            ({**info, 'schema': False}, check, 'schema'),
            ({**info, 'schema': 'true'}, check, 'schema'),
            ({**info, 'module_path': '/outside/research_assurance/__init__.py'}, check, 'module_path'),
            ({**info, 'distribution_path': '/outside'}, check, 'distribution_path'),
            ({**info, 'module_path': 'relative/path'}, check, 'module_path'),
            (info, {**check, 'issues': ['bad']}, 'issues'),
            (info, {**check, 'issues': None}, 'issues'),
            (info, {**check, 'formal_release_record_check': 'passed'}, 'release'),
            (info, {'issues': []}, 'release'),
        ]:
            with self.subTest(message=message, info=bad_info, check=bad_check):
                result = self.run_smoke(bad_info, bad_check)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertNotIn('local_no_deps_no_build_isolation_install_succeeded', result.stdout)


if __name__ == '__main__':
    unittest.main()
