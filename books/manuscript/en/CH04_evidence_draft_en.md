# Chapter 4 | Counting the People Behind a Number

> **Draft v0.1 (English), 2026-11-28.** Working title in [OUTLINE_v1](../OUTLINE_v1.md): "What Counts as Evidence: Denominators, Source Families, and Replication". Written in English first (DEC-016). It follows its entry in [DETAILED_OUTLINE_VOL1](DETAILED_OUTLINE_VOL1.md). Source material: V7 §01 in `corpus/`, plus the project's own audits. This is new writing that uses them as leads, not a translation. The reader-facing title is a candidate until the author confirms it.
>
> **Status:**
> - For author and domain review only; not a frozen text.
> - Self-checked by the same assistant that wrote it. Independent human review was waived by the owner on 2026-11-28 (DEC-020). The [claim audit agent](../../../review/CLAIM_AUDIT_AGENT_RECEIPT.json) runs mechanical checks in its place; it does not certify that any claim is scientifically correct.
> - Twelve claim units are bound to verbatim source excerpts, to project records, or to the project's own synthetic calculation ([chapter 4 pilot](../../../knowledge_base/pilots/ch04_evidence_en/README.md)). Sources were read at abstract depth; the counts by time point for CALERIE and BASE-II come from project audits of the full texts. Any edit to this file or to an excerpt makes the affected claims stale until they are re-bound.
> - This chapter teaches reading habits. It does not settle any real conflict between studies (chapter 31) and gives no medical advice.

## 1 | Every percentage has a denominator: find it

Readers often ask how to tell a strong study from a press release, or whether "clinically proven" means proven in people like them. Most of the answer is not statistics. It is counting: who was counted, out of whom, when, and by whom.

Start with the bottom of the fraction. A percentage is a count divided by another count, and the second count is where most misreadings hide. "Ten percent overdiagnosed" means something very different if the ten percent is of everyone screened, of everyone who tested positive, or of the cancers found.

A modelling study of multicancer blood tests shows how much the choice matters. Its authors used a microsimulation model, not a trial, to estimate what would happen if people aged 50 to 75 in Canada were screened. They estimated that 2.1 to 6.0 percent of yearly screen-detected cancers would be overdiagnoses, rising with age from 1 percent at 50 to over 10 percent of screen-detected cancers by 75. The denominator is cancers found by screening, not people screened, so these figures cannot be read as one person in ten being harmed. The same model gives the test a positive predictive value of 15.9 to 77.6 percent: for every true cancer it detects, there could be 0.3 to 5.3 false positives with no cancer.[^1]

None of these numbers is wrong. Each answers a different question, and a reader who moves a number from one denominator to another without noticing will misread it, in either direction. Chapter 5 returns to this model, and to the trial in section 4, to ask what a screening test has to show before it is useful.

A common objection deserves an answer here: insisting on denominators is pedantry, because the direction of an effect is usually clear. Sometimes it is. But the denominator can reverse the direction itself.

A synthetic example, built by this project with no real data, shows how. Two treatments are each given to 800 patients. Among mild patients, the new treatment helps 180 of 200, 90.0 percent, and the old one 520 of 600, 86.7 percent. Among severe patients, the new treatment helps 300 of 600, 50.0 percent, and the old one 80 of 200, 40.0 percent. The new treatment does better in both groups. Pool the groups and it does worse: 480 of 800, 60.0 percent, against 600 of 800, 75.0 percent. Nothing is miscounted. The new treatment was simply given mostly to severe patients, so its overall denominator is full of people who were less likely to recover anyway.

This is not only a textbook trap. A 1975 study of graduate admissions at the University of California, Berkeley, found that the aggregate data for fall 1973 showed "a clear but misleading pattern" of bias against women. Department by department, few units departed significantly from the expected admissions of women, and about as many appeared to favour women as men. Once the data were pooled in a way that took account of each department deciding for itself, and of women tending to apply to departments that were harder for anyone to enter, there was a small but statistically significant bias in favour of women.[^2] The direction of the pooled number came from where people applied, not from how they were treated.

So the first habit is to ask, of every percentage: out of whom? And then: would splitting those people into the groups that matter change the answer?

## 2 | Who was counted, and when

A randomised trial makes one promise: at the moment of randomisation, the groups differ only by chance. Every later subset can break that promise, because the people who stay, give a sample, or come back for a visit may differ between the groups in ways that chance did not decide.

The CALERIE trial of calorie restriction is a careful study, and it shows how many denominators one trial can hold. In it, 220 adults without obesity were randomised to 25 percent calorie restriction or to their usual diet for two years. A later analysis of DNA methylation in their blood, described by its authors as post hoc, did not analyse 220 people at each step. The project's audit of the published paper lists 128 people in the restriction group and 69 in the control group with a baseline and at least one follow-up sample; 117 and 68 for the change to 24 months; and 105 and 59 with data at all three time points. The audit also found that the counts given in different parts of the paper cannot all describe the same people under simple assumptions, and it does not decide which number is wrong; the authors' clarification has not been obtained.[^3]

None of this makes the analysis invalid. It means that "a randomised trial found" applies, strictly, to comparisons that keep the randomised groups, and every narrower analysis has to show that the people it lost were lost in the same way in both groups.

Observational cohorts have their own version. The Berlin Aging Study II compared 14 candidate biomarkers of aging as predictors of death, and its abstract reports 1,083 people aged 60 to 80 at baseline, followed for an average of 7.4 years. It concluded that DunedinPACE, a methylation measure of the pace of aging, had the strongest and most consistent association with mortality. The project's audit of the full text records that the study began with 1,671 participants aged 60 and over; the 1,083 are those who also took part in a later wave of measurements, and the methylation measures were available only for people who took part in that later wave.[^4] A prediction made among people who returned describes people who returned. That can still be useful, but it is a different denominator from everyone who enrolled.

Time matters inside randomised comparisons too. In an exploratory substudy of the LoDoCo2 trial of colchicine in coronary disease, researchers followed the growth of clonal haematopoiesis, an aging-related condition in which clones of blood cells carrying driver mutations expand. In total, 854 participants contributed 2,047 observations across four time points, including before and after a run-in period in which everyone took colchicine before randomisation. In the placebo group, clone size grew by 14.9 percent a year; in the colchicine group, a nonsignificant 6.3 percent. It is tempting to conclude that colchicine stopped the growth. But the difference between the two groups was not statistically significant (P for interaction 0.13). One group changing significantly and the other not is two separate tests, not a comparison of the groups. Among people with mutations in one gene, TET2, the difference between groups did reach P=0.04, in an exploratory analysis. The authors themselves wrote that further validation in prospective studies is warranted.[^5]

The second habit, then, is to ask: is this comparison between the groups that were randomised, or between subsets chosen later? And did "significant in one group" quietly become "different between groups"?

## 3 | Source families: why two papers are not always two replications

Two papers that agree look like twice the evidence. They are only if they could have disagreed independently.

In 2026 one laboratory group published two related studies of epigenetic clocks. The first assembled TranslAGE, a harmonised database of 51 public and private longitudinal intervention studies, and calculated 16 prominent clocks for each. It found that clocks trained to predict mortality or pace of aging show the strongest responses across all interventions, and agree with one another. The second, from the same group, proposed three criteria for trusting a clock result, one of which is that mortality-trained or pace-of-aging clocks respond. Six authors appear on both papers.[^6]

The two papers are consistent, and each may well be right. But their agreement is not an independent replication. They share people and methods, and the second builds on the kind of result the first reports. The project's ledger records exactly this: the second paper's findings are cited as a source of evidence about clocks, not as independent confirmation of the first (X126).[^3] Chapter 3 met the same pattern with two theoretical papers that share an author.

The habit is to group sources into families before counting them. A family can be a laboratory, a cohort used by many groups, a company and the academics it funds, or a single dataset reanalysed many times. Ten papers from one family are closer to one well-documented result than to ten.

## 4 | Company-reported numbers

Companies fund much of the research in this field, and their involvement is not a reason to dismiss a result. It is a reason to know which number to read first.

The NHS-Galleri trial of a multicancer blood test was funded by Grail, and some of its authors work for Grail Bio UK. It randomised 71,122 people to have their blood tested and 71,128 to have it stored. The primary end point was the rate of stage III or IV cancer among 12 prespecified types. It did not differ significantly between the groups (incidence rate ratio 1.03, 95 percent confidence interval 0.92 to 1.14). A key secondary end point, stage IV cancer alone, had a ratio of 0.86 (0.74 to 1.00). The authors called for further follow-up of both.[^1]

That is a company-funded trial reporting a null primary result in plain terms, which is to its credit. It also shows the reader's task. The primary end point is the answer the trial was designed to give. A secondary end point whose interval reaches 1.00 is worth following up, not worth headlining, and a reader who sees only the secondary figure in a press release has been given a different study.

Financial interests also run through academic work. Two authors of the CALERIE methylation analysis are listed as inventors on DunedinPACE, which was licensed to a commercial entity. Two authors of the BASE-II comparison own stock in a company called Vitas, one as a cofounder and one as its chief executive. Two authors of the TranslAGE paper are named co-inventors of a patented clock, and three are employees of TruDiagnostic who developed a biomarker called OMICmAge.[^7] Each of these interests was declared, as it should be. None shows that a result is wrong. Together they show why declared interests belong next to the number, so that a reader can ask whether the measure that came out best is one that someone sells.

Some checks need no access to the data. Percentages that have been rounded carry a trace of their denominator. In a second synthetic example, three counts are reported as 7 (3.7 percent), 12 (6.3 percent) and 19 (9.9 percent). Of every denominator from 100 to 400, only 191 is consistent with all three. The project ran this check on a real supplementary table from a 2026 CALERIE report: its 10 pairs of counts and rounded percentages were compatible, within that range, only with a denominator of 191, while the main text describes 190 people. Another report from the same trial has exactly 191. The check does not prove which denominator the table used, and the ledger records it as a question to ask the authors, not a correction (X106).[^3]

## 5 | Replication, and what counts as "the same result"

A result is replicated when someone else, with other data, asks the same question and gets an answer that agrees. Each part of that sentence can fail quietly.

"The same question" means the same population, intervention, comparison, outcome and time. A trial in coronary disease does not replicate a trial in healthy adults; a 12-week change in a marker does not replicate a five-year change in survival.

"An answer that agrees" means more than a P value below 0.05 in both studies. It means effects in the same direction, of compatible size, with intervals that overlap in a meaningful way. Two studies can each be "significant" with effects that differ tenfold, or each be "not significant" with estimates that agree closely.

"Someone else, with other data" is where source families matter, and also where many readouts matter. In the second clock paper, the authors took intervention studies that had reported a positive result with a single clock and recalculated the effect with other clocks. No additional clocks reached statistical significance. They suggested that some single-clock findings may need to be re-examined.[^6]

A third synthetic calculation shows why one positive readout among many is weak evidence. If an intervention has no effect at all, and 16 independent readouts are each tested at the 5 percent level, the chance that at least one comes out "significant" is 0.56. Real clocks are correlated, so the true chance is lower, but the lesson holds: the more readouts a study reports, the less one positive among them should move a reader.

The fifth habit, then, is to ask of any "replication": same question? Same direction and size? Different people, different data, different hands?

These five habits do not decide between conflicting studies; chapter 31 takes that up. They do something earlier: they tell a reader how many people stand behind a number, which people, and how many independent groups have looked. Chapter 5 turns from studies to measurements, and asks what a reading has to show before it can be used for prediction, for tracking change, for mechanism or as a stand-in for an outcome.

---

**What this chapter does not settle:**
- how to weigh studies that conflict (chapter 31);
- when a claim should be withdrawn (chapter 33);
- whether colchicine, multicancer screening or calorie restriction helps anyone; they appear here only as examples of counting;
- formal denominator audits, which belong in B3 or a companion paper (conditional, DEC-012).

**Unresolved:**
- all eight studies were read at abstract depth; the CALERIE and BASE-II counts by time point come from the project's own audits of the full texts, not re-read for this chapter;
- the CALERIE count inconsistency (X31) and the 191 denominator (X106) are open questions for the authors, not findings;
- the Berkeley study is not about health; it is used because its abstract states a reversal plainly;
- independent review by a statistician and a trialist has not taken place.

[^1]: [Malagón et al., *Cancer Med* 2026;15(11):e72455](https://pubmed.ncbi.nlm.nih.gov/42989814/) (PMID 42989814), a microsimulation model; [Sasieni et al., *N Engl J Med* 2026;395:1374–1386](https://pubmed.ncbi.nlm.nih.gov/42776074/) (PMID 42776074), NHS-Galleri, funded by Grail. Abstracts read.
[^2]: [Bickel, Hammel and O'Connell, *Science* 1975;187:398–404](https://pubmed.ncbi.nlm.nih.gov/17835295/) (PMID 17835295), abstract read.
[^3]: Project records: ledger rows X31, X40, X106 and X126, and audits of the CALERIE and BASE-II papers ([CALERIE](../../../knowledge_base/CALERIE_TEMPORAL_AUDIT_2026-11-27.md), [BASE-II](../../../knowledge_base/SCREENING_PREDICTION_DURABILITY_AUDIT_2026-11-27.md)). These are earlier readings by the same assistant, not independent sources. The randomised count is from [Waziry et al., *Nat Aging* 2023;3:248–257](https://pubmed.ncbi.nlm.nih.gov/37118425/) (PMID 37118425).
[^4]: [Vetter et al., *Biomark Res* 2026;14:37](https://pubmed.ncbi.nlm.nih.gov/41792861/) (PMID 41792861), abstract read; full-text counts from the project audit (note 3).
[^5]: [Mohammadnia et al., *J Am Coll Cardiol* 2025;86:1983–1996](https://pubmed.ncbi.nlm.nih.gov/40892620/) (PMID 40892620), abstract read.
[^6]: [Sehgal et al., *Nat Med* 2026;32:3477–3490](https://pubmed.ncbi.nlm.nih.gov/42629466/) (PMID 42629466); [Borrus et al., *Aging Cell* 2026;25(10):e70756](https://pubmed.ncbi.nlm.nih.gov/42850743/) (PMID 42850743). Abstracts read.
[^7]: Competing-interests statements in the PubMed records for notes 3, 4 and 6.
