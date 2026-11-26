"""Offline software validation. Does not refresh sources, assessments or trust baselines."""
from pathlib import Path
import hashlib,importlib.metadata,json,os,re,shutil,subprocess,sys,tempfile,unittest
P=Path(__file__).resolve().parents[1]
C=P/'methods/research-assurance'

def run_units():
 sys.path.insert(0,str(C/'src'))
 suite=unittest.defaultTestLoader.discover(str(P/'tests'))
 result=unittest.TextTestRunner(verbosity=1).run(suite)
 return {'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful()}

def units_at(root,seed):
 env={**os.environ,'PYTHONHASHSEED':str(seed)}
 r=subprocess.run([sys.executable,str(root/'tools/run_validation.py'),'--unit-only'],cwd=root,env=env,capture_output=True,text=True,timeout=90)
 if r.returncode:raise RuntimeError(r.stderr)
 return json.loads(r.stdout)

def main():
 if '--unit-only' in sys.argv:
  result=run_units();print(json.dumps(result,sort_keys=True));return 0 if result['passed'] else 1
 env={**os.environ,'PYTHONPATH':str(C/'src')}
 r=subprocess.run([sys.executable,'scripts/run_validation.py'],cwd=C,env=env,capture_output=True,text=True,timeout=120)
 if r.returncode:raise RuntimeError(r.stdout+'\n'+r.stderr)
 library=json.loads((C/'results/VALIDATION.json').read_text())
 units=units_at(P,7);units2=units_at(P,113)
 with tempfile.TemporaryDirectory() as td:
  clone=Path(td)/'moved-workbench';shutil.copytree(P,clone,ignore=shutil.ignore_patterns('__pycache__','.git','*.egg-info','build'))
  moved=units_at(clone,113)
 links=[]
 for f in sorted(P.rglob('*.md')):
  for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',f.read_text()):
   if not link.startswith(('http:','https:','mailto:','#')) and not (f.parent/link.split('#')[0]).exists():links.append({'file':str(f.relative_to(P)),'link':link})
 out={'component_version':(C/'src/research_assurance/__init__.py').read_text().split('__version__ = ')[1].strip().strip("'\""),
      'library_tests':library['tests_run'],'project_tests':units['tests_run'],'total_test_functions':library['tests_run']+units['tests_run'],
      'failures':units['failures']+library['failures'],'errors':units['errors']+library['errors'],
      'project_unit_summary_seed7_seed113_moved_equal':units==units2==moved,
      'library_cli_outputs_seed7_seed113_moved_byte_identical':library['seed7_seed113_and_moved_directory_byte_identical'],
      'example_inputs_unchanged':library['example_inputs_unchanged'],'schema_copies_identical':library['schema_copies_identical'],
      'broken_markdown_links':links,'no_html':not any(f.suffix.lower()=='.html' for f in P.rglob('*') if f.is_file()),
      'environment':{'python':sys.version.split()[0],**{n:importlib.metadata.version(n) for n in ['networkx','jsonschema']}},
      'external_review':'not_performed','scientific_truth':'not_computed','scope':'software properties only; local source replays and original-history verification are separate optional provenance checks'}
 out['all_software_checks_passed']=not out['failures'] and not out['errors'] and units['passed'] and out['project_unit_summary_seed7_seed113_moved_equal'] and all(out['library_cli_outputs_seed7_seed113_moved_byte_identical'].values()) and out['example_inputs_unchanged'] and out['schema_copies_identical'] and not links and out['no_html']
 (P/'artifacts').mkdir(exist_ok=True)
 (P/'artifacts/VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
 return 0 if out['all_software_checks_passed'] else 1
if __name__=='__main__':raise SystemExit(main())
