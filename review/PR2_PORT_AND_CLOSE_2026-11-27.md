# PR #2 选择性移植与关闭记录

2026-11-27｜依据用户在本会话中的明确选择“选择性移植后关闭 PR #2”。来源为 [PR #2](https://github.com/Ginple/The_Measures_of_Longevity/pull/2) 固定头 `b8434e22ec62ba21814546560a33fc38f4939e9f`；目标为本分支 `arena/1883e654-the-measures-of-longevity`（PR #1 谱系）。早先的部分整合见 [PR2_AUDIT_AND_INTEGRATION](PR2_AUDIT_AND_INTEGRATION_2026-11-27.md)。本记录是同一助手的工程处置，**不是**对移植内容的科学复核或独立外审。

## 1｜规则

- **只移植 PR #2 新增、而本分支没有的文件**。PR #2 对共同文件的修改不移植，因为两条谱系对同一文件的改法冲突。
- **命名空间隔离**：PR #2 的 X 编号、章号与本分支同号不同义（例如 PR2-X32 是成熟退出，本分支 X32 是 TranslAGE）。每个移植的 Markdown 文件顶部都有横幅，说明文中编号属 PR #2 命名空间、未经本分支复核、不得作为正文或 KERNEL 证据。
- **链接处理**：指向本分支已有文件或同批移植文件的链接，改写为新的相对路径；其余链接改写为固定提交 `b8434e2` 的 GitHub 永久链接。移植后 0 条新增断链。
- **测试**：只移植能在本分支当前代码上原样通过的测试。

## 2｜已移植（76 个文件，即 PR #2 新增的 80 个文件减去下表 4 个）

| 类别 | 数量 | 位置 |
|---|---:|---|
| 合成实验代码与预注册模板 | 10 | `knowledge_base/experiments/`（新模块，与已有模块不重名） |
| 项目测试 | 11 | `tests/`：assurance_fixture_comparison、clock_unit_counterexample、compare_pr_snapshot、familywise_illustration、inversion_weight_calibration、mixture_decomposition、post_randomization_selection_demo、rounded_percentage_denominators、shared_type2_bounds、sorted_sample_sensitivity、survivor_selection_demo |
| 快照比较工具 | 1 | `scripts/compare_pr_snapshot.py` |
| 定向审计（PR #2 命名空间） | 14 | [knowledge_base/imported_pr2/](../knowledge_base/imported_pr2/README.md) |
| 论文笔记与各论文 KERNEL 候选 | 8 | `papers/P1…P3/`；PR #2 的 `KERNEL.md` 改名为 `KERNEL_PR2_CANDIDATE.md`，避免与唯一权威的 `knowledge_base/KERNEL.md` 冲突 |
| 书稿候选与段落对照 | 10 | [books/pr2_candidates/](../books/pr2_candidates/README.md)，不进入 `books/manuscript/`，避免同题重复稿 |
| 对 PR #1 早期提交的审计与快照比较 | 22 | `review/pr2_archive/`（历史存档） |

移植后根验证：项目测试 134 项（原 106 项＋本次移植 28 项）、实验 103 项、pilot 21 项，全部通过；0 条新增断链 / 29 条历史断链；无 HTML；无大小写碰撞。

## 3｜未移植及原因

| 内容 | 原因 |
|---|---|
| `tests/test_calerie_bounds.py`、`tests/test_time_origin_counterexample.py` | 依赖 PR #2 改过的 `calerie_denominator_bounds.py` / `time_origin_counterexample.py` 接口；本分支已有自己的模块与测试，导入 PR #2 版会覆盖已审计代码 |
| `tests/test_validation_fail_closed.py` | 针对 PR #2 的根验证器（`project_files`、`require_checks`），本分支的验证器结构不同 |
| PR #2 对 45 个共同文件的修改（台账、KERNEL、MASTER、FRONTIERS、实验模块、协议、CI 等） | 与 PR #1 谱系冲突；台账编号同号不同义。值得采用的结论此前已经逐条改写进本分支（X71–X74、X77–X80 等） |
| PR #2 对六个冻结研究模块与根级 `longevity_v6|v7/README.md` 的修改 | 冻结证据不改；根级遗留副本等 DEC-005 裁决 |
| PR #2 删除的 110 个文件、7 个测试改名 | 本分支保留现有布局 |
| `review/legacy_broken_links.json` | 本分支用 `governance/legacy_broken_links.json` |

## 4｜关闭

移植提交推送后，在 PR #2 留言说明，并以 `gh pr close 2` 关闭（不删除分支）。PR #2 的分支 `arena/61c999d8-the-measures-of-longevity` 与固定头保持可查，任何未移植的内容日后都能从那里取回。
