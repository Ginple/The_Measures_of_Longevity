"""Bind selected claims of the English chapter 9 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch09_reserve_en'
EN_PATH = 'books/manuscript/en/CH09_reserve_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH9-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016), written English-first; no inherited chapter; working copy'),
    ('A-VITAL', f'{EV}/VITALITY_MODELS_abstract.txt', 'source', 'study-Anderson-process-POV', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/27885527/', 'PubMed abstract 2026-11-28; secondary description of Strehler-Mildvan 1960'),
    ('A-RENAL', f'{EV}/RENAL_RESERVE_abstract.txt', 'source', 'study-Fliser-renal-reserve', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/8439649/', 'PubMed abstract (truncated at 250 words) 2026-11-28'),
    ('A-AERO-T', f'{EV}/AEROBIC_THRESHOLD_abstracts.txt', 'source', 'aerobic-threshold-Paterson-Shephard', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/10613433/', 'PubMed abstracts (Paterson 1999; Shephard 2009) 2026-11-28'),
    ('A-AERO-D', f'{EV}/AEROBIC_DECLINE_abstract.txt', 'source', 'cohort-BLSA-Fleg', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/16043637/', 'PubMed abstract 2026-11-28 (same excerpt as the ch7 pilot)'),
    ('A-TRAJ', f'{EV}/TRAJECTORY_abstract.txt', 'source', 'cohort-interRAI-Egbujie', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42632919/', 'PubMed abstract and COI 2026-11-28'),
    ('A-RES-CODE', 'knowledge_base/experiments/margin_time_to_threshold.py', 'code', 'longevity-project-derivation', 'code', '',
     'project synthetic reserve calculation (X131); tests alongside'),
    ('A-RES-OUT', f'{EV}/RESERVE_SYNTHETIC_output.json', 'dataset', 'longevity-project-derivation', 'data', '',
     'saved stdout of margin_time_to_threshold.py; tests/test_ch09_en_pilot.py recomputes it'),
    ('A-SR2', 'knowledge_base/experiments/SR_PUBLISHED_PARAMS_ROBUSTNESS_2026-11-27.md', 'code',
     'longevity-project-derivation', 'fulltext', '', 'project synthetic-model memo (X94); script and tests alongside'),
]
EVIDENCE = {
    'E-VIT-POV': ('A-VITAL', 'such as the Strehler-Mildvan and stochastic vitality models', 1),
    'E-VIT-CHAL': ('A-VITAL', 'defines death as challenges to vitality', 1),
    'E-VIT-SECOND': ('A-VITAL', '# Used only as a secondary description', 1),
    'E-REN-RAT': ('A-RENAL', 'is impaired in the aged rat', 1),
    'E-REN-N': ('A-RENAL', 'in 15 healthy normotensive subjects of young age', 1),
    'E-REN-REST': ('A-RENAL', 'virtually all GFR values of the elderly were still within the normal range', 1),
    'E-REN-LOAD': ('A-RENAL', 'Median Cin upon infusion of AA was 118', 1),
    'E-REN-SIG': ('A-RENAL', 'Cin increased significantly (P < 0.01) after the AA load', 1),
    'E-REN-TRUNC': ('A-RENAL', '# The PubMed record is marked', 1),
    'E-PAT-N': ('A-AERO-T', 'on a total of 298 subjects (152 men and 146 women)', 1),
    'E-PAT-37': ('A-AERO-T', 'age explained at most 37% of the variance', 1),
    'E-PAT-SLOPE': ('A-AERO-T', 'similar in men (0.31', 1),
    'E-PAT-THRESH': ('A-AERO-T', 'The minimum level of aerobic power compatible with an independent life', 1),
    'E-PAT-SAMPLE': ('A-AERO-T', 'random sample of independently living men and women', 1),
    'E-SHE-UNABATED': ('A-AERO-T', 'continues unabated during the retirement years', 1),
    'E-SHE-THRESH': ('A-AERO-T', 'reached at 80-85 years', 1),
    'E-SHE-10': ('A-AERO-T', "reducing the individual's biological age by 10 or more years", 1),
    'E-SHE-CLARIFY': ('A-AERO-T', 'There remains a need to clarify', 1),
    'E-FLEG-N': ('A-AERO-D', 'in 375 women and 435 men', 1),
    'E-FLEG-ACC': ('A-AERO-D', 'accelerated from 3% to 6% per 10 years', 1),
    'E-FLEG-XS': ('A-AERO-D', 'misleading, overly optimistic', 1),
    'E-TRAJ-DATA': ('A-TRAJ', 'routinely collected interRAI Home Care data', 1),
    'E-TRAJ-N': ('A-TRAJ', '302 467 home care recipients', 1),
    'E-TRAJ-5': ('A-TRAJ', 'Five distinct IC trajectories', 1),
    'E-TRAJ-BASE': ('A-TRAJ', 'baseline IC level alone did not fully capture', 1),
    'E-TRAJ-LTC': ('A-TRAJ', '(48.4% vs 38.1%)', 1),
    'E-TRAJ-COI': ('A-TRAJ', 'Conflict of interest statement: None declared.', 1),
    'E-RC-R': ('A-RES-CODE', 'r = -ln(0.8)/10', 1),
    'E-RC-MODEL': ('A-RES-CODE', '比例模型 V(t) = V0·exp(-r t)', 1),
    'E-RC-LEVEL': ('A-RES-CODE', '- 水平提高到 g 倍', 1),
    'E-RC-RATE': ('A-RES-CODE', '- 速率降低比例 c', 1),
    'E-RC-T': ('A-RES-CODE', 'T_MEN = 18.0', 2),
    'E-RO-NATURE': ('A-RES-OUT', '"nature"', 1),
    'E-RO-20': ('A-RES-OUT', '"V0": 20.0,', 5),
    'E-RO-25': ('A-RES-OUT', '"V0": 25.0,', 5),
    'E-RO-CROSS': ('A-RES-OUT', '"crossover_years_g1.1_c0.1"', 1),
    'E-RO-PLUS10': ('A-RES-OUT', '"from_V0": 25.0', 3),
    'E-SR2-SCOPE': ('A-SR2', '**合成压力测试**', 1),
    'E-SR2-ROW': ('A-SR2', '| 0.1 | 0.05/0.1 |', 1),
    'E-SR2-DIR': ('A-SR2', '清除型干预让 70 岁时活着的人更多', 1),
    'E-SR2-D01': ('A-SR2', '**新的、更强的反例（d = 0.1）**', 1),
    'E-SR2-LIMIT': ('A-SR2', '- 仍是一维 SR 模型', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


SYN = 'none: synthetic algebra with published values as illustrative inputs (threshold 18, linear 0.31/yr, proportional r=0.0223/yr), men only, not fitted to any cohort'
CLAIMS = [
    dict(id='CH9-EN-C001', anchor='The idea is not new.', kind='reported', role='asserted', critical=False,
         context=ctx('none (description of a theoretical model family)', '1960 theory; 2017 description', 'how process models of mortality represent death',
                     'publication', 'secondary description in a modelling paper', 'mortality theory'),
         evidence=['E-VIT-POV', 'E-VIT-CHAL', 'E-VIT-SECOND'], state='supported',
         rationale='"Loss of survival capacity through challenges and dissipation" and "death as challenges to vitality" match the secondary abstract. The text says the 1960 paper is unread and the description secondhand, as ledger X136 requires. Corrected 2026-11-28: v0.1 gave the authors\' first names and the paper title, which are not in the stored excerpt; now only surnames, year and journal (Science, from the evidence header).',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C002', anchor='In a small study, researchers measured filtration before and after', kind='reported', role='asserted', critical=True,
         context=ctx('15 healthy young (median 26) and 10 healthy older (median 70) normotensive volunteers', 'single study; before and after amino acid infusion',
                     'GFR (inulin clearance) at rest and after amino acid load', 'participant', 'small physiological comparison', 'renal functional reserve'),
         evidence=['E-REN-N', 'E-REN-REST', 'E-REN-LOAD', 'E-REN-SIG'], state='supported',
         rationale='15 and 10; medians 26 and 70; AA infusion; resting medians 102 vs 122; virtually all elderly GFR within normal range; after load 118 vs 146; significant increase in both. All match. Corrected 2026-11-28: v0.1 also said "overnight" and "German", neither of which is in the stored abstract; both words removed.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C003', anchor='Two things stand out.', kind='reported', role='asserted', critical=True,
         context=ctx('same 25 volunteers', 'same study', 'comparison of group medians at rest and after load (derived differences of medians)',
                     'group median', 'small physiological comparison; abstract truncated', 'renal functional reserve'),
         evidence=['E-REN-REST', 'E-REN-LOAD', 'E-REN-RAT', 'E-REN-TRUNC'], state='supported',
         rationale='118 < 122 and the rises 118-102=16 and 146-122=24 are arithmetic on the quoted medians, labelled as differences of medians. The rat statement is background in the abstract and is described as such. Truncation disclosed; the text declines a general claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C004', anchor='One research group measured it in 298 people aged 55 to 86', kind='reported', role='asserted', critical=True,
         context=ctx('random sample of 298 independently living adults aged 55-86 (152 men, 146 women)', 'single cross-sectional assessment',
                     'age-related VO2max decline (linear fit) and minimum VO2max compatible with independent living at 85', 'participant',
                     'cross-sectional treadmill testing', 'maximal aerobic capacity'),
         evidence=['E-PAT-N', 'E-PAT-37', 'E-PAT-SLOPE', 'E-PAT-THRESH', 'E-PAT-SAMPLE'], state='supported',
         rationale='298 (152/146), 55-86, random sample of independently living people; linear fit; at most 37% of variance; 0.31 and 0.25 per year; slower than younger groups; 18 and 15 at age 85. All match. Corrected 2026-11-28: v0.1 said "A Canadian group"; the affiliation is not in the stored excerpt, so the word was removed. The next paragraph (lower envelope, not observed failure) is the chapter\'s reasoning, consistent with ledger X129.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C005', anchor='A brief review takes the same threshold values', kind='reported', role='asserted', critical=True,
         context=ctx('none (narrative review)', 'published 2009', 'claimed link between aerobic fitness and loss of independence',
                     'publication', 'brief narrative review', 'maximal aerobic capacity'),
         evidence=['E-SHE-THRESH', 'E-SHE-10', 'E-SHE-CLARIFY'], state='supported',
         rationale='Same 18/15 thresholds reached at 80-85; exercise can slow or reverse, reducing biological age by 10+ years and potentially prolonging independence by a similar amount; need to clarify importance relative to other causes. All match. Corrected 2026-11-28: v0.1 said "a Canadian exercise physiologist"; neither the affiliation nor the profession is in the stored excerpt, so both were removed.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C006', anchor='The sources disagree in an instructive way.', kind='reported', role='asserted', critical=True,
         context=ctx('Paterson (cross-sectional, 55-86); Shephard (review); BLSA 810 adults 21-87 free of clinical heart disease', 'BLSA median follow-up 7.9 years',
                     'shape of aerobic-capacity decline with age', 'participant / publication', 'cross-sectional study, narrative review, longitudinal cohort',
                     'maximal aerobic capacity'),
         evidence=['E-PAT-N', 'E-PAT-SLOPE', 'E-SHE-UNABATED', 'E-FLEG-N', 'E-FLEG-ACC', 'E-FLEG-XS'], state='supported',
         rationale='Slower in old age (Paterson); continues unabated (Shephard); 810 = 375 + 435 followed 7.9 years, 3-6% to >20% per decade, cross-sectional misleading and overly optimistic (Fleg). All match. Corrected 2026-11-28: v0.1 said "The Canadian study"; now "the study of 298 people". "Stronger design for measuring a rate" is the chapter 7 argument, not a source claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C007', anchor='To see what this does to an answer', kind='formal', role='asserted', critical=True,
         context=ctx(SYN, 'starting capacity 25 or 20 mL/kg/min', 'years to threshold under linear vs proportional decline',
                     'hypothetical individual', 'deterministic algebra (script, saved output, tests)', 'aerobic-capacity reserve'),
         evidence=['E-RC-R', 'E-RC-MODEL', 'E-RC-T', 'E-RO-NATURE', 'E-RO-20', 'E-RO-25'], state='supported',
         rationale='Threshold 18, linear 0.31/yr, r from >20% per decade as a lower bound so proportional years are an upper bound; V0=25: 22.6 vs 14.7; V0=20: 6.5 vs 4.7. All match the saved output. Formal claim: support means the arithmetic is reproduced as reported.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH9-EN-C008', anchor='The same choice governs claims about what a gain is worth.', kind='formal', role='asserted', critical=True,
         context=ctx(SYN, 'gain from 25 to 35 mL/kg/min, assumed persistent', 'added years to threshold under each decline model',
                     'hypothetical individual', 'deterministic algebra (script, saved output, tests)', 'aerobic-capacity reserve'),
         evidence=['E-RO-PLUS10', 'E-RC-MODEL'], state='supported',
         rationale='32.3 (linear) vs 15.1 (proportional, upper) years for 25 to 35. Assumptions (fixed threshold, smooth decline, lasting gain) stated; explicitly not a training effect.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH9-EN-C009', anchor='In the synthetic calculation, raising the level by 10 percent', kind='formal', role='asserted', critical=True,
         context=ctx(SYN, 'distance to threshold as in the V0 grid', 'years gained from +10% level vs -10% rate; crossover distance',
                     'hypothetical individual', 'deterministic algebra (script, saved output, tests)', 'aerobic-capacity reserve'),
         evidence=['E-RC-LEVEL', 'E-RC-RATE', 'E-RO-20', 'E-RO-25', 'E-RO-CROSS'], state='supported',
         rationale='+10% level: ln(1.1)/r = 4.3 years at every V0; -10% rate: t/9, 0.5 at V0=20 and 1.6 at V0=25; crossover 38.4 years ("about 38"). All match.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH9-EN-C010', anchor='The four measures of chapters 6 to 9 belong together.', kind='reported', role='asserted', critical=True,
         context=ctx('302,467 Canadian home-care recipients (interRAI Home Care), median age 81', 'retrospective; follow-up length not read',
                     'association of intrinsic-capacity trajectory group with long-term-care admission', 'person', 'retrospective cohort; group-based trajectory modelling',
                     'intrinsic capacity, five domains'),
         evidence=['E-TRAJ-DATA', 'E-TRAJ-N', 'E-TRAJ-5', 'E-TRAJ-BASE', 'E-TRAJ-LTC', 'E-TRAJ-COI'], state='supported',
         rationale='302,467; median 81; five trajectories; baseline level alone did not fully capture outcomes; moderate baseline vs low-improving LTC 48.4% vs 38.1%. All match; no conflicts declared. Observational and model-dependent caveats stated in the paragraph.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH9-EN-C011', anchor="The project's synthetic model, used in chapters 6 and 8, shows how far this can go.", kind='formal', role='asserted', critical=True,
         context=ctx('none: synthetic one-dimensional saturating-removal model with published human parameter values; no heterogeneity or Makeham term',
                     'interventions from age 60; survival to 70 and 90', 'survival curves of production- vs clearance-type interventions matched on mean damage at 70',
                     'simulated cohort', 'constructive counterexample (numerics; script and tests)', 'saturating-removal dynamics only'),
         evidence=['E-SR2-SCOPE', 'E-SR2-ROW', 'E-SR2-DIR', 'E-SR2-D01', 'E-SR2-LIMIT'], state='supported',
         rationale='Matched mean damage at 70; at d=0.1 life expectancy 74.43 vs 74.42; curves cross; clearance more alive at 70, production more at 90; only curve shape, late slope or recovery rate distinguish them; one-dimensional limits. All match. Formal claim.',
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
        claim = dict(id=c['id'], artifact_id='A-CH9-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH9-EN': arts['A-CH9-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch09-reserve-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Eleven paragraph units of the English chapter 9 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=11, registered_claims=len(claims),
                         note='Reasoning paragraphs (lower envelope is not an observed threshold; level versus rate near the threshold; reserve is not just level; the five questions; the four measures together) make no source claim. Abstract depth throughout; synthetic claims are formal.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH9-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent domain or statistical review of these claims (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH9-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All sources read at abstract depth; the renal-reserve abstract is truncated before its conclusions; Strehler-Mildvan 1960 read only secondhand (X136); no observed failure threshold for independent living',
                 next_action='Read the Fliser and Paterson full texts and Strehler-Mildvan 1960; search for prospective thresholds of capacity at loss of independence',
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
