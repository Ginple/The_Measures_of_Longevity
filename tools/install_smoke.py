"""Install a local candidate without downloading/build isolation; smoke-test installed CLI."""
from pathlib import Path
import json,os,shutil,subprocess,sys,tempfile
P=Path(__file__).resolve().parents[1]

def main():
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);installed=td/'installed';C=td/'source'
  shutil.copytree(P,C,ignore=shutil.ignore_patterns('.git','.venv','venv','__pycache__','build','dist','node_modules','*.egg-info'))
  r=subprocess.run([sys.executable,'-m','pip','install','--no-deps','--no-build-isolation','--target',str(installed),str(C)],capture_output=True,text=True,timeout=90)
  if r.returncode:raise RuntimeError(r.stdout+r.stderr)
  env={**os.environ,'PYTHONPATH':str(installed)}
  s=subprocess.run([sys.executable,'-c','import research_assurance,importlib.metadata,json; from pathlib import Path; print(json.dumps({"module":research_assurance.__version__,"metadata":importlib.metadata.distribution("research-assurance-toolkit").version,"schema":(Path(research_assurance.__file__).with_name("project.schema.json")).is_file()}))'],cwd=td,env=env,capture_output=True,text=True,timeout=30)
  if s.returncode:raise RuntimeError(s.stderr)
  info=json.loads(s.stdout)
  c=subprocess.run([sys.executable,'-m','research_assurance.cli','check',str(C/'examples/toy/project.json')],cwd=td,env=env,capture_output=True,text=True,timeout=30)
  if c.returncode:raise RuntimeError(c.stderr)
  check=json.loads(c.stdout)
 out={'local_no_deps_no_build_isolation_install_succeeded':True,'installed_module_version':info['module'],'installed_distribution_version':info['metadata'],'embedded_schema_present':info['schema'],
      'installed_cli_outside_source_directory':{'returncode':c.returncode,'issues':check['issues'],'formal_release_record_check':check['formal_release_record_check']},
      'scope':'Package plumbing only. Dependencies were preinstalled; no clean online dependency resolution was tested. CLI exit 0 is not academic release approval.'}
 print(json.dumps(out,ensure_ascii=False,indent=2))
 assert info['module']==info['metadata']=='0.1.1' and info['schema'] and not check['issues'] and check['formal_release_record_check']=='blocked'
if __name__=='__main__':main()
