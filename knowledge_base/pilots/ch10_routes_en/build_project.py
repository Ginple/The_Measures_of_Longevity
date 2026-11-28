"""Bind selected claims of the English chapter 10 draft (DEC-016, written English-first) to exact source spans.

Run deliberately to (re)bind after a reviewed change; tests never run it. Spans are located by anchor
text and frozen into project.json as line numbers, exact text and sha256, so a later edit to the
chapter, to an excerpt or to a synthetic output or memo shows up as drift in `inspect_project`.
Helpers (span location, hashing, dimension template, reviewer label) are imported from the ch5 builder
so the pilots share one binding procedure. Assessments are the same assistant's comparison of each
paragraph with the quoted excerpts, not independent review.
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
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)

HERE = 'knowledge_base/pilots/ch10_routes_en'
EN_PATH = 'books/manuscript/en/CH10_routes_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH10-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016); new writing using V6 sections 06-07 as leads; working copy'),
    ('A-TRIALS', f'{EV}/ROUTES_TRIALS_abstracts.txt', 'source', 'routes-illustrative-trials', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/26551272/', 'PubMed abstracts (SPRINT 2015; Skou 2015 knee replacement; ACHIEVE 2023) 2026-11-28; three independent groups'),
    ('A-IMMUNE', f'{EV}/IMMUNE_SUPPORT_abstract.txt', 'source', 'friedrich-hepatic-immune', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/41407851/', 'PubMed abstract (Friedrich 2026 Nature, mouse study) 2026-11-28'),
    ('A-CAPABLE', f'{EV}/CAPABLE_abstract.txt', 'source', 'capable-trial', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/30615024/', 'copy of the chapter 1 excerpt (Szanton 2019) 2026-11-28'),
    ('A-RECORDS', f'{EV}/LEDGER_X15_X79_excerpt.txt', 'source', 'longevity-project-record', 'fulltext', '',
     'verbatim copy of ledger rows X15 and X79 (2026-11-28): records of earlier reading by the same assistant; not a primary source'),
]
EVIDENCE = {
    'E-SP-HDR': ('A-TRIALS', '# [1] SPRINT Research Group', 1),
    'E-SP-METH': ('A-TRIALS', '[1] METHODS: We randomly assigned 9361', 1),
    'E-SP-PRIM': ('A-TRIALS', '[1] The primary composite outcome', 1),
    'E-SP-BP': ('A-TRIALS', '[1] RESULTS: At 1 year', 1),
    'E-SP-STOP': ('A-TRIALS', '[1] The intervention was stopped early', 1),
    'E-SP-MORT': ('A-TRIALS', '[1] All-cause mortality', 1),
    'E-SP-AE': ('A-TRIALS', '[1] Rates of serious adverse events', 1),
    'E-KN-HDR': ('A-TRIALS', '# [2] Skou ST', 1),
    'E-KN-METH': ('A-TRIALS', '[2] METHODS: In this randomized', 1),
    'E-KN-ARMS': ('A-TRIALS', '[2] Patients were randomly assigned', 1),
    'E-KN-OUT': ('A-TRIALS', '[2] The primary outcome was the change', 1),
    'E-KN-CROSS': ('A-TRIALS', '[2] In the nonsurgical-treatment group', 1),
    'E-KN-RES': ('A-TRIALS', '[2] In the intention-to-treat analysis', 1),
    'E-KN-AE': ('A-TRIALS', '[2] The total-knee-replacement group had a higher', 1),
    'E-AC-HDR': ('A-TRIALS', '# [3] Lin FR', 1),
    'E-AC-BG': ('A-TRIALS', '[3] BACKGROUND:', 1),
    'E-AC-METH': ('A-TRIALS', '[3] METHODS: The ACHIEVE', 1),
    'E-AC-END': ('A-TRIALS', '[3] The primary endpoint', 1),
    'E-AC-POP': ('A-TRIALS', '[3] Participants were recruited', 1),
    'E-AC-ARMS': ('A-TRIALS', '[3] Participants were randomly assigned', 1),
    'E-AC-N': ('A-TRIALS', '[3] We randomly assigned 490', 1),
    'E-AC-ARIC': ('A-TRIALS', '[3] Participants from ARIC', 1),
    'E-AC-PRIM': ('A-TRIALS', '[3] In the primary analysis', 1),
    'E-AC-SENS': ('A-TRIALS', '[3] However, a prespecified', 1),
    'E-AC-SUGG': ('A-TRIALS', '[3] These findings suggest', 1),
    'E-AC-COI': ('A-TRIALS', '[3] Conflict of interest statement', 1),
    'E-IM-HDR': ('A-IMMUNE', '# Friedrich MJ', 1),
    'E-IM-MAIN': ('A-IMMUNE', 'Here we show that the liver', 1),
    'E-IM-MAP': ('A-IMMUNE', 'These immune cues were found', 1),
    'E-IM-DEL': ('A-IMMUNE', 'Delivery of mRNAs', 1),
    'E-IM-FUNC': ('A-IMMUNE', 'Treatment with these mRNAs', 1),
    'E-IM-REV': ('A-IMMUNE', 'These effects were reversible', 1),
    'E-IM-COI': ('A-IMMUNE', 'Conflict of interest statement', 1),
    'E-CA-HDR': ('A-CAPABLE', '# Szanton SL', 1),
    'E-CA-DES': ('A-CAPABLE', 'DESIGN, SETTING, AND PARTICIPANTS', 1),
    'E-CA-INT': ('A-CAPABLE', 'INTERVENTIONS: The CAPABLE group', 1),
    'E-CA-CTRL': ('A-CAPABLE', 'The control group received', 1),
    'E-CA-ADL': ('A-CAPABLE', 'CAPABLE participation resulted in 30%', 1),
    'E-CA-IADL': ('A-CAPABLE', 'CAPABLE participation resulted in a statistically', 1),
    'E-CA-COI': ('A-CAPABLE', 'Conflict of interest statement', 1),
    'E-R-X15': ('A-RECORDS', '| X15 | 2026-11-27 |', 1),
    'E-R-X79': ('A-RECORDS', '| X79 | 2026-11-27 |', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


CLAIMS = [
    dict(id='CH10-EN-C001', anchor='Lowering blood pressure is maintenance in this sense.', kind='reported', role='asserted', critical=True,
         context=ctx('adults with systolic BP >=130 mm Hg, increased cardiovascular risk, no diabetes', 'median 3.26 years (stopped early)', 'hazard ratios for a composite cardiovascular outcome and all-cause death; serious adverse events',
                     'participant', 'randomized controlled trial', 'blood-pressure targets (illustration of maintenance)'),
         evidence=['E-SP-HDR', 'E-SP-METH', 'E-SP-PRIM', 'E-SP-BP', 'E-SP-STOP', 'E-SP-MORT', 'E-SP-AE'], state='supported',
         rationale='9361; SBP >=130, increased CV risk, no diabetes; <120 vs <140; 121.4 vs 136.2 at 1 year; stopped early at median 3.26 years; composite (MI, other ACS, stroke, HF, CV death) 1.65% vs 2.19% per year, HR 0.75; all-cause HR 0.73; more serious AEs of hypotension, syncope, electrolyte abnormalities, AKI, not injurious falls. All match. "Heart attack", "low blood pressure", "fainting" gloss MI, hypotension, syncope. The remark that the trial did not measure arterial age is the chapter\'s reading of the end points.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C002', anchor='Replacement is the clearest case of restoring a task without reversing a process.', kind='reported', role='asserted', critical=True,
         context=ctx('100 people with moderate-to-severe knee osteoarthritis eligible for unilateral total knee replacement', '12 months', 'change in KOOS4; serious adverse events; crossover',
                     'participant', 'randomized controlled trial', 'knee replacement (illustration of replacement)'),
         evidence=['E-KN-HDR', 'E-KN-METH', 'E-KN-ARMS', 'E-KN-OUT', 'E-KN-CROSS', 'E-KN-RES', 'E-KN-AE'], state='supported',
         rationale='100 patients; TKR plus 12 weeks nonsurgical vs 12 weeks nonsurgical (exercise, education, dietary advice, insoles, pain medication); KOOS4 pain, symptoms, ADL, QoL, 0 worst to 100 best; 32.5 vs 16.0, adjusted difference 15.8; serious AEs 24 vs 6; 13 (26%) of nonsurgical group had TKR before 12 months. All match. The remark about the comparison being the best alternative is the chapter\'s reading.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C003', anchor='Compensation is often judged against a question it was never designed to answer.', kind='reported', role='asserted', critical=True,
         context=ctx('adults aged 70-84 with untreated hearing loss, no substantial cognitive impairment', '3 years', 'difference in 3-year change of a global cognition factor score',
                     'participant', 'randomized controlled trial (unmasked)', 'hearing intervention (illustration of compensation)'),
         evidence=['E-AC-HDR', 'E-AC-BG', 'E-AC-METH', 'E-AC-END', 'E-AC-POP', 'E-AC-ARMS', 'E-AC-N', 'E-AC-ARIC', 'E-AC-PRIM', 'E-AC-SENS', 'E-AC-SUGG', 'E-AC-COI'], state='supported',
         rationale='Background association; 70-84, untreated hearing loss, no substantial impairment; hearing aids plus counselling 490 vs health education 487; difference 0.002 SD, p=0.96; prespecified sensitivity analysis: effect differed between ARIC (older, more risk factors) and de novo volunteers, p interaction 0.010; authors suggest possible benefit at higher risk. COI: Sonova/Phonak in-kind donation of hearing technologies; FRL directs a centre funded in part by a philanthropic donation from Cochlear. All match. The lead-not-result framing is the chapter\'s.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C004', anchor='A mouse study published in 2025 makes the difference concrete.', kind='reported', role='asserted', critical=True,
         context=ctx('aged mice', 'during dosing', 'lymphoid progenitors, thymopoiesis, T cells, vaccine and antitumour responses',
                     'mouse', 'animal experiment', 'immune support via hepatic mRNA delivery'),
         evidence=['E-IM-HDR', 'E-IM-MAIN', 'E-IM-MAP', 'E-IM-DEL', 'E-IM-FUNC'], state='supported',
         rationale='Epub 2025 Dec 17 (header). Multi-omic mapping of central and peripheral niches in young and aged animals; Notch and FLT3L pathways plus IL-7 decline; mRNAs for DLL1, FLT3L, IL-7 to hepatocytes; liver transiently repurposed to restore age-diminished cues; expanded common lymphoid progenitors, boosted de novo thymopoiesis without affecting HSC composition, replenished T cells; improved peptide vaccine responses and restored antitumour immunity in aged mice. All match. "Early cells from which lymphocytes develop" glosses common lymphoid progenitors.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C005', anchor='Two things in this abstract need stating precisely.', kind='reported', role='asserted', critical=True,
         context=ctx('aged mice', 'during and after dosing', 'reversibility; self-tolerance',
                     'mouse', 'animal experiment', 'immune support via hepatic mRNA delivery'),
         evidence=['E-IM-HDR', 'E-IM-DEL', 'E-IM-REV', 'E-IM-COI'], state='supported',
         rationale='Thymopoiesis boosted (so not bypassed); reversible after dosing ceased; did not breach self-tolerance, contrasted with inflammatory and autoimmune liabilities of recombinant cytokines; two authors co-inventors on a provisional patent application relating to the work. All match. The limits (repeated dosing over years, full pathogen range, lifespan) are the chapter\'s statements of what was not shown.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C006', anchor='But the objection treats biological age as the only outcome.', kind='reported', role='asserted', critical=True,
         context=ctx('300 low-income community-dwelling adults 65+ with a disability, Baltimore', '5 months', 'relative risk of ADL and IADL disability scores',
                     'participant', 'randomized clinical trial', 'home-based compensation and capacity'),
         evidence=['E-CA-HDR', 'E-CA-DES', 'E-CA-INT', 'E-CA-CTRL', 'E-CA-ADL', 'E-CA-IADL'], state='supported',
         rationale='300; low-income, community-dwelling, 65+, disability, Baltimore; up to 10 visits over 5 months by OTs, RNs and home modifiers on self-identified goals via capacity and home environment; control 10 social visits by a research assistant; ADL score RR 0.70 (30% reduction); IADL nonsignificant 17%. All match. "Living in their own homes" glosses community-dwelling and in their home.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C007', anchor='The same trial shows why compensation deserves the same scrutiny', kind='reported', role='asserted', critical=False,
         context=ctx('CAPABLE trial documents', 'design 2014, registration (current), results 2019', 'stated primary outcome across documents; declared interests',
                     'document', 'project record of document comparison', 'trial reporting'),
         evidence=['E-CA-COI', 'E-R-X79'], state='supported',
         rationale='COI: Szanton and Gitlin inventors of the CAPABLE training program; Johns Hopkins entitled to fees. X79: design paper ADL primary, IADL secondary; current registration ADL only; 2019 results both primary; without full protocol and analysis plan, cannot judge violation, error or bias direction. Match; the university is not named in the text.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH10-EN-C008', anchor='None of the three can be folded into a single score.', kind='reported', role='asserted', critical=False,
         context=ctx('none: project record', 'not applicable', 'status of the maintenance-capacity formula',
                     'formula', 'project ledger row', 'project governance'),
         evidence=['E-R-X15'], state='supported',
         rationale='X15: the multiply-subtract maintenance-capacity formula is undefined; variables, units, interactions and the meaning of the operations not given; cannot be computed; equality withdrawn, kept as a research concept. Match. Chapter 21 ownership is from the glossary, a cross-reference.',
         dimensions=dims(source_support='supported', extraction='supported')),
]


def build():
    arts = {a[0]: dict(id=a[0], path=a[1], sha256=base.sha(a[1]), role=a[2], family=a[3], access_depth=a[4],
                       url=a[5], version=a[6]) for a in ARTIFACTS}
    evidence = []
    for eid, (aid, anchor, n) in EVIDENCE.items():
        span, text = base.locate(arts[aid]['path'], anchor, n)
        evidence.append(dict(id=eid, artifact_id=aid, lines_1based_halfopen=span, text=text))
    ev = {e['id']: e for e in evidence}
    claims = []
    for c in CLAIMS:
        span, text = base.locate(EN_PATH, c['anchor'], 1)
        claim = dict(id=c['id'], artifact_id='A-CH10-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH10-EN': arts['A-CH10-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch10-routes-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Eight paragraph units of the English chapter 10 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=8, registered_claims=len(claims),
                         note='The route table, the durability argument, the reply to the objection and the reporting rule are the book\'s framework and make no source claim. Abstract depth throughout; X15 and X79 rest on project records.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH10-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent review by a geriatrician, a trialist or an immunologist (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH10-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='Four trials and one mouse study at abstract depth; the mouse study\'s follow-up after stopping and safety window not read; X79 needs dated protocol and registration history',
                 next_action='Read full texts (Friedrich methods and extended data; ACHIEVE sensitivity analysis); retrieve the CAPABLE registration history',
                 closure_evidence='Full-text reading notes bound as excerpts'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if out.exists() and json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
