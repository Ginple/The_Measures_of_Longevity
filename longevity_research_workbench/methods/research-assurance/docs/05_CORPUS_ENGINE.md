# corpus_engine：结构分析子系统 / Corpus Structural Analysis Subsystem

## 输入不是“世界”，而是声明的语料投影

必须冻结：版本与范围、纳入／排除、抽取器版本、单位（句／段／列表项／表格行／章）、词表、别名、人工关注关系与参数。概念本体是**分析透镜 / analytical ontology**，不是世界的全部本体。

原历史V1区分自然段、列表项、表格行，排除部分参考／附录并另报六实验范围；本通用0.1解析器仅实现**Markdown空行块 / Markdown blocks**，保留所有非空块并分类，不自动继承旧版全部预处理。不能将两者输出不加说明地并排当作完全相同测量。PDF、Word、LaTeX用独立适配器；语义单元、标题、引用和表格要分别验收。

## 七项任务 / Seven Local Task Families

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

## 拓扑定义 / Topological Definitions

- 边权：共同命中的单位数；同单位重复出现不重复计权。
- strength：加权度；介数用distance=1/weight，不把大权重误当长距离。
- participation coefficient：`1 − Σc(s_ic/s_i)^2`；只是话语连接模式。
- 集群对密度：实际边数 / 两群节点数乘积；与跨边权重不同。
- 真实孤立点：检出过但当前图无边；零检出词表项另列，不能把它们当实际出现的孤岛。
- 最短路径：当前图的无权路径；桥梁候选不是新边的科学证据。

代码报告Q时统一使用γ=1评估分区，即使Louvain优化用了另一resolution。历史V2另报优化目标Q_objective，本0.1不输出该值，不能误认为两者相同。

## 四状态 / Four Local Structural States

完全公开继承历史阈值，仅作未验证话语结构标签：
1. 非最大分量节点比例>0.20，或Q≥0.55且跨群权重份额<0.10：`dispersed`。
2. 否则最大群strength份额≥0.60且Q<0.25：`biased_single_cluster_dominance_only`。
3. 否则至少3群、Q≥0.30且最大群strength份额≤0.50：`diversified`。
4. 其余`focused`；空图`not_applicable_empty_graph`。

`biased`在这里**只表示单群主导，不表示作者认知偏见**。分类稳定也不证明量表有效；不能为了得到“diversified”而往正文填无意义概念。

## 敏感性 / Sensitivity

通用示例实际运行seed=0/1/2 × γ=.75/1/1.25 × support≥1/2，共18项；另输出prose-only主图。ARI仅在节点集相同时比较，节点集不同返回null，不悄悄取交集冒充整体稳定。

历史V2范围更广：seed0–19、5种构图模式含余弦、删宽泛hub等。本通用0.1**没有声称已移植全部模式**。新项目应按风险扩充分段、词表、权重和阈值对照；保存本体变动理由，不能看结果后偷改词表。

## 人工透镜审计 / Lens Audit

每个透镜记录：为什么适用、原文位置、观察、反解释、未覆盖和裁决。允许“不适用”，不得为了“十透镜齐全”硬造形式逻辑、博弈均衡、现象学访谈或心理诊断。

有修辞效果不代表论证有效；有规范理由不代表临床获益。对支持者与反对者采用相同外推标准，保留作者原声，不用夸大缺陷来证明工具有用。
