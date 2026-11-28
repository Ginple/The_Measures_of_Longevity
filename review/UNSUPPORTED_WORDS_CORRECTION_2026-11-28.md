# Unsupported words in English chapters 6, 7 and 9: correction record (2026-11-28)

> **Status.** Self-found by the drafting assistant while closing a loose end from chapter 9. Not a human or independent review (D05 open). The corrections remove words; no claim gains strength.

## 1. What happened

While checking whether "overnight" in chapter 9's kidney paragraph appeared in the stored Fliser abstract, it turned out that it did not, and neither did "German". The pilot rationale for that claim nevertheless said "All match". A scan of all bound claims in chapters 6–9 found more cases of the same kind:

| Chapter | Claim | v0.1 wording | Stored source says | Fix |
|---|---|---|---|---|
| 6 | CH6-EN-C008 | "across the 4,058 people" | "an analysis of 4,058 samples" (number not bound to this claim) | "4,058 samples"; E-COMP-4058 bound |
| 7 | CH7-EN-C001 | "a birth cohort in New Zealand" | "the Dunedin Study birth cohort" | country removed |
| 7 | unbound, ¶ 49 | "New Zealanders born in 1972–73" | "Dunedin Study 1972-1973 birth cohort" | "one birth cohort, born in 1972–73" |
| 9 | CH9-EN-C001 | "Bernard Strehler and Albert Mildvan published a general theory of mortality and aging" | surnames, year and journal only (secondary source; header) | "Strehler and Mildvan published a theory of mortality in *Science*" |
| 9 | CH9-EN-C002 | "a small German study … an overnight amino acid infusion" | neither word | both removed |
| 9 | CH9-EN-C004 | "A Canadian group" | no affiliation in the excerpt | "One research group" |
| 9 | CH9-EN-C005 | "a Canadian exercise physiologist" | no affiliation or profession | "A brief review" |
| 9 | CH9-EN-C006 | "The Canadian study"; 298 not bound to this claim | — | "The study of 298 people"; E-PAT-N bound |

All of these words are very probably true of the real papers (the affiliations are on the papers). That is not the standard. The standard in this project is that a word in a bound claim is in the stored excerpt, so that a reader can check it without trusting the writer. Each affected rationale now carries a "Corrected 2026-11-28" note, and the three chapters are v0.1.1.

## 2. Why the checks missed it

The span check confirms that a claim's anchor is in the chapter and that each evidence excerpt is in its file at the stated lines. It does not compare the words of the claim with the words of the evidence. "All match" in a rationale was the writer's own judgement, and in these cases it was wrong.

## 3. What now catches it

[`tools/claim_token_scan.py`](../tools/claim_token_scan.py) lists every number and capitalised word in a bound claim that its bound evidence does not contain. It compares the list with a per-claim reviewed allowlist, where each entry has a reason code: year, chapter cross-reference, sentence-initial word, arithmetic on bound numbers, evidence-file header, synthetic-model value written differently, or number spelled out. [`tests/test_claim_token_scan.py`](../tests/test_claim_token_scan.py) fails on any unreviewed token and on any allowlist entry that no longer applies. Affiliations kept in chapter 7 (Stanford, Singapore, Yale), chapter 8 (Johns Hopkins, Irish) and chapter 9 (Canadian, for the interRAI cohort, whose title says so) are recorded in the evidence-file headers at fetch time. They are marked H, which is weaker than a quote.

A wider one-off pass over all body text of chapters 6–9, bound or not, found no other unsupported proper noun. Every number with no match in the stored evidence was illustrative, arithmetic or chapter-internal.

## 4. Limits

- The scan sees numbers and capitalised words only. A paraphrase that adds meaning in lowercase words ("overnight" was one) is invisible to it unless the word is capitalised. Those can still only be caught by reading.
- The allowlist reasons are the same assistant's judgement.
- Chapter 5 (Chinese v0.3 and English v0.1) uses a different pilot and was not scanned.
