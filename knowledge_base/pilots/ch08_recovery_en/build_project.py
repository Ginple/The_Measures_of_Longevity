"""Bind selected claims of the English chapter 8 draft (DEC-016, written English-first) to exact source spans.

Run deliberately to (re)bind after a reviewed change; tests never run it. Spans are located by anchor
text and frozen into project.json as line numbers, exact text and sha256, so a later edit to the
chapter, to an excerpt or to the synthetic-model memo shows up as drift in `inspect_project`.
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

HERE = 'knowledge_base/pilots/ch08_recovery_en'
EN_PATH = 'books/manuscript/en/CH08_recovery_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH8-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016), written English-first from V6-16/V7-17 source material; working copy'),
    ('A-CONCEPT', f'{EV}/RESILIENCE_CONCEPT_abstracts.txt', 'source', 'resilience-concept-literature', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/18938195/', 'PubMed abstracts (Varadhan 2008; Manning 2026) 2026-11-28'),
    ('A-CHALL', f'{EV}/CHALLENGE_TESTS_abstracts.txt', 'source', 'challenge-test-cohorts-TILDA-BLSA', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/27330018/', 'PubMed abstracts (McCrory 2016; Schumock 2024) 2026-11-28'),
    ('A-HOSP', f'{EV}/HOSPITAL_RECOVERY_abstract.txt', 'source', 'study-Boyd-hospital-ADL-recovery', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/19093915/', 'PubMed abstract 2026-11-28'),
    ('A-EXTRAP', f'{EV}/EXTRAPOLATION_abstract.txt', 'source', 'study-Pyrkov-Gero-DOSI', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/34035236/', 'PubMed abstract and COI 2026-11-28'),
    ('A-WITHDRAW', f'{EV}/WITHDRAWAL_abstract.txt', 'source', 'trial-STEP1-extension', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/35441470/', 'PubMed abstract and COI 2026-11-28'),
    ('A-SR', 'knowledge_base/experiments/SR_SNAPSHOT_IDENTIFIABILITY_2026-11-27.md', 'code',
     'longevity-project-derivation', 'fulltext', '', 'project synthetic-model memo; script and tests alongside'),
]
EVIDENCE = {
    'E-VAR-PROP': ('A-CONCEPT', 'based on the stimulus-response experimental paradigm', 1),
    'E-VAR-CORE': ('A-CONCEPT', 'signifies a loss of resilience in homeostatic regulation', 1),
    'E-VAR-BEN': ('A-CONCEPT', 'establishment of the value of provocative tests', 1),
    'E-MAN-RANGE': ('A-CONCEPT', 'general notions of recovery or adaptation', 1),
    'E-MAN-PHYS': ('A-CONCEPT', 'the term physical was rarely explicitly defined', 1),
    'E-MAN-TWO': ('A-CONCEPT', 'Only two studies referenced formal models of resilience', 1),
    'E-HRR-N': ('A-CHALL', 'A total of 4475 participants completed an active stand', 1),
    'E-HRR-BEAT': ('A-CHALL', 'Beat-to-beat heart rate', 1),
    'E-HRR-FU': ('A-CHALL', 'mean follow-up duration of 4.3 years', 1),
    'E-HRR-6': ('A-CHALL', 'increased the hazard of mortality by 6%', 1),
    'E-HRR-Q': ('A-CHALL', 'Sixty-nine participants in the slowest HRR quartile', 1),
    'E-OGTT-N': ('A-CHALL', 'on 1,120 adults older than 50 years', 1),
    'E-OGTT-MODEL': ('A-CHALL', 'First, we fit OGTT curves with the Ackerman model', 1),
    'E-OGTT-36': ('A-CHALL', 'unable to adequately fit 36% of the OGTT curves', 1),
    'E-OGTT-NULL': ('A-CHALL', 'found no associations between Ackerman model summaries', 1),
    'E-OGTT-FPC': ('A-CHALL', 'The second functional principal component score', 1),
    'E-HOSP-SET': ('A-HOSP', 'SETTING: Tertiary care hospital', 1),
    'E-HOSP-POP': ('A-HOSP', 'PARTICIPANTS: Older (aged >or=70)', 1),
    'E-HOSP-TIME': ('A-HOSP', 'at preadmission baseline and 1, 3, 6, and 12 months', 1),
    'E-HOSP-NEW': ('A-HOSP', '41.3% died, 28.6% were alive', 1),
    'E-HOSP-BASE': ('A-HOSP', 'Of those discharged at baseline function, 17.8% died', 1),
    'E-HOSP-1M': ('A-HOSP', 'recovery by 1 month was associated with long-term outcomes', 1),
    'E-PYR-DATA': ('A-EXTRAP', 'database of CBC measurements from a consumer diagnostics laboratory', 1),
    'E-PYR-LOSS': ('A-EXTRAP', 'progressive loss of physiological resilience', 1),
    'E-PYR-EXTRAP': ('A-EXTRAP', 'critical point of 120 - 150 years of age', 1),
    'E-PYR-LIMIT': ('A-EXTRAP', 'signifies a fundamental or absolute limit of human lifespan', 1),
    'E-PYR-COI': ('A-EXTRAP', 'Conflict of interest statement: P.O.F. is a shareholder of Gero PTE.', 1),
    'E-STEP-DESIGN': ('A-WITHDRAW', 'randomized 1961 adults', 1),
    'E-STEP-STOP': ('A-WITHDRAW', 'At week 68, treatments (including lifestyle intervention) were discontinued.', 1),
    'E-STEP-EXPL': ('A-WITHDRAW', 'All analyses in the extension were exploratory.', 1),
    'E-STEP-327': ('A-WITHDRAW', 'Extension analyses included 327 participants.', 1),
    'E-STEP-LOSS': ('A-WITHDRAW', 'mean weight loss was 17.3%', 1),
    'E-STEP-REGAIN': ('A-WITHDRAW', 'regained 11.6 (SD: 7.7)', 1),
    'E-STEP-CM': ('A-WITHDRAW', 'Cardiometabolic improvements seen from week 0 to week 68', 1),
    'E-STEP-COI': ('A-WITHDRAW', 'KKa reports being employed by and owning stock in Novo Nordisk', 1),
    'E-SR-SCOPE': ('A-SR', '**仅为合成教学模型。**', 1),
    'E-SR-A': ('A-SR', '**发现 A：读数匹配，生存曲线却交叉。**', 1),
    'E-SR-LAMBDA': ('A-SR', '- 局部回复率（按存活者平均水平近似计算）', 1),
    'E-SR-C': ('A-SR', '**发现 C：只是暂时变年轻。**', 1),
    'E-SR-ID': ('A-SR', '**可识别条件**', 1),
    'E-SR-LIMIT': ('A-SR', '“回复率”取在存活者平均水平上', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


CLAIMS = [
    dict(id='CH8-EN-C001', anchor='Geriatricians have argued for this view for some time.', kind='reported', role='asserted', critical=False,
         context=ctx('none (conceptual proposal)', '2008', 'proposed framework for measuring loss of resilience in frailty', 'publication',
                     'conceptual and methods proposal', 'homeostatic regulation in older adults'),
         evidence=['E-VAR-PROP', 'E-VAR-CORE', 'E-VAR-BEN'], state='supported',
         rationale='Stimulus-response dynamical modelling, frailty as loss of resilience in homeostatic regulation, provocative tests and sentinel systems for screening all match. "Johns Hopkins group" is from the affiliation.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C002', anchor='The idea is old enough that one might expect a settled definition.', kind='reported', role='asserted', critical=False,
         context=ctx('peer-reviewed physical-resilience literature (PubMed, Web of Science)', 'review published 2026',
                     'how definitions of physical resilience vary', 'publication', 'scoping review', 'gerontology and rehabilitation'),
         evidence=['E-MAN-RANGE', 'E-MAN-PHYS', 'E-MAN-TWO'], state='supported',
         rationale='Range from general recovery/adaptation to post-perturbation trajectory models; "physical" rarely defined; only two studies referenced formal models; few distinguished resilience from adaptation or robustness. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C003', anchor='The first is as simple as standing up.', kind='reported', role='asserted', critical=True,
         context=ctx('4,475 community-dwelling adults aged 50+ (TILDA, nationally representative)', 'mean follow-up 4.3 years; 138 deaths',
                     'association of orthostatic heart-rate recovery speed with all-cause mortality', 'participant',
                     'prospective cohort with clinic-based active-stand test', 'beat-to-beat heart rate over 2 minutes after standing'),
         evidence=['E-HRR-N', 'E-HRR-BEAT', 'E-HRR-FU', 'E-HRR-6', 'E-HRR-Q'], state='supported',
         rationale='4,475; aged 50+; supine to stand; beat-to-beat over 2 minutes; 4.3 years; 138 deaths; strong predictor in first 20 s; 6% per 1 bpm between 10 and 20 s adjusted for established risk factors; 69 vs 14 deaths; 2.3 times. "Irish" from the TILDA affiliation. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C004', anchor='The second example is the oral glucose tolerance test', kind='reported', role='asserted', critical=True,
         context=ctx('1,120 adults over 50, Baltimore Longitudinal Study of Aging', 'single OGTT per analysis; survival follow-up (length not read)',
                     'association of mechanistic-model and descriptive OGTT curve summaries with gait speed and survival', 'participant',
                     'two-stage modelling in a cohort', '75 g oral glucose tolerance test'),
         evidence=['E-OGTT-N', 'E-OGTT-MODEL', 'E-OGTT-36', 'E-OGTT-NULL', 'E-OGTT-FPC'], state='supported',
         rationale='1,120 over 50 in BLSA; Ackerman parametric model and fPCA; 36% inadequate fits; no association of Ackerman summaries with gait speed or survival; second fPC associated with faster gait and better survival. "Two hours" is the standard OGTT duration and not quoted; acceptable explanatory gloss.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C005', anchor='A study of patients aged 70 and over', kind='reported', role='asserted', critical=True,
         context=ctx('patients aged 70+ nonelectively admitted to general medical services in two hospitals', '1993-1998 admissions; 12 months after discharge',
                     'death, sustained ADL decline or recovery to baseline ADL function after discharge', 'patient', 'observational cohort',
                     'basic activities of daily living'),
         evidence=['E-HOSP-SET', 'E-HOSP-POP', 'E-HOSP-TIME', 'E-HOSP-NEW', 'E-HOSP-BASE', 'E-HOSP-1M'], state='supported',
         rationale='Two hospital types; aged 70+; 1993-1998; 1/3/6/12 months; 41.3/28.6/30.1% versus 17.8% and 67%; recovery by 1 month associated with long-term outcomes. ADL examples (bathing, dressing, eating) are a standard gloss, not quoted.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C006', anchor='Using a large longitudinal database of complete blood counts', kind='reported', role='asserted', critical=True,
         context=ctx('customers of a consumer diagnostics laboratory with repeated blood counts', 'ages observed in the database; extrapolated beyond',
                     'age trend of autocorrelation (recovery) time of a blood-count mortality indicator; extrapolated divergence point', 'person-trajectory',
                     'longitudinal observational analysis with extrapolation', 'complete blood count'),
         evidence=['E-PYR-DATA', 'E-PYR-LOSS', 'E-PYR-EXTRAP', 'E-PYR-LIMIT', 'E-PYR-COI'], state='supported',
         rationale='Consumer lab CBC database; single indicator; broadening explained by loss of resilience measured as autocorrelation time; extrapolated divergence at 120-150; authors conclude a fundamental or absolute limit; five employees, one also shareholder, one advisory-board member; funded by the company. All match. The following paragraph (extrapolation is not an observation) is the chapter\'s reasoning, consistent with KERNEL §6 and ledger X86.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C007', anchor='A clear example comes from a large weight-loss trial.', kind='reported', role='asserted', critical=True,
         context=ctx('STEP 1: 1,961 randomized adults with BMI >=30 (or >=27 with comorbidity) without diabetes; extension subset of 327', 'treatment weeks 0-68; off-treatment follow-up to week 120',
                     'body-weight and cardiometabolic change after withdrawal', 'participant', 'off-treatment extension of a randomized trial (exploratory)',
                     'semaglutide 2.4 mg weekly plus lifestyle intervention'),
         evidence=['E-STEP-DESIGN', 'E-STEP-STOP', 'E-STEP-EXPL', 'E-STEP-327', 'E-STEP-LOSS', 'E-STEP-REGAIN', 'E-STEP-CM', 'E-STEP-COI'], state='supported',
         rationale='1,961 randomized; 68 weeks; all treatment including lifestyle stopped; 327 in extension; 17.3% loss; regained 11.6 points by week 120; net 5.6%; most cardiometabolic improvements reverted toward baseline; exploratory; manufacturer employees among authors. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH8-EN-C008', anchor="The project's synthetic model, introduced in chapter 6, makes the same point", kind='formal', role='asserted', critical=True,
         context=ctx('none: synthetic one-dimensional saturating-removal model with illustrative parameters, not fitted to any cohort',
                     'interventions from age 60; readings at 61 and 70', 'local recovery rate at matched readings; transient pulse; identifiability of production and clearance parameters',
                     'simulated survivor population', 'constructive counterexample (Fokker-Planck numerics; script and tests)', 'saturating-removal dynamics only'),
         evidence=['E-SR-SCOPE', 'E-SR-A', 'E-SR-LAMBDA', 'E-SR-C', 'E-SR-ID', 'E-SR-LIMIT'], state='supported',
         rationale='Matched mean damage at 70; local recovery rates 0.137 vs 0.114 per year (about 20%), computed at the survivor mean as a linearised approximation; pulse reading returns at a speed set by the recovery rate; level plus recovery rate at two levels identifies beta and kappa only if the model is correctly specified; no measurement noise or finite samples. Formal claim: support means the construction is valid as reported.',
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
        claim = dict(id=c['id'], artifact_id='A-CH8-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH8-EN': arts['A-CH8-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch08-recovery-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Eight paragraph units of the English chapter 8 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=8, registered_claims=len(claims),
                         note='Reasoning paragraphs (what a resting reading hides; association versus effect for heart-rate recovery; curve shape versus model parameters; extrapolation is not a limit; week 68 versus week 120; consumer recovery scores) make no source claim. Abstract depth throughout.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH8-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent domain or statistical review of these claims (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH8-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All sources read at abstract depth; age-adjusted heart-rate recovery estimates (X132) not restated; no human study measuring level, rate and recovery in the same people before and after an intervention found',
                 next_action='Read full texts; search for repeated challenge-test studies around interventions',
                 closure_evidence='Full-text reading notes bound as excerpts; search log'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if out.exists() and json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
