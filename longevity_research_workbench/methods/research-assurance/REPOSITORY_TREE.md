# 仓库目录树 / Repository Tree

可作为仓库根，也可置于现有仓库`methods/research-assurance/`。下面列的模块均已创建；它们的可执行／人工合同边界见README与docs。不是仅供未来实现的空目录。

```text
research_assurance_toolkit/
├── README.md                         总入口、准确定位与快速运行
├── METHOD_HANDBOOK_ZH_EN.md           单文件完整方法手册
├── SKILL.md                          Agent总技能合同
├── DELIVERY_NOTES.md                 本轮执行与验收说明
├── pyproject.toml                    安装与CLI入口
├── requirements-tested.txt           本轮实际测试依赖版本
├── REPOSITORY_TREE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE_POLICY.md                 权利人尚未选择开源许可证
├── .github/workflows/ci.yml           软件性质CI；尚未在远端执行
├── docs/
│   ├── 01_POSITIONING.md              认识论/方法论/工程/工作流/Skill分层
│   ├── 02_METHODOLOGY.md              通用方法论与正确性向量
│   ├── 03_WORKFLOW.md                 生命周期、门槛、责任与停止
│   ├── 04_DATA_CONTRACTS.md           机器合同、版本失效与人审状态
│   ├── 05_CORPUS_ENGINE.md            七任务、真实拓扑及敏感性边界
│   ├── 06_VALIDATION.md               反例、复现、H⁰与证明边界
│   ├── 07_ADAPTATION.md               专著/论文/综述/不同学科适配
│   ├── 08_LINEAGE.md                  V1–V6真实谱系与未移植能力
│   ├── 09_LIMITATIONS.md              框架自身欠债
│   ├── 10_SKILL_DISTILLATION.md       原10参考Skill的取舍，不逐字复制
│   ├── GLOSSARY.md                    中英双语关键词
│   └── INTEGRATION.md                 作为已有GitHub仓库组件集成
├── skills/                           每目录含可调用SKILL.md
│   ├── 01-scope-and-route/
│   ├── 02-search-and-provenance/
│   ├── 03-corpus-topology/
│   ├── 04-claim-evidence/
│   ├── 05-measurement-and-identification/
│   ├── 06-reproduce-and-challenge/
│   ├── 07-rivals-and-contracts/
│   ├── 08-synthesis-and-writing/
│   ├── 09-review-and-debts/
│   └── 10-change-and-release/
├── src/research_assurance/
│   ├── __init__.py
│   ├── cli.py                        check / diff / topology / diagnostics
│   ├── core.py                       schema/精确绑定/失效/diff/新快照
│   ├── corpus.py                     Markdown blocks与词表/否定式扫描
│   ├── topology.py                   Louvain、Q、中心性、边密度、ARI
│   ├── tasks.py                      七项本地任务接口
│   ├── consistency.py                有限CSP；历史h0名仅别名
│   ├── measurement.py                重编码/分母界/加权诊断
│   └── project.schema.json           安装内嵌schema
├── schemas/project.schema.json       公开机器合同，同字节副本
├── templates/                        12份人审/研究模板，不冒充全自动验证
│   ├── PROJECT_CHARTER.md
│   ├── PROTOCOL.md
│   ├── SEARCH_LOG.csv
│   ├── CLAIM_REVIEW.md
│   ├── RESEARCH_CONTRACT.md
│   ├── MEASUREMENT_CONTRACT.md
│   ├── INDEPENDENT_REVIEW.md
│   ├── LENS_AND_RHETORIC.md
│   ├── TRANSFER_AND_IMPLEMENTATION.md
│   ├── SCENARIO.md
│   ├── CHANGE_REVIEW.md
│   └── DEBT_LEDGER.csv
├── examples/toy/                     构造示例，不是真实科学数据
│   ├── project.json
│   ├── ontology.json
│   ├── corpus/draft.md
│   └── evidence/synthetic_source.txt
├── tests/test_toolkit.py             正向/破坏性/边界测试
├── scripts/
│   ├── run_validation.py             常规验收，只读证据与旧基线
│   ├── verify_history.py             缺历史不冒称已验
│   ├── package_delivery.py           新包hash/CRC，不改旧历史
│   ├── build_schema.py               维护用schema作者工具
│   ├── build_handbook.py             第一方方法文档合订，不刷新证据
│   ├── create_toy_example.py         维护toy，不用于真实基线刷新
│   ├── write_templates.py            本轮模板生成源
│   └── write_skills.py               本轮Skill生成源
├── session/                          本Session谱系，不是通用域金标
│   ├── NEXT_PRIORITIES.md
│   ├── DATA_ACCEPTANCE_CONTRACTS.md
│   ├── OWED_DEBTS.json                11项研究债+7项方法债
│   ├── HISTORY_REVIEW.json            23项核读深度与hash
│   ├── METHOD_REFERENCES.json         本轮3组定向方法参考
│   ├── SELF_REVIEW.md                 同助手自查和真实设计收紧，不当外审
│   ├── history_before.json           465历史文件保护基线
│   └── run_real_binding_pilot.py      一条真实历史断言迁移；无旧目录时不运行
├── results/                          实际执行回执和派生结果
│   ├── VALIDATION.json
│   ├── HISTORY_INTEGRITY.json
│   ├── REAL_BINDING_PILOT.json
│   ├── PROJECT_CHECK.json
│   ├── TOPOLOGY.json
│   ├── DIAGNOSTICS.json
│   └── INSTALL_SMOKE.json
└── FILE_MANIFEST.json                 本包交付文件hash；不含自身递归hash
```

`results/`为本轮执行结果，不是CI将来必定通过的承诺。真实历史试验需旧工作区；独立下载新包可运行toy／测试／CLI，不应把“旧原件不可用”标成通过。当前无新HTML交付。
