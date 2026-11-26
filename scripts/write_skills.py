from pathlib import Path
P=Path(__file__).resolve().parents[1]/'skills'
items=[
('01-scope-and-route','范围与路由 / Scope & Routing','立项、研究目标不明、继续历史欠债或多种作品混在一起','问题、用途、旧稿、授权、预算','界定研究类型和源域／目标域；记录协议前已知；区分轻量与高风险模式；优先能改变核心结论的任务；关键歧义才向用户提问。','PROJECT_CHARTER、范围、权限矩阵、优先队列','无外部写入授权就不写外部系统；无真实模型路由能力不假称启用。','templates/PROJECT_CHARTER.md','范围具体、已知／未知／排除与负责人清楚；不把探索后协议说成预注册。'),
('02-search-and-provenance','检索与溯源 / Search & Provenance','需要新事实、原文、注册／更正、源代码或数据','问题家族、数据库能力、已有来源与权限','并行搜索正证／反证／邻接领域／注册更新；保留query/date和筛选理由；合法取源检查实际内容与错误页；登记版本、访问深度和来源家族；明确未搜渠道。','SEARCH_LOG、artifact ledger、访问失败和未覆盖','401/403不绕过；metadata不冒充下载成功；同一研究多个载体不算独立研究。','templates/SEARCH_LOG.csv','每个外部主张有实际读取证据；不声称本轮完成了未重跑的旧查询。'),
('03-corpus-topology','语料与拓扑 / Corpus & Topology','审查专著结构、孤岛、缺边、概念分布和透镜适切性','冻结正文、单位适配器、声明词表、分析目标','先读原文和适配器边界；抽取块与角色线索；算Louvain、Q、中心性、实际跨边／缺边；跑分段／阈值／seed敏感性；回原文审假缺口；分别看修辞、逻辑与作者目标。','结构候选、源单位ID、连续量与不稳定性、人工透镜卡','缺边不是知识未知；低词频不是低价值；不用四状态诊断人；不冒充外部服务分数。','docs/05_CORPUS_ENGINE.md','边有单位证据，零检出另列，假孤点可解释；可运行CLI topology。'),
('04-claim-evidence','断言与证据 / Claim & Evidence','事实核验、修订正文、来源内部冲突、H⁰或内容正确性质询','实际正文片段、来源原件、类型／角色／上下文','拆分原句；定位来源；核数字单位符号分母；按来源支持、抽取、测量、推断、外推等维度评审；绑定正文／源hash；冲突保留；仅在新副本修订。','claim/evidence ledger、窄裁决、精确diff与债务','SAT不等真值；不得以引用存在代替语义支持；不能通过拆不同version键悄悄消除实质冲突。','templates/CLAIM_REVIEW.md','故意改正文／源后旧判定失效；未读／未覆盖保持unknown；CLI check不输出科学正确。'),
('05-measurement-and-identification','测量与识别 / Measurement & Identification','代理结局、追踪身份、缺失选择、分母或因果效应需要评估','测量合同、原始数据资格、分组与参考标准、估计目标','先定义单位／构念／时间／独立参考；区分失追踪与死亡、后代与founder、观测与供者；核capture/copy加权及选择；检查分组切分和因果识别；记录外推条件。','资格裁决、错误分类与真实数据需求、无法识别原因','不借癌细胞／跨周期方差设人体功效；无金标不报真实误差；不做跨研究伪同细胞配对。','templates/MEASUREMENT_CONTRACT.md','解释数据到底能估什么；可用diagnostics演示逻辑但明确构造而非实证。'),
('06-reproduce-and-challenge','复现与反例 / Reproduce & Challenge','拿到公开代码／数据、需要检验必要性质或门禁有效性','原件校验、环境、实际代码、科学性质与范围','静态先于执行；隔离最小函数；显式依赖注入与兼容改动；复算预定义数据集；注入篡改；测试重标记、守恒和参数稳定；保留失败与补丁候选。','可执行反例、环境与回执、非破坏性diff、影响范围','不执行未知shell/notebook/pickle；局部补丁不等完整修复；不删异常点或挑参数凑图。','docs/06_VALIDATION.md','测试可独立运行；“预期失败确认”不写成被测系统健康；构造不等原论文重分析。'),
('07-rivals-and-contracts','竞争解释与合同 / Rivals & Contracts','证据不足以裁决、需要新视角／四向深入或研究计划','已观察现象、候选解释、约束与待决策','向上／下／外／内生成问题；保留不同立场最佳版本；分开发现与评估；找不同解释预测不一致的观察；做有假设的情景而非概率预测；写最少信息和停止条件。','research contract、scenario、判别优先级','不为配额捏造关系；不预设对手恶意；不赋无依据成功概率；研究问题不认证新颖性。','templates/RESEARCH_CONTRACT.md','至少一个真实竞争解释，若不可判别明确写出；实现tasks.generate_research_questions只渲染合同。'),
('08-synthesis-and-writing','合成与写作 / Synthesis & Writing','写长篇章节、论文讨论、修复结论或提出机制／功能／实施桥梁','审阅过的主张、证据向量、读者任务与原作者声音','先定可写结论与禁止升级；区分结果／假说／价值；跨层桥接逐步说明；具体错误在正文修；保持原声与最小干预；附冲突和未覆盖。','有范围MD、修订副本、论证依赖与未偿项','漂亮叙事不替代数据；不因图密度要求连接所有概念；不把文体优化等同规避AI披露。','templates/TRANSFER_AND_IMPLEMENTATION.md','每个主要结论可回到来源与担保；独立外审未做则只交阶段包。'),
('09-review-and-debts','独立复核与欠债 / Review & Debts','发布前、源冲突、长期未决或需要排下一优先级','原件定位、反例、完整欠债与真实审阅者状态','对正反双方同标准；先自查再请求真正独立取源／复标／复算；保留意见与回应；按结论影响／判别力／可取得性／阻塞排序；定义关闭证据。','review receipt（真实才填）、OWED_DEBTS、NEXT_PRIORITIES','同一助手多轮和多角色不当独立外审；blocked不等closed；准备请求不等已发送或签收。','templates/INDEPENDENT_REVIEW.md','每笔债有已偿范围、下一动作与关闭条件；未授权不发外部请求。'),
('10-change-and-release','更新与发布 / Change & Release','正文／原件／词表／参数／代码变化，或新版本准备交付','冻结快照、候选差异、依赖图、验收与偏好','逐字节hash和全文diff；沿依赖图标stale；人工重审而非自动重绑；跑正向／反例／移目录复现；保留首失败；打包清单与限定发布；登记外部重查时间。','变更清单、失效队列、版本化MD/JSON/代码、交付回执','验收不刷新信任基线；不覆盖历史；本Session不生成STATE_DASHBOARD.HTML；不自动push。','templates/CHANGE_REVIEW.md','旧文件未变、新包可复跑、归档hash/CRC一致；软件验收不宣称科学认证。')]
for slug,title,trigger,inputs,steps,outputs,stops,ref,accept in items:
 d=P/slug;d.mkdir(parents=True,exist_ok=True)
 text=f'''---
name: {slug.split('-',1)[1]}
description: {title}。用于{trigger}。Evidence-bound research subskill; no automatic scientific certification.
---

# {title}

## 触发 / Trigger
{trigger}。

## 输入 / Inputs
{inputs}。

## 执行 / Procedure
{steps}

## 产出 / Outputs
{outputs}。

## 拒绝升级与转交 / Stop & Handoff
{stops}

## 验收 / Acceptance
{accept}

## 参考合同 / Contract
仓库根目录下`{ref}`；总规则见`SKILL.md`。这些是本项目编写的执行合同，不是对外部Skill逐字转载；工具测试只验证相应软件性质。
'''
 (d/'SKILL.md').write_text(text)
print('subskills',len(items))
