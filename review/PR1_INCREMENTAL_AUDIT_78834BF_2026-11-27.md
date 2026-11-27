# PR #1 增量审计：78834bf

2026-11-27｜固定头 `78834bfce863ced1ba3cf31cb682a713f56974d0`；较上次 `c56c97bc91b254af48df9343f73af3aedb370d7e` 增加1个提交、13路径，主要为第21章空间可达性示范稿、证据审计、两个合成例及其测试。本文是同助手定向审计，不是独立外审，也不是全面系统搜索。PR审计期间可能继续变化，此结论仅限固定头。

## 发现和建议

1. **Fig 6F 的荧光术语需核并统一（P3，口径不明确，非断言数值错误）**：新增[来源审计第11行](https://github.com/Ginple/The_Measures_of_Longevity/blob/78834bfce863ced1ba3cf31cb682a713f56974d0/knowledge_base/SPATIAL_ACCESS_EVIDENCE_AUDIT_2026-11-27.md#L11)称“24h 珠子**总**荧光强度”；而[论文 Fig 6 图注](https://pmc.ncbi.nlm.nih.gov/articles/PMC8963880/figure/fig6/)引用 [Fig 5 C–E 图注](https://pmc.ncbi.nlm.nih.gov/articles/PMC8963880/figure/fig5/)，后者将追踪读数称 bead fluorescence 的 **mean fluorescence intensity (MFI)**，并对 24h 各生物重复给均值。建议将“总荧光”改为原文 MFI、明确起点归一化和 24h 值的具体统计定义；核原始方法及图表轴后再判断 24h 是时间点还是窗口平均。此处未访问原始图像或重新识别归一化单位；章节脚注已写“平均荧光”，与审计表不一致。仅凭图注未证明源表或结果数值有误，不能把荧光直接解作珠子质量百分比。
2. **之前负向测试发现仍适用**：新提交没修改快照 verifier 和独立 pilot validator。`c56c97b` 临时副本的优化模式 `assert` 被跳过、空 manifest 通过，以及独立 pilot 零测试通过，详见[负向审计报告](PR1_DEEP_INTEGRITY_AUDIT_C56C97B_2026-11-27.md)。根级验证器单独拒绝零测试，但没有涵盖快照校验；不能把根级软件测试通过当快照来源认证。上述是可复现工程风险，非证据证明当前快照受篡改。pilot 逻辑基线已有，非此 PR 新引入。
3. **来源边界仍需外部审读**：论文 [Fig 6 补图2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8963880/figure/fig6/)确为一次代表实验的3个技术重复，不能视作3只独立动物；[Fig 8D](https://pmc.ncbi.nlm.nih.gov/articles/PMC8963880/figure/fig8/)每基因型3鼠，图注称非内化 TUNEL 阳性细胞。新增章节将其保留为染色分类下的组织线索，而非清除速率证明，方向谨慎。仍待独立核原始图像、分类/投影、输入和区域分母、6F 的跨组配对；[Wu 方法协议](https://pmc.ncbi.nlm.nih.gov/articles/PMC11338188/)确采用酸敏感与酸不敏感双标签、测吞入及酸化，不能据此推断终末降解。

## 隔离核验与未决

- 在固定头的 `git archive` 临时副本用 Python 3.11.2、networkx 3.6.1、jsonschema 4.26.0、beautifulsoup4 4.15.0 运行 `scripts/run_validation.py`：project **85**、experiments **81**、pilot **21**；双种子/搬迁套件数量与三个 CLI 输出一致，29条历史断链、0新增；返回 `all_software_checks_passed=true`。这是兼容依赖而不是 `requirements-tested.txt` 的精确锁定环境；既有 networkx 3.7 要求 Python ≥3.12，当前3.11无法安装该锁。它也不替代科学审稿或远程 CI。
- 两个人工模型的单位、守恒及约束已经由对应新增测试核算：库存例假设恒定输入、恒定退出风险和稳态；时空例有源端排队、不得中间缓存、接触与处理同时发生。小整数穷举仅覆盖规定模型；两者不拟合生物数据，不证明机制。
- 比较相对基线的137个变化路径：本地22相同、31不同、84缺失，另有 `STATE_DASHBOARD.HTML` / `STATE_DASHBOARD.html` 大小写冲突。明细见[快照比较](PR1_SNAPSHOT_78834BF_COMPARISON_2026-11-27.json)；计数取于本轮本地修复后的工作树，不能与历史计数机械比较。不要整树合并或覆盖本地不同编号及版本。
- Actions jobs `140660886401`、`140660854460` 的注释均称付款失败或额度需增加，**未启动**；GitHub 状态 `UNSTABLE`。本地通过不是远程 CI 已通过。`git diff --check c56c97b 78834bf` 通过。
- 第21章是示范稿且自审不构成独立外审；人类临床外推、证据权利与原始图像未全面核实。未更改仪表盘、未合并或推送。
