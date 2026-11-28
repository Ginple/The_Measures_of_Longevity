# Glossary (back matter B1) — working draft v0.1

*2026-11-28. English is canonical (DEC-016); the Simplified Chinese column gives the second-language term. Checked against [KERNEL v0.9.11](../../../knowledge_base/KERNEL.md) by `tests/test_glossary_en.py`.*

**What this list is.**
- It fixes one English word for each concept the book relies on, so chapters do not drift between synonyms. Owner chapters follow the [ownership table](DETAILED_OUTLINE_SPEC.md) §3.
- The printed glossary (B1) will be shorter and written for readers. This working list also records deprecated words and the KERNEL or ledger anchor behind each entry.
- A term marked **KERNEL** must keep the Chinese term that KERNEL uses. If KERNEL changes, this file and the chapters that use the term must change with it (KERNEL §7).
- Candidate glossaries in uploaded files, such as V7.0 EN Appendix B, were not copied. Where they differ, this list and KERNEL govern.

## 1. The four measurable quantities (chapters 6–9)

| Term | 中文 | Meaning in this book | Owner | Not to be confused with | Anchor |
|---|---|---|---|---|---|
| level | 水平 | Where a quantity stands at one time: a stock or a reading | 6 | rate; "biological age" as a whole | KERNEL §2 |
| rate | 速率 | How fast a level changes over time, within the same person or system | 7 | a cross-sectional difference between age groups | KERNEL §2; X150, X130 |
| recovery | 恢复 | How quickly a system returns toward its former course after a perturbation | 8 | a single post-intervention reading | KERNEL §2 (Varadhan 2008) |
| reserve | 余量 | Distance from the current level to the threshold at which a system fails | 9 | **margin** (deprecated: used in KERNEL up to v0.9.10, X158); spare capacity that cannot be reached (chapter 22) | KERNEL §2; X129–X132 |

These four are measurement categories, not parameters, unless a stated model makes them parameters (KERNEL §2, I11). None is original to this project.

## 2. Readings and what they can carry

| Term | 中文 | Meaning in this book | Owner | Not to be confused with | Anchor |
|---|---|---|---|---|---|
| reading | 读数 | The number a test reports for one sample at one time | 6 | the biological quantity the test is meant to track | KERNEL I11 |
| parameter | 参数 | A quantity in a stated model that governs how readings change (for example damage production or clearance) | 6 (stated), 9 (closed) | a reading; I11: a reading is not a parameter | KERNEL I11 |
| reference population | 参照人群 | The people a reading is compared with ("younger than whom?") | 6 | the general population; the reader's own peers | X149 |
| cell composition | 细胞构成 | The mix of cell types in a sample; a change in the mix can move a mixed reading | 15 | noise; fraud. Composition can be real biology | KERNEL I2 (KERNEL form: 构成); X162 |
| biological age | — | A model's estimate of age from biological data, compared with a reference population | 6 | a measured property of the body; "real age" | X149, X162 |
| age acceleration | 年龄加速 | The gap between a clock's estimate and calendar age | 6 | rate of aging (a gap at one time is a level) | KERNEL §3.2; X162 |
| pace of aging | — | A reading trained to estimate a rate of change from one sample | 7 | an observed within-person change | X96, X126, X27 |
| challenge test | 负荷试验 | A defined, safe push (standing up, a glucose drink) followed by repeated readings of how the system responds and returns | 8 | a single reading taken after the push; a push created on purpose outside clinical care | X165; X132 |
| resilience | — | Used in the literature for recovery after a disturbance, with no agreed definition; the book says "recovery" and names the push, the start and the time to return | 8 | robustness; adaptation; a consumer "recovery score" | X165 |
| extrapolated divergence point | — | The age at which a fitted trend, projected beyond the data, reaches infinity or zero | 8 | a lifespan limit; an observed age at death | X86, X165 |

## 3. The measurement contract (chapter 5)

| Term | 中文 | Meaning in this book | Owner | Not to be confused with | Anchor |
|---|---|---|---|---|---|
| measurement contract | 测量合同 | The explicit statement of which of the five properties below a reading has shown, for whom, and on what evidence | 5 | a certificate of validity | KERNEL §3 (part-number mapping) |
| reliability | — | Stability of a reading for the same material or under similar conditions | 5 | accuracy; validity | X163 |
| predictive ability | 预测能力 | Whether a reading helps tell who is at higher risk of a future outcome | 5 | causal effect; surrogacy | KERNEL §3.2 |
| mechanistic specificity | 机制特异性 | Which layer a change comes from: inside cells, cell composition, or the measurement | 5 | biological plausibility | KERNEL §3.2 |
| responsiveness | 响应性 | Whether a reading changes after an intervention | 5 | benefit; surrogate status | KERNEL §6; X96 |
| surrogate endpoint | 替代终点 | A reading whose change reliably predicts an intervention's effect on a clinical outcome, validated at trial level | 5 | a responsive or predictive reading | KERNEL §6; X135 |

## 4. Attribution and bookkeeping (Volume Ⅱ)

| Term | 中文 | Meaning in this book | Owner | Not to be confused with | Anchor |
|---|---|---|---|---|---|
| identity map | 身份映射 | The rule that matches baseline entities to follow-up entities (same cell, lineage, clone or person) | 14 | a barcode; philosophical identity | KERNEL §2 |
| rejuvenation attribution | 年轻化归属 | Bookkeeping that assigns an improved reading to who changed and at which layer | 14 | proof of rejuvenation | KERNEL §2 |
| observation operator | 观测算子 | The mapping from the state of entities to a reported reading (number, copies, capture, normalisation, threshold) | 16 | the assay alone | KERNEL §2 |
| recovery trajectory | 恢复轨迹 | System behaviour after an intervention stops or a new challenge arrives; part of the outcome | 8 | follow-up as optional extra information | KERNEL §2 |
| state turnover | 状态周转 | Persistence of a cell-state label as distinct from persistence of the cells carrying it (I6) | 15 | migration; cell survival | KERNEL I6 |
| maintenance capacity | 维护容量 | A research concept for discussing source output, timely and spatial reachability, selectivity and the contribution of removed components. **Not a formula** | 21 | the withdrawn multiplicative identity (KERNEL §2) | KERNEL §2 |
| capacity accounting | 容量核算 | Chapters 21–22's bookkeeping of who maintains whom, when, and where | 21, 22 | a single capacity score | KERNEL §5 |
| estimand | estimand | What exactly is to be estimated: population, variable, time window, handling of missing data, observation operator, attribution, decision rule | 5 (contract), 14–16 | an estimate; an endpoint name | KERNEL §5 |

## 5. Judgement and life (Volume Ⅲ)

| Term | 中文 | Meaning in this book | Owner | Not to be confused with | Anchor |
|---|---|---|---|---|---|
| measure (three senses) | 尺度 | Measurement (readings); the limits of intervention; life judgment. Kept distinct in the text, not used as a pun | 1 | — | KERNEL §2 |
| two ledgers | 双账本 | Body maintenance and life opportunities kept as separate accounts, never added into one life score (I8) | 30 | a wellness index | KERNEL I8 |

## 6. Words the manuscript avoids

| Avoid | Why | Use instead |
|---|---|---|
| margin (for reserve) | Superseded canonical term (X158) | reserve |
| "reverses aging", "X years younger" as an outcome | KERNEL §6: a clock change is not rejuvenation of X years | "the reading fell by X years" plus what it does and does not show |
| "first", "fills the gap", "first framework" | Prior art exists (X85, X133–X137); market section 4 | describe what is done, with citations to prior work |
| "proven safe" / "10–100 times cancer risk" (reprogramming) | KERNEL §6: both extremes unsupported | state what was measured, in whom, for how long |
| "150-year lifespan limit" | KERNEL §6, X86 | "the extrapolated divergence point in one model" |
