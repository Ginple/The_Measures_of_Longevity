#!/usr/bin/env python3
"""Deterministic audit agent for the post-positioning restructure (DEC-018).

What it is
    A V1 verifier (playbook R3.8 section 3.3): formal and deterministic checks of properties that the L1
    receipt asserts, or that the protocol and the frozen L2 packet require. It does not read the L1 receipt's
    reasoning when computing a result. Phase 1 computes facts from the frozen inputs; phase 2 compares each
    computed fact with the receipt's claim ID, so a wrong claim in the receipt shows up as a mismatch.

What it is not
    It is not peer review, not an independent model judgement (V4) and not a human review. It cannot judge
    whether a K3 restructure is warranted; it only checks encoded properties. A clean run does not close
    D05.

Isolation (playbook section 7B.6)
    Every run copies its inputs into a fresh, uniquely named scratch directory and reads only those copies.
    The run fails if an input is missing (fail closed).

Non-vacuity (playbook section 3.6)
    `--self-test` mutates scratch copies (inserts a banned word, deletes a slot, drops a ledger row, and so on)
    and requires that each targeted check then fails.

Standard library only. Usage:
    python tools/restructure_audit_agent.py            # print JSON receipt
    python tools/restructure_audit_agent.py --write    # also write review/RESTRUCTURE_AUDIT_AGENT_RECEIPT.json
    python tools/restructure_audit_agent.py --self-test
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'review/RESTRUCTURE_AUDIT_AGENT_RECEIPT.json'
M = 'books/manuscript/'
INPUTS = [
    M + 'outline_v1.json', M + 'OUTLINE_v1.md', M + 'outline_build.py',
    M + 'CH01_长寿的五个问题_示范稿.md', M + 'en/CH05_measurement_contracts_draft_en.md',
    M + 'en/README.md', M + 'en/DETAILED_OUTLINE_SPEC.md', M + 'en/DETAILED_OUTLINE_VOL1.md',
    'knowledge_base/KERNEL.md', 'knowledge_base/MASTER.md', 'knowledge_base/CLAIM_LEDGER.md',
    'books/BOOK_PROPOSAL.md', 'books/market/MARKET_POSITIONING_2026-11.md',
    'review/MARKET_RESTRUCTURE_AUDIT_PROTOCOL_2026-11-27.md',
    'review/MARKET_RESTRUCTURE_AUDIT_PACKET_L2_2026-11-27.md',
]
PACKET = 'review/MARKET_RESTRUCTURE_AUDIT_PACKET_L2_2026-11-27.md'
PROTOCOL = 'review/MARKET_RESTRUCTURE_AUDIT_PROTOCOL_2026-11-27.md'
RECEIPT = 'review/MARKET_RESTRUCTURE_AUDIT_RECEIPT_L1_2026-11-27.md'
PREREG_COMMIT = 'e20d915'
BANNED = ['首次', '首个', '填补空白', 'first framework', 'fills the gap', 'fill the gap']
REQUIRED_FIELDS = ['Readers and questions', 'Owns', 'Uses', 'Sections', 'Candidate evidence',
                   'Strongest counterexample', 'Not answered here', 'To appendix or paper']
SCHEME_A = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ']


def stage(root: Path) -> Path:
    scratch = Path(tempfile.mkdtemp(prefix='restructure_audit_agent_'))
    for rel in INPUTS:
        src = root / rel
        if not src.is_file():
            raise FileNotFoundError(f'missing audit input (fail closed): {rel}')
        dst = scratch / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return scratch


def read(s: Path, rel: str) -> str:
    return (s / rel).read_text(encoding='utf-8')


def table_rows(text: str):
    for line in text.splitlines():
        if line.startswith('|') and not set(line.replace('|', '').strip()) <= set('-: '):
            yield [c.strip() for c in line.strip().strip('|').split('|')]


def outline_sections(text: str):
    """Split the detailed outline into {key: {field: content}} keyed 'F1' or chapter number."""
    out, key = {}, None
    for line in text.splitlines():
        m = re.match(r'^## (F1|Chapter (\d+)) ·', line)
        if m:
            key = m.group(2) and int(m.group(2)) or 'F1'
            out[key] = {}
        elif key is not None and line.startswith('| ') and not line.startswith('| Field') and not line.startswith('| Route'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) >= 2 and not set(cells[0]) <= set('-: '):
                out[key][cells[0]] = cells[1]
    return out


def check(cid, claim, ok, detail):
    return {'id': cid, 'receipt_claim': claim, 'result': 'PASS' if ok else 'FAIL', 'detail': detail}


def run_checks(s: Path, root: Path = ROOT, git: bool = True):
    res = []
    data = json.loads(read(s, M + 'outline_v1.json'))
    ch = data['chapters']
    nums = [c['n'] for c in ch]
    res.append(check('A01', 'O2: 33 chapters, 8 parts, 3 volumes, order unchanged',
                     nums == list(range(1, 34)) and len({c['part'] for c in ch}) == 8
                     and len({c['volume'] for c in ch}) == 3, f'chapters={len(ch)}'))
    v3 = sum(c['volume'] == 'Ⅲ' for c in ch) / len(ch)
    res.append(check('A02', 'V2: Volume III chapter share >= 28%', v3 >= 0.28, f'{v3:.3f}'))
    matter = data.get('matter', [])
    ids = {m['id']: m for m in matter}
    ok = (ids.get('F1', {}).get('position') == 'front'
          and all(ids.get(b, {}).get('position') == 'back' for b in ['B1', 'B2', 'B3', 'B4'])
          and not any(k in {str(n) for n in nums} for k in ids))
    res.append(check('A03', 'O2/F-01/F-12: slots F1 (front) and B1-B4 (back), not numbered chapters', ok, sorted(ids)))
    b2 = ids.get('B2', {}).get('purpose', '').lower()
    res.append(check('A04', 'V3: B2 is questions only, never thresholds', 'never thresholds' in b2, b2[:80]))
    f1 = ids.get('F1', {}).get('purpose', '')
    res.append(check('A05', 'O7 RT-E: F1 scene must differ from the chapter 5 opening', 'differ from the chapter 5' in f1, f1[:120]))
    build = read(s, M + 'outline_build.py')
    res.append(check('A06', "F-01: DEC-011 budget has a 'frame' entry", re.search(r"'frame':\s*20_000", build) is not None, 'BUDGET frame'))
    ch01 = read(s, M + 'CH01_长寿的五个问题_示范稿.md')
    res.append(check('A07', 'F-01: chapter 1 demo declares it is not the book introduction', '不是全书导论' in ch01[:600], 'CH01 header'))
    ch05 = read(s, M + 'en/CH05_measurement_contracts_draft_en.md')
    body = [p for p in ch05.split('\n\n') if p and not p.startswith(('#', '>'))]
    res.append(check('A08', 'F-01: the reader-report scene opens chapter 5', bool(body) and 'biological age' in body[0], body[0][:80] if body else ''))
    om = read(s, M + 'OUTLINE_v1.md')
    master = read(s, 'knowledge_base/MASTER.md')
    enr = read(s, M + 'en/README.md')
    prop = read(s, 'books/BOOK_PROPOSAL.md')
    stale = []
    if '预算约' in om:
        stale.append('OUTLINE 预算约')
    if re.search(r'^6\. 全书 25–35 万字', master, re.M):
        stale.append('MASTER §2.6 current budget')
    if re.search(r'drafted towards about 4,500 words', enr):
        stale.append('en/README 4,500 target')
    if '待作者裁决）。本文件保留为历史提案' in prop:
        stale.append('BOOK_PROPOSAL stale authority banner')
    res.append(check('A09', 'F-04/F-10: no stale length targets or authority banners', not stale, stale))
    kernel = read(s, 'knowledge_base/KERNEL.md')
    bad = []
    for row in table_rows(kernel):
        if len(row) >= 4 and row[0] not in ('主题', 'ID', '#', '方案 A 部号'):
            cells = [row[2]] + row[4:]  # allowed interpretation and relation/ledger columns, not 'misreading'
            bad += [f'{row[0]}: {w}' for w in BANNED for c in cells if w in c]
    res.append(check('A10', 'F-06: no banned novelty words in KERNEL allowed-interpretation/relation cells', not bad, bad))
    refs = set(re.findall(r'第([ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪ])部', kernel)) | set(re.findall(r'书第([ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪ])', kernel))
    mapped = {r[0].split(' ')[0] for r in table_rows(kernel) if r and r[0].split(' ')[0] in SCHEME_A}
    res.append(check('A11', 'F-05: every Scheme-A part numeral used in KERNEL is in the mapping table',
                     bool(mapped) and refs <= mapped, {'used': sorted(refs), 'unmapped': sorted(refs - mapped)}))
    t9 = next(c['title_en'] for c in ch if c['n'] == 9)
    t22 = next(c['title_en'] for c in ch if c['n'] == 22)
    res.append(check('A12', 'F-07: reserve is the English term in KERNEL and in chapter 9/22 titles',
                     '**reserve**' in kernel and 'Reserve' in t9 and 'Reserve' in t22, [t9, t22]))
    spec = read(s, M + 'en/DETAILED_OUTLINE_SPEC.md')
    own_rows = [r for r in table_rows(spec) if len(r) == 3 and r[0] != 'Concept, invariant or case']
    owners, bad_refs = {}, []
    for concept, owner, used in own_rows:
        for n in re.findall(r'\d+', owner):
            owners.setdefault(int(n), []).append(concept)
        for tok in re.findall(r'\b(F1|\d+)\b', owner + ' ' + used):
            if tok != 'F1' and not 1 <= int(tok) <= 33:
                bad_refs.append(tok)
    unowned = [n for n in range(1, 34) if n not in owners]
    res.append(check('A13', 'F-03: concept-ownership table names only chapters 1-33 or F1', not bad_refs, bad_refs))
    res.append(check('A14', 'F-02 (diagnostic): every chapter owns at least one concept', not unowned, {'chapters_owning_nothing': unowned}))
    vol1 = read(s, M + 'en/DETAILED_OUTLINE_VOL1.md')
    secs = outline_sections(vol1)
    missing_ch = [k for k in ['F1'] + list(range(1, 10)) if k not in secs]
    res.append(check('A15', 'O4: detailed outline covers F1 and chapters 1-9', not missing_ch, missing_ch))
    gaps = {}
    for k in range(1, 10):
        fields = secs.get(k, {})
        miss = [f for f in REQUIRED_FIELDS if not any(x.startswith(f) for x in fields)]
        if not any(x.startswith(('Gaps', 'Source state')) for x in fields):
            miss.append('Gaps or Source state')
        if miss:
            gaps[k] = miss
    res.append(check('A16', 'Spec section 2: every chapter entry has the required fields', not gaps, gaps))
    ledger = read(s, 'knowledge_base/CLAIM_LEDGER.md')
    have = set(re.findall(r'^\| (X\d+) \|', ledger, re.M))
    cited = set(re.findall(r'\bX\d{2,3}\b', vol1 + spec))
    res.append(check('A17', 'Candidate evidence: every cited ledger ID exists', cited <= have, sorted(cited - have)))
    mism = []
    for k in range(1, 10):
        for inv in re.findall(r'\bI(\d{1,2})\b', secs.get(k, {}).get('Owns', '')):
            row = next((r for r in own_rows if re.search(rf'\bI{inv}\b', r[0])), None)
            if row is None or str(k) not in re.findall(r'\d+', row[1]):
                mism.append(f'ch{k} owns I{inv}; spec owner: {row[1] if row else "none"}')
    res.append(check('A18', 'F-03: invariants owned in Vol I outline match the ownership table', not mism, mism))
    rules = [n for n in range(7, 11) if re.search(rf'^{n}\. \*\*', enr, re.M)]
    res.append(check('A19', 'O6: English writing rules 7-10 present', rules == [7, 8, 9, 10], rules))
    banned_hits = [w for w in BANNED for t in (vol1, spec) if w in t]
    res.append(check('A20', 'Market section 4 / X137: no banned novelty words in the new planning files', not banned_hits, banned_hits))
    dec = all(f'| {d} |' in master for d in ['DEC-017', 'DEC-018'])
    xs = all(f'| {x} |' in ledger for x in ['X157', 'X158', 'X159'])
    sup = re.search(r'^\| X147 \|.*superseded', ledger, re.M) is not None
    res.append(check('A21', 'DEC-017/018 recorded; X157-X159 exist; X147 superseded', dec and xs and sup, {'dec': dec, 'x': xs, 'x147': sup}))
    hours = (200_000 / 155 / 60, 200_000 / 150 / 60)
    res.append(check('A22', 'F-14: 200k words at 150-155 wpm is about 21-22 hours', 21 <= hours[0] and hours[1] < 23, [round(h, 2) for h in hours]))
    prot = read(s, PROTOCOL)
    res.append(check('A23', 'Protocol section 3 rule 1: B/C market evidence caps at K2', '最高只能支持 K2' in prot, 'rule 1'))
    pk = read(s, PACKET)
    persona = {r[0].split(' ')[0]: chapters_in(r[-1]) for r in table_rows(pk) if re.match(r'R[1-4]\b', r[0])}
    routes = {r[1]: chapters_in(r[2]) for r in table_rows(vol1) if len(r) == 3 and re.fullmatch(r'R[1-4]', r[1])}
    diff = {k: sorted(v - routes.get(k, set())) for k, v in persona.items() if v - routes.get(k, set())}
    res.append({'id': 'D01', 'receipt_claim': 'F-09 (diagnostic): F1 reading routes cover the packet persona-to-chapter map',
                'result': 'PASS' if not diff else 'DIFF', 'detail': {'packet_chapters_not_on_route': diff,
                'note': 'DIFF is not a failure; each difference needs a recorded disposition'}})
    if git:
        res.extend(git_checks(s, root))
    return res


def chapters_in(text: str) -> set:
    out = set()
    for a, b in re.findall(r'(\d+)\s*[–-]\s*(\d+)', text):
        out |= set(range(int(a), int(b) + 1))
    text = re.sub(r'(\d+)\s*[–-]\s*(\d+)', ' ', text)
    out |= {int(n) for n in re.findall(r'\b(\d+)\b', text) if 1 <= int(n) <= 33}
    return out


def git_checks(s: Path, root: Path):
    out = []

    def first_commit(rel):
        r = subprocess.run(['git', '-C', str(root), 'log', '--diff-filter=A', '--format=%H', '--', rel],
                           capture_output=True, text=True)
        hs = r.stdout.split()
        return hs[-1] if hs else None

    p, rcp = first_commit(PROTOCOL), first_commit(RECEIPT)
    order = False
    if p and rcp:
        r = subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', p, rcp])
        order = r.returncode == 0 and p != rcp
    out.append(check('G01', 'Pre-registration: protocol committed before the receipt', order,
                     {'protocol': (p or '')[:7], 'receipt': (rcp or '')[:7]}))
    r = subprocess.run(['git', '-C', str(root), 'show', f'{PREREG_COMMIT}:{PACKET}'], capture_output=True)
    frozen = r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest() == hashlib.sha256((s / PACKET).read_bytes()).hexdigest()
    out.append(check('G02', 'L2 packet bytes unchanged since pre-registration', frozen, PREREG_COMMIT))
    return out


def summarize(res, scratch):
    fails = [r['id'] for r in res if r['result'] == 'FAIL']
    diffs = [r['id'] for r in res if r['result'] == 'DIFF']
    return {'agent': 'tools/restructure_audit_agent.py', 'verifier_level': 'V1 (deterministic; encoded properties only)',
            'not': ['peer review', 'independent model judgement (V4)', 'human review', 'closure of D05'],
            'inputs_sha256': {rel: hashlib.sha256((scratch / rel).read_bytes()).hexdigest() for rel in INPUTS},
            'checks': res, 'failed': fails, 'diagnostic_differences': diffs,
            'passed': len(res) - len(fails) - len(diffs), 'total': len(res)}


def self_test():
    """Each mutation must make its targeted check fail (non-vacuity)."""
    mutations = {
        'A10': ('knowledge_base/KERNEL.md', lambda t: t.replace('| PAI-1 药理抑制与时钟变化的直接', '| 首次 PAI-1 药理抑制与时钟变化的直接', 1)),
        'A09': (M + 'OUTLINE_v1.md', lambda t: t + '\n预算约 90k\n'),
        'A17': (M + 'en/DETAILED_OUTLINE_VOL1.md', lambda t: t + '\nX999\n'),
        'A16': (M + 'en/DETAILED_OUTLINE_VOL1.md', lambda t: re.sub(r'\| Strongest counterexample \|[^\n]*\n', '', t)),
        'A19': (M + 'en/README.md', lambda t: t.replace('8. **Audio-ready', '8. Audio-ready')),
        'A20': (M + 'en/DETAILED_OUTLINE_SPEC.md', lambda t: t + '\nThis is the first framework.\n'),
        'A11': ('knowledge_base/KERNEL.md', lambda t: t.replace('| Ⅷ 环境 |', '| (removed) |')),
    }
    report = {}
    for cid, (rel, fn) in mutations.items():
        scratch = stage(ROOT)
        try:
            p = scratch / rel
            before = p.read_text(encoding='utf-8')
            after = fn(before)
            if after == before:
                report[cid] = 'MUTATION_NOT_APPLIED'
                continue
            p.write_text(after, encoding='utf-8')
            r = next(x for x in run_checks(scratch, git=False) if x['id'] == cid)
            report[cid] = 'DETECTED' if r['result'] == 'FAIL' else 'MISSED'
        finally:
            shutil.rmtree(scratch, ignore_errors=True)
    return report


def main(argv):
    if '--self-test' in argv:
        rep = self_test()
        print(json.dumps(rep, indent=2))
        return 0 if all(v == 'DETECTED' for v in rep.values()) else 1
    scratch = stage(ROOT)
    try:
        receipt = summarize(run_checks(scratch), scratch)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    text = json.dumps(receipt, ensure_ascii=False, indent=2) + '\n'
    if '--write' in argv:
        OUT.write_text(text, encoding='utf-8')
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
