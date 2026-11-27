"""Dependency invalidation record for DEC-011/DEC-012/X125-X128 (08_LINEAGE §6.3).

Edges and per-node actions are human judgements; the stale queue itself is computed with
research_assurance.core.impact so the record cannot silently omit a dependent node.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from research_assurance.core import impact  # noqa: E402

OUT = ROOT / 'review/DEC011_DEC012_IMPACT_2026-11-27.json'
C1, C2, C3 = 'change:DEC-011_architecture', 'change:DEC-012_papers', 'change:X125-X128_prior_art_and_attribution'
M = 'books/manuscript/'
DEMOS = ['CH01_长寿的五个问题_示范稿.md', 'CH15_测量合同_示范稿.md', 'CH19_谁替谁维护_示范稿.md',
         'CH20_平均不等于及时_示范稿.md', 'CH21_有余量却用不上_示范稿.md', 'CH22_清除之后谁来接班_示范稿.md',
         'CH23_状态还在细胞换了吗_示范稿.md', 'CH24_修好这一次还剩多少下一次_示范稿.md']
P2N = ['BINARY_CAPTURE_IDENTIFICATION_NOTE_2026-11-27.md', 'DECOMPOSITION_NOTE_2026-11-27.md',
       'SHARED_COMPONENT_CONSTRAINT_2026-11-27.md']
EDGES = ([(C1, p) for p in ['knowledge_base/MASTER.md', 'books/BOOK_PROPOSAL.md', M + 'README.md',
                            'books/CHAPTER_CROSSWALK_DRAFT.md', M + 'PART_VI_维护容量_写作骨架.md', 'books/pr2_candidates/']]
         + [(C1, M + d) for d in DEMOS]
         + [(C2, p) for p in ['knowledge_base/MASTER.md', 'papers/PUBLICATION_MAP.md', M + DEMOS[0], M + DEMOS[1],
                              'papers/P1_identity_selection/SURVIVOR_IDENTIFICATION_NOTE_2026-11-27.md',
                              'knowledge_base/KERNEL.md']]
         + [(C2, 'papers/P2_weighting_observability/' + n) for n in P2N]
         + [(C3, p) for p in ['knowledge_base/CLAIM_LEDGER.md#X94',
                              'knowledge_base/experiments/sr_published_params_robustness.py',
                              'knowledge_base/experiments/SR_PUBLISHED_PARAMS_ROBUSTNESS_2026-11-27.md',
                              'papers/PI_rejuvenation_identifiability/PROTOCOL.md']]
         + [('knowledge_base/MASTER.md', 'README.md'), ('papers/PUBLICATION_MAP.md', 'README.md'),
            ('knowledge_base/MASTER.md', 'external:Linear THE-227/228/229/230/231')])
SR, KV, RV = 'stale_requires_review', 'kept_valid', 'revised'
ACTIONS = {
    'knowledge_base/MASTER.md': ('global', RV, '§3/§4 改为已定，历史候选原文保留；DEC-011–014；v1.3'),
    'books/BOOK_PROPOSAL.md': ('local', RV, '文件头指针：§3 被 OUTLINE_v1 取代，§4 证据契约继续有效'),
    M + 'README.md': ('local', RV, '文件头指针：方案 A 地图是历史，现行见 OUTLINE_v1'),
    'books/CHAPTER_CROSSWALK_DRAFT.md': ('local', KV, '主题桶本就声明不是终稿章号；章级落点改由 outline_v1.json 承担'),
    M + 'PART_VI_维护容量_写作骨架.md': ('local', SR, '六模块分到第 15/17/19/21/22 章；写作时重审'),
    M + DEMOS[0]: ('local', SR, '新第 1 章；"论文关联"仍写 P1/P2'),
    M + DEMOS[1]: ('local', SR, '新第 5 章；"关联论文"仍写 P1/P2；建议作为 §7.2 单章试点'),
    M + DEMOS[2]: ('local', SR, '并入第 21 章'),
    M + DEMOS[3]: ('local', SR, '并入第 21 章'),
    M + DEMOS[4]: ('local', SR, '→第 22 章'),
    M + DEMOS[5]: ('local', SR, '→第 19 章'),
    M + DEMOS[6]: ('local', SR, '→第 15 章'),
    M + DEMOS[7]: ('local', SR, '→第 17 章；标题行仍写"第24章"'),
    'books/pr2_candidates/': ('local', SR, 'PR2 候选样章用自身章号；只作素材，不改'),
    'papers/PUBLICATION_MAP.md': ('global', RV, '文件头 DEC-012 指针；正文保留历史'),
    'papers/P1_identity_selection/SURVIVOR_IDENTIFICATION_NOTE_2026-11-27.md': ('local', KV, 'PI 第①层输入，内容不变'),
    **{'papers/P2_weighting_observability/' + n: ('local', KV, 'PI 第②层输入，内容不变') for n in P2N},
    'knowledge_base/KERNEL.md': ('global', KV, '不变式/定义不受影响；§4 表"P1/P2"标签留待下个 KERNEL 版本统一改为 PI'),
    'knowledge_base/CLAIM_LEDGER.md#X94': ('local', RV, '原文与数值不改；X128 追加作者归属更正'),
    'knowledge_base/experiments/sr_published_params_robustness.py': ('local', RV, '只改文档串的作者归属；数值、变量名不变'),
    'knowledge_base/experiments/SR_PUBLISHED_PARAMS_ROBUSTNESS_2026-11-27.md': ('local', RV, '文件头加更正注'),
    'papers/PI_rejuvenation_identifiability/PROTOCOL.md': ('local', RV, '新建协议 v2，引用 X125–X128'),
    'README.md': ('global', RV, '"待作者裁决"改为已定，并指向 OUTLINE_v1 与 PI'),
    'external:Linear THE-227/228/229/230/231': ('global', RV, '评论更正：上一轮 2bb8edc 未推送已丢失，以本 PR 为准'),
}
FROZEN = {
    'papers/P1_identity_selection/PROTOCOL.md': '冻结历史协议：被 PI 取代，但字节不改（上一轮在文件头插注不合规，本次撤回该做法）',
    'papers/P2_weighting_observability/PROTOCOL.md': '同上',
    'papers/P3_research_assurance/PROTOCOL.md': '冻结；P3 处置记录在 MASTER 与 PUBLICATION_MAP',
    'review/ARCHITECTURE_AUDIT_PACKET_L2_2026-11-27.md': 'L2 盲审包须对 L1 与本决定保持不可见：不失效、不修改',
    'corpus/longevity_v6/': '冻结语料，只读；hash 由 tests/test_outline_source_binding.py 复核',
    'corpus/longevity_v7/': '同上',
}


def build():
    queue = [n for n in impact(EDGES, [C1, C2, C3]) if not n.startswith('change:')]
    missing = set(queue) ^ set(ACTIONS)
    if missing:
        raise ValueError(f'actions and computed stale queue differ: {sorted(missing)}')
    return {'change_ids': [C1, C2, C3], 'tool': 'research_assurance.core.impact (transitive, cycle-safe)',
            'edges': [list(e) for e in EDGES],
            'stale_queue': [{'node': n, 'scope': ACTIONS[n][0], 'state_after_this_turn': ACTIONS[n][1],
                             'note': ACTIONS[n][2]} for n in queue],
            'frozen_not_invalidated': FROZEN,
            'warning': 'stale_requires_review is not refutation; kept_valid/revised are recorded human judgements, not machine-verified truth.'}


if __name__ == '__main__':
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
