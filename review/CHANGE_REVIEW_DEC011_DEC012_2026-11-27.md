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
  - 10 个待重审节点（文末追加后为 9 个）；
  - §7.2 单章试点（后续已执行，见文末追加）；
  - PI 系统近邻检索（后续门槛 1–2 已完成，见文末追加）；
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

## 追加 · `change:X133-X137_PI_novelty`（PI 系统近邻检索）

- **What changed / 变化内容：**
  - 按预先写好的[检索协议](../papers/PI_rejuvenation_identifiability/NOVELTY_SEARCH_PROTOCOL.md)完成门槛 1–2：PubMed 11 个查询（573 条命中，202 条看了标题，11 篇读了摘要），Europe PMC 4 个查询加引文追踪（53 条），留痕见 `knowledge_base/search_logs/SEARCH_LOG_2026-11-27_PI_NOVELTY.csv`（P01–P17）。
  - 读了 Yücel 2024 七节中的四节（X133），更正 X125 的定位：它是第①②层的定性先行，没有给出三层统一的 estimand。
  - 新增先行或必引文献：Zhang & Gems、Thapa、Fulton（X134），Yi 2026（X135）；Strehler–Mildvan 原文付费墙，维持二手引述（X136）。
- **Prior judgement → new / 旧判定→新判定：**
  - 旧："新颖性未认证，投稿前须完成系统近邻检索"。
  - 新（X137）：A（三层统一框架）未命中；B、C 部分命中。按协议 §4 处置为**保留原创、收窄主张**。PI 协议升为 v3，贡献收窄为三条；列出必引清单；禁用"首次""首个框架""填补空白"。
  - 架构决定 §6 的触发条件"近邻检索发现三层框架已有发表"**未触发**。
- **Impacted / 受影响对象：** PI 协议、MASTER、架构决定、knowledge_base/README、工作流对照、台账 X125 节点。全部是 revised；X125 原文不改，更正追加在 X133。
- **Debt still open / 未偿债务：**
  - 门槛 3：Scopus/WoS 检索与独立第二筛选人（外部条件）；
  - 检索的已知条目召回失败一次：摘要检索没有召回 Yücel 2024，这是检索方法的已知局限；
  - 未读部分：Yücel 第 1、5、6 节，部分引文追踪页。

## 追加 · `change:ch05_pilot_V7-06_reassign`（08_LINEAGE §7.2 单章试点）

- **What changed / 变化内容：**
  - 在第 5 章（测量合同，示范稿 CH15）执行单章试点。从章内挑出 5 段，每段绑定逐字来源片段：
    - 时钟替代终点（Yi 2026、Borrus 2026 摘要）；
    - CALERIE 轨迹分析（Warmbrunn 正文与补表 S3）；
    - 两类混合反例（P2 技术备忘录）；
    - NHS-Galleri（正文）；
    - 使用规则（V7-06 原文，规范性主张，故意保持 unknown）。
  - 记录在 `knowledge_base/pilots/ch05_measurement_contract/project.json`，由 `build_project.py` 生成，由 `tests/test_ch05_pilot.py` 复核。
  - `inspect_project` 结果：0 个完整性问题，0 个漂移；正式发布 **blocked**，原因是无独立审阅、清单未完整、债务未清。
- **Prior judgement → new / 旧判定→新判定：**
  - 试点暴露一处标题级映射错误：V7-06《表观时钟的两个极端都错了》的正文就是第 5 章标题里的四种属性和使用规则，原先被归到第 6 章（水平）。ASSIGN 改为 5，重新生成地图。**第 6 章因此变为无继承、需新写**（与第 7、9 章同）。章数与部结构不变。
  - CH15 由 stale_requires_review 改为 revised（v0.3，原位修订，未另建同名稿）。
  - 核对正文数字：14.2 万、17 个月、706/688、IRR 1.03（0.92–1.14）、190/20、57 个缺失、26 项研究，均与来源片段一致。没有发现需要撤回的数字。
- **Impacted / 受影响对象：** outline_build.py → outline_v1.json、OUTLINE_v1.md → MASTER、knowledge_base/README、架构决定、工作流对照；CH15；书稿 README。影响记录现为 33 个节点：revised 19、kept_valid 5、stale_requires_review 9。
- **Debt still open / 未偿债务：**
  - CH15 中 3 段带脚注的证据段尚未登记（CALERIE 甲基化与骨密度、DO-HEALTH、Malagón 微模拟）；
  - Yi 2026 只读到摘要；
  - 这是**一章的记账试点**，不能说成迁移验收或方法有效；
  - 其余 7 份示范稿仍待重审；D05 独立外审仍开放。

**本次仍未刷新任何旧的信任基线**：FILE_MANIFEST、`governance/history_before.json`、L2 盲审包与冻结协议的字节均未改动（测试复核）。
