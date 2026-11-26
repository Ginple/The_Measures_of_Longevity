# 长寿研究工作台 · Longevity Research Workbench

**定位 / Positioning**：一本长篇跨学科专著与三篇独立问题导向的 companion papers 的研究仓库；内含可测试的研究保障子组件，而不是“用一组提示词生成一本书”。

**当前版本**：workbench 0.1.0；内嵌 toolkit **0.1.1 候选修订版**。2026-11-25。本地工程验收不等学术发布许可。人工独立外审 **未发生**；科学债未因本轮测试关闭。

## 从这里读 / Start here

1. [本轮决策与附件比较](docs/DECISION_REPORT_ZH_EN.md)
2. [书名、研究纲领与章节架构](books/longevity/BOOK_PROPOSAL.md)
3. [三篇论文及成果分工](papers/PUBLICATION_MAP.md)
4. [敌对测试报告](evaluation/ADVERSARIAL_REVIEW.md)
5. [手动建库、运行、许可与公开边界](docs/GITHUB_HANDOFF.md)
6. [架构决策记录](governance/ADR_001.md) · [实际目录树](REPOSITORY_TREE.md)

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
