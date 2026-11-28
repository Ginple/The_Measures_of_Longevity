# Claim audit agent: first run and decision DEC-020 (2026-11-28)

## Why it exists

On 2026-11-28 the owner wrote: "（D05）如果你已经编排了一个独立审计AGENT了，就不再需要 独立评审（D05）". In English: if an independent audit agent is already in place, the independent review D05 is no longer needed.

The agent that existed then, [`tools/restructure_audit_agent.py`](../tools/restructure_audit_agent.py) (DEC-019), checks only the structure of the book plan (26 properties). It never looked at the chapters' bound claims. So before recording the waiver, the assistant built a second agent, [`tools/claim_audit_agent.py`](../tools/claim_audit_agent.py), aimed at the claims themselves.

## What it checks (V1, deterministic)

These seven checks run on staged copies of every English chapter pilot (chapters 1–10, including the English chapter 5):

| ID | Property |
|---|---|
| C01 | `inspect_project`: schema valid, no integrity issue, no artifact drift, no stale claim |
| C02 | Every number and capitalised word in a claim that its evidence lacks has a reviewed reason; no reviewed token is stale (chapter 5 English is outside the token scan) |
| C03 | Every PubMed ID cited in the chapter appears in one of the pilot's bound artifacts |
| C04 | If bound evidence says a result is from mice or rats, from a model, post hoc, exploratory, from a preprint, or not significant, the claim carries the same qualifier |
| C05 | No wording the manuscript has ruled out (glossary §6, KERNEL §6) appears in the body text |
| C06 | Every claim is supported (a normative proposal may stay "unknown"), has a rationale and evidence, and no whole ledger or audit file is bound in place of an excerpt |
| C07 | The draft header states reading depth, that the text was self-checked, and that it is not frozen |

`--self-test` plants 9 errors, and each one must make its target check fail. All 9 are detected.

## First run: 63 of 69 passed

The first run found six failures. Four were real problems, now fixed; two came from rules that were too blunt and have been narrowed.

| Finding | Kind | Action |
|---|---|---|
| C04, chapter 1, claims C003 and C004: the CALERIE methylation analysis is post hoc in its abstract, but the chapter said only "a later analysis" | real (missing caveat) | Added "post hoc" to both sentences; re-bound |
| C06, chapter 2: the whole HALE methods audit file was bound, so any edit to the audit would make claims stale | real (binding practice) | Bound a verbatim excerpt of §1 instead (`evidence/HALE_AUDIT_excerpt.txt`) |
| C07, English chapter 5: the header did not state reading depth | real (disclosure) | Header now states abstracts or short excerpts |
| C06, English chapter 5, claim C005: state "unknown" | rule too blunt | It is a normative proposal, which no source can support. The rule now allows "unknown" for normative proposals |
| C05, chapters 5 and 6: "years younger" | rule too blunt | Both chapters report what a clock says, which KERNEL §6 allows. The rule now targets "years younger" only as an outcome of an intervention |
| C05, chapter 6: "made the reading about four years younger" (synthetic model) | rule too blunt (second pass) | It is a reading in a synthetic model. The rule now excludes "the reading/estimate/clock" |

After the fixes, 69 of 69 checks pass. The receipt is in [`CLAIM_AUDIT_AGENT_RECEIPT.json`](CLAIM_AUDIT_AGENT_RECEIPT.json).

## What the agent cannot do

- It cannot see paraphrase that changes meaning, a caveat for which it has no keyword, a source that is itself wrong, or a better source that was not used.
- It does not judge whether an interpretation is fair.
- It was written by the same assistant that drafted the chapters, so the choice of checks is self-assessment (V5).
- A clean run means only that the encoded properties hold.

## Decision recorded (DEC-020)

- The owner waives independent human review (D05) as a prerequisite. The two audit agents stand in its place.
- In every pilot, the debt `*-INDEPENDENT-REVIEW` is closed. Its closure evidence is this waiver plus the agent receipt. **No review record was created**: `reviews` stays empty.
- `inspect_project` still reports formal release as `blocked`. The reasons are the open depth debts, the claim inventories not declared complete, and the missing review records. This is intended: the waiver removes a requirement and does not create evidence.
- The draft headers now say that review was waived and that the agent's checks are mechanical.
- The owner can reverse this decision at any time. Reversing it means reopening the debts and restoring the header sentence.
