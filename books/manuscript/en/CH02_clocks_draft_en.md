# Chapter 2 | Which Clock Are We Talking About?

> **Draft v0.1 (English), 2026-11-28.** Working title in [OUTLINE_v1](../OUTLINE_v1.md): "Age Is Not the Only Clock". Written in English first (DEC-016). It follows its entry in [DETAILED_OUTLINE_VOL1](DETAILED_OUTLINE_VOL1.md). Source material: V6 §04 and V7 §21 in `corpus/`. This is new writing that uses those sections as leads, not a translation. The reader-facing title is a candidate until the author confirms it.
>
> **Status:**
> - For author and domain review only; not a frozen text.
> - Self-checked by the same assistant that wrote it. Independent human review was waived by the owner on 2026-11-28 (DEC-020). The [claim audit agent](../../../review/CLAIM_AUDIT_AGENT_RECEIPT.json) runs mechanical checks in its place; it does not certify that any claim is scientifically correct.
> - Eight claim units are bound to verbatim source excerpts, to project records, or to the project's own synthetic calculation ([chapter 2 pilot](../../../knowledge_base/pilots/ch02_clocks_en/README.md)). Sources were read at abstract depth. Any edit to this file or to an excerpt makes the affected claims stale until they are re-bound.
> - This chapter explains what population statistics measure. It does not forecast anyone's lifespan and gives no personal medical advice.

## 1 | Three numbers on one page

Picture a single page of a newspaper. One article says that life expectancy in a country has reached a new high. A second says that healthy life expectancy there is about ten years lower. An advertisement in the corner of the page offers a test that will tell you your "biological age". All three are numbers of years. They sound like readings from the same clock, and they are not.

The first is a property of a population in a period. The second is the same property after each year has been weighted by an estimate of health. The third claims to be a property of one person. This chapter is about the first two, and about the question people most often ask of them: is there a limit? Biological-age readings belong to chapter 6; this chapter returns to them only at the end, to say why they are a different kind of clock.

Start with calendar age and life expectancy. A period life table takes the death rates observed at each age in one year and asks what would happen to an imaginary group of newborns who met exactly those rates all their lives. The answer, the average length of their imaginary lives, is the period life expectancy that appears in news reports. No real person lives that life. Someone born this year will meet next year's rates at age one, and rates decades from now in old age.

A small synthetic calculation, built by this project with no real data, shows the size of the difference. Give a population death rates that rise steeply with age, in the pattern called Gompertz, and let every death rate fall by 1 percent each calendar year. Life expectancy computed from the rates of year 0 alone is 73.4 years. People actually born in year 0 meet lower rates as they age, and their average lifetime is 80.8 years, 7.4 years longer. Neither number is an appointment. In the year-0 table, 43 percent of people die before reaching the average, a quarter have died by 66.4, and a quarter are still alive at 82.9.

So a period life expectancy is a compact description of one year's risks. It is useful for comparing places and years. It is not a forecast for anyone born in that year, and it says very little about when any one person will die. The cohort figure, the average for people actually born in a year, can be known only after nearly all of them have died, or estimated by assuming how death rates will change. How life tables are built is set out in B3; this chapter needs only the distinction.

## 2 | Health-adjusted time and its weights

Health-adjusted life expectancy goes one step further. It takes the years in the life table and counts each one as less than a full year when, on average, people at that age live with illness or disability. A year at full health counts as one; a year with a health loss counts as less. The result is never longer than life expectancy, and the difference is the gap discussed in section 3.

Everything then depends on how much less. A year with mild back pain and a year unable to walk cannot be counted the same, so someone has to put a number on each health state. That number is a weight, and it is a judgement, not a reading of a body.

Where do the weights come from? The Global Burden of Disease study uses disability-adjusted life-years, which need a set of disability weights to put a health level on non-fatal outcomes. For its 2013 round, web-based surveys of participants aged 18 to 65 in Hungary, Italy, the Netherlands and Sweden were combined with earlier survey data. Respondents considered two hypothetical people in different health states and said which one they thought was healthier. The answers were rescaled to run from 0, no loss of health, to 1, a loss equivalent to death. When the descriptions of some states were revised, their weights moved a great deal: complete hearing loss went from 0.033 to 0.215, and a treated spinal cord lesion below the neck from 0.047 to 0.296. The authors conclude that the weights are sensitive to particular details in the descriptions of health states, but robust to how long the states last.[^1]

That is not a flaw to be fixed by a better survey. It is what a weight is. Someone who has never been deaf is asked to compare two descriptions on a screen, and the wording of a description changes the answer. Someone who has lived with a spinal cord injury for twenty years might weigh it differently again, and so might someone whose city has step-free transport. None of these judgements is the true one.

Here is the strongest case for healthy life expectancy as the single target, and much of it is right. It refuses to count survival alone. It rewards both preventing death and preventing illness. It can be compared across countries and decades, and it puts conditions that rarely kill, such as hearing loss or depression, onto the same scale as those that do. A health system that pursued life expectancy alone could ignore millions of people living with treatable disability; this measure makes that harder.

But a single target has to fix its weights, and the weights carry choices the number does not show: whose judgement counts, which descriptions they were given, and whether the burden of a condition belongs to the body or to the surroundings that make it disabling. A weight of 0.3 is also not a statement that a year in that state is worth 30 percent of a life. The weight measures health loss as respondents ranked it. What a life with that health is worth to the person living it is a separate account. This book keeps the two apart: the body's maintenance and the person's opportunities are two ledgers that are not added into one score. Chapter 30 owns that argument; here it is enough to see that healthy life expectancy belongs to the first ledger only.

Even where whole lives can be watched, health and length do not simply move together. In a 2024 study of 960 genetically diverse female mice, calorie restriction and intermittent fasting both extended lifespan, in proportion to the degree of restriction. But the health effects differed between the regimes and had inconsistent relationships with the extra life. The strictest regime, 40 percent calorie restriction, extended life the most and also led to a loss of lean mass and immune changes that could make infections more likely. Lower body fat and lower fasting glucose were not associated with longer life. The authors' own summary is that improving health and extending lifespan are not synonymous. Several authors were employees of Calico Life Sciences.[^2]

The study does not say how any of this applies to people. Its value here is narrower: in an experiment where every animal could be followed to death, no single health measure stood in for lifespan, and lifespan did not stand in for health.

## 3 | The gap, and why it is not a single-cause story

The difference between life expectancy and health-adjusted life expectancy is often called the healthspan–lifespan gap. A 2024 study used World Health Organization data for 183 member states over two decades. It reported that the gap had widened globally to 9.6 years and was wider for women than for men. It also reported that gaps were positively associated with the burden of noncommunicable diseases and total morbidity, and negatively with mortality.[^3]

That last association is easy to skip, and it matters most. A wider gap can come from more illness. It can also come from less death: when fewer people die of conditions that once killed them, more live long enough to spend years with chronic disease. Usually both happen at once. The study compared countries at the level of national statistics, so it describes which features go together, not which causes which. A widening gap is not, by itself, evidence that health care is failing; nor is it evidence that all is well.

Two further cautions come from this project's reading of the full paper and of WHO's method documents. First, the 9.6 years is a global figure; the paper also reports a mean across the 183 member states of 9.2 years. The two summarise different things, and neither should be passed off as the other (ledger X21). Second, WHO's health-adjusted estimates combine its life tables with estimates of years lived with disability that rest mainly on the Global Burden of Disease, and WHO states that its newer series cannot be compared directly with earlier releases. A trend built by splicing figures from different releases is not a trend. The paper's annual rate of change also divides the change between 2000 and 2019 by 20, although those years are 19 apart if both are annual end points; the project has recorded the point but cannot resolve it without the authors' data (ledger X61).[^4]

Chapter 1 made one more point that belongs here as well: a gap of 9.6 years is a population's equivalent lost years, not the number of years any one person will spend ill. Some people will spend far longer in poor health, and many far less.

## 4 | Is there a limit?

The question readers ask most often about lifespan is whether there is a maximum. It sounds like one question. It is at least three, depending on which statistic is meant: the highest age at death ever recorded, the risk of dying for people who have already reached extreme old age, or the median lifespan a model predicts under stated assumptions.

Two well-known papers seem to answer in opposite directions. In 2016 Dong, Milholland and Vijg analysed global demographic data and reported that improvements in survival with age tend to decline after age 100, and that the age at death of the world's oldest person had not increased since the 1990s; they concluded that the maximum lifespan of humans is fixed and subject to natural constraints. In 2018 Barbi and colleagues estimated death rates for all inhabitants of Italy aged 105 and older between 2009 and 2015, a total of 3,836 documented cases, and observed hazard curves that were essentially constant beyond age 105: a plateau, not an ever-steeper climb.[^5]

These are less contradictory than they look once each is matched to its statistic. The first is about records and about where improvements in survival are happening. The second is about the yearly risk of death among people already past 105. A plateau at a high level is compatible with records that rarely move: if a large share of people at that age die each year, very few will reach a new record, ceiling or no ceiling. Neither paper observed an age that no one can pass.

The same synthetic population from section 1 shows how much rides on an assumption about the tail. Up to age 105 nothing changes; at 105 the yearly probability of death in this made-up table is 0.66. Then compare two tails. If the hazard keeps rising, the chance that someone alive at 105 reaches 115 is about 1.6 in a hundred million. If the hazard stays flat from 105 onward, the chance is about 2.2 in a hundred thousand, some 1,400 times larger. For reaching 122, the two assumptions differ by a factor of about 710 billion. The table up to 105 is identical in both cases; only the assumption about the rarely observed tail differs, and it decides almost everything a headline would report.

A third kind of answer comes from models of mechanism. A 2026 paper in npj Aging built a model of population survival in which every cause of aging is removed except somatic mutations, which accumulate with age and can cause cell death. In the model, cells that no longer divide, such as neurons and heart muscle cells, are the bottlenecks: mutations alone bring median lifespan down from a theoretical non-aging baseline of 1759 years to 156. Combining organs gives median lifespans of 146 to 194 years. The authors read this as showing that somatic mutations matter but cannot alone account for observed mortality, which implies comparable contributions from other causes. The paper's title speaks of an upper bound; its numbers are medians under stated assumptions, not an age that no individual can exceed.[^6]

Chapter 8 meets a fourth kind of "limit": the age at which a fitted trend, projected beyond the data, reaches zero. That is a property of a model's extrapolation, not an observed age at death. The rule for all four is the same. Before asking whether a limit exists, ask which statistic the word "limit" is attached to, what data it rests on, and which part of it is assumption.

## 5 | Why none of these is the clock in a consumer report

Return to the newspaper page. Life expectancy and healthy life expectancy are summaries of populations over periods. They change when a population's death rates and illness rates change. They do not belong to any one person, and a person cannot have "a life expectancy of 81" in the way a person has a blood pressure.

The "biological age" in the advertisement is a different kind of object. It is a reading taken from one body, usually a blood or saliva sample, and converted into years by a model trained on other people. Whether that reading predicts anything for you, whether it responds to what you change, and whether a change in it is a benefit, are questions about a measurement, not about a population. Chapter 5 sets out the contract such a reading has to meet, and chapter 6 asks what a single reading can tell you.

Expressing all three in years makes them easy to place side by side and easy to confuse. Life expectancy is a summary of one period's death rates. Healthy life expectancy is that summary weighted by judgements about health. A biological-age reading is a model's translation of one sample. Asking "which clock?" before reading any of them is the first defence against treating one as another.

---

**What this chapter does not settle:**
- whether any intervention changes these statistics for real populations (chapter 20);
- what a single biological-age reading can tell a person (chapters 5 and 6);
- how life tables are constructed in detail (B3);
- what a year of life with a given state of health is worth to the person living it (chapter 30).

**Unresolved:**
- all five studies were read at abstract depth only;
- the healthspan paper's aggregation method (X21) and the denominator of its annual rate (X61) remain open;
- the V7 corpus reports further tail figures for the somatic-mutation model and a preprint range that differs from the published one; neither has been checked against the paper, and neither is used here;
- the mouse study's tables, and how the weight surveys' respondents were recruited, have not been read;
- independent review by a demographer, a health economist and a disability-studies reader has not taken place.

[^1]: [Salomon et al., *Lancet Glob Health* 2015;3(11):e712–23](https://pubmed.ncbi.nlm.nih.gov/26475018/) (PMID 26475018), abstract read. Funded, according to the abstract, by the European Centre for Disease Prevention and Control and the Bill and Melinda Gates Foundation.
[^2]: [Di Francesco et al., *Nature* 2024;634:684–692](https://pubmed.ncbi.nlm.nih.gov/39385029/) (PMID 39385029), abstract and competing-interests statement read.
[^3]: [Garmany and Terzic, *JAMA Netw Open* 2024;7(12):e2450241](https://pubmed.ncbi.nlm.nih.gov/39661386/) (PMID 39661386), abstract read; no conflicts reported.
[^4]: Ledger X21 and X61; [HALE methods audit](../../../knowledge_base/HALE_METHODS_VERSIONS_AND_TIME_AUDIT_2026-11-27.md) §1, written by the same assistant from the paper's methods and results and WHO's method documents. Not an independent check.
[^5]: [Dong, Milholland and Vijg, *Nature* 2016;538:257–259](https://pubmed.ncbi.nlm.nih.gov/27706136/) (PMID 27706136); [Barbi et al., *Science* 2018;360:1459–1461](https://pubmed.ncbi.nlm.nih.gov/29954979/) (PMID 29954979). Abstracts read. Both papers drew published comments that have not been read here.
[^6]: [Efimov et al., *NPJ Aging* 2026;12:116](https://pubmed.ncbi.nlm.nih.gov/42350444/) (PMID 42350444), abstract read; no competing interests declared.
