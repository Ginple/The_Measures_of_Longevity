"""Bind selected claims of the English chapter 1 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch01_measure_en'
EN_PATH = 'books/manuscript/en/CH01_measure_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH1-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016); rewrite of the Chinese demonstration draft CH01 v0.2 (V6-01); working copy'),
    ('A-GAP', f'{EV}/HEALTHSPAN_GAP_abstract.txt', 'source', 'study-Garmany-healthspan-gap', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/39661386/', 'PubMed abstract and COI 2026-11-28'),
    ('A-CAL', f'{EV}/CALERIE_abstracts.txt', 'source', 'trial-CALERIE-phase2', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/37118425/', 'PubMed abstracts (Waziry 2023; Villareal 2016; Romashkan 2016) 2026-11-28; one trial'),
    ('A-CAP', f'{EV}/CAPABLE_abstract.txt', 'source', 'trial-CAPABLE-Szanton', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/30615024/', 'PubMed abstract and COI 2026-11-28'),
    ('A-LT-CODE', f'{HERE}/synthetic_life_table.py', 'code', 'longevity-project-derivation', 'code', '',
     'project synthetic life-table calculation; tests/test_ch01_en_pilot.py recomputes it'),
    ('A-LT-OUT', f'{EV}/LIFE_TABLE_SYNTHETIC_output.json', 'dataset', 'longevity-project-derivation', 'data', '',
     'saved stdout of synthetic_life_table.py'),
    ('A-LEDGER', f'{EV}/LEDGER_X21_X29_excerpt.txt', 'source', 'longevity-project-record', 'fulltext', '',
     'verbatim copy of ledger rows X21 and X29 (2026-11-28): records of earlier full-text reading by the same assistant; not a primary source'),
]
EVIDENCE = {
    'E-GAP-DEF': ('A-GAP', 'Health-adjusted life expectancy, a measure of healthy longevity', 1),
    'E-GAP-WHO': ('A-GAP', 'World Health Organization (WHO) Global Health Observatory', 1),
    'E-GAP-183': ('A-GAP', 'The 183 WHO member states were investigated.', 1),
    'E-GAP-96': ('A-GAP', 'extending to 9.6 years', 1),
    'E-GAP-SEX': ('A-GAP', '2.4 (0.5) years wider than men', 1),
    'E-GAP-US': ('A-GAP', 'amounting to 12.4 years', 1),
    'E-GAP-COI': ('A-GAP', 'Conflict of Interest Disclosures: None reported.', 1),
    'E-LED-X21': ('A-LEDGER', '| X21 | 2026-11-27 |', 1),
    'E-LED-X29': ('A-LEDGER', '| X29 | 2026-11-27 |', 1),
    'E-LT-NATURE': ('A-LT-OUT', '"nature"', 1),
    'E-LT-A': ('A-LT-OUT', '"A": {', 16),
    'E-LT-B': ('A-LT-OUT', '"B": {', 14),
    'E-LT-C': ('A-LT-OUT', '"C": {', 16),
    'E-LT-DESIGN': ('A-LT-CODE', '- A: 20 people die at 10 and 80 die at 20', 4),
    'E-CAL-220': ('A-CAL', 'n = 220 adults without obesity were randomized to 25% CR', 1),
    'E-CAL-PACE': ('A-CAL', 'slowed the pace of aging, as measured by the DunedinPACE', 1),
    'E-CAL-SMALL': ('A-CAL', 'Treatment effect sizes were small.', 1),
    'E-CAL-COI': ('A-CAL', 'are listed as inventors on a Duke University and University of Otago invention, DunedinPACE', 1),
    'E-CAL-218': ('A-CAL', 'Two-hundred eighteen non-obese', 1),
    'E-CAL-BMD': ('A-CAL', 'the CR group had greater changes in BMD at 24 months', 1),
    'E-CAL-LIMIT': ('A-CAL', 'represents a potential limitation of prolonged CR', 1),
    'E-CAL-FRAC': ('A-CAL', 'contributes to fracture risk', 1),
    'E-CAL-SAFE': ('A-CAL', 'at levels achieved in CALERIE was safe and well tolerated', 1),
    'E-CAL-MON': ('A-CAL', 'Close monitoring for excessive bone loss and anemia', 1),
    'E-CAP-DESIGN': ('A-CAP', 'In this randomized clinical trial of 300 low-income', 1),
    'E-CAP-INT': ('A-CAP', 'The CAPABLE group received up to 10 home visits', 1),
    'E-CAP-CTRL': ('A-CAP', 'The control group received 10 social home visits', 1),
    'E-CAP-SCORE': ('A-CAP', 'Each ADL and IADL task was self-scored from 0 to 2', 1),
    'E-CAP-RANGE': ('A-CAP', 'The overall score ranged from 0 to 16 points.', 1),
    'E-CAP-ADL': ('A-CAP', '30% reduction in ADL disability scores at 5 months', 1),
    'E-CAP-IADL': ('A-CAP', 'statistically nonsignificant 17% reduction in IADL', 1),
    'E-CAP-COI': ('A-CAP', 'reported being inventors of the CAPABLE training program', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


CLAIMS = [
    dict(id='CH1-EN-C001', anchor='Granting that does not settle what a statistic about time means.', kind='reported', role='asserted', critical=True,
         context=ctx('183 WHO member states (national-level WHO Global Health Observatory estimates)', 'two decades to 2019 (period estimates)',
                     'gap between life expectancy and health-adjusted life expectancy; sex difference; largest national gap',
                     'country / global aggregate', 'retrospective cross-sectional analysis of WHO estimates', 'population health statistics'),
         evidence=['E-GAP-DEF', 'E-GAP-WHO', 'E-GAP-183', 'E-GAP-96', 'E-GAP-SEX', 'E-GAP-US', 'E-GAP-COI', 'E-LED-X21'], state='supported',
         rationale='WHO data, 183 member states, gap widened over two decades to 9.6 years, women 2.4 years wider, US largest at 12.4: all in the abstract. The global-versus-country-average distinction comes from the project ledger X21 (earlier full-text reading by the same assistant), cited as such, not from the abstract. The definitions of the two statistics restate the abstract\'s importance statement and general demographic usage.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH1-EN-C002', anchor='What does a gap of 9.6 years mean for one person?', kind='formal', role='asserted', critical=True,
         context=ctx('none: three synthetic populations of 100 people', 'synthetic lifetimes up to 20 years',
                     'life expectancy, health-adjusted life expectancy, gap, and their person-level distributions',
                     'synthetic person', 'exact arithmetic (script and tests)', 'life-table arithmetic only'),
         evidence=['E-LT-NATURE', 'E-LT-A', 'E-LT-B', 'E-LT-C', 'E-LT-DESIGN'], state='supported',
         rationale='All three populations: LE 18, HALE 15, gap 3. A: deaths 20 at 10, 80 at 20; losses 1 (20) and 7/2 (80); nobody at 18 or at 3. B: all die at 18, all lose 3. C: deaths as A; losses 1 (80) and 11 (20). All match the saved output. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH1-EN-C003', anchor='One trial shows why "did it work?" can have more than one answer.', kind='reported', role='asserted', critical=True,
         context=ctx('CALERIE phase 2: adults without obesity (bone report: non-obese younger adults, mean age 37.9)', 'two years',
                     'DNAm pace and clock changes; BMD change at 24 months; safety and tolerability',
                     'participant', 'randomized trial; methylation analysis post hoc', 'calorie restriction versus ad libitum diet'),
         evidence=['E-CAL-220', 'E-CAL-PACE', 'E-CAL-SMALL', 'E-CAL-COI', 'E-CAL-BMD', 'E-CAL-LIMIT', 'E-CAL-FRAC', 'E-CAL-SAFE', 'E-CAL-MON'], state='supported',
         rationale='Target 25% CR vs ad libitum for 2 years; DunedinPACE slowed, PhenoAge/GrimAge not significantly changed, small effects; inventor COI; greater BMD loss at 24 months at three sites, potential limitation, fracture risk needs longer studies; safe and well tolerated at levels achieved, monitor bone loss and anemia. All match. "Later analysis" renders "post hoc"; "usual diet" renders "ad libitum"; "commercial company" renders "commercial entity".',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH1-EN-C004', anchor='These are three reports from one trial, not three confirmations.', kind='reported', role='asserted', critical=True,
         context=ctx('CALERIE phase 2 reports', 'two years', 'number randomized as described in each report; target versus achieved restriction',
                     'report', 'comparison of published descriptions', 'reporting of one trial'),
         evidence=['E-CAL-220', 'E-CAL-218', 'E-CAL-SAFE', 'E-LED-X29'], state='supported',
         rationale='220 (methylation report) and 218 (bone report, spelled out) match; "at levels achieved in CALERIE" quoted exactly; the participant-overlap point cites ledger X29. The chapter does not say which count is right or why they differ.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH1-EN-C005', anchor='A randomized trial in Baltimore, Maryland, shows a change that happens outside the cell.', kind='reported', role='asserted', critical=True,
         context=ctx('300 low-income community-dwelling adults aged 65+ with self-reported ADL/IADL difficulty, Baltimore', '5-month end point (12-month follow-up not read)',
                     'ADL and IADL disability scores, intervention versus attention control', 'participant',
                     'randomized clinical trial, intention to treat', 'home-based multidisciplinary programme'),
         evidence=['E-CAP-DESIGN', 'E-CAP-INT', 'E-CAP-CTRL', 'E-CAP-ADL', 'E-CAP-IADL', 'E-CAP-COI'], state='supported',
         rationale='300, low-income, 65+, community-dwelling, difficulty with daily activities; up to 10 visits over 5 months by OTs, RNs and home modifiers on self-identified goals vs 10 social visits; ADL RR 0.70 (0.54-0.93), 30% reduction; IADL 0.83 (0.65-1.06) nonsignificant; inventor COI with university fees. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH1-EN-C006', anchor='That result is worth taking seriously, and it is easy to over-read.', kind='reported', role='asserted', critical=True,
         context=ctx('CAPABLE participants', '5 months; 12-month interviews existed', 'interpretation limits of the ADL score ratio',
                     'participant', 'randomized clinical trial', 'home-based multidisciplinary programme'),
         evidence=['E-CAP-SCORE', 'E-CAP-RANGE', 'E-CAP-DESIGN', 'E-CAP-INT'], state='supported',
         rationale='Self-scored 0-2 per task, total 0-16; interviews at 12 months; programme combined OTs, RNs and home modifiers. The reading of 0.70 as a comparison of scores, not an event risk, follows from the outcome definition; the abstract itself labels it "relative risk" and "30% reduction", which the chapter reports in the previous paragraph. No claim of longer life is made by the trial abstract.',
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
        claim = dict(id=c['id'], artifact_id='A-CH1-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH1-EN': arts['A-CH1-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch01-measure-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Six paragraph units of the English chapter 1 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=6, registered_claims=len(claims),
                         note='Reasoning and value paragraphs (the scene, three senses of measure, the strongest objection, disability is not a verdict, cells as who, seen and missed, caution, two accounts, the five questions) make no source claim. Abstract depth throughout; the synthetic claim is formal.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH1-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent domain, statistical or disability-studies review of these claims (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH1-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All four studies read at abstract depth here; CAPABLE 12-month results, the healthspan paper aggregates (X21, X61) and CALERIE participant overlap (X29, X31, X49) unresolved',
                 next_action='Read the full texts; bind the relevant tables as excerpts',
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
