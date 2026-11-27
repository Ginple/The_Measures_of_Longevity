# 长寿的尺度 · The Measures of Longevity

**定位 / Positioning**：长篇跨学科专著《长寿的尺度》与伴生论文的研究仓库；内含可测试的研究保障子组件，而不是“用一组提示词生成一本书”。

**当前版本**：scaffold v0.9（2026-11-27）：knowledge_base 四件套 + Linear 看板已建；书稿架构与论文处置待作者裁决。人工独立外审 **未发生**；科学债未关闭。

## 从这里读 / Start here

1. **[KERNEL.md](knowledge_base/KERNEL.md)** — 核心内核：不变式、定量锚点、范式转换候选
2. **[MASTER.md](knowledge_base/MASTER.md)** — 总控：权威路径、书稿架构方案、论文处置方案、里程碑
3. [CLAIM_LEDGER.md](knowledge_base/CLAIM_LEDGER.md) — 交叉验证台账 · [RESEARCH_FRONTIERS.md](knowledge_base/RESEARCH_FRONTIERS.md) — 前沿扫描 · [模型作表与跌倒结局审计](knowledge_base/MCED_CODE_AND_HOME_FALLS_AUDIT_2026-11-27.md) · [执行时长诊断及后续任务](review/EXECUTION_DURATION_REVIEW_2026-11-27.md)
4. [本轮决策与附件比较](docs/DECISION_REPORT_ZH_EN.md)
5. [书名与历史提案](books/BOOK_PROPOSAL.md)（架构以 MASTER §3 为准）
6. [三篇论文及成果分工](papers/PUBLICATION_MAP.md)（处置以 MASTER §4 为准）
7. [敌对测试报告](evaluation/ADVERSARIAL_REVIEW.md)
8. [手动建库、运行、许可与公开边界](docs/GITHUB_HANDOFF.md)
9. [架构决策记录](governance/ADR_001.md) · [实际目录树](REPOSITORY_TREE.md)

## 本地验证 / Local verification

```bash
python -m pip install -e . 'beautifulsoup4>=4.12,<5'
python scripts/run_validation.py  # tools/run_validation.py 是等价入口
```

CI 的 CPython 3.11 Linux 固定版本环境（与宽依赖的开发安装不同）：

```bash
python -m pip install -r requirements-ci-py311.txt
python -m pip install --no-build-isolation --no-deps -e .
python -m pip check
python scripts/run_validation.py
python knowledge_base/pilots/real_claims_001/scripts/validate.py
python tools/install_smoke.py
python -O tools/install_smoke.py
```

`requirements-ci-py311.txt` 钉住直接及当次解析出的传递/构建依赖版本，不含包哈希，不锁定 pip、操作系统、Python 补丁版或 Actions 本身，因此不是供应链字节锁；其他Python版本及平台未验证。原 `requirements-tested.txt` 是历史记录，其 networkx 3.7 不能安装到 Python 3.11，不用作该CI环境。宽依赖的 `pyproject.toml` 依旧支持从 Python 3.10 起安装，并非所有支持版本均由本CI覆盖。详见[依赖验证回执](review/CI_DEPENDENCY_REPRODUCIBILITY_2026-11-27.md)。

安装依赖需要联网或本地wheel；工具运行本身不请求网络。已经安装依赖时直接运行第二条即可；脚本设置子进程导入路径，不要求修改环境变量。
验证输出当前回执到标准输出，不覆盖历史 `artifacts/`、`results/` 或信任基线。它运行根目录、合成实验和真实断言试点的测试；检查所请求看板基本结构、两个大小写副本的一致性及精确 HTML 允许列表（排除本地缓存/构建目录）；检查 Markdown 相对链接并逐项报告 `governance/legacy_broken_links.json` 所列已知历史断链，新增断链仍失败；比较两种 hash seed 及移目录后的测试与 CLI 输出。测试不认证科学结论或独立评审。两个仅大小写不同的看板在不区分大小写的文件系统存在 checkout 风险，尚需决定可移植的发布策略。上游原包的对照复现及附件钩子实验是**可选的本地来源重放**，不属于公开仓库必需CI：

```bash
python tools/audit_prior_toolkit.py /path/to/frozen/research_assurance_toolkit
python tools/audit_attachment_hook.py /path/to/CGEE_R5.5.md
```

附件重放先验固定SHA256，新版必须重新阅读与审查；不可自动更新预期hash来“修复”失败。

## 分层 / Layers

- `governance/`：人类决策、来源接收和历史保护；不是自动执法服务。
- `knowledge_base/`：共享断言目录规范；当前**没有**把所有书稿断言提取为经人审的登记表。
- `books/`、`papers/`：研究纲领与各自贡献，不是已完成新专著/论文。
- `corpus/longevity_v6/`、`corpus/longevity_v7/`：V6/V7 正文的活跃编辑源；根级同名目录为遗留副本，保留不同透镜，不称新V8。
- `src/research_assurance/`：上一轮工具包的派生候选修订，原0.1.0在仓库外冻结不改。
- `platform_adapters/`：部署边界说明；无已启用Claude/GitHub/Linear/Notion执法。
- `review/external/`：独立评审空缺及验收要求，不能用目录存在代替评审。
- `artifacts/`：本轮实际运行回执；`references/`只存附件接收记录与定向核验说明，不复制第三方全文。

## 不作出的承诺 / Non-claims

不判科学真值；不认证返老还童；不把有限全局截面可满足性当世界真理；不把1050候选说成全部人审；不把示例命令测试说成操作系统安全认证。用户要求的新状态看板已提供，当前工作已推送至 PR；历史交付记录中的“无新 HTML / 无远端”仅指当时会话，不是现行约束。

**公开前**请完成作者、许可、版权、敏感数据与原始历史材料纳入范围审查。此工作台包含两份正文及方法组件，**并未打包全部历代引擎、原始证据大文件和会话对话**。见 `docs/GITHUB_HANDOFF.md`。
