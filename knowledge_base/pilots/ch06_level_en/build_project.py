"""Bind selected claims of the English chapter 6 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch06_level_en'
EN_PATH = 'books/manuscript/en/CH06_level_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH6-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016), written English-first; working copy'),
    ('A-RELIAB', f'{EV}/RELIABILITY_excerpts.txt', 'source', 'clock-reliability-literature', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/36277076/',
     'PubMed abstracts (Higgins-Chen 2022 incl. COI; Sugden 2020) and PMC introduction (Borrus 2026), 2026-11-28'),
    ('A-SEX', f'{EV}/SEX_SPECIFIC_abstract.txt', 'source', 'study-MULTI-sex-specific-clocks', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42749890/', 'PubMed abstract 2026-11-28; erratum not read'),
    ('A-COMP', f'{EV}/COMPOSITION_abstract.txt', 'source', 'study-Jonkman-blood-composition', 'abstract',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC13632308/', 'Europe PMC abstract 2026-11-28'),
    ('A-ORGAN', f'{EV}/ORGAN_CLOCKS_abstract.txt', 'source', 'study-Oh-plasma-organ-age', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/40634782/', 'Europe PMC abstract 2026-11-28'),
    ('A-COMP-FT', f'{EV}/COMPOSITION_fulltext_results.txt', 'source', 'study-Jonkman-blood-composition', 'fulltext',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC13632308/', 'PMC full text, Results passages, 2026-11-28'),
    ('A-TELO', f'{EV}/TELOMERE_abstract.txt', 'source', 'study-Ye-telomere-meta-analysis', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/37567392/', 'PubMed abstract 2026-11-28'),
    ('A-SR', 'knowledge_base/experiments/SR_SNAPSHOT_IDENTIFIABILITY_2026-11-27.md', 'code',
     'longevity-project-derivation', 'fulltext', '', 'project synthetic-model memo; script and tests alongside'),
]
EVIDENCE = {
    'E-HC-9Y': ('A-RELIAB', 'deviations up to 9 years', 1),
    'E-HC-PC': ('A-RELIAB', 'agreement between most replicates within 1.5 years', 1),
    'E-HC-COI': ('A-RELIAB', 'Competing Interests Statement MEL and AHC', 1),
    'E-HC-DATA': ('A-RELIAB', 'Elysium provided paired blood', 1),
    'E-BOR-RETEST': ('A-RELIAB', 'fluctuations between 0.9 and 2.4 years', 1),
    'E-BOR-PC': ('A-RELIAB', 'median deviation of technical replicates to 0.3–0.8 years', 1),
    'E-SUG-350': ('A-RELIAB', 'in 350 blood DNA samples', 1),
    'E-SUG-UNREL': ('A-RELIAB', 'Unreliable probes were less replicable', 1),
    'E-SEX-POOLED': ('A-SEX', 'trained on sex-pooled samples', 1),
    'E-SEX-38': ('A-SEX', 'Here we developed 38 sex-specific', 1),
    'E-SEX-REF': ('A-SEX', 'sex-specific healthy normative references', 1),
    'E-SEX-PRED': ('A-SEX', 'in a sex-dependent and organ-dependent manner', 1),
    'E-SEX-POOLOK': ('A-SEX', 'sex-pooled and sex-interaction approaches remain valuable', 1),
    'E-COMP-4058': ('A-COMP', 'in an analysis of 4,058 samples', 1),
    'E-COMP-18859': ('A-COMP', 'using a study of 18,859 individuals', 1),
    'E-COMP-53': ('A-COMP', 'up to 53% of the variation', 1),
    'E-COMP-21': ('A-COMP', 'up to 21% variance explained', 1),
    'E-COMP-MIX': ('A-COMP', 'artificial cell mixtures', 1),
    'E-COMP-ATT': ('A-COMP', 'although this effect remains modest', 1),
    'E-COMP-MINOR': ('A-COMP', 'only has a minor contribution', 1),
    'E-COMP-RANGE': ('A-COMP-FT', 'likewise 44–53% of the variance for all DNAmAges except DunedinPACE', 1),
    'E-COMP-INSILICO': ('A-COMP-FT', 'generated in silico artificial cell mixtures', 1),
    'E-COMP-MORT': ('A-COMP-FT', 'the attenuation ranged from 1% for Horvath to 6% for PhenoAge', 1),
    'E-ORG-N': ('A-ORGAN', 'from 44,498 individuals in the UK Biobank', 1),
    'E-ORG-DIS': ('A-ORGAN', "within 17 years' follow-up", 1),
    'E-ORG-HR': ('A-ORGAN', '8+ aged organs, HR = 8.3', 1),
    'E-TEL-N': ('A-TELO', '414 study samples comprising 743,019', 1),
    'E-TEL-R': ('A-TELO', 'cross-sectional samples was -0.19', 1),
    'E-TEL-METH': ('A-TELO', 'Methodological factors including TL measurement', 1),
    'E-SR-SCOPE': ('A-SR', '**仅为合成教学模型。**', 1),
    'E-SR-A': ('A-SR', '**发现 A：读数匹配，生存曲线却交叉。**', 1),
    'E-SR-S90': ('A-SR', '- 到 90 岁反转', 1),
    'E-SR-LE': ('A-SR', '- 预期寿命：清除组 89.75 岁', 1),
    'E-SR-B': ('A-SR', '**发现 B：符号反转。**', 1),
    'E-SR-C': ('A-SR', '**发现 C：只是暂时变年轻。**', 1),
    'E-SR-ID': ('A-SR', '**可识别条件**', 1),
}
dims = base.dims

CLAIMS = [
    dict(id='CH6-EN-C001', anchor='Return to the split tube.', kind='reported', role='asserted', critical=True,
         context=dict(population='Higgins-Chen 2022: replicate DNA samples from several cohorts; Sugden 2020: 350 blood DNA samples measured on two Illumina arrays',
                      time='technical replicates and repeat measurement of the same DNA; no biological change implied',
                      estimand='between-replicate deviation of clock estimates; probe-level reliability',
                      unit='DNA sample (replicate pair)',
                      design='methods studies; Borrus 2026 is a later summary by the Higgins-Chen laboratory family',
                      domain='six prominent epigenetic clocks and their principal-component retrainings; Illumina 450K/EPIC probes'),
         evidence=['E-HC-9Y', 'E-HC-PC', 'E-BOR-RETEST', 'E-BOR-PC', 'E-SUG-350', 'E-SUG-UNREL'], state='supported',
         rationale='Up to 9 years for six clocks; most replicates within 1.5 years for PC versions; 0.9-2.4 years retest fluctuation and 0.3-0.8 years median PC deviation are quoted from Borrus (same family, stated as such in the text); 350 samples, unreliable probes less replicable and unknown volume of false negatives match Sugden. Abstract/introduction depth; which six clocks and which cohorts not restated.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C002', anchor='Third, it matters who reports a reliability problem', kind='reported', role='asserted', critical=False,
         context=dict(population='authors of Higgins-Chen 2022', time='declaration at publication (2022)',
                      estimand='declared competing interests and data provenance; not an assessment of bias',
                      unit='publication', design='competing-interests statement', domain='research integrity disclosure'),
         evidence=['E-HC-COI', 'E-HC-DATA', 'E-SUG-UNREL'], state='supported',
         rationale='Two authors built metrics using the described technology, licensed to Elysium Health through Yale; Elysium supplied paired replicate datasets. The text says the disclosure does not make the result wrong and that an independent study points the same way (Sugden). It does not characterise the company\'s products.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C003', anchor='The most obvious difference between groups of people', kind='reported', role='asserted', critical=True,
         context=dict(population='MULTI Consortium cohorts (not restated in the abstract)', time='longitudinal survival analyses; follow-up length not read',
                      estimand='value of sex-stratified training for normative references; sex- and organ-dependent prediction of disease and mortality',
                      unit='participant', design='model development and survival analysis', domain='38 sex-specific clocks across 15 organ systems and several omics'),
         evidence=['E-SEX-POOLED', 'E-SEX-38', 'E-SEX-REF', 'E-SEX-PRED', 'E-SEX-POOLOK'], state='supported',
         rationale='Pooled training assumption, 38 clocks / 15 organ systems, importance of sex-stratified training for normative references, sex- and organ-dependent prediction, and the authors\' caveat that pooled and interaction models remain valuable all match. No hazard ratios are used (X149: V7.0 HRs unverified).',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C004', anchor='How large is the second source?', kind='reported', role='asserted', critical=True,
         context=dict(population='4,058 samples (composition analysis); 18,859 individuals (outcome analysis)', time='incident outcomes over the study follow-up (length not read)',
                      estimand='variance in DNAmAge and AgeAccel attributable to estimated cell counts; attenuation of AgeAccel-outcome associations after composition adjustment',
                      unit='sample / participant', design='observational analysis with PCA of cell counts; validation with in silico artificial cell mixtures',
                      domain='six first- and second-generation blood epigenetic clocks'),
         evidence=['E-COMP-4058', 'E-COMP-18859', 'E-COMP-53', 'E-COMP-21', 'E-COMP-MIX', 'E-COMP-INSILICO', 'E-COMP-ATT'], state='supported',
         rationale='4,058; up to 53% (naive/memory T-cell balance); up to 21% for age acceleration; 176 outcomes in 18,859; significant but modest attenuation all match the abstract. The full text shows the artificial mixtures were generated in silico from sorted-cell data, which the text now states.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C008', anchor='Read that carefully, because it cuts both ways.', kind='reported', role='asserted', critical=True,
         context=dict(population='4,058 samples (variance); 18,859 individuals (mortality attenuation)', time='incident outcomes over the study follow-up (length not read)',
                      estimand='range across clocks of DNAmAge variance explained by cell counts; attenuation of AgeAccel-mortality hazard ratios after composition adjustment',
                      unit='sample / participant', design='observational analysis with PCA of cell counts',
                      domain='six blood epigenetic clocks; DunedinPACE reported separately'),
         evidence=['E-COMP-RANGE', 'E-COMP-MORT', 'E-COMP-ATT', 'E-COMP-MINOR'], state='supported',
         rationale='44-53% for five clocks and 26% for DunedinPACE, and mortality attenuation from 1% (Horvath) to 6% (PhenoAge), match the Results passages; these also confirm the KERNEL §3.2 ranges, which the abstract gives only as maxima. The statements that the figure describes differences between people rather than one person and that composition is not noise are interpretive limits, not source claims; the T-cell sentence restates the abstract.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C005', anchor='These readings can predict.', kind='reported', role='asserted', critical=True,
         context=dict(population='44,498 UK Biobank participants', time="up to 17 years' follow-up",
                      estimand='association of plasma-proteomic organ age with incident disease and mortality (hazard ratios)',
                      unit='participant', design='prospective cohort analysis', domain='11 organs from 2,916 plasma proteins'),
         evidence=['E-ORG-N', 'E-ORG-DIS', 'E-ORG-HR'], state='supported',
         rationale='11 organs, 2,916 proteins, 44,498 participants, sensitivity to lifestyle and medications, diseases listed, 17-year follow-up, HR 8.3 for 8+ aged organs all match. "Chronic lung disease" renders COPD. The following paragraph on non-independence of organ readings is explicitly labelled as reasoning about measurement, not a study result, and is not part of this claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C006', anchor='A level also carries less information than its precision suggests.', kind='reported', role='asserted', critical=False,
         context=dict(population='414 study samples, 743,019 individuals aged 0-112', time='cross-sectional samples for the correlation',
                      estimand='pooled corrected correlation between telomere length and age', unit='study sample (meta-analysis)',
                      design='systematic review and meta-analysis', domain='telomere length across tissues and measurement methods'),
         evidence=['E-TEL-N', 'E-TEL-R', 'E-TEL-METH'], state='supported',
         rationale='414 samples, 743,019 people, 0-112 years, r = -0.19 (-0.22 to -0.15), weakening with age, method and tissue effects match. "Weak at the level of a person" is an interpretation of r of this size, not a source statement.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH6-EN-C007', anchor='The clearest way to see this is in a model where we know the truth', kind='formal', role='asserted', critical=True,
         context=dict(population='none: synthetic one-dimensional saturating-removal model with illustrative parameters, not fitted to any cohort',
                      time='interventions from age 60; readings at 61 and 70; survival to 90',
                      estimand='existence of interventions with matched survivor mean damage but different survival and life expectancy; sign reversal; transient change',
                      unit='simulated survivor population', design='constructive counterexample (Fokker-Planck numerics; script and tests)',
                      domain='saturating-removal dynamics only'),
         evidence=['E-SR-SCOPE', 'E-SR-A', 'E-SR-S90', 'E-SR-LE', 'E-SR-B', 'E-SR-C', 'E-SR-ID'], state='supported',
         rationale='Matched reading at 70; S90 0.605 vs 0.572 rendered as about 61 vs 57 in 100; life expectancy 91.66 vs 89.75 rendered as about 91.7 vs 89.8; threshold +1 gives damage age 71.5 and +1.46 years; pulse 4.1 years younger at 61, 69.9 at 70, +0.33 years. The text states the model shows possibility only and is not fitted or evaluative, matching the memo scope line. Formal claim: support means the construction is valid as reported, not that biology behaves this way.',
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
        claim = dict(id=c['id'], artifact_id='A-CH6-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH6-EN': arts['A-CH6-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch06-level-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Eight paragraph units of the English chapter 6 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=9, registered_claims=len(claims),
                         note='Unregistered: the bookkeeping paragraph on the two 2025 organ-age studies (rests on ledger X81). Reasoning paragraphs (non-independence of organ readings; what a level can carry) make no source claim. Abstract depth except the Borrus introduction and the Jonkman Results passages.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH6-EN-INDEPENDENT-REVIEW', status='blocked', blocks_formal_release=True,
                 question='No independent domain or statistical review of these claims (D05)',
                 next_action='Real external review; never fabricate receipts',
                 closure_evidence='Object-bound review record with declared independence and responses'),
            dict(id='CH6-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='Sources read at abstract depth except Jonkman 2026 (Results passages read) and Borrus (introduction); Song 2026 erratum unread; no independent test-retest study of a consumer-marketed clock found',
                 next_action='Read full texts and erratum; search again for an unconflicted consumer-clock reliability study',
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
