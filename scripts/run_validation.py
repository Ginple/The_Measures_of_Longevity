"""Current offline software diagnostics; prints JSON without modifying frozen receipts."""
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
EXCLUDED_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'build', 'dist',
                 'node_modules', '.pytest_cache', '.mypy_cache', '.ruff_cache', '.cache'}


def project_files(root, suffixes):
    """Walk project files only; do not inspect local dependency environments."""
    root = Path(root)
    for directory, names, files in os.walk(root, followlinks=False):
        names[:] = sorted(name for name in names if name not in EXCLUDED_DIRS)
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix.lower() in suffixes and path.is_file():
                yield path


def digest(b):
    return hashlib.sha256(b).hexdigest()


def require_checks(checks):
    """Fail closed even when Python runs with optimization enabled (-O)."""
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise RuntimeError('validation checks failed: ' + ', '.join(failed))


def derived(root, seed):
    env = {**os.environ, 'PYTHONHASHSEED': str(seed), 'PYTHONPATH': str(root/'src')}
    commands = {
        'PROJECT_CHECK': ['check','examples/toy/project.json'],
        'TOPOLOGY': ['topology','examples/toy/corpus/draft.md','examples/toy/ontology.json'],
        'DIAGNOSTICS': ['diagnostics']}
    out = {}
    for name, args in commands.items():
        r = subprocess.run([sys.executable,'-m','research_assurance.cli',*args],cwd=root,env=env,capture_output=True,text=True,timeout=120)
        if r.returncode:
            raise RuntimeError((name, r.returncode, r.stderr))
        json.loads(r.stdout)
        out[name] = r.stdout.encode()
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--unit-only', action='store_true', help='run only project unit tests')
    args = parser.parse_args()
    if args.unit_only:
        suite = unittest.TestLoader().discover(str(P/'tests'))
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        passed = result.wasSuccessful() and not result.skipped and result.testsRun > 0
        print(json.dumps({'tests_run': result.testsRun, 'failures': len(result.failures),
                          'errors': len(result.errors), 'skipped': len(result.skipped), 'passed': passed}))
        if not passed:
            raise SystemExit(1)
        return
    before = {str(f.relative_to(P)):digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    loader = unittest.TestLoader()
    suite = loader.discover(str(P/'tests'))
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful() or result.skipped or result.testsRun == 0:
        raise RuntimeError("unit tests failed, skipped, or did not run")
    first = derived(P,7)
    second = derived(P,113)
    with tempfile.TemporaryDirectory() as td:
        clone = Path(td)/'moved-component'
        shutil.copytree(P,clone,ignore=shutil.ignore_patterns('__pycache__','.git','*.egg-info',
                                                               '.venv','venv','build','dist','node_modules',
                                                               '.pytest_cache','.mypy_cache','.ruff_cache'))
        moved = derived(clone,113)
    repro = {k: first[k] == second[k] == moved[k] for k in first}
    schema_identical = (P/'schemas/project.schema.json').read_bytes() == (P/'src/research_assurance/project.schema.json').read_bytes()
    after = {str(f.relative_to(P)):digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    # Validate first-party Markdown relative hyperlinks, excluding code-style mentions.
    import re
    broken = []
    for f in project_files(P, {'.md'}):
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
            if not link.startswith(('http:','https:','mailto:','#')) and not (f.parent/link.split('#')[0]).exists():
                broken.append({'file':str(f.relative_to(P)),'link':link})
    # Historical handoff/playbook paths are recorded as debt, not treated as valid.
    legacy = json.loads((P/'review/legacy_broken_links.json').read_text(encoding='utf-8'))
    unexpected = [item for item in broken if item not in legacy]
    html = [str(f.relative_to(P)) for f in project_files(P, {'.html', '.htm'})]
    # This is a historical optional snapshot, not a deliverable to regenerate.
    allowed_html = set(html) <= {'STATE_DASHBOARD.HTML'}
    out = {'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
           'seed7_seed113_and_moved_directory_byte_identical':repro,
           'example_inputs_unchanged':before == after,'schema_copies_identical':schema_identical,
           'broken_markdown_links':broken,'unexpected_broken_markdown_links':unexpected,
           'known_legacy_broken_links':len(broken)-len(unexpected),
           'html_files':html,'only_authorized_dashboard_html':allowed_html,
           'environment':{'python':sys.version.split()[0],**{n:importlib.metadata.version(n) for n in ['networkx','jsonschema']}},
           'scope':'software and artifact properties only; not scientific validity or independent review'}
    print(json.dumps(out,ensure_ascii=False,indent=2))
    require_checks({'derived_outputs_reproducible': all(repro.values()),
                    'example_inputs_unchanged': before == after,
                    'schema_copies_identical': schema_identical,
                    'no_unexpected_broken_links': not unexpected,
                    'only_authorized_historical_html': allowed_html})


if __name__ == '__main__':
    main()
