"""Bind selected claims of the English chapter 2 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch02_clocks_en'
EN_PATH = 'books/manuscript/en/CH02_clocks_draft_en.md'
EV = f'{HERE}/evidence'
HALE_AUDIT = 'knowledge_base/HALE_METHODS_VERSIONS_AND_TIME_AUDIT_2026-11-27.md'
ARTIFACTS = [
    ('A-CH2-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016); new writing using V6 section 04 and V7 section 21 as leads; working copy'),
    ('A-WEIGHTS', f'{EV}/DISABILITY_WEIGHTS_abstract.txt', 'source', 'study-Salomon-GBD2013-disability-weights', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/26475018/', 'PubMed abstract 2026-11-28'),
    ('A-MICE', f'{EV}/DR_MICE_abstract.txt', 'source', 'study-DiFrancesco-DR-mice', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/39385029/', 'PubMed abstract and COI 2026-11-28'),
    ('A-GAP', f'{EV}/HEALTHSPAN_GAP_abstract.txt', 'source', 'study-Garmany-healthspan-gap', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/39661386/', 'PubMed abstract and COI 2026-11-28 (fuller excerpt than the ch1 pilot)'),
    ('A-LIMIT', f'{EV}/LIFESPAN_LIMIT_abstracts.txt', 'source', 'studies-lifespan-limit', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/29954979/', 'PubMed abstracts (Dong 2016; Barbi 2018; Efimov 2026) 2026-11-28; three independent groups'),
    ('A-PC-CODE', f'{HERE}/period_cohort.py', 'code', 'longevity-project-derivation', 'code', '',
     'project synthetic period/cohort and tail calculation; tests/test_ch02_en_pilot.py recomputes it'),
    ('A-PC-OUT', f'{EV}/PERIOD_COHORT_SYNTHETIC_output.json', 'dataset', 'longevity-project-derivation', 'data', '',
     'saved stdout of period_cohort.py'),
    ('A-LEDGER', f'{EV}/LEDGER_X21_X61_excerpt.txt', 'source', 'longevity-project-record', 'fulltext', '',
     'verbatim copy of ledger rows X21 and X61 (2026-11-28): records of earlier full-text reading by the same assistant; not a primary source'),
    ('A-HALE', HALE_AUDIT, 'source', 'longevity-project-record', 'fulltext', '',
     'project HALE methods audit (2026-11-27), same assistant, from the paper and WHO method documents; not a primary source'),
]
EVIDENCE = {
    'E-PC-MODEL': ('A-PC-CODE', 'Model: a Gompertz hazard', 4),
    'E-PC-PERIOD': ('A-PC-OUT', '"period_year0": {', 6),
    'E-PC-COHORT': ('A-PC-OUT', '"cohort_born_year0": {', 2),
    'E-PC-DIFF': ('A-PC-OUT', '"cohort_minus_period_years"', 1),
    'E-PC-TAILDESIGN': ('A-PC-CODE', 'Tail comparison', 3),
    'E-PC-Q105': ('A-PC-OUT', '"annual_death_probability_at_105"', 1),
    'E-PC-TAIL': ('A-PC-OUT', '"tail_given_alive_at_105": {', 12),
    'E-PC-RATIO': ('A-PC-OUT', '"flat_over_rising_ratio": {', 5),
    'E-W-DALY': ('A-WEIGHTS', 'BACKGROUND: The Global Burden of Disease (GBD) study', 1),
    'E-W-SURVEY': ('A-WEIGHTS', 'METHODS: We analysed data from new web-based surveys', 1),
    'E-W-PAIRED': ('A-WEIGHTS', 'Surveys used paired comparison questions', 1),
    'E-W-SCALE': ('A-WEIGHTS', 'rescaled results to disability weight units', 1),
    'E-W-REVISED': ('A-WEIGHTS', 'For health state descriptions that were revised', 1),
    'E-W-INTERP': ('A-WEIGHTS', 'disability weights are sensitive to particular details', 1),
    'E-M-DESIGN': ('A-MICE', 'on the health and survival of 960 genetically diverse female mice', 1),
    'E-M-LS': ('A-MICE', 'both resulted in lifespan extension in proportion', 1),
    'E-M-INCONS': ('A-MICE', 'Health effects differed between interventions', 1),
    'E-M-40': ('A-MICE', '40% caloric restriction had the strongest', 1),
    'E-M-METAB': ('A-MICE', 'Metabolic responses to dietary restriction', 1),
    'E-M-SYN': ('A-MICE', 'improving health and extending lifespan are not synonymous', 1),
    'E-M-COI': ('A-MICE', 'are employees of Calico Life Sciences', 1),
    'E-G-DEF': ('A-GAP', 'IMPORTANCE: Health-adjusted life expectancy', 1),
    'E-G-WHO': ('A-GAP', 'World Health Organization (WHO) Global Health Observatory', 1),
    'E-G-183': ('A-GAP', 'The 183 WHO member states were investigated.', 1),
    'E-G-2DEC': ('A-GAP', 'EXPOSURES: Data represent 2 decades', 1),
    'E-G-96': ('A-GAP', 'extending to 9.6 years', 1),
    'E-G-SEX': ('A-GAP', '2.4 (0.5) years wider than men', 1),
    'E-G-ASSOC': ('A-GAP', 'positively associated with the burden of noncommunicable diseases', 1),
    'E-G-COI': ('A-GAP', 'Conflict of Interest Disclosures: None reported.', 1),
    'E-LED-X21': ('A-LEDGER', '| X21 | 2026-11-27 |', 1),
    'E-LED-X61': ('A-LEDGER', '| X61 | 2026-11-27 |', 1),
    'E-HALE-AGG': ('A-HALE', '研究在 2024 年初查询 WHO GHO', 1),
    'E-HALE-VERS': ('A-HALE', '[当前 WHO 元数据](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752)说明', 1),
    'E-L-DONG': ('A-LIMIT', '[1] Here, by analysing global demographic data', 1),
    'E-L-DONG2': ('A-LIMIT', '[1] Our results strongly suggest', 1),
    'E-L-BARBI-N': ('A-LIMIT', '[2] In this study, we estimated hazard rates', 1),
    'E-L-BARBI-FLAT': ('A-LIMIT', '[2] We observed level hazard curves', 1),
    'E-L-EF-SOM': ('A-LIMIT', '[3] Somatic mutations accumulate with age', 1),
    'E-L-EF-MODEL': ('A-LIMIT', '[3] We developed an incremental modeling framework', 1),
    'E-L-EF-156': ('A-LIMIT', '[3] Our analysis reveals fundamental asymmetry', 1),
    'E-L-EF-146': ('A-LIMIT', '[3] Multi-organ integration predicts', 1),
    'E-L-EF-READ': ('A-LIMIT', '[3] This substantial yet incomplete reduction', 1),
    'E-L-EF-COI': ('A-LIMIT', '[3] Conflict of interest statement', 1),
    'E-L-HDR': ('A-LIMIT', '# [1] Dong X, Milholland B, Vijg J.', 1),
    'E-L-HDR2': ('A-LIMIT', '# [2] Barbi E, Lagona F', 1),
    'E-L-HDR3': ('A-LIMIT', '# [3] Efimov E, Fedotov V', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


SYN = ctx('none: one synthetic population with a Gompertz hazard', 'synthetic calendar years and ages up to 130',
          'period and cohort life expectancy; spread of ages at death; tail survival from 105 under two hazard assumptions',
          'synthetic person', 'numerical integration (script and tests)', 'life-table arithmetic only')
CLAIMS = [
    dict(id='CH2-EN-C001', anchor='A small synthetic calculation, built by this project with no real data, shows the size of the difference.',
         kind='formal', role='asserted', critical=True, context=SYN,
         evidence=['E-PC-MODEL', 'E-PC-PERIOD', 'E-PC-COHORT', 'E-PC-DIFF'], state='supported',
         rationale='Gompertz hazard falling 1 percent per calendar year; period LE 73.4, cohort LE 80.8, difference 7.4; 0.43 of the period table die before LE; quartile ages 66.4 and 82.9. All match the saved output and the script docstring. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH2-EN-C002', anchor='Where do the weights come from?', kind='reported', role='asserted', critical=True,
         context=ctx('web-survey respondents aged 18-65 in four European countries plus GBD 2010 survey respondents', '2013 (with earlier GBD 2010 data)',
                     'disability weights from paired comparisons; changes after description revisions', 'health state',
                     'survey with probit analysis', 'Global Burden of Disease disability weights'),
         evidence=['E-W-DALY', 'E-W-SURVEY', 'E-W-PAIRED', 'E-W-SCALE', 'E-W-REVISED', 'E-W-INTERP'], state='supported',
         rationale='DALYs need disability weights for non-fatal outcomes; web surveys of 18-65-year-olds in Hungary, Italy, the Netherlands and Sweden combined with GBD 2010 data; paired comparison of two hypothetical individuals; rescaled 0 (no loss) to 1 (equivalent to death); hearing loss 0.033 to 0.215 and treated spinal cord lesion below the neck 0.047 to 0.296 after revised descriptions; sensitive to description details, robust to duration. All match; the source uses a middle-dot decimal mark.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH2-EN-C003', anchor='Even where whole lives can be watched, health and length do not simply move together.', kind='reported', role='asserted', critical=True,
         context=ctx('960 genetically diverse female mice', 'whole lifespan', 'lifespan and health traits under graded caloric restriction and intermittent fasting',
                     'animal', 'controlled animal experiment', 'dietary restriction in mice'),
         evidence=['E-M-DESIGN', 'E-M-LS', 'E-M-INCONS', 'E-M-40', 'E-M-METAB', 'E-M-SYN', 'E-M-COI'], state='supported',
         rationale='960 genetically diverse female mice; CR and IF extended lifespan in proportion to restriction; health effects differed and related inconsistently to lifespan extension; 40% CR strongest extension with lean-mass loss and immune changes that could confer infection susceptibility; reduced adiposity and lower fasting glucose not associated with longer lifespan; "not synonymous"; Calico employees. All match.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH2-EN-C004', anchor='The difference between life expectancy and health-adjusted life expectancy is often called the healthspan', kind='reported', role='asserted', critical=True,
         context=ctx('183 WHO member states (national-level WHO estimates)', 'two decades', 'healthspan-lifespan gap; sex difference; association with morbidity and mortality',
                     'country / global aggregate', 'retrospective cross-sectional analysis of WHO estimates', 'population health statistics'),
         evidence=['E-G-DEF', 'E-G-WHO', 'E-G-183', 'E-G-2DEC', 'E-G-96', 'E-G-SEX', 'E-G-ASSOC', 'E-G-COI'], state='supported',
         rationale='WHO data, 183 member states, two decades, widened globally to 9.6 years, wider for women, positively associated with NCD burden and total morbidity and negatively with mortality. All match the abstract.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH2-EN-C005', anchor="Two further cautions come from this project's reading of the full paper", kind='reported', role='asserted', critical=True,
         context=ctx('Garmany and Terzic 2024; WHO HALE series', '2000-2019 analysis; later WHO releases', 'aggregate definitions, version comparability, annualisation divisor',
                     'report / data release', "project's reading of the paper's methods and results and of WHO method documents", 'population health statistics'),
         evidence=['E-LED-X21', 'E-LED-X61', 'E-HALE-AGG', 'E-HALE-VERS'], state='supported',
         rationale='Global 9.6 versus 183-country mean 9.2 as different aggregates (X21, audit section 1); WHO HALE uses WHO life tables and YLD mainly based on GBD (audit section 1); the current WHO series is not directly comparable with older releases (audit section 1); (Estimate2019-Estimate2000)/20 versus 19 intervals if annual end points, unresolved without data (X61). All from project records by the same assistant, cited as such; not primary sources and not independent.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH2-EN-C006', anchor='Two well-known papers seem to answer in opposite directions.', kind='reported', role='asserted', critical=True,
         context=ctx('global demographic data (Dong); all documented Italians aged 105+ in 2009-2015 (Barbi)', 'Dong: to 2016; Barbi: 2009-2015',
                     'trend in survival improvement and record age at death; hazard at extreme ages', 'population / person', 'demographic analyses', 'human mortality at extreme ages'),
         evidence=['E-L-HDR', 'E-L-DONG', 'E-L-DONG2', 'E-L-HDR2', 'E-L-BARBI-N', 'E-L-BARBI-FLAT'], state='supported',
         rationale='Dong, Milholland and Vijg 2016: improvements in survival decline after 100; oldest-person age at death not increased since the 1990s; maximum lifespan fixed and subject to natural constraints. Barbi 2018: all Italians aged 105+ in 2009-2015, 3836 documented cases; hazard essentially constant beyond 105. All match; "and colleagues" stands for the four co-authors in the header.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH2-EN-C007', anchor='The same synthetic population from section 1 shows how much rides on an assumption about the tail.',
         kind='formal', role='asserted', critical=True, context=SYN,
         evidence=['E-PC-TAILDESIGN', 'E-PC-Q105', 'E-PC-TAIL', 'E-PC-RATIO'], state='supported',
         rationale='Year-0 rates; death probability at 105 0.66; reach 115 given 105: 1.6e-08 rising versus 2.2e-05 flat, ratio 1400; reach 122 ratio 7.1e11 (710 billion). All match the saved output. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH2-EN-C008', anchor='A third kind of answer comes from models of mechanism.', kind='reported', role='asserted', critical=True,
         context=ctx('none: a population survival model', 'model time', 'median lifespan with all hallmarks removed except somatic mutations',
                     'model population', 'mathematical model', 'somatic mutations and lifespan'),
         evidence=['E-L-HDR3', 'E-L-EF-SOM', 'E-L-EF-MODEL', 'E-L-EF-156', 'E-L-EF-146', 'E-L-EF-READ', 'E-L-EF-COI'], state='supported',
         rationale='NPJ Aging 2026; model removes all hallmarks except somatic mutations; mutations accumulate with age and can cause cell death; post-mitotic neurons and cardiomyocytes are bottlenecks, 1759 to 156 years median; multi-organ 146-194 median; cannot alone account for observed mortality, comparable contributions from other hallmarks; title says upper bound. All match. "Cells that no longer divide" renders "post-mitotic"; "heart muscle cells" renders "cardiomyocytes".',
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
        claim = dict(id=c['id'], artifact_id='A-CH2-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH2-EN': arts['A-CH2-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch02-clocks-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Eight paragraph units of the English chapter 2 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=8, registered_claims=len(claims),
                         note='Reasoning and value paragraphs (the newspaper page, period table definition, what a weight is, the strongest counterexample, two ledgers, reading the gap association, matching each limit paper to its statistic, the consumer clock) make no source claim. Abstract depth throughout; two synthetic claims are formal; one claim rests on project records.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH2-EN-INDEPENDENT-REVIEW', status='blocked', blocks_formal_release=True,
                 question='No independent demographic, health-economic or disability-studies review of these claims (D05)',
                 next_action='Real external review; never fabricate receipts',
                 closure_evidence='Object-bound review record with declared independence and responses'),
            dict(id='CH2-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All five studies read at abstract depth; healthspan paper aggregation (X21) and divisor (X61) open; comments on Dong and Barbi unread; V7 tail figures for the mutation model unchecked',
                 next_action='Read the full texts and comments; bind the relevant tables as excerpts',
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
