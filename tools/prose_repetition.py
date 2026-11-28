#!/usr/bin/env python3
"""Template-repetition diagnostic for manuscript chapters (playbook R3.8 section 7G, item 1).

For each chapter draft, this tool reports the share of body sentences that also appear, after
normalisation, in at least K other chapters (default K=3, as in the playbook). It also lists the most
repeated sentences, so that shared method text can be moved to one place and cited.

Status: diagnostic only. It never blocks, never scores "AI style" and is not an AI detector (section
7G item 3). A low number does not mean the prose is good. The fix for a high number is structural
(write what is specific to the chapter, or move shared text to one place). Paraphrasing a sentence to
make it unique is not a fix (section 7G item 2).

Usage: python tools/prose_repetition.py [--k 3] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOBS = {'zh': 'books/manuscript/CH*_*.md', 'en': 'books/manuscript/en/CH*_*.md'}
MIN_CHARS = {'zh': 12, 'en': 40}
SPLIT = {'zh': re.compile(r'(?<=[。！？；])'), 'en': re.compile(r'(?<=[.!?;])\s+')}


def body_sentences(text: str, lang: str):
    out = []
    for block in text.split('\n\n'):
        b = block.strip()
        if not b or b.startswith(('#', '>', '|', '```', '- **', '*')) or b.startswith('---'):
            continue
        for s in SPLIT[lang].split(' '.join(b.split())):
            norm = re.sub(r'[\s\W_]+', '', s.lower())
            if len(norm) >= MIN_CHARS[lang]:
                out.append((norm, s.strip()))
    return out


def analyse(root: Path = ROOT, k: int = 3):
    report = {}
    for lang, pattern in GLOBS.items():
        files = sorted(root.glob(pattern))
        sents = {f: body_sentences(f.read_text(encoding='utf-8'), lang) for f in files}
        where = defaultdict(set)
        sample = {}
        for f, ss in sents.items():
            for norm, raw in ss:
                where[norm].add(f)
                sample.setdefault(norm, raw)
        chapters = []
        for f, ss in sents.items():
            rep = sum(1 for norm, _ in ss if len(where[norm] - {f}) >= k)
            chapters.append({'file': str(f.relative_to(root)), 'sentences': len(ss), 'repeated': rep,
                             'share': round(rep / len(ss), 3) if ss else None})
        shares = sorted(c['share'] for c in chapters if c['share'] is not None)
        top = sorted(((len(v), sample[n]) for n, v in where.items() if len(v) > 1), reverse=True)[:10]
        report[lang] = {'chapters': chapters, 'k_other_chapters': k,
                        'median_share': shares[len(shares) // 2] if shares else None,
                        'comparable': len(files) > k,
                        'most_repeated': [{'chapters': c, 'sentence': s[:160]} for c, s in top]}
    report['status'] = 'diagnostic; never blocks; not an AI detector'
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--k', type=int, default=3)
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    r = analyse(k=a.k)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return
    for lang in GLOBS:
        d = r[lang]
        note = '' if d['comparable'] else f' (fewer than {a.k + 1} chapters: share cannot exceed 0)'
        print(f"[{lang}] median share repeated in >= {a.k} other chapters: {d['median_share']}{note}")
        for c in d['chapters']:
            print(f"  {c['file']}: {c['repeated']}/{c['sentences']}")
        for m in d['most_repeated'][:5]:
            print(f"  x{m['chapters']}: {m['sentence']}")
    print(r['status'])


if __name__ == '__main__':
    main()
