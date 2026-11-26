---
name: reproduce-and-challenge
description: 复现与反例 / Reproduce & Challenge。用于拿到公开代码／数据、需要检验必要性质或门禁有效性。Evidence-bound research subskill; no automatic scientific certification.
---

# 复现与反例 / Reproduce & Challenge

## 触发 / Trigger
拿到公开代码／数据、需要检验必要性质或门禁有效性。

## 输入 / Inputs
原件校验、环境、实际代码、科学性质与范围。

## 执行 / Procedure
静态先于执行；隔离最小函数；显式依赖注入与兼容改动；复算预定义数据集；注入篡改；测试重标记、守恒和参数稳定；保留失败与补丁候选。

## 产出 / Outputs
可执行反例、环境与回执、非破坏性diff、影响范围。

## 拒绝升级与转交 / Stop & Handoff
不执行未知shell/notebook/pickle；局部补丁不等完整修复；不删异常点或挑参数凑图。

## 验收 / Acceptance
测试可独立运行；“预期失败确认”不写成被测系统健康；构造不等原论文重分析。

## 参考合同 / Contract
仓库根目录下`docs/06_VALIDATION.md`；总规则见`SKILL.md`。这些是本项目编写的执行合同，不是对外部Skill逐字转载；工具测试只验证相应软件性质。
