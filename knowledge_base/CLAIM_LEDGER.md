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
| X04 | 2026-11-27 | TRIIM "逆转 11/28 年" | 二手来源引用 Fahy 口径（naive CD8 +20%≈11 年、CD4 +13%≈28 年）；原始论文只报 GrimAge −2.5 年、持续 6 月 | T 细胞计数→"逆转年数"换算口径未核实 | 仅引原始数字；换算句禁入正文 | open |
| X05 | 2026-11-27 | Buck TPE 钟数与人数版本口径 | [2024 预印本 v1](https://www.medrxiv.org/content/10.1101/2024.08.02.24310303v1.full) 报 35 钟；[2025 发表版](https://onlinelibrary.wiley.com/doi/10.1111/acel.70103) 图 2 报 36 钟，结果 §2 报 44 入组随机、42 完成 | 发表版结果与图注写 36，但同一发表版引言和 §4.6 写 35，故原先“仅版本不同”表述撤回；注册及分配另有待核口径 | 见 [后续核读](TPE_ALLOCATIONS_AND_CLOCK_UNITS_2026-11-27.md)，保留版本/段落差异并核真实计数；人数原文区分入组与完成 | open（同一版本 35/36 差异与统计合同待核） |
| X06 | 2026-11-27 | 器官钟 UKB 样本量 | Nat Aging 正文 43,616（分析集）；一处二手报道 44,498（全集） | 两个口径都真实存在，引用需指明口径 | 以原文口径为准 | resolved（以 43,616 为准） |
| X07 | 2026-11-27 | 14 项共识清单的误传 | Grokipedia 等二手页把 VO2max/HbA1c 列入共识；原文共识为 IGF-1/GDF-15/hsCRP/IL-6/肌肉量/肌力/握力/TUG/步速/平衡/衰弱指数/认知/血压/DNAm 钟 | 无 | 已按原文裁决；作为"来源卫生"示例保留在台账 | resolved |
| X08 | 2026-11-27 | 器官钟纵向研究状态 | bioRxiv 预印本（2026-02，n=1,250） | 未同行评审 | 只作 Known Unknown（U3），不作定论 | open |
| X09 | 2026-11-27 | 旧债关联确认 | 本台账不复制 OWED_DEBTS.json 内容 | — | D03/D04/D08/D10 的推进在 THE-232；D05 在 THE-234 | resolved（机制确立） |
| X10 | 2026-11-27 | TRIIM/TRIIM-X 持久性两说 | 原始叙事：GrimAge 逆转停药后持续 6 个月（多篇二手）；2026-08 Int Immunol 综述：TRIIM 类治疗停药 6 个月后胸腺脂肪、初始 T 细胞、表观年龄**回落至基线**（引其 ref 131） | 两者可能描述不同随访终点或不同指标；需核 TRIIM-X 原始数据 | KERNEL §3.2 TRIIM 行加冲突标记；转换八表述降级为"持久性必须在停药后测量（结果可能为回落）"；核原文前正文不引"持续" | open |
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
| X30 | 2026-11-27 | SPRINTT 多病潜类与干预效应异质性 | [2026 事后分析](https://www.nature.com/articles/s43587-026-01188-x) 包括潜类及部分池化亚组分析 | 统计交互、潜类不确定性、多重比较、先验及外部验证尚未复核 | 禁止由亚组显著与否直接断言效应差异；核模型、先验与 protocol | open |

| X31 | 2026-11-27 | CALERIE 甲基化分析时点人数的集合边界冲突 | [原文 Main 与 Fig. 1 说明](https://www.nature.com/articles/s43587-022-00357-y)：分析 128/69，12 月变化 125/66、24 月变化 117/68；三时点均有数据 105/59 | 若各时点是同一组 197 人母集且同一定义的个体，完整数据下界分别 114/65，与报告值不相容；可能另有口径或报告问题 | 核图、补充表、数据字典及作者；暂不判哪项出错或影响方向；[条件算术](COUNTEREXAMPLES_AND_DENOMINATORS_2026-11-27.md)；另见固定 PR 的 [公开源码静态审计](../review/PR1_RECONCILIATION_2026-11-27.md)，无 ID 的数据不可按行序配对或重建身份 | open |

| X32 | 2026-11-27 | KERNEL I6 曾把模型 m 误写为迁移 | [状态周转模型](../longevity_state_turnover/状态还在_不等于细胞没换.md) §4：m 是成熟退出率，d 是其他丢失；模型不含迁移 | 真实系统可能有迁移，原模型不能排除 | 已修正 KERNEL；须审查其他引用 | open（下游传播待核） |
| X33 | 2026-11-27 | 基于甲基化的谱系标记在甲基化干预后可能漂移 | [EPI-Clone](https://www.nature.com/articles/s41586-025-09041-8) 摘要/主文开头；项目假说非原文结论 | 干预是否改写其标记、错分方向与程度未知，未经直接测试 | 正交遗传参照、干预前后误分类校准；不声称实测漂移 | open |

| X34 | 2026-11-27 | CALERIE 12 月对照组在发表版 Fig.1 与补充 S1 的计数口径 | [发表版 Fig.1](https://www.nature.com/articles/s43587-022-00357-y)描述基线到 12 月变化 66；[补充 S1](https://rcastoragev2.blob.core.windows.net/a9fc145035a1ff44bee8d283ac3ca9b6/43587_2022_357_MOESM1_ESM.pdf)描述同一分析样本 12 月随访 65 | 随访可用与变化分数不必自动同口径；需确认样本、时钟和配对 | 见 [版本审计](CALERIE_X31_VERSION_AUDIT_2026-11-27.md)；不静默替换，非独立复现 | open |

| X35 | 2026-11-27 | COLON26 类器官洗脱与体内肿瘤抑制时间窗 | [Fig.2m–n 和 Methods](https://www.nature.com/articles/s41586-026-10258-4)：体外处理后洗脱 20 天；体内抑制与 APC 诱导重叠 | 体外形态非体内肿瘤；培养选择和统计单位待独立核查；非显著不等效 | 更新历史读深，不能称体内停药后持久防癌；见 [续审](RECOVERY_MEMORY_CAUSAL_AUDIT_2026-11-27.md) | open（部分时间窗已核） |
| X36 | 2026-11-27 | GUT26 抗体给药和再次照射间的残效 | [Fig.7 与 Results](https://www.nature.com/articles/s41467-026-79014-6)：图注 5 次每三天起于第一次之前一日；三周再照射 | 确切给药时间、药物/靶点占有及再挑战期效应未验证；首轮处理与恢复后编辑不同 | 按图注推算间隔但不等于测得洗脱；求作者及实验数据澄清 | open |

| X37 | 2026-11-27 | CAPABLE 注意对照的实际接触与再测选择 | [原文 Methods、Results](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2720136)：8–10 次访视 141/152 vs 73/148；5 月再测 130/152 vs 133/148；2019 论文将 ADL 与 IADL 均列主要结果 | 访视不均并不单独证伪随机效果；未再测者更老、功能差，模型依赖假设；主要终点多重性、协议与补充材料未全核 | 纳入 [CAPABLE 核读](CAPABLE_RECHECK_2026-11-27.md) 与书稿；不归因单个部件，后续核协议 | open |

| X38 | 2026-11-27 | CAPABLE 早期设计与结果文主要终点的口径 | [2014 设计文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4074085/)称 ADL 主要、IADL 次要；[2019 结果文](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2720136)将二者列主要；[登记 API 当前记录](https://clinicaltrials.gov/api/v2/studies/NCT01576133)列 ADL 主要 | 两文属于同一试验；登记历史、批准修订、最终方案及多重性未核，不知口径变化原因 | 书稿并列说明；查注册历史及有日期方案，不判违规、差错或方向影响 | open |

| X39 | 2026-11-27 | CAPABLE 登记与论文收入及住房资格口径 | [登记 API](https://clinicaltrials.gov/api/v2/studies/NCT01576133)：收入低于 175% FPL，未列公寓排除；[2014 设计文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4074085/) 200% 或以下并排除公寓；[2019 结果文](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2720136)低于 200% 并排除公寓 | 登记为摘要且当前记录的历史版本尚未核；差异原因、实际筛选及修订均未知 | 如实披露多版本；查注册历史、批准方案与筛选数据，不判违规或效果偏倚 | open |

| X40 | 2026-11-27 | LoDoCo2 导入期总体斜率点估计与置信区间不相容 | [出版版 Results](https://www.jacc.org/doi/10.1016/j.jacc.2025.08.025) 及 [PMC 作者稿](https://pmc.ncbi.nlm.nih.gov/articles/PMC12557339/)：β=−0.026，CI −0.099 至 −0.046，P=.48 | 点估计不在所报区间；如果这些是同一参数及通常双侧区间，则还与未显著说法不协调。两版本同源，尚未核统计输出、图或勘误 | 暂不修数值或引用该区间；见 [LoDoCo2 核读](LODOCO2_AUDIT_2026-11-27.md)，核补充图、统计输出并请求澄清 | open |

## 带命名空间的新增待核条目（2026-11-27）

| ID | 事项及一手来源 | 处置/限制 | 状态 |
|---|---|---|---|
| L:FIND-TABLE1 | [骨折论文表1](https://www.sciencedirect.com/science/article/pii/S8756328226003078#t0005)过去一年跌倒 309/829 印 33.1%，按列出整数计算约 37.3%。 | 记为口径/报告待澄清，未核个体数据、作者或勘误；不修改 HR，见 [跨结局核读](FIND_CANCER_FALLS_FRACTURES_2026-11-27.md)。 | open |
| L:FIND-FIRST | [FIND 主文](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/)癌症死亡第一事件 0/0/0，但正文另报癌症死亡 11/14/10 且称非第一事件。 | 限定第一事件口径，不写成“无人癌症死亡”；不从它推断全因死亡完整计数。 | open（文字口径已核） |
| L:DOHEALTH-FUNCTION | [2026 原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC13396198/)功能比较为观察性、最近访视定义可早于确诊；正文敏感性句与[补表2](https://pmc.ncbi.nlm.nih.gov/articles/instance/13396198/bin/41514_2026_360_MOESM1_ESM.docx)单位与标签不一致；先由 PR1@94ce2ff:X57–X58 记录。 | 补表主估计跨时汇总，不能当终年估计或干预因果效应；原始代码、不同样本数及勘误待核。 | open |

| L:COLCOT-VERSION | [COLCOT 预印本 v1](https://www.medrxiv.org/content/10.1101/2024.10.17.24315679v1.full)链接至 [2026 Circulation](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.125.077665)，[PubMed](https://pubmed.ncbi.nlm.nih.gov/41730026/)无摘要、发表正文需访问权限。 | 不把预印本数值自动归于发表版，取得最终正文、补充材料后逐项对照；同一研究两版本不算重复。详见[比较](COLCOT_LODOCO2_TRIANGULATION_2026-11-27.md)。 | open |
| L:CH-POSTSELECT | [COLCOT v1](https://www.medrxiv.org/content/10.1101/2024.10.17.24315679v1.full)的自愿子研究、两次采样及常在治疗后首次采血；[LoDoCo2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12557339/)随机后任一时点 CH 检出分析。 | 可能涉及随机后选择，不断言必有偏差或其方向；需采样流程、失访、检测和事件时序及敏感性分析；人工反例不提供真实偏倚估计。 | open |

| L:CALERIE-AUC-CONTRAST | [CALERIE 2026 表2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13094879/table/T2/) AUC 回升组与轻微回升组12月变化 −4.9、−10.8，直接相减 +5.9，表列交互 +3.0；24月 +15.9、−7.6，直接相减 +23.5，表列 +21.2。 | 若同模型同尺度同对比则不能仅靠舍入解释；可能有变换、样本或其他口径区别；[补充材料可提取文本](CALERIE_TRAJECTORY_MISSINGNESS_FIGSHARE_2026-11-27.md)现已读取，AUC 对应模型和代码仍未核。暂不更改原值或判计算错误；详见 [PR审计](../review/PR1_INCREMENTAL_AUDIT_52362B6_2026-11-27.md)，另见 PR1@52362b6:X59 分组阈值。 | open |
| L:CANTOS-CRP-UNIT | [CANTOS 子研究正文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988022/) CHIP/无CHIP中位 hs-CRP 0.44/0.42 mg/dL，[表1](https://pmc.ncbi.nlm.nih.gov/articles/PMC8988022/table/hoi220009t1/) 4.40/4.20 亦标 mg/dL；若同组统计口径则相差10倍。 | mg/L 可能解释数字，但不得静默修正；需核出版PDF、数据字典/作者、勘误，不由此推断临床HR错误。见 [核读](CANTOS_TET2_CLINICAL_INTERACTION_2026-11-27.md)。 | open |

## 交叉验证规则（本轮起生效）

1. 任何进入 KERNEL §3.2 的数字，至少一个来源须为一手（原文/官方 PDF）；二手来源只能提供线索。
2. 两来源冲突 → 登记 X-item → 读一手 → 裁决 → 在此留痕（不删除记录）。
3. 公司/竞赛自报数据（X02 类）永久带标注；不得以"已获奖"佐证科学结论。
4. 预印本（X08 类）永久带标注；升级为"已核"须有同行评审版本。
5. 台账与 KERNEL 冲突时：先修 KERNEL 并递增版本，再修改下游书稿/论文。

| L:CALERIE-S3-DENOM | [轨迹报告](https://pmc.ncbi.nlm.nih.gov/articles/PMC13094879/)分析190人；[S3](https://ndownloader.figshare.com/files/61614040)胰岛素 AUC 基线缺57（29.8%）、12月33（17.3%）、24月6（3.1%）。 | 在缺失数除以共同整数分母并按一位小数最近舍入的假设下，57和29.8%仅与191相容；不证明该分母或样本身份。条件 N=190/191 完整三时点界分别94–133/95–134，非实际模型N；见[细读](CALERIE_TRAJECTORY_MISSINGNESS_FIGSHARE_2026-11-27.md)。先由 PR1@370dd15:X60 取得并记录补表。 | open |
| L:CALERIE-MEDIATION | [同试验脂质组报告](https://pmc.ncbi.nlm.nih.gov/articles/PMC13482398/)的中介方法分别写处理为暴露、时间为暴露与按组分析，可能是不同模型；逐项 bootstrap 区间不自动控制多重假阳性。 | 核代码、具体估计目标和检验家族；图6是工作假说，不是直接机制确定，不作独立试验复制。见[定向审计](CALERIE_LIPID_MEDIATION_2026_2026-11-27.md)。 | open |
