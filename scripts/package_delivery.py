from pathlib import Path
import hashlib
import json
import zipfile
P = Path(__file__).resolve().parents[1]
OUT = P.parent/'Research_Assurance_Toolkit_证据约束型研究工程_0.1.0.zip'
EXCLUDED={'__pycache__','build','dist','.git','.pytest_cache'}

def include(path):
    return path.is_file() and not any(x in EXCLUDED or x.endswith('.egg-info') for x in path.relative_to(P).parts) and path.name!='FILE_MANIFEST.json'

def main():
    files=sorted(f for f in P.rglob('*') if include(f))
    assert not any(f.suffix.lower()=='.html' for f in files),'new_dashboard_forbidden_by_user'
    sha=lambda b:hashlib.sha256(b).hexdigest()
    manifest={f.relative_to(P).as_posix():{'bytes':f.stat().st_size,'sha256':sha(f.read_bytes())} for f in files}
    (P/'FILE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    files.append(P/'FILE_MANIFEST.json')
    with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in sorted(files):
            z.write(f, 'research_assurance_toolkit/'+f.relative_to(P).as_posix())
    with zipfile.ZipFile(OUT) as z:
        assert z.testzip() is None
        for name,row in manifest.items():assert sha(z.read('research_assurance_toolkit/'+name))==row['sha256']
        count=len(z.namelist())
    receipt={'file':OUT.name,'bytes':OUT.stat().st_size,'sha256':sha(OUT.read_bytes()),'files':count,'manifest_entries':len(manifest),'CRC_ok':True,'manifest_hashes_verified':True,'new_html_files':0,'remote_repository_created_or_pushed':False,'meaning':'delivery integrity only, not scientific certification'}
    (P.parent/'Research_Assurance_Toolkit_0.1.0_交付回执.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
