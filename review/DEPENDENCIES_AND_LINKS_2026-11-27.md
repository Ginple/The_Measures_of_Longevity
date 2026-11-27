# X39 下游及历史链接：限定范围复查

2026-11-27；同助手定向复核，不是独立审阅。范围仅下列文件及对 `papers/`、`books/` 的关键词搜索，不是全库语义证明。

## 状态周转

- [源模型](../longevity_state_turnover/状态还在_不等于细胞没换.md) §4：`m` 成熟退出，`d` 其他丢失；明确模型不含增殖、逆转、迁移、年龄依赖及空间分区。`T*=j/(m+d)` 有限稳态要求 `m+d>0`；静态图像不能识别真实速率。
- [V7 §37](../corpus/longevity_v7/长寿研究_V7_谁在变年轻.md)：参数标签与公式一致，已有“人工”“理想”限定，但正文未展开**常风险、无新标记及竞争退出模型**；预定修订时应补这些假设，不能无条件推广。该稿及配对副本属冻结来源，本轮未覆盖或重签；此项仍待编辑/外审复核。
- [恢复后随机化合同](../knowledge_base/experiments/POST_RECOVERY_RANDOMIZATION_CONTRACT_DRAFT.md) §4：旧“转出与死亡等之和”可能暗示一般模型可直接辨识；本轮限定为 I6 模型的成熟与其他丢失风险之和，提醒更一般模型需新建假设。
- [KERNEL](../knowledge_base/KERNEL.md) I6 及状态周转表已改；`papers/`、`books/` 中以 m+d、成熟、标签及周转等关键词检索，未发现需要立即修改的同公式重复定义；不代表逐段人工审查或排除同义句。标题地图仅记录 V7 §37 标题，不能承担内容复审。
- 复核仍需：对全库同义句和跨学科推论作人工检索，核独立方法学审阅及预设标记方案。X39 保持 open。

## 已知 29 个断链，不用刷新基线消除历史

[历史逐对清单](../governance/legacy_broken_links.json)包含 22 条外来通用 playbook 引向未随仓库提供的 `SKILLS/GSK-*`；本仓库 `skills/` 下的十个技能不是同名同内容替代，不应伪造指向或称它们等价。

另有 7 条历史 [HANDOFF](../HANDOFF.md) 链接含旧前缀，现行入口如下（链接是替代**位置**，不意味着文件版本与当时字节相同）：

| 历史目标 | 当前入口 |
|---|---|
| corpus/editions/v6 | [V6 稿件](../corpus/longevity_v6/长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md) |
| corpus/editions/v7 | [V7 稿件](../corpus/longevity_v7/长寿研究_V7_谁在变年轻.md) |
| papers/P1_identity_selection/PROTOCOL.md | [P1 协议](../papers/P1_identity_selection/PROTOCOL.md) |
| papers/P2_weighting_observability/PROTOCOL.md | [P2 协议](../papers/P2_weighting_observability/PROTOCOL.md) |
| papers/P3_research_assurance/PROTOCOL.md | [P3 协议](../papers/P3_research_assurance/PROTOCOL.md) |
| papers/PUBLICATION_MAP.md | [出版地图](../papers/PUBLICATION_MAP.md) |
| books/longevity/BOOK_PROPOSAL.md | [书稿提案](../books/BOOK_PROPOSAL.md) |

本轮保留历史 HANDOFF 及外来 playbook，未直接修补原文，也不改 29 项允许清单；需作者确定历史文档修订策略和原文件继承语义。自动扫描只处理简单相对行内 Markdown 链接，不覆盖外链、片段、引用式链接或全部格式，不是完整链接可用性审计。
