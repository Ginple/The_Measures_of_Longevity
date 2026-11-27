# L2 Audit Packet — Does *The Measures of Longevity* Need Restructuring After Market Positioning?

Frozen 2026-11-27 (UTC), together with the [pre-registered protocol](MARKET_RESTRUCTURE_AUDIT_PROTOCOL_2026-11-27.md). **Do not edit.** If the packet must change, issue a v2.

## Instructions to the auditor

- You are auditing a book architecture. Use **only** this packet.
- Do not look at the project's own audit receipts, decision rationales, or chat history. They contain the author-side assistant's opinions, and the point of this audit is to test them without that influence.
- Write your receipt as `MARKET_RESTRUCTURE_AUDIT_RECEIPT_L2_<date>.md` (or L3 if you are a human editor, agent, or domain expert). State:
  - who you are, as a category (model / human role);
  - any interest you have in the outcome.
- Be adversarial. Your job is to find what is wrong, not to confirm.

## 1. The question

After the market positioning summarized in §3, and given the author's two decisions in §2, does any of the following need restructuring, and to what level?

| Code | Object | What it is |
|---|---|---|
| O1 | KERNEL | Internal shared core: invariants, definitions, quantitative anchors, forbidden inferences (§5) |
| O2 | Framework | Three volumes, eight parts, 33 chapters (§4) |
| O3 | Outline | The chapter map in §4 |
| O4 | Detailed outline | Section-level outline. **Does not exist yet** |
| O5 | Scaffold | A writing skeleton for an older "maintenance capacity" part, plus an older self-audit; both predate the current architecture |
| O6 | Proposal and writing rules | Book proposal (title, promise, chapter evidence contract) and English manuscript rules |
| O7 | Existing sample text | Chapter 5, as an English draft v0.1 and a Chinese v0.3; seven other Chinese demonstration drafts written for an older numbering |

**Levels** (give each object exactly one):

| Level | Meaning |
|---|---|
| K0 | Keep |
| K1 | Local revision: wording, pointers, stale references, working titles, writing rules |
| K2 | Rearrangement within a part: chapter order, merge or split, add a preface or appendix. Volume and part boundaries unchanged |
| K3 | Architectural restructure: change volumes, parts, or chapter count, or change what a part carries |

**Evidence rules:**
1. Market evidence graded B/C (most of §3) can support at most K2, never K3. K3 needs grade-A market evidence, completed reader interviews, scientific evidence, or an author instruction.
2. Market reasons may never change invariants, evidence grades, claim strength, or forbidden inferences.
3. Grade-C evidence alone triggers nothing.

**Vetoes.** Reject any proposal that does any of the following:
- strengthens a claim without new evidence;
- drops Volume III below 28% of chapters or of actual words;
- brings individual prescriptions, longevity promises, or attacks on named authors into the text;
- rests solely on an unverified rule of thumb;
- conflicts with the author decisions in §2.

**Required adversarial roles.** Perform each:
- (A) a US/Canada trade editor or agent arguing for restructure;
- (B) a scientific-integrity reviewer opposing market concessions;
- (C) a reader-path walk-through for each persona R1–R4;
- (D) a red team on internal documents masquerading as reader structure;
- (E) a status-quo-bias check on any "keep" verdict.

## 2. Author decisions (fixed; not to be audited)

- **Title**: *The Measures of Longevity* — subtitle *Maintaining the Body, Identifying Rejuvenation, and Expanding the Possibilities of a Life Worth Living*. Locked.
- **DEC-016**: English is the first language of the monograph and papers; Simplified Chinese is second, derived from the English.
- **DEC-017**: Length is decided by content, not by a word target. An English full edition of about 200,000 words or more is acceptable. No abridged trade edition is planned at present.
- **Earlier decision**: the book gives no individual prescriptions and promises no life extension.

## 3. Market positioning, round 1 (summary)

- **Priority markets**: (1) USA and Canada; (2) other English-speaking countries; (3) Simplified Chinese, Traditional Chinese, Japan.
- **Working positioning**: "For readers who already track their health — or are being sold tests that claim to — the book explains what longevity numbers can and cannot tell you, how to judge claims that someone has 'become younger,' and why a longer life only matters if it remains a life worth living."
- **Lane**: "measurement literacy + life judgment". Not a clock book; not a protocol book.

**Facts** (grade in brackets: A = industry or official statistics; B = retailer, publisher or major media; C = blogs or third-party estimates):

- US adult nonfiction 2025: $6.0B (+1.3%); unit sales −0.3%, so growth came from price. [A]
- US audiobooks $2.5B (+5.3%) exceed ebooks $2.2B (+3.2%); publishers report AI narration is 0.03% of revenue. [A, partly secondhand]
- Amazon "Aging" bestsellers at search time: Means *Good Energy*, Attia *Outlive*, *Ikigai*, Buettner *Blue Zones Kitchen*, Topol *Super Agers*, Gupta *Keep Sharp*, Longo *The Longevity Diet*. [B, snapshot]
- Clock-centred popular books have modest reach: Levine *True Age* ~128 Goodreads ratings; Steele *Ageless* ~1,500; Brendborg *Jellyfish Age Backwards* ~6,000. [B, weak proxy]
- Consumer biological-age testing: Function Health claims >500k members; TruDiagnostic claims >120k tests; a third-party summary says none has been shown to make people healthier. [C, company claims]
- Common criticisms of *Outlive*: causal claims from observational data; heavy testing and overdiagnosis risk; unclear marker–outcome links; male-dominated study populations. [C]
- Canada print 2025: C$1.146B, +4.1%; nonfiction 30%; Canadian-author share 14%. [A]
- UK nonfiction 2025 about −3%. [C]
- Japan: Sinclair *LIFESPAN* translation sold >100k copies; readers mostly aged 40–59. [B]
- Taiwan: two-volume sets of long health books sell. [B]
- **Not available**: BookScan or Nielsen unit data; reader interviews. Both are planned but not done.

**Personas:**

| Code | Persona | Their question | Chapters the author side maps them to |
|---|---|---|---|
| R1 (core) | Ages 35–60, educated, has bought a biological-age test or wears a tracker, has read *Outlive* | "My biological age is 5 years younger — what does that mean? This intervention made me 3 years younger — is that credible?" | Vol I (1–9), 18, 20, 25, 29 |
| R2 | Primary-care clinicians, nurses, pharmacists, trainers, dietitians | How to explain test reports and "age reversal" claims without overselling or dismissing | 4, 5, 18, 29, 31 |
| R3 | Science-minded general readers (*Why We Die*, *Ageless*) | What aging science knows and does not know | Vol II (10–22), 32, 33 |
| R4 (secondary; possibly primary in Japan/Taiwan) | Caregivers of aging parents; local health and housing policy people | How longevity relates to a life worth living; how resources are allocated | Vol III (23–30) |
| R5 (companion) | Students and researchers | Methods and identifiability | Companion papers, appendices |

**Marketing red lines**: no life-extension promises; no individual prescriptions (FTC health-claim rules); no "first framework" or "fills the gap" language; company data labelled as company-reported; criticise methods, never people.

## 4. Current architecture (DEC-011; English working titles)

- **Evidence class**: S = mostly published/measured; M = mixed; H = led by hypothesis, synthetic model or experimental contract.
- **"Inherited"**: the number of numbered chapters from two earlier Chinese manuscripts (V6: 33 chapters; V7: 39 chapters) assigned to that chapter by title. 0 = new writing.

| Ch | Volume · Part | English working title | Evidence | Paper link | Inherited |
|---|---|---|---|---|---|
| 1 | Ⅰ Measures · Part 1 Questions | What Does Longevity Actually Measure? | M | — | 1 |
| 2 | Ⅰ · Part 1 | Age Is Not the Only Clock | S | — | 2 |
| 3 | Ⅰ · Part 1 | Explanation, Prediction, Control, and Benefit | M | — | 3 |
| 4 | Ⅰ · Part 1 | What Counts as Evidence: Denominators, Source Families, and Replication | S | P3 | 1 |
| 5 | Ⅰ · Part 2 Four Measures | Measurement Contracts: Prediction, Responsiveness, Mechanism, Surrogacy | M | PI | 2 |
| 6 | Ⅰ · Part 2 | Level: What a Single Reading Tells You | S | PI | 0 |
| 7 | Ⅰ · Part 2 | Rate: A Slope Is Not a State | S | PI | 0 |
| 8 | Ⅰ · Part 2 | Recovery: The Capacity You See Only After a Perturbation | M | PI | 2 |
| 9 | Ⅰ · Part 2 | Reserve: How Far from the Threshold? | M | PI | 0 |
| 10 | Ⅱ The Body · Part 3 Maintaining the Body | Maintenance, Repair, Replacement, and Compensation | M | — | 2 |
| 11 | Ⅱ · Part 3 | The Costs of Damage and Repair | M | — | 4 |
| 12 | Ⅱ · Part 3 | Organs, Interfaces, and Environments | M | — | 5 |
| 13 | Ⅱ · Part 3 | Competition Within the Body | M | — | 3 |
| 14 | Ⅱ · Part 4 Identifying Rejuvenation | Identity: Who Is Getting Younger? | M | PI | 2 |
| 15 | Ⅱ · Part 4 | Younger Samples, Younger Entities: State Turnover | M | PI | 2 |
| 16 | Ⅱ · Part 4 | The Weights Inside Composite Measures | M | PI | 4 |
| 17 | Ⅱ · Part 4 | History and Memory: After This Repair, How Many Remain? | H | P5 | 4 |
| 18 | Ⅱ · Part 5 Interventions and Costs | When Markers and Outcomes Part Ways | S | PI | 2 |
| 19 | Ⅱ · Part 5 | Reprogramming and Senescent Cells: After Clearance, Who Takes Over? | M | — | 4 |
| 20 | Ⅱ · Part 5 | Tiers of Evidence for Nutrition, Exercise, Prevention, and Medicine | S | — | 4 |
| 21 | Ⅱ · Part 5 | Capacity Accounting I: Who Maintains Whom, and When Help Arrives | H | P4 | 1 |
| 22 | Ⅱ · Part 5 | Capacity Accounting II: Reserve You Cannot Use | H | P4 | 1 |
| 23 | Ⅲ Life · Part 6 Conditions of a Life | Housing, Environment, and Infrastructure | S | — | 2 |
| 24 | Ⅲ · Part 6 | Care, Dependence, and Autonomy | M | — | 1 |
| 25 | Ⅲ · Part 6 | Bodily Experience and Technological Monitoring | M | — | 2 |
| 26 | Ⅲ · Part 6 | Art, Relationships, and Meaning | M | — | 3 |
| 27 | Ⅲ · Part 6 | Inequality and Distribution | M | — | 1 |
| 28 | Ⅲ · Part 7 Judgment and Action | Different Trade-offs for Different People | M | — | 2 |
| 29 | Ⅲ · Part 7 | Clinical and Personal Decisions | S | — | 4 |
| 30 | Ⅲ · Part 7 | Two Ledgers and a Minimal Safe Architecture for LIFE OS | M | — | 2 |
| 31 | Ⅲ · Part 8 Revisable Knowledge | How to Read Conflicting Studies | S | P3 | 2 |
| 32 | Ⅲ · Part 8 | Unknowns and the Anomaly Log | M | — | 3 |
| 33 | Ⅲ · Part 8 | Knowledge That Can Be Withdrawn | M | — | 1 |

- **Volume III protection rule**: if Volume III falls below 28% of chapters or of actual words, stop expanding Volume II.
- **The "four measures"** (level, rate, recovery, reserve) are a reorganisation of established constructs: biomarker level; longitudinal slope; stimulus–response and critical slowing; physiological reserve and Strehler–Mildvan vitality. The book claims only to put them into one estimand framework and to show why a single-time-point reading cannot distinguish them.
- **Companion papers**:
  - PI, a merged paper on the identifiability of rejuvenation, with three layers: selection/identity, aggregate weights, readings versus parameters;
  - P3, research assurance, conditional;
  - P4 and P5, deferred or contract-only.

## 5. KERNEL summary (internal; Chinese in the repository)

**Invariants:**

| ID | Invariant |
|---|---|
| I1 | Explanation ≠ control ≠ benefit ≠ deciding for others what a good life is |
| I2 | A better average reading does not imply that the same entity became younger: within-type change, composition change and a cross term must be separated |
| I3 | Cellular fitness ≠ host fitness |
| I4 | Persistence can be damage or maintenance |
| I5 | Average capacity ≠ reachable capacity |
| I6 | Persistence of a state label does not split maturation from other loss |
| I7 | Cell-average, molecule-weighted and individual-function readings are different |
| I8 | Values are not collapsed into one score ("two ledgers") |
| I9 | Claims must be able to fail and be withdrawn |
| I10 | Any "rejuvenation" claim must answer four questions: cell number, composition, lineage fate, within-type function |
| I11 | A reading is not a parameter: a younger snapshot can come from changed state, rate or reserve |

**Other content:**
- Canonical definitions: maintenance capacity (a concept awaiting formalisation; an earlier formula was withdrawn); rejuvenation attribution; observation operator; identity map; recovery trajectory; the four measures; "measure" in three senses (measurement, limits of intervention, life judgment).
- About 45 quantitative anchors, each with "allowed interpretation" and "most dangerous misreading".
- Nine candidate paradigm shifts: six inherited, two added, one flagged as a duplicate.
- An 8-step estimand skeleton.
- About 10 added forbidden inferences, for example "a clock falling X years = X years of rejuvenation".

**Known state:**
- The KERNEL is internal and Chinese-language.
- Some anchor rows still refer to part numbers of an older architecture (for example "Part Ⅷ", "Part Ⅸ").
- It has not been fully re-verified item by item.
- No independent external review has taken place.

## 6. Manuscript state

- **Chapter 5**: English v0.1, about 2,200 words of body text. Five claim units are bound verbatim to source excerpts, with drift detection. The Chinese v0.3 is bound the same way.
- **Seven other Chinese demonstration drafts** exist for chapters now numbered 1, 15, 17, 19, 21 (two drafts) and 22. Each is marked as needing review under the new numbering.
- **Chapters 6, 7 and 9** inherit nothing and must be written from scratch.
- **No detailed (section-level) outline exists** for any chapter.
- **An older writing scaffold** exists for a six-module "maintenance capacity" part that was dissolved into chapters 15, 17, 19, 21 and 22.

## 7. Receipt checklist

- [ ] One K level per object O1–O7, with reasons.
- [ ] Numbered findings, each with severity, evidence (a section of this packet) and level.
- [ ] Veto check for every proposal.
- [ ] Persona walk-through table: for R1–R4, the entry chapter, core chapters, and the likely drop-off point.
- [ ] For every K0/K1 verdict: the strongest counter-argument, and what evidence would upgrade it.
- [ ] Your own uncertainties.
