# CLAIM LEDGER｜交叉验证与不确定项台账

**用途**：登记"本轮研究与写作中发现的冲突、待核项与跨来源不一致"。规则：不确定 → 先登记 → 交叉验证 → 裁决 → 修改来源文件并递增版本。**不得静默采用任何一方数字。**

**与旧债的关系**：D02–D10、M01/M06 等历史科学债在 `session/OWED_DEBTS.json` 保持原状态，本台账不复制其内容、不自动关闭；仅登记新 X-item 与其关联。

**状态图例**：`open`（待核）· `resolved`（已交叉验证并裁决）· `blocked`（需外部数据/作者）

## X-item 登记

| ID | 日期 | 事项 | 证据 | 不确定点 | 处置 | 状态 |
|---|---|---|---|---|---|---|
| X01 | 2026-11-27 | ER-100 获许可与给药时间线 | 公司 2026-01-28 [公告 IND 已获 FDA 许可](https://www.lifebiosciences.com/life-biosciences-announces-fda-clearance-of-ind-application-for-er-100-in-optic-neuropathies/)；2026-06-09 [公告首位已给药](https://www.lifebiosciences.com/life-biosciences-announces-first-patient-dosed-in-phase-1-trial-of-er-100-for-optic-neuropathies/) | 两者是公告日期，未核 FDA 有效日期与实际给药日；历史二手 06-08 说法不可靠 | 以公告日期和公司自报明确表述；FDA 原始确认、首例认证仍待查 | open（公告时间核实） |
| X02 | 2026-11-27 | RS5614 半决赛数据性质 | 公司自报 PDF：19 人、4 月、Horvath −3.4 年 / PC-Horvath −1.9 年 | 是否盲法/安慰剂对照；终点是否预注册；评审委员会是否已独立复核 | 引用时一律标注"公司自报、半决赛数据"；追踪 XPRIZE 官方发布 | open |
| X03 | 2026-11-27 | GLP-1 与时钟 | [RCT 探索性分析 n=84](https://www.nature.com/articles/s41467-026-72861-3)：−0.09；[SLIM LIVER n=41](https://www.nature.com/articles/s41514-026-00383-9)是单臂，DunedinPACE 中位变化 +0.018 | 先前将后者误写为“无组间减速”；两研究人群/设计不同，均不能证明延寿；AD 阴性结果仍待核 | 撤销组间表述；原文相关段已读；协议、数据和 AD 试验待核 | open（设计/指标局部核实） |
| X04 | 2026-11-27 | TRIIM "逆转 11/28 年" | 二手来源引用 Fahy 口径（naive CD8 +20%≈11 年、CD4 +13%≈28 年）；原始论文 12 月四钟平均 EA−A 相对基线约 −2.5 年；GrimAge 12/18 月为 −2.16/−2.12 年，18 月仅第一队列有血样（见 X10） | T 细胞计数→"逆转年数"换算口径未核实 | 仅引原始数字；换算句禁入正文 | open |
| X05 | 2026-11-27 | Buck TPE 钟数与人数版本口径 | [2024 预印本 v1](https://www.medrxiv.org/content/10.1101/2024.08.02.24310303v1.full) 报 35 钟；[2025 发表版](https://onlinelibrary.wiley.com/doi/10.1111/acel.70103) 图 2 报 36 钟，结果 §2 报 44 入组随机、42 完成 | 版本不同，不是同一版本计数冲突；效应量的分母与统计解释仍需独立复核 | 发表版引用 36；人数明确入组与完成；不视为疗效认证 | resolved（仅钟数和人数口径） |
| X06 | 2026-11-27 | 器官钟 UKB 样本量 | Nat Aging 正文 43,616（分析集）；一处二手报道 44,498（全集） | 两个口径都真实存在，引用需指明口径 | 以原文口径为准 | resolved（以 43,616 为准） |
| X07 | 2026-11-27 | 14 项共识清单的误传 | Grokipedia 等二手页把 VO2max/HbA1c 列入共识；原文共识为 IGF-1/GDF-15/hsCRP/IL-6/肌肉量/肌力/握力/TUG/步速/平衡/衰弱指数/认知/血压/DNAm 钟 | 无 | 已按原文裁决；作为"来源卫生"示例保留在台账 | resolved |
| X08 | 2026-11-27 | 器官钟纵向研究状态 | bioRxiv 预印本（2026-02，n=1,250） | 未同行评审 | 只作 Known Unknown（U3），不作定论 | open |
| X09 | 2026-11-27 | 旧债关联确认 | 本台账不复制 OWED_DEBTS.json 内容 | — | D03/D04/D08/D10 的推进在 THE-232；D05 在 THE-234 | resolved（机制确立） |
| X10 | 2026-11-27 | TRIIM 停药后各指标的持久性两说 | [Fahy 2019 原文](https://gwern.net/doc/longevity/epigenetics/2019-fahy.pdf) Table 1：GrimAge 的 EA−A 变化 12/18 月 −2.16/−2.12 年，Horvath −2.50/−0.94 年；[2026 综述](https://academic.oup.com/intimm/advance-article-pdf/doi/10.1093/intimm/dxag042/70632311/dxag042.pdf)概括诸参数回基线，ref 131 指向同一原研究而非 TRIIM-X | 原图 naive T 比例回近基线，与 GrimAge 保留可并存；综述总体表述与原文 GrimAge 结果冲突。18 月指标各自人数、胸腺 MRI 随访与更正待核；单臂不能确立因果 | [逐指标审读](SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)；只报告来源与期限，不能将时钟读数作寿命获益或已证长期持久 | open（原文及综述部分核实） |
| X11 | 2026-11-27 | 目的/意义与死亡率的再分析缩水 | UK Biobank 153,505 人 6 年：每 SD 意义 → 全因死亡 −15%；2026 汇总（~50 万人、32 年随访）：~24% → 校正健康习惯/抑郁后 9–15%；Sias & Turtle 2026：仔细测基线健康后大部分关联消失 | 观察性；反向因果（健康→有意义感）未排除 | 书第Ⅸ部意义章用双刃证据写法（15% 与 9–15% 同段给出）；不把目的写成"处方" | resolved（写法约束确立） |
| X12 | 2026-11-27 | 美国热适应研究证据等级 | SSRN 工作论文（3,135 县、25 年、三重差分）：老年人热脆弱性随空调普及**下降**，LIHEAP=气候适应政策 | 未同行评审 | 只作机制线索；欧洲部分（Nat Commun 2025 同行评审：89.4% 热死亡在 65+）可正常引用 | open |
| X13 | 2026-11-27 | D+Q MASH RCT 来源与缺失口径 | [原文 Results/Fig. 2 与敏感性分析](https://www.nature.com/articles/s42255-026-01643-4)：8/17 vs 1/14，复合终点含 MASH 未恶化；4 例缺失活检按未应答；不同缺失假设影响精度 | 原文相关段已读；注册、附录协议和源表未核、未复算；见 LON-C000004 | 改正 KERNEL/FRONTIERS，引用结果与不良事件/缺失分析并列 | open（主终点文本已核，协议/源表待核） |
| X14 | 2026-11-27 | 器官钟 43,616 误写成全部训练集 | [原文 Methods / Fig. 1](https://www.nature.com/articles/s43587-025-01016-8) | 分析集随机 7:3 训练/测试；r=0.98/0.93 为跨队列模型表现相关，不是个体内器官钟相关 | 已更正 KERNEL/FRONTIERS；引用和下游复核 | resolved（样本口径） |
| X15 | 2026-11-27 | 维护容量乘减式未定义 | KERNEL 旧 §2 | 各项变量、单位、相互作用、加减的物理意义均未给出；不能据此运算 | 撤回等号，保留为分项研究概念；形式化需新模型、量纲与反例 | open |
| X16 | 2026-11-27 | 读深图例与审计不一致 | FRONTIERS 图例 vs 审计 B/F5 | ◇ 被同时用作全文、摘要和二手，不能证明读深 | 历史标记降为不可用；逐项记录实际读取位置 | open |
| X17 | 2026-11-27 | 方案 A 章数和压缩方案自相矛盾 | MASTER §3、审计 C、书稿地图 | 实为 40 slot，旧审计称 36；C 一处压环境体验，另一处不压；无具体验证的 ≤36 地图 | 暂停认定最优方案；保持现有图作参考，独立审计前不得定稿 | open |
| X18 | 2026-11-27 | MASH 原文男性比例内部不一致 | [摘要](https://www.nature.com/articles/s42255-026-01643-4)称 76%；[基线表](https://www.nature.com/articles/s42255-026-01643-4/tables/1)为 13/17 和 9/14，合计 22/31≈71% | 可能是摘要或表口径/报告错误，未取得作者澄清 | 不能静默采用摘要总体比例；引用组别人数并联系作者或查勘误 | open |
| X19 | 2026-11-27 | LoDoCo2 TET2 安慰剂斜率区间正负号不一致 | [JACC 原文](https://www.jacc.org/doi/10.1016/j.jacc.2025.08.025)摘要下限 +0.16，Results 正文下限 −0.157 | 图、补充表与更正尚未核；两个版本不是独立验证 | 暂不引用该区间；核图表/作者并记录 | open |
| X20 | 2026-11-27 | CAPABLE 干预组年龄均值正文与表不一致 | [JAMA 原文 Results 与 Table 1](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2720136)：正文 75.7，表 76.1 | 口径或报告差异待核 | 暂不引用干预组均值；待核图表和更正 | open |
| X21 | 2026-11-27 | 健康预期寿命差 9.6 与 9.2 混同 | [原文 Results Fig.1/Fig.2](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2827753)：2019 全球差值 9.6 年；183 会员国差值均值 9.2 年 | 原文未在已读段落明确两个统计口径的权重来源，不能猜测 | 修正全球值/会员国均值；核 WHO 原始数据与权重；不将差值解释为个人必然疾病年数 | open（统计来源待核） |
| X22 | 2026-11-27 | p53 数值被误写成癌变风险 | [综述摘要](https://www.researchgate.net/publication/406907247_Cellular_Reprogramming_as_a_Strategy_for_Radical_Rejuvenation)称 27.8 倍是 p53 抑制与**体外全重编程效率**的汇总，不是肿瘤发生风险 | 原文页面元数据和 PDF 关联有异常，同行评审及计算质量未核 | 撤回全部将此数当癌变风险的说法，不将综述数值作安全证据；原始研究核查另行进行 | open（报告与证据真实性待核；误读已撤回） |
| X23 | 2026-11-27 | ER-100 的 2026-10 公司期中数据 | [公司公告](https://www.lifebiosciences.com/life-biosciences-announces-first-in-human-data-from-ongoing-phase-1-trial-evaluating-er-100-in-optic-neuropathies/)自报 3 人第 56 天安全、2 人视野信号 | 开放标签无对照；归因、长期安全与有效性不能确定；不作为独立验证 | 仅以公司自报表述，跟踪正式文章、注册结果及长期监测 | open |
| X24 | 2026-11-27 | HEAL-HOA 12 月失访及小效应 | [原文 Results](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2844641)：699/1151 失访，组间比例不等，UCLA 差约 0.7 分 | 混合模型与模式混合敏感性分析不自动排除所有 MNAR；中介因果需额外假设 | 引用效应、量表、失访、对照及限制并列；不承诺大规模成本效益 | open |
| X25 | 2026-11-27 | 司美格鲁肽小鼠寿命 vs 限食比较 | [Nature 2026](https://www.nature.com/articles/s41586-026-10940-7)寿命组为药物 vs 溶媒；另有 5 个月限食功能队列 | 非直接终生药物 vs 等摄入限食生存比较；仅雌鼠单品系 | 区分队列和终点，不将功能对照推成寿命机制裁决 | open |

| X26 | 2026-11-27 | Corley 等单核细胞 EpiTOC P/区间不一致 | [原文 Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC10776116/) 同一药物组内 EpiTOC P=.003，95% CI −0.003 至 +0.008 | 若两者对应同一参数与通常双侧检验则不一致；尺度、方法或笔误未核，其他指标不能代替核查 | 暂不以该 P 或 CI 作确定证据；核补充图、统计方法、作者更正和源数据 | open |
| X27 | 2026-11-27 | METFORAGING 使用 DunedinPACE 代码的实际版本 | [论文 Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC13098334/) 链到官方 GitHub；本轮固定快照 commit 4b569983543e51d1022aecec9a25e694bb3a336a，双接口字节一致 | 论文所用提交、权重、环境和具体批处理未核，本地代码观察不证明试验有偏差 | 记录 [manifest](source_snapshots/dunedinpace_4b569983/manifest.json)；申请运行版本与数据并验证 | open |


| X28 | 2026-11-27 | ILLUMINATE 主要复合结局的协议修订与批准 | [NEJM Study Design](https://www.nejm.org/doi/full/10.1056/NEJMoa0706628)称 2006-11-28 修订加入不稳定心绞痛住院，停试时尚未经 IRB 批准 | 原始协议、预先主要终点与敏感性分析尚未核，尚不能断定调整对结果的影响 | 摘录时同步披露修订与批准状态，核原协议及各结局 | open |
| X29 | 2026-11-27 | CALERIE 时钟与安全论文不同样本不能推断个体联合效应 | [DNAm 事后分析](https://www.nature.com/articles/s43587-022-00357-y)197；[安全报告](https://digitalcommons.wustl.edu/cgi/viewcontent.cgi?article=6013&context=open_access_pubs)218；220 原随机 | 参与者样本、时间点及缺失交集未取得；两个研究是同一试验 | 报告随机、分析人群及不同终点；仅取得可连接数据后评价个体联合画像 | open |
| X30 | 2026-11-27 | SPRINTT 多病潜类与干预效应异质性 | [2026 事后分析](https://www.nature.com/articles/s43587-026-01188-x) 包括潜类及部分池化亚组分析；报告交互 P=0.870 | 交互检验不支持已证实的亚组差异；潜类不确定性、多重比较、先验及外部验证尚未复核；结果段每人年事件单位待核 | 禁止由亚组显著与否直接断言效应差异；核模型、先验、单位与 protocol | open |

| X31 | 2026-11-27 | CALERIE 甲基化分析时点人数的集合边界冲突 | [Main 与 Fig. 1](https://www.nature.com/articles/s43587-022-00357-y/figures/1)：分析 128/69，12 月变化 125/66、24 月变化 117/68；Main 三时点 105/59。[补充表 S1](https://static-content.springer.com/esm/art%3A10.1038%2Fs43587-022-00357-y/MediaObjects/43587_2022_357_MOESM1_ESM.pdf)称 AL 12 月随访 65 | 在共同人群、个人唯一与共同筛选假设下，图注给出交集下界 114/65；换 S1 的 65 后为 114/64，均与 Main 不相容。随访数据与变化数据的定义、筛选可能不同；作者澄清、数据和模型未取得 | 不判哪个数字错误或效应方向；核数据字典、样本 QC 和作者解释；[本轮溯源与两种条件算术](CALERIE_TEMPORAL_AUDIT_2026-11-27.md) | open |

| X32 | 2026-11-27 | TranslAGE 的“从不分歧”被误写成逐钟从无方向冲突 | [原文 Fig. 4c 与方法](https://www.nature.com/articles/s41591-026-04562-9)：仅在某钟显著时与同研究其他显著钟比较；多数同向、少于半数同向和唯一显著分别分类 | 未读取/复算补充表确认每一逐钟比较及平手如何处理；多数规则下无“分歧类别”不等于所有配对方向一致；17.6%分母为该钟自身显著结果 | 修正 FRONTIERS F2 与 ANOM-003；后续逐条核源表，勿把响应性或组内变化当临床替代终点 | open（概念误写已更正，逐项数据未核） |
| X33 | 2026-11-27 | TranslAGE 描述性组内变化与随机生活方式荟萃分析的 estimand 不同 | [TranslAGE Methods](https://www.nature.com/articles/s41591-026-04562-9)描述配对前后检验和参考队列标准化；[Sanchez 2026 摘要](https://pubmed.ncbi.nlm.nih.gov/43038634/)为平均年龄≥45岁的生活方式 RCT 组间荟萃 | 试验重叠、每项估计/时钟与质量、荟萃模型和全文未核；不同人群、干预和尺度不能简单解释为互相否定 | 分开报告人群、设计、估计量与低确定性；取得全文/补充数据后核研究重叠与方法 | open |

| X34 | 2026-11-27 | MTO 青少年精神健康原论文撤稿并替换；PubMed 旧摘要与更正不一致 | [2016 撤稿替换公告](https://pmc.ncbi.nlm.nih.gov/articles/PMC6005353/)：女生重度抑郁结果 P=.06，而非原文 .04 | 旧摘要和新闻继续传播原结论；事后探索与多个终点均需注意，非成人健康分析的独立复制 | 不引旧显著结论；如引用此亚组须注明替换与探索性质，核更新论文与分析代码 | open（版本及主要更正已核，完整替换与方法未审） |

| X35 | 2026-11-27 | p16-3MR 报告/清除功能争议 | [Hori 2026](https://link.springer.com/article/10.1038/s44319-026-00802-8)报告其条件下弱信号与清除失败；[Wang 等回应](https://link.springer.com/article/10.1038/s44319-026-00801-9)强调场景、灵敏度与对照差异并反对全面否定 | 两方与独立研究的模型批次、剂量、分析和原数据未逐项复核；不能将此争议直接套用 Cell 2024 的不同交叉遗传系统 | 核同窝对照、底物背景、遗传型×药物交互、正交指标及独立复制 | open |

| X36 | 2026-11-27 | TranslAGE 多重检验与 90% 方差 PCA 阈值的依据 | [论文方法](https://www.nature.com/articles/s41591-026-04562-9)称经典 Bonferroni 假设独立、名义 .05 与有效检验数修正类似；[合成反例](MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)说明 90% PCA 维数不能一般性保证 FWER | 有效单检验 P 下 Bonferroni 不要求独立；补表20、每个结论实际阈值、原数据与代码未核；合成 FWER 不是论文的 FWER | 分清论文原话、数学性质与尚未复算；获取补表及数据逐项核检验家族和阈值，不断言全部结果无效 | open |

| X37 | 2026-11-27 | methylCIPHER 许可元数据不一致与 PoAm38 包装器待测 | [固定提交的 LICENSE](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/LICENSE)为 BSD 3-Clause，但 DESCRIPTION License 为占位；[PoAm38 源码](https://github.com/HigginsChenLab/methylCIPHER/blob/bfe5d02817e7dd5e923e8bf96528d5bfd52e1636/R/calcDunedinPoAm38.R)输入转置后缺失探针检查/填补方向存在待测疑点 | 尚无 R 运行、外部权重或试验版本对照；疑点不是已确认错误、也不证明影响任何论文 | 请维护者澄清许可证和依赖数据权利；用合成矩阵按固定依赖版本写回归测试，区分 PoAm38 与 DunedinPACE | open |

| X38 | 2026-11-27 | DO-HEALTH 时钟结果标准化差值换算成月数的公式待澄清 | [Fig.2 图注](https://www.nature.com/articles/s43587-024-00793-y/figures/2)和[扩展表3脚注](https://www.nature.com/articles/s43587-024-00793-y/tables/4)写 `(standardized estimate × SD + mean) × 12`；[方法](https://www.nature.com/articles/s43587-024-00793-y)称对变化量减均值并除 SD | 共同中心及尺度下组间差的逆变换均值项会相消；不确定脚注例子具体系数、变量与作者意图，未获得原数据/代码，不能判论文数值错误 | [条件性推导和复核清单](DO_HEALTH_UNIT_CONVERSION_AUDIT_2026-11-27.md)；请求作者澄清，不把时钟月数写成寿命获益 | open |

| X39 | 2026-11-27 | KERNEL I6 状态周转参数 m 被误写为迁移 | [原模型](../longevity_state_turnover/状态还在_不等于细胞没换.md) §4 定义 m 为成熟退出风险率、d 为其他丢失风险率，并明确不含迁移；[脚本](../longevity_state_turnover/identifiability_check.py)以 `maturation_hazard` 实现 | 原 KERNEL 的“迁移+死亡”与模型及 V7 不一致；其他丢失不必全为死亡；标签留存结论依赖理想脉冲、无新标记和常风险假设 | KERNEL 升 v0.9.5 修正术语与条件；受影响书稿及论文接口需人工复审，原计算和冻结数据不重签；同助手旧审计的公式符号通过不代表术语通过 | open（术语纠正，人工依赖复审及独立外审待完成） |

X33 后续：已读取 [Sanchez 综述全文方法、主要结果及偏离协议表](CLOCK_REVIEWS_ESTIMANDS_2026-11-27.md)，确认 CALERIE 因平均年龄 38 被排除；DO-HEALTH 合并的是运动因子、不能换成 omega-3 对比。补表及逐试验与 TranslAGE 重叠仍未核，综述提取和合并结果未复算；X33 保持 open。

X31 后续：作者[固定版本 Stata 脚本及筛选/模型](MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)已静态查阅，公开仓库无患者数据；导出脚本标示按 ID/时点排序且发布不含 ID，提示隐私风险而非授权按行配对。分母矛盾、真实模型与身份保护仍待核。

X30 后续：已对照 SPRINTT 原试验事件判定、安全与事后潜类交互；两报告同一试验、不算独立复制；事后交互 P=.870 不支持已证实亚组差异，亦不证明相同。详见[审计](MODEL_MULTIPLICITY_FUNCTION_AUDIT_2026-11-27.md)。

| X40 | 2026-11-27 | BASE-II 发表版预测比较的时间、选择与摘要差异 | [Vetter 2026](https://link.springer.com/article/10.1186/s40364-026-00909-z)：T0 1671/316、T1 1083/90，主单指标非统一时间或风险集；联合模型 T1 参与者、左截断，AICc 同数据选模 | 摘要列五项，正文 model 2 另列肌力（握力阈值派生）；model 3 肌力不显著；多重性、选择偏差与外部验证待核 | [审计](SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)；不把预测排序当干预替代终点；核补表、代码与外部验证 | open |
| X41 | 2026-11-27 | 多癌检测模型与随机试验的分母、版本和净收益 | [Malagón 发表版](https://pmc.ncbi.nlm.nih.gov/articles/PMC13740675/)的 1.1%/10.8% 是对应年龄段筛检癌中过诊断模型比例；[NHS-Galleri](https://pmc.ncbi.nlm.nih.gov/articles/PMC7619610/) 12 癌 III/IV 主要终点未达，IV 仅描述 | 发表/预印本同研究；模型不是试验数据；75–79 岁表与 50–75 岁筛查方案年龄口径待核；死亡与过诊断随访未完成 | [审计及合成反例](SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)；筛出癌分母不可改成所有受检者 | open |
| X42 | 2026-11-27 | 多癌微模拟发表版 Table 3 特定行统计待复核 | [Table 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC13740675/table/cam472455-tbl-0003/) 78,183 TP、73,810 FP、PPV 53.4%、NNS 108；分项中位数之比约 51.44% | 中位数之比通常不等于比值中位数；数值异常不单凭这一点判错，逐次配对数据/定义/代码和作者解释未核；Fig.2 图注 III 期灵敏度 50% 而表1基础情景为 60%，差异未裁决 | [V1 代码静态审读](MCED_CODE_AND_HOME_FALLS_AUDIT_2026-11-27.md)表明 PPV 从独立指标取边际汇总；数组无年度逐次配对信息。取最终发表脚本、年度逐次数据及作者定义再复算；人工反例不是原模型数据 | open |

## 交叉验证规则（本轮起生效）

1. 任何进入 KERNEL §3.2 的数字，至少一个来源须为一手（原文/官方 PDF）；二手来源只能提供线索。
2. 两来源冲突 → 登记 X-item → 读一手 → 裁决 → 在此留痕（不删除记录）。
3. 公司/竞赛自报数据（X02 类）永久带标注；不得以"已获奖"佐证科学结论。
4. 预印本（X08 类）永久带标注；升级为"已核"须有同行评审版本。
5. 台账与 KERNEL 冲突时：先修 KERNEL 并递增版本，再修改下游书稿/论文。

| X43 | 2026-11-27 | MCED 模型作表边际极值与逐次比值口径 | [Borealis V1 代码审计](MCED_CODE_AND_HOME_FALLS_AUDIT_2026-11-27.md)：表 2 比例极值使用过诊断边际极值/筛出癌中位数；表 3 不同列算法不同 | 最终发表脚本和年度逐次配对数组未核，发表表两年龄行与该算法相容不证明使用该版本；NNS min/max 代码命名亦需核 | 取最终版本和逐次数据复算；不把这些括号自动当逐次比例范围或 CI，不声称论文已错 | open |
| X44 | 2026-11-27 | HARP 首次跌倒与重复跌倒的结局和时零 | [原文和 2017 方案审读](MCED_CODE_AND_HOME_FALLS_AUDIT_2026-11-27.md)：主要 HR 0.90（0.66–1.27），次要事件率比 0.62；两组报告的时零不同，正文合计 140 vs 分组 141 | 非全随机人群的分析和干预前事件、删失处理待核；不知偏差方向；正文与表 2 的 CI 小幅不一 | 复核方案/登记及数据，不把事件率当无跌倒人数或主要终点成功；CAPABLE 为不同干预及结局 | open |
| X45 | 2026-11-27 | Cochrane 综述的引用重叠和摘要表格不一致 | [Cochrane](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/)含 HARP，摘要 vs 汇总表对质量生活研究数及骨折证据等级不同 | 文献检索截止在 HARP 结果发表前，纳入渠道及版本、表与摘要差异及勘误待核 | 不将单试验与其所在汇总算独立复制；核森林图、勘误和数据 | open |
| X46 | 2026-11-27 | Cochrane 高风险跌倒人数绝对风险算术和 HARP 附录分母冲突 | [汇总表](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/table/CD013258-tbl-0001/) 550/1000、RR .74，却列 461/1000；[HARP 表2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8408671/table/zoi210656t2/) 与[附录5](https://pmc.ncbi.nlm.nih.gov/articles/PMC9998238/table/CD013258-tblf-0004/)两组分母对调 | 550×.74=407；四舍五入不足以解释，但精确输入、计算口径、森林图所用数据及勘误未核 | [算术与分母审计](FALLS_STUDIES_DEEP_AUDIT_2026-11-27.md)；禁把条件算术称为汇总复算，核原数据和作者澄清 | open |
| X47 | 2026-11-27 | OTIS 敏感性段 IRR 与区间不一致 | [NIHR 结果](https://www.ncbi.nlm.nih.gov/books/NBK571976/)两处敏感性段写 0.17（0.99–1.38），主要估计为 1.17（0.99–1.38） | 表述疑似笔误但未核代码或勘误；不可把 0.17 当可靠效果或自行改写来源 | [方案、缺失和实施审计](FALLS_STUDIES_DEEP_AUDIT_2026-11-27.md)；查原分析与作者更正 | open |
| X48 | 2026-11-27 | 独立 MCED 生存者模型的输入文件命名及作者稿数值歧义 | [代码/论文审计](MCED_SURVIVOR_MODEL_REPRODUCIBILITY_2026-11-27.md)：README `BC_Incidence...` vs 代码 `BC_incidence...`；作者稿正文写 39–11，摘要/表 3 为 39–111（每 100,000 人年） | 仅静态阅读，缺原工作簿、R 环境、发表版确切提交和最终版核验；大小写敏感系统按说明原样放置可能失败，未实际运行 | 核作者、最终版本、输入数据及许可证；不把这一独立模型冒充 Malagón 模型或判论文计算错误 | open |

| X49 | 2026-11-27 | CALERIE 目标限食与实际时间分期被混用 | [骨密度报告](https://pmc.ncbi.nlm.nih.gov/articles/PMC4834845/)：目标 25%，前六个月 19.5±0.8%，后六个月 10.8±0.7%，再 12 个月 8.3±0.8%；[安全报告](https://digitalcommons.wustl.edu/cgi/viewcontent.cgi?article=6013&context=open_access_pubs)两年平均 11.9% | [2024 JCI 讨论](https://pmc.ncbi.nlm.nih.gov/articles/PMC11383369/)将 19.5% 写为随机分配两年；缺患者级暴露和报告间计算口径，不能推断单人依从性 | [剂量、骨密度及书稿接口审计](CALERIE_BONE_AND_EXPOSURE_AUDIT_2026-11-27.md)；区分目标、分期实际暴露、骨折与 BMD；核不同报告测量、缺失和后续长期事件 | open |

X38 后续：原文辨认 −0.16 为 PC PhenoAge、−0.32 为 GrimAge2，后者与全安慰剂比较而非其余因子主效应；扩展表 3 脚注同时写只乘 SD 和加均值两条规则。各钟均值、SD 与代码仍待核，详见[单位换算审计](DO_HEALTH_UNIT_CONVERSION_AUDIT_2026-11-27.md)。

| X50 | 2026-11-27 | CALERIE 停用随访、Legacy 登记与样本选择 | [Marlatt 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5366052/)单中心按依从性筛选，39 人参加、29 人两次随访完成；[Legacy 登记](https://clinicaltrials.gov/api/v2/studies/NCT05651620)为长期计划、截至 2026-06-09 更新未发布结果 | 两年随访不是全随机样本或重新随机的继续/停止比较；登记的全身骨矿物含量不是部位 BMD 或骨折；登记 42 与论文 39 口径待核 | [停用随访审计](CALERIE_POST_INTERVENTION_FOLLOWUP_AUDIT_2026-11-27.md)；核选择、缺失、登记更新与后续骨折数据 | open |
| X51 | 2026-11-27 | CALERIE 停用随访论文 FFM 恢复比例与表值 | [正文及表1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5366052/)称 FU24 恢复 27%，表列 M24 −2.7、FU24 +0.1 kg，按组均值及 0.1 kg 舍入条件推导约 101.8%–105.7% | 句子的分母、个体比例、样本及设备换算未明确；组均值比例不等于个体比例均值，不能判哪项错误 | [审计及算术测试](CALERIE_POST_INTERVENTION_FOLLOWUP_AUDIT_2026-11-27.md)；请求作者阐明计算和核勘误，勿将 27% 引为确定结论 | open |
| X52 | 2026-11-27 | DO-HEALTH 原试验主要终点、探索性癌症及钟分析重叠 | [癌症论文](https://www.frontiersin.org/journals/aging/articles/10.3389/fragi.2022.852643/full)三项 vs 全对照 4/264 vs 12/270，调整 HR .39（.18–.85），癌症为母试验预定探索性结局 | JAMA 六个主要终点未达预设显著性；癌症分析及 777 人钟子样本同一母试验、多比较，不能当独立复制或时钟中介已证；NNT 有时域和模型条件 | [临床与癌症审计](DO_HEALTH_CLINICAL_CANCER_AUDIT_2026-11-27.md)；核方案版本、风险集、未验证病例及独立复制 | open |
| X53 | 2026-11-27 | VITAL 与 DO-HEALTH 因子主效应、三项组合和癌症结局不可混作独立复制 | [比较审计](VITAL_DO_HEALTH_CANCER_COMPARISON_2026-11-27.md)：VITAL D 和鱼油总侵袭癌主效应 HR .96、1.03；其晚期癌复合二次分析 D HR .83 | VITAL 无随机家庭运动、不同年龄/配方；VITAL 主报告和二次分析同一试验；复合不是单独癌死亡，交互未显著不证实无交互 | 查相同三项组合的独立随机研究及预注册；系统综述、患者级复算未做 | open |
| X54 | 2026-11-27 | 混合读数及已知固定权重不能单独确定类型内部变化方向 | [P2 合成两类锐界](experiments/P2_TWO_TYPE_SHARP_BOUNDS_2026-11-27.md)：p=.5、y .6→.4 时类型1变化区间 [−1,+.6]；两端有构造见证 | 仅在精确、两类、线性、[0,1]、无跨时约束下成立；权重为有效测量权重，不是自动等于细胞比例，非时钟或真实人群估计 | 验证应用假设、误差、配对与外部同行评议，未进行真实数据检验 | open |
