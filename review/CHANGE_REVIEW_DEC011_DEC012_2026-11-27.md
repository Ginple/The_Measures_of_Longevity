# 更新与失效审阅 / Change & Invalidation Review — DEC-011 / DEC-012 / X125–X128

（按 `templates/CHANGE_REVIEW.md` 填写）

- **Change ID / 更新ID：**
  - `change:DEC-011_architecture`
  - `change:DEC-012_papers`
  - `change:X125-X128_prior_art_and_attribution`
- **What changed / 变化内容：**
  - 书稿架构由"待裁决"改为三卷·八部·33 章；
  - 论文 P1+P2 合并为 PI，P3 有条件保留，P4 暂缓；
  - 新增四条先行文献与更正记录，含一项作者归属错误。
- **Before/after hashes & diff / 前后版本：**
  - 基线提交 `e0a598d`；
  - 逐文件差异见本 PR 的 `git diff e0a598d`；
  - 冻结文件的基线 sha256 写在 `tests/test_dec011_impact.py`。
- **Impacted / 受影响对象：**
  - 26 个节点，由 `tools/dec011_impact.py` 调用 `research_assurance.core.impact` 计算，结果见 [影响记录 JSON](DEC011_DEC012_IMPACT_2026-11-27.json)；
  - 分为局部（local）与全局（global）。全局指 MASTER、PUBLICATION_MAP、README、KERNEL 和 Linear。
- **Prior judgement state / 旧判定：**
  - MASTER §3 记为"待裁决"，A/A′/B/C 为候选；
  - MASTER §4 记为"待裁决"；
  - X94 写作"Karin 2025"。
- **New status / 新状态：**
  - revised 10；
  - kept_valid 6；
  - stale_requires_review 10，包括 8 份示范稿、PART_VI 骨架和 PR2 候选样章。
  - stale_requires_review 表示需要重审，**不等于**已被推翻。
- **Re-reading/recomputation required / 需要重读或复算的：**
  - 示范稿按新章号重审"论文关联"和"变更影响"两节；
  - CH24 的标题行仍写"第24章"；
  - X94 的数值不需要复算，已逐项核对原文。
- **Reviewer and actual action / 审阅者与实际动作：**
  - 同一助手，不是独立审阅；
  - 动作见 JSON 中各节点的 note。
- **New judgement & bound versions / 新裁决与绑定版本：**
  - OUTLINE_v1 绑定 V6/V7 语料的 sha256，测试负责复核。
- **Debt still open / 未偿债务：**
  - 10 个待重审节点；
  - §7.2 单章试点；
  - PI 系统近邻检索；
  - L2 回执（可选）；
  - D05 独立外审。

**本次未刷新任何旧的信任基线：** FILE_MANIFEST、`governance/history_before.json` 与 L2 盲审包都未改动。

## 追加 · `change:X129-X132_margin_recovery_anchors`（同日第二轮检索）

- **What changed / 变化内容：**
  - 余量与恢复找到直接的人体测量（X129、X132）；
  - 横断面下降斜率偏乐观（X130）；
  - 新增合成算例：余量换算年数（X131）。
- **Prior judgement → new / 旧判定→新判定：**
  - 架构决定 §3 原定"第 9 章为有条件章节"；条件未触发，**保留 33 章**。
  - 第 8、9 章的外部锚点由"弱"调为"中"；OUTLINE 的证据等级本来就是 M，不需要重建。
- **Impacted / 受影响对象：** 同一影响记录 JSON 现有 29 个节点：revised 13、kept_valid 6、stale_requires_review 10。
  - KERNEL 升为 v0.9.10（由 kept_valid 改为 revised）；
  - 8 份示范稿已在稿内标注新章号与 PI 映射，正文仍待重审，状态不变。
- **Debt still open / 未偿债务：**
  - Strehler–Mildvan 原文未读；
  - 肾储备研究的具体数值只在综述片段中见到。
