# PI 系统近邻检索协议（投稿前门槛，PI 协议 §2）

2026-11-27｜**写于检索执行之前。**
- 检索式、纳入/排除标准和判定规则在第一次正式检索前固定。
- 之后的任何修改都在 §6 留痕，并说明理由。
- 执行与筛选由同一助手完成，没有双人独立筛选。这是已知局限，报告时须声明。

## 1. 问题

是否已有发表或预印的工作，在"年轻化/逆龄读数"这一问题上，给出了以下任何一项：

- **A（整体框架）：** 一个统一框架，同时处理身份/选择、汇总/组成、动力学/参数中的**至少两层**。
- **B（第②层形式结果）：** 混合读数在部分已知权重下，对类型内变化的锐界或部分识别结果。
- **C（第③层形式结果）：** 证明同一快照读数可来自不同参数，而未来轨迹不同，并给出区分它们的最小测量设计。

## 2. 来源与工具

- **PubMed：** 用 NCBI E-utilities 的 esearch 获取命中数和 PMID，用 esummary 获取题名与期刊。检索不限语言，日期限定为 2015/01/01–2026/11/27。
- **Europe PMC：** 对锚点论文做正向引文追踪（REST `citations`），并做全文检索补充预印本。
- **不使用：** Scopus/Web of Science（本环境不可访问）。这是已知局限。

## 3. 固定检索式

| ID | 层 | 检索式（PubMed） |
|---|---|---|
| Q1 | A | `(rejuvenat*[tiab] OR "age reversal"[tiab] OR "reversal of aging"[tiab]) AND (criteria[tiab] OR framework[tiab] OR definition*[tiab]) AND (clock*[tiab] OR biomarker*[tiab] OR "biological age"[tiab])` |
| Q2 | ① | `(rejuvenat*[tiab] OR reprogramming[tiab]) AND ("selection bias"[tiab] OR survivor*[tiab] OR "clonal selection"[tiab] OR "cell replacement"[tiab] OR "selective"[tiab]) AND (epigenetic[tiab] OR clock*[tiab])` |
| Q3 | ② | `("epigenetic clock*"[tiab] OR "epigenetic age"[tiab] OR "DNAm age"[tiab]) AND ("cell type composition"[tiab] OR "cell composition"[tiab] OR "cellular composition"[tiab] OR deconvolution[tiab]) AND (intervention*[tiab] OR rejuvenat*[tiab] OR trial*[tiab])` |
| Q4 | ② B | `("partial identification"[tiab] OR "sharp bound*"[tiab] OR "nonidentifiab*"[tiab] OR "non-identifiab*"[tiab]) AND (mixture*[tiab] OR composition[tiab] OR "cell type*"[tiab] OR deconvolution[tiab])` |
| Q5 | ③ | `("saturating removal"[tiab] OR "damage accumulation"[tiab] OR "Gompertz"[tiab]) AND (intervention*[tiab] OR rejuvenat*[tiab]) AND (identifiab*[tiab] OR "survival curve*"[tiab] OR "same lifespan"[tiab] OR steepness[tiab])` |
| Q6 | ③ C | `identifiab*[tiab] AND (aging[tiab] OR ageing[tiab]) AND (intervention*[tiab] OR rejuvenat*[tiab] OR "biological age"[tiab] OR clock*[tiab])` |
| Q7 | A | `("biological age"[tiab] OR "epigenetic clock*"[tiab] OR "aging biomarker*"[tiab]) AND ("surrogate endpoint*"[tiab] OR "surrogate marker*"[tiab]) AND (validat*[tiab] OR criteria[tiab] OR framework[tiab])` |
| Q8 | ① | `("partial reprogramming"[tiab] OR "in vivo reprogramming"[tiab] OR "transient reprogramming"[tiab]) AND (selection[tiab] OR "cell death"[tiab] OR clonal[tiab] OR heterogeneity[tiab]) AND (age[tiab] OR aging[tiab] OR clock*[tiab])` |

**引文追踪锚点：**
- Yang…Alon 2025（Nat Commun，③）
- Borrus…Higgins-Chen 2026（Aging Cell，②）
- Zhang 等 2022（Aging Cell acel.13538，A）
- Moqri 等 2023（Cell，"Biomarkers of aging for the identification and evaluation of longevity interventions"，A/surrogate）
- Yücel & Gladyshev 2024（Nat Commun，①）

## 4. 筛选与判定

- **题名/期刊初筛：**
  - 纳入：方法学、框架、综述或形式分析，且讨论"读数变年轻 ≠ 系统变年轻"的某一机制。
  - 排除：单一干预的效果报告，且无方法学主张；单纯开发时钟的研究；动物或细胞生物学机制研究，且未讨论推断问题。
- **对纳入项读摘要**，必要时读全文，并按 A/B/C 判定：
  - **A 命中：** 统一处理至少两层，并给出可操作判据 → PI 的整体框架主张降级。
  - **B/C 命中：** 已有相应形式结果 → PI 在该层只能引用，不能主张增量。
- **PI 的处置规则（预先固定）：**
  - A 命中且覆盖三层 → PI 降为综述或评论。
  - A 命中但只覆盖两层，或 B/C 部分命中 → PI 保留为原创，但贡献声明收窄为未覆盖部分。
  - 都未命中 → 保留原创，同时声明检索局限（没有 Scopus，单人筛选）。

## 5. 记录

- 每条检索式记入 `knowledge_base/search_logs/SEARCH_LOG_2026-11-27_PI_NOVELTY.csv`（13 列模板），写明命中数、筛选数、纳入家族、排除理由和访问深度。
- 判定结果写入 `NOVELTY_SEARCH_RESULT.md` 与台账。
- **零命中的检索式必须先核对**：放宽一个限制，确认数据库能返回已知相关文献，然后才能记为"无"。

## 6. 协议修改记录

- **M0（协议前探索，不计入正式记录）：** 写协议之前做过一次 esearch（rejuvenation × selection/cell composition × identifiability/estimand/causal inference），命中 0。它启发了 Q2 与 Q4 的拆分，但不作为证据。
- **M1（2026-11-27，Q2 执行后）：** Q2 原式命中 337，retmax=200 只返回前 200 个 ID，且未逐条筛选。原因是 `"selective"[tiab]` 把癌症耐药、代谢/免疫"重编程"文献大量带入。改用 Q2a（去掉 `"selective"`），命中 69。**原式未完整筛选，属于偏离协议**。
- **M2（同日）：** Q2a 前 35 条题名全部与年轻化读数无关，同形词"reprogramming"仍在污染。改用 Q2b：把干预词限定为 rejuvenat*/partial reprogramming/epigenetic reprogramming，把选择词限定为 7 个短语，并加衰老语境词。命中 15，全部筛选。
- **M3（同日，追加）：** 为提高第②层 B 的查全，追加 Q4b（部分识别/可识别性 × 时钟或细胞组成），命中 7。
- **已知项召回核对（替代零命中核对）：** 正式检索式没有零命中，所以 §5 的零命中核对未触发。改做已知项召回：
  - Q5 召回了锚点 Yang…Alon 2025 与 Karin 2019；
  - Q1 召回了 Zhang 2022 与 Gladyshev PNAS 2026；
  - **Q2b/Q8 没有召回 Yücel & Gladyshev 2024**，因为它的选择讨论只在正文、不在摘要。这是摘要级检索的结构性局限，由正向引文追踪与原文核读（P16）补足。
- **锚点 PMID：** Yang 2025 = 40199852；Moqri 2023 = 37657418；Zhang 2022 = 34972247；Yücel 2024 = 38431638；Borrus 2026 = 42850743。Moqri（施引 616 条）以及 Zhang/Yücel/Borrus 的施引，改为"施引 AND 摘要关键词"过滤，没有逐条读全部施引。这是偏离，已记录。

结果见 [NOVELTY_SEARCH_RESULT.md](NOVELTY_SEARCH_RESULT.md)，逐式记录见 [检索日志](../../knowledge_base/search_logs/SEARCH_LOG_2026-11-27_PI_NOVELTY.csv)。
