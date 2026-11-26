"""Read-only to evidence/fixtures/baselines. Writes only results, never refreshes trust."""
from pathlib import Path
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


def digest(b):
    return hashlib.sha256(b).hexdigest()


def derived(root, seed):
    env = {**os.environ, 'PYTHONHASHSEED': str(seed), 'PYTHONPATH': str(root/'src')}
    commands = {
        'PROJECT_CHECK': ['check','examples/toy/project.json'],
        'TOPOLOGY': ['topology','examples/toy/corpus/draft.md','examples/toy/ontology.json'],
        'DIAGNOSTICS': ['diagnostics']}
    out = {}
    for name, args in commands.items():
        r = subprocess.run([sys.executable,'-m','research_assurance.cli',*args],cwd=root,env=env,capture_output=True,text=True)
        if r.returncode:
            raise RuntimeError((name, r.returncode, r.stderr))
        json.loads(r.stdout)
        out[name] = r.stdout.encode()
    return out


def main():
    before = {str(f.relative_to(P)):digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    loader = unittest.TestLoader()
    suite = loader.discover(str(P/'tests'))
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    assert result.wasSuccessful()
    first = derived(P,7)
    second = derived(P,113)
    with tempfile.TemporaryDirectory() as td:
        clone = Path(td)/'moved-component'
        shutil.copytree(P,clone,ignore=shutil.ignore_patterns('__pycache__','.git','*.egg-info'))
        moved = derived(clone,113)
    repro = {k: first[k] == second[k] == moved[k] for k in first}
    for name, content in first.items():
        (P/'results'/f'{name}.json').write_bytes(content)
    schema_identical = (P/'schemas/project.schema.json').read_bytes() == (P/'src/research_assurance/project.schema.json').read_bytes()
    after = {str(f.relative_to(P)):digest(f.read_bytes()) for f in (P/'examples').rglob('*') if f.is_file()}
    # Validate first-party Markdown relative hyperlinks, excluding code-style mentions.
    import re
    broken = []
    for f in sorted(P.rglob('*.md')):
        if '__pycache__' in f.parts:
            continue
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',f.read_text()):
            if not link.startswith(('http:','https:','mailto:','#')) and not (f.parent/link.split('#')[0]).exists():
                broken.append({'file':str(f.relative_to(P)),'link':link})
    out = {'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
           'seed7_seed113_and_moved_directory_byte_identical':repro,
           'example_inputs_unchanged':before == after,'schema_copies_identical':schema_identical,
           'broken_markdown_links':broken,'no_new_dashboard_html':not any(P.rglob('*.HTML')) and not any(P.rglob('*.html')),
           'environment':{'python':sys.version.split()[0],**{n:importlib.metadata.version(n) for n in ['networkx','jsonschema']}},
           'scope':'software and artifact properties only; not scientific validity or independent review'}
    (P/'results/VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
    assert all(repro.values()) and before == after and schema_identical and not broken and out['no_new_dashboard_html']


if __name__ == '__main__':
    main()
