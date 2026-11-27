# 共享断言层 / Shared claims layer

**当前为接入规范，无全稿完整人审声明。** 不把V6/V7的段落自动视为已验证断言。toolkit的toy是构造数据，不可迁入正文充当证据。

## 本目录四件套（2026-11-27 scaffold）

| 文件 | 角色 |
|---|---|
| [KERNEL.md](KERNEL.md) | 核心内核：不变式、定义、定量锚点、范式转换候选、estimand 骨架、禁写句、版本失效协议 |
| [MASTER.md](MASTER.md) | 总控：权威路径表、书稿架构三方案、论文处置四方案、里程碑、决策日志 |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | 交叉验证与不确定项台账（X-item） |
| [RESEARCH_FRONTIERS.md](RESEARCH_FRONTIERS.md) | 前沿扫描（第 1 期 2026-11-27）与 Known/Unknown Unknowns、候选转向 |
| [ANOMALY_LOG.csv](ANOMALY_LOG.csv) | 异常现象日志（Unknown unknowns 发现机制） |
| [claims/RESEARCH_CARDS_2026-11-27.md](claims/RESEARCH_CARDS_2026-11-27.md) | 四张定向主张卡试点；尚未绑定引擎或外审 |
| [DEEP_RESEARCH_RESTART_2026-11-27.md](DEEP_RESEARCH_RESTART_2026-11-27.md) | 研究重启：四方向案例、反例、三个论文边界、独立审阅条件 |

规则：**唯一编辑源是 `corpus/longevity_v6|v7`**；根级 `longevity_v6|v7` 为遗留副本禁止编辑。架构与论文处置待作者裁决（Linear THE-227/229），裁决前本目录文件为 v0.9 草案。

---

稳定ID建议 `LON-C000001`（断言）、`LON-E000001`（提取）、`LON-A000001`（来源/稿件快照）。ID永久不重用。来源去重记录版本/来源家族，独立来源不能仅按URL数量计算。

最小接收：明确对象/人群、干预或暴露、比较、结果、时间窗、estimand、效应尺度、不确定性、原始文件hash、精确片段、访问深度、主张kind、适用范围、竞争解释、债务、负责人。二进制表格/图像坐标需要扩展，本轮没有假装全部支持。

toolkit当前用schema作机械合同，不自动理解医学或规范伦理。多前提论证需拆分claims并显式记录依赖；当前实现对artifact→evidence→claim可传播，不宣称已经从全书自动抽出任意语义依赖。book/paper引用映射仍需人工接入。

共享层只维护证据判断；不同写作产物可采用不同叙事，但必须显式处理同一claim的版本。增加新来源后先失效旧判断，再由人重新判断；自动计算新hash不等重新审阅。

## 2026-11-27 深化与纠错

- [四方向穿透综合](DEPTH_SYNTHESIS_2026-11-27.md)；[工作证据卡 C000007–14](claims/ROUND_2026-11-27_DEPTH.md)。非系统综述、非独审、外源无字节快照。
- [交叉验证台账 X21–X25](CLAIM_LEDGER.md) 包含三项既有误读及两项新证据边界；D05 仍为正式合成 blocker。
- [STATE_DASHBOARD.HTML](../STATE_DASHBOARD.HTML) 为用户本轮单项授权的状态快照；小写副本同字节，不代表独立审计或实时 Linear 状态。

## 同日对抗研究增量

- [对抗研究与证据卡 C000015–20](RED_TEAM_RESEARCH_2026-11-27.md)：比较组内与组间、血压反例、克隆谱系、机构干预和时钟组成。
- [恢复后随机化测量合同草案](experiments/POST_RECOVERY_RANDOMIZATION_CONTRACT_DRAFT.md)：没有审批、样本量或具体方案。
- [确定版本代码快照及哈希清单](source_snapshots/dunedinpace_4b569983/manifest.json)：仅代码与许可证，非试验实际使用版本或研究源数据。

## 同日：决策层级与反例

[深研增量：从指标改善到可审计的净受益](RESEARCH_DECISION_LAYERS_2026-11-27.md)记录 ILLUMINATE、CAST、CALERIE 安全和 SPRINT 联合画像；附件为另项目状态页，仅作界面参考。X28–X30 保持 open。

## 同日续研：反例与人数边界

[四向续研：反例成对比较与分母一致性审查](COUNTEREXAMPLES_AND_DENOMINATORS_2026-11-27.md)包括 CETP 药物、D+Q 可行性、家庭环境反例及 CALERIE 报告人数的条件性集合冲突（X31）；[可运行边界计算](experiments/calerie_denominator_bounds.py)并非试验数据复算。

## 同日续研：替代终点、组织修复与长期结局

[定向审计与后续执行队列](LONGITUDINAL_SURROGATE_REPAIR_AUDIT_2026-11-27.md)：比较 TranslAGE 和生活方式 RCT 估计量，修正多数一致性误读（X32），核小鼠 p16 谱系、DPPOS 临床追踪、CAPABLE 5/12 月及 MTO 撤稿替换（X34）；[合成替代终点反例](experiments/surrogate_identifiability_demo.py)附测试，不是临床数据或验证。

## 同日续研：两篇时钟研究的估计量

[时钟研究比较与试验对比](CLOCK_REVIEWS_ESTIMANDS_2026-11-27.md)已读 Sanchez 生活方式 RCT 综述全文主要方法和结果：CALERIE 因平均年龄被排除，DO-HEALTH 汇总运动而非 omega-3；表格、原始试验和 TranslAGE 样本重叠未逐条复核。X33 保持 open。进一步[核查 DO-HEALTH 单位换算](DO_HEALTH_UNIT_CONVERSION_AUDIT_2026-11-27.md)：组间标准化差值的中心项是否抵消需作者解释（X38），不能把时钟月数当寿命收益。

## 同日续研：分析代码与多重检验

[模型、多重检验与功能试验专项审计](MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)：定位 CALERIE 作者固定版本 Stata 脚本及模型/筛选，识别公开无 ID 导出的隐私风险；X31 未解决、无患者数据复算。登记 X36：TranslAGE 论文 Bonferroni 独立性说法与 90% PCA 维数保障有数学边界，真实分析阈值待核；[可执行合成反例及测试](experiments/README_MULTIPLICITY.md)不是实际论文错误率。登记 X37：methylCIPHER 许可元数据冲突和 PoAm38 包装器待测疑点，不等于发现已确认错误。复核 SPRINTT 原试验及同一试验事后分析、判定规则与安全。

## 同日续研：时间尺度与来源条件

[CALERIE 时间尺度与分母复核](CALERIE_TEMPORAL_AUDIT_2026-11-27.md)：发表版补充表与图注 AL 12 月人数不同；两种条件算术均不闭合，X31 仍 open；端粒、EWAS 为同一试验不同测量，不是独立复制。发表版 Fig. 2 源表[离线审计脚本](experiments/calerie_fig2_audit.py)仅做合成数据测试，未取得原始字节或计算实际行数，不作模型复算。

## 同日续研：筛查、预测与停药后的尺度

[筛查、预测和持久性专项审计](SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)：NHS-Galleri 主要结局、加拿大 MCED 模型的筛出癌分母、BASE-II 跨时间预测和 TRIIM 原文逐指标；登记 X40–X42、修正 X10。配套合成反例及测试不是试验复算。[状态周转依赖与历史链接定位](../review/DEPENDENCIES_AND_LINKS_2026-11-27.md)限定复核范围；独立审阅与原始数据分析仍未完成。

## 同日续研：实际暴露、骨密度与因子对比

[CALERIE 骨密度和暴露审计](CALERIE_BONE_AND_EXPOSURE_AUDIT_2026-11-27.md)区分处方目标、分期实现与次要结局（X49），不把同一试验的时钟样本和骨样本当独立或个人联合数据；[DO-HEALTH 审计](DO_HEALTH_UNIT_CONVERSION_AUDIT_2026-11-27.md)补充钟、比较组及同一脚注两种换算规则（X38）。合成因子反例只展示估计量、不是实际 trial 数据。

## 同日续研：停用随访和临床终点

[CALERIE 停用与登记审计](CALERIE_POST_INTERVENTION_FOLLOWUP_AUDIT_2026-11-27.md)核实单中心两年后随访，登记随访选择及 FFM 表述疑点 X50–X51；[DO-HEALTH 临床与癌症审计](DO_HEALTH_CLINICAL_CANCER_AUDIT_2026-11-27.md)区分原主要终点、探索性癌症与同一试验的钟子样本 X52。算术与合成缺失反例附测试，不是患者级复算。

## PR #2 选择性整合

[固定版本审计与取舍](../review/PR2_AUDIT_AND_INTEGRATION_2026-11-27.md)：命名空间和章号不可直接合并；新增X71–X74、两个有条件的数学示例及 P3 评价合同。软件负向检查不验证科学真实性；其余未移植内容可按固定提交继续复审。

## 修复记忆：PR #2 后续审读

[时间窗与因果审计](RECOVERY_MEMORY_CAUSAL_AUDIT_2026-11-27.md)按一手图注及方法区分体外洗脱、诱导期干预和记忆形成期干预；[人工恢复资格反例](experiments/RECOVERY_ELIGIBILITY_COUNTEREXAMPLE_2026-11-27.md)及测试只说明选择问题，不是实际数据。X74–X76未关闭；第24章仍待独立审读。

## TPE 审计修订

[时间窗、分配与跨钟推断单位](TPE_TIMING_ALLOCATION_CLOCK_UNIT_AUDIT_2026-11-27.md)经原文和固定源码定向核读，重新开放 X05、登记 X77–X78；KERNEL 升至 v0.9.7，撤回未经证明的收益递减。两研究不是置换液随机对照。合成反例与测试不是试验复算，历史依赖需继续人工复审。

## CAPABLE 写作边界续核

[终点和资格审计](CAPABLE_OUTCOMES_ELIGIBILITY_AUDIT_2026-11-27.md)按PR2固定头线索核对2014设计文、当前登记及2019结果文；X79/X80未关闭。2025出院后研究只读摘要，不能做正式综合。

## HARP 方案与登记续核

[HARP续审](HARP_PROTOCOL_REGISTRY_FOLLOWUP_2026-11-27.md)以 PR2 固定来源为线索，核标记2014的方案、2021结果和当前登记；X44补充且X81/X82开放。首次事件、重复事件和不同分母不能互换；登记当前版本不证明历史修订，也未取得个体数据或独立审阅。

## FIND 跌倒与骨折续核

[FIND/VITAL 骨折与跌倒定向核读](FIND_FRACTURE_FALLS_VITAL_AUDIT_2026-11-27.md)区分同一母试验的多结局、骨折干预及延长随访与独立VITAL的不同剂量/结局；X83/X84为待澄清口径，未取得原始数据或独立审核，不是个人医疗建议。

## 克隆造血、取样与测序续核

[LoDoCo2/COLCOT比较](COLCOT_LODOCO2_SELECTION_AND_ASSAY_AUDIT_2026-11-27.md)区分母试验、随机后DNA样本、检出规则及临床终点；登记X85/X86，保留COLCOT仅核2024预印本v1的限定。人工选择例不估计真实偏差；KERNEL更新至v0.9.8，冻结V7不改。

[分选后比例的条件敏感性示例](experiments/PR2_SORTED_SAMPLE_SENSITIVITY_2026-11-27.md)择取 PR2 的精确算术与测试，补充uPAR分选后与总体的区别；假设的纳入比不代表真实回收率。

[CALERIE补表条件舍入与缺失续核](CALERIE_S3_ROUNDING_AND_MISSINGNESS_2026-11-27.md)引入PR2的精确分数算术：在指定舍入规则下57（29.8%）对应的整数分母候选为191，不能据此判定实际样本或完整记录人数。

[CANTOS TET2临床交互续审](CANTOS_CHIP_INTERACTION_AND_INDEPENDENCE_AUDIT_2026-11-27.md)区分亚组内检验、组间交互、三剂量合并与母试验单剂量，以及同试验不同报告；人工多重性例不是论文实际假阳性率。

[CALERIE脂质中介与公开评议续审](CALERIE_LIPID_MEDIATION_AND_PEER_REVIEW_2026-11-27.md)区分随机总效果、未随机中介和同试验报告，登记X88/X89并补充X60线索；[人工等价世界](experiments/randomized_mediator_equivalent_worlds.py)不是患者数据。

[HALE共享坐标与区间续审](HALE_SHARED_AXES_AND_INTERVALS_AUDIT_2026-11-27.md)根据PR2增量审计核图3A的均值/差值共享项及标称95%区间，人工例不拟合国家数据；X90/X91开放。

[DO-HEALTH 癌症时间编码续审](DO_HEALTH_CANCER_TIME_REFERENCE_AUDIT_2026-11-27.md)区分功能模型的最近访视编码和时钟变化模型中病例确诊天数、无癌赋零；X57/X58/X92待核，人工参数例不复算论文。
