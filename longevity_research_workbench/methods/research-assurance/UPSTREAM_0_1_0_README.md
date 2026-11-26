# 证据约束型研究工程工具包
# Evidence-Bound Research Engineering · Research Assurance Toolkit

**状态 / Status：0.1.0 可运行工程草案 / executable engineering draft。未经真实独立外审，不是科学正确性认证工具。**

面向 Scientific Deep Research（科学深度研究）、长篇专著（Monograph）、论文（Research Paper）和证据综合（Evidence Synthesis）。由本Session的`corpus_engine_v1–v6`迭代提炼；保留历史失败及能力边界，不把一次衰老领域审计伪装成已跨学科验证的通用方法。

> **定位 / Positioning：以认识论约束为基础、以方法论协议为骨架、以工作流和Skill为执行接口、以代码与证据账本为载体的研究工程实践。**
>
> `corpus_engine`起初是语料结构分析环节；至v6已扩展成跨阶段的研究审计子系统。它不是新的认识论学派，不是完整科研方法，也不只是一个Prompt或单个Skill。

“Evidence-Bound Research Engineering / 证据约束型研究工程”是本项目建议的描述性名称，**不是声称已存在的学术标准或新学科**。通用组件版本从0.1.0开始，与历史引擎V1–V6、作品V6/V7分开编号。

## 三分钟入口 / Quick Start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
research-assurance check examples/toy/project.json
research-assurance topology examples/toy/corpus/draft.md examples/toy/ontology.json
research-assurance diagnostics
```

无须安装包的源码模式 / source mode：

```bash
PYTHONPATH=src python -m research_assurance.cli check examples/toy/project.json
PYTHONPATH=src python scripts/run_validation.py
```

示例全部为**构造数据 / constructed fixtures**，不是论文原始数据。`check`预期返回：绑定无机械问题，但正式发布记录门槛`blocked`，因为没有完整断言盘点和真实独立审阅。退出码0仅表示schema与绑定未发现问题，**不表示研究结论通过**。结果从不提供`scientifically_correct=true`。

## 先读什么 / Reading Paths

- 单文件完整方法手册：[`METHOD_HANDBOOK_ZH_EN.md`](METHOD_HANDBOOK_ZH_EN.md)
- 理解“它到底是什么”：[`docs/01_POSITIONING.md`](docs/01_POSITIONING.md)
- 完整可复用方法：[`docs/02_METHODOLOGY.md`](docs/02_METHODOLOGY.md)
- 每阶段如何执行及停止：[`docs/03_WORKFLOW.md`](docs/03_WORKFLOW.md)
- 数据合同、状态与更新：[`docs/04_DATA_CONTRACTS.md`](docs/04_DATA_CONTRACTS.md)
- 语料图与七类任务：[`docs/05_CORPUS_ENGINE.md`](docs/05_CORPUS_ENGINE.md)
- 测试什么、不能测试什么：[`docs/06_VALIDATION.md`](docs/06_VALIDATION.md)
- 专著／论文／领域迁移：[`docs/07_ADAPTATION.md`](docs/07_ADAPTATION.md)
- V1–V6真实来历与错误修复：[`docs/08_LINEAGE.md`](docs/08_LINEAGE.md)
- 已知不足与方法自身债务：[`docs/09_LIMITATIONS.md`](docs/09_LIMITATIONS.md)
- 原参考Skill的取舍：[`docs/10_SKILL_DISTILLATION.md`](docs/10_SKILL_DISTILLATION.md)
- 中英术语：[`docs/GLOSSARY.md`](docs/GLOSSARY.md)
- 仓库集成：[`docs/INTEGRATION.md`](docs/INTEGRATION.md)
- Agent总入口：[`SKILL.md`](SKILL.md)；可拆分子技能：[`skills/`](skills/)
- 本轮真实推进和下一优先项：[`session/NEXT_PRIORITIES.md`](session/NEXT_PRIORITIES.md)

## 核心闭环 / Core Loop

```text
问题与用途 Question & use
  ↓
范围/协议/权限 Scope, protocol & authority
  ↓
检索→筛选→取源 Search → screening → source access
  ↓
不可变原件 + 来源家族 Immutable artifacts + source families
  ├─ 语料透镜→结构候选 Corpus lens → structural candidates
  └─ 断言→源文绑定→研究设计/测量/推断 Claim → evidence → validity dimensions
                  ↓
        竞争解释与判别试验 Rival explanations & discriminating tests
                  ↓
        欠债/停止/独立复核 Debts, stopping & independent review
                  ↓
        分范围写作与发布 Scoped synthesis & release
                  ↓
        全文diff/依赖失效/新证据更新 Change control & invalidation ↺
```

这是多次循环的**控制平面 / control plane**，不是保证研究成功的线性流水线。问题生成、证据评估和发布裁决必须分开；不能由同一个生成过程给自己发“独立通过证书”。

## 交付物与实现边界 / Deliverables & Implementation

**本包实际实现：**
- JSON Schema与交叉引用检查；原件hash、精确行范围／原文引句绑定；断言判定绑定旧版本时报警。
- 全文diff登记，包括旧抽样片段外的新增句；依赖图上的传递失效分析。
- 有预算的有限关系CSP兼容性检查；`h0_global_section_exists`仅作历史别名，非层上同调算法。
- Markdown空行块抽取、声明词表匹配、无向共现图、Louvain、真实跨群边／缺边／共同邻居与最短路径、中心性、敏感性。
- 七个本地任务接口，不冒称外部InfraNodus调用；四状态标签是历史未验证启发式。
- 名义重编码诊断、固定基线founder缺失结果界、copy/capture加权构造对照。
- 反例／篡改／变异测试、CI配置、可复现检查；所有测试仅限其编码性质。

**本包不自动实现：**
- 全书语义断言穷尽抽取、自然语言蕴含裁决、系统检索数据库覆盖、真实死亡／功能金标。
- 完整风险偏倚评估、因果识别或跨域净益证明、伦理审批、预注册、独立外审。
- 直接下载／执行任意来源程序、自动邮件、外部平台写入、自动刷新信任基线。

## 放进你的GitHub仓库 / Repository Integration

可将整个目录放入现有仓库的`methods/research-assurance/`，也可作为独立工具目录。见[`REPOSITORY_TREE.md`](REPOSITORY_TREE.md)。包内相对路径在移动后仍有效；`session/history_before.json`是本Session历史回执，在独立仓库缺少旧文件时不能冒称复验通过。

这里只交付**可提交的本地仓库组件**，未创建远端仓库、未commit/push、未向任何已连接应用写入。`.github/workflows/ci.yml`在本组件作为仓库根目录时可用；嵌入`methods/`时需修改working-directory，见集成说明。

按用户最新要求，本轮及后续**不再生成或交付STATE_DASHBOARD.HTML**；历史HTML只留在冻结历史，不装进新包。新包仅Markdown、JSON、Python与配置。

## 治理 / Governance

贡献请读[`CONTRIBUTING.md`](CONTRIBUTING.md)、[`SECURITY.md`](SECURITY.md)、[`LICENSE_POLICY.md`](LICENSE_POLICY.md)。未替用户选择开源许可证；在正式发布前由权利人确定。不能因为目录能上传GitHub就声称已获上游代码／论文／Skill再许可授权。本包不搬运第三方全文和历史证据大包。
