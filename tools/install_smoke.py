"""Install a local candidate without downloading/build isolation; smoke-test installed CLI."""
from pathlib import Path
import json,os,shutil,subprocess,sys,tempfile
P=Path(__file__).resolve().parents[1]

def require_install_contract(info, check, installed):
 """Fail before emitting success, including when Python runs with -O."""
 failures=[]
 target=Path(installed).resolve()
 for key in ('module_path','distribution_path'):
  value=info.get(key)
  if not isinstance(value,str) or not value or not Path(value).is_absolute() or not Path(value).resolve().is_relative_to(target):
   failures.append(key+' is outside the install target')
 if info.get('module') != '0.1.1' or info.get('metadata') != '0.1.1':
  failures.append('installed versions do not match 0.1.1')
 if info.get('schema') is not True:
  failures.append('embedded schema is missing')
 if check.get('issues') != []:
  failures.append('installed CLI issues are not an empty list')
 if check.get('formal_release_record_check') != 'blocked':
  failures.append('formal release record is not blocked')
 if failures:
  raise RuntimeError('install smoke contract failed: ' + '; '.join(failures))

def main():
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);installed=td/'installed';C=td/'source'
  shutil.copytree(P,C,ignore=shutil.ignore_patterns('.git','.venv','venv','__pycache__','build','dist','node_modules','*.egg-info'))
  r=subprocess.run([sys.executable,'-m','pip','install','--no-deps','--no-build-isolation','--target',str(installed),str(C)],capture_output=True,text=True,timeout=90)
  if r.returncode:raise RuntimeError(r.stdout+r.stderr)
  env={**os.environ,'PYTHONPATH':str(installed)}
  s=subprocess.run([sys.executable,'-c','import research_assurance,importlib.metadata,json; from pathlib import Path; d=importlib.metadata.distribution("research-assurance-toolkit"); print(json.dumps({"module":research_assurance.__version__,"metadata":d.version,"schema":(Path(research_assurance.__file__).with_name("project.schema.json")).is_file(),"module_path":str(Path(research_assurance.__file__).resolve()),"distribution_path":str(Path(d.locate_file("")).resolve())}))'],cwd=td,env=env,capture_output=True,text=True,timeout=30)
  if s.returncode:raise RuntimeError(s.stderr)
  info=json.loads(s.stdout)
  c=subprocess.run([sys.executable,'-m','research_assurance.cli','check',str(C/'examples/toy/project.json')],cwd=td,env=env,capture_output=True,text=True,timeout=30)
  if c.returncode:raise RuntimeError(c.stderr)
  check=json.loads(c.stdout)
  require_install_contract(info,check,installed)
 out={'local_no_deps_no_build_isolation_install_succeeded':True,'installed_module_version':info['module'],'installed_distribution_version':info['metadata'],'embedded_schema_present':info['schema'],
      'module_and_distribution_in_install_target':True,
      'installed_cli_outside_source_directory':{'returncode':c.returncode,'issues':check['issues'],'formal_release_record_check':check['formal_release_record_check']},
      'scope':'Package plumbing only. Dependencies were preinstalled; no clean online dependency resolution was tested. CLI exit 0 is not academic release approval.'}
 print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
