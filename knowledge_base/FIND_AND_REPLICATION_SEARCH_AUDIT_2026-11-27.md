# FIND 主癌症终点与 DO-HEALTH 复现线索的定向审读

2026-11-27。阅读 FIND [原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/)、[表2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/table/tbl2/)、[表3](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/table/tbl3/)与 [NCT01463813](https://clinicaltrials.gov/api/v2/studies/NCT01463813)，并做有限登记和网络检索。不是系统综述、正式证据综合或患者级复算。

## 1｜另一个独立随机试验：FIND

芬兰 2012–2018 年试验随机 2,495 人，安慰剂 830、D3 1600 IU/天 832、D3 3200 IU/天 833；白人男性 ≥60 岁、绝经后女性 ≥65 岁，基线无癌史（非黑色素瘤皮肤癌除外）或心血管病史。侵袭癌为预设主要终点之一。表 2 随访病例分别 41、48、40；年龄、性别调整 Cox HR 为 **1.14（95% CI 0.75–1.72）**和 **0.95（0.61–1.47）**，分别对安慰剂。这是额外不同剂量维生素 D 的试验证据，不是对 D+omega-3+运动的直接检验；区间较宽，不证明绝对无效，也不否定特定低维生素 D 人群的效果。另一维度见 [VITAL/DO-HEALTH 比较](VITAL_DO_HEALTH_CANCER_COMPARISON_2026-11-27.md)。

研究原目标 18,000、实际随机 2,495；原文对五年累积发病所需量估计每组 2,572，不应把原设计所宣称的 >80% 功效直接当实际研究功效。原文报告平均随访 4.3 年、中位 5.0 年；551 人更详细检查子队列基线均值约 75 nmol/L，不是全部随机者的实测均值，子队列与其他人在人口特征上有差异。95.3% 自报服用至少八成药片的分母仅为 1,609 末次问卷完成者，而非全部随机者。两维生素 D 组合组相对安慰剂 HR 1.04（.72–1.51）是作者称因事件少而做的**事后**分析，两个主动组共用一个对照，不得把它们当两项独立对照试验、重复计数对照病例。

## 2｜两项需澄清的原文口径，不能自行修正

1. 方法的终点获取段说登记链接且“无失访”，统计段又说随访至个人原因退出（n=412）等时点；二者可能涉及不同定义或资料权限，但正文目前未在本次读取中解释。须查方案、流程图、注册链接权限及作者说明，不能武断视为矛盾证明出错，也不能以“无失访”替代退出删失。
2. [表 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/table/tbl3/)标题为主要终点亚组，癌症行写 `Any cancer`，男女两个互斥亚组事件求和分别为安慰剂 37+25=62、1600 IU 38+33=71、3200 IU 33+29=62（合计 195）；按年龄亚组重算也同样得到 62/71/62。[表 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9071497/table/tbl2/)主侵袭癌却是 41/48/40（合计 129），正文方法说交互分析仅做主要终点。若两表是同一随访、同一事件定义与受试者计数，互斥分组之和理应相同；目前不能排除 `Any cancer` 包含不同癌种/事件、分析数据集或表格标注差异。尚未核代码、补充方法或正式作者澄清，不推断原因、方向或 HR 错误，**不要把表 3 直接写成主侵袭癌亚组效应**。

## 3｜定向注册检索：哪些不是复现

2026-11-27 在 ClinicalTrials.gov API 以 `"vitamin D" AND "omega-3" AND exercise AND cancer` 查询，返回 [11 条记录的简表](https://clinicaltrials.gov/api/v2/studies?query.term=%22vitamin%20D%22%20AND%20%22omega-3%22%20AND%20exercise%20AND%20cancer&pageSize=100&countTotal=true&fields=NCTId%2CBriefTitle%2COverallStatus%2CStudyType)；未逐条全文审查，搜索依赖登记措辞、仅一个库，不能声称不存在独立复现。

| 候选登记 | 为什么不是此处要找的独立三项癌症预防复现 |
|---|---|
| [NCT05062018 DO-HEALTH-C](https://clinicaltrials.gov/api/v2/studies/NCT05062018) | 原试验参与者停干预后的观察性队列，可探索长期轨迹，但不是另一次随机化；登记状态 UNKNOWN，日期 2022-12-06 更新，不可由预计完成日期推断已完成或有结果。 |
| [NCT03649698 ENHANce](https://clinicaltrials.gov/api/v2/studies/NCT03649698) | 老年肌少/前肌少人群，5 臂含运动、蛋白与 omega-3；D 依方案所有组均补充，主要为体能，12 周，不是随机 D 因子或癌症预防复制；状态 UNKNOWN。 |
| [NCT05331807](https://clinicaltrials.gov/api/v2/studies/NCT05331807) | 已诊断乳癌、接受化疗者，D/omega-3 营养干预，不是首次侵袭癌预防或随机运动三项组合；登记 completed 不等于本次核实了发表结果。 |
| [NCT05955248](https://clinicaltrials.gov/api/v2/studies/NCT05955248) 和 [NCT04610606](https://clinicaltrials.gov/api/v2/studies/NCT04610606) | 肺癌手术前后复健的多营养素/运动研究，目标为术后功能或可行性，含额外蛋白等；不是一般人群癌症发生预防复现。前者状态 UNKNOWN、后者因疫情终止；未核结局报告。 |

后续需预设数据库、同义词与时间范围，逐条审查研究设计和终点，进一步检查 WHO ICTRP、欧洲登记及新发表报告，并核作者对 FIND 表3/退出删失的解释；当前没有联系作者或外部审稿人。

## 4｜补充材料及扩展检索（续）

阅读 [FIND 补充材料 DOCX 的可提取文本](https://pmc.ncbi.nlm.nih.gov/articles/instance/9071497/bin/nqab419_supplemental_file.docx)，其中有功效计算、血清测定和子队列特征，但本次读取的文字没有解释表2/表3的癌症计数差异或 412 人退出删失与“无失访”的关系；补充图中的图形内容未由文本提取完整，不等于检查了全部图像细节。补充方法说 52 月邀请 120、116 同意，其中 60 来自子队列、54 来自其余人；然而同一句括号列其余三组 18+18+20=56，补图2图注也写 56；`60+54=114`，`60+56=116`。这是**文字计数不一致**，不能据此判定哪项错误，且不能把它迁移成主癌症终点错误。亦未取得原始样本名单或联系作者。

扩展 [ClinicalTrials.gov 查询](https://clinicaltrials.gov/api/v2/studies?query.term=%28vitamin%20D%20OR%20cholecalciferol%29%20AND%20%28fish%20oil%20OR%20DHA%20OR%20EPA%29%20AND%20%28exercise%20OR%20%22physical%20activity%22%29%20AND%20cancer&pageSize=100&countTotal=true&fields=NCTId%2CBriefTitle%2COverallStatus%2CStudyType)为 D/鱼油/运动同义词，返回 20 条简表。另看以下可能误命中的登记：

- [NCT01178892 MsFLASH-02](https://clinicaltrials.gov/api/v2/studies/NCT01178892)：随机 omega-3 与瑜伽/运动/平常活动，研究更年期症状而非三项癌症预防，未有随机 D 因子。
- [NCT03831841 EXERNET](https://clinicaltrials.gov/api/v2/studies/NCT03831841)：非随机运动、测量 25-OH D 与功能；不是补充 D 和 omega-3 的随机组合。
- [NCT04574323](https://clinicaltrials.gov/api/v2/studies/NCT04574323)：乳癌放疗中的非随机生活方式可行性研究；登记称不允许补充剂，不是一般人群新发癌的随机预防。
- [NCT04871412 POISE](https://clinicaltrials.gov/api/v2/studies/NCT04871412)：已患胸部肿瘤手术者的多组分综合照护，含个体化 D、鱼油和运动建议等额外措施；登记估计纳入 20，不能视为相同剂量、对照、目标人群和结局的验证。
- [NCT07007169 MEDITERRACARE](https://clinicaltrials.gov/api/v2/studies/NCT07007169)：早期乳癌治疗期间的地中海饮食随机试验，主要为肠道微生物变化，不是相同预防试验。
- [NCT03372109](https://clinicaltrials.gov/api/v2/studies/NCT03372109)：23 人随机改良禁食和多补充剂，主要体重；不是三项组合癌症预防试验。

这些是选定记录的定向设计排除，不是对 20 条全部全文筛选，登记查询受术语、字段和覆盖范围限制；无关候选不证实三项复制不存在。

原 DO-HEALTH [登记](https://clinicaltrials.gov/api/v2/studies/NCT01745263)当前版本 `otherOutcomes` 列 incident cancer（any、胃肠、乳腺、前列腺）及 36 个月；与癌症论文将其称为预定义探索性结局相符，但当前 2018 更新记录不能独自证明每个特定对比、模型、方案版本或分析时序均为事先确定，需核登记历史与完整预设分析计划。
