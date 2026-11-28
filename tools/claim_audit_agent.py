#!/usr/bin/env python3
"""Deterministic audit agent for the bound claims of the English chapter drafts (DEC-020).

What it is
    A V1 verifier (see docs/VERIFICATION_AND_DISCLOSURE.md): formal, deterministic checks run over staged
    copies of every English chapter pilot (project.json, the chapter draft and every bound artifact). It reads
    nothing the drafting assistant wrote about its own checks (no receipts, no rationales as input to a result).

What it checks, per pilot
    C01 integrity      inspect_project: schema valid, no issues, no artifact drift, no stale claims.
    C02 tokens         every number and capitalised word in a claim that its evidence lacks has a reviewed
                       reason in tools/claim_token_scan.py, and no reviewed token has gone stale.
    C03 citations      every PubMed ID cited in the chapter is present in one of the pilot's bound artifacts.
    C04 caveats        if bound evidence says a result is from mice, a model, a post hoc or exploratory analysis,
                       a preprint, or not significant, the claim text carries that qualifier too.
    C05 language       no wording the manuscript has ruled out (glossary section 6, KERNEL section 6) in the body.
    C06 records        every claim is supported (a normative proposal may stay unknown), has a rationale and
                       evidence, and no whole ledger or audit file
                       is bound in place of a verbatim excerpt.
    C07 disclosure     the draft header states abstract depth or reading depth, self-checking, and that it gives
                       no frozen text.

What it is not
    It is not peer review, not a model judgement (V4) and not a human domain review. It cannot see paraphrase
    that changes meaning, a missing caveat it has no keyword for, a source that is wrong, or a better source
    that was not used. It was written by the same assistant that drafted the chapters, so the choice of
    checks is self-assessment (V5). Under DEC-020 the owner accepted this gate in place of independent
    human review (D05); that decision does not make any claim scientifically verified.

Isolation and non-vacuity follow tools/restructure_audit_agent.py: inputs are copied to a fresh scratch
directory (fail closed if missing), and `--self-test` mutates scratch copies and requires each targeted check
to fail.

Usage:
    python tools/claim_audit_agent.py            # print JSON receipt
    python tools/claim_audit_agent.py --write    # also write review/CLAIM_AUDIT_AGENT_RECEIPT.json
    python tools/claim_audit_agent.py --self-test
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
sys.path.insert(0, str(ROOT / 'tools'))
from research_assurance.core import inspect_project  # noqa: E402
import claim_token_scan as scan  # noqa: E402

OUT = ROOT / 'review/CLAIM_AUDIT_AGENT_RECEIPT.json'
PILOTS = scan.PILOTS + ['ch05_measurement_contract_en']
PMID = re.compile(r'PMID:?\s*(\d{6,9})|pubmed\.ncbi\.nlm\.nih\.gov/(\d{6,9})')
# (name, pattern in evidence, pattern the claim must then contain)
CAVEATS = [
    ('animal', re.compile(r'\b(mice|mouse|murine)\b', re.I), re.compile(r'\b(mice|mouse)\b', re.I)),
    ('animal', re.compile(r'\brats?\b', re.I), re.compile(r'\brats?\b', re.I)),
    ('model', re.compile(r'microsimulation', re.I), re.compile(r'\bmodel', re.I)),
    ('post hoc', re.compile(r'post hoc', re.I), re.compile(r'post hoc', re.I)),
    ('exploratory', re.compile(r'\bexploratory\b', re.I), re.compile(r'\bexploratory\b', re.I)),
    ('preprint', re.compile(r'\bpreprint\b', re.I), re.compile(r'\bpreprint\b', re.I)),
    ('null', re.compile(r'not (statistically )?significant|nonsignificant|non-significant|did not (reduce|improve|differ)|no significant', re.I),
     re.compile(r'not (statistically )?significant|nonsignificant|non-significant|\bnull\b|no (clear |significant )?difference|the same|did not|no effect|no benefit', re.I)),
]
# "X years younger" is allowed when the text reports what a clock or report says (chapters 5 and 6 do this);
# it is ruled out as an outcome of an intervention (KERNEL section 6).
AVOID = [r'\bmargins?\b', r'reverses? aging', r'(made|make|makes|became|become|becomes) (?!(the|its|their|a) (reading|estimate|clock|prediction))(\w+ ){0,3}\w+ years younger',
         r'years younger after', r'proven safe', r'150-year', r'fills? the gap', r'first framework',
         r'aging is (universally )?reversible']


def drafts_and_artifacts(pdir: Path):
    data = json.loads((pdir / 'project.json').read_text(encoding='utf-8'))
    return data, [a['path'] for a in data['artifacts']]


def stage(root: Path) -> Path:
    scratch = Path(tempfile.mkdtemp(prefix='claim_audit_agent_'))
    for p in PILOTS:
        rel = f'knowledge_base/pilots/{p}/project.json'
        if not (root / rel).is_file():
            raise FileNotFoundError(f'missing audit input (fail closed): {rel}')
        _, paths = drafts_and_artifacts(root / f'knowledge_base/pilots/{p}')
        for r in [rel] + paths:
            src, dst = root / r, scratch / r
            if not src.is_file():
                raise FileNotFoundError(f'missing audit input (fail closed): {r}')
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return scratch


def check(cid, pilot, ok, detail):
    return {'id': cid, 'pilot': pilot, 'result': 'PASS' if ok else 'FAIL', 'detail': detail}


def body(text: str) -> str:
    """Chapter text without the status block quote and footnote definitions."""
    return '\n'.join(l for l in text.splitlines() if not l.startswith('>') and not l.startswith('[^'))


def run_checks(s: Path):
    res = []
    for p in PILOTS:
        data = json.loads((s / f'knowledge_base/pilots/{p}/project.json').read_text(encoding='utf-8'))
        ev = {e['id']: e['text'] for e in data['evidence']}
        draft_rel = next(a['path'] for a in data['artifacts'] if a['role'] == 'manuscript')
        draft = (s / draft_rel).read_text(encoding='utf-8')

        r = inspect_project(data, s)
        ok = r['schema_valid'] and not r.get('issues') and not r.get('artifact_drift') and not r.get('stale_nodes')
        res.append(check('C01', p, ok, {'schema_valid': r['schema_valid'], 'issues': (r.get('issues') or r.get('errors') or [])[:5],
                                        'drift': r.get('artifact_drift', []), 'stale': r.get('stale_nodes', [])[:5]}))

        if p in scan.PILOTS:
            found = {}
            for c in data['claims']:
                text = re.sub(r'\[\^\d+\]', '', c['text'])
                evt = ' '.join(ev[i] for i in c['evidence_ids'])
                evn = {scan.norm(x) for x in scan.NUM.findall(evt)}
                toks = sorted({x for x in scan.NUM.findall(text) if scan.norm(x) not in evn} |
                              {w for w in scan.CAP.findall(text) if w not in evt})
                if toks:
                    found[c['id']] = toks
            mine = {k: v for k, v in scan.REVIEWED.items() if any(k == c['id'] for c in data['claims'])}
            unrev = {cid: [t for t in toks if t not in mine.get(cid, {})] for cid, toks in found.items()}
            unrev = {k: v for k, v in unrev.items() if v}
            gone = {cid: [t for t in toks if t not in found.get(cid, [])] for cid, toks in mine.items()}
            gone = {k: v for k, v in gone.items() if v}
            res.append(check('C02', p, not unrev and not gone, {'unreviewed': unrev, 'reviewed_but_gone': gone}))

        cited = {a or b for a, b in PMID.findall(draft)}
        bound_text = ''.join((s / a['path']).read_text(encoding='utf-8') for a in data['artifacts'] if a['role'] != 'manuscript')
        have = {a or b for a, b in PMID.findall(bound_text)}
        missing = sorted(cited - have)
        res.append(check('C03', p, not missing, {'cited': len(cited), 'not_in_bound_artifacts': missing}))

        lacks = []
        for c in data['claims']:
            evt = ' '.join(ev[i] for i in c['evidence_ids'])
            for name, in_ev, in_claim in CAVEATS:
                if in_ev.search(evt) and not in_claim.search(c['text']):
                    lacks.append((c['id'], name))
        res.append(check('C04', p, not lacks, {'claim_missing_qualifier': sorted(set(lacks))}))

        b = body(draft).lower()
        hits = [pat for pat in AVOID if re.search(pat, b)]
        res.append(check('C05', p, not hits, {'avoided_wording_found': hits}))

        bad = []
        for c in data['claims']:
            a = c['assessment']
            # A normative proposal cannot be supported by a source; it may stay 'unknown' if it says so.
            normative_ok = a['state'] == 'unknown' and (c['kind'] == 'normative' or c['role'] == 'proposal')
            if (a['state'] != 'supported' and not normative_ok) or not a['rationale'].strip() or not c['evidence_ids']:
                bad.append(c['id'])
        whole = [a['path'] for a in data['artifacts'] if a['path'] == 'knowledge_base/CLAIM_LEDGER.md'
                 or re.search(r'knowledge_base/[A-Z_]+_AUDIT_[0-9-]+\.md$', a['path'])]
        res.append(check('C06', p, not bad and not whole and len(data['claims']) > 0,
                         {'claims': len(data['claims']), 'not_supported_or_unevidenced': bad, 'whole_files_bound': whole}))

        head = '\n'.join(l for l in draft.splitlines()[:15] if l.startswith('>')).lower()
        need = {'depth': bool(re.search(r'abstract depth|full text|reading depth', head)),
                'self-checked': 'self-checked' in head, 'not frozen': 'not a frozen text' in head}
        res.append(check('C07', p, all(need.values()), need))
    return res


def summarize(res, scratch):
    fails = [f"{r['id']}:{r['pilot']}" for r in res if r['result'] == 'FAIL']
    inputs = sorted(str(q.relative_to(scratch)) for q in scratch.rglob('*') if q.is_file())
    return {'agent': 'tools/claim_audit_agent.py', 'verifier_level': 'V1 (deterministic; encoded properties only)',
            'decision': 'DEC-020 (owner accepted this gate in place of independent human review, D05)',
            'not': ['peer review', 'model judgement (V4)', 'human domain review', 'scientific verification',
                    'a check of paraphrase, of sources not used, or of caveats without a keyword'],
            'independence': 'written by the same assistant that drafted the chapters; choice of checks is V5',
            'pilots': PILOTS,
            'inputs_sha256': {rel: hashlib.sha256((scratch / rel).read_bytes()).hexdigest() for rel in inputs},
            'checks': res, 'failed': fails, 'passed': len(res) - len(fails), 'total': len(res)}


def _json_edit(fn):
    def apply(t):
        d = json.loads(t)
        fn(d)
        return json.dumps(d, ensure_ascii=False, indent=2) + '\n'
    return apply


def self_test():
    """Each mutation must make its targeted check fail (non-vacuity)."""
    pj = 'knowledge_base/pilots/{}/project.json'
    c10 = 'books/manuscript/en/CH10_routes_draft_en.md'

    def drop_mouse(d):
        c = next(c for c in d['claims'] if c['id'] == 'CH10-EN-C004')
        c['text'] = c['text'].replace('A mouse study', 'A study').replace('aged mice', 'aged animals')

    def add_token(d):
        d['claims'][0]['text'] += ' In 4321 people.'

    def unsupport(d):
        d['claims'][0]['assessment']['state'] = 'contested'

    def bind_ledger(d):
        d['artifacts'][-1]['path'] = 'knowledge_base/CLAIM_LEDGER.md'

    mutations = {
        'C01': ('ch10_routes_en', 'knowledge_base/pilots/ch10_routes_en/evidence/IMMUNE_SUPPORT_abstract.txt', lambda t: t + '\nEdited.\n'),
        'C02': ('ch10_routes_en', pj.format('ch10_routes_en'), _json_edit(add_token)),
        'C03': ('ch10_routes_en', c10, lambda t: t + '\n[^99]: Someone. PMID 99999999.\n'),
        'C04': ('ch10_routes_en', pj.format('ch10_routes_en'), _json_edit(drop_mouse)),
        'C05': ('ch10_routes_en', c10, lambda t: t.replace('## 5 | What to report for any route', '## 5 | What to report for any route\n\nThis reverses aging.', 1)),
        'C05b': ('ch10_routes_en', c10, lambda t: t.replace('## 5 | What to report for any route', '## 5 | What to report for any route\n\nThe programme made participants three years younger.', 1)),
        'C06': ('ch10_routes_en', pj.format('ch10_routes_en'), _json_edit(unsupport)),
        'C06b': ('ch10_routes_en', pj.format('ch10_routes_en'), _json_edit(bind_ledger)),
        'C07': ('ch10_routes_en', c10, lambda t: t.replace('Self-checked', 'Checked', 1)),
    }
    report = {}
    for key, (pilot, rel, fn) in mutations.items():
        cid = key[:3]
        scratch = stage(ROOT)
        try:
            q = scratch / rel
            before = q.read_text(encoding='utf-8')
            after = fn(before)
            if after == before:
                report[key] = 'MUTATION_NOT_APPLIED'
                continue
            q.write_text(after, encoding='utf-8')
            if key == 'C06b':
                (scratch / 'knowledge_base/CLAIM_LEDGER.md').parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / 'knowledge_base/CLAIM_LEDGER.md', scratch / 'knowledge_base/CLAIM_LEDGER.md')
            got = next(x for x in run_checks(scratch) if x['id'] == cid and x['pilot'] == pilot)
            report[key] = 'DETECTED' if got['result'] == 'FAIL' else 'MISSED'
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
    return 0 if not receipt['failed'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
