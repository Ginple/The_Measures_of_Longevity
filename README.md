# 长寿的尺度 · The Measures of Longevity

**定位 / Positioning**：长篇跨学科专著《长寿的尺度》与伴生论文的研究仓库；内含可测试的研究保障子组件，而不是“用一组提示词生成一本书”。

**当前版本**：scaffold v0.9（2026-11-27）：knowledge_base 四件套 + Linear 看板已建；书稿架构与论文处置待作者裁决。人工独立外审 **未发生**；科学债未关闭。

## 从这里读 / Start here

1. **[KERNEL.md](knowledge_base/KERNEL.md)** — 核心内核：不变式、定量锚点、范式转换候选
2. **[MASTER.md](knowledge_base/MASTER.md)** — 总控：权威路径、书稿架构方案、论文处置方案、里程碑
3. [CLAIM_LEDGER.md](knowledge_base/CLAIM_LEDGER.md) — 交叉验证台账 · [RESEARCH_FRONTIERS.md](knowledge_base/RESEARCH_FRONTIERS.md) — 前沿扫描
4. [本轮决策与附件比较](docs/DECISION_REPORT_ZH_EN.md)
5. [书名与历史提案](books/BOOK_PROPOSAL.md)（架构以 MASTER §3 为准）
6. [三篇论文及成果分工](papers/PUBLICATION_MAP.md)（处置以 MASTER §4 为准）
7. [敌对测试报告](evaluation/ADVERSARIAL_REVIEW.md)
8. [手动建库、运行、许可与公开边界](docs/GITHUB_HANDOFF.md)
9. [架构决策记录](governance/ADR_001.md) · [实际目录树](REPOSITORY_TREE.md)

## 本地验证 / Local verification

```bash
python -m pip install -e ./methods/research-assurance
python tools/run_validation.py
```

安装依赖需要联网或本地wheel；工具运行本身不请求网络。已经安装依赖时直接运行第二条即可；脚本设置子进程导入路径，不要求修改环境变量。
验证会写入 `artifacts/` 和子组件 `results/`，不刷新历史信任基线，也不重签判断。上游原包的对照复现及附件钩子实验是**可选的本地来源重放**，不属于公开仓库必需CI：

```bash
python tools/audit_prior_toolkit.py /path/to/frozen/research_assurance_toolkit
python tools/audit_attachment_hook.py /path/to/CGEE_R5.5.md
```

附件重放先验固定SHA256，新版必须重新阅读与审查；不可自动更新预期hash来“修复”失败。

## 分层 / Layers

- `governance/`：人类决策、来源接收和历史保护；不是自动执法服务。
- `knowledge_base/`：共享断言目录规范；当前**没有**把所有书稿断言提取为经人审的登记表。
- `books/`、`papers/`：研究纲领与各自贡献，不是已完成新专著/论文。
- `corpus/editions/`：V6/V7 两份正文的逐字节快照；保留不同透镜，不称新V8。
- `methods/research-assurance/`：上一轮工具包的派生候选修订，原0.1.0在仓库外冻结不改。
- `platform_adapters/`：部署边界说明；无已启用Claude/GitHub/Linear/Notion执法。
- `review/external/`：独立评审空缺及验收要求，不能用目录存在代替评审。
- `artifacts/`：本轮实际运行回执；`references/`只存附件接收记录与定向核验说明，不复制第三方全文。

## 不作出的承诺 / Non-claims

不判科学真值；不认证返老还童；不把有限全局截面可满足性当世界真理；不把1050候选说成全部人审；不把示例命令测试说成操作系统安全认证；无新HTML；未创建或推送远端仓库。

**公开前**请完成作者、许可、版权、敏感数据与原始历史材料纳入范围审查。此工作台包含两份正文及方法组件，**并未打包全部历代引擎、原始证据大文件和会话对话**。见 `docs/GITHUB_HANDOFF.md`。
