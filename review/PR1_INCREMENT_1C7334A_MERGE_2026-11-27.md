# PR #1 增量审计与合并（dd47ce6 → 1c7334a，2026-11-27）

**背景：** 本分支此前审计的是 PR #1 的 dd47ce6（见 [PR1_AUDIT_DD47CE6](PR1_AUDIT_DD47CE6_2026-11-27.md)）。之后 PR #1 继续推进了 9 个提交、35 个文件，与本分支并行地从 PR #2 里择取了相同的题目。这次合并为真合并（merge commit），因此 PR #1 的全部提交都是 PR #3 的祖先。

**性质：** 软件合同与内容的定向审计，不是独立外审（D05 open）。

## 1. 冲突与处理

| 冲突 | 原因 | 处理 |
|---|---|---|
| 台账 X81–X91 同号不同义 | 两边都从 X81 起编号 | 本分支 X81–X111 保持不变；PR #1 新增条目整体 +31（X81→X112 … X91→X122）。做法是先在 PR #1 一侧改号，再以 dd47ce6 为基做三方合并，因此只改 PR #1 引入的文本。涉及 8 个增量文件、KERNEL、README 与 `review/PR2_AUDIT_AND_INTEGRATION_2026-11-27.md` |
| KERNEL 两个不同的 v0.9.8 | 两边各自升版 | 本分支内容保留为 v0.9.8；PR #1 的变更记为 **v0.9.9**，并注明原号；文件头升到 v0.9.9 |
| README 同一位置各自追加 | 并行追加 | 两段都保留：本分支在前，PR #1 段落降为三级标题，统一置于"PR #1 增量"下 |
| 3 个文件 add/add | 两边都从 PR #2 移植，PR #1 又加固过 | 采用 PR #1 版本，它是严格加强：`rounded_percentage_denominators.py` 增加纯小数格式与空输入检查；`assurance_fixture_comparison.py` 把 `assert` 改为 fail-closed 的 `ValueError` 并补了测试 |
| 5 个同名测试分处 `tests/` 与 `knowledge_base/experiments/` | 本分支移植 PR #2 时放进 `tests/`，PR #1 放进 experiments，导致 unittest 发现时模块名冲突，**validation 直接失败** | 删除 `tests/` 下的 5 份。PR #1 版本是超集（3→4、1→1、4→6、3→4、4→6 项），引用这些测试的 4 份文档链接已改指 experiments |

## 2. PR #1 增量的内容判定

| 条目 | 判定 |
|---|---|
| X116（原 X85）LoDoCo2 导入期 β 在区间外 | 与本分支 X102 一致；本轮已对原文逐字核过 |
| X112/X113、X114、X117–X120、X60 两条后续 | 与 X103–X110 是同一发现的两次核读。台账有对应表，并明确**不算两项独立证据** |
| X115 FIND 两篇论文共用同一组人年 | 新发现，保留为 open |
| X121 HALE 图 3A：用国家间 SD 标为"95% CI" | 新发现，保留为 open |
| X122 HALE 图 3A 均值轴与差值轴共享变量 | 恒等式 Cov((L+H)/2, L−H) = [Var(L) − Var(H)]/2 已核对，正确；属于 Bland–Altman 型结构，是已知方法学问题，不称首创。对书稿有用："健康缺口随长寿扩大"有一部分来自坐标构造 |
| 合成实验（`mean_difference_shared_axes`、`randomized_mediator_equivalent_worlds`、`shared_type2_bounds` 等） | 只用标准库和精确分数，测试只检验算术 |

## 3. 未做与保留

- 根目录旧的 `longevity_v6|v7` **按作者决定保留**，不删。
- 历史 builder 未重跑，`governance/history_before.json` 未刷新。
- 增量中各审计依赖的一手来源，本轮只重核了 LoDoCo2 一处。
