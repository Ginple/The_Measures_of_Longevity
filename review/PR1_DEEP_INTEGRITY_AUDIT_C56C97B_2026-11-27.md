# PR #1 深入审计：来源快照和零测试（固定 c56c97b）

2026-11-27｜本负向审计针对固定头 `c56c97bc91b254af48df9343f73af3aedb370d7e`；审计期间 PR 前进至 `78834bfce863ced1ba3cf31cb682a713f56974d0`，两个涉及的验证脚本在此增量中未变。新头的新增内容与隔离软件检查见[补充增量报告](PR1_INCREMENTAL_AUDIT_78834BF_2026-11-27.md)。这是同助手审计，不是独立外审。[上轮增量报告](PR1_INCREMENTAL_AUDIT_C56C97B_2026-11-27.md)仍有效。下述破坏操作仅在临时副本，未修改 PR 原分支或本地源数据、原始 manifest。

## P2｜快照校验在优化模式跳过校验，空清单也返回成功（PR 新增）

[`knowledge_base/source_snapshots/verify_snapshots.py` 第9–16行](https://github.com/Ginple/The_Measures_of_Longevity/blob/c56c97bc91b254af48df9343f73af3aedb370d7e/knowledge_base/source_snapshots/verify_snapshots.py#L9-L16)将长度、SHA-256 和 Git blob SHA-1 检查全部放在 `assert`；优化模式会移除这些检查，但仍打印全部 `OK`。此外没有要求 records 非空或涵盖应核文件，`records=[]` 正常模式即退出0、没有检查任何文件。该 verifier 属本 PR 新增。

**可复现**：使用干净 `git archive` 副本，翻转 `PACEProjector.R` 的首字节且不改变长度，不动清单。普通 `python verify_snapshots.py` 返回1；`python -O verify_snapshots.py` 返回0、两行均报告长度与两个摘要 OK。另在副本令清单 `records=[]`，普通运行返回0、无输出。这里仅模拟单字节损坏及清单缺项，未证明实际快照被更改。

根验证器没有调用这个**单独的**快照校验器：在同一被篡改的临时 PR 副本，`scripts/run_validation.py` 仍返回0、`all_software_checks_passed=true`（85/73/21）。其当前说明限定为软件合同、不是科学或来源真实性认证；不应把此返回值理解为已核来源快照。建议明确报告 provenance check 未运行或将其作为显式门槛；替换 `assert` 为不可优化掉的失败分支，要求清单非空、明确预期条目/唯一性，验证文件约束，添加普通/`-O`、等长损坏和空/缺项负向测试。清单本身也是本地文件，哈希匹配仅证明和清单一致，不是独立签名、原始研究实际使用版本或科学真实性证明。

## P2｜独立 pilot 校验在运行零测试时仍返回通过（基线已有）

[`pilot .../scripts/validate.py` 第7–9行](https://github.com/Ginple/The_Measures_of_Longevity/blob/c56c97bc91b254af48df9343f73af3aedb370d7e/knowledge_base/pilots/real_claims_001/scripts/validate.py#L7-L9)只判 `wasSuccessful()` 和无 skip；`unittest` 零测试也算成功。该逻辑在基线 `6be77be` 已有；PR修改了同一验证脚本的搬迁和只读输出，但未引入这个条件。

在临时 PR 副本仅删除 pilot `tests/test*.py`：`validate.py --unit-only` 退出0、`test_functions: 0, passed: true`；完整 `validate.py` 也退出0、原位置与搬迁均0测试且 `portable_software_checks_passed: true`。**根级** `scripts/run_validation.py` 对三个测试套件另有零测试检查；以同一副本执行实际返回1，报告 `pilot suite did not run tests`。因此不能将 standalone 的缺陷错误地说成根级 CI 对零测试也通过。建议独立 pilot 的 `passed` 加 `testsRun > 0`，同时测试普通、优化模式及完整版；除零之外，少量意外漏发现仍需明确测试清单/最低覆盖策略，不能靠“>0”解决。

## 当前工作分支的有限修复（不在 PR 中）

- 本地 `knowledge_base/source_snapshots/verify_snapshots.py` 改为显式失败分支，要求固定快照的两条唯一路径、相符长度和双哈希，拒绝空/缺项及根外路径，不变更文件或 manifest。固定条目变更应经审查后同步更新检查；这仍不是独立来源验证。
- 本地 `knowledge_base/pilots/real_claims_001/scripts/validate.py` 的 `units()` 加 `testsRun > 0`；保留既有本地搬迁及只读输出修改。
- 增加 `tests/test_snapshot_verifier_fail_closed.py`（4项：原件、同长度损坏、空/缺/重复、缺文件，含正常及 `-O`）与 `tests/test_pilot_empty_suite_fail_closed.py`（2项：真实非空、移除测试后普通/优化/完整版退出失败）。首次运行 pilot 新测试因临时副本的组件导入路径未配置而失败，后改为**指向临时副本自身**的 `PYTHONPATH` 并重跑通过；不隐藏此调整。

本地独立临时副本执行主验证器：164项通过，CLI双种子/搬迁一致，输入与schema一致，22条历史断链、0新增；pilot 21项通过；本地原始快照 `python -O` 校验通过。软件检查不代表科学可靠性、外部审稿或发布许可。本次未重跑上次账单/额度阻塞的远程任务，也未动仪表盘。
