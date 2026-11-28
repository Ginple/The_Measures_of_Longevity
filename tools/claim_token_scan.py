"""Find numbers and capitalised words in bound claim text that its bound evidence does not contain.

Why: the span check confirms that a claim's anchor is in the chapter and that its evidence excerpts exist.
It does not check that every word of the claim is supported. On 2026-11-28 this let through "German",
"overnight", "Canadian", "New Zealand", authors' first names and "4,058 people" (source: samples).

What it does: for every claim in the English-first pilots (chapters 6-9), list
- numbers in the claim that do not occur in its bound evidence text;
- capitalised words of 4+ letters that do not occur in its bound evidence text,
and compare the result with REVIEWED, a per-claim record of tokens a person (here: the drafting assistant)
has looked at and judged acceptable, with the reason.
Anything new fails `--check` until it is reviewed. A clean result means only "no unreviewed token";
it does not mean the claim is right. Supported-but-paraphrased wording is invisible to this scan.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PILOTS = ['ch06_level_en', 'ch07_rate_en', 'ch08_recovery_en', 'ch09_reserve_en']
NUM = re.compile(r'(?<![\w.])\d+(?:[.,]\d+)*')
CAP = re.compile(r'\b[A-Z][a-z]{3,}\b')

# Reason codes: Y = year of publication (in the footnote/header); X = cross-reference to a chapter of this book;
# S = sentence-initial or ordinary word; A = arithmetic on bound numbers (stated in the rationale);
# H = from the evidence-file header (bibliographic metadata recorded at fetch time, not a quote);
# M = synthetic-model input or output written differently in the text (25 vs 25.0, 0.572 as "57 in 100");
# W = number spelled out in the evidence ("Sixty-nine").
REVIEWED = {
    'CH6-EN-C001': {'Return': 'S'},
    'CH6-EN-C002': {'2022': 'Y', 'That': 'S', 'Third': 'S'},
    'CH6-EN-C003': {'2026': 'Y'},
    'CH6-EN-C004': {'2026': 'Y'},
    'CH6-EN-C005': {'2025': 'Y', 'That': 'S', 'These': 'S'},
    'CH6-EN-C006': {'Telomere': 'S', 'Whether': 'S'},
    'CH6-EN-C007': {'100': 'M', '57': 'M', '91.7': 'M', '89.8': 'M'},
    'CH6-EN-C008': {'Composition': 'S', 'Read': 'S', 'What': 'S', 'Whether': 'S'},
    'CH7-EN-C001': {'Researchers': 'S'},
    'CH7-EN-C002': {'6': 'X', 'Telomeres': 'S'},
    'CH7-EN-C003': {'Researchers': 'S'},
    'CH7-EN-C004': {'Californians': 'H', 'Stanford': 'H'},
    'CH7-EN-C005': {'Singapore': 'H'},
    'CH7-EN-C006': {'Several': 'S'},
    'CH7-EN-C008': {'States': 'H', 'Three': 'S', 'United': 'H', 'Yale': 'H'},
    'CH7-EN-C009': {'Across': 'S'},
    'CH7-EN-C010': {'80': 'A', '70': 'A', 'Clocks': 'S'},
    'CH8-EN-C001': {'2008': 'Y', 'Geriatricians': 'S', 'Hopkins': 'H', 'Johns': 'H'},
    'CH8-EN-C002': {'2026': 'Y', 'There': 'S'},
    'CH8-EN-C003': {'69': 'W', 'Irish': 'H'},
    'CH8-EN-C004': {'Researchers': 'S'},
    'CH8-EN-C006': {'Five': 'S', 'Using': 'S'},
    'CH8-EN-C008': {'6': 'X'},
    'CH9-EN-C001': {'Later': 'S'},
    'CH9-EN-C002': {'After': 'S'},
    'CH9-EN-C003': {'16': 'A', '24': 'A', 'First': 'S', 'Second': 'S'},
    'CH9-EN-C004': {'They': 'S'},
    'CH9-EN-C006': {'7': 'X', '810': 'A', 'Three': 'S'},
    'CH9-EN-C007': {'25': 'M', '18': 'M', 'Take': 'S'},
    'CH9-EN-C008': {'25': 'M', '35': 'M', 'Neither': 'S'},
    'CH9-EN-C009': {'10': 'M', '20': 'M', '25': 'M', '38': 'M', 'Slowing': 'S'},
    'CH9-EN-C010': {'6': 'X', '9': 'X', '302,467': 'H', 'Canadian': 'H', 'That': 'S'},
    'CH9-EN-C011': {'6': 'X', '8': 'X', 'Only': 'S', 'Their': 'S', 'Which': 'S', 'With': 'S'},
}


def norm(x):
    return x.replace(',', '')


def scan():
    out = {}
    for p in PILOTS:
        d = json.loads((ROOT / 'knowledge_base/pilots' / p / 'project.json').read_text(encoding='utf-8'))
        ev = {e['id']: e['text'] for e in d['evidence']}
        for c in d['claims']:
            text = re.sub(r'\[\^\d+\]', '', c['text'])
            evt = ' '.join(ev[i] for i in c['evidence_ids'])
            evn = {norm(x) for x in NUM.findall(evt)}
            toks = sorted({x for x in NUM.findall(text) if norm(x) not in evn} |
                          {w for w in CAP.findall(text) if w not in evt})
            if toks:
                out[c['id']] = toks
    return out


def unreviewed(found):
    return {cid: [t for t in toks if t not in REVIEWED.get(cid, {})]
            for cid, toks in found.items() if any(t not in REVIEWED.get(cid, {}) for t in toks)}


def stale_reviews(found):
    return {cid: [t for t in toks if t not in found.get(cid, [])]
            for cid, toks in REVIEWED.items() if any(t not in found.get(cid, []) for t in toks)}


if __name__ == '__main__':
    found = scan()
    new, stale = unreviewed(found), stale_reviews(found)
    print(json.dumps({'unreviewed': new, 'reviewed_but_gone': stale}, indent=1, ensure_ascii=False))
    if '--check' in sys.argv:
        sys.exit(1 if new or stale else 0)
