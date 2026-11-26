---
name: change-and-release
description: 更新与发布 / Change & Release。用于正文／原件／词表／参数／代码变化，或新版本准备交付。Evidence-bound research subskill; no automatic scientific certification.
---

# 更新与发布 / Change & Release

## 触发 / Trigger
正文／原件／词表／参数／代码变化，或新版本准备交付。

## 输入 / Inputs
冻结快照、候选差异、依赖图、验收与偏好。

## 执行 / Procedure
逐字节hash和全文diff；沿依赖图标stale；人工重审而非自动重绑；跑正向／反例／移目录复现；保留首失败；打包清单与限定发布；登记外部重查时间。

## 产出 / Outputs
变更清单、失效队列、版本化MD/JSON/代码、交付回执。

## 拒绝升级与转交 / Stop & Handoff
验收不刷新信任基线；不覆盖历史；本Session不生成STATE_DASHBOARD.HTML；不自动push。

## 验收 / Acceptance
旧文件未变、新包可复跑、归档hash/CRC一致；软件验收不宣称科学认证。

## 参考合同 / Contract
仓库根目录下`templates/CHANGE_REVIEW.md`；总规则见`SKILL.md`。这些是本项目编写的执行合同，不是对外部Skill逐字转载；工具测试只验证相应软件性质。
