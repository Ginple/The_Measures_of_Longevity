"""Create a hashed delivery ZIP; verification receipt lives OUTSIDE the ZIP.

No baselines or scientific judgements are regenerated. Run validation first.
"""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,zipfile
P=Path(__file__).resolve().parents[1]
OMIT={'__pycache__','.git','.venv','venv','build','dist','node_modules'}
def files():
 return sorted(f for f in P.rglob('*') if f.is_file() and not any(x in OMIT or x.endswith('.egg-info') for x in f.relative_to(P).parts))
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
 raise SystemExit('Historical packager disabled: it trusts a stale receipt and overwrites frozen manifests. Create and review a new packaging workflow.')
 validation=json.loads((P/'artifacts/VALIDATION.json').read_text());assert validation['all_software_checks_passed']
 # A file listing, not a planned conceptual tree. Include itself and the new manifest.
 names=sorted(set([str(f.relative_to(P)) for f in files()]+['REPOSITORY_TREE.md','FILE_MANIFEST.json']))
 (P/'REPOSITORY_TREE.md').write_text('# 实际文件清单 / Repository tree\n\n排除缓存、构建产物和.git；精确hash见FILE_MANIFEST.json。\n\n```text\nlongevity_research_workbench/\n'+''.join('  '+n+'\n' for n in names)+'```\n')
 manifest={str(f.relative_to(P)):digest(f.read_bytes()) for f in files() if f.name!='FILE_MANIFEST.json'}
 # Only the ROOT manifest is self-excluded; upstream manifest was intentionally not copied.
 (P/'FILE_MANIFEST.json').write_text(json.dumps({'algorithm':'sha256','self_excluded':True,'files':manifest},ensure_ascii=False,indent=2)+'\n')
 dest=P.parent/'Longevity_Research_Workbench_0.1.0.zip'
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
  for f in files():
   info=zipfile.ZipInfo(P.name+'/'+str(f.relative_to(P)),date_time=(2026,11,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,f.read_bytes())
 with zipfile.ZipFile(dest) as z:
  crc=z.testzip();assert crc is None
  for name,h in manifest.items():assert digest(z.read(P.name+'/'+name))==h
  members=len(z.namelist())
  with tempfile.TemporaryDirectory() as td:
   z.extractall(td);root=Path(td)/P.name
   r=subprocess.run([sys.executable,'tools/run_validation.py'],cwd=root,capture_output=True,text=True,timeout=120)
   if r.returncode:raise RuntimeError(r.stdout+r.stderr)
   smoke=json.loads((root/'artifacts/VALIDATION.json').read_text());assert smoke['all_software_checks_passed']
 receipt={'zip_name':dest.name,'bytes':dest.stat().st_size,'sha256':digest(dest.read_bytes()),'members':members,'manifest_file_count':len(manifest),'zip_crc_ok':crc is None,'all_manifest_hashes_verified':True,
          'extracted_validation':smoke,'scope':'Local private-candidate handoff; no remote push, no new independent review, no scientific certification.'}
 out=P.parent/'Longevity_Research_Workbench_0.1.0_交付回执.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
