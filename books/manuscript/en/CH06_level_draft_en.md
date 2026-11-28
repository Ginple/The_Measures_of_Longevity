# Chapter 6 | One Reading, Many Stories

> **Draft v0.1.1 (English), 2026-11-28.** v0.1.1 corrects "4,058 people" to "4,058 samples", as the source says ([correction record](../../../review/UNSUPPORTED_WORDS_CORRECTION_2026-11-28.md)). Working title in [OUTLINE_v1](../OUTLINE_v1.md): "Level: What a Single Reading Tells You". Written in English first (DEC-016). No earlier chapter is inherited. Follows its entry in [DETAILED_OUTLINE_VOL1](DETAILED_OUTLINE_VOL1.md). The reader-facing title is a candidate until the author confirms it.
>
> **Status:**
> - For author and domain review only; not a frozen text.
> - Self-checked by the same assistant that wrote it. Independent external review has not taken place (D05 open).
> - Eight claim units are bound to verbatim source excerpts or to the project's own synthetic model ([chapter 6 pilot](../../../knowledge_base/pilots/ch06_level_en/README.md)). Sources were read at abstract depth, with two exceptions noted in the pilot. Any edit to this file or to an excerpt makes the affected claims stale until they are re-bound.
> - The chapter is about reading measurements. It does not recommend, rank or discourage any test, product or treatment, and it gives no personal medical advice.

Imagine drawing one tube of blood, splitting it in two, and sending both halves to the same laboratory under two different names. The two reports come back a week apart. One says the body behind the blood is three years younger than its birthday. The other says it is two years older. Nothing about the person changed between the two halves of the tube. Only the measurement did.

This chapter is about what a single reading can carry. It is the first of four chapters on the quantities a longevity number can describe. A **level** is where something stands at one time. The next three chapters take up a **rate** (how fast the level is changing, chapter 7), **recovery** (how quickly a system returns after it is pushed, chapter 8), and **reserve** (how far a system is from the point where it fails, chapter 9). None of these four categories is new; each has a long history in physiology and gerontology. What this book adds is a single discipline for keeping them apart, because one number at one time cannot tell them apart by itself.

## 1 | What a level is, and how much one level can carry

A level is a snapshot. Your cholesterol on Tuesday morning, the length of the telomeres in a blood sample, the "biological age" printed on a report: each is a value at one time, measured in one way, on one kind of sample. A level can be very useful. It can tell you where you stand relative to other people. It can help predict who is more likely to develop a disease. But a level, by itself, says nothing about how fast things are moving, or in which direction.

A level also carries less information than its precision suggests. A number printed to one decimal place feels exact. Whether it is informative depends on how tightly it tracks the thing we care about across real people, and the answer is often "loosely." Telomere length is a useful example, because telomere shortening is a proposed hallmark of aging. A meta-analysis of 414 study samples, covering 743,019 people aged from birth to 112 years, found that the pooled corrected correlation between telomere length and age in cross-sectional samples was about minus 0.19, with a 95 percent confidence interval from minus 0.22 to minus 0.15, and that the correlation weakened in older age groups; how telomeres were measured, and in which tissue, changed the strength of the correlation.[^1] A correlation of that size is real at the level of populations, and it is weak at the level of a person. Two people of the same age can differ widely in telomere length, and one measurement will not place either of them reliably on the aging curve.

None of this makes a level worthless. It means a level answers a narrow question, "where does this sample stand, on this assay, compared with these people?", and every word of that question matters.

## 2 | The same blood, twice

Return to the split tube. The thought experiment is not far from what researchers actually do when they test a measurement's reliability: they measure the same material more than once and see how much the answer moves. For epigenetic clocks, which estimate age from chemical marks on DNA, the answer turned out to be uncomfortable. A 2022 study reported that technical noise alone produced deviations of up to 9 years between replicate measurements for six prominent epigenetic clocks; retrained versions of the same six clocks, built from principal components of the data rather than from individual sites on the genome, brought most replicates within 1.5 years of each other; a later paper from the same laboratory summarized the earlier work as showing that re-testing the same individual could move a clock by between 0.9 and 2.4 years, and that the retrained clocks reduced the median gap between technical replicates to between 0.3 and 0.8 years; a different group, which measured 350 blood DNA samples twice, found that unreliable sites on the genome were less replicable and generated an unknown volume of false negatives.[^2]

Three things follow, and none of them is "never trust a clock."

First, reliability is a property of a specific version of a specific clock on a specific platform. It improved substantially when the method changed. A reader cannot assume that the clock behind a given report is the reliable version, and the report may not say.

Second, reliability limits everything that comes after it. If two halves of one tube can differ by years, then a difference of one or two years between this year's report and last year's may be noise. The question "did my number change?" comes before "what does the change mean?", and it needs to be answered with repeat measurements, not with a single pair.

Third, it matters who reports a reliability problem and who solves it. The authors of the 2022 study disclosed that two of them had built epigenetic aging metrics using the method the paper describes, and that those metrics are licensed to a company, Elysium Health, through their university; the company also supplied some of the replicate data. That disclosure does not make the result wrong. The replicate study from a different group, which declared no competing interests, points in the same direction. But it is the kind of fact a careful reader should know, and it is why this book reports conflicts of interest wherever they are declared.

## 3 | Compared with whom?

"Two years younger than your age" is a comparison, not a measurement. It means that a model, trained on some group of people, predicted a lower age for your sample than for a typical person of your age in that group. Change the group, and the comparison can change.

The most obvious difference between groups of people is the one most clocks have ignored. A 2026 study noted that most biological aging clocks were trained on samples that pooled women and men, implicitly assuming that aging looks the same in both; the authors built 38 sex-specific clocks across 15 organ systems, showed that training them separately mattered for constructing sex-appropriate healthy reference values, and found that the clocks predicted disease and death in a way that depended both on sex and on the organ; they also wrote that pooled and sex-interaction models remain valuable, because women and men share fundamental features of aging and disease.[^3]

The careful reading of that study is not "women and men age by different mechanisms." It is narrower and more useful: the meaning of a reading depends on the reference population behind it. Sex is one dimension. Age range, ancestry, health status, the country and decade in which samples were collected, and the laboratory platform are others. A reading compared with a reference group that does not resemble you is still a number, but it answers a different question from the one you are asking.

This is why the first question to ask of any biological-age report is not "how young am I?" but "compared with whom?" A responsible report names its reference population. If a report does not, that is worth asking about.

## 4 | How much of the reading is the mix of cells?

A blood sample is not one thing. It is a mixture of many kinds of cells, in proportions that shift over time and with age. Most blood-based clocks measure the mixture as a whole. So a change in the reading can come from two quite different sources: a change inside the cells, or a change in which cells are present.

How large is the second source? A 2026 study of 4,058 samples estimated the contribution of blood cell composition to six first- and second-generation epigenetic clocks: up to 53 percent of the variation in clock-estimated age could be attributed to cell counts, with a particularly strong role for the balance between naive and memory T cells; the link between cell counts and "age acceleration" (the gap between clock age and calendar age) was weaker, up to 21 percent of its variation; the authors checked the result with computer-simulated mixtures built from data on sorted blood cells, not with real blood; and, across 176 health outcomes in a separate study of 18,859 people, accounting for composition significantly weakened the association between age acceleration and later disease, although the effect remained modest.[^4]

Read that carefully, because it cuts both ways. It does not say that half of every "rejuvenation" is an illusion. The 53 percent is the top of a range: for five of the six clocks, cell counts explained between 44 and 53 percent of the variation in estimated age across the 4,058 samples, and for the pace-of-aging clock 26 percent. It describes differences between people, not the share of any one person's change after an intervention. Composition is also not noise: a shift from naive toward memory T cells is itself part of how the immune system ages. And the predictive value of age acceleration for disease and death survived the adjustment largely intact: for mortality, the weakening ranged from 1 percent for one clock to 6 percent for another. What the study does show is that a blood clock reading is partly a reading of the cell mix, and that a change in the reading can come from a change in the mix. Whether that matters depends on the question. If you want to predict risk, composition may be useful information. If you want to claim that the cells themselves became younger, composition is a rival explanation you have to rule out.

The arithmetic of mixtures, and why an average can fall even when every component rises, belongs to chapter 15, which owns the question of composition. The formal version is in back matter B3.

## 5 | Eleven organs, one blood draw

Newer tests go further. Instead of one age for the whole body, they report a separate age for the brain, the heart, the kidneys, the immune system and other organs, estimated from proteins in the blood that are thought to come mainly from each organ.

These readings can predict. That should be said plainly, because it is the strongest case against the caution of this chapter. A 2025 study estimated the biological age of 11 organs from 2,916 plasma proteins in 44,498 people in the UK Biobank; the organ ages were sensitive to lifestyle factors and medications and were associated with the later onset of diseases including heart failure, chronic lung disease, type 2 diabetes and Alzheimer's disease over up to 17 years of follow-up; and the more organs that looked aged, the higher the risk of death, rising to a hazard ratio of 8.3 for people with eight or more aged organs.[^5]

So prediction is not in doubt. What a set of organ ages cannot do is count as many independent facts as there are organs. All eleven come from one blood draw, measured on one platform, on one day, in one laboratory batch. Anything that affects that sample, from a recent infection to how long the tube waited before processing, can move several "organs" at once. And a protein assigned to one organ is not necessarily made only there. Eleven readings from one draw are better thought of as eleven views through one window than as eleven windows. This is a point about how the measurements are made, not a result of the study; it is the kind of question a reader should put to any multi-organ report.

There is also a bookkeeping warning. Two large plasma-protein organ-age studies were published in 2025, one with 44,498 people and eleven organs, the other with 43,616 people and ten organs. Both numbers are correct, and they belong to different studies. Mixing them, as this project's own earlier notes once did, produces a study that does not exist.

## 6 | Three ways to look younger at one time point

Suppose a reading does come back younger, reliably, against an appropriate reference group, and not because the cell mix changed. Is that enough to say the person is aging more slowly? It is not, and the reason is the central idea of this chapter.

A younger snapshot can arise in at least three ways. The amount of accumulated damage can be lower right now: a change of **state**. The speed at which damage builds up, or is cleared, can have changed: a change of **rate**. Or the point at which damage becomes dangerous can have moved: a change of **reserve**. These three can produce the same reading at one time point, readings that move in opposite directions from the outcome, or a reading that improves only briefly.

The clearest way to see this is in a model where we know the truth because we wrote it. The project built a deliberately simple synthetic model of damage accumulating and being cleared, based on a published model of aging, with illustrative values chosen to give human-like survival curves; it is not fitted to any real population and does not evaluate any real treatment; in it, two interventions were tuned so that the average damage of survivors at age 70 was identical, yet at 90 the group whose damage production had been reduced had more survivors (about 61 in 100 against about 57 in 100) and a longer life expectancy (about 91.7 against 89.8 years) than the group whose clearance had been boosted; raising the danger threshold instead made the reading look about one and a half years older at 70 while life expectancy rose by about one and a half years, because more people survived with higher damage; and a one-time clearing pulse made the reading about four years younger at 61, but by 70 the reading was back to about where it would have been, with less than half a year gained in life expectancy.[^6]

A model like this proves only that such cases are possible, not that they are common or that they describe any real treatment. But possibility is enough for the point at hand. If one reading at one time cannot, even in principle, distinguish a change of state from a change of rate or reserve, then the sentence "this intervention made you younger" needs more than one reading at one time. In the model, measuring how quickly the system bounces back after a disturbance, at two or more points, is what separates the cases. That is the subject of chapters 7 to 9.

## 7 | What a single reading can carry

A level can carry a great deal. It can say where a sample stands, on a given assay, compared with a named group of people. A good level, measured reliably, can predict risk, sometimes strongly. That is not a small thing, and nothing in this chapter takes it away.

What a single level cannot carry is an answer to the question most people actually ask of it: "Am I aging more slowly than before?" That is a question about a rate, and it needs at least two readings, taken in the same way, far enough apart to rise above the noise. Even then, as the synthetic model shows, a better number at one time can come from different underlying changes with different futures.

So, before acting on a single reading, it helps to run five checks. They serve the book's five questions (chapter 1) for the case of a single reading. How much does this test move when the same sample is measured twice? Compared with whom? How much of this reading could be the mix of cells in the sample? If there are several readings, do they come from one sample and one assay? And is the claim about where I stand, or about how fast I am changing? Back matter B2 collects questions like these for any longevity number. Whether a person's aging actually slowed is the subject of the next chapter.

---

- **Linked papers:**
  - PI layer ② (composition and weights) for section 4; PI layer ③ (readings and parameters) for section 6.
- **Scope:**
  - The reliability and composition results concern specific epigenetic clocks on blood samples; other clocks and tissues may differ.
  - The organ-age results come from UK Biobank volunteers.
  - The synthetic model is a teaching construction, not an estimate.
  - The chapter does not evaluate any commercial test.
- **Unresolved:**
  - external review (D05);
  - full-text reading of the cited studies, including the erratum to the sex-specific clocks paper;
  - a test–retest study of a consumer-marketed clock as sold, by a group with no stake in it (searched for, not yet found);
  - the hazard ratios for individual sex-specific organ clocks (not used here, ledger X149);
  - a bilingual derivation once the English is frozen (DEC-016).
- **Change impact:**
  - A correction or retraction affecting any cited study, or a change to the synthetic model, requires rechecking the bound claims (`tests/test_ch06_en_pilot.py`) and re-binding.

[^1]: [Ye et al., *Ageing Res Rev* 2023;90:102031](https://pubmed.ncbi.nlm.nih.gov/37567392/) (PMID 37567392), abstract read (ledger X150). The corresponding author declares membership of the Telomere Research Network steering committee.
[^2]: [Higgins-Chen et al., *Nat Aging* 2022;2:644–661](https://pubmed.ncbi.nlm.nih.gov/36277076/) (PMID 36277076), abstract and competing-interests statement read; [Borrus et al., *Aging Cell* 2026;25(10):e70756](https://pmc.ncbi.nlm.nih.gov/articles/PMC13650178/), introduction read (same laboratory family, ledger X126); [Sugden et al., *Patterns* 2020;1:100014](https://pubmed.ncbi.nlm.nih.gov/32885222/) (PMID 32885222), abstract read; a different group from the 2022 study (the Duke and King's College London group that later built DunedinPACE, chapter 7), no competing interests declared. Ledger X163.
[^3]: [Song et al. (MULTI Consortium), *Nat Med* 2026;32(11):4268–4279](https://pubmed.ncbi.nlm.nih.gov/42749890/) (PMID 42749890), abstract read; erratum 32(11):4350 not read (ledger X149).
[^4]: [Jonkman et al., *Genome Med* 2026;18:142](https://pmc.ncbi.nlm.nih.gov/articles/PMC13632308/) (PMID 42823742), abstract and the Results passages behind the ranges read (ledger X162; this traces the KERNEL §3.2 anchor).
[^5]: [Oh et al., *Nat Med* 2025;31:2703–2711](https://pubmed.ncbi.nlm.nih.gov/40634782/) (PMID 40634782), abstract read. The 43,616-person ten-organ study is a different paper ([*Nat Aging* 2025](https://www.nature.com/articles/s43587-025-01016-8)); ledger X81.
[^6]: [Synthetic saturating-removal model](../../../knowledge_base/experiments/SR_SNAPSHOT_IDENTIFIABILITY_2026-11-27.md) (in Chinese; script and tests alongside), ledger X93; robustness under published human parameters, X94. Synthetic teaching model only.
