"""Verify original session history. Never recreates baseline, never treats missing as pass."""
from pathlib import Path
import hashlib
import json
P = Path(__file__).resolve().parents[1]

def main():
    before = json.loads((P/'session/history_before.json').read_text())
    missing, changed = [], []
    for name, expected in before.items():
        f = P.parent/name
        if not f.exists():
            missing.append(name)
        elif hashlib.sha256(f.read_bytes()).hexdigest() != expected:
            changed.append(name)
    out = {'historical_files':len(before),'changed':changed,'missing':missing,
           'status':'verified_unchanged' if not changed and not missing else 'not_verified',
           'scope':'Session byte integrity, not content review or scientific certification.'}
    (P/'results/HISTORY_INTEGRITY.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0 if out['status']=='verified_unchanged' else 2

if __name__ == '__main__':
    raise SystemExit(main())
