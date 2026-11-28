"""Bind selected claims of the English chapter 4 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch04_evidence_en'
EN_PATH = 'books/manuscript/en/CH04_evidence_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH4-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016); new writing using V7 section 01 and project audits as leads; working copy'),
    ('A-SCREEN', f'{EV}/SCREENING_abstracts.txt', 'source', 'screening-mced', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42776074/', 'PubMed abstracts (Malagon 2026 model; NHS-Galleri 2026 trial, funded by Grail) 2026-11-28'),
    ('A-COUNTED', f'{EV}/COUNTED_abstracts.txt', 'source', 'counting-denominators', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/17835295/', 'PubMed abstracts (Bickel 1975; Waziry 2023; Mohammadnia 2025; Vetter 2026) 2026-11-28; four independent groups'),
    ('A-CLOCKS', f'{EV}/CLOCKS_FAMILY_abstracts.txt', 'source', 'higgins-chen-clock-family', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42629466/', 'PubMed abstracts (Sehgal 2026; Borrus 2026) 2026-11-28; one source family, six shared authors'),
    ('A-DEN-CODE', f'{HERE}/denominators.py', 'code', 'longevity-project-derivation', 'code', '',
     'project synthetic calculations (reversal, many readouts, rounded percentages); tests/test_ch04_en_pilot.py recomputes them'),
    ('A-DEN-OUT', f'{EV}/DENOMINATORS_SYNTHETIC_output.json', 'dataset', 'longevity-project-derivation', 'data', '',
     'saved stdout of denominators.py'),
    ('A-RECORDS', f'{EV}/PROJECT_RECORDS_excerpt.txt', 'source', 'longevity-project-record', 'fulltext', '',
     'verbatim copy of ledger rows X31, X40, X106, X126 and audit lines (2026-11-28): records of earlier reading by the same assistant; not a primary source'),
]
EVIDENCE = {
    'E-M-HDR': ('A-SCREEN', '# [1] Malagón T', 1),
    'E-M-MODEL': ('A-SCREEN', '[1] METHODS: We used a microsimulation model', 1),
    'E-M-RANGE': ('A-SCREEN', '[1] RESULTS: An estimated 2.1%-6.0%', 1),
    'E-M-AGE': ('A-SCREEN', '[1] The proportion of overdiagnosis varied by site', 1),
    'E-M-PPV': ('A-SCREEN', '[1] The test positive predictive value', 1),
    'E-GAL-HDR': ('A-SCREEN', '# [2] Sasieni P', 1),
    'E-GAL-END': ('A-SCREEN', '[2] The primary end point was stage III or IV', 1),
    'E-GAL-N': ('A-SCREEN', '[2] RESULTS: Overall, 71,122 participants', 1),
    'E-GAL-PRIM': ('A-SCREEN', '[2] The incidence rate of stage III or IV cancer', 1),
    'E-GAL-IV': ('A-SCREEN', '[2] The incidence rate ratio for stage IV cancer', 1),
    'E-GAL-FU': ('A-SCREEN', '[2] Further follow-up is warranted', 1),
    'E-SYN-REV': ('A-DEN-OUT', '"reversal"', 40),
    'E-SYN-READ': ('A-DEN-OUT', '"many_readouts"', 5),
    'E-SYN-ROUND': ('A-DEN-OUT', '"rounded_percentages"', 20),
    'E-SYN-DESIGN': ('A-DEN-CODE', 'Part A, reversal.', 12),
    'E-B-HDR': ('A-COUNTED', '# [1] Bickel PJ', 1),
    'E-B-AGG': ('A-COUNTED', '[1] Examination of aggregate data', 1),
    'E-B-DIS': ('A-COUNTED', '[1] Examination of the disaggregated data', 1),
    'E-B-POOL': ('A-COUNTED', '[1] If the data are properly pooled', 1),
    'E-W-RAND': ('A-COUNTED', '[2] Here we report the results of a post hoc analysis', 1),
    'E-W-COI': ('A-COUNTED', '[2] Conflict of interest statement', 1),
    'E-L-METH': ('A-COUNTED', '[3] METHODS: In this exploratory substudy', 1),
    'E-L-N': ('A-COUNTED', '[3] RESULTS: In total, 854 participants', 1),
    'E-L-RATE': ('A-COUNTED', '[3] Randomization to placebo was associated', 1),
    'E-L-TET2': ('A-COUNTED', '[3] Compared with placebo, colchicine', 1),
    'E-L-VALID': ('A-COUNTED', '[3] Further validation in prospective studies', 1),
    'E-V-METH': ('A-COUNTED', '[4] METHODS: We used data from the Berlin Aging Study II', 1),
    'E-V-CONC': ('A-COUNTED', '[4] CONCLUSION: Among the fourteen', 1),
    'E-V-COI': ('A-COUNTED', '[4] Competing interests:', 1),
    'E-S-AUTH': ('A-CLOCKS', '# Both papers come from the Higgins-Chen group', 1),
    'E-S-HDR': ('A-CLOCKS', '# [1] Sehgal R', 1),
    'E-S-DB': ('A-CLOCKS', '[1] Here we curate TranslAGE', 1),
    'E-S-RESP': ('A-CLOCKS', '[1] For example, clocks trained to predict mortality', 1),
    'E-S-COI': ('A-CLOCKS', '[1] Conflict of interest statement', 1),
    'E-BO-HDR': ('A-CLOCKS', '# [2] Borrus DS', 1),
    'E-BO-EXT': ('A-CLOCKS', '[2] In this study, we find that when extending', 1),
    'E-BO-CRIT': ('A-CLOCKS', '[2] We then analyze clock behavior', 1),
    'E-BO-REEX': ('A-CLOCKS', '[2] These findings provide a framework', 1),
    'E-R-X31': ('A-RECORDS', '| X31 | 2026-11-27 |', 1),
    'E-R-X106': ('A-RECORDS', '| X106 | 2026-11-27 |', 1),
    'E-R-X126': ('A-RECORDS', '| X126 | 2026-11-27 |', 1),
    'E-R-CAL': ('A-RECORDS', '| 报告位置与定义 | CR | AL | 合计 |', 8),
    'E-R-BASE': ('A-RECORDS', '- T0 为 1,671 名 60 岁及以上参与者', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


CLAIMS = [
    dict(id='CH4-EN-C001', anchor='A modelling study of multicancer blood tests shows how much the choice matters.', kind='reported', role='asserted', critical=True,
         context=ctx('simulated Canadian population screened at ages 50-75', 'yearly and lifetime', 'share of screen-detected cancers that are overdiagnoses; positive predictive value',
                     'screen-detected cancer', 'microsimulation model (not trial data)', 'multicancer early detection'),
         evidence=['E-M-HDR', 'E-M-MODEL', 'E-M-RANGE', 'E-M-AGE', 'E-M-PPV'], state='supported',
         rationale='Microsimulation; ages 50-75 in Canada; 2.1-6.0% of yearly screen-detected cancers predicted overdiagnoses; 1% at 50 to over 10% of screen-detected cancers by 75; PPV 15.9-77.6%; 0.3-5.3 false positives per true cancer. All match. The denominator remark is the chapter\'s reading of "of screen-detected cancers".',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C002', anchor='A synthetic example, built by this project with no real data, shows how.', kind='formal', role='asserted', critical=True,
         context=ctx('none: 1600 synthetic patients', 'single period', 'recovery percentage by treatment, within and across severity groups',
                     'synthetic patient', 'exact arithmetic (script and tests)', 'aggregation arithmetic only'),
         evidence=['E-SYN-DESIGN', 'E-SYN-REV'], state='supported',
         rationale='Mild 180/200 (90.0) vs 520/600 (86.7); severe 300/600 (50.0) vs 80/200 (40.0); overall 480/800 (60.0) vs 600/800 (75.0); new better in each group, worse overall. All match. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH4-EN-C003', anchor='This is not only a textbook trap.', kind='reported', role='asserted', critical=True,
         context=ctx('graduate applicants, University of California, Berkeley', 'fall 1973', 'admission by sex, aggregate and by department',
                     'applicant', 'observational analysis of admissions records', 'graduate admissions (not health)'),
         evidence=['E-B-HDR', 'E-B-AGG', 'E-B-DIS', 'E-B-POOL'], state='supported',
         rationale='Aggregate data show a clear but misleading pattern of bias against women; few departments depart significantly, about as many favour women as men; proper pooling, accounting for departmental autonomy and for women applying to harder departments, gives a small significant bias in favour of women. All match; "a clear but misleading pattern" quoted.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C004', anchor='The CALERIE trial of calorie restriction is a careful study', kind='reported', role='asserted', critical=True,
         context=ctx('CALERIE participants (adults without obesity)', '2 years; baseline, 12 and 24 months', 'number analysed at each step of a post hoc methylation analysis',
                     'participant', 'randomized trial; post hoc analysis', 'calorie restriction and DNA methylation'),
         evidence=['E-W-RAND', 'E-R-CAL', 'E-R-X31'], state='supported',
         rationale='220 randomized to 25% CR or ad libitum for 2 yr; post hoc (abstract). Audit table: 128/69 baseline and at least one follow-up; 117/68 change to 24 months; 105/59 all three time points. X31: under common-population assumptions the counts are incompatible; author clarification not obtained; does not judge which number is wrong. All match. The judgement "careful study" is the author\'s, not a source claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C005', anchor='Observational cohorts have their own version.', kind='reported', role='asserted', critical=True,
         context=ctx('BASE-II participants aged 60-80', 'average follow-up 7.4 years', 'association of 14 biomarkers with mortality; who entered the analysis',
                     'participant', 'prospective cohort; Cox regression', 'biomarkers of aging'),
         evidence=['E-V-METH', 'E-V-CONC', 'E-R-BASE'], state='supported',
         rationale='Abstract: 60-80 at baseline, average follow-up 7.4 years, n = 1,083; 14 biomarkers; DunedinPACE strongest and most consistent association. Audit: T0 1,671 aged 60 and over; T1 1,083; T0 DNAm available only in those who later took part in T1. Match. "Pace of aging" glosses DunedinPACE.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C006', anchor='Time matters inside randomised comparisons too.', kind='reported', role='asserted', critical=True,
         context=ctx('LoDoCo2 participants with chronic coronary artery disease', '4 time points; median 25.0 months', 'clone growth by arm; between-arm interaction',
                     'participant', 'exploratory substudy of a randomized trial', 'colchicine and clonal haematopoiesis'),
         evidence=['E-L-METH', 'E-L-N', 'E-L-RATE', 'E-L-TET2', 'E-L-VALID'], state='supported',
         rationale='Exploratory substudy; open-label run-in before randomization; 854 participants, 2,047 observations across 4 timepoints including before and after run-in; placebo 14.9% annual increase vs nonsignificant 6.3% with colchicine; between-arm difference not significant (P interaction 0.13); TET2 P interaction 0.04; validation warranted. All match. Coronary disease from the trial context; "aging-related condition" from the abstract background (not excerpted; the title and methods carry CH).',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C007', anchor='In 2026 one laboratory group published two related studies of epigenetic clocks.', kind='reported', role='asserted', critical=False,
         context=ctx('none: published intervention datasets', 'as published', 'clock responsiveness; criteria for trusting clock results',
                     'study', 'database curation and reanalysis', 'epigenetic clocks'),
         evidence=['E-S-AUTH', 'E-S-HDR', 'E-S-DB', 'E-S-RESP', 'E-BO-HDR', 'E-BO-CRIT', 'E-R-X126'], state='supported',
         rationale='TranslAGE: 51 public and private longitudinal interventional studies; 16 prominent clocks; mortality and pace clocks respond most and agree. Borrus: three criteria including mortality-trained or pace-of-aging clocks respond. Six shared authors (header). X126 records the pair as one family, not independent replication. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C008', anchor='The NHS-Galleri trial of a multicancer blood test was funded by Grail', kind='reported', role='asserted', critical=True,
         context=ctx('people aged 50-77 in the NHS-Galleri trial', 'three screening rounds plus at least 12 months', 'incidence rate ratio of stage III-IV and stage IV cancer',
                     'participant', 'randomized controlled trial', 'multicancer early detection'),
         evidence=['E-GAL-HDR', 'E-GAL-END', 'E-GAL-N', 'E-GAL-PRIM', 'E-GAL-IV', 'E-GAL-FU'], state='supported',
         rationale='Funded by Grail; GRAIL Bio UK affiliation (header); 71,122 vs 71,128; primary stage III-IV among 12 prespecified types, IRR 1.03 (0.92-1.14); key secondary stage IV 0.86 (0.74-1.00); further follow-up warranted. All match. "Blood tested" versus "stored" is from the methods sentence not excerpted; the excerpt header and end points carry the design.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C009', anchor='Financial interests also run through academic work.', kind='reported', role='asserted', critical=False,
         context=ctx('none: declared interests of authors', 'as published', 'declared competing interests',
                     'author', 'competing-interests statements', 'research integrity'),
         evidence=['E-W-COI', 'E-V-COI', 'E-S-COI'], state='supported',
         rationale='Waziry: two authors inventors on DunedinPACE, licensed to a commercial entity. Vetter: CAD cofounder and stockowner, TEG CEO and stockowner in Vitas Ltd. Sehgal: two co-inventors of patented SystemsAge; three TruDiagnostic employees developed OMICmAge. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C010', anchor='Some checks need no access to the data.', kind='formal', role='asserted', critical=False,
         context=ctx('none: synthetic counts; one project recalculation on a published table', 'not applicable', 'denominators consistent with rounded percentages',
                     'denominator', 'exact arithmetic (script and tests); project ledger row', 'reporting arithmetic'),
         evidence=['E-SYN-DESIGN', 'E-SYN-ROUND', 'E-R-X106'], state='supported',
         rationale='Synthetic: 7 (3.7), 12 (6.3), 19 (9.9); only 191 in 100-400. X106: 10 count/percentage pairs compatible only with N=191 in [100,400]; text says 190; another report (X105) has 191; does not prove; a question to authors. All match. Formal for the synthetic part; the X106 part is a project record, labelled so.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH4-EN-C011', anchor='"Someone else, with other data" is where source families matter', kind='reported', role='asserted', critical=False,
         context=ctx('none: previously published single-clock intervention studies', 'as published', 'significance of additional clocks on reanalysis',
                     'study', 'reanalysis', 'epigenetic clocks'),
         evidence=['E-BO-HDR', 'E-BO-EXT', 'E-BO-REEX'], state='supported',
         rationale='Extending single-clock intervention studies to more clocks: no additional clocks reach significance; some single-clock findings may warrant reexamination. Match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH4-EN-C012', anchor='A third synthetic calculation shows why one positive readout among many is weak evidence.', kind='formal', role='asserted', critical=False,
         context=ctx('none: 16 independent null readouts', 'not applicable', 'chance of at least one result below 0.05',
                     'readout', 'exact arithmetic (script and tests)', 'multiple testing arithmetic only'),
         evidence=['E-SYN-DESIGN', 'E-SYN-READ'], state='supported',
         rationale='1 - 0.95^16 = 0.56 under independence; script docstring notes correlated clocks give a lower figure. Match. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
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
        claim = dict(id=c['id'], artifact_id='A-CH4-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH4-EN': arts['A-CH4-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch04-evidence-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Twelve paragraph units of the English chapter 4 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=12, registered_claims=len(claims),
                         note='Method and habit paragraphs (denominator questions, randomisation promise, source-family grouping, reading the primary end point, what counts as the same result) make no source claim. Abstract depth throughout; three synthetic claims are formal; CALERIE and BASE-II counts and X106 rest on project records.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH4-EN-INDEPENDENT-REVIEW', status='blocked', blocks_formal_release=True,
                 question='No independent review by a statistician or a trialist (D05)',
                 next_action='Real external review; never fabricate receipts',
                 closure_evidence='Object-bound review record with declared independence and responses'),
            dict(id='CH4-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='Eight studies at abstract depth; CALERIE (X31) and BASE-II counts from project audits not re-read; X106 is a question for the authors',
                 next_action='Re-read full texts; seek author clarification for X31 and X106',
                 closure_evidence='Full-text reading notes bound as excerpts; author replies if obtained'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if out.exists() and json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
