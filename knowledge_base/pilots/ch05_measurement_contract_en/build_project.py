"""Bind the English ch5 draft (DEC-016) to the same source spans as the Chinese v0.3 pilot.

Run deliberately to (re)bind after a reviewed change; tests never run it. The evidence spans, claim
contexts and assessment states are imported from the Chinese pilot builder so the two language
versions cannot silently diverge in what they claim a source says. Each English claim also binds the
Chinese paragraph it was rewritten from (evidence id E-ZH-...), so an edit to either language makes
the English claim stale until it is re-bound. Assessments are the same assistant's comparison, not
independent review, and add no new empirical claim.
"""
from pathlib import Path
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import claim_record_hash  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    'ch05_zh_builder', ROOT / 'knowledge_base/pilots/ch05_measurement_contract/build_project.py')
zh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zh)

HERE = 'knowledge_base/pilots/ch05_measurement_contract_en'
EN_PATH = 'books/manuscript/en/CH05_measurement_contracts_draft_en.md'
ARTIFACTS = [('A-CH5-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
              'English draft v0.1 (DEC-016), rewritten from zh v0.3; working copy')] + list(zh.ARTIFACTS)
# English claim -> (zh claim id, anchor in the English draft, number of lines in the claim unit,
#                   English-specific rendering note)
EN_CLAIMS = {
    'CH5-EN-C001': ('CH5-C001', 'This distinction is not just theoretical caution.', 1,
                    '26 studies, no full concordance in controlled comparative studies, no pooled combination, no trial-level surrogate validation, very low certainty, exploratory or supportive only, no added clock significant: all carried over unchanged.'),
    'CH5-EN-C002': ('CH5-C002', 'A 2026 analysis of CALERIE provides exactly this kind of example.', 1,
                    '190 analyzable, months 12-24, largest-rebound group of 20 from both arms, 57 missing baseline insulin AUC, second year inside the intervention and maintenance window, no life-years: all carried over unchanged.'),
    'CH5-EN-C003': ('CH5-C003', 'A blood sample contains many kinds of cells.', 1,
                    'Two-type linear model with known, unchanging weights; aggregate fall compatible with a within-type rise or fall; explicitly not an estimate of a real body: carried over unchanged.'),
    'CH5-EN-C004': ('CH5-C004', 'NHS-Galleri is a large randomized trial in England.', 5,
                    'About 142,000 (zh: about 142 thousand) for 142,250 randomized; 17-month median; 12 prespecified types; 706 vs 688; rate ratio 1.03 (0.92 to 1.14); secondary results descriptive after the primary test failed. The English splits the paragraph into an intro line and four bullets; the unit spans all five lines.'),
    'CH5-EN-C005': ('CH5-C005', 'So a responsible clock study should at least do four things:', 7,
                    'Four reporting rules plus the sieve sentence and the two-arms-are-not-two-replications sentence; the unit spans the intro line, four bullets, a blank line and the closing sentence.'),
}


def build():
    arts = {a[0]: dict(id=a[0], path=a[1], sha256=zh.sha(a[1]), role=a[2], family=a[3], access_depth=a[4],
                       url=a[5], version=a[6]) for a in ARTIFACTS}
    zh_claims = {c['id']: c for c in zh.CLAIMS}
    evidence = []
    for eid, (aid, anchor, n) in zh.EVIDENCE.items():
        span, text = zh.locate(arts[aid]['path'], anchor, n)
        evidence.append(dict(id=eid, artifact_id=aid, lines_1based_halfopen=span, text=text))
    for zid, c in zh_claims.items():  # lineage: the Chinese paragraph each English claim was rewritten from
        span, text = zh.locate(arts['A-CH5']['path'], c['anchor'], 1)
        evidence.append(dict(id='E-ZH-' + zid[4:], artifact_id='A-CH5', lines_1based_halfopen=span, text=text))
    ev = {e['id']: e for e in evidence}
    claims = []
    for cid, (zid, anchor, n, note) in EN_CLAIMS.items():
        z = zh_claims[zid]
        span, text = zh.locate(EN_PATH, anchor, n)
        ev_ids = list(z['evidence']) + ['E-ZH-' + zid[4:]]
        claim = dict(id=cid, artifact_id='A-CH5-EN', lines_1based_halfopen=span, text=text, kind=z['kind'],
                     role=z['role'], critical=z['critical'], context=z['context'], evidence_ids=ev_ids)
        bound = {'A-CH5-EN': arts['A-CH5-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in ev_ids})
        rationale = (f'English rendering of {zid} (zh v0.3), same evidence and state. Rendering check: {note} '
                     f'Original {zid} rationale: {z["rationale"]}')
        claim['assessment'] = dict(state=z['state'], reviewer=zh.REVIEWER, rationale=rationale, bound_hashes=bound,
                                   record_sha256='', dimensions=z['dimensions'])
        if z['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch05-measurement-contract-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='The five English claim units that correspond to the five registered zh v0.3 paragraphs of OUTLINE_v1 ch5; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=5, registered_claims=len(claims),
                         note='Same gaps as the zh pilot: CALERIE methylation/bone, DO-HEALTH and Malagón microsimulation paragraphs are not registered. Translation accuracy beyond the bound numbers and qualifiers is not machine-checked.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH5-EN-INDEPENDENT-REVIEW', status='blocked', blocks_formal_release=True,
                 question='No independent domain, statistical or translation review of the English text (D05)',
                 next_action='Real external review, including a bilingual check; never fabricate receipts',
                 closure_evidence='Object-bound review record with declared independence and responses'),
            dict(id='CH5-EN-INVENTORY', status='open', blocks_formal_release=True,
                 question='3 of 7 footnoted evidence paragraphs unregistered, as in the zh pilot',
                 next_action='Register remaining paragraphs in both languages',
                 closure_evidence='Declared complete inventory with human acceptance'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if out.exists() and json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
