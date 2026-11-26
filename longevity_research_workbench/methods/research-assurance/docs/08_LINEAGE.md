# V1–V6谱系与真实能力 / Lineage & Actual Capabilities

本表根据本轮实际核读本地协议与代表实现建立，不把用户回忆清单当代码存在证明。旧版本保持原样，通用包不回写旧通过状态。

|历史版本|当时解决什么|代表产物|关键边界／教训|
|---|---|---|---|
|V1 / v1.1|冻结语料、类型词表、共现、否定式扫描与定向人审|ANALYSIS_PROTOCOL.md、corpus_ontology.py、apophatic_scan.py、manual_review.json|分析本体不是世界本体；词表零命中不是概念不存在；对V6/V7并非全部分析完全对称|
|V2|对称复核、真实拓扑、七任务本地对应、研究合同|topology_engine.py、analysis_tasks.py、argument_surface.py、rhetorical_reviews.json、implementation_bridges.json、lens_audit.json、selection_sensitivity.py、scenarios.json|Louvain与敏感性在此加入；不能回填到V1。四状态本地阈值未验证，不冒充InfraNodus|
|V3|结构缺口、事实候选、可追踪修订、有限全局兼容|structure_audit.py、fact_consistency.py、claims.json、research_design.py|H⁰以有限CSP操作化，未构造完整层上同调；build_sections人工常量未与当前正文同步|
|V4|从自洽到有证据支持的正确；纠正global section误释|content_verifier.py、identification_checks.py、mutation_tests.py、OWED_DEBTS.json|global section是全局截面不是章节。源绑定／篡改测试；SAT不等外部真值。来源家族不当独立证据|
|V5|实际公开数据复算、源闭环、片段门禁与访问资格|analyze_public_data.py、verify_content.py、version_audit.py、研究回执|独立bulk不等每个单细胞配对金标；源表Pearson系数差异未解；不删异常点凑图|
|V6|官方代码版本、隔离缺陷、名义度量与死亡代理、全文diff|research_audit.py、document_change_guard.py、test_and_propose.py|原代码两函数／shell问题不证明发表结果已受影响；重编码反例不推翻真实分群；全文diff不验未改内容；外审仍欠|

## 版本纠偏 / Version Attribution

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

## 不能遗失的历史失败

1. “global section=章节”曾是错误解释，已公开纠正；新增免责声明不替代具体纠错。
2. 人工常量即使自洽，也可能与正文实际改动脱钩；需源文绑定和变异测试。
3. 片段级hash漏掉片段外新增句；全文diff补上的是变更覆盖，不是科学语义覆盖。
4. 同一研究多载体不构成独立复制；Crossmark current和updates0不解决源内冲突。
5. 代理死亡、幸存者选择、copy/capture加权、伪供者配对和名义数值距离可能使目标不可识别。
6. 本项目自身未排序glob曾造成独立目录字节复现失败；修复与失败回执均保留在历史V6。
7. 1050结构候选仅既有10对定向人审；软件计数不能扩大成人工覆盖。
8. 正式独立外审从未因多次自查或新测试而自动发生。

本轮核读索引与hash见`session/HISTORY_REVIEW.json`，完整旧原件不重新分发进通用包。
