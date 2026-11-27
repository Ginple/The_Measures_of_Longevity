# 实际文件清单 / Repository tree（2026-11-27 同步）

排除缓存、构建产物和 .git；本树为**实际布局**（工具包已从 methods/research-assurance/ 平铺到根；V6/V7 正文位于 corpus/）。精确 hash 以各 manifest 为准。

```text
The_Measures_of_Longevity/
  .gitattributes
  .github/
  .gitignore
  ARENA_AGENT_UNIVERSAL_P0_P8_PLAYBOOK_ZH_2026-11-10_R3.8.md
  CGEE_R5.5.md
  CHANGELOG.md
  CONTRIBUTING.md
  DELIVERY_NOTES.md
  FILE_MANIFEST.json
  HANDOFF.md
  LICENSE_POLICY.md
  METHOD_HANDBOOK_ZH_EN.md
  README.md
  REPOSITORY_TREE.md
  RESEARCH_DATE_CLARIFICATION.md
  Research Assurance Toolkit — 0.1.1 candidate.md
  SECURITY.md
  SESSION_UPDATE_RECEIPT.json
  SKILL.md
  UPSTREAM_0_1_0_README.md
  WORKSPACE_CLEANUP_RECEIPT.json
  WORKSPACE_STORAGE_NOTE.md
  artifacts/
  books/
  corpus/
  docs/
  evaluation/
  examples/
  governance/
  history/
  knowledge_base/
  longevity_capacity_timing/
  longevity_caretaker_selectivity/
  longevity_new_territories/
  longevity_repair_memory/
  longevity_spatial_access/
  longevity_state_turnover/
  longevity_v6/
  longevity_v7/
  papers/
  platform_adapters/
  pyproject.toml
  references/
  requirements-tested.txt
  results/
  review/
  schemas/
  scripts/
  session/
  skills/
  src/
  templates/
  tests/
  tools/
```

## 关键路径与角色（权威表见 knowledge_base/MASTER.md §1）

- `knowledge_base/` — KERNEL / MASTER / CLAIM_LEDGER / RESEARCH_FRONTIERS / ANOMALY_LOG（scaffold 四件套 + 异常日志）
- `corpus/longevity_v6|v7/` — 两份专著正文的**唯一活跃编辑源**
- `longevity_v6|v7/`（根级）— 字节相同遗留副本，待 THE-236 处置
- `longevity_new_territories/` 等 6 个 `longevity_*` 目录 — 六轮研究模块（证据，冻结）
- `papers/P1|P2|P3/PROTOCOL.md` — 三篇论文协议；处置方案见 MASTER §4
- `src/research_assurance/`、`tools/`、`tests/` — 研究保障工具包 0.1.1 候选
- `session/OWED_DEBTS.json` — 历史科学债（状态保留，不自动关闭）
