# HANDOFF｜LONGEVITY SESSION收束与下一会话接续
## Session Handoff — Existing Manuscripts Updated, Research Boundaries Preserved

> **路径维护注（2026-11-27）**：本文保留上一会话的时间与历史状态。原工作台目录已迁移，以下七处链接目的地改指当前 `corpus/`、`papers/`、`books/`；历史原路径见 [续审记录](review/PR1_CONTINUATION_AUDIT_2026-11-27.md)。旧会话“不另建 HTML”限制已被用户随后明确要求创建 `STATE_DASHBOARD.HTML` 所覆盖；不能据旧状态推断当前进度。本文其余历史叙述未整体重写。

**交接日期标签：2026-11-25（当前会话提供的America/Los_Angeles日期）。** 文件系统mtime可能显示11-26，不能拿mtime反向重写会话日期；日期记录冲突见[日期说明](RESEARCH_DATE_CLARIFICATION.md)。

**用户本轮明确要求：本SESSION最后一轮；交付HANDOFF及必要文件；更新原有专著和论文，不另建新版稿件；下SESSION将连接GitHub。**

---

## 0｜给下一SESSION的十分钟入口

1. 先读本文第1—4节，核对[更新回执](SESSION_UPDATE_RECEIPT.json)，再读现有书稿新增部分。不要重新生成同题新文件或完整V8。
2. 本轮已将六轮研究**作为待独立审阅工作稿**加入原有V6/V7；P1/P2/P3更新的是既有`PROTOCOL.md`，不是不存在的完整论文。
3. 原始专著目录为`longevity_v6/`、`longevity_v7/`；工作台`corpus/editions/`已有副本已同步。接入仓库后明确一个唯一编辑源，避免两边独立修改。
4. 研究核心仍是新探索，不是无限清旧债：源—接收容量、时间/空间可达、清除与维护、状态周转、修复记忆与未来挑战。原始事实、描述复算、人工模型、待验假说不混写。
5. 独立外审未发生。此次作者要求的在位更新不代表正式合成门槛通过；不称新实验、临床疗效、寿命预测、无人做过认证或涌现发现。
6. 当前工作区约112 MiB（最终以回执为准）；已清理541个可恢复重复文件，释放87,825,186 bytes。不要重新全量展开已归档的引擎目录或复制大型源表。
7. 没有远端提交。当前轮查询GitHub工具返回`unsupported`；只说明本轮工具状态，不预断新SESSION连接状态。新SESSION须重新查询可用工具、读取真实仓库/分支，不猜owner/repo/ID，不擅自覆盖或push。

## 1｜实际更新了哪些原文件

### A. 专著正文：原路径更新，不另建新稿

|角色|文件|本次内容|
|---|---|---|
|V6原正文|[长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md](longevity_v6/长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md)|保留原有广度；新增“维护的不只是今天的身体，还有下一次恢复的可能”，S6.1—S6.6专题|
|V7原正文|[长寿研究_V7_谁在变年轻.md](longevity_v7/长寿研究_V7_谁在变年轻.md)|保留前33编号章；新增第十部34—39章，接入六轮机制与可证伪实验|
|工作台既有V6副本|[同名V6](corpus/longevity_v6/长寿的科学艺术哲学与工程_V6_维护身体扩展生活.md)|与V6原正文逐字节一致，角色改为同步工作稿|
|工作台既有V7副本|[同名V7](corpus/longevity_v7/长寿研究_V7_谁在变年轻.md)|与V7原正文逐字节一致，角色改为同步工作稿|

两书开头均标明本次授权更新、尚待独立审阅及历史产物范围。新增引用在新增正文直接给出；没有假装旧机器索引已覆盖全部新增来源。未重写V4/V5或把两种透镜粗暴合并。

### B. 论文与书架构：更新现存协议，不虚构全文

- [P1 身份与选择协议](papers/P1_identity_selection/PROTOCOL.md)：状态持续/同细胞持续、队列退出/成熟、细胞内记忆编辑/克隆选择；恢复后随机化的目标人群。
- [P2 权重与可见性协议](papers/P2_weighting_observability/PROTOCOL.md)：静态存量、动态通量、时间窗口和空间覆盖的测量合同；仍不把线性混合推广为万能动力学模型。
- [P3 研究保障协议](papers/P3_research_assurance/PROTOCOL.md)：来源层级、重复单位、人工参数、生效窗口与授权变更后的版本失效；新样例只能算已见回归集，非盲测。
- [PUBLICATION_MAP](papers/PUBLICATION_MAP.md)、[BOOK_PROPOSAL](books/BOOK_PROPOSAL.md)：同步本次接入与投稿门槛，不新增P4/P5凑数。

三篇正式题名保留：

1. **谁在变年轻？** / *Who Is Getting Younger?* — 身份、替换与选择。
2. **指标下降，谁更年轻？** / *A Lower Biomarker, a Younger System?* — 组成、权重与可见性。
3. **让研究结论随证据变化而失效** / *Making Research Claims Expire When Their Evidence Changes* — 研究保障与可重放审计。

### C. 配套在位更新

V6/V7的README、RESEARCH_LOG与当前manifest；工作台README、CHANGELOG、`corpus/editions/README.md`、`docs/GITHUB_HANDOFF.md`、`governance/NEXT_PRIORITIES.md`和FILE_MANIFEST均已更新。逐文件前后hash、大小和原正文恢复位置见回执。

**仅新增交接文件与小型迁移包，没有另建专著或论文版本。**

## 2｜当前文件的权威关系：不要用旧产物覆盖新稿

|文件类型|当前角色|下一SESSION注意|
|---|---|---|
|V6/V7当前Markdown及工作台同名副本|待独立审阅的活跃工作稿|接入后选定一个编辑源；本地同步不是两个独立版本|
|旧STATE_DASHBOARD.HTML、截图、V6 manuscript.txt|更新前的历史阅读器/构建中间物|不含新增文字，不作为当前正文；用户不要新HTML|
|旧evidence_index.json/tsv|原发布来源索引|不冒称全覆盖新章节；新源先看六模块读取记录|
|旧QA_REPORT/PRE_SYNTHESIS_AUDIT/VALIDATION/HISTORY_INTEGRITY|过去版本及既定范围的历史记录|不为新文字背书，不把同助手自查叫独立外审|
|当前V6/V7 manifest、工作台FILE_MANIFEST|当前分发字节清单|可校验完整性，不代表科学重审、许可或历史未变|
|governance/history_before.json|原始历史信任基线，保留不动|不能改hash来伪造原稿未改；旧验证会报告已授权修改/归档缺失|
|既有ZIP|冻结历史交付与恢复依据|本轮不改字节；准确成员位置见回执|

旧builder可能从历史输入重建/覆盖产物。**不要直接运行V6/V7 build.py、工作台package_delivery.py、旧pilot builder或旧prepare_bindings来“刷新”新稿。** 它们没有为本轮写作更新重新验收。旧历史验证不再全部unchanged是可解释版本差异，不能通过重签基线消除。

## 3｜六轮探索：当前目录与最重要结论

所有路径相对于本文所在根目录。模块分层：研究框架＋工具包＋局部可复算脚本；不是统一长寿引擎，也不是已部署平台Skill。

|轮次/模块|主文|完成与边界|
|---|---|---|
|1 源—接收分工|[谁在为年轻买单](longevity_new_territories/谁在为年轻买单_新领土研究.md)|3份真实xlsx的选择性描述复算；容量/克隆与顺序人工反例；14实现检查、11迁移输出同为此前自查|
|2 时间|[平均未超载，为什么仍会积压](longevity_capacity_timing/平均未超载_为什么仍会积压.md)|人工饱和处理脉冲反例；21检查；无细胞拟合、剂量或寿命结论|
|3 空间|[有余量却用不上](longevity_spatial_access/有余量却用不上_空间可达性的研究盲点.md)|eLife两CSV描述＋人工网络；23检查、5迁移输出同；技术/生物重复与MFI单位已核|
|4 清除选择性|[清除者也在靶标里](longevity_caretaker_selectivity/清除者也在靶标里_保留维护能力的年轻化.md)|靶点/状态/净功能分离；维护保护实验；人工比值恒等式8检查/110精确格点|
|5 状态周转|[状态还在，不等于细胞没换](longevity_state_turnover/状态还在_不等于细胞没换.md)|肺泡命运证据＋人工竞争退出反例；7检查、2迁移输出同；预印本人体静态图像不等动态速率|
|6 修复记忆|[修好这一次，还剩多少下一次](longevity_repair_memory/修好这一次_还剩多少下一次.md)|骨/肌/肠正反证据；建立/调用/擦除分开；6来源表，8文件一致性检查；无新数值模型|

以上计数主要来自各轮既有回执，本收束轮没有冒称全部重新计算。收束轮新增的是修改前后完整性、同步与迁移包核查，不是重新验证生物学。

### 3.1 必须保留的定量结果与单位

- **TBX3真实源表描述**：KO/WT组均值比ALT（3月）0.598165、肝TG（6月）0.744179、血TG（6月）1.496824、GTT AUC 1.274047；P407条件分泌1.315824、3h ApoB 3.208930。不同面板/时长不配对，全肝KO≠人体稀有克隆，未算新p值。
- **基质ABT真实描述**：两组变化之差为−2.18394、−26.72056、−25.01667个百分点，分别对应衰老MSC频率、供者BM/HSC贡献；ABT非MSC特异。
- **β-catenin真实描述**：年轻健康肝不同横断面队列中，6.5月突变/报告对照每鼠密度组均值比约0.059053；非同鼠损失轨迹，不遍历N03的Figure7D百万行。
- **人工时间**：V=K=1、平均输入0.6、周期8、占空比0.125；恒定存量1.5，脉冲平均2.020450972780、峰4.400382475555；线性对照均值均0.6。标准非线性/Jensen反例，非新定理。
- **eLife真实源表**：24h归一化总珠MFI，生物汇总n=3，WT 46.76990145、Itgb1KO 69.9984771033、KO2× 50.6739104367、WT2×32.29053866；不是残余珠数/终末降解。悬液内化面板技术n=3，不升级动物n，不跨面板配对。
- **人工空间**：总输入1、总容量1.2，受限网络最大流0.6；远端容量翻倍仍0.6，桥容量增加可至1；乐观可行流而非实际生物路由。
- **人工选择性**：`rho后=rho前*(1-a)/(1-b)`；a是输入通量减少比例，b是有效容量损失比例，不是细胞清除率；固定饱和模型有限稳态还需rho后<1。
- **人工状态周转**：`T*=j/(m+d)`；同样100→50，成熟输出可8→9或8→4；标签留存只约束m+d，不独自区分成熟与死亡。

### 3.2 关键原始来源导航

|主题|来源|读取深度/最重要限制|
|---|---|---|
|TBX3局部—系统冲突|https://www.jci.org/articles/view/191855|源表选择性描述；未重做实验|
|双向线粒体EV|https://www.nature.com/articles/s41556-026-01896-x|巨噬不同亚群相反功能，不混单向清除|
|基质与DNMT3A|https://www.nature.com/articles/s41556-026-02025-4|机制研究＋ABT源表描述，非特异因果|
|空间巡查|https://elifesciences.org/articles/75354|主站壳后用API核图注/Methods，原始小CSV保留|
|结构p16High细胞|https://pubmed.ncbi.nlm.nih.gov/32485135/|特定模型屏障/替代风险，非所有senolysis无益|
|uPAR肠道获益/不同构型毒性|https://www.nature.com/articles/s43587-025-01022-w 及 https://pmc.ncbi.nlm.nih.gov/articles/PMC13620297/|构型、剂量、模型不同；NHP短暂异常不等无不良反应|
|DATP与持续IL-1β|https://pmc.ncbi.nlm.nih.gov/articles/PMC7487779/|摘要与相关Figure5/7正文；类器官成熟标记非气体交换证明|
|ISRIB与谱系输出|https://www.pnas.org/doi/10.1073/pnas.2101100118|直接AT2谱系为年轻成年鼠，不把整篇老龄实验混入|
|状态周转新近邻|https://www.biorxiv.org/content/10.64898/2026.11.08.765110v1.full|未同行评审，部分正文/图注；人体静态图不提供速率|
|骨再挑战|https://www.nature.com/articles/s41467-026-76108-z|含12周间隔；形态不代表全骨机械功能，救援不等停药后持久重置|
|肌肉修复经验|https://pmc.ncbi.nlm.nih.gov/articles/PMC10496398/|50天间隔；形态与pS6关联非寿命/必要性证明|
|小肠修复记忆|https://www.nature.com/articles/s41467-026-79014-6|21天间隔、首次期IFNγ抗体；不是恢复后擦除，残余药效未核|
|结肠炎记忆/早期肿瘤|https://www.nature.com/articles/s41586-026-10258-4|APC诱导模型；并非所有宏观肿瘤数增加；AP1抑制不足以擦记忆|
|修复记忆双面性先例|https://www.nature.com/articles/s41556-023-01120-0|本轮仅摘要/引言chunk0，不虚称机制全文通读|

更细的逐块读取/未采用线索，以各模块READING_RECORD及首包docs为准。GVHD23仅为Research Square v1预印本且本轮未逐图核，不能升级成主结论。搜索没找到不证明无人做过。

## 4｜尚未完成、不得在新SESSION悄悄升级的事

- 没有独立领域/统计外审，没有注册实验、伦理审批、新动物/人体实验或长期疗效。
- 没有“真正稳定衰老普遍可逆”“清除越多越好”“记忆越少越年轻”“先清除后OSK”的证据结论。
- 没有自动关闭D02–D10、D05或M01/M06等历史债。旧具体债的原状态保留在工作台/工具包session记录与归档；不要因新概念或hash更新关闭。
- 旧引擎的拓扑/H⁰/全局截面、fact_consistency及原代码核验已有历史交付；不为续研重建，不把局部可满足性当世界真理，不把代码归档存在当发表时真实执行证明。
- 旧临床/组学案例仍缺的身份、死亡、配对bulk/单细胞、capture/copy及crosswalk金标，没有被本SESSION新源表替代。
- 没有启动AGENTIC MAX ROUTER或切换指定模型的工具；不伪称模型路由、外部会审或子代理已执行。
- 没有新HTML/仪表盘，不建议下一会话重建。保留旧HTML仅为历史。
- 谨慎处理2026新近邻；不为题名、理论或新颖性提供“未有人类做过”认证。

## 5｜下一SESSION最值得推进的研究，而非再造工具

### 当前新切口

**在记忆已经建立后，能否降低异常克隆增长，又保留正常再修复？**

先核首次期干预与恢复后编辑的区别、残余药效、同细胞编辑与克隆替换。恢复后随机化；确认药效消退；用独立样本分支测试无挑战、同类/异类再损伤和合规的异常克隆启动。预设非劣效界值，不用“不显著”冒充保留修复；分析按供体/动物分层，不把视野/肿瘤/细胞当独立个体。

### 更早但仍值得保留的实验主线

定义一种cargo，先识别源—接收者终末处理，再扩展输出型克隆比例×接收能力。控制生成、摄取和炎症等多效性；若不可独立操纵，承认识别失败或换设计。不直接上寿命实验。

### 只处理关键证据债

1. GUT26抗体时间/残余药效与首次损伤等效性；不把ns当等效。
2. BONE26部分救援的停药再挑战、全骨机械功能和老龄外推。
3. 过渡状态的人体动态周转与老龄直接命运追踪。
4. 近邻与可行性独立评审；仅在会改变路线时补Methods/SI，不为了“查完”而拉取大组学库。

## 6｜新SESSION连接GitHub：接收顺序与真实边界

### 已有工作区完整可用时

先核目录与回执，再检查实际远端。最少保留本根的工作台＋六研究模块；V6/V7原目录与工作台内副本在首次接入时说明权威关系。若远端已有另一布局，先产生映射/差异再应用，不盲覆。只读连接不等授权发布，push前确认目标分支、变更、许可与敏感性。

### 新会话只收到下载文件时

**推荐最小携带三件套：**

1. `SESSION_HANDOFF_PATCH.zip`（本轮新小型增量包）；
2. `Longevity_Research_Workbench_0.1.0.zip`（既有完整工作台基底，约334 KiB）；
3. `Longevity_New_Territories_谁在为年轻买单.zip`（既有首包，约17.5 MB，含真实xlsx和读取凭据）。

如需完整V6/V7历史HTML/QA/构建文件，另带原`长寿V6_完整作品与原生HTML附件.zip`、`长寿V7_谁在变年轻_完整作品与原生HTML.zip`；PATCH已含当前书稿本身，不需要为读新增部分强制带旧HTML。

**应用顺序**：在新暂存目录中，先检查ZIP成员名无绝对路径/`..`，解压需要的旧基底，然后**最后应用PATCH**。已有真实仓库时先人工diff，不直接覆盖；不要在PATCH之后再用旧基底覆盖同名文件。上述既有ZIP均已核其前缀分别为`longevity_research_workbench/`、`longevity_new_territories/`、`longevity_v6/`、`longevity_v7/`。

PATCH包含：本根HANDOFF/回执/日期与清理说明、21个现存文件更新、后五个小型研究模块完整文件；另携带工作台0.1.0旧基底所缺的既有pilot001增量，使基底加PATCH可以恢复当前完整工作台。pilot001本身的研究裁决与冻结数据没有因此改写。**不含首包全部源表/缓存、工作台全部工具源码、全部历史档案或会话聊天。** 因此PATCH单独不是完整可复现仓库。归档恢复收据引用的旧ZIP需另带，PATCH不复制它们。精确成员以回执为准，不能只看目录名推断已完整迁移。

### 许可、安全与发布

先Private为宜。原创正文/代码许可分别确认；出版方图表、PDF及第三方全文缓存不自动拥有可公开再分发权。不要把token放文件或发给助手；普通低权限PR CI，真实reviewer与分支规则必须远端实际设置。没有自动替用户授予MIT/CC，也没有设置远端保护规则。

## 7｜本地复现命令与不应重跑的项

命令默认在包含六模块的根目录执行；会覆盖各模块输出，正式核对前复制到临时目录。

```bash
# 核对实际依赖后运行；无需远端应用或密钥
OPENBLAS_NUM_THREADS=1 python longevity_new_territories/scripts/source_reanalysis.py
OPENBLAS_NUM_THREADS=1 python longevity_new_territories/scripts/mechanistic_countermodels.py
OPENBLAS_NUM_THREADS=1 python longevity_capacity_timing/pulse_counterexample.py
OPENBLAS_NUM_THREADS=1 python longevity_spatial_access/analyze.py
python longevity_caretaker_selectivity/condition_check.py
python longevity_state_turnover/identifiability_check.py
python longevity_repair_memory/audit_package.py
```

首包依赖见其requirements；时间/空间用numpy/pandas/scipy/matplotlib；后三区分标准库脚本。source_reanalysis只读预定源表片段，不遍历Figure7D百万行。失败下载响应不当xlsx；eLife网页壳问题已通过API图注/Methods解决，无需重走死路。

原工作台软件单元测试可选择`python longevity_research_workbench/tools/run_validation.py --unit-only`；它不验医学。完整run_validation会写回执并递归查本地链接；移动布局前不要假称跨机器全通过。旧verify_history预期会看到已授权修改/归档缺失，**不能刷新基线使其变绿**。

## 8｜工作区清理与恢复

已删除的8个展开目录：`corpus_engine_v1`至`v6`、`longevity_frontiers_round3`、`longevity_frontiers_round4`；共541文件，均在删除前逐SHA确认保留ZIP含相同字节。精确恢复映射见[WORKSPACE_CLEANUP_RECEIPT.json](WORKSPACE_CLEANUP_RECEIPT.json)，说明见[WORKSPACE_STORAGE_NOTE.md](WORKSPACE_STORAGE_NOTE.md)。

恢复按每条`archive/member/path/sha256`映射，不能假设某目录都对应一个ZIP根；只恢复确需文件，不全量展开。唯一源文件、uploads和历史ZIP未删除。旧对话展开链接失效不是数据损失，但要有相应ZIP才能在新机器恢复。

## 9｜下一SESSION可直接使用的接续请求

> 先读取HANDOFF.md和SESSION_UPDATE_RECEIPT.json，检查我连接的真实GitHub仓库/分支及文件结构。对照当前V6/V7与工作台同名副本、P1/P2/P3协议，不另建同题新稿或完整V8。先给出差异和权威路径，再进行授权范围内更新。研究继续采用“新探索优先、旧债只做关键项”，保留真实源表/人工反例/假说及外审边界，不新建HTML、不重跑历史builder或刷新旧信任基线。下一窄问题是恢复后记忆编辑能否降低异常克隆增长同时保留再修复；没有真实数据或独立评审就不宣称验证完成。

## 10｜收束验收口径

本次验证：21个现有文件的修改记录、V6/V7副本一致、原章保留与新增章节存在、现有链接、当前manifest、冻结ZIP/旧信任基线未改、增量包成员字节及CRC。结果见回执与最终答复。**这是交接/工程自查，不是独立外审或科学认证。**
