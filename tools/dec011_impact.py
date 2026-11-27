"""Dependency invalidation record for DEC-011/DEC-012/X125-X137, the ch5 pilot and DEC-016 (08_LINEAGE §6.3).

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
C4 = 'change:X129-X132_margin_recovery_anchors'
C5 = 'change:X133-X137_PI_novelty'
C6 = 'change:ch05_pilot_V7-06_reassign'
C7 = 'change:DEC-016_english_first_language'
CHANGES = [C1, C2, C3, C4, C5, C6, C7]
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
         + [(C4, p) for p in ['books/ARCHITECTURE_DECISION_2026-11-27.md', 'knowledge_base/KERNEL.md',
                              'review/RESTRUCTURE_WORKFLOW_CONFORMANCE_2026-11-27.md', 'books/manuscript/OUTLINE_v1.md']]
         + [(C5, p) for p in ['papers/PI_rejuvenation_identifiability/PROTOCOL.md', 'knowledge_base/MASTER.md',
                              'books/ARCHITECTURE_DECISION_2026-11-27.md', 'knowledge_base/README.md',
                              'review/RESTRUCTURE_WORKFLOW_CONFORMANCE_2026-11-27.md', 'knowledge_base/CLAIM_LEDGER.md#X125']]
         + [(C6, p) for p in ['books/manuscript/outline_build.py', M + DEMOS[1], M + 'README.md']]
         + [(C7, p) for p in ['books/manuscript/outline_build.py', 'books/BOOK_PROPOSAL.md', M + 'README.md',
                              'papers/PUBLICATION_MAP.md', 'knowledge_base/MASTER.md', M + DEMOS[1],
                              'books/market/MARKET_POSITIONING_2026-11.md', M + 'en/']]
         + [('books/manuscript/outline_build.py', p) for p in ['books/manuscript/outline_v1.json',
                                                               'books/manuscript/OUTLINE_v1.md']]
         + [('books/manuscript/OUTLINE_v1.md', p) for p in ['knowledge_base/MASTER.md', 'knowledge_base/README.md',
                                                            'books/ARCHITECTURE_DECISION_2026-11-27.md',
                                                            'review/RESTRUCTURE_WORKFLOW_CONFORMANCE_2026-11-27.md']]
         + [('books/ARCHITECTURE_DECISION_2026-11-27.md', 'knowledge_base/MASTER.md'),
            ('knowledge_base/MASTER.md', 'README.md'), ('papers/PUBLICATION_MAP.md', 'README.md'),
            ('knowledge_base/MASTER.md', 'external:Linear THE-227/228/229/230/231')])
SR, KV, RV = 'stale_requires_review', 'kept_valid', 'revised'
ACTIONS = {
    'knowledge_base/MASTER.md': ('global', RV, '§3/§4 改为已定，历史候选原文保留；DEC-011–015；v1.3.2：PI 行改协议 v3 与 X137，§3 无继承章改为 6、7、9；v1.3.3：DEC-016 行、权威路径表加英文书稿行'),
    'books/BOOK_PROPOSAL.md': ('local', RV, '文件头指针：§3 被 OUTLINE_v1 取代，§4 证据契约继续有效；DEC-016 指针：§3 末尾中文字数预算是历史'),
    M + 'README.md': ('local', RV, '文件头指针：方案 A 地图是历史，现行见 OUTLINE_v1；CH15 链接文字注明现为第 5 章 v0.3；DEC-016 指针指向 en/'),
    'books/CHAPTER_CROSSWALK_DRAFT.md': ('local', KV, '主题桶本就声明不是终稿章号；章级落点改由 outline_v1.json 承担'),
    M + 'PART_VI_维护容量_写作骨架.md': ('local', SR, '六模块分到第 15/17/19/21/22 章；写作时重审'),
    M + DEMOS[0]: ('local', SR, '新第 1 章；"论文关联"仍写 P1/P2；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[1]: ('local', RV, 'v0.3：§7.2 试点原位修订——章号改第五章，关联论文改为 PI ①②，并入 V7-06 的机制特异性与使用规则，补 X126/X135；5 段主张逐字绑定（pilots/ch05_measurement_contract）；未绑定的 3 段仍待人工审读。DEC-016：字节不改，成为英文稿 v0.1 的来源，在英文稿绑定前仍是已绑定版本'),
    M + DEMOS[2]: ('local', SR, '并入第 21 章；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[3]: ('local', SR, '并入第 21 章；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[4]: ('local', SR, '→第 22 章；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[5]: ('local', SR, '→第 19 章；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[6]: ('local', SR, '→第 15 章；论文标签与新章号已在稿内标注，正文未重审'),
    M + DEMOS[7]: ('local', SR, '→第 17 章；标题已改为新章号（本稿原无论文关联行），正文未重审'),
    'books/pr2_candidates/': ('local', SR, 'PR2 候选样章用自身章号；只作素材，不改'),
    'papers/PUBLICATION_MAP.md': ('global', RV, '文件头 DEC-012 指针；正文保留历史；DEC-016 指针：论文以英文撰写与投稿'),
    'papers/P1_identity_selection/SURVIVOR_IDENTIFICATION_NOTE_2026-11-27.md': ('local', KV, 'PI 第①层输入，内容不变'),
    **{'papers/P2_weighting_observability/' + n: ('local', KV, 'PI 第②层输入，内容不变') for n in P2N},
    'knowledge_base/README.md': ('local', RV, '架构段：无继承章改为 6、7、9 并链接试点；论文段加 v3/X133–X137'),
    'knowledge_base/CLAIM_LEDGER.md#X125': ('local', RV, '原文不改；X133 追加更正（Yücel 2024 是第①②层定性先行）'),
    'books/manuscript/outline_build.py': ('local', RV, 'ASSIGN 一处：V7-06 由 6 改为 5，附注释；DEC-016：加 TITLES_EN/PARTS_EN/VOLUMES_EN 与 language 字段，ASSIGN 与章数不变'),
    'books/manuscript/outline_v1.json': ('local', RV, '由 outline_build.py 重新生成；源文 hash 不变；DEC-016 后多出英文章名与 language 字段'),
    'knowledge_base/KERNEL.md': ('global', RV, 'v0.9.10：§4/§5 论文标签改为 PI；四个尺度注明经典出处与余量—年数公式；不变式无增删'),
    'books/ARCHITECTURE_DECISION_2026-11-27.md': ('global', RV, '§3 第 9 章条件未触发，保留 33 章；锚点表与 K3 处置更新；§6 两条触发行加处置：PI 检索未触发、§7.2 映射错误已触发一次'),
    'review/RESTRUCTURE_WORKFLOW_CONFORMANCE_2026-11-27.md': ('local', RV, '§1/§2/§3/§4 追加后续：试点已执行、近邻检索门槛 1–2 完成、Yücel 已读、V7-06 改归'),
    'books/manuscript/OUTLINE_v1.md': ('local', RV, 'C4：章数与证据等级不变；C6：重新生成，第 5 章继承 V6-15、V7-06，第 6 章变为新写；C7：重新生成，标题列改为英文/中文，继承列不变'),
    'knowledge_base/CLAIM_LEDGER.md#X94': ('local', RV, '原文与数值不改；X128 追加作者归属更正'),
    'knowledge_base/experiments/sr_published_params_robustness.py': ('local', RV, '只改文档串的作者归属；数值、变量名不变'),
    'knowledge_base/experiments/SR_PUBLISHED_PARAMS_ROBUSTNESS_2026-11-27.md': ('local', RV, '文件头加更正注'),
    'papers/PI_rejuvenation_identifiability/PROTOCOL.md': ('local', RV, 'v2 引用 X125–X128；v3：近邻检索门槛 1–2 完成，主张收窄为三条，加必引清单与禁用词（X133–X137）'),
    'README.md': ('global', RV, '"待作者裁决"改为已定，并指向 OUTLINE_v1 与 PI'),
    'books/market/MARKET_POSITIONING_2026-11.md': ('local', RV, '§3.1 加 DEC-016 更新：M-A 的中文为源前提与 M-C 作废，改列 E-1/E-2/E-3 篇幅选项（作者未裁决）；§1.4 简体中文解读与 MR-6 同步'),
    M + 'en/': ('local', RV, '新建：英文书稿目录与工作规则；第 5 章英文稿 v0.1 由 v0.3 改写，未逐字绑定来源'),
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
    queue = [n for n in impact(EDGES, CHANGES) if not n.startswith('change:')]
    missing = set(queue) ^ set(ACTIONS)
    if missing:
        raise ValueError(f'actions and computed stale queue differ: {sorted(missing)}')
    return {'change_ids': CHANGES, 'tool': 'research_assurance.core.impact (transitive, cycle-safe)',
            'edges': [list(e) for e in EDGES],
            'stale_queue': [{'node': n, 'scope': ACTIONS[n][0], 'state_after_this_turn': ACTIONS[n][1],
                             'note': ACTIONS[n][2]} for n in queue],
            'frozen_not_invalidated': FROZEN,
            'warning': 'stale_requires_review is not refutation; kept_valid/revised are recorded human judgements, not machine-verified truth.'}


if __name__ == '__main__':
    OUT.write_text(json.dumps(build(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
