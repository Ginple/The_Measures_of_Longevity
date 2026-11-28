"""Bind selected ch5 (测量合同) claims to exact source spans — 08_LINEAGE §7.2 pilot, step 2.

Run deliberately to (re)bind after a reviewed change; tests never run it. Spans are located by
anchor text, then frozen into project.json as line numbers + exact text + sha256, so any later
edit to the chapter, an excerpt or a derivation shows up as drift in `inspect_project`.
Assessments below are the same assistant's source comparison, not independent review.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import claim_record_hash, read_span  # noqa: E402

HERE = 'knowledge_base/pilots/ch05_measurement_contract'
REVIEWER = 'same-assistant-source-comparison-not-human-or-independent-review'
ARTIFACTS = [
    ('A-CH5', 'books/manuscript/CH15_测量合同_示范稿.md', 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'demo draft v0.3 (OUTLINE_v1 ch5), working copy'),
    ('A-V7', 'corpus/longevity_v7/长寿研究_V7_谁在变年轻.md', 'manuscript', 'longevity-manuscript', 'fulltext', '',
     'V7 frozen corpus (DEC-005)'),
    ('A-P2', 'knowledge_base/experiments/P2_TWO_TYPE_SHARP_BOUNDS_2026-11-27.md', 'code', 'longevity-project-derivation',
     'fulltext', '', 'project technical memo; exact-rational script and tests alongside'),
    ('A-GALLERI', f'{HERE}/evidence/NHS_GALLERI_excerpts.txt', 'source', 'study-NHS-Galleri', 'excerpt',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC7619610/', 'Europe PMC fullTextXML snapshot 2026-11-27; selected quotes'),
    ('A-WARM', f'{HERE}/evidence/WARMBRUNN_excerpts.txt', 'source', 'study-CALERIE-2', 'excerpt',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC13094879/', 'PMC page + figshare S3 snapshot 2026-11-27; selected quotes'),
    ('A-CLOCK', f'{HERE}/evidence/CLOCK_SURROGATE_abstracts.txt', 'source', 'clock-surrogate-literature', 'abstract',
     'https://doi.org/10.1016/j.exger.2026.113367', 'Europe PMC abstracts 2026-11-27 (Yi 2026; Borrus 2026)'),
]
# evidence id -> (artifact, anchor substring of the first line, number of lines)
EVIDENCE = {
    'E-GAL-N': ('A-GALLERI', '142,250 (99.6%)', 1),
    'E-GAL-FU': ('A-GALLERI', 'a median of 17', 1),
    'E-GAL-COUNTS': ('A-GALLERI', 'There were 706 and 688', 1),
    'E-GAL-IRR': ('A-GALLERI', 'IRR: 1.03 [0.92-1.14]', 1),
    'E-GAL-SEQ': ('A-GALLERI', 'Testing stopped at the first', 1),
    'E-GAL-MORT': ('A-GALLERI', 'not powered for mortality', 1),
    'E-WARM-DESIGN': ('A-WARM', 'CALERIE-2) trial (n = 220)', 1),
    'E-WARM-STRATA': ('A-WARM', 'regardless of randomization', 1),
    'E-WARM-20': ('A-WARM', 'regained >5% of baseline weight', 1),
    'E-WARM-190': ('A-WARM', 'For this secondary analysis, 190', 1),
    'E-WARM-S3': ('A-WARM', 'Table S3 row | AUC insulin', 1),
    'E-YI-SCOPE': ('A-CLOCK', 'We systematically reviewed', 2),
    'E-YI-CONC': ('A-CLOCK', 'no comparative study or study of patient-important', 1),
    'E-YI-SURR': ('A-CLOCK', 'no trial-level surrogate-endpoint validation', 1),
    'E-YI-CONCL': ('A-CLOCK', 'exploratory or adjunctive', 1),
    'E-BORRUS-NONE': ('A-CLOCK', 'no additional clocks reach statistical significance', 1),
    'E-BORRUS-CRIT': ('A-CLOCK', 'propose three criteria', 1),
    'E-P2-SETUP': ('A-P2', '假设两时点 `p=0.5`', 1),
    'E-P2-WORLDS': ('A-P2', '| A | (0.2,1)', 2),
    'E-P2-SCOPE': ('A-P2', '这不是说每种生物体系都存在这两个世界', 1),
    'E-V7-FOUR': ('A-V7', '预测能力、机制特异性、干预响应性、替代终点资格是四种不同属性', 1),
    'E-V7-RULES': ('A-V7', '**本稿的使用规则**：预先指定主钟', 1),
}
DIMS = ('source_support', 'extraction', 'measurement', 'statistical_inference', 'causal_identification',
        'transportability', 'net_benefit', 'independent_review')


def dims(**kw):
    return {d: kw.get(d, 'unknown') for d in DIMS}


CLAIMS = [
    dict(id='CH5-C001', anchor='这种区分并不只是理论上的谨慎', kind='reported', role='asserted', critical=True,
         context=dict(population='Yi 2026: 26 human geroscience intervention studies reporting a DNAm clock and a clinical outcome; Borrus 2026: re-analysed published single-clock intervention datasets',
                      time='pre-post intervention windows of the included studies; no long-term outcome follow-up implied',
                      estimand='study-level concordance between clock change and clinical-outcome change; significance of additional clocks; not intervention efficacy',
                      unit='study (Yi); dataset x clock (Borrus)',
                      design='systematic review (abstract only) and secondary re-analysis; different lab families',
                      domain='DNA-methylation clocks as intervention endpoints'),
         evidence=['E-YI-SCOPE', 'E-YI-CONC', 'E-YI-SURR', 'E-YI-CONCL', 'E-BORRUS-NONE'], state='supported',
         rationale='Every number and qualifier in the paragraph matches the quoted abstracts (26 studies, comparative-only scope, no trial-level surrogate validation, very low certainty, no additional clock significant). Abstract depth only: inclusion criteria, concordance definitions and Borrus dataset list not checked. Paragraph also says "this does not show the interventions failed", which is an interpretive limit, not a source claim.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH5-C002', anchor='CALERIE 的一项 2026 年分析正提供了这样的例子', kind='reported', role='asserted', critical=True,
         context=dict(population='CALERIE-2 non-obese adults 21–50 y; 190 of 220 randomized with available OGTT data (120 CR, 70 control)',
                      time='trajectory defined on months 12–24, inside the 2-year trial (maintenance phase), not after the intervention stopped',
                      estimand='post-hoc trajectory-group comparison balanced by propensity weighting; not a randomized contrast and not life-years',
                      unit='participant; per-variable analysable counts differ from 190',
                      design='secondary analysis of an RCT, groups formed after randomization regardless of arm',
                      domain='insulin-IGF-1 markers and a biomarker biological-age estimate'),
         evidence=['E-WARM-DESIGN', 'E-WARM-STRATA', 'E-WARM-20', 'E-WARM-190', 'E-WARM-S3'], state='supported',
         rationale='190/20/12-24-month window/maintenance phase/regardless-of-randomization all match; "57 missing baseline insulin AUC" matches Table S3. Arm composition of the 20 (9 CR, 11 control) is in the project audit, not re-checked here, and the chapter does not state it. Denominator of 29.8% remains unresolved (X60).',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH5-C003', anchor='甚至在一个极简的两类线性模型里', kind='formal', role='asserted', critical=True,
         context=dict(population='none: constructed two-type noiseless linear mixture, not human data',
                      time='two time points with fixed known weight p=0.5',
                      estimand='set of within-type changes compatible with an observed aggregate change',
                      unit='abstract operational type, not a tracked cell',
                      design='constructive counterexample with exact rationals (script + tests)',
                      domain='linear aggregate readouts only; nonlinear clocks excluded'),
         evidence=['E-P2-SETUP', 'E-P2-WORLDS', 'E-P2-SCOPE'], state='supported',
         rationale='Worlds A and B give the same aggregate 0.6->0.4 with type-1 change +0.6 vs -1; the chapter states the model is not an estimate of real bodies, matching the memo scope line. Formal claim: support means the construction is valid, not that the biology behaves this way.',
         dimensions=dims(source_support='supported', extraction='supported', transportability='not_applicable')),
    dict(id='CH5-C004', anchor='NHS-Galleri 是一项在英格兰开展的大型随机试验', kind='reported', role='asserted', critical=True,
         context=dict(population='England, volunteers aged 50–77 invited by NHS; 142,250 randomized',
                      time='3 annual screening rounds, median 17 months after the third round; mortality analyses pending at 3 and 6 years',
                      estimand='ITT incidence rate ratio of stage III/IV cancer among 12 prespecified types; secondary outcomes descriptive',
                      unit='randomized participant',
                      design='randomized controlled trial, fixed-sequence testing',
                      domain='multi-cancer early detection blood test added to standard care'),
         evidence=['E-GAL-N', 'E-GAL-FU', 'E-GAL-COUNTS', 'E-GAL-IRR', 'E-GAL-SEQ', 'E-GAL-MORT'], state='supported',
         rationale='约14.2万 = 142,250 randomized; 17-month median; 706 vs 688; IRR 1.03 (0.92–1.14); secondary endpoints descriptive after the primary step failed; mortality not yet reported. Supplement tables not read.',
         dimensions=dims(source_support='supported', extraction='supported')),
    dict(id='CH5-C005', anchor='所以，一项负责任的时钟研究至少应当', kind='normative', role='proposal', critical=False,
         context=dict(population='authors and readers of clock-based intervention studies',
                      time='current reporting practice',
                      estimand='minimum reporting rules; not an evidence claim',
                      unit='study report',
                      design='editorial rule inherited from V7-06, informed by Borrus 2026 criteria',
                      domain='DNA-methylation clock studies'),
         evidence=['E-V7-RULES', 'E-V7-FOUR', 'E-BORRUS-CRIT'], state='unknown',
         rationale='Lineage record: rule text carried from V7-06 (frozen corpus) into ch5. A normative proposal is not supported or refuted by a source; kept unknown on purpose.',
         dimensions=dims(net_benefit='unknown')),
]


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def locate(path, anchor, n):
    lines = (ROOT / path).read_text(encoding='utf-8').splitlines()
    hits = [i for i, line in enumerate(lines, 1) if anchor in line]
    if len(hits) != 1:
        raise ValueError(f'{path}: anchor {anchor!r} found {len(hits)} times')
    start = hits[0]
    return [start, start + n], read_span((ROOT / path).read_bytes(), start, start + n)


def build():
    arts = {a[0]: dict(id=a[0], path=a[1], sha256=sha(a[1]), role=a[2], family=a[3], access_depth=a[4], url=a[5],
                       version=a[6]) for a in ARTIFACTS}
    evidence = []
    for eid, (aid, anchor, n) in EVIDENCE.items():
        span, text = locate(arts[aid]['path'], anchor, n)
        evidence.append(dict(id=eid, artifact_id=aid, lines_1based_halfopen=span, text=text))
    ev = {e['id']: e for e in evidence}
    claims = []
    for c in CLAIMS:
        span, text = locate(arts['A-CH5']['path'], c['anchor'], 1)
        claim = dict(id=c['id'], artifact_id='A-CH5', lines_1based_halfopen=span, text=text, kind=c['kind'],
                     role=c['role'], critical=c['critical'], context=c['context'], evidence_ids=c['evidence'])
        bound = {'A-CH5': arts['A-CH5']['sha256']}
        bound.update({ev[e]['artifact_id']: arts[ev[e]['artifact_id']]['sha256'] for e in c['evidence']})
        claim['assessment'] = dict(state=c['state'], reviewer=REVIEWER, rationale=c['rationale'], bound_hashes=bound,
                                   record_sha256='', dimensions=c['dimensions'])
        if c['state'] != 'unknown':
            claim['assessment']['record_sha256'] = claim_record_hash(claim, ev)
        claims.append(claim)
    return {
        'schema_version': '0.1', 'project_id': 'longevity-ch05-measurement-contract-pilot',
        'authors': ['project-author-unassigned'],
        'coverage': dict(scope='Five selected paragraphs of OUTLINE_v1 ch5 demo draft v0.3; not an exhaustive claim inventory of the chapter',
                         human_inventory_complete=False, candidate_units=5, registered_claims=len(claims),
                         note='Paragraph units may hold several propositions. CALERIE methylation/bone paragraph, DO-HEALTH paragraph and Malagón microsimulation paragraph are not registered.'),
        'artifacts': list(arts.values()), 'evidence': evidence, 'claims': claims, 'reviews': [],
        'debts': [
            dict(id='CH5-INDEPENDENT-REVIEW', status='closed', blocks_formal_release=False,
                 question='No independent domain or statistical review of these claims (D05)',
                 next_action='None: the owner waived independent human review (DEC-020, 2026-11-28); tools/claim_audit_agent.py runs mechanical checks in its place',
                 closure_evidence='DEC-020 owner waiver plus review/CLAIM_AUDIT_AGENT_RECEIPT.json (V1, encoded properties only; not a review record and not scientific verification)'),
            dict(id='CH5-INVENTORY', status='open', blocks_formal_release=True,
                 question='3 of 7 footnoted evidence paragraphs unregistered; Yi 2026 read at abstract depth only',
                 next_action='Register remaining paragraphs; read Yi full text if access allows',
                 closure_evidence='Declared complete inventory with human acceptance'),
        ],
    }


if __name__ == '__main__':
    out = ROOT / HERE / 'project.json'
    data = build()
    if '--check' in sys.argv:
        sys.exit(0 if json.loads(out.read_text(encoding='utf-8')) == data else 1)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(out.relative_to(ROOT), len(data['claims']), 'claims', len(data['evidence']), 'evidence')
