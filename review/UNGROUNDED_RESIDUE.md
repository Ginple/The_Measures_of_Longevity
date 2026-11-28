# Ungrounded Residue

*List only (CGEE R5.5 §3 item 5; §6 release conditions). Started 2026-11-28.*

**What this file is.** It lists load-bearing statements and states that the repository relies on but has not grounded with a replayable check, an external record or a human review.

**Rules:**

- Nothing here was deleted from or rewritten in the text because it is listed.
- The owner decides each item: add evidence, downgrade the label, or authorize removal. Each decision goes into the [claim ledger](../knowledge_base/CLAIM_LEDGER.md).
- IDs use the `UR-` prefix so they do not collide with the `U` numbers in RESEARCH_FRONTIERS.

## A. Statements used in planning that have no grounded source

| ID | Statement | Where used | Why ungrounded | Load-bearing for |
|---|---|---|---|---|
| UR-01 | US trade nonfiction typically runs 80–120k words | `books/market/MARKET_POSITIONING_2026-11.md` §3.1; X147 (superseded) | Rule of thumb, graded B/C; no agent or editor confirmation | Only historical now. DEC-017 made length content-driven |
| UR-02 | About 200k words ≈ 21–22 audiobook hours | L1 receipt F-14 | Assumes 150–155 words per minute. The arithmetic is V1-checked (agent A22); the rate is not sourced | Audio format planning (human narration is a priority) |
| UR-03 | Lifespan-limit debate and record probabilities | `DETAILED_OUTLINE_VOL1.md`, chapter 2 | KERNEL §3.3 anchor; no ledger entry yet | Chapter 2 evidence |
| UR-04 | Composition share of DNAmAge variance (4,058 samples) | `DETAILED_OUTLINE_VOL1.md`, chapter 6 | KERNEL §3.1 anchor; no ledger entry yet | Chapter 6 evidence |
| UR-05 | Reading routes R1–R4 | `DETAILED_OUTLINE_VOL1.md`, F1 | Desk walk-through (RT-C, V4 role-play) plus agent D01 consistency. No reader evidence | F1 design; DEC-018 |
| UR-06 | R1 readers stay with the book through Volume Ⅱ | DEC-018 reopen trigger; MR-2 | No reader test | Whether K3 is reopened |

## B. Process states that are not verified

| ID | State | Current status | What would ground it |
|---|---|---|---|
| UR-07 | Independent review of the architecture | L1 self-audit (V5), plus the V1 audit agent of 2026-11-28. Clean-session blind review prepared but not run | Run [the prepared prompt](blind/BLIND_REVIEW_PROMPT_2026-11-28.md) (V4); then human review (D05) |
| UR-08 | Tools as gates | 0 tools `verified` ([register](../docs/TOOL_STATUS.tsv)) | Known-answer validation by someone other than the authoring assistant |
| UR-09 | Funding and conflict-of-interest ledger | **Missing.** The interests of Ginple Life Science Inc. in any test, product or service the book discusses are not recorded | The owner states interests once. Then they are copied identically into the book, every paper, and each place the product is discussed (playbook §11) |
| UR-10 | AI-use disclosure acceptable to target venues | Draft only ([§4.2](../docs/VERIFICATION_AND_DISCLOSURE.md)); no editor asked | Ask each venue before submission |
| UR-11 | Reporting guideline for each paper chosen at P0 | Not confirmed in the paper protocols (playbook §11) | Name the study type and guideline in each `PROTOCOL.md` revision. Do not edit the frozen P1–P3 protocols |
| UR-12 | Actions are attributable to the assistant | Pushes and comments use the owner's GitHub account | A separate Write-only agent account (playbook §7E) |
| UR-13 | Paragraph-level repetition and per-chapter unique-claim ratio | Not built; sentence-level check only | Playbook §7G item 6 |
