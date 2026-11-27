"""Offline software contracts; no evidence, frozen receipts or baselines are rewritten."""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'src'))
sys.path.insert(0, str(P / 'tools'))
from dashboard_contract import check_dashboard
from markdown_links import classify_links


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unit_tests():
    # Run each suite in its own subprocess: tests use different local modules.
    suites = {'project': 'tests', 'experiments': 'knowledge_base/experiments',
              'pilot': 'knowledge_base/pilots/real_claims_001/tests'}
    summaries = {}
    for name, directory in suites.items():
        env = {**os.environ, 'PYTHONPATH': os.pathsep.join((str(P/'src'), str(P/'tools'), str(P/'knowledge_base/experiments')))}
        r = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', directory, '-v'],
                           cwd=P, env=env, capture_output=True, text=True, timeout=120)
        if r.returncode:
            raise RuntimeError(f'{name} tests failed:\n{r.stdout}\n{r.stderr}')
        # unittest's exit status allows skips; explicitly forbid silent skips.
        if 'skipped=' in r.stderr:
            raise RuntimeError(f'{name} tests skipped:\n{r.stderr}')
        import re
        match = re.search(r'Ran (\d+) tests? in ', r.stderr)
        if not match or int(match.group(1)) == 0:
            raise RuntimeError(f'{name} suite did not run tests:\n{r.stderr}')
        summaries[name] = int(match.group(1))
    return summaries


def derived(root, seed):
    env = {**os.environ, 'PYTHONHASHSEED': str(seed), 'PYTHONPATH': str(root/'src')}
    commands = {'PROJECT_CHECK': ['check', 'examples/toy/project.json'],
                'TOPOLOGY': ['topology', 'examples/toy/corpus/draft.md', 'examples/toy/ontology.json'],
                'DIAGNOSTICS': ['diagnostics']}
    out = {}
    for name, args in commands.items():
        r = subprocess.run([sys.executable, '-m', 'research_assurance.cli', *args], cwd=root,
                           env=env, capture_output=True, text=True, timeout=120)
        if r.returncode:
            raise RuntimeError(f'{name}: {r.stderr}')
        json.loads(r.stdout)
        out[name] = r.stdout.encode()
    return out


def units_at(root, seed):
    env = {**os.environ, 'PYTHONHASHSEED': str(seed)}
    r = subprocess.run([sys.executable, str(root/'scripts/run_validation.py'), '--unit-only'],
                       cwd=root, env=env, capture_output=True, text=True, timeout=180)
    if r.returncode:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit-only', action='store_true', help='run test suites and report counts')
    args = parser.parse_args()
    if args.unit_only:
        print(json.dumps(unit_tests(), sort_keys=True))
        return 0
    before = {f.relative_to(P).as_posix(): digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    units7, units113 = units_at(P, 7), units_at(P, 113)
    first, second = derived(P, 7), derived(P, 113)
    with tempfile.TemporaryDirectory() as td:
        clone = Path(td)/'moved-workbench'
        shutil.copytree(P, clone, ignore=shutil.ignore_patterns('__pycache__', '.git', '.venv', 'venv', '*.egg-info', 'build', 'dist', 'node_modules', '.pytest_cache'))
        moved_units = units_at(clone, 113)
        moved = derived(clone, 113)
    after = {f.relative_to(P).as_posix(): digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    repro = {k: first[k] == second[k] == moved[k] for k in first}
    schema_identical = (P/'schemas/project.schema.json').read_bytes() == (P/'src/research_assurance/project.schema.json').read_bytes()
    links = classify_links(P)
    dashboard_errors = check_dashboard(P)
    result = {'test_counts': units7, 'unit_counts_equal_seed7_seed113_moved': units7 == units113 == moved_units,
              'cli_byte_identical_seed7_seed113_moved': repro,
              'example_inputs_unchanged': before == after, 'schema_copies_identical': schema_identical,
              'dashboard_errors': dashboard_errors, 'markdown_links': links,
              'environment': {'python': sys.version.split()[0], **{n: importlib.metadata.version(n) for n in ['networkx', 'jsonschema', 'beautifulsoup4']}},
              'external_review': 'not_performed', 'scientific_truth': 'not_computed',
              'scope': 'Software contracts and artifact properties only; historical known broken links are reported, not certified.'}
    result['all_software_checks_passed'] = (units7 == units113 == moved_units and all(repro.values()) and before == after
                                              and schema_identical and not dashboard_errors and not links['new'])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['all_software_checks_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
