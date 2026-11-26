# 证据约束型研究工程：通用方法与技能手册
# Evidence-Bound Research Engineering · Method & Skill Handbook

**0.1.0｜可运行工程草案，不是独立审定的科学方法标准。**

这是本Session corpus_engine V1–V6积累的通用提炼，不是作品V6/V7重写。建议总称为“研究工程框架与工具包 / Research Engineering Framework & Toolkit”；corpus_engine保留为跨阶段的语料结构与证据审计子系统。

本文是docs中方法文件的合订阅读版，机器实现、Skill、模板和实际回执在配套仓库目录中。关键词保留中英文；本轮及后续不再交付STATE_DASHBOARD.HTML。

## 阅读地图 / Reading Map

1. [它到底是什么？ / What Is This System?](docs/01_POSITIONING.md)
2. [可复用方法论 / Reusable Methodology](docs/02_METHODOLOGY.md)
3. [执行工作流与门槛 / Workflow & Gates](docs/03_WORKFLOW.md)
4. [数据合同与状态机 / Data Contracts & State Machines](docs/04_DATA_CONTRACTS.md)
5. [corpus_engine：结构分析子系统 / Corpus Structural Analysis Subsystem](docs/05_CORPUS_ENGINE.md)
6. [测试与证明边界 / Validation & Proof Boundaries](docs/06_VALIDATION.md)
7. [面向不同作品与学科的适配 / Adaptation Profiles](docs/07_ADAPTATION.md)
8. [V1–V6谱系与真实能力 / Lineage & Actual Capabilities](docs/08_LINEAGE.md)
9. [已知边界与框架自身债务 / Limitations & Method Debts](docs/09_LIMITATIONS.md)
10. [Session技能提炼与取舍 / Skill Distillation & Selection](docs/10_SKILL_DISTILLATION.md)
11. [中英文关键词 / Bilingual Glossary](docs/GLOSSARY.md)
12. [GitHub目录集成 / GitHub Repository Integration](docs/INTEGRATION.md)


---

## 它到底是什么？ / What Is This System?

### 不是四选一 / Not Mutually Exclusive

|层级 / Layer|回答的问题|本项目中的实体|不能混淆成什么|
|---|---|---|---|
|认识论立场 / Epistemic commitments|何以有理由相信？什么会使我们撤回？|可错性、证据依赖、适用域、反例、独立性、未知保留|一种新近被证明的哲学理论|
|方法论 / Methodology|怎样系统地提出、检查和修订主张？|断言分型、竞争解释、判别观察、测量资格、证据综合、停止规则|某套全学科统一的固定评分表|
|协议 / Protocol|这个项目具体按什么规则做？|语料范围、词表、单位、估计目标、阈值、权限、评审标准|探索后补写的协议被追认为预注册|
|工作流 / Workflow|先后／并行做哪些活动？|搜索、取源、审计、计算、修订、复核、发布、更新|一次线性搜索→生成答案|
|系统／工程实践 / System & engineering practice|如何让过程可追踪、可执行、可维护？|corpus_engine、账本、hash、合同、依赖图、门禁、测试|自动真理机|
|Skill / 可调用技能|Agent遇到什么任务，应按什么合同执行？|有触发器、输入、步骤、产出、拒绝条件、验收的可复用包|只有风格提示或模型人格|
|工具／实现 / Tool & implementation|具体计算什么？|Python模块、JSON Schema、NetworkX、CLI|方法有效性的独立证据|

**准确的总称：研究工程框架与工具包 / Research Engineering Framework & Toolkit。**

若强调认识论，可称“认识论约束的工程化实现 / engineering of epistemic constraints”；若强调结论如何被辩护，可称“研究论证保障 / research assurance”。这里的assurance是有范围的理由与证据组织，**不是保证正确**。

### corpus_engine的角色随迭代变化

- V1–V2主要是**语料结构／透镜审计子系统**：帮助发现写作中的分布、连接、欠展开与候选研究问题。
- V3加入**上下文一致性与可追踪修订**：图结构、事实问题、源内未决不再混为一类。
- V4–V6加入**证据绑定、测量／设计资格、公开数据重算、源码与不变性审计、更新治理**。
- 因而今天它横跨获取、分析、验证、写作、维护多个阶段；在更大的科学研究生命周期中，仍只是支持系统，不替代实验设计和实证工作。

不建议继续把整个通用框架叫`corpus_engine_v7/v8`：那会把“关于语料的图”误当作“关于世界的全部研究”。保留`corpus_engine`作为结构分析模块，顶层用`research-assurance-toolkit`。旧版号描述历史迭代，不代表六次经外部验证的成熟度升级。

### 最小知识对象不是节点，而是带条件的断言

```text
Claim 主张
+ role 话语角色：断言／假设／被拒绝误读／提案
+ context 上下文：对象、时间、估计目标、单位、设计、域
+ provenance 来源链：版本、访问深度、位置、家族、权限
+ warrant 推理担保：为什么证据允许推出这句话
+ defeaters 潜在击败条件：什么观察会使它失效
+ uncertainty 未决项：源冲突、缺失、偏倚、外推条件
```

图节点之间有边，最多先说明某种声明过的关系。共现图、论证图、证据溯源图和因果图必须分开，不能靠换图标把`cooccurs_with`升级为`causes`。

### 为什么不是“发现正确性算法”？

1. 一致的主张可能一起错；多个互相冲突的报告也可能各自准确转述了不同条件下的研究。
2. 原件真实存在，不能证明测量有效；测量有效，不能自动识别因果；内域因果，也不能自动外推到新群体。
3. 工具只能检查已编码的合同。编码、取源、上下文对齐和判定也会出错，因此框架必须能接受对自身的审计。
4. 价值／权利／目标冲突不能被一个P值、中心性或总分消除。

这套框架的价值不是承诺永不犯错，而是**降低错误被隐藏、被版本漂移掩盖、被范围偷换扩大的概率，并让修正有位置、有责任、有条件**。这种价值本身尚需跨领域实测，不能因本Session使用过就声称验证成功。


---

## 可复用方法论 / Reusable Methodology

### 0. 三种产出必须分轨 / Separate Three Tracks

- **发现轨 / Discovery**：候选关系、假说、解释、研究问题。允许发散，但必须标`proposed`。
- **证据轨 / Evidence**：实际取到什么、读到哪里、数据怎么算、设计支持什么。不能由候选自动升级。
- **决策轨 / Decision**：何时足以写作、实施或暂缓；纳入错误代价、权利、成本与授权，不假装纯粹事实决定一切。

每次“范式转换 / paradigm shift”或“涌现 / emergence”都先作为候选表述：旧框架不能解释什么？新框架改变什么可检验预测？是否有替代解释？如果只是换组织方式，就写“重构／新视角”，不写成经验发现。

### 1. 断言分型 / Claim Typing

|类型|需要什么检查|常见越级|
|---|---|---|
|形式 / formal|定义、公理、推导、可检查证明、反例|有限模型SAT变成世界真值|
|报告 / reported|该版本该位置是否确实报告X、上下文是否完整|作者写了X就当X事实无误|
|描述／测量 / descriptive & measurement|观察单位、构念、测量流程、校准／误差、选择机制|代理信号变成功能或临床终点|
|统计 / statistical|估计目标、独立单位、分母、缺失、多重性、模型、精度|P显著变成效应可靠、样本数变成独立n|
|因果 / causal|可辨识假设、设计、混杂／选择／干预版本、竞争解释|相关或聚类变成因果机制|
|外推 / transport|目标域、效应修饰、覆盖、测量可比性、桥接证据|体外→人体、年轻诱导→自然老化|
|决策／规范 / decision & normative|净益、风险、可行性、价值来源、权利、分配与机会成本|生物改善自动变成生活机会改善|

同一句可能含多类，优先拆分。正文中的“不是因果”“错误解读是X”不能抽成作者肯定了X。

### 2. 正确性是向量，不是总分 / Validity Vector, Not a Total Score

至少记录：

```text
source_support         原文支持
extraction             抽取/数字/单位/符号正确性
measurement            测量与构念效度
statistical_inference  统计推断资格
causal_identification  因果识别
transportability       跨域适用性
net_benefit            净益与实施
independent_review     独立复核
```

每一维用`supported / refuted / mixed / unknown / not_applicable`。断言总体状态用`supported / refuted / mixed / unknown`，**是带范围的人工判断，不是算法事实**。这四种证据状态与V2的四种话语结构标签完全不同。

- `unknown`：未读、数据不可得、上下文不明或检查尚未完成；不等于反对。
- `mixed`：存在实质冲突或限定；不能取平均后“消解”。
- `not_applicable`：确实不适用，必须在评审理由说明；不能拿来隐藏困难检查。
- 所有“支持”都必须回答“支持哪一类主张、在哪个范围、依赖什么假设”。

不要把这8维汇成“92分可信”。同一结论可能原文支持充分但测量效度未知；降低另一维的权重不能补上关键断裂。

### 3. 来源链 / Provenance Chain

```text
实际正文片段
→ 断言ID与角色
→ 来源家族、版本、访问深度与权利
→ 本地原件/可定位原文
→ 数字/语义/设计的比较
→ 人工裁决与其绑定hash
→ 竞争解释和反例
→ 独立复核范围与回执
```

引文是证据入口，不是断言担保；一段尾部引用不自动支持每一句。摘要、全文、补图、XML、代码若来自同一研究，算同一来源家族，不能当多次独立实证支持。下载成功不是读完；读完不是复算；复算不是独立新样本复制。

本项目用“同数据代码计算复现 / computational reproducibility”和“新数据独立复制 / replicability”的区分，参考NASEM定义；领域可能另有用语，需在项目协议中声明。[2](https://nap.nationalacademies.org/read/25303/chapter/6)

### 4. 负向／否定式检查 / Apophatic Audit

依次区分四个问题：

1. 词表是否检出？未检出可能只是漏同义词、分段、否定或领域术语。
2. 图中是否有边？缺边可能是单位、阈值、删高频词导致。
3. 原文是否确实缺少论证？需要看相邻段、整章、跨章和作者目标。
4. 研究领域是否有知识缺口？需要外部检索、已有工作和专家判断。

前一层不能直接推出后一层。把“结构空白 / structural gap”“事实错误 / factual error”“来源未决 / source uncertainty”“可检验问题 / testable question”分开登记。

### 5. 四向深入 / Four Directions of Inquiry

- **向下 / Downward**：概念→操作化→测量→原始数据→代码与仪器；检查聚合和实现。
- **向上 / Upward**：局部效应→系统功能→目标和生活机会；检查跨层推理与净益。
- **向外 / Outward**：不同群体、学科、竞争理论、失败结果和实施环境；寻找范围边界。
- **向内 / Inward**：自己的词表、选择、参数、取源、提示、版本与评审；检查框架如何制造结果。

这四向是问题生成策略，不是声称每轮都穷尽了四个方向。并行搜索按**问题家族**分工，汇合时去重来源依赖；最大并发不等于最大认识收益。

### 6. 竞争解释合同 / Rival-Explanation Contract

每个研究问题最少有：
- 目标系统／人群、比较、终点、时间、估计目标、独立单位；
- 支持解释与至少一个真正可能的竞争解释；
- 两者预测不同的观察、所需数据与测量误差；
- 排除／缺失／死亡／分裂／迁移等事件策略；
- 失败、停止、无法判别的条件；
- 迁移假设、伦理与数据权利；
- 最少新增信息以及为什么优先取得。

不能为填表硬凑8种解释、编效应量／样本量／成功概率。没目标域方差、最小有意义效应与独立单位，就不能从示例细胞数计算人体试验功效。

### 7. 性质挑战比更多“通过”更重要 / Challenge Necessary Properties

常用可执行挑战：
- **重标记不变性 / relabelling invariance**：名义类别换编号不应制造生物距离。
- **分母守恒 / denominator conservation**：从固定基线集合追踪；不能只保留可测幸存者。
- **尺度／单位一致性 / scale & unit consistency**：减幅正数与处理−对照负数不能混作同一CI。
- **绑定敏感性 / binding sensitivity**：改正文或来源后，旧判定必须失效；不能仍引用人工expected常量。
- **对称复核 / symmetric scrutiny**：支持和反对、新旧版本用同样标准；版本章节不相同时不用同编号机械对齐。
- **来源依赖 / source dependency**：同家族PDF和XML一致不是独立复制。
- **停止可见 / visible stop conditions**：没有数据、权限或关键假设时停止升级结论，而不是继续加引用。

每项性质先证明“为什么对该对象必须成立”。不适用的不变性不能硬套，例如有生物意义的有序剂量不能随意当名义类别交换。

### 8. 欠债与信息优先级 / Debts & Information Priorities

优先考虑会改变核心结论／实施决定的欠债；再考虑可判别性、可合法取得性、所阻塞的下游任务、成本与可逆性。没有校准概率时使用透明的词典序／支配比较，不造伪精确的Expected Value of Information。

推荐分层：
1. **P0：可使既有裁决失效的完整性问题**：正文与人工常量脱钩、来源漂移、单位混淆。
2. **P1：决定主要主张能否成立的证据问题**：测量资格、估计目标、关键源冲突、真实独立复核。
3. **P2：结构／表达／拓展问题**：候选桥梁、欠展开主题、可选功能。

每笔债务必须有：已做什么、未做什么、阻塞原因、下一动作、需要谁或什么、关闭证据。`blocked`不是失败也不是关闭。

### 9. 写作与更新 / Synthesis & Maintenance

先写范围和主张等级，再写结论。以章节／断言为单位组织“主张—理由—证据—限制”，不用末尾统一免责声明替代正文具体纠错。修订为新副本，记录old/new、理由、来源与影响。

源版本／正文／代码／词表／参数变化后，沿依赖图撤销相关判定的当前有效性；不能自动改成反驳，也不能自动重绑成支持。新发表更正即使不改变旧字节也可能影响结论，必须有主动重查计划，hash监控发现不了它。

### 10. 方法外部参考的边界

本框架不是PRISMA、GRADE、PROV或某风险偏倚工具的替代认证。PRISMA 2020明确不是研究质量／方法质量评估工具，不能把填清单当成系统综述正确性证明。[1](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/)

W3C PROV提供关于实体／活动／责任主体的溯源组织方式，本包只借鉴概念，没有输出完整RDF、PROV约束验证或声称兼容认证。见[W3C PROV-Overview](https://www.w3.org/TR/prov-overview/)。

本轮是定向方法参考核读，不是对全部科学方法的系统综述。索引、访问深度和本地历史核读回执见`session/`。


---

## 执行工作流与门槛 / Workflow & Gates

**Gate是流程条件，不是科学真值。** 下表定义建议的人机分工；`templates/`可复制起步。每个阶段可循环返回，不必为推进进度把unknown改成supported。

|阶段|输入|活动|输出|退出／停止条件|负责人|
|---|---|---|---|---|---|
|0 立项 / charter|问题、用途、权限、旧版本|澄清研究类型、目标域、风险、是否允许外部写入|PROJECT_CHARTER、范围／预算|问题可界定；权限不足时只做本地只读|研究负责人|
|1 协议 / protocol|范围、已有阅读|声明探索／确认性、单位、词表、估计目标、评审与更新策略|PROTOCOL与版本ID|探索后制定必须直说，禁止追认为预注册|负责人+方法审阅|
|2 检索 / search|问题家族、数据库能力|正反证、相邻领域、注册／更正、代码／数据；记录query/date/results/exclusion|SEARCH_LOG与来源候选|预算耗尽仍有盲区则登记；不能声称穷尽|检索者|
|3 取源 / acquire|URL、许可、候选|合法取原件，检查HTML错误页/文件类型、校验、家族与版本|artifact ledger、访问深度|401/403停止该路径；保留失败，不绕过|取源者|
|4 盘点 / inventory|冻结正文与来源|块／句／数字候选；人工拆分主张、话语角色和上下文|claim ledger、未覆盖清单|自动候选不是语义全集；覆盖不足公开|抽取者+人工核读|
|5A 结构 / structure|冻结语料、分析词表|共现、真实拓扑、透镜审阅、分段／阈值／seed敏感性|结构候选，不是事实裁决|缺边先查人工误配和构图假象|结构分析者|
|5B 证据 / evidence|断言、实际取到的源|原文／数字／设计／测量／推断／域逐项核读|证据向量、支持／冲突／未知|源内矛盾保留；不能挑值凑结果|证据审阅者|
|6 挑战 / challenge|高风险主张及代码／数据|反例、变异、不变性、竞争解释、真实复算|失败见证、范围受限补丁、未决合同|测试失败先判断是程序、测量还是推断；不得偷换输入|分析者|
|7 研究设计 / design|不能由现数据判别的解释|确定比较、终点、单位、事件、最少信息和停止条件|research contract，不是实验已实施|样本量／伦理不足则阻塞实施|领域与方法专家|
|8 独立复核 / independent review|原件定位、方法、失败例、全部阻塞|真实不同审阅者独立取源、复标／复算、书面意见和回应|review receipt与回应／复审|同助手再跑不是独立外审；缺真实回执则不称正式审定|独立审阅者|
|9 合成／发布 / synthesize & release|断言范围、债务、评审记录|改正文具体错误，保留条件，生成MD/机器账本/归档|draft／provisional pack／scoped reviewed release|阶段包可发；正式审定必须满足声明的外审与证据范围|编辑+负责人|
|10 维护 / maintenance|新正文／源／代码／更正|全文diff、hash、传递失效、定期重查|更新队列与新版本，不覆盖旧版|旧判定stale后人工重审；无实质发现不喊涌现|维护者|

### 并行策略 / Parallel Routing

适合并行：不同问题家族的公开检索、不同来源家族核读、独立反例、独立审阅。必须合流后再检查重复研究、域差异和冲突。

不适合盲目并行：一边修改信任基线一边验收；一边选择参数一边声称确认性检验；同一生成器复制成多个角色后当作独立审阅。

没有“AGENTIC MAX”开关或可指定模型的真实能力时，直接说明；用任务切分与记录提高质量，不假称已切换模型／路由。

### 发布规则 / Release Rules

- **工作草稿 / draft**：可含假说和未知，必须清楚标记。
- **证据阶段包 / provisional evidence pack**：允许主要债务未闭环，但不能把未知写成已证实；可包含复现失败与局部补丁。
- **限定范围审定 / scoped reviewed release**：需要真实范围、断言盘点、证据状态、独立评审和阻塞项处置记录。只对该范围负责。
- **不存在本项目认可的“全书科学正确认证 / whole-book truth certification”按钮。**

CLI的`formal_release_record_check`只检查登记前提，不验证审阅者身份和能力，也不能判断人工是否诚实完成盘点。即便显示记录齐全，仍不叫科学认证。

### 长周期节奏 / Cadence

每轮结束保存：已执行动作、回执、结论变化、未决、下一最小信息。历史本体／参数／正文不可静默覆盖。重跑应该只读旧基线，不通过自动重算expected让失败消失。

新项目如有独立前瞻实验，应在看确认性结果前冻结方案；本Session历史均为阅读后定向研究，不追认前瞻预注册。


---

## 数据合同与状态机 / Data Contracts & State Machines

### 可执行合同 / Executable Contract

`schemas/project.schema.json`是实际JSON Schema 2020-12；同字节副本随Python包安装。它验证字段／枚举／类型，不验证自然语言真实语义。`inspect_project`补充全局唯一ID、交叉引用、精确片段与hash、判定绑定、外审记录范围及发布阻塞检查。

```text
Project 项目
├── artifacts 原件/正文/数据/代码：id path sha256 role family access_depth url version
├── evidence 证据片段：id artifact_id lines_1based_halfopen text
├── claims 断言：id artifact_id lines text kind role critical context evidence_ids assessment
│   └── assessment：state reviewer rationale bound_hashes record_sha256 dimensions
├── reviews 复核：reviewer independence_declared receipt claim_ids bound_hashes claim_record_hashes response_complete
├── debts 欠债：status blocks_formal_release question next_action closure_evidence
└── coverage 覆盖：scope human_inventory_complete candidate_units registered_claims note
```

#### 字节与位置 / Bytes & Locations

- 文件以原始字节SHA-256绑定，UTF-8逐行定位。
- `[2,3)`指第2行，不含第3行；保留换行与空格，不做“看起来一样”的静默归一化。
- 二进制PDF／图片不能塞入文本行号机制。应保留二进制原件hash，另登记提取文本／渲染图的派生活动、页码／bbox；本原型暂不自动验证这种坐标转换。不要把提取文本hash伪称PDF原件hash。
- 一个报告中的同一句在不同地方出现，必须按准确位置绑定，不以全局子串查找代替定位。

#### 账本记录本身也要绑定 / Bind the Record, Not Only the Files

`assessment.record_sha256`绑定断言原句／角色／类型／上下文及所选evidence的ID、位置、原句；修改人群或换成同一来源的另一句，即使源文件hash不变也会使旧裁决失效。`reviews.claim_record_hashes`进一步绑定含assessment的记录，不能将旧外审悄悄迁移到新人工判断。

注意：有意改错语义后又重新签上所有hash仍可能通过机械检查；本包明确测试了这种盲区，结果仍是`scientific_truth=not_computed`。记录签名防无声漂移，不保证审阅者诚实、胜任或语义判断无误。

#### 版本失效 / Version Invalidation

```text
artifact字节变化
→ 该artifact的evidence/claim变为stale
→ 依赖它的claim/综合节点进入review queue
→ 人工重新核读
→ 新的判定绑定新hash
```

若维护者只刷新artifact hash，旧assessment.bound_hashes仍不匹配，测试应报警。若同时人工改所有hash但没有真正核读，机器仍可能被骗；此类责任／身份／语义不能由hash证明。因此“新基线”是显式受治理操作，不是验收脚本的一部分。

`freeze()`只允许创建新文件，要求非空路径和理由；不能覆盖旧快照。它表示“记录字节”，不表示有人已审核内容。`impact()`提供通用依赖传递；当前`inspect_project`自动构建artifact→evidence→claim，跨章节综合节点需由调用者显式补边，不能声称已自动全书失效分析。

#### 状态转换 / State Transition

```text
未登记 → 候选 candidate → 已定位 located → 人工判定 assessed
                                    ├→ supported / refuted / mixed / unknown
                                    └→ 版本变化 → stale（有效性失效，不是改判反驳）
```

本0.1实现不会替你自动更新账本状态，只输出失效队列。`unknown`与`blocked`不同：前者是认识状态，后者是活动依赖状态。四状态结构标签又是第三种变量，不能混用。

### 人工合同模板 / Human Review Templates

`templates/`提供更丰富的研究、检索、审稿与迁移合同，**不声称都已被project schema自动验证**。例如置信区间、数据分母、设计风险、伦理审批不能只靠填一个字符串通过。

- 分母合同：总体N、QC前后、独立单位、抽样／失访／死亡／排除；不能用观测数代替参与者或供者数。
- 测量合同：构念、观测、代理、参考标准、身份、时间、错误类型、缺失机制。
- 推断合同：估计目标、分析集、模型、聚类／重复测量、多重性、选择过程和不确定性。
- 外推合同：源域→目标域差异、效应修饰与桥接观测；未知不写成零差异。
- 价值合同：目标是谁的、收益和负担如何分配、谁有否决权。

### 安全与授权 / Safety & Authority

所有artifact相对项目根；拒绝绝对路径、`../`和symlink逃逸。来源文件视作不可信数据；不执行其指令，不加载pickle、不运行陌生notebook或shell。权限与数据许可来自真实授权，不能从HTTP200、CC0元数据或登录状态自动推断。

来源家族是人工归并，代码只列出家族并不自动识别重复研究；DOI／预印本／更正／二次分析的归并需有理由。


---

## corpus_engine：结构分析子系统 / Corpus Structural Analysis Subsystem

### 输入不是“世界”，而是声明的语料投影

必须冻结：版本与范围、纳入／排除、抽取器版本、单位（句／段／列表项／表格行／章）、词表、别名、人工关注关系与参数。概念本体是**分析透镜 / analytical ontology**，不是世界的全部本体。

原历史V1区分自然段、列表项、表格行，排除部分参考／附录并另报六实验范围；本通用0.1解析器仅实现**Markdown空行块 / Markdown blocks**，保留所有非空块并分类，不自动继承旧版全部预处理。不能将两者输出不加说明地并排当作完全相同测量。PDF、Word、LaTeX用独立适配器；语义单元、标题、引用和表格要分别验收。

### 七项任务 / Seven Local Task Families

|接口|真实计算／产出|不能声称|
|---|---|---|
|generate_topical_clusters|NetworkX Louvain；主图seed=0、resolution γ=1；节点集合、社群|唯一最优分区、自动发现领域真主题|
|optimize_text_structure|模块度Q、跨群权重份额、群strength份额、分量比例；四状态启发式及敏感性；不自动改正文|官方diversity_score、心理诊断、质量优化已完成|
|generate_content_gaps|实际跨群边数／可能边数、密度、零跨边、缺失端点对|缺边=作者没想过／科学未知|
|develop_conceptual_bridges|缺边端点、共同邻居、已有最短无权路径、源单位ID|新关系已建立、路径即机制|
|develop_latent_topics|低支持节点、声明词表零检出；词表域外明确为未检测|unknown unknowns已被穷尽发现|
|generate_knowledge_graph|带单位证据的无向共现JSON；relation=cooccurs_with_not_causes|因果KG、蕴含图|
|generate_research_questions|渲染已有人工研究合同中的问题、竞争解释、判别观察、下一信息和停止条件|自动创新性认证、自动实验方案已有效|

`src/research_assurance/tasks.py`包含实际可调用接口。保留历史方法对应关系，但不是InfraNodus API、并未调用其服务。

### 拓扑定义 / Topological Definitions

- 边权：共同命中的单位数；同单位重复出现不重复计权。
- strength：加权度；介数用distance=1/weight，不把大权重误当长距离。
- participation coefficient：`1 − Σc(s_ic/s_i)^2`；只是话语连接模式。
- 集群对密度：实际边数 / 两群节点数乘积；与跨边权重不同。
- 真实孤立点：检出过但当前图无边；零检出词表项另列，不能把它们当实际出现的孤岛。
- 最短路径：当前图的无权路径；桥梁候选不是新边的科学证据。

代码报告Q时统一使用γ=1评估分区，即使Louvain优化用了另一resolution。历史V2另报优化目标Q_objective，本0.1不输出该值，不能误认为两者相同。

### 四状态 / Four Local Structural States

完全公开继承历史阈值，仅作未验证话语结构标签：
1. 非最大分量节点比例>0.20，或Q≥0.55且跨群权重份额<0.10：`dispersed`。
2. 否则最大群strength份额≥0.60且Q<0.25：`biased_single_cluster_dominance_only`。
3. 否则至少3群、Q≥0.30且最大群strength份额≤0.50：`diversified`。
4. 其余`focused`；空图`not_applicable_empty_graph`。

`biased`在这里**只表示单群主导，不表示作者认知偏见**。分类稳定也不证明量表有效；不能为了得到“diversified”而往正文填无意义概念。

### 敏感性 / Sensitivity

通用示例实际运行seed=0/1/2 × γ=.75/1/1.25 × support≥1/2，共18项；另输出prose-only主图。ARI仅在节点集相同时比较，节点集不同返回null，不悄悄取交集冒充整体稳定。

历史V2范围更广：seed0–19、5种构图模式含余弦、删宽泛hub等。本通用0.1**没有声称已移植全部模式**。新项目应按风险扩充分段、词表、权重和阈值对照；保存本体变动理由，不能看结果后偷改词表。

### 人工透镜审计 / Lens Audit

每个透镜记录：为什么适用、原文位置、观察、反解释、未覆盖和裁决。允许“不适用”，不得为了“十透镜齐全”硬造形式逻辑、博弈均衡、现象学访谈或心理诊断。

有修辞效果不代表论证有效；有规范理由不代表临床获益。对支持者与反对者采用相同外推标准，保留作者原声，不用夸大缺陷来证明工具有用。


---

## 测试与证明边界 / Validation & Proof Boundaries

### 六种证据不要混读

|种类|实际证明范围|不证明|
|---|---|---|
|Schema/ID/路径/CRC/hash|文件合同、位置和字节是否按登记一致|原件诚实、语义正确|
|回归／变异测试|构造错误是否被特定程序发现|全书全部错误都能发现|
|性质／不变性测试|所需性质在被测输入／变换下是否成立|该性质足以保证科学有效|
|同数据代码计算复现|给定输入／环境下输出一致|独立新样本复制、测量效度、世界真值|
|新数据／外部域复制|特定研究问题上的新样本一致性及不确定性|绝对真理、所有目标域净益|
|真实独立审阅|另一审阅者对指定范围的挑战和回应|审阅无误、全书认证|

所有软件check名称应尽量指明性质，而不是`content_is_true`。预期缺陷被成功复现也是测试通过；必须说明被测系统实际失败，不能把“15个预期观察确认”改写成原管线15项健康通过。

### 本包测试策略

`tests/test_toolkit.py`包含正向和破坏性fixture：
- 来源字节变化→断言stale；只刷新source hash不能让旧人工判断自动恢复。
- 旧抽样片段外新增句→正文hash／全文diff可见。
- 引句、行范围、未知evidence、重复ID、覆盖数不一致、元数据冒充正文证据。
- 路径穿越／symlink逃逸、新快照拒绝覆盖。
- 假自我独立、缺回执、旧版本审阅、发布记录齐全也不叫科学认证。
- 两两SAT但整体UNSAT；空模型和搜索预算耗尽unknown；JSON布尔与整数不混同。
- 名义重编码、缺失不当作真实状态、固定founder分母、加权聚合反例。
- 英文别名边界、真实缺边、阈值造孤点、社群计数、ARI节点集变化、空图状态。

构造反例不是对原论文的经验影响估计。用测试驱动边界收紧，而非用数量制造“医学可信度”。

### CSP与H⁰ / Compatibility Is Not Truth

主接口改为`finite_global_compatibility`。历史别名`h0_global_section_exists`保留便于追踪，不表示计算层、限制映射、上同调群或统计零假设。

返回：
- `sat`：已编码有限关系有全局兼容赋值；
- `unsat`：该编码集无兼容赋值；
- `unknown`：模型无效、空模型或预算／递归限制。

每次同时返回`external_truth=unknown`。上下文键仍必须人工对齐；错误分离版本键能藏冲突，错误合并不同人群能造冲突，求解器不会替你理解研究对象。

### 自身软件复现 / Self-Reproducibility

本轮验收脚本在两个hash seed下运行测试和CLI，并比较派生结果字节；临时目录迁移测试验证无绝对路径依赖。不是独立科学复现。

历史V6第一次独立目录复现因未排序glob造成数组顺序差异，后来显式排序修复且保留失败回执。这一教训被移植为：输入顺序显式、集合输出排序、与真值基线分开、首次失败不删除。本轮如有新失败，记录在`results/VALIDATION.json`和修复说明，不许只改expected成输出。

### 外部效度尚未验证

通用化本身是新假说：这套过程可能提高可追踪性，但是否降低真实研究严重错误、以何种成本、是否使研究者过度保守，需要跨项目实测。

建议前瞻评价：多学科项目、预定义严重错误和覆盖／耗时指标、独立盲评、比较常规流程与工具流程、记录漏检／误报／新增负担。工具参与者不能自己充当唯一金标。没有这些数据，不写“经验证的通用科学深度研究框架”。


---

## 面向不同作品与学科的适配 / Adaptation Profiles

### 不变内核与可替换适配器 / Invariants vs Adapters

**不变内核**：断言带上下文、来源可追踪、判断绑定版本、角色不误读、未知不当零、失败保留、独立性不伪造、变化需复核。

**必须适配**：测量构念、证据等级、估计目标、独立单位、研究伦理、语料单位、权威来源、风险偏倚工具、发布规范。通用化应移植“要问什么”和“不能越哪一步”，不是把细胞追踪规则强加给所有领域。

|场景|主要审计对象|额外要求|不能照搬|
|---|---|---|---|
|科学深度研究 / scientific deep research|问题地图、主张、竞争证据和判别需求|检索日志、失败搜索、来源依赖、研究合同|把开放式定向搜索叫系统综述|
|长篇专著 / monograph|跨章主张、概念一致性、论证与价值桥接|稳定段落ID、章节依赖、版本对称、作者目标与读者任务、重复／遗漏人工裁决|为了高图密度强行连所有章节|
|实证论文 / empirical paper|问题—设计—数据—估计—结论链|协议／探索与确认分开、数据权利、完整分析集与选择过程、适用报告规范|先看结果再称预注册、把test反复用于选择|
|综述 / evidence synthesis|检索、纳入、风险偏倚、研究依赖和综合|协议、数据库检索能力、去重／筛选记录、适用的PRISMA扩展及独立筛选安排|只有PRISMA checklist就当方法质量通过|
|形式理论 / formal theory|定义、公理、证明、反模型|证明依赖、边界条件、形式化与自然语言映射|要求每个定理有临床样本；把有限SAT称完整证明|
|社会／人文学术 / social & interpretive work|概念、史料、诠释、论证、价值与权力|来源立场、翻译、时期语境、反诠释与研究者位置|用共现频率替代文本解释、把人的意义变成未验证分数|
|计算／AI论文 / computational research|数据来源、切分、泄漏、实现、指标和外部域|个体／场景／时间分组、训练选择与最终测试隔离、环境、安全、基准污染|随机图像切分自动等于跨供者泛化|
|物理／化学／工程 / physical & engineering research|仪器校准、单位、边界、仿真和误差传播|量纲、守恒、参考标准、工况、模型失配与安全裕度|将生物学死亡代理直接搬成工程失效定义|

### 长篇专著的三张图 / Three Graphs for a Monograph

1. **共现结构图 / discourse cooccurrence graph**：哪几个概念在哪些单位共同出现。
2. **论证依赖图 / argument dependency graph**：主张依赖哪些理由／假设；边需人工标注支持、反驳或限定。
3. **证据来源图 / provenance graph**：哪些研究家族／数据／代码支持哪些主张。

因果图如需要另建，不能从前三张自动推出。本包实际计算第一张并提供第三张的简化依赖失效；第二张的语义边与因果图尚未自动实现。

### 从旧项目迁移的最小步骤

1. 只复制不可变原稿与合法来源；不复制旧判定当新域金标。
2. 填PROJECT_CHARTER，界定作品类型和真正要回答的问题。
3. 设计该领域的语料适配器和分析词表；看过文本后设计就直说。
4. 定向抽样高风险断言起步，报告明确分母与未覆盖；不要假装零成本全书核验。
5. 用本领域已知错误／反例测试工具，估计误报／漏检和人工成本。
6. 外审检查方法迁移本身，而不仅检查最终文笔。

轻量模式只用来源账本、精确片段、竞争解释与债务；高风险模式增加完整盘点、原始数据、独立复标与外审。不是每本书都值得先做复杂网络，也不是任何问题都可在缺原始数据时继续计算。


---

## V1–V6谱系与真实能力 / Lineage & Actual Capabilities

本表根据本轮实际核读本地协议与代表实现建立，不把用户回忆清单当代码存在证明。旧版本保持原样，通用包不回写旧通过状态。

|历史版本|当时解决什么|代表产物|关键边界／教训|
|---|---|---|---|
|V1 / v1.1|冻结语料、类型词表、共现、否定式扫描与定向人审|ANALYSIS_PROTOCOL.md、corpus_ontology.py、apophatic_scan.py、manual_review.json|分析本体不是世界本体；词表零命中不是概念不存在；对V6/V7并非全部分析完全对称|
|V2|对称复核、真实拓扑、七任务本地对应、研究合同|topology_engine.py、analysis_tasks.py、argument_surface.py、rhetorical_reviews.json、implementation_bridges.json、lens_audit.json、selection_sensitivity.py、scenarios.json|Louvain与敏感性在此加入；不能回填到V1。四状态本地阈值未验证，不冒充InfraNodus|
|V3|结构缺口、事实候选、可追踪修订、有限全局兼容|structure_audit.py、fact_consistency.py、claims.json、research_design.py|H⁰以有限CSP操作化，未构造完整层上同调；build_sections人工常量未与当前正文同步|
|V4|从自洽到有证据支持的正确；纠正global section误释|content_verifier.py、identification_checks.py、mutation_tests.py、OWED_DEBTS.json|global section是全局截面不是章节。源绑定／篡改测试；SAT不等外部真值。来源家族不当独立证据|
|V5|实际公开数据复算、源闭环、片段门禁与访问资格|analyze_public_data.py、verify_content.py、version_audit.py、研究回执|独立bulk不等每个单细胞配对金标；源表Pearson系数差异未解；不删异常点凑图|
|V6|官方代码版本、隔离缺陷、名义度量与死亡代理、全文diff|research_audit.py、document_change_guard.py、test_and_propose.py|原代码两函数／shell问题不证明发表结果已受影响；重编码反例不推翻真实分群；全文diff不验未改内容；外审仍欠|

### 版本纠偏 / Version Attribution

用户列出的清单覆盖多个历史轮次；`topology_engine.py`、`argument_surface.py`和七类任务接口的实际实现集中在V2，并非都已存在于V1。V1–V6是**Session迭代记录**，不是六个完整独立科研产品，也不是作品V6/V7的编号。

通用工具包0.1重新组织实现：

|历史路径／概念|通用承接位置|移植程度|
|---|---|---|
|extract_corpus.py / corpus_ontology.py|src/research_assurance/corpus.py、examples/toy/ontology.json|简化Markdown block适配器与声明别名；不含历史完整行拆分|
|apophatic_scan.py|corpus.apophatic_scan|真实词表零检出／预设连接检查；人工语义裁决保留|
|topology_engine.py / analysis_tasks.py|topology.py、tasks.py|七接口、主拓扑、18项参数敏感性；非历史全部300模式|
|argument_surface / rhetorical_reviews / lens_audit|templates/LENS_AND_RHETORIC.md、skills/03-corpus-topology/SKILL.md|人工审阅合同；未伪称已实现通用修辞语义解析|
|implementation_bridges / scenarios / research_contracts|templates/RESEARCH_CONTRACT.md、TRANSFER_AND_IMPLEMENTATION.md、SCENARIO.md|通用合同，不搬用衰老项目结论|
|selection_sensitivity.py|topology.sensitivity + docs/05_CORPUS_ENGINE.md|实现seed/resolution/support；其他选择敏感性须按项目扩展|
|fact_consistency / h0_global_section_exists|consistency.py|有限CSP重写，明确scope；历史名保留别名，不再误释|
|source-bound gate / verify_content|core.inspect_project|人工裁决绑定实际文件版本／精确行号与来源片段；不做自动蕴含判定|
|document_change_guard|core.document_diff、impact|全文改动登记与通用依赖失效；不验原文真值|
|研究源码审计／标签反例|measurement.py、skills/06-reproduce-and-challenge/SKILL.md|通用性质函数与安全审计程序；不捆绑执行第三方程序|

### 不能遗失的历史失败

1. “global section=章节”曾是错误解释，已公开纠正；新增免责声明不替代具体纠错。
2. 人工常量即使自洽，也可能与正文实际改动脱钩；需源文绑定和变异测试。
3. 片段级hash漏掉片段外新增句；全文diff补上的是变更覆盖，不是科学语义覆盖。
4. 同一研究多载体不构成独立复制；Crossmark current和updates0不解决源内冲突。
5. 代理死亡、幸存者选择、copy/capture加权、伪供者配对和名义数值距离可能使目标不可识别。
6. 本项目自身未排序glob曾造成独立目录字节复现失败；修复与失败回执均保留在历史V6。
7. 1050结构候选仅既有10对定向人审；软件计数不能扩大成人工覆盖。
8. 正式独立外审从未因多次自查或新测试而自动发生。

本轮核读索引与hash见`session/HISTORY_REVIEW.json`，完整旧原件不重新分发进通用包。


---

## 已知边界与框架自身债务 / Limitations & Method Debts

### 当前已知 / Known Limitations

- **非自动真理裁决器**：精确引用同一段虚假论证也能通过字节检查；人工蕴含／设计评审可错。
- **身份／独立性不可机器保证**：review记录的姓名、独立声明、回执字符串与回应状态都需真实治理；不同模型或不同提示不自动独立。
- **覆盖依赖人工定义**：human_inventory_complete是声明，不是算法证明。块数、数字命中数、词表节点数都不是全书事实总数。
- **正文适配器有限**：当前Markdown空行块不完整解析嵌套列表、复杂表格、脚注、LaTeX和PDF；引文／否定／跨段推理仍需人工。
- **领域适用性未实测**：尚无跨领域比较试验、独立盲评、误报／漏检或成本效益数据。
- **拓扑启发式未校准**：四状态阈值是历史操作化；图稳定不等概念测量有效，结构优化可能损害论证。
- **源码缺陷的影响需数据**：函数／语法问题和论文实际运行结果之间有版本、环境与分析集距离。
- **时间新颖性无法由本地hash发现**：未改旧原件也可能被新研究或更正击败，需要外部更新计划。
- **无完整标准适配**：不是PRISMA／GRADE／PROV兼容或认证实现；无完整风险偏倚、数据权利、伦理与功效求解。
- **工程安全有限**：防路径逃逸不等隔离任意恶意代码；不要执行未信任来源，不用此工具处理未授权敏感数据。

### 自身债务 / Toolkit Backlog

|ID|优先级|未偿任务|关闭证据|
|---|---|---|---|
|M01|P1|真实独立方法／代码审阅|独立取源／复跑、意见、回应、必要复审；目前未发生|
|M02|P1|至少两个非衰老领域试点|真实输入、人工金标、错误／误报／耗时及失败分析；构造例不算|
|M03|P1|断言盘点与语义蕴含的覆盖评价|预定义范围、独立标注和漏检评估；不能把模型自评当真值|
|M04|P2|二进制原件→页码／bbox→提取文本的溯源适配器|PDF/图/表定位的可核映射与困难例；当前不实现|
|M05|P2|论证／因果图与结构图分型接口|人工边型、来源与反例验证，防止共现升级|
|M06|P2|扩展稳定性／边界测试|复杂Markdown、多语言、打包安装、不同平台、历史全敏感性模式|
|M07|发布前|权利与许可／维护责任|权利人决定许可证，上游再分发核查、维护者与贡献规则|

“通用”的含义目前是**设计目标和可复用接口**，不是经验证所有学科都有效。该限制必须跟随工具被复用，不能从主README删除后只留在附录。

### 未知的未知 / Unknown Unknowns

只能记录发现渠道：外部对手审阅、异常样本、失败复现、跨域差异、用户反馈、与其他方法的冲突。不能列一张概念表后声称unknown unknowns已被扫描完。每发现一个新失败模式，写成可重演问题并更新测试，而不是只新增一句“注意风险”。


---

## Session技能提炼与取舍 / Skill Distillation & Selection

这里的10个新子Skill是按研究活动重新设计的合同，**不是原参考10个Skill的一一复制或再许可版本**。原参考文件留在旧工作区，不随本包分发。原Skill是方法灵感，不是医学证据或心理／认知量表验证。

|Session参考技能|保留并工程化的做法|明确不继承／不升级|
|---|---|---|
|scientific-brainstorming / 科学头脑风暴|发现、证据评估、验证与决策分离；保留竞争解释与少数意见|头脑风暴不验证假说，不自动伦理批准或评出“赢家”|
|critical-perspective / 批判视角|质疑前提、寻找反解释、对自己的框架反审|不是为了反对而反对；未知不默认负面|
|shifting-perspective / 视角转移|根据实际结构提出深入／桥接／换域候选；先核工具能力|无外部服务不捏造其diversity_score；本地算法和分数独立命名|
|cognitive-variability / 视角与尺度变化|向上／下／外／内切换、收敛与发散交替|话语图四状态不诊断作者认知；不由标点或疲劳词推断心理状态|
|rhetorical-analyst / 修辞分析|说服、修辞结构、逻辑支持分开；对双方同标准|不把高说服力当真实因果／临床支持；无读者实验不报真实说服效果|
|ontology-creator / 本体生成|实体／概念／关系分型；显式声明分析透镜|不用固定关系配额迫使编造；wikilink不使共现成为因果KG|
|perspective-reversal / 反向视角|从最强竞争解释和对立假说看问题|不继承“对手必恶意”的预设，也不把战术角色扮演当科学证据|
|what-if-oracle / 情景分析|明确假设、扰动、决策触发、二阶后果与停止分支|故事不是校准预测；DOI／预印本存在不证明情景方法有效；不赋假概率|
|vipassana-meditation / 非反应式观察|观察先于命名，对支持与不利证据同质量注意；愿意撤回旧结论|仅作为注意与记录启发，不声称模型有禅修／意识，也不当经验证科学理论|
|writing-assistant / 写作辅助|保留作者声音、最小必要修订、同语言与格式|不采纳由文体诊断心理；不以规避AI检测或隐藏协助来源为目标|

### 从提示到Skill / From Prompt to Skill

一个可复用Skill至少包含：

```text
trigger       什么情况下调用
inputs        必要输入与未知
procedure     可执行步骤及人机责任
outputs       文件／账本／分析合同
stops         权限、数据、方法与安全的停止条件
acceptance    哪些性质实际被检查、哪些仍需人工／外审
handoff       下一技能、专家或数据依赖
```

单句“请批判性深入研究”不能代替这些。反过来，Skill文件本身也不自动带来可执行能力：需要真实工具、环境、数据和授权。适合机器检查的内容落到schema／测试；语义与价值判断保留可追踪人工责任。

### 对本Session的递归应用 / Reflexive Use

本框架也接受相同标准：其名称是建议名，不是学术共识；跨域通用是待检验目标；代码测试不证明方法有净益；总Skill不能替自己填独立外审回执。当前只能交付“可运行工程草案与方法提炼”，不称已经完成独立审定的方法学新范式。


---

## 中英文关键词 / Bilingual Glossary

|中文|English|本项目含义／防混淆|
|---|---|---|
|认识论约束|epistemic constraints|何时有理由相信／撤回主张；不是新哲学学派|
|研究工程|research engineering|把方法约束变为可追踪、可执行、可维护的实践|
|研究论证保障|research assurance|组织有范围的理由、证据、挑战；不是保证真理|
|方法论|methodology|选择和论证研究方式的原则体系|
|协议|protocol|某项目具体规则；探索后协议不等预注册|
|工作流|workflow|活动顺序、并行、依赖、门槛与反馈|
|技能|skill|有触发器、输入、步骤、产出、拒绝条件、验收的可调用执行合同|
|分析本体／透镜|analytical ontology / lens|人为界定的概念／别名／关系视角，不是世界本体|
|否定式审计|apophatic audit|检查缺失的不同层次；不由零检出推出不存在|
|断言／主张|claim|带角色与上下文的可评估语句|
|证据溯源|provenance|原件、版本、生成活动、责任主体与依赖链|
|来源家族|source family|同一研究的PDF/XML/补图/代码等相关载体|
|推理担保|warrant|为什么证据允许推出主张的理由|
|潜在击败条件|defeater|什么证据／假设失败会削弱或推翻论证|
|结构空缺|structural gap|某种图投影中的缺边／断连，不等语义或科学未知|
|共现图|cooccurrence graph|同一声明单位共同出现的无向连接|
|论证图|argument graph|人工有类型的支持／反驳／限定依赖|
|因果图|causal graph|具有因果语义和识别假设的模型，不从共现自动得到|
|全局截面|global section|不是章节；本项目历史上仅用有限全局兼容赋值作操作化|
|有限约束满足|finite CSP satisfiability|编码关系的兼容性，不是外部真值|
|源文绑定|source-bound verification|正文／证据精确片段与版本绑定，不是自动自然语言蕴含|
|变异／篡改测试|mutation / tamper testing|故意改坏输入，检验某检查是否响应|
|变形测试／不变性|metamorphic testing / invariance|在有理由预期不变的变换下挑战输出|
|计算复现|computational reproducibility|本项目采用同数据／方法／代码重算定义，需声明领域用法|
|独立新数据复制|replicability|新研究／新数据对同一科学问题的重复检验|
|适用性／可迁移性|generalizability / transportability|从源域到目标域的条件，不因图稳定而成立|
|独立统计单位|independent statistical unit|供者／实验单元等；不同于图像／细胞／重复观测数|
|估计目标|estimand|在何人群／系统、条件、终点、时间和事件策略下要估计什么|
|代理终点／参考标准|proxy endpoint / reference standard|代理不能与独立真值循环互证|
|固定基线原始单元|baseline founder|不能将分裂后代或可追踪幸存者重新定义成全部基线|
|缺失／失追踪|missingness / lost tracking|未知事件，不自动死亡或成功|
|净益|net benefit|收益、风险、成本、机会与价值的有条件权衡|
|认识债务／欠债|epistemic debt / owed debt|尚未满足的证据／推断／复核条件，有动作与关闭证据|
|阻塞|blocked|活动无法继续；不是科学反驳，也不是关闭|
|过期／失效|stale / invalidated|旧判定不再绑定当前版本，需重审；不是自动改判|
|阶段证据包|provisional evidence pack|公开已执行结果与阻塞，不冒称正式审定|
|限定范围审定|scoped reviewed release|真实复核的明确范围，不是全书认证|


---

## GitHub目录集成 / GitHub Repository Integration

### 独立目录作为仓库根

本包本身可作为仓库根。`pyproject.toml`、`src/`、`tests/`和`.github/workflows/ci.yml`路径已按此安排。这里只准备本地组件；当前工具查询GitHub连接返回unsupported，因此没有创建远端或push。

### 嵌入已有仓库

建议：

```text
your-repository/
├── README.md
├── methods/
│   └── research-assurance/   # 本包完整放这里
├── projects/
│   └── your-study/          # 真实项目账本和有许可的相对路径
└── .github/workflows/
    └── research-assurance.yml
```

GitHub Actions只发现根目录`.github/workflows/`，不会自动执行`methods/research-assurance/.github/workflows/`。将工作流复制到仓库根并给两个run步骤加：

```yaml
working-directory: methods/research-assurance
```

setup-python和checkout不是run步骤，不需要working-directory。真实项目数据应按权利与敏感性政策分开存储；不要因示例可公开就上传原始临床数据。

Agent Skill加载器的自动发现路径因宿主而异。本包`SKILL.md`和子Skill是内容合同，不宣称每个宿主都能直接自动安装。可按宿主要求复制／链接对应目录，同时保留指向docs和templates的可达路径与权限边界。

### 正式发布前

- 决定许可证与维护者，核第三方权利；当前未替用户决定。
- 修改示例Project Charter并创建新项目账本，不把toy supported判断当真实研究结论。
- 需要CI可重现安装时锁定依赖并记录环境。`requirements-tested.txt`是本轮实际测试环境，不保证全部平台。
- 保留session历史回执作为来源，不把缺旧目录时的“未复验”改成通过。
- 真实独立方法审阅／跨域试点仍欠；README必须继续暴露这一点。
