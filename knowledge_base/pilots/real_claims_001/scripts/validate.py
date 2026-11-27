"""Validate current pilot without updating any baseline, source selection or judgement."""
from pathlib import Path
import argparse,hashlib,importlib.metadata,json,os,re,shutil,subprocess,sys,tempfile,unittest
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P/'scripts'))
from pilot_core import inspect,quantitative_checks,check_source_trace

def units():
 suite=unittest.defaultTestLoader.discover(str(P/'tests'));r=unittest.TextTestRunner(verbosity=1).run(suite)
 return {'test_functions':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),'skipped':len(r.skipped),'passed':r.wasSuccessful() and not r.skipped}

def history_check(workspace):
 b1=json.loads((P/'governance/history_before.json').read_text());b2=json.loads((P/'governance/prior_540_expected.json').read_text());conflicts=[x for x in b1.keys()&b2.keys() if b1[x]!=b2[x]];merged={**b2,**b1};changed=[];missing=[]
 for name,h in merged.items():
  f=Path(workspace)/name
  if not f.is_file():missing.append(name)
  elif hashlib.sha256(f.read_bytes()).hexdigest()!=h:changed.append(name)
 return {'prior_historical_baseline_count':len(b2),'pre_increment_baseline_count':len(b1),'unique_protected_existing_files':len(merged),'expectation_conflicts':conflicts,'changed':changed,'missing':missing,'status':'verified_unchanged' if not conflicts and not changed and not missing else 'not_verified','scope':'Read-only byte check, not full reading or academic validation'}

def subprocess_inspect(root,seed):
 env={**os.environ,'PYTHONHASHSEED':str(seed)}
 r=subprocess.run([sys.executable,str(root/'scripts/validate.py'),'--inspect-only'],cwd=root,env=env,capture_output=True,text=True,timeout=45)
 if r.returncode:raise RuntimeError(r.stderr)
 return r.stdout.encode()

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--source-cache');parser.add_argument('--history-workspace');parser.add_argument('--inspect-only',action='store_true');parser.add_argument('--unit-only',action='store_true');a=parser.parse_args()
 if a.inspect_only:print(json.dumps(inspect(P),ensure_ascii=False,sort_keys=True));return 0
 if a.unit_only:
  u=units();print(json.dumps(u));return 0 if u['passed'] else 1
 before={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for d in ['corpus','evidence','provenance','governance'] for f in (P/d).rglob('*') if f.is_file()}
 u=units();base=inspect(P);quant=quantitative_checks();s7=subprocess_inspect(P,7);s113=subprocess_inspect(P,113)
 # Preserve correct location relative to the existing main component, without copying a second live engine.
 with tempfile.TemporaryDirectory() as td:
  work=Path(td)/'moved-workbench';work.mkdir()
  shutil.copytree(P.parents[2]/'src',work/'src',ignore=shutil.ignore_patterns('__pycache__','*.egg-info'))
  moved=work/'knowledge_base/pilots/real_claims_001';moved.parent.mkdir(parents=True)
  shutil.copytree(P,moved,ignore=shutil.ignore_patterns('__pycache__'))
  relocated=subprocess_inspect(moved,113)
  rr=subprocess.run([sys.executable,str(moved/'scripts/validate.py'),'--unit-only'],cwd=moved,capture_output=True,text=True,timeout=60)
  mu=json.loads(rr.stdout) if rr.returncode==0 else {'passed':False,'stderr':rr.stderr}
 after={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for d in ['corpus','evidence','provenance','governance'] for f in (P/d).rglob('*') if f.is_file()}
 links=[]
 for f in sorted(P.rglob('*.md')):
  for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',f.read_text()):
   if not link.startswith(('http:','https:','mailto:','#')) and not (f.parent/link.split('#')[0]).exists():links.append({'file':str(f.relative_to(P)),'link':link})
 result={'unit_tests':u,'moved_unit_tests':mu,'seed7_seed113_and_moved_inspection_byte_identical':s7==s113==relocated,'immutable_inputs_unchanged':before==after,'engine_integrity_issues':base['engine']['issues'],'mapping_issues':base['mapping_issues'],'broken_markdown_links':links,'no_html_in_export':not any(f.suffix.lower()=='.html' for f in P.rglob('*') if f.is_file()),'environment':{'python':sys.version.split()[0],**{n:importlib.metadata.version(n) for n in ['networkx','jsonschema','beautifulsoup4']}},'external_review':'not_performed','formal_academic_release':'blocked','scientific_truth':'not_computed'}
 result['portable_software_checks_passed']=u['passed'] and mu['passed'] and s7==s113==relocated and before==after and not base['engine']['issues'] and not base['mapping_issues'] and not links and result['no_html_in_export']
 (P/'results').mkdir(exist_ok=True)
 for name,data in [('PROJECT_CHECK',base),('QUANTITATIVE_CHECKS',quant),('VALIDATION',result)]: (P/f'results/{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 if a.source_cache:
  traced=inspect(P,a.source_cache);(P/'results/SOURCE_TRACE_LOCAL.json').write_text(json.dumps(traced,ensure_ascii=False,indent=2)+'\n');result['local_source_trace_ok']=not traced['source_trace']['issues']
 if a.history_workspace:
  hist=history_check(a.history_workspace);(P/'results/HISTORY_INTEGRITY_LOCAL.json').write_text(json.dumps(hist,ensure_ascii=False,indent=2)+'\n');result['local_history_unchanged']=hist['status']=='verified_unchanged'
 # Local optional results are separate provenance receipts, not falsely portable prerequisites.
 print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['portable_software_checks_passed'] and result.get('local_source_trace_ok',True) and result.get('local_history_unchanged',True) else 1
if __name__=='__main__':raise SystemExit(main())
