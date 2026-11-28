"""Bind selected claims of the English chapter 3 draft (DEC-016, written English-first) to exact source spans.

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

HERE = 'knowledge_base/pilots/ch03_four_links_en'
EN_PATH = 'books/manuscript/en/CH03_four_links_draft_en.md'
EV = f'{HERE}/evidence'
ARTIFACTS = [
    ('A-CH3-EN', EN_PATH, 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'English draft v0.1 (DEC-016); new writing using V6 sections 02-03 and V7 section 02 as leads; working copy'),
    ('A-THEORY', f'{EV}/THEORIES_abstracts.txt', 'source', 'frameworks-aging-theory', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/42993579/', 'PubMed abstracts (Gladyshev 2026; Yucel 2026; Lemaitre 2024) 2026-11-28; the first two share an author'),
    ('A-TRIALS', f'{EV}/TRIALS_abstracts.txt', 'source', 'trials-marker-outcome', 'abstract',
     'https://pubmed.ncbi.nlm.nih.gov/1900101/', 'PubMed abstracts (CAST 1991; ILLUMINATE 2007; ACCORD 2008; Voight 2012) 2026-11-28; four independent studies'),
    ('A-CM-CODE', f'{HERE}/confounded_marker.py', 'code', 'longevity-project-derivation', 'code', '',
     'project synthetic confounded-marker calculation; tests/test_ch03_en_pilot.py recomputes it'),
    ('A-CM-OUT', f'{EV}/CONFOUNDED_MARKER_SYNTHETIC_output.json', 'dataset', 'longevity-project-derivation', 'data', '',
     'saved stdout of confounded_marker.py'),
    ('A-LEDGER', f'{EV}/LEDGER_X28_X85_excerpt.txt', 'source', 'longevity-project-record', 'fulltext', '',
     'verbatim copy of ledger rows X28 and X85 (2026-11-28): records of earlier reading by the same assistant; not a primary source'),
]
EVIDENCE = {
    'E-G-HDR': ('A-THEORY', '# [1] Gladyshev VN. Simply aging.', 1),
    'E-G-DEFAULT': ('A-THEORY', '[1] The organizing principle is that aging is a default outcome', 1),
    'E-G-UNIFY': ('A-THEORY', '[1] The deleteriome provides a unifying framework', 1),
    'E-G-MEASURE': ('A-THEORY', '[1] Modern biomarkers make biological age', 1),
    'E-G-REVERS': ('A-THEORY', '[1] Biological age is heterogeneous across cells', 1),
    'E-G-COI': ('A-THEORY', '[1] Conflict of interest statement', 1),
    'E-Y-HDR': ('A-THEORY', '# [2] Yücel AD, Molière A, Gladyshev VN.', 1),
    'E-Y-PROPOSE': ('A-THEORY', '[2] Here we propose that ageing reflects progressive decanalization', 1),
    'E-Y-LOCAL': ('A-THEORY', '[2] Subsequently, these constraints can only be maintained', 1),
    'E-Y-ASYM': ('A-THEORY', '[2] The asymmetry between high-fidelity writing', 1),
    'E-Y-PRC2': ('A-THEORY', '[2] Consistent with this framework, the vast majority', 1),
    'E-Y-TEST': ('A-THEORY', '[2] It provides testable predictions', 1),
    'E-Y-COI': ('A-THEORY', '[2] Conflict of interest statement', 1),
    'E-L-HDR': ('A-THEORY', '# [3] Lemaître JF, Moorad J', 1),
    'E-L-WHY': ('A-THEORY', '[3] Why and how we age are 2 intertwined questions', 1),
    'E-L-COMPART': ('A-THEORY', '[3] However, attempts to answer these questions', 1),
    'E-L-DST': ('A-THEORY', '[3] We argue that the current lack of knowledge', 1),
    'E-L-MODEL': ('A-THEORY', '[3] In this Essay, we propose a new hierarchical model', 1),
    'E-L-HYP': ('A-THEORY', '[3] The new framework will help to generate testable hypotheses', 1),
    'E-CM-DESIGN': ('A-CM-CODE', 'Population of 1000 people.', 6),
    'E-CM-OUT': ('A-CM-OUT', '"people_marker_high"', 9),
    'E-V-HDR': ('A-TRIALS', '# [4] Voight BF', 1),
    'E-V-BG': ('A-TRIALS', '[4] BACKGROUND: High plasma HDL cholesterol', 1),
    'E-V-MR': ('A-TRIALS', '[4] Exploiting the fact that genotypes', 1),
    'E-V-OBS': ('A-TRIALS', '[4] From observational epidemiology', 1),
    'E-V-GEN': ('A-TRIALS', '[4] However, a 1 SD increase in HDL cholesterol due to genetic score', 1),
    'E-V-LDL': ('A-TRIALS', '[4] For LDL cholesterol, the estimate', 1),
    'E-V-INT': ('A-TRIALS', '[4] INTERPRETATION:', 1),
    'E-V-INT2': ('A-TRIALS', '[4] These data challenge the concept', 1),
    'E-T-AIM': ('A-TRIALS', '[2] We investigated whether torcetrapib', 1),
    'E-T-STOP': ('A-TRIALS', '[2] The trial was terminated prematurely', 1),
    'E-T-N': ('A-TRIALS', '[2] METHODS: We conducted a randomized, double-blind study', 1),
    'E-T-LIPIDS': ('A-TRIALS', '[2] RESULTS: At 12 months in patients who received torcetrapib', 1),
    'E-T-HR': ('A-TRIALS', '[2] There was also an increased risk', 1),
    'E-T-MECH': ('A-TRIALS', '[2] CONCLUSIONS: Torcetrapib therapy resulted', 1),
    'E-T-OFF': ('A-TRIALS', '[2] Although there was evidence of an off-target effect', 1),
    'E-C-DESIGN': ('A-TRIALS', '[1] BACKGROUND AND METHODS: In the Cardiac Arrhythmia Suppression Trial', 1),
    'E-C-STOP': ('A-TRIALS', '[1] The use of encainide and flecainide was discontinued', 1),
    'E-C-N': ('A-TRIALS', '[1] RESULTS: Of 1498 patients', 1),
    'E-C-DEATHS': ('A-TRIALS', '[1] After a mean follow-up of 10 months', 1),
    'E-C-MECH': ('A-TRIALS', '[1] The mechanisms underlying the excess mortality', 1),
    'E-A-HDR': ('A-TRIALS', '# [3] Action to Control Cardiovascular Risk in Diabetes', 1),
    'E-A-BG': ('A-TRIALS', '[3] BACKGROUND: Epidemiologic studies', 1),
    'E-A-N': ('A-TRIALS', '[3] METHODS: In this randomized study, 10,251 patients', 1),
    'E-A-ACHIEVED': ('A-TRIALS', '[3] RESULTS: At 1 year, stable median', 1),
    'E-A-DEATHS': ('A-TRIALS', '[3] At the same time, 257 patients', 1),
    'E-A-CONC': ('A-TRIALS', '[3] CONCLUSIONS: As compared with standard therapy', 1),
    'E-LED-X85': ('A-LEDGER', '| X85 | 2026-11-27 |', 1),
}
dims = base.dims


def ctx(population, time, estimand, unit, design, domain):
    return dict(population=population, time=time, estimand=estimand, unit=unit, design=design, domain=domain)


THEORY = ctx('none: conceptual frameworks', 'not applicable', 'what each framework proposes and how it would be tested',
             'framework', 'perspective, review and essay (no new primary data described in the abstracts)', 'theories of aging')
CLAIMS = [
    dict(id='CH3-EN-C001', anchor='Consider two recent frameworks from one laboratory.', kind='reported', role='asserted', critical=True, context=THEORY,
         evidence=['E-G-HDR', 'E-G-DEFAULT', 'E-G-UNIFY', 'E-G-COI', 'E-Y-HDR', 'E-Y-PROPOSE', 'E-Y-LOCAL', 'E-Y-ASYM', 'E-Y-PRC2', 'E-Y-TEST', 'E-Y-COI'], state='supported',
         rationale='Gladyshev 2026: aging as default outcome, imperfect processes, deleteriome accumulates and erodes functional reserve; covers damage, drift, remodeling, system failure without reducing to genes, pathways, hallmarks, pathologies. Yucel, Moliere and Gladyshev 2026 (Nature review per header): decanalization of cell identity; grammar written in development; local mechanisms with limited fidelity; most age-associated methylation gain in somatic mitotic tissues at PRC2-bound regions; testable predictions for stabilising architecture. All match. "One laboratory" rests on the shared author and affiliation in the headers. "Loosening" renders "decanalization"; "dividing tissues" renders "somatic mitotic tissues".',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C002', anchor='A third framework comes from evolutionary biology.', kind='reported', role='asserted', critical=False, context=THEORY,
         evidence=['E-L-HDR', 'E-L-WHY', 'E-L-COMPART', 'E-L-DST', 'E-L-MODEL', 'E-L-HYP'], state='supported',
         rationale='Lemaitre 2024 Essay: why and how we age intertwined; attempts compartmentalized; lack of clarity on DST and DTA relative to MA and AP; hierarchical model linking genes to vital rates; testable hypotheses on how selection shapes hallmarks. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C003', anchor='The words matter even inside one paper.', kind='reported', role='asserted', critical=False, context=THEORY,
         evidence=['E-G-HDR', 'E-G-MEASURE', 'E-G-REVERS'], state='supported',
         rationale='Biological age partially reversible or resettable in some contexts, aging itself irreversible; biomarkers make biological age imperfectly but increasingly measurable. Both quoted from the abstract; the reading that the two terms name different things is the chapter\'s inference, stated as such ("can be true only if").',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C004', anchor='A small synthetic calculation, built by this project with no real data, shows how this can happen.', kind='formal', role='asserted', critical=True,
         context=ctx('none: 1000 synthetic people', 'single period', 'risk by marker level; events before and after setting the marker low',
                     'synthetic person', 'exact arithmetic (script and tests)', 'confounding arithmetic only'),
         evidence=['E-CM-DESIGN', 'E-CM-OUT'], state='supported',
         rationale='1000 people, 300 with Z; marker high 80%/20%; event 40%/10% regardless of marker; 380 high with 110 events (0.289); 620 low with 80 events (0.129); ratio 2.24; events 190 before and after. All match. Formal claim.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH3-EN-C005', anchor='The marker in that calculation is an excellent predictor and a useless target', kind='reported', role='asserted', critical=True,
         context=ctx('myocardial infarction cases and controls in up to 20 studies', 'not stated in the excerpt', 'association of HDL cholesterol with MI, observational and genetic',
                     'person', 'mendelian randomisation', 'HDL cholesterol and myocardial infarction'),
         evidence=['E-V-HDR', 'E-V-BG', 'E-V-MR', 'E-V-OBS', 'E-V-GEN', 'E-V-INT', 'E-V-INT2'], state='supported',
         rationale='Observational OR 0.62 per SD; genotypes assigned at meiosis and unmodified by disease; genetic-score OR 0.93 (0.68-1.26); some genetic mechanisms that raise HDL do not seem to lower MI risk; challenges uniform translation. All match; source uses middle-dot decimals. "Heart attack" renders myocardial infarction; "natural experiment" glosses mendelian randomisation.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C006', anchor='Control without benefit is the next gap.', kind='reported', role='asserted', critical=True,
         context=ctx('15,067 patients at high cardiovascular risk', '12-month lipid change; trial stopped early', 'lipids, blood pressure, cardiovascular events and all-cause death',
                     'patient', 'randomized double-blind trial', 'CETP inhibition'),
         evidence=['E-T-AIM', 'E-T-STOP', 'E-T-N', 'E-T-LIPIDS', 'E-T-HR', 'E-T-MECH', 'E-T-OFF'], state='supported',
         rationale='Potent CETP inhibitor; 15,067 patients; HDL +72.1%, LDL -24.9%, SBP +5.4 mm Hg at 12 months; CV events HR 1.25; death HR 1.58 (1.14-2.19); terminated prematurely; unknown mechanism; off-target evidence but CETP-related harm not ruled out. All match. The protocol amendment (X28) is disclosed in the chapter footnote and the unresolved list.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C007', anchor='The Cardiac Arrhythmia Suppression Trial shows the same gap', kind='reported', role='asserted', critical=True,
         context=ctx('post-myocardial-infarction patients whose ventricular ectopy could be suppressed', 'mean 10 months', 'deaths by cause, active drug versus placebo',
                     'patient', 'randomized placebo-controlled trial', 'antiarrhythmic suppression of ventricular ectopy'),
         evidence=['E-C-DESIGN', 'E-C-STOP', 'E-C-N', 'E-C-DEATHS', 'E-C-MECH'], state='supported',
         rationale='Hypothesis: suppression of ventricular ectopy after MI reduces sudden death; only suppressible patients randomized; 1498 patients in the encainide/flecainide comparisons; mean 10 months; arrhythmic deaths 43 drug vs 16 placebo; discontinued for excess mortality; mechanisms unknown. All match. "Extra beats from the ventricles" renders ventricular ectopy; "control of the marker was achieved before randomisation" follows from the eligibility rule.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C008', anchor='The ACCORD trial moved a marker with a documented link to the outcome.', kind='reported', role='asserted', critical=True,
         context=ctx('10,251 patients with type 2 diabetes and CVD or additional risk factors', 'mean 3.5 years', 'glycated haemoglobin achieved; all-cause death; major CV events',
                     'patient', 'randomized trial', 'intensive glucose lowering'),
         evidence=['E-A-HDR', 'E-A-BG', 'E-A-N', 'E-A-ACHIEVED', 'E-A-DEATHS', 'E-A-CONC'], state='supported',
         rationale='Epidemiologic relationship between HbA1c and CV events; 10,251 patients; targets below 6.0% versus 7.0-7.9%; achieved 6.4% and 7.5% at 1 year; deaths 257 vs 203, HR 1.22 (1.01-1.46); over 3.5 years increased mortality without significant reduction in major CV events. All match.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C009', anchor='Here is the strongest objection to this chapter', kind='reported', role='asserted', critical=False,
         context=ctx('myocardial infarction cases and controls', 'not stated in the excerpt', 'observational versus genetic association of LDL cholesterol with MI',
                     'person', 'mendelian randomisation (positive control)', 'LDL cholesterol and myocardial infarction'),
         evidence=['E-V-HDR', 'E-V-LDL'], state='supported',
         rationale='LDL observational OR 1.54 per SD concordant with genetic-score OR 2.13. Matches. The objection itself is the outline\'s strongest counterexample, stated in the chapter\'s words; no source claim beyond the LDL figures.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH3-EN-C010', anchor='This book is not exempt from prior work either.', kind='reported', role='asserted', critical=False,
         context=ctx('none: project record about prior literature', 'as of 2026-11-27', 'prior work on queueing and capacity models of aging mortality',
                     'publication', "project ledger row (same assistant's earlier search)", 'originality of the book\'s framework'),
         evidence=['E-LED-X85'], state='supported',
         rationale='X85: Ledberg 2020 derives Gompertz from queueing theory; Karin/Alon SR model; critical slowing and dynamic resilience literature; originality to be downgraded to recombination and identifiability. Matches the ledger excerpt; the underlying papers were not re-read (footnote says so).',
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
        claim = dict(id=c['id'], artifact_id='A-CH3-EN', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH3-EN': arts['A-CH3-EN']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=base.REVIEWER, rationale=c['rationale'],
                                   bound_hashes=bound, record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch03-four-links-pilot-en',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Ten paragraph units of the English chapter 3 draft v0.1 that carry numbers or source statements; not an exhaustive claim inventory',
                         human_inventory_complete=False, candidate_units=10, registered_claims=len(claims),
                         note='Reasoning and value paragraphs (I1 statement, frameworks compared, breadth has a cost, entropy, information, identity, control, prediction defined, answer to the objection, benefit is not deciding, map of the book, candidate shifts) make no source claim. Abstract depth throughout; one synthetic claim is formal; one claim rests on a project record.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH3-EN-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent review by an aging biologist, a trialist or a philosopher (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH3-EN-DEPTH', status='open', blocks_formal_release=True,
                 question='All seven studies read at abstract depth; ILLUMINATE protocol amendment (X28) and the X85 prior-work search unresolved; two of three theory papers share an author',
                 next_action='Read full texts; add a framework from outside these groups if the author wants balance',
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
