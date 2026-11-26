from pathlib import Path
P=Path(__file__).resolve().parents[1]/'templates'
T={
'PROJECT_CHARTER.md':'''# 项目立项 / Project Charter

- Project ID / 项目ID：
- Research question / 核心问题：
- Intended use & decision owner / 用途与决策责任人：
- Work type / 作品类型：deep research / monograph / empirical paper / review / formal theory / other
- Source domain → target domain / 源域→目标域：
- In scope / 纳入：
- Out of scope / 排除及理由：
- Corpus versions & unit adapter / 语料版本与单位适配器：
- Claim inventory scope / 断言盘点范围与未覆盖：
- Existing knowledge before protocol / 协议前已知与已阅读：
- Exploratory vs confirmatory / 探索性与确认性：
- Permissions / 权限：public read / local write / external write / contact / controlled data（逐项授权；默认无外部写入）
- Sensitive/dual-use/ethics restrictions / 敏感／双用途／伦理限制：
- Budget, stop conditions & update date / 预算、停止与更新日：
- Independent review scope / 独立复核范围、责任与真实回执要求：
- Output formats / 交付格式：Markdown + JSON + code（本Session不交付STATE_DASHBOARD.HTML）
''',
'PROTOCOL.md':'''# 项目研究协议 / Study & Audit Protocol

## Timing / 时间与先验信息
Created at / 制定时间：
What was already read/analysed / 已读／已算：
Preregistered? / 预注册？默认否；须有真实前瞻登记与版本，不能回填。

## Objects / 对象
Corpus hashes / 语料hash；source families / 来源家族；units / 单位；ontology / 词表及变更。

## Search / 检索
Question families / 问题家族；positive/negative/adjacent evidence / 正反及邻接；databases / 数据库；access limits / 访问限制。

## Verification / 核验
Claim types / 类型；estimands / 估计目标；independent units / 独立单位；missing/event rules / 缺失／事件；reference standards / 参考标准；rival explanations / 竞争解释。

## Analysis / 分析
Parameters fixed before outputs / 输出前参数；sensitivity grid / 敏感性网格；test oracles / 性质依据；not implemented / 未实现。

## Governance / 治理
Stop/failure conditions / 停止／失败；independent review / 独立复核；release scope / 发布范围；amendment log / 修订日志。
''',
'SEARCH_LOG.csv':'''search_id,question_family,query,database_or_endpoint,executed_at_timezone,filters,results_seen,screened,included_source_families,exclusion_reason,access_depth,limitations,next_action
''',
'CLAIM_REVIEW.md':'''# 断言审阅卡 / Claim Review Card

- Claim ID / 断言ID：
- Exact manuscript text & location / 正文原句、版本、行号、hash：
- Role / 话语角色：asserted / hypothesis / rejected_misreading / proposal
- Claim type / 类型：formal / reported / descriptive / statistical / causal / transport / decision / normative
- Context / 上下文：population/system, tissue/site, time, estimand, unit, design, domain, analysis stage/version
- Exact evidence & source family / 精确证据、位置、家族、访问深度、许可：
- Warrant / 推理担保：
- Counterevidence & defeaters / 反证与击败条件：
- Source support / 原文支持：unknown
- Extraction / 抽取数字单位：unknown
- Measurement / 测量：unknown
- Statistical inference / 统计：unknown
- Causal identification / 因果：unknown
- Transportability / 外推：unknown
- Net benefit / 净益：unknown
- Independent review / 独立复核：unknown
- Narrow judgement & scope / 窄裁决与范围：
- Reviewer, versions bound & rationale / 责任、所绑版本与理由：
- Allowed wording / 可写：
- Prohibited upgrade / 不可写：
- Debt & closure evidence / 欠债与关闭证据：

状态为supported/refuted/mixed/unknown/not_applicable；不适用需解释，不合并总分。
''',
'RESEARCH_CONTRACT.md':'''# 研究合同 / Research Contract

- ID & originating claim/source units / ID与起源位置：
- Question / 研究问题：
- Target population/system / 目标系统：
- Comparator & intervention versions / 比较与干预版本：
- Endpoint, timing & measurement validity / 终点、时间与测量效度：
- Estimand / 估计目标：
- Independent statistical unit / 独立统计单位：
- Baseline denominator / 固定基线分母：
- Event strategy / 死亡／失访／分裂／迁移／撤药等事件：
- Main explanation / 主解释：
- Genuine rivals / 真实竞争解释：
- Discriminating observation / 判别观察（若没有则明确无法判别）：
- Measurement error & selection / 测量误差与选择机制：
- Minimum new information / 最少新增信息：
- Variance/effect inputs still unknown / 方差／最小效应待定：
- Failure, stop & inconclusive conditions / 失败、停止、无法裁决条件：
- Transport assumptions / 迁移假设：
- Ethics, rights & feasibility / 伦理、权利与可行性：
- Priority rationale, no invented probabilities / 优先理由，不造概率：
- Status / 状态：proposed_not_implemented

不是实验SOP、伦理批准、功效已计算或新颖性认证。
''',
'MEASUREMENT_CONTRACT.md':'''# 测量资格合同 / Measurement Qualification Contract

Construct / 要测的构念：
Observable / 实际观测：
Proxy / 代理与推断链：
Unit & identity / 单位与身份维持：
Reference standard / 独立参考标准（非同模型插补）：
Time & event definitions / 时间与事件定义：
All-baseline eligibility / 全基线纳入与排除：
Missingness taxonomy / 未测、失追踪、离场、失败与死亡分开：
Validation labels & blindness / 真实标签、复标者与盲态：
Error measures with independent denominators / 错误类型、分母与精度：
Nominal/ordinal/continuous representation / 名义／有序／连续表征与合理距离：
Leakage/split map / 供者／批次／视野／个体／时间切分：
Pass/stop criteria / 由领域专家预设的标准与停止条件：
Status / 当前数据与缺口：

不得将黑色lost tracking默认死亡，不得把代理与自身插补结果当独立互证；其他领域替换具体事件但保留区分原则。
''',
'INDEPENDENT_REVIEW.md':'''# 独立复核回执 / Independent Review Receipt

**未填写不代表已发生 / Blank means no review has occurred.**
- Reviewer real identity/contact or verifiable protected record / 真实身份／可核受保护记录：
- Independence & conflicts / 独立性与利益冲突：
- Received/finished date / 签收／完成日期：
- Scope & versions/hashes / 范围与版本：
- Independently acquired sources / 独立取得来源：
- Recomputed/relabelled/re-read actions / 实际复算／复标／核读：
- Findings, disagreements & failures / 发现、分歧与失败：
- Author responses / 逐项回应：
- Re-review required/completed / 是否需复审及状态：
- What is NOT covered / 未覆盖：

同一助手多轮、自我审查、多个角色Prompt、论文已有同行评审都不自动满足本项目独立复核。
''',
'LENS_AND_RHETORIC.md':'''# 透镜与修辞审阅 / Lens & Rhetorical Review

Lens / 透镜：
Why applicable / 为什么适用（允许不适用）：
Observed source units / 实际原文位置：
Surface clue vs semantic reading / 表面线索与语义核读分开：
Persuasion / 说服效果（若未做读者研究就只记分析假设）：
Rhetorical structure / 修辞结构：
Logical support / 逻辑支持：
Symmetric challenge / 对支持与反对的同标准挑战：
Alternative reading / 反向理解与作者最佳版本：
Uncovered scope / 未覆盖：
Proposed edit with original voice preserved / 保留作者原声的最小修订：

不得由标点／图四状态诊断人的心理、同理心或意识。不得把高说服力当高证据质量。
''',
'TRANSFER_AND_IMPLEMENTATION.md':'''# 跨域与实施桥接 / Transport & Implementation Bridge

Source domain → target domain / 源域→目标域：
Mechanism → function → lived opportunity / 机制→功能→真实生活机会：
Effect modifiers & support / 效应修饰与覆盖：
Measurement comparability / 测量可比性：
Required bridge observations / 必需桥接观测：
Net benefit: harms, benefits, cost, burden / 净益、伤害、成本与负担：
Rights, consent, access & distribution / 权利、同意、可及与分配：
Who decides and who bears error / 谁决定与谁承担错误：
Failure & withdrawal conditions / 失败与撤回条件：
Unknown / 未知：

不创造跨研究同细胞／同供者映射，不因机制漂亮跳过功能与实施。
''',
'SCENARIO.md':'''# 情景压力测试 / Scenario Stress Test

Decision, horizon, system / 决策、时间与系统：
Observed baseline / 已观察基线：
Assumptions / 假设：
Perturbation & coupled changes / 扰动与联动：
Favorable/reference/adverse/contrarian branch / 有利／参照／不利／反向分支：
Observable decision trigger / 可观测决策触发：
Reversible actions & stop / 可逆行动与停止：
Second-order consequences / 二阶后果：
Minimum discriminating information / 最少判别信息：

情景不是预测概率或因果效应估计，不赋无依据的成功率。保留无法判别与不行动分支。
''',
'CHANGE_REVIEW.md':'''# 更新与失效审阅 / Change & Invalidation Review

Change ID / 更新ID：
What changed / 正文、来源、词表、阈值、代码、环境或新外部证据：
Before/after hashes & diff / 前后版本与差异：
Impacted evidence/claims/synthesis / 受影响证据／主张／综合：
Prior judgement state / 旧判定：
New status / 新状态：stale_requires_review（不是自动refuted）
Re-reading/recomputation required / 所需重读／复算：
Reviewer and actual action / 真实审阅者与动作：
New judgement & bound versions / 新裁决与版本：
Debt still open / 仍未偿：

验收脚本不得顺便刷新expected/hash绑定。未变字节也须按更新计划检查新更正。
''',
'DEBT_LEDGER.csv':'''debt_id,claim_ids,priority,status,repaid_scope,remaining_question,next_action,blocking_dependency,owner_or_role,closure_evidence,blocks_formal_release,last_checked
'''
}
for n,t in T.items():(P/n).write_text(t)
print('templates',len(T))
