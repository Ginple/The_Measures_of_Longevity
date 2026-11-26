"""Local packaging self-check only. Does not validate scientific claims."""
from pathlib import Path
import csv, hashlib, json, re
P=Path(__file__).resolve().parent
checks=[]
def check(label,ok):
    assert ok,label
    checks.append(label)
expected={'README.md','修好这一次_还剩多少下一次.md','READING_RECORD.md','EVIDENCE_MAP.csv','audit_package.py'}
check('required content files',all((P/n).is_file() for n in expected))
with (P/'EVIDENCE_MAP.csv').open(newline='') as f: rows=list(csv.DictReader(f))
check('six distinct evidence entries',len(rows)==6 and len({r['id'] for r in rows})==6)
check('all source URLs use https',all(r['url'].startswith('https://') for r in rows))
record=(P/'READING_RECORD.md').read_text()
check('source IDs and URLs appear in reading record',all(r['id'] in record and r['url'] in record for r in rows))
check('preprint explicitly classified',sum('preprint' in r['evidence_status'].lower() for r in rows)==1)
links=[]
for f in P.glob('*.md'):
    for u in re.findall(r'\]\(([^)]+)\)',f.read_text()):
        if '://' not in u and not u.startswith('#'):
            links.append(u)
            check('local link: '+f.name+' -> '+u,(f.parent/u.split('#')[0]).exists())
check('no html or zip generated',not any(f.suffix.lower() in {'.html','.zip'} for f in P.iterdir()))
report={'scope':'local structure and provenance consistency only; not scientific verification',
        'checks_passed':len(checks),'checks':checks,'source_rows':len(rows),
        'independent_review_completed':False,
        'sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in sorted(expected)}}
(P/'SELF_CHECK.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'independent_review_completed':False}))
