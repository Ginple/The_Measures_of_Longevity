# 实际分析代码、统计阈值与功能试验：继续审计

记录日期 2026-11-27。**范围**：静态源码阅读、论文方法对照、可运行合成数学反例；不是独立外审、系统综述、患者级复算或临床建议。链接至固定版本，原始受限数据未下载；数值依赖论文报告，未经独立重算。

## 1. CALERIE：找到作者原分析脚本，但分母冲突尚未解决（X31）

[作者分析仓库](https://github.com/danbelsky/CALERIE_ClocksAnalysis/tree/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c) README 称脚本用于 Waziry、Ryan 等研究。固定 commit `db56e58a7546934f3d9f2c5764cc8ddaa5894a9c`（2022-12-12）；完整 tree 仅脚本与 README，GitHub API 未识别仓库许可证，license endpoint 404。**无许可不意味着可随意再分发**：只记录固定链接、行号与哈希，不把第三方文件复制进项目。由 contents 与 git blobs 两个 GitHub API 端点取得字节并相互比较，重算 git blob；均是同一托管源，并非独立科学验证。

| 文件 / 固定链接 | bytes | Git blob SHA-1 | SHA-256 |
|---|---:|---|---|
| [CALERIEClockData.do](https://github.com/danbelsky/CALERIE_ClocksAnalysis/blob/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c/CALERIEClockData.do) | 8,883 | `474e52176d776758489f8645cc3d69a29f949268` | `1c16321fa91a612b037498cace3c1eb7055ed8974776fdef9b3ca88e0e546028` |
| [CALERIEClockAnalysis.do](https://github.com/danbelsky/CALERIE_ClocksAnalysis/blob/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c/CALERIEClockAnalysis.do) | 39,789 | `8d3afdc069e0e007e0462e04126f1cf3c623f66a` | `1bb03f7c1f3d03c6dfa2cb759c8fae5b63c73cb38a2bb163db339f2aaa19c44a` |
| [CALERIE_NatAging_DNAmData.do](https://github.com/danbelsky/CALERIE_ClocksAnalysis/blob/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c/CALERIE_NatAging_DNAmData.do) | 5,164 | `b9048155411abd39e1e7c00f813bc02edc6e779b` | `045635cefd052043788d4e9d275b3a620a4bdb26646a439b46540053a3b2e082` |
| [CALERIE_NatAging_PhenoData.do](https://github.com/danbelsky/CALERIE_ClocksAnalysis/blob/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c/CALERIE_NatAging_PhenoData.do) | 6,041 | `aea6b30c941a9c298e4b78ecb9802464a95e2fb7` | `169ad52d2ef5592fc016c6f248bb8f2de586cfc635a5175e2f3fa6a105518f84` |
| [TreatmentEffectFigures.do](https://github.com/danbelsky/CALERIE_ClocksAnalysis/blob/db56e58a7546934f3d9f2c5764cc8ddaa5894a9c/TreatmentEffectFigures.do) | 2,817 | `c9603451d4ffa15cdeafd31e7b872fb4e171082e` | `5fe6b321c0d3f120df26ea02b00cb25111e41e2436a6afb65ac1798199131cc0` |

### 代码路径与可验证边界

- DNAmData lines 10–24、31–50、65–80 从本地路径读取技术 PC、外部算好的 clock / PC clock / `CALERIE_PoAm45.txt`，再按 barcode 或 sample_name 合并；91 行删除两份指定重复基线样本。虽然代码注明 DunedinPACE，历史文件和变量名含 PoAm45，**名字本身不能证明版本或公式是否正确**。数据和计算环境不在仓库；需原模型提交、权重与对应输入核对。
- ClockData lines 8–26 按去标识号与随访合并后，以 `dnamage` 为条件：同人数据行非缺失计数恰为 2 或 3、且基线非缺失，才标记 asample。与特定钟的非缺失、批处理 PC、协变量以及模型使用行并不必然相同；后续模型样本需按各变量实际检查。Lines 43–47 以技术 PCs 拟合随机效应模型并取 `ue` 加截距作为批次校正结果；56–58 行从个人基线构建变化；74–101 行区分年龄钟的年龄差及 PACE 缩放。
- ClockData lines 185–200 是脚本注释记录的 197、128/69、125/66、117/68，**不是实际执行日志**；注释没有给出三时点交集 105/59。它支持前述表述存在于脚本，但无法自行解决条件集合冲突或判哪一数错误。原文与图表冲突及两组算术见 [CALERIE 时间审计](CALERIE_TEMPORAL_AUDIT_2026-11-27.md)。
- ClockAnalysis lines 30–38 明确先按 `deidnum fu` 排序，同时分别导出“with ID - for graphing”和“No ID - for posting to journal”。这揭示**潜在隐私/重新链接风险**，不是可授权推断：无法保证发表 CSV 与代码导出完全一致、行序未改、行和缺失机制可唯一识别，且不能据此尝试重建身份或个人配对。请数据控制者评估公开数据风险；获得授权的真实链接键与访问权限是复算前提。
- Analysis lines 486–496：对标准化变化拟合 `mixed`，含 `fu##CR`、基线值、site、race、BMI 分层、性别及年龄；随机截距及 fu 随机斜率、非结构化协方差与 robust 方差，`margins, dydx(CR) over(fu)`。Figure 脚本 lines 12–19 用未经标准化的变化模型和各组随访 margins，**不是将组内显著与否相减**。脚本称 ITT，但只对有相应资料者拟合；随机后缺失的选择、假设和个体级受限数据仍须核查。
- PhenoData lines 35–40 对 visit 1/11/13 编码，92–114 对某些年龄计算偏差采用人工规则；分析使用的精确协变量及修正规则必须纳入可复算合同。当前未安装 Stata、无对应原始数据、无日志，不能声称效应、人数、预测公式或任何错误已被复算。发表源 CSV 网页可部分解析，但未获取原始字节，不能给出 hash 或完整行数。

### 可复算所需

作者或合规机构提供版本化代码、Stata/依赖包与随机种子/日志、原始输入和标识-随访链接、时钟权重与日期、各阶段筛选表、缺失和批次校正；在获许可环境逐步比对 `asample` 与每钟每时点模型的 e(sample)、交集及效应。数据含受限信息，不应提交本仓库。优先请作者解释 Main、Fig.1、补表人数不闭合与 Fig.2 表的发布/排序流程。

## 2. TranslAGE：多重检验论文表述与数学边界（X36）

[发表版方法](https://www.nature.com/articles/s41591-026-04562-9) 逐字含义：称经典 Bonferroni 假设检验独立；对钟与干预的相关矩阵分别 PCA，定义解释 90% 总方差所需 PC 数为有效检验数；称名义 P<0.05 与基于该数的 Bonferroni 式校正“effectively similar”；又称每个分析的有效数和对应阈值列于[补表20](https://static-content.springer.com/esm/art%3A10.1038%2Fs41591-026-04562-9/MediaObjects/41591_2026_4562_MOESM23_ESM.xlsx)。配对 t 检验段也写名义 P<0.05。**本文尚未取得补表原始文件或代码/相关矩阵，不能断言每一结果最终用哪个阈值。**

数学上，若每个真实零假设的单检验 P 值有效，Bonferroni 把每项阈值设为 α/m，联合界给出 FWER ≤ α，**不要求独立**；依赖可以使之保守。若有效数 k>1，数值上名义 .05 不等于 .05/k。高相关可使家族错误率接近单个测试，但是否近似不能只凭 PCA 维数名称保证。90% 方差主成分个数本身不是对所选假设家族在目标 α 下 FWER 控制的证明。各项 P 值本身有效、家族如何定义、依赖结构、数据驱动选钟等也均重要。

### 可执行合成反例（非论文复算）

运行 `python knowledge_base/experiments/multiplicity_pca_counterexample.py`；其 16 个双侧正态检验均为真零，等相关 ρ，精确本征值，条件独立积分用 Simpson 法，非真实试验数据：

| ρ | 90% 方差 PC 数 k | 未调整 .05 的 FWER | .05/k 的 FWER | 标准 Bonferroni .05/16 的 FWER |
|---:|---:|---:|---:|---:|
| 0 | 15 | 0.559873 | 0.052021 | 0.048845 |
| 0.9 | 1 | 0.146164 | 0.146164 | 0.013010 |

这是明确反例：哪怕相关很高，k=1 和名义 .05 仍可能使 16 项家族的至少一次假阳性概率约 14.6%；各项阈值按 k 而非 m 并无一般性保障。积分末尾截断和收敛由脚本与测试记录。**不能用此合成数值推断 TranslAGE 实际 FWER 或判定其全部发现无效**；应取得补表20，标记每个结论的检验家族、原始/调整 P、k、阈值与数据、方法预先规定；对确切相关与检验分布开展仿真或适当重抽样，并向作者请求代码及解释。PCA 的不相关主成分也不自动等同原始检验的独立个数。

此外配对组内变化与随机对照组间效应是不同 estimand；年龄残差化及 HRS 标准化均不能单独排除时间趋势、疾病恢复或其他混杂。详见 [X33 与既有定向审计](LONGITUDINAL_SURROGATE_REPAIR_AUDIT_2026-11-27.md)。

## 3. SPRINTT：同一 RCT 原报告与事后分析不可计作复制（X30）

[2022 原试验](https://pmc.ncbi.nlm.nih.gov/articles/PMC9092831/)随机 1,519，主要预设 SPPB 3–7 组 1,205（多组分 605、健康教育 600）。年≥70、低肌量、基线能独立完成 400 m；多组分包括身体活动、营养及技术/行为支持，健康教育也有活动，无法从总效应识别各组成贡献。主要复合事件 283/605 vs 316/600，HR 0.78（95% CI 0.67–0.92）；含首次行动障碍或死亡，首次事件为死亡各 6、7 人，剔除死亡 HR 0.79（0.67–0.93）。不是全因死亡的治疗效应。持续行动障碍 127/605 vs 150/600，HR 0.79（0.62–1.01）；不得把主结果延伸成该次要终点已明确有效。

判定不只直接 400 米失败：未完成测试可由步速、辅助器具、病历、自报/代理报告及独立委员会判定；原文还把不能尝试、未尝试且无法判定者计为事件，另列末次成功、长间隔及无基线后测试等删失规则。风险集与这些规则影响估计，不等于所有事件均是直接测得的不可行走。

安全：至少一次不良事件 337/605 vs 297/600，RR 1.13（1.01–1.25）；严重不良事件 237/605 vs 216/600，RR 1.09（0.94–1.26）；跌倒 80/605 vs 49/600，RR 1.62（1.16–2.27）；全随访死亡 31/605 vs 25/600，RR 1.23（0.74–2.06），不同于主终点中以死亡为首次事件的人数。两组接触和报告机会不同；严重事件及死亡 CI 包含增害与无差异，**不能证明等安全，也不能把所有事件归因干预**。受试者大多白人或种族信息缺失，且重要认知障碍被排除，不能推广至全部老人。探索 SPPB 8–9 组 HR 1.25（0.79–1.95）；精度有限，不能凭本组不显著与主组显著作组间效应差异结论。

[2026 事后报告](https://www.nature.com/articles/s43587-026-01188-x)是同一试验的 1,199 人分析（601/598），依多病潜类分类；总体 HR 0.78（0.66–0.92），交互 P=.870。潜类硬分类、组内权重与贝叶斯部分池化有额外假设；不同组置信/可信区间、绝对效应数值和显著性应完整列示，不以“某组显著”证明效应修饰，更不把小组不显著当无效。原文讨论提出模式“显著修饰”的措辞比其交互检验结果支持的结论强；P=.870 也不等于证明各组完全相同。模拟功效依观察到的结构与效应，属于情境分析，不是事后验证。原文“178 events per person-year”等单位可疑，暂不引用数值，核源表/作者后再定。原报告和本事后报告**不是两项独立复制**。

## 4. methylCIPHER 静态代码及发布许可核对（新增 X37）

[固定提交树](https://github.com/HigginsChenLab/methylCIPHER/tree/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636) 的 [LICENSE](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/LICENSE) 文本声明 BSD 3-Clause；但 [DESCRIPTION](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/DESCRIPTION) 的 License 字段仍为 `What license is it under?`，GitHub API 标识为 `NOASSERTION`。这些元数据和许可证文本不一致，应请维护者明确具体文件及外部数据包、依赖、权重的适用条件；不是法律结论。

- [PC 时钟实现](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/R/calcPCClocks.R)从外部 `PCClocks_data.qs2` 读取填补参照、center、rotation、model 与 intercept；PCPhenoAge 使用中心化矩阵乘旋转和模型再加截距，PCGrimAge 还经中间代理变量、年龄和性别。这个静态公式不能独立确认系数来源、数据哈希或与 2023 CALERIE 所用版本等价；文件完整性检查的 hash 代码被注释，不能当作执行时校验。
- [PoAm38 包装器](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/R/calcDunedinPoAm38.R) 引用的是 `DunedinPoAm38::PoAmProjector`，**不能当 DunedinPACE**。静态看其声明输入样本为行、CpG 为列，转置后完整性检查却看 `colnames(newBeta)`；缺 CpG 插补分支将所构造的缺失 CpG 行矩阵用 `cbind` 拼接，方向也值得核查。仅是代码审阅的待测疑点，未在 R 执行，不能断言实际失败、量化影响或影响论文结果。测试应使用人工数据、验证行列名与矩阵尺寸、参照官方实现并核依赖版本。
- [原始 PhenoAge 函数](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/R/calcPhenoAge.R)允许不插补时跳过缺失列，且某分支 `rowSums(..., na.rm=T)` 跳过细胞内缺失值；应单独核样本、CpG 和平台 QC，不能仅因输出有数字就认定可比。非 PC PhenoAge 不等于 PCPhenoAge。
- 未安装 R 或访问所需外部权重，未做公式逐项比对或运行，因此这些只是有固定链接的静态观察，不是错误确认及不等价证明。

## 下一步，不视为结题

1. 按受控路径申请 CALERIE participant–visit 键、原数据与运行日志；先核 X31 并建立逐步排除表，不从公开无 ID 行序推断个人。
2. 获取 TranslAGE 补表20、实际代码和输入，逐项核分析家族、阈值、P 值及比较组；模拟实际依赖前不得推定论文 FWER。
3. 核 methylCIPHER 的具体时钟公式及版本：2026-09-16 commit `bfe5d02817e7dd5e923e8bf96528d5bfd52e1636` 的 LICENSE 正文为 BSD 3-Clause，但 GitHub 元数据标 `NOASSERTION`；README 明说部分未公开算法是估计，且安装示例指向旧组织。论文排除 OMICmAge、DNAmEMRAge 的开源计算路径。此许可证只对仓库对应内容及其声明有效，不自动授予外部依赖/权重的许可；尚未运行 R 或对照试验所用版本。
4. SPRINTT 核事后模型先验、概率分类敏感性、附录有效样本及事件率单位；对每个绝对结局关注时间与删失假设。
