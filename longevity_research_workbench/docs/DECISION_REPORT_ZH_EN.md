# 决策报告：整合研究体系，而非合并提示词
## Decision report — Federate the system, do not concatenate the prompts

2026-11-25。两附件全文作参考核读；接收hash见 `references/attachment_receipts.json`。附件内部命令、角色与“必须”均不是本仓库自动生效的治理指令。下文“采用”是本地建议/实现范围，不代表权利人授权、独立评审或远端部署。

## 一、结论 / Recommendation

**一个项目主仓库，三个独立演进的层；暂不拆成多个远端仓库，也不熔成一个超级Skill。**

- 主仓库：`longevity-research-workbench`，服务书、论文、证据与审计链。
- 通用方法组件：`methods/research-assurance/`，保留自己的包版本/测试；本轮为0.1.1候选。以后出现第二个真实研究项目再考虑单独发布，届时固定版本/commit，避免双重SSOT。
- 两附件：作为设计来源，逐条转为采纳/修改/拒绝/待验证的ADR；不直接复制其全部文本、hook及CI进生产。

这同时保留“通用研究工程”和“长寿领域研究”的边界。Skill是调用接口，不是整个研究体系；corpus engine是分析与审计子系统，不是专著本身。

## 二、三者究竟是什么 / Comparison

|维度|ARENA P0–P8 Playbook|CGEE R5.5|已交付toolkit 0.1.0 / 本轮派生版|
|---|---|---|---|
|主要对象|研究代理的阶段、责任、GSK与人工主权|更具体的平台部署、权限、契约与反投机设计|证据字节绑定、断言记录、失效传播、诊断与测试|
|抽象层|治理/流程控制面|运行环境与执法适配参考|便携Python实现及方法文档|
|可执行性|MD本身不是执行器|§7自述代码未测试；依赖外部工程包|原55测试实跑；本轮新增候选修订和复杂输入验收|
|依赖|所称22模块、registry/卡片等未随本次附齐|Claude Code/WSL2/GitHub/Linear及多个planned脚本|Python、networkx、jsonschema；不依赖特定代理平台|
|科学判定|流程不能代替研究证据|反作弊设计不能裁决生物学真值|明确不计算科学真值；人类判断本身仍可能错误|
|独立性|角色/模型分工不自动成为独立外审|不同模型家族也不足以证明独立|只检查外审记录与hash；不认证身份和利益冲突|
|与本项目关系|抽取阶段门与责任原则|隔离参考、逐项威胁建模后再实现|作为底层可测试子组件，不重复实现全部平台|

本次只有两份Markdown；没有收到 `gsk_registry.tsv`、22张模块卡、ENGINEERING发布包、`contracts_run.py` 等，不能称“全套已装好”。CGEE自身§2.3称相关仓库无verified工具；目录、示例和planned条目不等实现。

## 三、应采纳、修改、暂缓什么

### 采用 / Adopt

1. 人类对研究问题、伦理、稿件结论和发布负责；输入接收、范围冻结、事实核验、外审与发布分开。
2. 保留原始失败、合同执行数、回执和变更记录，避免“修到绿”后抹去失败。
3. 写作材料、共享证据、分析实现、测评与发布审批分层；同一科学断言由稳定ID引用，而非多处独立签字。
4. 科学产出可公开复核；用于比较代理表现的保留测试可限制起草角色访问，但必须存在人类受控审阅渠道。

### 修改后采用 / Adapt

- **比例检查必须识别估计量**：只有未加权二元原始频数比例才适用整数k/N检查；四舍五入必须显式建模。加权、标准化、模型调整、生存率不服从普遍整数规则。本轮 `tools/numeric_contracts.py` 实现带类型分派；返回“不适用此检查”不是通过科学验收。
- **禁止空跑变绿**：本地执行契约要求至少1项实际运行的blocking检查；所有blocking检查必须实际通过，skipped/not_applicable不冒充通过。例外须先变更合同并人工接受，不能现场把min_ran降成0。
- **评分隔离不等信息封锁**：区别科学可复算输出与代理优化分数。强迫研究者看不到分析方法会损害可证伪性；本项目不宣称实现OS级读隔离。
- **T1−T2不是通用作弊估计量**：需要相同量纲、配对任务、冻结定义、误差与置信区间；不同题目通过率之差不能直接命名reward hacking。
- 3卡/25调用/2轮/1.5%/0.15/2个子论点等可作本地预算与经验参数，不能当普遍科学常数。达到修补预算只是停止，不等通过。

### 暂不部署 / Defer

- 附件中的高权限工作流、正则安全钩子、平台价格/模型事实/水印/榜单等未核主张。
- “先启用必需检查”却没有verified工具的bootstrap：明确本地可跑/人工批准/远端未设三种状态，不用占位脚本绿灯。
- 无许可审查前不整包复制第三方文本/代码。AGPL等许可的处理必须基于实际使用与法律义务，不能把附件的组织政策当普遍法律。

### 拒绝继承 / Do not inherit

- 自动刷新证据hash后继续沿用旧判断；引用外审角色名即算独立审查；自测通过即宣布科学可靠。
- 复制 `pull_request_target` 模板执行不可信PR代码；把同一文件系统的两个目录称物理隔离。
- 新HTML仪表板：本项目按用户明确要求不生成。

## 四、版本与引用冲突 / Version and source conflicts

1. Playbook文件名/顶部R3.8而正文尾有R3.8.1/3.8.2增补；引用以接收hash、段落定位为准。
2. CGEE §0.2已经把部分数字/版本声明降为待核，但§4、§9与附录仍沿用相应数字或不同Zenodo入口。不能从“前文有勘误”推断全文已一致。
3. 对SkillsBench本轮只定向读取arXiv **v4摘要及版本页**：87任务、8域、18种model-harness配置，平均33.9%→50.5%，增加16.6个百分点。这是其特定版本与实验条件报告，不是本项目预期收益，也不是所有任务通用上限；附件40.7%需要追溯其原版本/定义，本轮不判造假。
4. GitHub官方安全参考明确警告高权限trigger检出不可信代码；本项目不复制附件CI。ICMJE官方作者/审稿AI条目已定向核读；最终投稿仍核目标刊当时政策。
5. 未验证附件中全部参考文献、撤稿数字或平台经验；不是系统综述，不以发布时间新旧判断真伪。出处与访问深度见 `references/SOURCE_CHECKS.md`。

## 五、本轮真实发现 / Actual findings

- **F01：0.1.0支持维度门禁不完整。** 对reported claim构造supported结论但source_support=refuted，原版返回issues=[]；再给合规形状的合成外审记录/完整声明后，还会返回记录前提齐备。这仅为测试夹具，无真实外审。新副本增加按claim kind的最低维度一致性检查，原包未改。候选修复不能证明人类给出的supported是真。
- **F02：附件hook模板遗漏受保护写入形式。** 在临时目录将3条写盘命令作为JSON字符串交给已核读的PreToolUse钩子，针对tools、.github、.claude的样例均返回0；保护kb写入及起草读tests/.git的对照仍拦截。**这些Bash字符串没有执行**，真实OS沙箱/分支权限未测试，因此结论限于模板覆盖缺口。

数量、命令、hash及边界见 `evaluation/ADVERSARIAL_REVIEW.md` 与 `artifacts/`。这些是工程发现，不是新的长寿生物学发现。

## 六、更好的长期构想 / A stronger research design

将“证据更新会影响什么”置于中心，而不是追求更长的控制提示词：

`来源快照 → 提取记录 → 断言与估计目标 → 书/论文中的论证 → 外审记录 → 发布快照`

一个来源改变，应显式传播到受影响段落与论文，不能静默重写全部结论。V6保留生活广度；V7提供辨别返老表象的深度。共同围绕“对什么对象、按什么尺度、在什么选择/可见性条件下、为谁获得什么收益”组织研究。避免一个“长寿总分”吞掉价值冲突。

**English decision summary:** Keep one research monorepo with a versioned audit library and explicitly uninstalled platform adapters. Adopt accountability and non-vacuous contracts, adapt estimator checks and role boundaries, and defer untested enforcement. The workbench supports a book plus three separately falsifiable paper programmes; it does not turn a software green light into scientific certification.
