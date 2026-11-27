"""Read-only verification against the existing local-history baseline; NEVER refresh it."""
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parents[1]

def main():
 root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else P.parent
 baseline=json.loads((P/'governance/history_before.json').read_text())
 changed=[];missing=[]
 for name,expected in baseline.items():
  f=root/name
  if not f.is_file():missing.append(name)
  elif hashlib.sha256(f.read_bytes()).hexdigest()!=expected:changed.append(name)
 manuscripts=[]
 for name in ['longevity_v6/长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md','longevity_v7/长寿研究_V7_谁在变年轻.md']:
  old=root/name;folder='longevity_v6' if 'longevity_v6' in name else 'longevity_v7';new=P/'corpus'/folder/old.name
  manuscripts.append({'original':name,'copy':str(new.relative_to(P)),'byte_identical':old.is_file() and new.is_file() and new.read_bytes()==old.read_bytes()})
 out={'baseline_file_count':len(baseline),'changed':changed,'missing':missing,'manuscript_snapshots':manuscripts,
      'status':'verified_unchanged' if not changed and not missing and all(x['byte_identical'] for x in manuscripts) else 'not_verified',
      'scope':'Byte integrity only, not full reading, scientific validity or external review. Original files must be locally available.'}
 print(json.dumps(out,ensure_ascii=False,indent=2));return 0 if out['status']=='verified_unchanged' else 1
if __name__=='__main__':raise SystemExit(main())
