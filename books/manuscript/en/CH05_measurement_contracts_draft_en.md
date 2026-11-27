# Chapter 5 | Letting Numbers Answer the Questions They Can Answer

> **Draft v0.1 (English), 2026-11-27.** This is the first chapter drafted under DEC-016, which makes English the first language of the monograph and Simplified Chinese the second. It is an English rewrite of the Chinese demonstration draft v0.3 ([CH15_测量合同_示范稿.md](../CH15_测量合同_示范稿.md), now chapter 5 of [OUTLINE_v1](../OUTLINE_v1.md)). It keeps every number and source of v0.3 and adds no new empirical claim.
>
> **Status:**
> - For author and domain review only; not a frozen text.
> - Self-checked by the same assistant against v0.3; independent external review has not taken place.
> - The verbatim claim-to-source binding in the [ch5 pilot](../../../knowledge_base/pilots/ch05_measurement_contract/README.md) still points at the Chinese v0.3 text. This English text is **not yet bound**: re-binding it is the next step before it can replace v0.3 as the canonical version.
> - The chapter is about judging measurements. It does not give personal screening, medication, or diet advice.

One report says your biological age is two years younger than your actual age. Another says your blood test is positive and you need further examination. Both pieces of paper carry numbers, yet they invite completely different actions. The first may change how a person imagines their own body. The second may send a person to hospital for imaging, endoscopy, or other follow-up. Whether a reading can be repeated, what a reading means, and what happens when we act on it are three different questions.

The distinction does not belong only to the laboratory. One person's walking pace may slow, yet she can still shop for groceries on her own. Another person walks at the same pace but lives in a building without a lift and is confined to his home. We should not conclude that the second situation is less scientific because a blood marker cannot summarize it. On the contrary: to make measurement serve life, we first have to admit that there is still a road between a reading and a life.

## 1 | A reading is not the body's whole account

Biological age is not a quantity that can be read off a calendar like a date of birth. Different models use different information. Some use blood chemistry, some use DNA methylation patterns. Some are trained to predict chronological age; some are tied to mortality risk or to a particular physiological change. A model that predicts an outcome has not thereby measured every mechanism of aging. A model that changes after an intervention has not thereby shown that the intervention changed long-term clinical outcomes.

Keeping these abilities apart protects the measurements that are genuinely useful.

- **Reliability** asks whether a reading is stable for the same sample or under similar conditions.
- **Predictive ability** asks whether a reading helps distinguish who is at higher risk of a future outcome.
- **Mechanistic specificity** asks which layer a change comes from: inside cells, the composition of cells, or the measurement batch.
- **Responsiveness** asks whether the reading changes after an intervention.
- **Surrogate-endpoint status** asks something more: can a change in the reading be used to infer, reliably, the intervention's effect on the clinical outcome we actually care about?

The earlier abilities may be the foundation for studying the later ones, but they cannot stand in for the later validation.

This distinction is not just theoretical caution. A 2026 systematic review included 26 human intervention studies that reported changes in both methylation clocks and clinical outcomes. No controlled comparative study showed full agreement between clock and clinical outcome. No intervention–clock–outcome combination met the conditions for pooled analysis, and the review found no trial-level surrogate validation. The certainty of evidence was rated very low. The authors concluded that clocks can currently count only as exploratory or supportive readings, not as validated clinical surrogate endpoints.[^7] Another study took intervention data previously reported as positive on a single clock and extended them to more clocks: none of the added clocks reached statistical significance.[^8] This does not show that those interventions failed. It shows that a change in one clock cannot, on its own, carry the sentence "you became younger."

The CALERIE calorie-restriction trial gives an example. Investigators reported that some biological-age measures responded differently to the intervention. A separate bone-density analysis found unfavorable changes at some skeletal sites in the restriction group. The two reports do not use exactly the same samples and measurements, so their group averages cannot be stitched together into the complete fate of any one participant. Still less can we conclude that because one marker moved in the hoped-for direction, fracture risk, function, or lifespan must have improved. Equally, a change in bone density cannot automatically be converted into an observed increase in fractures. The intervention's target, the degree of restriction actually achieved, supplementation and monitoring, the length of observation, and each outcome all need to be recorded separately.[^1]

None of this argues for waiting until every question is answered before acting. In ordinary life, people must often choose on incomplete evidence. The job of a measurement contract is to state the incompleteness clearly, so that numbers have a chance to meet a person's actual situation, rather than posing as a referee who decides on that person's behalf.

## 2 | Whose change, and at what time?

A follow-up study can provide important clues without still answering the original randomized question. Suppose investigators first randomize an intervention and then regroup participants by the changes that actually happened to them: those who kept declining, those who later rebounded, those who barely changed. The new grouping helps describe different trajectories, but the trajectories were not randomly assigned. The illnesses, behaviors, and living conditions that shaped a trajectory may also shape the final measured outcome. Statistical adjustment for known differences is valuable, but it does not automatically remove unmeasured ones.

A 2026 analysis of CALERIE provides exactly this kind of example. Among the original trial's 190 analyzable participants, the authors grouped people by their weight trajectory from month 12 to month 24. The group with the largest rebound had only 20 people, and it included members of both the original restriction arm and the original control arm. Having 190 participants does not mean every measure has 190 results at every time point: the supplementary table lists 57 missing values for baseline insulin area under the curve, and the exact grouping and pairing remain to be verified. The investigators observed metabolic differences accompanying the different trajectories. But the second year still fell within the original trial's intervention and maintenance window, so the result cannot be told as "a randomized comparison after stopping the intervention proved something." Nor did the study measure how many more or fewer years any individual would live.[^2]

"Before" and "after" call for the same care. If a blood sample taken before a cancer diagnosis shows a different marker level, that cannot exclude a disease that was already present but not yet detected. A study may align event times to the nearest annual visit in order to use the data available. But if the diagnosis came after that visit, the visit should not be imagined as a strict post-diagnosis measurement. Temporal alignment is not a detail of the spreadsheet; it decides whether a causal sentence can stand.[^3]

## 3 | One mixed reading may tell more than one story

A blood sample contains many kinds of cells. A change in its reading may reflect a change inside one cell type, a change in how much each cell type weighs in the mixture, or both. Even in a minimal linear model with two cell types, where each type's effective weight is assumed to be exactly known and unchanging, a fall in the total reading can be compatible with the value inside one type either rising or falling. This counterexample is not an estimate of a real human body. It shows only that limited information is not enough to select a single story.[^4]

That does not make compositional change unimportant. If a harmful cell type declines, overall health may benefit. If a protective cell type declines, the overall reading may look better while leaving a new vulnerability behind. The point is not to demand that every improvement happen inside the same cell. It is to keep clear **what changed, who was counted, and which changes bear on the function we actually want to improve.**

More measurement can help, but under conditions. In an idealized model, if we independently know a plausible range for one cell type, the possible range for the other narrows. If we can measure the same components twice, with different and known weights, we can sometimes solve for both types' values. But if the two sets of weights are very close, small reading errors can be greatly amplified. In real samples, whether two measurements come from the same state, whether cell sorting is pure enough, and whether the instrument is stable must each be tested separately. An answer that can be computed is not necessarily an answer that can be relied on.

So a responsible clock study should at least do four things:
- prespecify the primary clock and the clinical or functional endpoint;
- report cell composition and batch alongside the clock;
- estimate measurement error with repeated sampling;
- correct for multiple comparisons when several clocks are used.

Several clocks pointing the same way is a sieve, not a clinical certification. Two intervention arms of the same trial cannot be recounted as two independent replications.

## 4 | Detecting more does not automatically mean harming less

Screening makes a more specific promise than prediction. We do not only want to know who may become ill. We hope that a test, and the actions that follow it, will reduce suffering or death without causing too much harm.

Detecting more early cancers is an important observation, but we also have to look at late-stage cancers, deaths, follow-up procedures, and overdiagnosis. Finding a disease earlier sometimes changes the outcome. Sometimes it only moves forward a diagnosis that would have been made a little later anyway. And some lesions might never cause a problem in a person's remaining lifetime, yet bring further tests or treatment once they are found.

NHS-Galleri is a large randomized trial in England. About 142,000 people volunteered to be randomized between usual care plus a multi-cancer early-detection blood test and usual care alone (control).
- Median follow-up after the last screening round was 17 months. This is not an observation of anyone's whole life.
- The primary analysis compared the incidence of stage III/IV cancer after three screening rounds, for 12 prespecified cancer types: 706 cases in the intervention group versus 688 in the control group, a rate ratio of 1.03 (95% confidence interval 0.92 to 1.14).
- That primary comparison did not show a reduction in late-stage diagnosis. It neither proves that every possible screening benefit is absent, nor can it be described as having shown a reduction in cancer deaths.
- The authors reported that stage IV results point in a direction worth further study. But once the primary test has not been passed, the related secondary results are descriptive and cannot be treated as established conclusions.[^5]

Age can also change the balance of screening. A Canadian microsimulation estimated the share of overdiagnosis among screen-detected cancers under specific assumptions about screening frequency, participation, and the natural history of cancer. The estimate was about 1.1% for ages 50–54 and 10.8% for ages 75–79.
- The denominator is **screen-detected cancers** in each age band, not everyone screened.
- The model is not data from NHS-Galleri participants.
- The age bands in the model's tables and in the description of the protocol differ in ways that still need clarification.
- These numbers serve only to show that the balance shifts with population and assumptions; they are not individual risks.[^6]

In a trial, a positive blood test is not a full stop without cost. A positive result requires confirmation. The yield of follow-up tests, false alarms, overdiagnosis, worry, travel, and cost may fall on different people. Deaths and overdiagnosis need appropriately long observation; they cannot be deduced directly from early detection counts or model predictions. When clinicians and patients discuss testing, they must also take into account existing recommended screening, the person's circumstances, and their preferences. This chapter does not advise any individual on whether to take a particular test.

## 5 | A revisable measurement contract

Faced with an attractive number, we can first write it down as a short contract. The contract does not require everyone to master statistical software. It asks whoever presents the result to answer five questions:

1. **Object and unit:** Is this a cell, a sample, a person, or a population? Is the value in years, a rate per person-year, a probability, a standardized difference, or a dimensionless rate?
2. **Comparison and time:** Compared with what control, from which time point to which? Was the control randomized, or formed afterwards from the outcome?
3. **Observation and missingness:** Who could be measured, and who is absent from the result because of loss to follow-up, death, or sample quality? Did instruments or processing change the reading?
4. **Outcome and trade-offs:** Is this a mechanistic clue, a prediction, a clinical event, or a person's function and life chances? Were harms and resource burdens recorded as well?
5. **Uncertainty and failure conditions:** What competing explanations exist? What new evidence would require this sentence to be narrowed or withdrawn?

The contract does not demand that every number be downgraded to "we know nothing." Sometimes a single high-quality randomized trial is enough to support a clear action. Sometimes a stable indicator helps with follow-up. Sometimes all we can say is that a result deserves replication.

More importantly, numbers do not decide for us which costs are worth bearing. Extending life, maintaining function, keeping one's energy, protecting autonomy and relationships do not always fall into a single order. A good measurement should make these questions clearer, not dissolve them into one total score.

The next four chapters take up the four measures in turn. The first is level: what a single reading can, and cannot, tell us.

---

## Editorial evidence contract (not part of the text)

- **Question and reader:** Helps non-specialist readers separate measurement, prediction, intervention, and life judgment. Not a clinical guideline.
- **Objects and terms:**
  - Distinguishes in-body mixed samples, study-group means, individual function, and clinical events.
  - "Biological age" is defined by each specific model.
- **Claim interface:**
  - KERNEL I1, I2, I7, I8, I9, I11.
  - Disputes and open items: X29, X31, X38, X41, X49–X51, X54, X56, X57, X59–X60, X126, X135, plus the sources cited here. KERNEL has not been fully re-reviewed.
  - Verbatim claim-to-source binding exists for the Chinese v0.3 text only ([pilot project.json](../../../knowledge_base/pilots/ch05_measurement_contract/project.json)). **This English text is unbound.**
- **Primary evidence and extraction depth:** As in v0.3.
  - CALERIE methylation and bone reports, and the NHS-Galleri trial paper's main results and methods: targeted extraction.
  - The 2026 trajectory analysis: text, Tables 1–2, and extractable supplementary text.
  - The 2026 cancer–function report: text and extractable supplementary tables.
  - No patient-level reanalysis; no systematic review of our own.
- **Strongest competing explanations / counterexamples:**
  - Compositional and within-type change can be confounded.
  - Post-randomization grouping is subject to selection and unmeasured confounding.
  - Earlier detection can mean lead time and overdiagnosis.
  - Physical function also depends on environment and personal goals.
- **Prohibited extrapolations:**
  - Marker response is not lifespan improvement.
  - Screening results are not individual medical advice.
  - Correlation is not causation.
  - Population results do not automatically represent each individual.
- **Linked papers:**
  - PI layer ② (composite weights and composition, §3) and layer ① (post-randomization grouping changes who is being compared, §2).
  - P3, for claim invalidation and version tracking.
  - PI layer ③ (readings and parameters) is developed in chapters 6–9.
- **Scope and practice:**
  - CALERIE refers to a specific trial of adult volunteers and its post hoc analyses.
  - NHS-Galleri refers to volunteers in England.
  - The microsimulation is a Canadian hypothetical scenario.
  - Readers can use the contract to ask questions, not as a substitute for medical consultation.
- **Unresolved:**
  - external review;
  - patient-level data;
  - real-world applicability of the mixture model;
  - long-term mortality and overdiagnosis results for screening;
  - global style and chapter order;
  - **re-binding this English text to sources (DEC-016)**;
  - an English terminology list checked against KERNEL.
  - Sources and evidence must be rechecked before publication or freezing.
- **Change impact:**
  - Any ruling on X41/X59/X135, NHS-Galleri follow-up (3- and 6-year mortality analyses), or a change in a key anchor requires rechecking the relevant paragraphs and notes.
  - Until this English text is bound, a change to v0.3 must be carried over here by hand, and vice versa.

[^1]: [CALERIE DNA methylation analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10148951/) ([author affiliation correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC10275750/)) and [bone density paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4834845/). Samples, dose, and evidential limits: [bone and exposure audit](../../../knowledge_base/CALERIE_BONE_AND_EXPOSURE_AUDIT_2026-11-27.md) and [temporal and denominator audit](../../../knowledge_base/CALERIE_TEMPORAL_AUDIT_2026-11-27.md) (in Chinese).
[^2]: [Warmbrunn et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13094879/). Grouping-threshold ambiguity and model limits: [dedicated audit](../../../knowledge_base/CALERIE_WITHIN_TRIAL_WEIGHT_TRAJECTORIES_2026_AUDIT_2026-11-27.md) (in Chinese).
[^3]: [Rösler et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13396198/). Temporal alignment and supplementary tables: [dedicated audit](../../../knowledge_base/DO_HEALTH_CANCER_FUNCTION_2026_AUDIT_2026-11-27.md) (in Chinese).
[^4]: [Synthetic sharp-bound derivation](../../../knowledge_base/experiments/P2_TWO_TYPE_SHARP_BOUNDS_2026-11-27.md), [additional measurements](../../../knowledge_base/experiments/P2_ADDITIONAL_MEASUREMENT_BOUNDS_2026-11-27.md), and [two-mixture inversion](../../../knowledge_base/experiments/P2_TWO_MIXTURE_INVERSION_2026-11-27.md). These are not measured data or a clinical clock validation.
[^5]: [NHS-Galleri trial report](https://pmc.ncbi.nlm.nih.gov/articles/PMC7619610/), methods and results. The different estimands of trial and model: [screening audit](../../../knowledge_base/SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md) (in Chinese).
[^6]: [Malagón et al. microsimulation](https://pmc.ncbi.nlm.nih.gov/articles/PMC13740675/), Table 2 and scenarios. Assumptions, denominator, and age-band issues: [screening audit](../../../knowledge_base/SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md) (in Chinese).
[^7]: [Yi et al., *Exp Gerontol* 2026;226:113367](https://doi.org/10.1016/j.exger.2026.113367), systematic review; abstract read only (ledger X135).
[^8]: [Borrus et al., *Aging Cell* 2026;25(10):e70756](https://pmc.ncbi.nlm.nih.gov/articles/PMC13650178/) (ledger X126). The authors also propose three criteria for increasing credibility. The paragraph above on what a responsible clock study should do carries over the rules organized in V7 chapter 06.
