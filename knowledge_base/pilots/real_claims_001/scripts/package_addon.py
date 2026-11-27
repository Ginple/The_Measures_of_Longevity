"""Package only this new pilot directory; never overwrite the previous main ZIP."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile,zipfile
P=Path(__file__).resolve().parents[1];W=P.parents[2];HOME=W.parent
PREFIX='longevity_research_workbench/knowledge_base/pilots/real_claims_001/'
def digest(b):return hashlib.sha256(b).hexdigest()
def files():return sorted(f for f in P.rglob('*') if f.is_file() and '__pycache__' not in f.parts and '.git' not in f.parts)
def main():
 raise SystemExit('Historical pilot packager disabled: it trusts a saved validation receipt and rewrites the historical pilot manifest. A new packaging workflow needs explicit review.')
 v=json.loads((P/'results/VALIDATION.json').read_text());assert v['portable_software_checks_passed']
 names=sorted(set(str(f.relative_to(P)) for f in files())|{'FILE_MANIFEST.json','REPOSITORY_TREE.md'})
 (P/'REPOSITORY_TREE.md').write_text('# 增量实际文件清单 / Additive file tree\n\n```text\n'+PREFIX+'\n'+''.join('  '+n+'\n' for n in names)+'```\n')
 manifest={str(f.relative_to(P)):digest(f.read_bytes()) for f in files() if f!=P/'FILE_MANIFEST.json'}
 (P/'FILE_MANIFEST.json').write_text(json.dumps({'algorithm':'sha256','self_excluded':True,'files':manifest},ensure_ascii=False,indent=2)+'\n')
 dest=HOME/'Longevity_Real_Claims_Pilot_001_增量包.zip'
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
  for f in files():
   info=zipfile.ZipInfo(PREFIX+str(f.relative_to(P)),date_time=(2026,11,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,f.read_bytes())
 with zipfile.ZipFile(dest) as z:
  assert z.testzip() is None
  for name,h in manifest.items():assert digest(z.read(PREFIX+name))==h
  assert all(n.startswith(PREFIX) for n in z.namelist())
  members=len(z.namelist())
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);work=root/'longevity_research_workbench';work.mkdir()
   shutil.copytree(W/'src',work/'src',ignore=shutil.ignore_patterns('__pycache__','*.egg-info'))
   z.extractall(root);pilot=root/PREFIX
   r=subprocess.run([sys.executable,'scripts/validate.py'],cwd=pilot,capture_output=True,text=True,timeout=90)
   if r.returncode:raise RuntimeError(r.stdout+r.stderr)
   smoke=json.loads((pilot/'results/VALIDATION.json').read_text());assert smoke['portable_software_checks_passed']
 receipt={'zip_name':dest.name,'bytes':dest.stat().st_size,'sha256':digest(dest.read_bytes()),'members':members,'manifest_file_count':len(manifest),'all_members_under_new_pilot_directory':True,'zip_crc_ok':True,'manifest_hashes_ok':True,'extracted_portable_validation':smoke,'full_third_party_sources_in_zip':False,'requires_existing_parent_component':'research-assurance toolkit 0.1.1 candidate at repository root src/','independent_review':'not_performed','academic_release':'blocked'}
 out=HOME/'Longevity_Real_Claims_Pilot_001_交付回执.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
