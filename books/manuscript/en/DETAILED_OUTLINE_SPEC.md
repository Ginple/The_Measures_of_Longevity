# Detailed Outline: Specification and Concept Ownership

*Working draft v0.1, 2026-11-27.*

- **Origin.** Created on the recommendation of the [post-positioning restructure audit](../../../review/MARKET_RESTRUCTURE_AUDIT_RECEIPT_L1_2026-11-27.md) (findings F-02 and F-03, level K2: a new layer; no text is moved).
- **Review status.** Written by the same assistant that wrote most of the plan it describes. Not independently reviewed (D05 open). The author may overrule any part of it.

## 1. Why this layer exists

Under DEC-017, content decides length: there is no total word target and no per-chapter target. That removes one crude control on scope, so something else must do the job. The detailed outline does it in three ways.

1. **Ownership.** Each concept, invariant and recurring case is *developed* in exactly one chapter. Other chapters may *use* it in a sentence or two and point back.
2. **Load-bearing sections.** Every section names the reader question it answers, or the claim it carries. A section that does neither is cut or moved.
3. **Right layer.** Derivations, assay details and long tables are assigned to back matter B3 (Methods Appendix) or a companion paper before drafting starts. This keeps the running text listenable for the human-narrated audiobook.

A chapter is not drafted in English until its detailed outline exists (writing rule 9 in [README](README.md)).

## 2. Fields for each chapter

| Field | Content |
|---|---|
| Working title | Map key from [OUTLINE_v1](../OUTLINE_v1.md); stable |
| Reader-facing title | Candidate only; settled when the chapter is drafted (writing rule 7) |
| Readers and questions | Personas R1–R5 from [market positioning §2](../../market/MARKET_POSITIONING_2026-11.md), each with the question in their own words |
| Owns | Concepts, invariants (KERNEL I1–I11) and cases that this chapter develops |
| Uses, does not develop | Concepts owned elsewhere, each with its owner chapter |
| Sections | Numbered; one line each stating the question or claim |
| Candidate evidence | Ledger IDs (X-numbers) and inherited source chapters. *Candidate* means not yet bound: a number enters the text only after it is traced to a ledger entry or bound excerpt |
| Strongest counterexample or competing explanation | Required |
| Not answered here | Questions a reader may expect that the chapter leaves to others or cannot answer |
| To appendix or paper | Material assigned to B3, B4 or a companion paper |
| Gaps | Missing evidence, or searches still needed |

## 3. Concept ownership across the 33 chapters

This table only assigns concepts to chapters. It is not a content audit. When a chapter's detailed outline is written, it may propose moving ownership; any such move is recorded here with a reason.

| Concept, invariant or case | Owner | Used briefly in |
|---|---|---|
| Three senses of "measure": measurement, limits of intervention, life judgment | 1 | Introduction F1, 30, 33 |
| Five questions of the book (what is maintained, who changes, what is observable, what is controllable, why it matters) | 1 | F1 |
| Lifespan, healthspan, health-adjusted life expectancy; the healthspan gap (X21); the "lifespan limit" statistic | 2 | 1, 28 |
| I1 explanation ≠ prediction ≠ control ≠ benefit ≠ deciding for others | 3 | 1, 18, 29 |
| Denominators, source families, replication as everyday reading skills | 4 | 5, 31 |
| Adjudicating conflicting studies with worked cases; ranking research without false precision | 31 | 4 |
| Measurement contract: reliability, prediction, mechanistic specificity, responsiveness, surrogacy | 5 | 6–9, 18, 29 |
| "Detecting more is not harming less" (screening as a contract example) | 5 | 29 (decision side) |
| I11 a reading is not a parameter (state, rate or reserve) | 6 (stated), 9 (closed) | 5, 7, 8, 18 |
| Reference population of a reading (X149) | 6 | 25 |
| Slope versus state; cross-sectional versus longitudinal (X150, X130); pace-of-aging clocks and responsiveness (X96, X126) | 7 | 18 |
| Recovery after perturbation; recovery period as part of the outcome (paradigm shifts 5 and 8) | 8 | 17, 19 |
| Reserve as distance to threshold; converting reserve into years (X129–X131) | 9 | 22, 24 |
| Maintenance, repair, replacement, compensation as distinct routes | 10 | 19, 20 |
| Costs of damage and of repair | 11 | 19 |
| Interface-centred view of organs (paradigm shift 4) | 12 | 23 |
| I3 cellular fitness ≠ host fitness; clonal competition | 13 | 18, 19 |
| Identity map; I10 four questions for any rejuvenation claim | 14 | 5, 15, 16, 19 |
| I2 within-type change versus composition change versus cross term; I6 state ≠ cell | 15 | 5 (preview only, one two-type example), 16 |
| I7 levels of measurement; observation operator; weights inside composite scores | 16 | 5, 6 |
| I4 persistence can be damage or maintenance; repair memory | 17 | 11 |
| Marker–outcome divergence: worked cases (CALERIE, colchicine, TranslAGE) | 18 | 5 (definitions only), 20 |
| Reprogramming; senescent-cell clearance; caretaker selectivity | 19 | 13 |
| Evidence tiers for nutrition, exercise, prevention, medicine | 20 | 29 |
| I5 average capacity ≠ reachable capacity (source, recipient, timing) | 21 | 9, 22 |
| Spatially unreachable reserve | 22 | 23 |
| Environment and infrastructure as interventions | 23 | 1, 27 |
| Dependence, care, autonomy | 24 | 1, 28 |
| Self-monitoring, wearables, consumer test practices, digital twins | 25 | F1, 29 |
| Meaning, purpose, relationships, art | 26 | 1 |
| Inequality and distribution; the "heritability pie" fallacy | 27 | 23 |
| Trade-offs differ across people; multistate time | 28 | 30 |
| From a test result to an action: clinical and personal decisions | 29 | 5, 25 |
| I8 two ledgers; minimal safe architecture for decision tools | 30 | 28 |
| Known unknowns, anomaly log | 32 | 33 |
| I9 claims that can fail and be withdrawn | 33 | 4, 31 |

**Known overlaps the table resolves** (audit F-03):

- **4 / 31.** Chapter 4 teaches reading skills. Chapter 31 applies them to real conflicts.
- **5 / 18.** Chapter 5 defines the contract. Chapter 18 owns the cases.
- **9 / 22.** Chapter 9 owns reserve as a measurable distance. Chapter 22 owns why measured reserve may not be usable.
- **1 / 2.** Chapter 1 raises the time question. Chapter 2 owns the statistics.
- **5 / 15.** The two-type example in chapter 5 §3 stays a preview. The full decomposition belongs to chapter 15.

## 4. Status

| Volume | Detailed outline |
|---|---|
| Ⅰ (chapters 1–9) | [v0.1](DETAILED_OUTLINE_VOL1.md) |
| Ⅱ (10–22) | Not yet written. Each chapter's outline is written before that chapter is drafted |
| Ⅲ (23–33) | Not yet written |
| Front and back matter (F1, B1–B4) | F1 sketched in the Volume Ⅰ file. B1–B4 accumulate as chapters are drafted |
