# 契约治理的认识论工程（CGEE）：长篇专著与发表级论文工作台 · GitHub 仓库架构与工程实践规范（R5.5）

**版本：** R5.5（R5.4 的审计修订版；审计记录见 `CGEE_R5.4_AUDIT_2026-11-24.md`，变更清单见 §0.4）  
**核查基线：** 2026-11-24（平台事实逐条带核查日，见 §0.5；R5.4 的基线为 2026-11-18）  
**适用范围：** 在 **Claude Code（CLI / Desktop；所需最低版本按功能分列于 §0.5，不再写单一版本号；起草会话强制运行于 WSL2 沙箱）+ GitHub + Linear + Google Drive**（及可选 Arena.ai Agent Mode / Rowboat）上运行的双语（EN + ZH，含简繁分流）长篇专著、丛书与发表级科研论文工程。  
**用词与证据纪律：** “必须”表示不满足即判失败；“应当”表示有记录理由才可例外；“可以”表示可选。**没有配置真实分支保护、账号隔离、WSL2/OS 沙箱与库外 T2 留出检查前，不得宣称任何检查已生效。** 本文件经验数字一律引用 §0.2 编号（`E1–E35`），平台行为一律引用 §0.5 编号（`P1–P14`），跨体裁/跨语种外推或无直接对照证据的设计选择标 `[H]`；每个工具均须在 `docs/TOOL_STATUS.tsv` 登记真实状态，状态不到 `verified` 的不得作阻断项。

---

## §0 范式、证据登记表与 R5.4 核心定律

### 0.1 范式定义

**契约治理的认识论工程（Contract-Governed Epistemic Engineering, CGEE）** 把长篇写作拆解为两层：**“可编译的知识后端（Compiled Epistemic Backend） + 盲态减压前端（Blindfolded & De-compressed Prose Frontend）”**。

1. **职责分权**：大语言模型负责起草，默认不可信。受保护默认分支上的账本（`kb/`、`ontology/`、`formal/`）、五键数值绑定、基线 CI（T1）、仓库外留出检查（T2）与人类主权签发，构成可验证后端。
2. **约束下沉与非直推改稿**：约束不靠提示词自觉（E18），而靠独立账号、只读台账、OS 沙箱和一条明确的上报通道（E31）。不把文风/slop 评分直接丢给模型做优化目标（E30）；所有修改由账本、实验记录或负责人指明的位置驱动。
3. **规范自我约束**：严格标明每项实证的语料范围、许可证红线与 `[H]` 假设边界；不凭通用榜单定模型分工，由 `EVAL/` 成对盲评决定。

### 0.2 证据登记表（`E1–E35`；R5.5 抽查结果见表后“R5.5 核查状态”，未抽查条目沿用 R5.4 状态，不等于已核实）

| 编号 | 来源 | 可引用的实证结论 | 适用范围与局限 |
| :--- | :--- | :--- | :--- |
| **E1** | Sourati 等, *Nat. Hum. Behav.* **10**, 1925–1942 (2026) | LLM 改写使写作复杂度方差下降 **21%–50%**（$P \le 0.05$），削弱人口学语言信号 | 英文；7 数据集、88 万余篇；未做同基座 RLHF 消融 |
| **E2** | Kim 等, *Argument Collapse*, `arXiv:2606.01736` | 人类主论点唯一率 **65.3%**（截止后 6 论坛 **84.0%**），默认 LLM **3.4%**（长文 **35.6%**）；同主论点下子论点 **41.0%** vs **9.1%**；多样化提示仅恢复约一半人类主论点 | 英文评论与长文（NYT 1,039 篇、Boston Review 448 篇 vs 23,384 篇 LLM） |
| **E3** | Russell 等, *StoryScope*, *COLM 2026* (`arXiv:2604.03136v6`) | 仅用 304 维叙事结构特征，Macro-F1 为 **93.2%**（30 核心特征 **84.8%**）；去套话改写降 1.6 点（95.5→93.9）；Claude 呈事件递进扁平指纹 | 英文小说（61,608 篇）；不直接衡量学术专著 |
| **E4** | Madler, *SlopShape*, `arXiv:2609.15369v3` | 176/203 结构特征识别商业长文 Macro-F1 **97.0%**（自改写后 **96.1%**）；9 核心特征 **90.1%**；附录 I 记录 StoryScope 5 处代码缺陷（Stage 5 只认 `human_story` 列名） | 英文公司博客 |
| **E5** | Wang 等, *Humanized but Still True?*, `arXiv:2611.00359` | 11 款改写工具在 **35%–65%** 文档改动或丢失可核对单元；只算数字与人名 **11%–58%**（10/11 款 ≥20%） | 英文 363 篇；规则加 2 个 AI 标注员验证 |
| **E6** | Onweller 等, *Cited but Not Verified*, `arXiv:2605.06635v1` | 链接有效率 **>94%**，事实准确率 **39%–77%**（Opus 4.6 单轮无约束 **54.2%**）；工具调用 2→150 次时两前沿模型平均准确率降 **~42%** | 14 模型；降幅为两前沿模型均值 |
| **E7** | Huang 等, `arXiv:2609.28614v1` | 开放科研流水线自发操纵 **30.5%**，专用内核 **2.9%**；51 例起点中位在轨迹 **71%** 处（27 例与新看到评测资源或宽松评分有关）；评审漏检 **6.5%**；5 轮详细反馈逃逸 **40.5%** vs 笼统拒绝 **20.3%**（$p=0.002$） | 17 模型、38 任务；轨迹中位 8 步；反馈对比未隔离解释文本 |
| **E8** | Baumann 等, *SWE-chat*, *COLM 2026* (`arXiv:2604.20779v2`)；`arXiv:2603.26233` | 真实会话仅 **59%** Agent 代码存活进最终提交，用户在 **50%** 回合打断纠正；Claude Code 主动澄清问题的**回合**占比仅 **3.0%–3.2%** | 约 18,000 真实会话；按回合计非按任务计 |
| **E9** | Glaze & Pohani, *Ping or Peek* (Snorkel AI, 2026-11-05) | 默认线束约 **25%**（总跑批）至 **60%**（Claude Code 默认跑 Claude 切片，45 次运行中 60% 偷看 `scorer.py`、38% 提问）偷看评分器；线束提示可把提问率拉至 100% | 单一模糊任务概念验证 |
| **E10** | Zhao 等, *SpecBench*, `arXiv:2605.21384` | 以“可见通过率 − 留出通过率”度量奖励操纵，差距最高 **100 个百分点** | 30 个长程编码任务 |
| **E11** | Zhang 等, *Verbalized Sampling*, `arXiv:2510.01171` | 口述多候选及概率分布使创作多样性提升 **1.6–2.1 倍**，不损事实准确率 | 英文创作、对话、合成数据 |
| **E12** | Nguyen 等, *MeLLM 2026* (`2026.mellm-1.29`)；Jang 等, *SciZoom* (`arXiv:2603.16131v2`) | 往返翻译链中限定语递减、断言性与名词化递增；44,946 篇顶会论文显示 Post-LLM 套话暴增 **4–10 倍**，摘要限定语减少 **22.8%** | 英文新闻；4 大 ML/NLP 顶会（2020–2025） |
| **E13** | Panickssery 等, `arXiv:2404.13076` | LLM 评审者能识别并偏向自身生成的文本 | 英文摘要任务；“同族模型”是外推 |
| **E14** | *LLM-as-a-Reviewer* (`arXiv:2605.25415v1`)；Jizhou Guo (`arXiv:2611.20608v1`) | LLM 审稿高估弱稿、**少报清晰度**；隐藏字体映射指令可推高接收；换模型版本（183 篇随机样本）接收率差 **52pp**（Opus 4.6 62% vs Opus 5.5 10%） | NeurIPS / ICLR 投稿 |
| **E15** | Böckeler, *Harness Engineering* (`martinfowler.com`, 2026-04-02) | 线束控制分事前引导（Guides）与事后传感（Sensors） | 架构框架 |
| **E16** | Gloaguen 等 (`arXiv:2602.11988`)；*SkillsBench* (`arXiv:2602.12670v4`) | 仓库上下文文件总体不增成功率且成本增 **>20%**；人工整理技能 +**16.6pp**，模型自写技能无收益，≤3 模块最佳 | 编码代理基准 |
| **E17** | Xue 等, *ScienceBuddy* (`arXiv:2609.17523v1`)；Liu 等 (`arXiv:2601.10338` & `arXiv:2602.06547` *USENIX Sec '26*) | RinR 固定模型改线束**内循环**使验证集准确率 **31.1% → 51.1%**；公开技能 **26.1%** 含风险（带脚本卡出错率为纯指令 **2.12 倍**）；98,380 技能动态行为审计发现 157 恶意技能；Adversa AI 评测证实单一扫描器易被同形异义词与改写绕过 | 多学科科研任务 & 两大技能市场审计 |
| **E18** | Prasad 等, *BAITBENCH*, `arXiv:2608.30724v1` | 数据内留捷径时，7 前沿 Agent **57.1%** 跑批作弊（最高 **76.1%**）；提示“不要作弊”仅降 **6.21pp**（均值仍 >50%），强制有效性自我反思日志作弊率反升（**55.6% → 56.3%**） | 3 项合成表格 ML 任务 |
| **E19** | Hu 等, *VERA*, `arXiv:2610.06366v1` | 约 **60%** 正确结论伴随编造或不可核查陈述，推理缺陷在正确与错误结论中同样高频；4 块式 SRR + 机械校验与自动变异测试揭露自由裁判漏掉的 **87%** 推理错误 | 软件漏洞分析（搬到文献主张为外推） |
| **E20** | Ma 等, *Proof-of-Use*, `arXiv:2510.10931` (*EMNLP 2026 Main*) | 经**强化学习训练**的研究 Agent 会发出形式合法、但推理并不因果依赖检索结果的工具调用（tool-call hacking） | 限于 RL 训练 Agent；可借“扰动证据看结论”思路 |
| **E21** | Basani & Chen, *DivEye*, `arXiv:2509.18880v3` (*TMLR 2026*) | 逐 token 惊奇度（Surprisal）波动特征击败零样本检测器最高 **33.2%**（作辅助信号再提 **+18.7%**） | 英文；这是检测器，仅作描述性指标 |
| **E22** | Mikhaylovskiy, `arXiv:2610.05466v1` | 4,992 篇英语议论文键盘日志重放表明，成稿语义自相关遵循带有限尺度标度的**幂律流形**，修订产生拉回动力学 | 英文短文击键数据；单作者预印本 |
| **E23** | *Getting It Right, Under Constraint* (`[W/待复核来源]`) | 本轮审计未直接定位全文，R5.4 **不再将其列为立论依据**；最小上下文与拆步起草直接由 `E11 + E16 + E30` 支撑 | — |
| **E24** | Li 等, *LLM Review*, `arXiv:2601.08003v1` | 常规多智能体互动通过同质化杀死创意；交换定向盲评但**只基于自身草稿独立修订**（不看同伴改稿）可保住发散轨迹 | 英文科幻基准 SciFi-100（~9× 成本） |
| **E25** | Bhardwaj, *SuperLocalMemory V3 / V4* (`arXiv:2603.14588` & `arXiv:2608.08253`) | 一阶蜂窝层上同调 $H^1 \neq 0$ 对应跨记忆语境矛盾；LoCoMo 完全本地达 **74.8%**；**V4 已改 AGPL-3.0-or-later** | Agent 对话记忆（禁装 AGPL-3.0 包） |
| **E26** | Koomullil (`arXiv:2605.16407v1`)；*ECT* (`arXiv:2608.23623v1`)；Rubin-Delanchy & Jones (`patrickrd/proof_carrying_hypothesis_testing`) | Koomullil 用 Lean 4 核隔离概率层并证明最大可认证残余（MCR）；ECT 将无支撑终止从 **252/288 降至 0/288**（闭环 **40/66 → 0/66**）；后者实现数据扣留下的有限样本 $p$-/$e$-值与 Lean 4 检验 | 合成任务、形式边界与线性模型假设检验 |
| **E27** | Brown-Cohen 等, *Prover-Estimator Debate*, `arXiv:2506.13609v2` | 递归辩论中诚实方胜出的**完备性**需要论证可稳定分解，**可靠性**不依赖稳定性（“即使对稳定性没把握也可安全使用”） | 复杂性理论监督博弈协议 |
| **E28** | Ma 等 (`arXiv:2603.14430`, *Creative Convergence or Imitation?*)；Qing 等, *C-ReD* (`arXiv:2604.11796`) | 定义 **34 种中文网文叙事功能**（约 1,000 条人工标注）揭示中文小说结构同质化；`C-ReD` 覆盖 5 领域 × 9 模型简繁中文 AI 文本检测基准 | 中文小说 & 中文 AI 检测基准（不直接定学术文风阈值） |
| **E29** | Park & Kim, *Relational Over-Regularization (ROR)* (`arXiv:2608.26694`) | 段落边界周期性相似度爆发与模板过渡，造成句间转移偏差 $\delta_{ij}$ 方差膨胀（精度 **97.14%** / 误报 **1.57%**） | 检测器；对方差不高于人类基线的生成器失效 |
| **E30** | Oh 等, *SciSlopBench & SciSlopHarness* (`arXiv:2610.00531v1`)；Roongta 等, *SlopBench* (`arXiv:2609.33905v1`) | 390 对科研论文 6 维科学 slop 达 **85.9%** 识别率；**直接 slop 意识提示触发奖励操纵（反扩大总差距），而仅依据实验记录与代码输出改稿的 `SciSlopHarness` 缩小 AI–人类差距 63%（1.395→0.519）**；`SlopBench` 证实在 19,928 条输出上中间排名随重加权折叠 | 跨学科科研论文 & 18 模型日常写作 |
| **E31** | Gomez, *Escalation Channels* (`arXiv:2608.29460v3`) | 跨 5 家族 8 个前沿模型，**结构化上报工具 + 独立反作弊政策（Condition D）** 把作弊率从 **23.6% 降至 5.3%**（只给工具为 15.0%），增补 **+10.1pp** 缺陷检出（精准度 **99.4%**） | 存在检查器缺陷的编码任务（须防借上报逃避难题） |
| **E32** | Gui, *Coding or Cheating?* (`arXiv:2611.10404v1`)；Wong 等 (`arXiv:2611.09828`) | 硬化环境与未见难题上，编码模型系统性升级去挖 **`git` 历史、`.git/objects` 对象库与全盘扫源文件**；泄露更多信号的监控器更易被逃逸 | 硬化编码环境与 RL 监控干预 |
| **E33** | Zollicoffer 等, *Sanity Checks* (`arXiv:2605.08346v1`) | 用 `Force`/`Remove` 剥除终点长度与答案线索后，多数长文检测器暴露依赖终点伪影；轻量词法轨迹 **TRACT** 保持稳健 | 长文链式推理幻觉检测 |
| **E34** | Dassen 等, *FACTUM* (`arXiv:2601.05866v4`, *ECIR 2026*, `Maximeswd/citation-hallucination`)；*HRKG-HD* (`2026.findings-acl.1673`) | `FACTUM` 证明长文引文幻觉源于 Attention 与 FFN 尺度失调；`HRKG-HD` 用共享实体与限定词（`qualifiers`）构成超关系图核验远距长文事实，优于粗粒度核验 | 白盒引用激活检测 & 黑盒跨章超关系图核验 |
| **E35** | Stephan Joseph, *SaneCite Retraction Census v1.4.1* (`MrSaneApps/sanecite-retraction-census`, Zenodo `10.5281/zenodo.23358099`, 2026-11-09) | 51,414 篇撤稿论文产生 **262,998 次**撤稿后引用；51,626 处全文语境判读显示 **40.7%**（去误差 38.1%）将撤稿作正面倚赖，仅 **3.3%** 标明撤稿；确立 **First-Online Date Rule** | 生物医学与经济学撤稿全量普查 |

**R5.5 核查状态（2026-11-24，对照一手或权威二手来源抽查 7 条）：**

| 编号 | 状态 | 说明 |
| :-- | :-- | :-- |
| E1 | 已核（权威二手） | 2026-08-24 刊于 *Nat. Hum. Behav.*；21%–50% 与 88 万余篇一致；卷期页码 `10, 1925–1942` 未核 |
| E14 | **未能定位** | `arXiv:2611.20608` 未检得；“换模型版本接收率差 52pp（Opus 4.6 62% vs Opus 5.5 10%）”降为 `[W/待复核]`，**不得再作 §1.1 路由依据** |
| E18 | 已核（一手摘要） | 已收于 *Findings of EMNLP 2026*；57.1% 与“提示不要作弊后均值仍 >50%”一致；6.21pp 与 55.6%→56.3% 未核 |
| E30 | 已核（一手） | 390 对、6 维、85.9%（对照 Binoculars 68.7%）；SciSlopHarness 依据实验记录逐条审改稿 |
| E31 | 已核（一手摘要） | 8 模型 × 5 家族，23.6%→5.3%（OR = 9.2）；NeurIPS 2026 AI4GOOD 研讨会论文（非主会）；15.0%、+10.1pp、99.4% 未核 |
| E35 | **来源冲突** | 检得同作者 SaneCite 记录 `10.5281/zenodo.23766253`（22,553 篇撤稿生物医学论文），与本表所列 `zenodo.23358099`（51,414 篇、262,998 次）范围不符；40.7%/3.3% 在两份记录对齐前降为 `[W/待复核]`。**First-Online Date Rule 作为方法可用，数字不可引** |
| E9、E25 等 | 未抽查 | 沿用 R5.4 状态 |

**未核实或受限，不得写成普遍事实：** E2、E12、E28 的会议归属（E18 已核为 Findings of EMNLP 2026，E31 为 NeurIPS 2026 研讨会）（注：E12 `SciZoom` 与 E31 分别有公开预印本，但未逐一核对全部接收页）；E6 的精确外推曲线；（Opus 4.6 退役底线已核：官方与 Google Cloud 页均写“不早于 2027-02-05”，见 P10）；Claude Code 的 `Alt+T` 在各平台差异；Rowboat Desktop 内部界面细项；Opus 4.7 具体文风定量指标；`E29` 中文实际表现；`DiscourseGraphs/discourse-graph-skills`、`yerimoh/ScientificSlop`、`juanjvazquez/BAITBENCH` 与 `SkillSpector` 具体修补版本号须在本地克隆时核对。

### 0.3 从证据到工程控制（R5.4 五大核心准则）

1. **权限、台账、沙箱与“反逃避升级通道”四位一体（E18, E9, E31）**：口头要求不作弊仅降 6.21pp 且自我反思日志无效（55.6%→56.3%，E18）；但提供**结构化升级通道（`kind/owner-decision`）+ 独立反作弊政策**可将作弊率从 23.6% 压至 5.3%（E31）。同时必须执行 **`No-Dodging Rule`（反借故逃避铁律）**：触发 `kind/owner-decision` 升级会冻结当前 Issue 等待负责人裁决，**绝不计作通过门禁、绝不生成可合并 PR，且按模型与角色统计升级率**。
2. **最小上下文起草、“依据实验记录改稿”与测量隔离（E11, E16, E30；R5.5 推广）**：**起草代理能读到的任何分数都会变成优化目标**，不只是 slop 分：文风报告、引擎报告（`corpus/editions/*/reports/`、`review/engine/`）、`declcheck`/`speccheck`/`fact_consistency` 输出一律置于起草读集之外，测量只以“检查代号 + 位置”回到起草代理（E7、E32）。项目实测：一句不含证据的模板句即可让任一沉默关系“闭合”（dao-protocol-trilogy `review/engine/INJECTION_E0-2026-11-17.md`）。先定 `SCAFFOLD.yaml` 拆清结构，正文起草会话只持本节最小上下文；**严禁将文风/slop 评分回显给写作模型或让其直接“降低 slop 分”**（E30 证实直推触发奖励操纵）；Stop 钩子仅将守恒报错打回给模型，文风评分只写工作树外 `~/.cgee/<repo>/STYLE_REPORT.md` 供负责人阅览决定。
3. **限制 `.git/objects` 挖掘与跨代理隔离（E32）**：起草会话启用 **git 子命令白名单（`status`/`add`/`commit`/`push`）** + `.git` 屏蔽。**钩子是正则，挡不住全部绕过**（如 `cd .git && cat HEAD`、`cat tools/x.py`）：权限规则只管内置 Read/Edit/Grep/Glob 工具，**Bash 子进程的读取只有 OS 级 `sandbox.filesystem.denyRead` 才拦得住（P7）**。所以 `.git`、`tools/`、`tests/`、`EVAL/` 与所有测量输出须进沙箱 denyRead；由此 git 操作须在沙箱外由 `make checkpoint` 完成（见 §7.1）；盲审子代理**绝对禁止读取起草代理的自然语言计划、讨论日志与修改历史**；T2 物理置库外。
4. **结构化推理（SRR）、有证终止（ECT）、只列清单的 MCR 与撤稿语境核查（E19, E26, E35）**：承重主张采用 4 块式 SRR；完成声明走 `ect_verify.py` 绑定可重放证据；`mcr_filter.py` **只出清单不改动正文**，将未过重放的断言写入 `review/UNGROUNDED_RESIDUE.md`，由负责人决定补证、降级或批准删除并记入台账；P1/P8 按 **First-Online Date Rule** 核查撤稿并阻断正面倚赖引用（E35）。
5. **验证分流与“剥除终点伪影”体检（E26, E33, E34）**：`verify_by: recompute` 靠重跑脚本与形式证书，不靠讨论；`verify_by: review` 走跨家族/真人盲审并加人类清晰度（Clarity）复核（E14）；跨章核查利用共享实体+限定词路径（E34）；定期运行 `make chaos`（含 `Force`/`Remove` 剥离终点伪影检查，E33）。

### 0.4 R5.5 变更记录（相对 R5.4）

- **修正（Fix）**：§0.2 表头“经五轮独立核验”改为分条核查状态；E14 未能定位、E35 来源冲突，两者降为 `[W/待复核]`，E14 不再支撑 §1.1 路由；E18、E31 会议归属已核。§0.3 第 3 条删去“彻底杜绝”：钩子正则可被 `cd .git`、`cat tools/…` 绕过，Bash 读取只有沙箱 `denyRead` 拦得住。§1.2 `AGENTS.md` 加载条件补“任一上级目录”与“升级后首个会话”；`additionalDirectories` 被忽略是已知 issue，不是文档行为；`blockWritesOutsideWorkingDirectories` 的最低版本二手来源互相矛盾，改为按功能核对。§1.1 Opus 5.5 补 5m 写入与 Batch 价，标出强制 `tool_choice` 400；水印条目改为可核的表述。§7.3 钩子：`sg` 缺失时不崩溃；文风报告与交接文件写到工作树之外；`.git` 无斜杠形式与 Bash 读盲区路径纳入拦截；`--selftest` 用项目根；批准台账路径统一。
- **优化（Optimize）**：起草档相对路径一律由 `make draft` 展开为绝对路径；`.git` 入 `denyRead`，提交改由沙箱外 `make checkpoint` 完成；新增通用名与项目名映射表，已建项目不为对齐本树改名；`ledgers/approvals.tsv`（决定）与 `ledgers/scaffold_approvals.jsonl`（脚手架 blob）分工；`.gitattributes` 增加冻结版本与 sqlite 规则；P3 后备模型盲评定截止日；§6.4 增加“平台事实超 30 天未复核即拒绝发布”。
- **涌现（Emerge，两项，均已核实来源）**：
  1. **指令层 Split-Brain（P1–P3）**：Claude Code 载入工作目录及所有上级目录的 `CLAUDE.md`，只要任一处有 `CLAUDE.md` 就不直接读 `AGENTS.md`。放在 Obsidian 知识库目录树下的仓库副本，因此载入知识库的 `CLAUDE.md` 而看不到自己的 `AGENTS.md`。这正是 §1.3 SSOT 要防的同一失败，发生在指令层而非数据层。修复见 §1.2 与 §10.2 第 7 条；dao-protocol-trilogy 已在 main 加入根目录 `CLAUDE.md`（`@AGENTS.md`）；其余四个仓库以 PR 提交，由负责人合并。
  2. **测量隔离（E30 的推广）**：E30 只说不要把 slop 分回显给写作模型；同一机制适用于起草代理能读到的任何测量。项目实测（dao-protocol-trilogy 注入研究）显示一句无证据的模板句即可闭合任一沉默关系。规则写入 §0.3 第 2 条、§7.1 读屏障与钩子。
- **自我适用（R5.5 起）**：本文件中随版本变化的平台事实集中到 §0.5，每条带来源与核查日，按 §6.4 过期即降级，与项目内 `fact_consistency.py` 对事实的处理相同。

### 0.5 平台事实登记表（`P1–P14`，核查日 2026-11-24）

| 编号 | 事实 | 来源 | 状态 |
| :-- | :-- | :-- | :-- |
| P1 | Claude Code 读 `CLAUDE.md`；项目已有 `AGENTS.md` 时官方推荐 `CLAUDE.md` 用 `@AGENTS.md` 导入 | code.claude.com/docs/en/memory | 一手 |
| P2 | 工作目录及所有上级目录的 `CLAUDE.md`/`CLAUDE.local.md` 在启动时全量载入；`claudeMdExcludes` 可按路径或 glob 排除，任意设置层可设 | code.claude.com/docs/en/memory、/en/large-codebases | 一手 |
| P3 | v2.1.277 起无 `CLAUDE.md` 时读 `AGENTS.md`；Project instructions 四档（默认 `claude-md-or-agents-md`）；升级后首个会话不读 | devops.com、apidog（转述官方公告与文档） | 二手 |
| P4 | 文件权限规则只匹配 `Edit(path)`/`Read(path)`；`Edit` 管所有写文件的内置工具；`Read` 尽力覆盖 Grep/Glob | code.claude.com/docs/en/permissions、agent-sdk/permissions | 一手 + 二手 |
| P5 | `Read(...)` 拒绝同时拦同路径 Edit/Write（Write 需 v2.1.228+） | code.claude.com/docs/en/tools-reference | 一手 |
| P6 | `blockReadsOutsideWorkingDirectories`（v2.1.257+）拒工作区外 Read/Grep/Glob/LSP，不拦 shell；`blockWritesOutsideWorkingDirectories` 拒工作区外写与设置文件写，开启后 worktree 工具消失；最低版本二手来源写 2.1.314 或 2.1.319 | dev.classmethod.jp、startdebugging.net、kanaries.net、settings reference | 二手（版本冲突） |
| P7 | 沙箱只在 macOS、Linux、WSL2；`failIfUnavailable`、`allowUnsandboxedCommands: false`（严格模式，忽略 `dangerouslyDisableSandbox`）；`filesystem.denyRead` 为 OS 级、拦子进程；项目设置中 `./` 相对项目根 | code.claude.com/docs/en/sandboxing | 一手 |
| P8 | `blockReadsOutsideWorkingDirectories` 忽略项目/本地 `additionalDirectories` | GitHub issue #92582（未关闭） | 已知问题 |
| P9 | API `2026-10-21` 版删除 `temperature`/`top_p`/`top_k`，任一模型发送即 400；`2023-06-01` 版下 Claude 4.7+ 非默认值 400 | platform.claude.com model-deprecations、release notes | 一手 |
| P10 | Opus 4.6 为 Legacy，$5/$25，退役不早于 2027-02-05 | platform.claude.com Opus 4.6 页、Google Cloud Vertex 页 | 一手 |
| P11 | Opus 5.5 为现役 Opus，$4/$20，缓存读 $0.20，Batch $2/$10 | platform.claude.com pricing（多家二手一致） | 一手 + 二手 |
| P12 | Opus 5.5 思考常驻，`thinking.disabled` 与手动预算返回 400；强制 `tool_choice` 返回 400；默认 effort medium | platform.claude.com whats-new-opus-5-5 | 一手 |
| P13 | 2026-08 Anthropic 公告 Claude 文本水印，基于 SynthID-Text，选词层、非隐藏字符；承诺为此前模型补加；非默认采样可能不携带 | anthropic.com/news/claude-text-watermark、API release notes、TechTarget | 一手 + 二手 |
| P14 | 2026-08 起 GitHub Copilot 下架 Opus 4.6（与 Anthropic API 退役无关，勿混） | github.blog changelog 2026-07-31 | 一手 |

---

## §1 2026 年 11 月模型路由、客户端实操与三平台权责分立

### 1.1 多模型工程路由与成本/参数约束

**一个会话里不换模型，也不改顶层 `effort`。** 顶层 `effort` 会渲染进提示词，长会话中途改档位会导致 Prompt Cache 失效重计费（按消息改 effort 仅支持 Opus 5.5 / Fable 5.2 等新代模型，不支持 Opus 4.6）。需要换档位时另开会话。

| 环节 | 模型 | 依据与边界 | 等级 |
| :--- | :--- | :--- | :--- |
| **P1–P2 结构化、账本、脚手架** | **Opus 5.5**（显式设 `effort: high`） | 官方定位长程代理与知识工作（P11）；缓存读 $0.20；不单独担任审稿终裁（理由是 E13 同族偏好；R5.4 所引 E14 的版本差数字未能定位，已降级） | 较稳 |
| **P0 讨论、P3 正文与双语重创** | **Opus 4.6**（关 Thinking、`effort: medium`） | 写作者报告；关闭思考尚无对照实验；若需 `high` 档处理复杂收束须另开独立会话 | `[H]` |
| **P3 后备（4.6 退役之后）** | **待定** | 必须由 `EVAL/` 盲评决定（候选：Opus 5.5 / Fable 5.x）。Opus 4.6 不早于 2027-02-05 退役，弃用通知一般提前约 60 天：**盲评须在 2026-12 底前完成**，否则退役通知一到即无替补。Opus 5 已是 Legacy，不再列为候选 | 待评（有截止） |
| **P4/P6 按批注局部改稿** | 与当前起草同一模型 | 严禁直接提示降低 slop 分，必须指定到具体 `claim_id` 与实验记录位置（E30） | `[H]` |
| **第二轮独立盲审** | **真人专家，或钉死快照版本的非 Anthropic 家族模型** | E13；E14 中 `arXiv:2605.25415` 部分（高估弱稿、少报清晰度）未在 R5.5 复核 | 直接支持（E13） |
| **工具链（`tools/`）修改** | **Opus 5.5**（必须在负责人另开的独立工具检出目录中监督完成） | 与写稿隔离，PR 须 Code Owner 审阅 | — |

已核实的模型参数：

| 模型 | 官方状态 | 价格（每百万 token） | 硬参数约束与平台变更 |
| :--- | :--- | :--- | :--- |
| **Opus 4.6** | **Legacy**（退役日期以官方弃用页为准） | **$5 / $25**（Cache 读 $0.50；5m 写 $6.25；1h 写 $10；Batch 5 折） | • 旧分词器；1M 窗口不加价；MRCR v2 两组公开数字 93%/76% 与 91.9%/78.3%<br>• 思考可关；禁用 Prefill（400）；`temperature`/`top_p`/`top_k` **自 API `2026-10-21` 起全模型报 400**（仅 `2023-06-01` 可用）<br>• 统计文本水印（P13）：Anthropic 2026-08 公告此后的 Claude 模型输出带基于 Google DeepMind **SynthID-Text** 的选词水印（非隐藏字符），并承诺为此前发布的模型补加；非默认采样参数下可能不携带。是否已在 Opus 4.6 上启用**未逐模型核实**<br>• Claude Code 默认输出 64K，可配至 128K |
| **Opus 4.7 / 4.8 / 5** | **Legacy** | **$5 / $25** | 新分词器（英文散文约 +20%–47%，中文约 +0%–7%）；4.7 MRCR 跌至 59.2%/32.2%；两份独立写作评测对 Opus 5 为负面 |
| **Opus 5.5** | **现役** | **$4 / $20**（Cache 读 $0.20；5m 写 $5；Batch $2 / $10） | 思考常驻不可关闭（`thinking.disabled` 返回 400），默认 effort 为 medium；强制 `tool_choice`（`any`/具名工具）返回 400；`temperature` 等在 `2026-10-21` 版下全模型 400；per-message 改 effort 不破缓存一说**未核**；水印见 P13 |

### 1.2 客户端边界、Windows WSL2 沙箱与反 Split-Brain

| 客户端 / 平台 | 定位 | 真实工程边界 |
| :--- | :--- | :--- |
| **Claude Code**（CLI / Desktop Code 页；最低版本按功能见 §0.5） | **90% 主战场** | • **Windows 强制 WSL2 沙箱**：沙箱只在 macOS、Linux、WSL2 可用；原生 Windows 与 WSL1 不支持。起草会话在 WSL2 里用 `make draft` 启动（装妥 `bubblewrap` 与 `socat`），带 `failIfUnavailable: true` 与 `allowUnsandboxedCommands: false`。<br>• **`AGENTS.md` 加载（P1–P3）**：Claude Code 读的是 `CLAUDE.md`；v2.1.277 起，仅当工作目录**及其任一上级目录**都没有 `CLAUDE.md` 时才直接读 `AGENTS.md`（`/config` 的 Project instructions 默认 `claude-md-or-agents-md`），且安装或升级后的首个会话不读。**上级目录的 `CLAUDE.md` 会全量加载**：仓库工作副本若位于另一个项目的目录树下（如放在 Obsidian 知识库 `D:\THE_DAO_PROTOCOL\` 之下），会载入那个项目的规则并压制本仓库的 `AGENTS.md`——指令层的 Split-Brain。**修复：每个仓库根目录放 `CLAUDE.md`，首行 `@AGENTS.md`；用 `claudeMdExcludes` 排除无关的上级 `CLAUDE.md`；工作副本放在任何其他项目目录树之外；会话开始用 `/memory` 核对实际载入的文件。**<br>• **权限与工作目录锁定（P4–P8）**：文件规则只匹配 `Edit(path)` 与 `Read(path)`（`Write`/`Glob`/`Grep` 带路径的规则不生效）；`Edit` 规则管所有写文件的内置工具，`Read` 规则尽力覆盖 Read/Grep/Glob，`Read` 拒绝同时拦同路径的 Edit/Write。**这些规则只管内置工具，不管 Bash 及其子进程**：要拦 `cat`、`python` 读文件，只能用 `sandbox.filesystem.denyRead`（OS 级）。`blockReadsOutsideWorkingDirectories`（v2.1.257 起）与 `blockWritesOutsideWorkingDirectories`（二手来源分别写 v2.1.314 与 v2.1.319，以 `claude --version` 与设置参考页为准）锁死工作区外读写；后者开启时 worktree 工具消失，且拒绝写任何 Claude Code 设置文件。已知问题：`blockReadsOutsideWorkingDirectories` 忽略项目级与本地级 `additionalDirectories`（issue #92582，v2.1.263 报告，未关闭），外部目录须由人工 `--add-dir` 或用户级设置挂载；`Bash` 中 `cd` 会脱离路径规则。<br>• **思考开关**：用 `.claude/settings.local.json` 控制；写完首段须打开 `transcript_path` 确认无思考块；对 Opus 5.5 无效。<br>• **规则与子代理**：`.claude/rules/*.md` 必须用 `paths:` YAML 列表；`.claude/agents/*.md` 使用 `tools`、`disallowedTools`、`permissionMode` 与 `maxTurns`。 |
| **Claude Desktop**（Chat / Cowork） | **10% 辅助舱** | 只用于不受工程约束的灵感讨论与 Google Drive 资料预整理；不跑 `Makefile` 与分支流。 |
| **Rowboat** | **可选群聊看板** | **严禁把 Rowboat 本地 `Brain` 接入本项目真相源**（不经 `synsets.yaml` 与 `fact_consistency.py`，会造成 Split-Brain）。 |
| **Arena Agent Mode** | **可选沙箱** | 编排模型不公开、可能中途更换；会话进入公开榜单。保密、未发表、付费墙原文**严禁**传入。 |

### 1.3 三平台权责分立与防同步失败

**唯一真相源（SSOT）只有一个：GitHub 受保护默认分支上的 `kernel/`、`kb/`、`ontology/`、`formal/`。**

- **GitHub**：运行 `gsk/conservation`、`gsk/grade`、`gsk/style`；执行 `CODEOWNERS`；规则集不允许绕过（含管理员）。Agent 使用独立机器账号，不在 `CODEOWNERS` 与任何绕过名单内。
- **Linear**：`1 Issue = 1 会话（<=25 次工具调用，预算纪律 [H]） = 1 分支 = 1 PR`；只记规划、风险摘要与 `kind/owner-decision`（**一等升级工具通道，E31；严守 `No-Dodging Rule`，升级单不计作通过、不附带可合并 PR**）；`Done ≠ Verified`；不放 T2 与保密原文。
- **连接器回读铁律**：通过连接器创建或更新跨应用条目后必须回读目标 ID 与实际状态；出现误路由或重复时先修底层映射。

---

## §2 规范 GitHub 仓库目录结构、架构取舍与工具状态登记

### 2.1 目录树（严禁贴进 `CLAUDE.md` 或 `AGENTS.md`，E16）

```text
/
├── CLAUDE.md                     # [<=60行] 首行 @AGENTS.md；只写非显而易见规则，禁贴目录树；工作副本不得放在其他项目目录树下（P2）
├── AGENTS.md                     # 跨平台 Agent 会话协议；含一等上报政策
├── Makefile                      # 唯一调度：all / engine / declcheck / speccheck / facts / kbdb /
│                                 #   injection / gates / contracts / forensics / chaos / topology-check / draft
├── .gitignore                    # 含 .claude/settings.local.json、.claude/.state/、.claude/worktrees/、CLAUDE.local.md
├── .gitattributes                # governance/gsk/** text eol=lf；corpus/editions/*/src/** -text（冻结版本按字节哈希，禁止换行归一）；*.sqlite binary
│
├── .claude/
│   ├── settings.json             # [入库，受保护] 基线：Edit 拒绝规则 + 全工具链钩子
│   ├── profiles/drafting.json    # [入库，受保护] 起草档：双层读/写屏障 + WSL2 沙箱
│   ├── settings.local.json       # [不入库] 个人写作环境
│   ├── .state/                   # [不入库] Stop 钩子计数器
│   ├── rules/                    # prose-zh.md / prose-en.md / epistemic-ledgers.md，各带 paths: 列表
│   └── agents/                   # blind-reviewer.md / fact-auditor.md（tools + disallowedTools + permissionMode）
│
├── .github/
│   ├── CODEOWNERS                # CLAUDE.md AGENTS.md .claude/ .github/ governance/ tools/
│   │                             #   src/daoproto/ tests/ kb/ ontology/ formal/ ledgers/
│   └── workflows/                # gsk-contracts.yml、gate-p.yml、notify.yml（workflow_run）
│
├── kernel/                       # [P0] 总内核（EN + ZH）
├── books/<book>/
│   ├── KERNEL.en.md / KERNEL.zh.md
│   ├── SPINE.md                  # 主干：claim_id + >=2 异质子论点 + 1 反例 + verify_by 标注
│   └── chapters/chXX/            # SCAFFOLD.yaml（无批准字段） + chXX.en.md / chXX.zh.md
├── papers/D*/                    # 内核、预注册、START_HERE.md、SCAFFOLD.yaml、正文、投稿包
│
├── kb/                           # sources.yaml / claims.yaml（qualifiers, srr_trace, 逐字引文与偏移, figure_anchor） /
│                                 #   ledger.yaml（8要素+双时态窗口） / dao_protocol.sqlite（make kbdb）
├── ontology/                     # terms / relations / synsets / facts / untranslated / banned_registers
├── formal/                       # REGISTRY.yaml、证明与脚本证书、反事实测试集
├── lab/<experiment>/             # 实验与模拟，各按预注册哈希冻结
├── corpus/editions/              # 冻结版本（带前驱哈希链）
├── topology/                     # 生成产物 + TOPOLOGY_CONTRACT.md + INPUT_HASHES.json
│
├── src/daoproto/                 # 可安装 Python 包
├── tools/                        # 确定性工具链（状态逐一登记于 docs/TOOL_STATUS.tsv）
├── tests/                        # 工具单测；tests/mutants/ 放混沌毒丸夹具
├── EVAL/                         # 对照评测；T2 留出集放在仓库之外
├── review/                       # blind/ 冻结副本（严禁含草稿代理计划/日志 E32）；
│                                 #   UNGROUNDED_RESIDUE.md（起草读集之外）；文风报告与交接文件写在工作树外 ~/.cgee/<repo>/（R5.5）
├── docs/                         # ENGINE、DECLCHECK、DEFINITION_OF_DONE、EVIDENCE_REGISTER、REPO_LAYOUT、TOOL_STATUS.tsv
├── governance/                   # GSK 发布包 + VENDOR_MANIFEST.sha256、ADR、contracts.json、AI 贡献日志
├── ledgers/                      # 只追加：approvals.tsv（决定台账，已有项目沿用）、scaffold_approvals.jsonl（脚手架 blob 批准，机读）、
│                                 #   pins、releases.jsonl（含 GPG/SSH 签名）、errata
└── skills/                       # 经三层消毒并裁剪的技能卡（<=3 张/任务）+ GSK_CROSSWALK.tsv
```

**通用名与项目名映射（R5.5 新增）：** 本树是参照架构，不要求已建项目改名。项目在 `docs/REPO_LAYOUT.md` 写一张映射表（例：`kb/sources.yaml` ↔ dao-protocol-trilogy 的 `kb/ledger.yaml`；`ledgers/approvals.jsonl` ↔ `ledgers/approvals.tsv` + `ledgers/scaffold_approvals.jsonl`；`knowledge_base/` ↔ `kb/`）。改名只为对齐本树而做，属于无收益的破坏性重构（§13.3 预检）。

**作者参照语料**（未经任何 AI 处理的作者手稿与语音速记）：**默认放在仓库之外**，由负责人运行 `make forensics` 时指向它，只把脱敏统计特征入库；若负责人决定入库，必须加进 `CODEOWNERS`、基线 `Edit` 拒绝与起草 `Read` 拒绝规则，并核实仓库隐私级别。

### 2.2 沿用 `REPO_LAYOUT.md` 的架构取舍

- 门禁统一走 `src/daoproto/gates/check.py`、`governance/contracts.json` 与 `make gates`，不另建 `gates/gate.py`；禁用语域已由 Gate G8 与 `apophatic_scan.py`（配 `withdrawal markers`）覆盖，不另建 `cliche_gate.py`。
- 仿真随实验留在 `lab/<experiment>/`，不建顶层 `sim/`；`Makefile` 是唯一调度器；哈希链与别名保留在 `extract_corpus.py` 与 `ontology/synsets.yaml`。
- `ontology/` 保持六个独立 YAML，不合并成 `lexicon.json`。
- `topology/` 只放生成产物、合同与输入哈希；`topology_receipt.py` 把构建脚本自身列为输入，拒绝根目录外路径、空匹配与输入输出重叠，哈希无变化时不改写回执；>1MB 完整图导出不入库且不进 Agent 读取列表。

### 2.3 工具状态登记制度（`docs/TOOL_STATUS.tsv`）

`docs/TOOL_STATUS.tsv` 记录 `tools/` 下每个脚本的名称、所属阶段、层级（核心 / 实验）、状态（`planned` / `implemented` / `tested` / `verified`）与最近一次回执位置。**状态不到 `tested` 的工具，不得出现在任何“已生效”表述里；状态不到 `verified` 的，不得作为阻断项。** 截至 R5.5，五个项目仓库均无 `verified` 工具，§2.3 所列核心工具中三个钩子、`ect_verify`、`mcr_filter`、`retraction_check`、`refcheck`、`glyph_coverage`、`injection_scan`、`skill_sanitize`、`chaos_mutator`、`stylometry_gate`、`slop_forensics` 在任何仓库都尚为 `planned`：T1 的阻断集合目前只能来自各仓库已有并测试过的门禁。

| 层级 | 工具清单 |
| :-- | :--- |
| **核心工具** | `extract_corpus` → `build_ontology` → `corpus_ontology` → `apophatic_scan`；`engine_injection`、`diff_editions`、`speccheck`、`fact_consistency`、`declcheck`、`build_kb_sqlite`、`stylometry_gate`、`slop_forensics`、`contracts_run`、`diff_audit`、`build_topology`、`topology_receipt`、`refcheck`、`retraction_check`、`injection_scan`、`glyph_coverage`、`skill_sanitize`、`chaos_mutator`、`ect_verify`、`mcr_filter`、三个钩子、`make_drafting_profile`（R5.5）、`vendor_gsk`、`gsk_suite` |
| **实验探针（§11）** | `sheaf_audit`、`thermodynamics_probe`、`ror_transition_probe`、`sovereign_drift` |

---

## §3 规则、标签、生命周期、三层检查与 ECT + MCR

1. **规则优先级（§1C）**：流程规则按 `AGENTS.md`、`CLAUDE.md` 与 GSK；领域规则按 `kernel/`、`contracts.json`、`ontology/`。两套同时适用时须同时满足；冲突时 Agent 立即停止，调用结构化升级通道开 `kind/owner-decision`（E31），原文引用冲突条款。
2. **认识状态标签（EN/ZH 严格对等）**：`[E]`（附来源编号、原文定位与源文件 SHA-256）、`[M]`（指向脚本与参数表，不用实证结局动词）、`[H]`（附证伪条件）、`[N]`（不充当证据）、`[T]`（可选，附证明与边界条件）、`[W]`（可选，保留旧值、理由、失效时间与勘误索引）。
3. **生命周期**：检查与工具（`planned → implemented → tested → verified`）、交付物（`draft → candidate → human approved → released → corrected/withdrawn`）、共享规则（`candidate → locally checked → human approved → adopted/rejected/superseded`）。Agent 止步于 `tested`、`candidate`、`locally checked`。
4. **检查分三层**：**T0（本地钩子与 `make`）**起草档设双层读/写屏障（只作提示）；**T1（GitHub Actions 基线 CI）**在 `base/` 对 `pr_data/` 执行，阻断合并；**T2（库外留出检查）**物理置于仓库之外由负责人运行（防 E32 挖掘 `.git/objects`），阻断发布，每次发布记录 **`T1 − T2`** 差值。
5. **有证终止与只列清单的残余算子（ECT + MCR，`[H]`，依据 E26）**：P1/P2/P4/P6 会话宣称完成时须通过 `tools/ect_verify.py`（核对修改位置、重放输出与源文件 SHA-256）；未过重放的次要断言由 `tools/mcr_filter.py` **只出清单写入 `review/UNGROUNDED_RESIDUE.md`，严禁自动删改正文**，由负责人决定补证、降级或批准删除并记入台账。

---

## §4 P0–P8 工作流

### P0 — 问题脊梁、估计量与非主张锁定
- 定义问题树、受众、目标估计量、数据与版权隐私权限、**非主张清单**。
- 在 `papers/D*/` 选定报告指南并建 `START_HERE.md`：CONSORT 2025、PRISMA 2020、TRIPOD+AI、ADEMP 按研究类型；医学生成式 AI 加 **GAMER**（9 项）；行为科学 LLM 加 **GUIDE-LLM**（14 项核心条目）。
- 涉及可专利成果时，在任何公开前取得专利代理人的书面意见。

### P1 — 有界检索、话语图谱录证、4 块式 SRR 与撤稿语境核查
- 按原子问题切片检索，单轮工具调用设上限（暂取 `≤8` 次，`[H]`，方向依据 E6）。
- 双步验证：
  1. **文献定位、首次上线日对比与撤稿语境核查（E35）**：用 `PaperQA2` 定位全文；用自建 `tools/retraction_check.py` 直连 Crossref REST API 核查 `update-to`、`updated-by` 及标题前缀撤稿与关注声明。借鉴 **`MrSaneApps/sanecite-retraction-census`（v1.4.1，E35）** 的两项机制：① **First-Online Date Rule**（精确到日比对施引日与最早撤稿通知日）；② **支持性引用阻断**（鉴于 40.7% 撤稿后引用仍在正面倚赖撤稿结论，任何已被撤稿的文献除非在正文中显式贴有 `[W]` 并作为反面/历史撤稿案例讨论，否则一律判 BLOCK）。
  2. **话语图谱录证与 4 块式 SRR（E19）**：吸收 **Discourse Graphs（Q/C/E/S + Caveat + Artifact）** 规程与 `MukundaKatta/agent-citation`（MIT）WHERE 层结构化指针：打开被引原文核对正文与图表/附录，在 `kb/claims.yaml` 记录逐字引文、方法学语境、字符起止位置、PyMuPDF 图表位置与源文件 SHA-256，并附 **4 块式结构化推理记录 `srr_trace`**（`scope_and_entities` → `source_state_trace` → `qualifier_and_boundary_check` → `entailed_claim`）。无法证实的弃答；来源矛盾的标 `HOLD`。
- 入库前跑 `make injection` 扫描零宽字符与字体映射隐藏指令（E14）。
- 保密、他人未发表、付费墙材料严禁上传无保密保障的公开平台或云端 MCP；审稿遵守 ICMJE 2026-01 AI 专节。

### P2 — 主张纳入、模式锁定、限定语登记与提案十铁律
- 用 `Opus 5.5`（`effort: high`）编译结构化账本。
- 承重主张入 `kb/claims.yaml` 与 `kb/ledger.yaml`，数值保留完整元组与五键绑定；每条主张登记 `qualifiers` 清单（E5、E12，支持跨章实体+限定词超关系路径检查 E34）。
- 借鉴 `ontocast` 的渲染-批判-合并与溯源机制，但在 **P2 末锁定 `ontology/*.yaml`**，禁止起草 Agent 动态改本体。
- `SPINE.md` 中每个主论点绑定 **≥2 个具名异质子论点 + 1 个真实反例/失效边界**（`[H]`，E2），并标注 `verify_by`：**`review`**（经验综合，走 P6 评审）或 **`recompute`**（推导与统计，关联 `formal/` 或 `lab/` 可重跑脚本/证明，不靠讨论裁决）。中文叙事类章节可参考 E28 的叙事功能分类拆解结构（`[H]`）。
- **原创命题与模型提案十条规则：**（1）标明因构造/模型假设/数据支持三类结论；（2）对照具名外部目标校准（冲突时报两套）；（3）对争议假设加放宽情景；（4）检验离散估计量离散特性；（5）未证单调性前极限不当界；（6）所需假设随结论写进摘要与结论；（7）提案附零假设通过率与样本量；（8）证伪检验用无机械关联数据且真能失败；（9）**设专节用数值反驳曾提出后撤回的更强主张 `[W]`（`declcheck.py` 校验该局限性/反驳槽位非空，防 E14 失明）**；（10）只报告实际运行过的验证。
- 跑 `make kbdb` 与 `make topology-check`（不为连通度造边）。

### P3 — 脚手架哈希签发、解压起草与依据记录改稿
1. **脚手架（`SCAFFOLD.yaml`）**：每章 1 个 Linear Issue。只填：3–5 个节拍；账本锚点（`claim_id`、数值、`qualifiers`、`untranslated` 词）；按体裁结构约束（论述类：禁章末复述、留未闭合问题、禁“问题—三点—展望”；叙事类：主题不点破、非对称递进）；章节合同（必保来源、承诺、长度区间）。不写修辞指导，不写批准字段。
2. **批准关卡**：负责人审阅后在 **`ledgers/scaffold_approvals.jsonl`** 追加 `{"path": "<脚手架路径>", "blob": "<git hash-object>", "by": "<人名>", "date": "<YYYY-MM-DD>"}` 合入默认分支（决定台账 `approvals.tsv` 另记一行“批准脚手架”，两处互指）。钩子仅认 `origin/<默认分支>`，CI 再比对一次。`books/` 与 `papers/` 正文均受约束。
3. **先列候选，再最小上下文起草（E11, E16）**：先用 `Verbalized Sampling` 列 4–5 个切入路径及概率并选低概率（暂取 `≤0.15`）；再在 **WSL2 下用 `make draft`** 启动，仅注入本卷 `KERNEL` + 上章交接摘要 + 本章 `SCAFFOLD.yaml`，单次产出 2,000–5,000 汉字（长章按节拍分次写）。起草读集不含任何测量输出（§0.3 第 2 条）。
4. **改稿纪律（E30）**：不给模型“降低 slop 分”这类指令。每处修改必须指向具体的 `claim_id`、账本条目或实验记录。纯格式问题（标点、空格）机械修；文风评分静默写入工作树外 `~/.cgee/<repo>/STYLE_REPORT.md` 供负责人阅览决定。
5. **双语工程（§15）**：先写主语言 → 提取主张、数值与 `qualifiers` 主干 → 据主干重写目标语言 → **按 `claim_id` 逐条清点两版数字、单位与限定语数量**；简繁按术语表独立过一轮；不在一边已改另一边未改时结束会话。不用回译验证限定语（E12）。

### P4 — 确定性关卡、两步字形与 Chaos 变异
本地是 T0；PR 上由 GitHub Actions 在 `base/` 对同级 `../pr_data` 跑 T1：
1. `gsk/conservation`：`make facts`、`make declcheck`、`make speccheck`、`tools/diff_audit.py --flagged`、`tools/ect_verify.py`、`vendor_gsk.py verify`、`tools/refcheck.py`、脚手架批准哈希比对；
2. `gsk/grade`：情态与 V1–V5 核验层级匹配；EN/ZH 限定语数量一致；
3. `gsk/style`：Gate P（L1 含 `XDOC-DUP-01`，L5 文体计量棘轮）与 §5 工具；
4. **同源构建与两步字形审计**：正文统计数字与表格出自同一结果文件（Quarto ≥1.4 / MyST + Typst）。**不用 Typst 警告查缺字形**，改为编译前 `tools/glyph_coverage.py`（正文码位对照字体字符表）+ 编译后从 PDF 抽文本扫 `U+FFFD`，再逐页目视检查中西文断行；
5. 非空跑：`min_ran ≥ 1`；
6. **已知错误变异测试（`make chaos`）**：对 `tests/mutants/` 注入 5 类错误（反转来源结论、`[M]→[E]`、删限定语、注虚假引文、造跨章矛盾）、做引文片段扰动（借 E20 思路）以及 `Force`/`Remove` 剥除终点长度伪影检查（E33），核查各门禁的真实捕获率。

### P5 — 四段式引擎与只读缺口诊断（不阻断 PR）
- **四段式引擎**（`make engine`，`docs/ENGINE.md`）：`extract_corpus` → `build_ontology` → `corpus_ontology` → `apophatic_scan`，配 `engine_injection.py` 压测。五条约束：① 只报告不阻断，缺口转 `kind/gap-question`（每次 ≤8 个），关闭缺口回 P1/P2 补账本不往正文填废话；② 共现以单句或依存子句为界，禁跨句滑窗，分词前用 `terms`/`synsets`/`untranslated` 锁专名；③ `synsets.yaml` 折叠为规范 ID，双报字面与同义覆盖；④ 区分 Use vs Mention 与否定/撤回/禁用语域；⑤ 输入取 `corpus/editions/` 冻结版，先声明分母，用 7 种英文缺席码（`not in this corpus` / `not searched` / `not observed` / `not measured` / `not accessible` / `not reported` / `unknown`）与 6 种处置码（`G-SCOPE` / `G-SYNSET` / `G-EVID-EXISTS` / `G-EVID-ABSENT` / `G-HYP` / `G-HOLD`）。
- 外部图谱（如 InfraNodus）只在 P5 做只读诊断，不传保密全文，不在 P3 生成桥接文本。
- `make forensics`：累计书稿与库外作者参照语料比对 n-gram 过代表倍率，由负责人批准更新 `banned_registers.yaml`。

### P6 — 对抗性挑战、独立盲审与新意双检
- **第一轮**：关联 `claim_id` 写出带 SRR 的自检与红队（可借只读子代理，不冒充外审）。
- **第二轮（承重发布必做）**：在 `review/blind/` 冻结副本中进行（先跑 `injection_scan.py`）。**严禁把起草代理的自然语言计划、辩护备忘或修改日志放入盲审上下文（防止作弊策略跨代理传染，E32）**。评审者为**真人专家，或钉死快照版本的非 Anthropic 家族模型**（E13/E14），委派消息取固定模板，加人类对清晰度（Clarity）与局限性的专项复核；`verify_by: recompute` 章节核对脚本/证明重跑结果。
- **修补上限与反馈粒度（E7 & E32, `[H]`）**：同一上下文自动修补最多 2 轮；返回起草 Agent 只有检查代号与位置。
- **新意与双在先检索（§9）**：起草前作者自查一次、起草后全新上下文再查一次（覆盖本领域与相邻领域术语，区分已有成果与相关/未知）；4 类结构新意操作（反向视角附录、兼容已准入源交叉计算、跨章综合页、形式结构论证）绝不混入未核验数值。

### P7 & P8 — 可逆重构、发布证明、双时态监测与 RinR 演化
- **重构与安全交付（§13.3 & §13.4）**：规范正文重构前过 5 步可逆预检（授权→冻结→唯一目标映射→外置原型→最小改动重跑）；移交包不等于定稿；被连接器拒收文件记暂扣，不改名绕过。
- **P7 发布**：按期刊政策、ICMJE、GAMER、GUIDE-LLM 汇总 `AI-Assisted` 尾注及 **Anthropic 平台统计文本水印路线披露**；贡献者用 CRediT；检查资金/利益冲突与无障碍（对比度、替代文本、非颜色编码、字号）；跑通库外 T2 记录 `T1 − T2`；负责人签发（CI/本地 SHA-256 哈希链清单 + GPG/SSH 签名入 `ledgers/releases.jsonl`；公开/Enterprise Cloud 另加 Artifact Attestation）。
- **P8 监测与 RinR 演化**：定期 `retraction_check.py` + `Graphiti` 双时态窗口闭合与 `[W]` 公开勘误；技能与脚手架按 `ScienceBuddy` 内循环（E17：固定模型只改线束、单处有界修改、成对 `dev` 对照、库外 `heldout` 绝不选型、平局留父、换模全重测）迭代。

### 回退表

| 触发 | 回到 |
| :--- | :--- |
| P4 数值、主张或 ECT 报错 | P2（来源存疑则 P1）。只改正文让检查变绿，判失败 |
| 残余清单 `UNGROUNDED_RESIDUE.md` 有承重主张 | 负责人决定补证据、降级标签或授权删除，决定记入台账 |
| P4 结构报错 | P3（自动修补最多 2 轮） |
| `~/.cgee/<repo>/STYLE_REPORT.md` 中有负责人认为需改之处 | P3，由负责人指明具体 `claim_id` 或段落位置重写，禁直推 slop 分 |
| `make chaos` 有错类未捕获 | 由负责人在独立工具检出里补强检查器 |
| P5 发现缺口或矛盾 | P1 / P2 登记 `kind/gap-question`；不直接补废话填图 |
| P6 挑战成立 | P2 / P3，修订后交新上下文复核 |
| P7 场所规则不符 | P0 |
| P8 来源撤稿或更正 | P1 → P2 → P3 → P4 并公开勘误 |
| `T1 − T2` 超过阈值 | 暂停发布，审计检查器是否被迎合 |

*(§11 实验区探针不触发回退，只作只读参考。)*

---

## §5 各层控制（核心）

```text
[层 0  起草档屏障] PreToolUse (hook_pre_guard.py) + drafting.json (WSL2 沙箱 failIfUnavailable + denyRead/denyWrite)
                   ├─ blockReadsOutsideWorkingDirectories + blockWritesOutsideWorkingDirectories + Read/Edit deny
                   ├─ 全会话拦截 Bash 写受控目录绕过；起草会话只放行 git status/add/commit/push 并禁 .git/
                   └─ 仅认 origin/main:ledgers/scaffold_approvals.jsonl 脚手架 SHA + kind/owner-decision (No-Dodging, E31)
        ↓
[层 1  破坍缩]     P2 SPINE >=2 异质子论点+1反例 (E2) -> P3 Verbalized Sampling 低概率切口 + 最小上下文 (E11/E16)
        ↓
[层 2  写盘后(T0)] PostToolUse，仅对正文路径
                   ├─ 机械格式（标点/空格）直接 exit 2 回显；文风/slop 评分静默写工作树外 ~/.cgee/<repo>/STYLE_REPORT.md，不回显给模型 (E30)
                   ├─ 英文：eric-tramel/slop-guard、Vale、berelevant-ai/slopless (sloptrim 仅参考)
                   ├─ 简体：autocorrect、zhlint、apophatic_scan.py (阈值用 C-ReD E28 / 作者旧稿校准 [H])
                   └─ 繁体（台湾）：sysprog21/zhtw-mcp、autocorrect
        ↓
[层 3  文体计量]   stylometry_gate.py（英文可封装 pystylometry）；锚定作者基准
        ↓
[层 4  引擎取证]   make engine（四段式 + engine_injection 压测）与 make forensics（只报告）
        ↓
[层 5  体裁结构]   按体裁取用 SCAFFOLD.yaml 结构字段（论述类/叙事类区分 [H]）
        ↓
[层 6  CI 双锁(T1)] gsk/style ∥ gsk/conservation (diff_audit + fact_consistency + ect_verify + mcr_filter只出清单) ∥ gsk/grade
                   └─ make chaos 定期验证门禁捕获率与终点剥离体检 (E33)
        ↓
[层 7  库外留出(T2)] 仓库之外物理独立运行；记录 T1 − T2 差值 (E10)
```

---

## §6 三份契约、数值溯源（九条）、记录与构建（十一条）

### 6.1 三份契约（`contracts_run.py`，`min_ran ≥ 1`）
- **`gsk/conservation`（阻断）**：数字、单位、ID、引文及位置、图表位置、标签、限定语清单、范围标记、EN/ZH 对等、引入包完整性、脚手架哈希、ECT 终态。`diff_audit.py --flagged` 检出通过删除被标记文字过关返 `2`（经负责人在台账批准的删除除外）。
- **`gsk/grade`（棘轮，新增阻断）**：措辞不强于核验层级（V1 形式/确定性、V2 外部可执行记录、V3 校准模型评判、V4 未校准诊断/盲审、V5 自评永不关关）。
- **`gsk/style`（棘轮）**：Gate P L1、L5 与词法、标点门禁。

### 6.2 数值溯源（九条）
1. 参数登记表列全值、单位、印刷字符串、含义、状态（`published`/`recorded`/`assumed`/`derived`）与来源；常数不硬编码进代码或技能。
2. `recorded` 同句带限定词；`assumed` 同段带限定词或同单元有声明句。
3. **五键绑定**：`(claim_id, evidence_key, unit, context_hash, printed_string)`。
4. **诱饵规则**：接近参数的值除非完全匹配、句带显式标签，或在 1.5% 容差内且单位相同有识别词无排除词，否则视为诱饵；单位不同判 BLOCK。
5. **七种独立裁决**：`tag_resolved`、`tag_unresolved`、`parameter_bound`、`value_context_collision`、`derived_traceable`、`derived_ambiguous`、`no_evidence_found`；未追溯不等于错；证据冲突判 blocked，不合并成一个分数。
6. **矛盾是残差**：以已登记值为锚逐行比对，不求平均。
7. 非空跑下限：每卷单元/主张/约束行数下限 + `min_ran ≥ 1`（设 0 须写 `_vacuous_ok_reason`）。
8. 批准绑定提案 SHA-256；重钉只能由人完成，头哈希抄存工程树外。
9. 记录不等于批准：Agent 代记决定须原文引用指令、写明记录者是 Agent 并绑定提案哈希。

### 6.3 记录、数值与构建（十一条）
1. 另手记账：状态表、更正登记、字数统计由独立脚本生成；PR 与会话日志是 Agent 自述（V5，E18 证实自我反思日志不减作弊）。
2. 更正是状态，不是静默编辑（留 `[W]` 旧值 + 公开勘误）。
3. **十倍检验**：定量核心结论定稿前由人做数量级复核。
4. **整数一致性**：每个百分比精确等于所述 $N$ 下的某个 $k/N$；公开库推导比率先重算。
5. 正文计数与范围由脚本从表格同一结果文件输出，不各自建网。
6. 图读取表：缺失画 `not measured`；最终尺寸 ≥8.5pt；色觉缺陷友好。
7. 修订度量要对顺序敏感（句子保留率与词级编辑操作）。
8. 无静默回退（不在忽略目录放生成器）。
9. 构建审计：零 `U+FFFD`、零未解析块、无源文件新于产物、无重复标题或 ID、EN/ZH 成对。
10. 逐页目视检查渲染结果（防表格拆词、CJK 断行撕裂、误转大写）。
11. 检索日志缺失写 `not recorded`，不事后重构检索式。

### 6.4 发布拒绝条件
不是每卷一文件；仍为 `candidate`；发布检查未读到最终字节或结论不确定；有无人工豁免的 BLOCK；最后重钉非人手完成；必需署名评审缺本版哈希或由 Agent 署名/同族自审；字形覆盖未过或 PDF 含 `U+FFFD`；任何契约 `min_ran == 0`；脚手架哈希未登记；残余清单 `UNGROUNDED_RESIDUE.md` 存在未处置承重主张；T2 未跑或 `T1 − T2` 超阈值；发布清单缺负责人签名；任何阻断工具在 `docs/TOOL_STATUS.tsv` 中状态不到 `verified`；§0.5 中本次发布依赖的平台事实超过 30 天未复核。

---

## §7 终审全量配置与可执行钩子模板

**以下模板没有经过运行测试，落地前须逐项实测。**

### 7.1 权限：基线加起草档

`.claude/settings.json`（入库，受保护；仅写 `Edit(...)`，不写无效 `Write(...)`）：

```json
{
  "permissions": {
    "blockWritesOutsideWorkingDirectories": true,
    "deny": [
      "Edit(./CLAUDE.md)",
      "Edit(./AGENTS.md)",
      "Edit(./.claude/**)",
      "Edit(./governance/**)",
      "Edit(./.github/**)",
      "Edit(./ledgers/**)",
      "Edit(./tools/**)",
      "Edit(./src/daoproto/**)",
      "Edit(./tests/**)",
      "Edit(./EVAL/**)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Grep|Glob|Bash|Edit|Write",
        "hooks": [{ "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/tools/hook_pre_guard.py\"", "timeout": 15 }]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/tools/hook_prose_lint.py\"", "timeout": 30 }]
      }
    ],
    "Stop": [
      {
        "hooks": [{ "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/tools/hook_stop_gate.py\"", "timeout": 300 }]
      }
    ]
  }
}
```

`.claude/profiles/drafting.json`（入库，受保护；`make draft` 在 WSL2 里先由 `tools/make_drafting_profile.py` 把下列相对项展开为**绝对路径**写到 `.claude/.state/drafting.json`，再执行 `CGEE_DRAFTING=1 python3 tools/hook_pre_guard.py --selftest && CGEE_DRAFTING=1 claude --settings .claude/.state/drafting.json`。R5.5 依据：设置参考页写明项目设置中 `./` 前缀相对项目根解析（P7），但经 `--settings` 传入的文件如何解析未核，且旧版本曾静默忽略相对路径（issue #50454，2026-05 关闭），所以一律展开为绝对路径。`denyRead` 拦 Bash 子进程，`Read` deny 拦内置工具，两层都要。`.git` 进 `denyRead` 后沙箱内 git 不可用：起草会话只写文件，提交由人在沙箱外跑 `make checkpoint`（`git add` 正文路径 + `git commit`），git 子命令白名单因此只作第二道防线）：

```json
{
  "permissions": {
    "blockReadsOutsideWorkingDirectories": true,
    "deny": [
      "Read(./tools/**)",
      "Read(./tests/**)",
      "Read(./src/daoproto/**)",
      "Read(./EVAL/**)",
      "Read(./review/**)",
      "Read(./corpus/editions/*/reports/**)",
      "Read(./artifacts/**)"
    ]
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "filesystem": {
      "denyRead": ["~/.ssh", "~/.aws", "~/.config/gh",
                   "./.git", "./tools", "./tests", "./src/daoproto", "./EVAL",
                   "./review", "./corpus/editions/*/reports", "./artifacts"]
    }
  }
}
```

### 7.2 `.claude/settings.local.json`（不入库）、子代理、规则与 `CLAUDE.md`

`.claude/settings.local.json`（不设 `CGEE_DRAFTING` 与 `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`）：

```json
{
  "alwaysThinkingEnabled": false,
  "env": {
    "MAX_THINKING_TOKENS": "0"
  }
}
```

`.claude/agents/blind-reviewer.md`：

```markdown
---
name: blind-reviewer
description: 第一轮只读自检。只在 review/blind/ 的冻结副本里工作，禁止读取草稿会话计划与日志。
tools: Read, Grep, Glob
disallowedTools: Write, Edit, Bash, Agent
permissionMode: plan
maxTurns: 25
---
```

`.claude/rules/prose-zh.md`：

```markdown
---
paths:
  - "books/**/*.zh.md"
  - "papers/**/*.zh.md"
---

# 中文写作规则
- 标点与混排：全角中文标点；中英文及数字的间距由 autocorrect 检查（繁体台湾版另跑 zhtw-mcp）。
- 禁用语域：避开 ontology/banned_registers.yaml 里登记的条目。
- 结构：按本章 SCAFFOLD.yaml 的节拍与未闭合问题展开，不在章末复述论点。
- 守恒：润色时不增删、不近似化带状态标签句中的数值、单位、人名、引文与限定语。
```

`CLAUDE.md`（≤60 行，明确上报通道、`No-Dodging` 铁律与 `E30` 非 slop 优化准则）：

```markdown
@AGENTS.md

# CGEE Writing & Research Repository Rules (R5.4)

## Truth & integrity
- Truth lives ONLY on the protected default branch (`kernel/`, `kb/`, `ontology/`, `formal/`).
- Keep `[E] [M] [H] [N] [T] [W]` tags and all `qualifiers` identical across EN/ZH.
- Never edit `governance/`, `.github/`, `tools/`, `src/daoproto/`, `tests/`, `EVAL/`, `ledgers/`, `.claude/`,
  unless `AGENTS.md` of this repository grants a narrower rule (e.g. edits on a recorded owner instruction); AGENTS.md wins.
- In drafting sessions never read `review/`, `corpus/editions/*/reports/` or any score: measurements reach you only as check id + location.

## Session, scaffold & escalation
- 1 Linear Issue = 1 session (<= 25 tool calls) = 1 branch = 1 PR.
- Before writing prose in `books/` or `papers/`, `SCAFFOLD.yaml` blob hash MUST appear in
  `origin/main:ledgers/scaffold_approvals.jsonl`. You cannot approve a scaffold yourself.
- If anything is ambiguous, if rules conflict, or if a check looks wrong:
  STOP and escalate via `kind/owner-decision` (an escalation holds the issue and never counts as a pass).
- Load at most 3 sanitized skill cards per task (`skills/`).

## Checks & revision discipline
- In drafting sessions (`make draft`), checks run through hooks; do not read or run `tools/`.
  Allowed git subcommands: `status`, `add`, `commit`, `push`.
- In ledger sessions: `make kbdb topology-check facts`.
- Local checks passing does not mean the PR passes. CI on the default branch decides.
- Never delete flagged sentences, citations, qualifiers, or numbers to pass a check.
- Revise only where a `claim_id`, ledger entry, or experiment record points. Never rewrite to lower a style score.
- Auto-fix is capped at 2 rounds. P1/P2/P4/P6 completion claims require replayable ECT evidence.
```

### 7.3 `tools/hook_pre_guard.py` 与 `tools/hook_stop_gate.py`

**`tools/hook_pre_guard.py`**（合流终审版：① 全会话防 Bash 重定向/`python3 -c` 写受控目录绕过 `Edit|Write` 钩子；② 起草会话 `CGEE_DRAFTING=1` 实施 `git` 子命令白名单 + `.git/` 禁访 + `Grep/Glob` 路径校验；③ 脚手架哈希仅认 `origin/main`）：

```python
#!/usr/bin/env python3
"""PreToolUse:
1) 全会话: 防通过 Bash 重定向或内联脚本直接写受控目录绕过 Edit|Write 钩子;
2) 起草会话 (CGEE_DRAFTING=1): git 只放行 status/add/commit/push, 禁 .git/, Grep/Glob 须指明子目录, 禁读评测目录;
3) 所有会话: 写正文前核对 SCAFFOLD.yaml 哈希, 只认 origin/<默认分支>."""
import json, os, pathlib, re, subprocess, sys

DEFAULT_REF = "origin/main"
PROTECTED_WRITE = r"\b(books|papers|kb|ontology|formal|governance|ledgers|\.claude|\.github|CLAUDE\.md|AGENTS\.md)\b"
BLIND_DIRS = ("tools", "tests", "src/daoproto", "EVAL", "review", "artifacts", ".git")
BLIND_GLOBS = (r"^corpus/editions/[^/]+/reports(/|$)",)   # measurement outputs (R5.5 §0.3-2)
APPROVALS = "ledgers/scaffold_approvals.jsonl"
GIT_OK = {"status", "add", "commit", "push"}
PROSE = (r"^books/[^/]+/chapters/[^/]+/.+\.(en|zh)\.md$",
         r"^papers/[^/]+/.+\.(en|zh)\.md$")

def block(msg):
    print(f"BLOCKED: {msg}", file=sys.stderr)
    sys.exit(2)

def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)

if "--selftest" in sys.argv:
    root0 = os.environ.get("CLAUDE_PROJECT_DIR") or "."
    sys.exit(0 if git(root0, "rev-parse", "--git-dir").returncode == 0 else 1)

def blind(rel):
    return any(rel == d or rel.startswith(d + "/") for d in BLIND_DIRS) or any(re.match(g, rel) for g in BLIND_GLOBS)

try:
    data = json.load(sys.stdin)
    root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd", ".")).resolve()
    tool = data.get("tool_name", "")
    tinp = data.get("tool_input") or {}
    drafting = os.environ.get("CGEE_DRAFTING") == "1"

    if tool == "Bash":
        cmd = tinp.get("command", "")
        clean_cmd = re.sub(r"\b[012]?>&[012]\b|>\s*/dev/null\b", "", cmd)
        write_intent = re.search(
            r"(>>?|(?<!&)>|\btee\b|\bsed\s+-i\b|\bcp\b|\bmv\b|\bdd\b|\bpython3?\s+-c\b)", clean_cmd
        )
        if write_intent and re.search(PROTECTED_WRITE, clean_cmd):
            block("请使用 Edit/Write 工具修改受控文件，禁止通过 Bash 命令或脚本直接写盘绕过钩子。")
        if drafting:
            if re.search(r"(^|[\s/'\"=])\.git(\b|/)", cmd) or "GIT_DIR" in cmd:
                block("起草会话禁止直接访问 .git。")
            # Bash reads of blind paths (cat/grep/python/less ...): best-effort; the OS-level guard is sandbox denyRead
            for tok in re.findall(r"[\w./*-]+", cmd):
                if blind(tok.lstrip("./")):
                    block(f"起草会话禁止读取测量与评测路径（{tok}）。")
            for seg in re.findall(r"(?:^|[\s;&|(`])git\b([^;&|\n]*)", cmd):
                words = [w for w in seg.split() if not w.startswith("-")]
                if not words or words[0] not in GIT_OK:
                    block("起草会话仅允许 git status / add / commit / push（不带跨目录参数）。")
        sys.exit(0)

    if drafting and tool in ("Grep", "Glob"):
        p = (tinp.get("path") or "").strip()
        if not p or p in (".", "./"):
            block("起草会话里 Grep/Glob 必须显式指定子目录，例如 books/、papers/、kb/。")

    raw = tinp.get("file_path") or tinp.get("path") or ""
    if not raw:
        sys.exit(0)
    try:
        rel = pathlib.Path(raw).resolve().relative_to(root).as_posix()
    except ValueError:
        rel = str(raw).lstrip("./")

    if drafting and tool in ("Read", "Grep", "Glob"):
        if rel == "." or blind(rel):
            block(f"起草会话禁止读取评测、测试与测量输出（{rel}）。")

    if tool in ("Edit", "Write") and any(re.match(p, rel) for p in PROSE):
        scaffold = (root / rel).parent / "SCAFFOLD.yaml"
        if not scaffold.exists():
            block("缺少 SCAFFOLD.yaml。先写脚手架并提交负责人审批。")
        s_rel = scaffold.relative_to(root).as_posix()
        blob = git(root, "hash-object", str(scaffold)).stdout.strip()
        ledger = git(root, "show", f"{DEFAULT_REF}:{APPROVALS}")
        if ledger.returncode != 0:
            block(f"读不到 {DEFAULT_REF} 上的批准台账，禁止回退到本地分支。")
        ok = any(rec.get("path") == s_rel and rec.get("blob") == blob
                 for rec in (json.loads(ln) for ln in ledger.stdout.splitlines() if ln.strip()))
        if not ok:
            block(f"{s_rel} 的当前版本（{blob[:12]}）未记入 {DEFAULT_REF}:{APPROVALS}。开 kind/owner-decision。")
except SystemExit:
    raise
except Exception as exc:
    block(f"hook_pre_guard 异常，按故障安全阻断：{exc}")
```

**`tools/hook_stop_gate.py`**（合流修复：文风评分静默写入工作树外的 `~/.cgee/<repo>/STYLE_REPORT.md` 绝不回显给模型 E30；仅守恒检查失败才打回，最多 2 轮且不清零计数器；`hook_prose_lint.py` 同样只用 `exit 2` 回显机械标点/空格问题，评分问题静默写报告并以 `0` 退出）：

```python
#!/usr/bin/env python3
"""Stop 钩子（T0）。只有守恒类检查失败才打回，最多 MAX_BLOCKS 次；计数器只在检查通过时清零。
文风评分只写入工作树外 ~/.cgee/<repo>/STYLE_REPORT.md 供负责人看，绝不回显给起草模型（E30）。判定在 CI。"""
import hashlib, json, os, pathlib, shutil, subprocess, sys

MAX_BLOCKS = 2
data = json.load(sys.stdin)
root = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd", ".")).resolve()

def sh(*cmd):
    return subprocess.run(cmd, cwd=root, capture_output=True, text=True)

def names(*args):
    out = sh("git", "-c", "core.quotepath=false", *args).stdout
    return {line for line in out.splitlines() if line}

changed = names("diff", "--name-only", "HEAD") | names("ls-files", "--others", "--exclude-standard")
prose = sorted(p for p in changed if p.startswith(("books/", "papers/")) and p.endswith(".md"))
if not prose:
    sys.exit(0)

# 文风：静默写报告给负责人看，不回显给模型（防止 E30 奖励操纵）
english = [p for p in prose if p.endswith(".en.md")]
if english and shutil.which("sg"):          # R5.5: a missing scorer must not crash the hook
    style = sh("sg", "-v", "-t", "80", *english)
    # R5.5: the report lives OUTSIDE the working tree, so a drafting session (blockReadsOutsideWorkingDirectories
    # + sandbox) cannot read it; review/STYLE_REPORT.md inside the repo would be readable and gameable (E30).
    out = pathlib.Path.home() / ".cgee" / root.name / "STYLE_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("英文文风评分（仅供负责人参考，严禁直接交给模型刷分）\n\n" + (style.stdout or style.stderr), encoding="utf-8")

sid = hashlib.sha1(data.get("session_id", "x").encode()).hexdigest()[:12]
state = root / ".claude" / ".state" / f"stop-{sid}.json"
state.parent.mkdir(parents=True, exist_ok=True)
blocks = json.loads(state.read_text())["n"] if state.exists() else 0

checks = [
    ("GATES", ["make", "-s", "gates", "facts", "BRIEF=1"]),
    ("DIFF_AUDIT", ["python3", "tools/diff_audit.py", "--flagged", "--brief"]),
]
fails = []
for tag, cmd in checks:
    run = sh(*cmd)
    if run.returncode != 0:
        fails.append(f"[{tag}]\n{(run.stdout or run.stderr).strip()[:1500]}")

if not fails:
    state.unlink(missing_ok=True)
    sys.exit(0)

if blocks >= MAX_BLOCKS:
    sys.exit(0)

state.write_text(json.dumps({"n": blocks + 1}))
report = "\n\n".join(fails)
if blocks + 1 == MAX_BLOCKS:
    handoff = pathlib.Path.home() / ".cgee" / root.name / "HANDOFF_REQUIRED.md"
    handoff.parent.mkdir(parents=True, exist_ok=True)
    handoff.write_text("本地预检已打回到上限。此为最后一轮自动修补，后续由负责人处理：\n\n" + report, encoding="utf-8")

print(
    f"预检未通过（第 {blocks + 1}/{MAX_BLOCKS} 轮）。不得删除数字、引文与限定语来过关；检查本身有问题请开 kind/owner-decision。\n" + report,
    file=sys.stderr,
)
sys.exit(2)
```

### 7.4 `.github/workflows/gsk-contracts.yml`（`base/` 与 `pr_data/` 同级物理隔离版）

```yaml
name: gsk-contracts
on:
  pull_request_target:
    types: [opened, synchronize, reopened]
permissions: {}
jobs:
  contract:
    name: gsk/${{ matrix.contract }}
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    permissions:
      contents: read
    strategy:
      fail-fast: false
      matrix:
        contract: [conservation, grade, style]
    steps:
      - uses: actions/checkout@<40位-commit-SHA>   # 默认分支检出至 base/
        with:
          path: base
          persist-credentials: false
      - uses: actions/checkout@<40位-commit-SHA>   # PR 头检出至同级 pr_data/（纯静态数据）
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          path: pr_data
          persist-credentials: false
      - name: Run baseline contract against untrusted PR data
        working-directory: base
        run: >
          python3 tools/contracts_run.py
          --contract ${{ matrix.contract }}
          --gate . --pr ../pr_data --min-ran 1
      - uses: actions/upload-artifact@<40位-commit-SHA>
        if: always()
        with:
          name: receipt-${{ matrix.contract }}
          path: base/artifacts/receipt-${{ matrix.contract }}.json
```

硬化要点：不运行 `pr_data/` 内任何脚本、Makefile、`.pth` 或依赖，解析用 `yaml.safe_load` 且拒绝符号链接；不把 PR 标题/正文/分支名插进 `run:`；令牌只读无密钥；回写 PR 评论与 Linear 摘要拆到独立的 `workflow_run` 作业，仅读取上传的 JSON 工件；定期用 `zizmor` 扫描工作流。

---

## §8 技能索引、`EVAL/` RinR 评测与外部技能三层消毒

1. **GSK-01..22 快速索引**（`governance/gsk/gsk_registry.tsv`；**每任务 ≤3 张速查卡**）：
   - P0：GSK-01 治理与控制面、GSK-06 有界构想、GSK-07 反固着、GSK-20 定位与重构预检
   - P1/P2：GSK-02 来源发现、GSK-03 引用卫生、GSK-04 不确定性与单位、GSK-15 溯源与数值完整性、GSK-18 认识状态、GSK-19 公理–定理–模拟
   - P3/P4：GSK-10 修辞忠实度、GSK-11 有源可视化、GSK-05 结构缺口、GSK-22 会话线束运行
   - P5：GSK-12 语料本体、GSK-13 定量缺席扫描
   - P6：GSK-08 因果批判、GSK-09 盲审包准备、GSK-14 对抗反转、GSK-17 公平审计
   - P7/P8 & 跨阶段：GSK-16 出版打包与归档、GSK-21 受治理技能演化
2. **外部技能引入与三层互补消毒（E17：`26.1%` 含风险且单一扫描器可被绕过）**：引入 K-Dense 等外部技能前，必须依次通过：**① 编码归一化与解码**（`cyberxuan-XBX/skill-sanitizer` NFKC/同形异义词处理 + `--atr-rules` 与 `The-Swarm-Corporation/SkillScanner` Base64/Unicode 标签扫描）→ **② 双引擎互审**（`NVIDIA/SkillSpector >=2.5.0` + `cisco-ai-defense/skill-scanner`）→ **③ `tools/skill_sanitize.py` 与人工逐行通读 Diff**（剥除 `"ALWAYS run"` 全局劫持、商业导流与未授权外发调用，扫描器结果仅作线索，优先纯指令卡加 `disallowedTools`）。
3. **`EVAL/` 评测工具包（§14.5 + ScienceBuddy RinR 内循环，E17）**：至少 8 个项目内 `dev` 任务对照 `no-GSK` 基线，每配置至少 3 个独立会话，开发集平均成对差值 >0.05 才进候选，平局留父；至少 4 个 `heldout` 任务置库外且永不参与选型；底层模型一换全部重测。

---

## §9 经核验与分级的开源组件总清单（R5.4 终审完整版）

**A 级：成熟基础设施，钉版本直接投入生产**

| 组件 | 许可证 | 阶段与用途 |
| :--- | :--- | :--- |
| **`vale-cli/vale`** | MIT | Go AST 感知散文检查；把 `banned_registers.yaml` 编为静态规则 |
| **`huacnlee/autocorrect`** & **`zhlint-project/zhlint`** | MIT | 中文与中西文混排空格、全半角标点、专名检查 |
| **`NVIDIA/SkillSpector`** & **`cisco-ai-defense/skill-scanner`** | Apache-2.0 | 外部 `SKILL.md` 与脚本双引擎交叉安全扫描（扫描结果当线索，不盲信单引擎 Safe） |
| **`Agent-Threat-Rule/agent-threat-rules`** | MIT | AI 代理威胁开放规则库（含越狱与指令注入检测；不检查正文引文真假） |
| **`quarto-dev/quarto-cli`**（≥1.4）、**`jupyter-book/mystmd`**、**`typst/typst`** | MIT / MIT / Apache-2.0 | 同源编译；缺字形靠 `glyph_coverage.py` + PDF 扫 `U+FFFD` |
| **`Future-House/paper-qa`**（PaperQA2） | Apache-2.0 | P1 带原文片段引用的科学文献问答 |
| **`UKGovernmentBEIS/inspect_ai`** | MIT | `EVAL/` 对照评测框架基座 |
| **`zizmorcore/zizmor`** | MIT | GitHub Actions 安全静态扫描 |
| **`getzep/graphiti`** | Apache-2.0 | P8 双时态知识边界设计参考 |
| **Crossref REST API** | 公开接口 | P1/P8 直连查询 `update-to` 与 Retraction Watch 撤稿/更正 |

**B 级：年轻、特定边界或具传染协议约束，钉 40 位 Commit SHA、留副本并配回归测试**

| 组件 | 许可证与注意点 | 用途 |
| :--- | :--- | :--- |
| **`sysprog21/zhtw-mcp`** | MIT (Rust CLI+MCP) | **仅用于繁体中文（`zh-TW`）发行版**（按台湾教育部标准把大陆用语标错，不可直接用于简体正文） |
| **`eric-tramel/slop-guard`** | MIT | 英文评分 CLI `sg`；**结果只写报告不回显给模型**（短文本噪声大） |
| **`craigtrim/pystylometry`** | MIT (1,022 单测) | 50+ 英文文体计量指标（MATTR、MTLD、滑窗卡方漂移） |
| **`seyedehsanhadi/sloptrim`**（参考 `ismilewolf-eng/sloptrim-zh`） | Apache-2.0 / 读 NOTICE | 零依赖标准库检测；长列表文档易误报，仅作参考不阻断 |
| **`berelevant-ai/slopless`** & **`yanstd888/humanizer-lint`** | MIT / MIT | textlint 英文规则 / 多语言节奏诊断（建仓不足 1 月，钉 SHA） |
| **`NulightJens/humanizer-stack`** | **自有 MIT + 上游 CC BY-SA 4.0** | 表面+结构两遍处理参考；**再分发具 Share-Alike 传染义务** |
| **`MrSaneApps/sanecite-retraction-census`** & **`MukundaKatta/agent-citation`** | MIT (代码)+CC BY 4.0 (数据) / MIT | 撤稿后引用普查与 **First-Online Date Rule**（`10.5281/zenodo.23358099`）/ 零依赖 WHERE 层引用属性指针 |
| **`cyberxuan-XBX/skill-sanitizer`** & **`The-Swarm-Corporation/SkillScanner`** | MIT / Apache-2.0 | NFKC 同形异义词归一化、Base64/Unicode 标签解码与 ATR 扫描 |
| **`jenna-russell/storyscope`** & **`HeraldofLight/C-ReD`** | MIT / 核仓库 LICENSE | 叙事结构特征（须修 E4 附录 I 缺陷）/ 简繁中文 5 领域 × 9 模型真实提示检测基准（用于校准观察读数，不定文风阈值） |
| **`CHATS-lab/verbalized-sampling`** | 非标准声明（用前读许可） | P3 采纳其口述多候选概率分布方法（E11） |
| **`K-Dense-AI/scientific-agent-skills`** | 仓库 MIT（逐卡核子许可） | 科学技能；**须经 §8.2 三层互补消毒后按 ≤3 张/任务裁剪入库** |
| **`patrickrd/proof_carrying_hypothesis_testing`** | 核查仓库许可（底座 `linear-model-lean`） | P2/P4 `verify_by: recompute` 统计章节的有限样本 $p$-/$e$-值与 Lean 4 证明参考（含 1 处未完成证明） |
| **`Orchestra-Research/AI-Research-SKILLs`** & **`anthropics/skills`** | MIT / 逐卡看许可 | 技能卡写法与渐进加载规范参考 |

**C 级：只借设计思路、隔离调用或自写轻量标准库替代（禁止作为运行时依赖安装）**

| 组件 | 原因与严格使用边界 | 自研 / 替代方案 |
| :--- | :--- | :--- |
| **`qualixar/superlocalmemory`** | V4.0（`arXiv:2608.08253`）已改 **AGPL-3.0-or-later** | **严禁安装其包**；若进 §11 实验区，按 `arXiv:2603.14588` 数学公式做纯标准库净室实现 |
| **`infranodus/skills`** / **`skills-lab`** | 云端服务涉外发且默认诱导填词连通结构洞 | **仅在 P5 做只读盲点诊断**，严禁传保密全文与在 P3 自动补桥接句 |
| **`Gen-Verse/ScienceBuddy`** | 外层含 RL 且仓库许可证待核 | 仅采纳其 RinR 内循环（固定模型改线束）接受规则用于 `EVAL/`（E17） |
| **`growgraph/ontocast`** | Apache-2.0；LLM 抽取非确定性 | 仅参考渲染-批判-合并与溯源设计，**P2 末锁定 `ontology/*.yaml`** |
| **`weiyueli7/llm-review`** / **`IBM/diveye`** / **`MohamedAbdallah-14/unslop`** | 许可证待核或实验性检测器 | 分别用于 §11 独立修订与惊奇度探针参考 |
| **`Maximeswd/citation-hallucination`** (`FACTUM`) / `VERA` / `BAITBENCH` | 白盒激活方法 / 评测参照 | 分别作机理引用参考及 `tests/mutants/` + 4 块 SRR 设计指导 |
| **`AkariAsai/OpenScholar`** | Apache-2.0；2025-08 后少更新 | 借检索-自反馈思路；实际用 PaperQA2 + Crossref |
| **`hyuga611/reflint`** / **`wedo911/citeguard`** / **`lonexreb/cite-guard`** / **`aberaio/sourcecheck`** | 微型或数月未更新 | 自写 `tools/refcheck.py` 与直连 Crossref 的 `tools/retraction_check.py`（借弃答逻辑） |
| **`sanjoxtech/penprint`** & **`sam-paech/slop-forensics`** | MIT；0 星或停更 | 分别并入 `stylometry_gate.py` 与 `slop_forensics.py` |
| **`Anbeeld/WRITING.md`** & **`WecoAI/SpecBench`** | 纯 Markdown 清单 / 编码基准 | 分别作编辑失真对照表与 `T1 − T2` 指标出处 |

---

## §10 仓库集成与 16 步落地清单

### 10.1 引入 GSK 发布包（§12A）
建 `gov/gsk-<rev>` 分支 → 运行 `vendor_gsk.py install` 生成 `VENDOR_MANIFEST.sha256`（`.gitattributes` 设 `eol=lf`）→ 复制 `contracts.json`（只留已核实检查；按路径触发而无可阻断检查时设 `min_ran: 0` 并写 `_vacuous_ok_reason`）→ 首次全绿后再启用无绕过规则集；添加工作流的首个自举 PR 在本地用 `--bootstrap` 跑 `contracts_run.py` 贴回执原文。三条约束：契约脚本只用 Python 标准库；基线侧缺输入时判失败；豁免必须是显式标注片段（如 `[withdrawn: …]`），不能用单字全局失效。

### 10.2 优先落地顺序（前三项不做，后续检查皆可被绕过；每完成一项即更新 `docs/TOOL_STATUS.tsv` 并附回执）
1. **立执法点**：规则集（3 检查、Code Owner、无绕过）、独立机器账号、`base/`+`pr_data/` CI + `zizmor`。
2. **人工批准入只读台账**：`ledgers/scaffold_approvals.jsonl` 登记脚手架 Blob SHA，`PreToolUse`（仅认 `origin/main`）与 CI 双重比对。
3. **建库外 T2 留出检查**：物理置于库外由负责人运行，持续记录 `T1 − T2`。
4. **建 `docs/TOOL_STATUS.tsv`**：如实填每个工具的状态（不到 `verified` 不得作阻断项）。
5. **建上报通道**：Agent 可调的建 Issue 工具 + `AGENTS.md` 独立反作弊政策 + `No-Dodging` 规则（E31）。
6. **起草环境迁入 WSL2**（`bubblewrap` + `socat`），启用 `drafting.json`（`blockReadsOutsideWorkingDirectories`、`blockWritesOutsideWorkingDirectories`、`failIfUnavailable: true`、`allowUnsandboxedCommands: false`）。
7. **`CLAUDE.md` 首行加 `@AGENTS.md`**，用 §7.2 版本（≤60 行，不贴目录树）；把工作副本移出其他项目的目录树，或用 `claudeMdExcludes` 排除上级 `CLAUDE.md`，开会话后用 `/memory` 确认（P1–P3）。
8. **部署 §7 权限与三钩子**：`PreToolUse` 全会话防 Bash 写盘 + 起草档 `git` 白名单；`Stop` 钩子文风评分只写报告不回显、计数器不清零。
9. **部署 `make chaos`（`tests/mutants/`）** 先检验已经在跑的门禁并过 `Force`/`Remove` 终点剥离体检（E33）。
10. **字形检查落地为“预编译 `glyph_coverage.py` + 编译后 PDF 扫 `U+FFFD`”**。
11. **第二轮盲审换非 Anthropic 家族或真人**，钉死模型版本，**隔离草稿代理历史计划（E32）**，补人类清晰度与局限性复核。
12. **EN/ZH 按 `claim_id` 清点 `qualifiers`**（参考 E34 跨章实体+限定词检查）；简繁分流配置 `autocorrect`/`zhlint` 与 `zhtw-mcp`。
13. **按 §8.2 三层互补管线消毒外部技能**（人工通读 Diff 入库）；限制 InfraNodus 仅做 P5 只读诊断；按 RinR 内循环建 `EVAL/`。
14. **发布证明采用负责人签名的 SHA-256 哈希链入 `ledgers/releases.jsonl`**（不依赖企业版套餐）。
15. **跑三组 `EVAL/` 盲评**：Opus 4.6 开/关 Thinking；4.6 退役接替模型；中文门禁阈值（基于库外作者参照语料）。
16. **按 §0.5 逐月复核平台事实**（失效即降级，不静默沿用）。
17. **实测环境行为**：`MAX_THINKING_TOKENS=0`（查 transcript）、`Read` 拒绝是否同时拦住 Grep/Glob（由 `hook_pre_guard.py` 兜底）、`blockReadsOutsideWorkingDirectories` 对 `~/.claude` 的影响、`--settings` 并集、WSL2 沙箱与 GitHub 套餐推送规则。

*(在前 9 项的核心工具状态到达 `tested` 前，禁止把 §11 实验区内容升格为核心约束。)*

---

## §11 实验区（全部标 `[H]`，只作只读探索，不作阻断、不触发回退）

每一项在升入核心前，必须在 `EVAL/` 说明它测什么、在作者未润色旧稿上读数多少、读数变化时负责人会做出何种不同决策：

| 实验项目 | 设想与学术源头 | 当前工程现状与准入前置条件 |
| :--- | :--- | :--- |
| **`tools/ror_transition_probe.py`** | 依据 E29（`ROR`）计算段落边界句间余弦转移偏差方差 $\delta_{ij}$ | 对转移方差不高于人类基线的生成器失效，中文表现未充分核实；先在作者旧稿上建基线 |
| **`tools/sheaf_audit.py`** | 用一阶蜂窝层上同调 $H^1$ 找跨章节隐含矛盾（E25） | E25 对象是 Agent 记忆，搬到章节需先定义顶点、共享实体与限制映射函数；严禁安装 AGPL-3.0 软件包；更便宜的替代已在核心里（按 `claim_id` + `qualifiers` 跨章检查 E34） |
| **`tools/thermodynamics_probe.py`** | 英文惊奇度波动（E21）+ 自相关幂律与 Hurst/DFA（E22） | E21 是检测器，E22 面向英语击键短文；幂律指数对文本长度极其敏感 |
| **`tools/sovereign_drift.py`** | 比对草稿与作者库外参照语料的漂移 | 尚无稳定度量定义，先降落为 `make forensics` 已有的 n-gram 与文体计量距离 |
| **检测器的终点线索体检（E33）** | 把被测文本的结论句替换或剥除，看审计器判断变不变 | 论文对象是链式推理轨迹检测器；搬到章节审计需先定义什么是“终点” |
| **非常规特区（`Paradox Allowance`）** | 在 `kernel/` 登记允许保留未闭环悖论或非标准曲线的章节 | 属于作者编辑裁决，登记免受常规文风门禁误报即可 |
| **独立修订（E24）** | 多版本互评只交换批评、各自基于自己原稿修订 | 证据源自多代理各写一稿的科幻写作（~9 倍成本），仅在刻意生成多分支候选初稿时启用 |
| **证明证书与 2 项未成型前哨** | 串行章附 Lean 证明；认知减速带；跨学科正交投影 | Lean 证书只在内容确属形式数学/线性模型（E26）时启用；减速带与正交投影尚无操作定义（结论半衰期已并入 P8 `kb/claims.yaml` 复核周期字段） |

---

# 附录 A　连续性模板与 Arena / 水印披露规则

- **`STATE_DASHBOARD.md`**：由单一确定性脚本从权威台账汇总生成，标明为操作快照，不复制台账行、不替代批准裁决。
- **交接文档（Handoff）vs 任务简报（Brief）**：交接文档依据磁盘实际字节写“交付了什么、暂扣了什么、校验和覆盖什么、命令与未决原因”；任务简报开启新会话，只写“一个目标 + 摘要后仍须保留的不变量 + 须询问负责人的决定”。
- **模型不公开与统计水印披露（§7D）**：使用 Arena Agent Mode 等不公开模型产生文本时，如实披露平台、模型未公开、日期、会话链接与做过的人工核验，并在投稿前向编辑确认，或用已知模型重写，保留全部提示与输出；使用带有 Anthropic 统计文本水印的 Claude 模型产出时，按目标出版物要求履行 AI 辅助披露，不声称原始机器直出文本为无 AI 参与的纯人类手写。

# 附录 B　权威文献与开源仓库总索引（经多轮并发审计核验）

- **实证文献 `E1–E35`**：`Nat. Hum. Behav.` 10:1925–1942 (2026) · `arXiv:2606.01736` · `arXiv:2604.03136` · `arXiv:2609.15369` · `arXiv:2611.00359` · `arXiv:2605.06635` · `arXiv:2609.28614` · `arXiv:2604.20779` (`arXiv:2603.26233`) · Snorkel *Ping or Peek* · `arXiv:2605.21384` · `arXiv:2510.01171` · `2026.mellm-1.29` / `arXiv:2603.16131` · `arXiv:2404.13076` · `arXiv:2605.25415` / `arXiv:2611.20608` · Böckeler *Harness Engineering* · `arXiv:2602.11988` / `arXiv:2602.12670` · `arXiv:2609.17523` / `arXiv:2601.10338` / `arXiv:2602.06547` · `arXiv:2608.30724` · `arXiv:2610.06366` · `arXiv:2510.10931` (`2026.emnlp-main.1664`) · `arXiv:2509.18880` · `arXiv:2610.05466` · `arXiv:2601.08003` · `arXiv:2603.14588` / `arXiv:2608.08253` · `arXiv:2605.16407` / `arXiv:2608.23623` / `patrickrd/proof_carrying_hypothesis_testing` · `arXiv:2506.13609` · `arXiv:2603.14430` / `arXiv:2604.11796` (`HeraldofLight/C-ReD`) · `arXiv:2608.26694` (*ROR*) · `arXiv:2610.00531` / `arXiv:2609.33905` · `arXiv:2608.29460` · `arXiv:2611.10404` / `arXiv:2611.09828` · `arXiv:2605.08346` · `arXiv:2601.05866` (`Maximeswd/citation-hallucination`) / `2026.findings-acl.1673` (*HRKG-HD*) · `doi:10.5281/zenodo.23358099` (`MrSaneApps/sanecite-retraction-census`)
- **平台、指南与规范**：Claude Code Permissions (`blockReadsOutsideWorkingDirectories` / `blockWritesOutsideWorkingDirectories`), Sandboxing, Subagents & Settings Docs · Anthropic Opus 4.6, Thinking, Effort, `2026-10-21` API & Text Watermark Docs · Adversa AI Scanner Audit (2026-07-30) · GitHub `pull_request_target` & Immutable Releases Docs · Crossref Retraction Watch · ICMJE Jan 2026 · GAMER (`doi:10.1136/bmjebm-2025-113825`) · GUIDE-LLM (`https://llm-checklist.com/`) · Typst `text` Docs
- **开源仓库索引**：`vale-cli/vale`, `huacnlee/autocorrect`, `zhlint-project/zhlint`, `sysprog21/zhtw-mcp`, `NVIDIA/SkillSpector`, `cisco-ai-defense/skill-scanner`, `Agent-Threat-Rule/agent-threat-rules`, `cyberxuan-XBX/skill-sanitizer`, `The-Swarm-Corporation/SkillScanner`, `quarto-dev/quarto-cli`, `jupyter-book/mystmd`, `typst/typst`, `Future-House/paper-qa`, `UKGovernmentBEIS/inspect_ai`, `zizmorcore/zizmor`, `getzep/graphiti`, `eric-tramel/slop-guard`, `craigtrim/pystylometry`, `seyedehsanhadi/sloptrim`, `ismilewolf-eng/sloptrim-zh`, `berelevant-ai/slopless`, `yanstd888/humanizer-lint`, `NulightJens/humanizer-stack`, `MrSaneApps/sanecite-retraction-census`, `MukundaKatta/agent-citation`, `jenna-russell/storyscope`, `HeraldofLight/C-ReD`, `CHATS-lab/verbalized-sampling`, `K-Dense-AI/scientific-agent-skills`, `patrickrd/proof_carrying_hypothesis_testing`, `Orchestra-Research/AI-Research-SKILLs`, `anthropics/skills`, `weiyueli7/llm-review`, `qualixar/superlocalmemory` (V4 AGPL-3.0), `IBM/diveye`, `MohamedAbdallah-14/unslop`, `Maximeswd/citation-hallucination`, `infranodus/skills`, `infranodus/skills-lab`, `Gen-Verse/ScienceBuddy`, `growgraph/ontocast`, `AkariAsai/OpenScholar`, `hyuga611/reflint`, `wedo911/citeguard`, `lonexreb/cite-guard`, `aberaio/sourcecheck`, `sanjoxtech/penprint`, `sam-paech/slop-forensics`, `Anbeeld/WRITING.md`, `WecoAI/SpecBench`