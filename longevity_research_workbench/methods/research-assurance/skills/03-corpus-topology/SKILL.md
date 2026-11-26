---
name: corpus-topology
description: 语料与拓扑 / Corpus & Topology。用于审查专著结构、孤岛、缺边、概念分布和透镜适切性。Evidence-bound research subskill; no automatic scientific certification.
---

# 语料与拓扑 / Corpus & Topology

## 触发 / Trigger
审查专著结构、孤岛、缺边、概念分布和透镜适切性。

## 输入 / Inputs
冻结正文、单位适配器、声明词表、分析目标。

## 执行 / Procedure
先读原文和适配器边界；抽取块与角色线索；算Louvain、Q、中心性、实际跨边／缺边；跑分段／阈值／seed敏感性；回原文审假缺口；分别看修辞、逻辑与作者目标。

## 产出 / Outputs
结构候选、源单位ID、连续量与不稳定性、人工透镜卡。

## 拒绝升级与转交 / Stop & Handoff
缺边不是知识未知；低词频不是低价值；不用四状态诊断人；不冒充外部服务分数。

## 验收 / Acceptance
边有单位证据，零检出另列，假孤点可解释；可运行CLI topology。

## 参考合同 / Contract
仓库根目录下`docs/05_CORPUS_ENGINE.md`；总规则见`SKILL.md`。这些是本项目编写的执行合同，不是对外部Skill逐字转载；工具测试只验证相应软件性质。
