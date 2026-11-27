# 共享断言层 / Shared claims layer

**当前为接入规范，无全稿完整人审声明。** 不把V6/V7的段落自动视为已验证断言。toolkit的toy是构造数据，不可迁入正文充当证据。

## 本目录四件套（2026-11-27 scaffold）

| 文件 | 角色 |
|---|---|
| [KERNEL.md](KERNEL.md) | 核心内核：不变式、定义、定量锚点、范式转换候选、estimand 骨架、禁写句、版本失效协议 |
| [MASTER.md](MASTER.md) | 总控：权威路径表、书稿架构三方案、论文处置四方案、里程碑、决策日志 |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | 交叉验证与不确定项台账（X-item） |
| [RESEARCH_FRONTIERS.md](RESEARCH_FRONTIERS.md) | 前沿扫描（第 1 期 2026-11-27）与 Known/Unknown Unknowns、候选转向 |
| [ANOMALY_LOG.csv](ANOMALY_LOG.csv) | 异常现象日志（Unknown unknowns 发现机制） |
| `claims/` | 断言卡目录（待建，LON-C/E/A 规范见下） |

规则：**唯一编辑源是 `corpus/longevity_v6|v7`**；根级 `longevity_v6|v7` 为遗留副本禁止编辑。架构与论文处置待作者裁决（Linear THE-227/229），裁决前本目录文件为 v0.9 草案。

---

稳定ID建议 `LON-C000001`（断言）、`LON-E000001`（提取）、`LON-A000001`（来源/稿件快照）。ID永久不重用。来源去重记录版本/来源家族，独立来源不能仅按URL数量计算。

最小接收：明确对象/人群、干预或暴露、比较、结果、时间窗、estimand、效应尺度、不确定性、原始文件hash、精确片段、访问深度、主张kind、适用范围、竞争解释、债务、负责人。二进制表格/图像坐标需要扩展，本轮没有假装全部支持。

toolkit当前用schema作机械合同，不自动理解医学或规范伦理。多前提论证需拆分claims并显式记录依赖；当前实现对artifact→evidence→claim可传播，不宣称已经从全书自动抽出任意语义依赖。book/paper引用映射仍需人工接入。

共享层只维护证据判断；不同写作产物可采用不同叙事，但必须显式处理同一claim的版本。增加新来源后先失效旧判断，再由人重新判断；自动计算新hash不等重新审阅。
