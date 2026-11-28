"""Bind selected claims of the English chapter 7 draft (DEC-016, written English-first) to exact source spans.

Run deliberately to (re)bind after a reviewed change; tests never run it. Spans are located by anchor
text and frozen into project.json as line numbers, exact text and sha256, so a later edit to the
chapter, to an excerpt or to the pinned DunedinPACE code snapshot shows up as drift in `inspect_project`.
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

HERE = 'knowledge_base/pilots/ch07_rate_en'
EN_PATH = 'books/manuscript/en/CH07_rate_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH7-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016), written English-first; working copy'),
    ('A-DUN15', f'{EV}/DUNEDIN_PACE_OF_AGING_abstract.txt', 'source', 'study-Dunedin-pace-of-aging', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/26150497/', 'PubMed abstract 2026-11-28'),
    ('A-TELR', f'{EV}/TELOMERE_RATE_abstract.txt', 'source', 'study-Ye-telomere-meta-analysis', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/37567392/', 'PubMed abstract 2026-11-28'),
    ('A-VO2', f'{EV}/AEROBIC_CAPACITY_abstract.txt', 'source', 'study-BLSA-aerobic-capacity', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/16043637/', 'PubMed abstract 2026-11-28'),
    ('A-NONLIN', f'{EV}/NONLINEAR_abstracts.txt', 'source', 'studies-nonlinear-aging-Stanford-and-Singapore', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/39143318/', 'PubMed abstracts (Shen 2024; Park 2026) 2026-11-28'),
    ('A-PACE', f'{EV}/PACE_CLOCK_abstracts.txt', 'source', 'Dunedin-Duke-Columbia-pace-clock-family', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/35029144/', 'PubMed abstracts and COI (Belsky 2022; Waziry 2023) 2026-11-28; erratum not read'),
    ('A-YALE', f'{EV}/RESPONSIVENESS_RELIABILITY_abstracts.txt', 'source', 'clock-reliability-literature', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42629466/', 'PubMed abstracts and COI (Sehgal Nat Med 2026; Sehgal Aging Cell 2026) 2026-11-28'),
    ('A-PACECODE', 'knowledge_base/source_snapshots/dunedinpace_4b569983/PACEProjector.R', 'code', 'Dunedin-Duke-Columbia-pace-clock-family', 'code',
     'https://github.com/danbelsky/DunedinPACE/blob/4b569983543e51d1022aecec9a25e694bb3a336a/R/PACEProjector.R',
     'commit 4b569983 pinned 2026-11-27 (manifest with SHA-256); documentation and code read, not executed'),
]
EVIDENCE = {
    'E-DUN-954': ('A-DUN15', 'We studied aging in 954 young humans', 1),
    'E-DUN-ORG': ('A-DUN15', 'pace of coordinated physiological deterioration', 1),
    'E-DUN-VAR': ('A-DUN15', 'Young individuals of the same chronological age varied', 1),
    'E-DUN-FAST': ('A-DUN15', 'Already, before midlife', 1),
    'E-TEL-SAMPLES': ('A-TELR', '414 study samples comprising 743,019', 1),
    'E-TEL-BP': ('A-TELR', '-23 bp/year in cross-sectional samples and -38 bp/year', 1),
    'E-TEL-NONLIN': ('A-TELR', 'gradual decrease in shortening rate until around age 50', 1),
    'E-VO2-XS': ('A-VO2', 'misleading, overly optimistic estimates', 1),
    'E-VO2-N': ('A-VO2', 'in 375 women and 435 men ages 21 to 87 years', 1),
    'E-VO2-RATE': ('A-VO2', 'accelerated from 3% to 6% per 10 years', 1),
    'E-SHEN-N': ('A-NONLIN', 'longitudinal human cohort of 108 participants', 1),
    'E-SHEN-FU': ('A-NONLIN', 'median period of 1.7 years, with a maximum follow-up duration of 6.8 years', 1),
    'E-SHEN-44': ('A-NONLIN', 'approximately 44 years and 60 years', 1),
    'E-PARK-N': ('A-NONLIN', '3.8 million peripheral blood mononuclear cells (PBMCs) from 1,828 individuals', 1),
    'E-PARK-PEAKS': ('A-NONLIN', 'Prominent peaks of differential gene expression around 40', 1),
    'E-PARK-SEX': ('A-NONLIN', 'stratified for sex outperformed sex-combined models', 1),
    'E-PACE-19': ('A-PACE', '19 indicators of organ-system integrity across four time points', 1),
    'E-PACE-RELPROBE': ('A-PACE', 'restricted to exclude probes with low test-retest reliability', 1),
    'E-PACE-RES': ('A-PACE', 'DunedinPACE showed high test-retest reliability', 1),
    'E-PACE-COI': ('A-PACE', 'DB, AC, DC, KS, RP, TM is listed as an inventor', 1),
    'E-CAL-220': ('A-PACE', 'n = 220 adults without obesity were randomized to 25% CR', 1),
    'E-CAL-RES': ('A-PACE', 'CALERIE intervention slowed the pace of aging', 1),
    'E-CAL-SMALL': ('A-PACE', 'Treatment effect sizes were small.', 1),
    'E-CAL-COI': ('A-PACE', 'D.L.C. and D.W.B. are listed as inventors', 1),
    'E-TA-51': ('A-YALE', 'harmonized database of 51 public and private longitudinal interventional studies', 1),
    'E-TA-PATTERN': ('A-YALE', 'clocks trained to predict mortality or pace of aging show the strongest responses', 1),
    'E-TA-SURR': ('A-YALE', 'eventual aim of uncovering DNAm biomarkers that can be used as surrogate aging endpoints', 1),
    'E-TA-COI': ('A-YALE', 'Competing interests: R. Sehgal and A.H.-C. are named as co-inventors of SystemsAge', 1),
    'E-REL-18': ('A-YALE', 'across 18 DNA methylation-based aging biomarkers', 1),
    'E-REL-TECH': ('A-YALE', 'Most clocks demonstrated excellent technical reproducibility', 1),
    'E-REL-SLIDE': ('A-YALE', 'such as slide position and DNA extraction protocols', 1),
    'E-REL-BIO': ('A-YALE', 'Biological reliability, assessed across repeated measures', 1),
    'E-REL-LOW': ('A-YALE', 'Most clocks showed only low to moderate stability', 1),
    'E-REL-NOPRED': ('A-YALE', 'technical reproducibility did not predict biological reliability', 1),
    'E-CODE-PARAM': ('A-PACECODE', "@param proportionOfProbesRequired (default: 0.8)", 1),
    'E-CODE-MISSING': ('A-PACECODE', "#' Missing data handled in two different ways", 1),
    'E-CODE-COHORT': ('A-PACECODE', 'it is recommended that entire cohorts be run at once', 1),
    'E-CODE-V2': ('A-PACECODE', '    proportionOfProbesRequired <- 0.7', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


CLAIMS = [
    dict(id='CH7-EN-C001', anchor='One of the clearest demonstrations of within-person rates', kind='reported', role='asserted', critical=True,
         context=ctx('954 members of the Dunedin Study birth cohort', 'three assessments across the third and fourth decades of life',
                     'within-person pace of multi-system biomarker decline; cross-sectional associations of pace with function and appearance',
                     'person', 'prospective birth-cohort study', 'multi-organ clinical biomarkers in young adults'),
         evidence=['E-DUN-954', 'E-DUN-ORG', 'E-DUN-VAR', 'E-DUN-FAST'], state='supported',
         rationale='954; three time points in the third and fourth decades; organ systems listed (pulmonary, periodontal, cardiovascular, renal, hepatic, immune) rendered in plain words; same-age variation; faster agers less physically able, cognitive decline and brain aging, worse self-rated health, looked older. All match the abstract. Corrected 2026-11-28: v0.1 placed the cohort "in New Zealand", which is not in the stored excerpt; removed.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C002', anchor='Telomeres again provide a simple example.', kind='reported', role='asserted', critical=True,
         context=ctx('414 study samples, 743,019 individuals aged 0-112', 'cross-sectional and longitudinal samples pooled in a meta-analysis',
                     'median telomere change rate in base pairs per year by design; z-score change rate across age',
                     'study sample', 'systematic review and meta-analysis', 'telomere length, various tissues and methods'),
         evidence=['E-TEL-SAMPLES', 'E-TEL-BP', 'E-TEL-NONLIN'], state='supported',
         rationale='414 samples; median -23 bp/year cross-sectional versus -38 bp/year longitudinal (rendered as rates of shortening of about 23 and 38 base pairs per year); shortening rate decreasing until about 50 then relatively stable. All in the abstract.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C003', anchor='The same pattern appears for a quantity that matters directly', kind='reported', role='asserted', critical=True,
         context=ctx('375 women and 435 men aged 21-87, Baltimore Longitudinal Study of Aging, free of clinical heart disease', 'median follow-up 7.9 years',
                     'longitudinal 10-year rate of change in peak VO2 by age decade', 'person', 'longitudinal cohort with serial treadmill tests',
                     'peak aerobic capacity in community-dwelling volunteers'),
         evidence=['E-VO2-XS', 'E-VO2-N', 'E-VO2-RATE'], state='supported',
         rationale='Sample sizes, ages, cohort description, 7.9-year median follow-up, decline in every decade in both sexes, acceleration from 3-6% to >20% per 10 years, and the authors\' warning about misleading, overly optimistic cross-sectional estimates all match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C004', anchor='A Stanford group profiled many kinds of molecules', kind='reported', role='asserted', critical=False,
         context=ctx('108 participants aged 25-75 in California', 'median follow-up 1.7 years, maximum 6.8 years',
                     'age points of concentrated molecular dysregulation', 'participant', 'longitudinal multi-omics cohort, largely cross-age comparison',
                     'blood and other multi-omic profiles'),
         evidence=['E-SHEN-N', 'E-SHEN-FU', 'E-SHEN-44'], state='supported',
         rationale='108; 25-75; California; median 1.7 and maximum 6.8 years; consistent nonlinear patterns with dysregulation at about 44 and 60. The text\'s later caveat (short follow-up means the age pattern is mainly between-person) is the chapter\'s own reasoning, not a source claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C005', anchor='A separate group in Singapore analyzed', kind='reported', role='asserted', critical=False,
         context=ctx('1,828 individuals aged 19-97, 35% Asian', 'single sampling per person as far as the abstract states',
                     'age peaks of differential gene expression by cell type; performance of sex-stratified clocks', 'cell / individual',
                     'single-cell transcriptomic cross-age analysis', 'peripheral blood mononuclear cells'),
         evidence=['E-PARK-N', 'E-PARK-PEAKS', 'E-PARK-SEX'], state='supported',
         rationale='3.8 million PBMCs; 1,828 people aged 19-97; 35% Asian ("of Asian ancestry"); peaks around 40 (mainly CD4) and after 60 (mainly CD8); sex-dependent kinetics; sex-stratified clocks outperform combined. Matches abstract and ledger X153.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C006', anchor='The best-known example was built from the Dunedin cohort itself.', kind='reported', role='asserted', critical=True,
         context=ctx('Dunedin Study 1972-73 birth cohort (training); five additional datasets (evaluation)', 'four time points spanning two decades',
                     'single-time-point DNAm prediction of two-decade within-person Pace of Aging; reliability and outcome associations',
                     'person / blood sample', 'biomarker development and validation', 'blood DNA methylation'),
         evidence=['E-PACE-19', 'E-PACE-RELPROBE', 'E-PACE-RES', 'E-PACE-COI'], state='supported',
         rationale='19 indicators, four time points over two decades, single-time-point blood test, reliability-filtered probes, high test-retest reliability, association with morbidity, disability and mortality, faster aging with childhood adversity, and inventor/licence disclosure all match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C007', anchor='Can a pace clock respond to an intervention?', kind='reported', role='asserted', critical=True,
         context=ctx('CALERIE: 220 randomized adults without obesity (methylation analysis sample smaller; ledger X31)', '2-year intervention',
                     'treatment effect on DNAm measures of aging', 'participant', 'post hoc analysis of a randomized controlled trial',
                     'blood DNA methylation clocks'),
         evidence=['E-CAL-220', 'E-CAL-RES', 'E-CAL-SMALL', 'E-CAL-COI'], state='supported',
         rationale='220 randomized to 25% CR or ad libitum for 2 years; DunedinPACE slowed; no significant change in other clocks including PhenoAge and GrimAge; small effect sizes; post hoc; two authors are DunedinPACE inventors. "Not part of the original plan" renders "post hoc".',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C008', anchor='Is responsiveness common?', kind='reported', role='asserted', critical=True,
         context=ctx('51 public and private longitudinal interventional studies (TranslAGE)', 'pre-post windows of included studies',
                     'responsiveness patterns of 16 clocks and 94 other DNAm biomarkers', 'study / sample', 'harmonized re-analysis database',
                     'blood DNA methylation biomarkers'),
         evidence=['E-TA-51', 'E-TA-PATTERN', 'E-TA-SURR', 'E-TA-COI'], state='supported',
         rationale='51 studies, 16 clocks, 94 other biomarkers; mortality and pace clocks strongest and mutually consistent; population and duration key; eventual surrogate aim; COI (three TruDiagnostic employees who developed OMICmAge; two SystemsAge co-inventors with US patent; consulting fees from TruDiagnostic for two) all match. "Yale-led" is from author affiliations.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C009', anchor='The same group also asked how stable these readings are', kind='reported', role='asserted', critical=True,
         context=ctx('TranslAGE datasets including ADNI', 'technical replicates; repeated biological samples over short intervals',
                     'technical versus biological reliability of 18 DNAm aging biomarkers', 'sample', 'methods study',
                     'blood DNA methylation clocks'),
         evidence=['E-REL-18', 'E-REL-TECH', 'E-REL-SLIDE', 'E-REL-BIO', 'E-REL-LOW', 'E-REL-NOPRED'], state='supported',
         rationale='18 biomarkers; excellent technical reproducibility for most; sensitivity to slide position and DNA extraction; biological reliability substantially lower under meals, stress and environmental exposures; low to moderate stability, lower after immune adjustment; technical does not predict biological. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH7-EN-C010', anchor='Clocks are software as well as chemistry.', kind='reported', role='asserted', critical=True,
         context=ctx('none: software behaviour as documented', 'commit 4b569983 retrieved 2026-11-27',
                     'documented missing-data handling and EPICv2 threshold of the DunedinPACE projector', 'code version',
                     'reading of pinned source code and its documentation; not executed', 'DunedinPACE R package, PACEProjector.R'),
         evidence=['E-CODE-PARAM', 'E-CODE-MISSING', 'E-CODE-COHORT', 'E-CODE-V2'], state='supported',
         rationale='Default threshold 0.8; within-threshold missing values set to the mean of the supplied betas matrix; beyond-threshold probes replaced with the training-data mean; EPICv2 detection sets the threshold to 0.7; documentation recommends running entire cohorts at once. The implication that a score can depend on batch composition follows from the documented imputation and is stated as a possibility ("slightly"), not measured.',
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
        claim = dict(id=c['id'], artifact_id='A-CH7-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH7-EN': arts['A-CH7-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch07-rate-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Ten paragraph units of the English chapter 7 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=12, registered_claims=len(claims),
                         note='Unregistered: the CALERIE achieved-restriction and analysis-sample paragraph (rests on ledger X31/X49) and the sentence on the unidentified software version of a published trial (ledger X27). Reasoning paragraphs (who remains in a cross-sectional sample; limits of the nonlinear studies; illustrative noise arithmetic) make no source claim. Abstract depth throughout.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH7-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent domain or statistical review of these claims (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH7-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All sources read at abstract depth; CALERIE erratum unread; no independent multi-year within-person repeated-clock study from a group without a stake in the clocks found; DunedinPACE code version used in published trials unknown (X27)',
                 next_action='Read full texts and erratum; search again for unconflicted longitudinal repeated-clock studies; request trial software versions',
                 closure_evidence='Full-text reading notes bound as excerpts; search log; version statements'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if out.exists() and json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
