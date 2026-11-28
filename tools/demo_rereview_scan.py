"""Mechanical scan behind the 2026-11-28 re-review of the seven stale Chinese demo drafts.

This is a software check, not a scientific review. It lists what a reviewer must look at in each draft:
- chapter cross-references and relative pointers ("next chapter");
- paper labels;
- ledger IDs, with their current status in CLAIM_LEDGER;
- watch-list terms (priority claims, rejuvenation and lifespan wording), with context, for a human to judge negation;
- whether the re-review note and the external-review status are present.
The human judgements live in review/DEMO_DRAFTS_REREVIEW_2026-11-28.md. Run with --check to compare against the stored receipt.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review/DEMO_DRAFTS_REREVIEW_SCAN_2026-11-28.json'
M = 'books/manuscript/'
# file -> (scheme-A chapter number, OUTLINE_v1 chapter number)
DRAFTS = {
    'CH01_长寿的五个问题_示范稿.md': (1, 1),
    'CH19_谁替谁维护_示范稿.md': (19, 21),
    'CH20_平均不等于及时_示范稿.md': (20, 21),
    'CH21_有余量却用不上_示范稿.md': (21, 22),
    'CH22_清除之后谁来接班_示范稿.md': (22, 19),
    'CH23_状态还在细胞换了吗_示范稿.md': (23, 15),
    'CH24_修好这一次还剩多少下一次_示范稿.md': (24, 17),
}
WATCH = ['首次', '首个', '首创', '填补空白', '返老还童', '寿命上限', '已证明安全', '逆转衰老', '抗衰', '延寿', '变年轻']
RELATIVE = ['下一章', '上一章', '前一章', '后一章']
CN = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}


def cn_number(s):
    if s.isdigit():
        return int(s)
    if s == '十':
        return 10
    if s.startswith('十'):
        return 10 + CN[s[1]]
    if '十' in s:
        a, _, b = s.partition('十')
        return CN[a] * 10 + (CN[b] if b else 0)
    return CN[s]


def ledger_status():
    text = (ROOT / 'knowledge_base/CLAIM_LEDGER.md').read_text(encoding='utf-8')
    out = {}
    for m in re.finditer(r'^\| (X\d+) \|(.*)$', text, re.M):
        cells = [c.strip() for c in m.group(2).strip().strip('|').split('|')]
        out[m.group(1)] = cells[-1] if cells else ''
    return out


def scan_one(name, status):
    text = (ROOT / M / name).read_text(encoding='utf-8')
    lines = text.split('\n')
    refs, relative, watch = [], [], []
    for i, line in enumerate(lines, 1):
        if i == 1 or '2026-11-28 重审' in line:
            continue
        for m in re.finditer(r'第\s*([0-9]+|[一二三四五六七八九十]+)\s*章', line):
            refs.append({'line': i, 'n': cn_number(m.group(1)), 'marked_old': '旧' in line[max(0, m.start() - 2):m.end() + 14]})
        for r in RELATIVE:
            if r in line:
                relative.append({'line': i, 'term': r})
        for w in WATCH:
            for m in re.finditer(w, line):
                watch.append({'line': i, 'term': w, 'context': line[max(0, m.start() - 12):m.end() + 12]})
    ids = sorted(set(re.findall(r'\bX\d+\b', text)), key=lambda x: int(x[1:]))
    return {
        'file': M + name, 'scheme_a_chapter': DRAFTS[name][0], 'outline_v1_chapter': DRAFTS[name][1],
        'heading': lines[0],
        'chapter_refs': refs, 'relative_refs': relative,
        'paper_labels': sorted(set(re.findall(r'\bP[1-5]\b', text))),
        'ledger_ids': {x: status.get(x, 'MISSING') for x in ids},
        'watch_terms': watch,
        'has_rereview_note': '2026-11-28 重审' in text,
        'has_external_review_status': '独立外审未开展' in text,
    }


def build():
    status = ledger_status()
    return {'scope': 'seven stale Chinese demo drafts (DEC-011 impact record)',
            'drafts': [scan_one(n, status) for n in DRAFTS],
            'warning': 'Mechanical listing for a human reviewer; a hit is not an error and a clean scan is not a scientific review.'}


if __name__ == '__main__':
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if OUT.exists() and json.loads(OUT.read_text(encoding='utf-8')) == data else 1)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(OUT.relative_to(ROOT), sum(len(d['chapter_refs']) for d in data['drafts']), 'chapter refs')
