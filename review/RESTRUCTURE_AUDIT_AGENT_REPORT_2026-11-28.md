# Restructure Audit Agent — Report and Dispositions (2026-11-28)

**Object audited:** the post-positioning restructure decision DEC-018 and what it produced: the frozen [L2 packet](MARKET_RESTRUCTURE_AUDIT_PACKET_L2_2026-11-27.md), the [protocol](MARKET_RESTRUCTURE_AUDIT_PROTOCOL_2026-11-27.md), the chapter map, the detailed-outline layer, KERNEL v0.9.11, writing rules 7–10 and the ledger and decision rows.

**Why this exists.** On 2026-11-28 the author declined an L2 (external) audit and asked for an independent audit agent instead, unless one had already run. None had: the 2026-11-27 audit was an L1 self-audit by the assistant that wrote the plan.

**Verification level (playbook R3.8 §3.3).**

| Part | Level | Can it close a gate? |
|---|---|---|
| Deterministic agent [`tools/restructure_audit_agent.py`](../tools/restructure_audit_agent.py) | **V1** for the 26 encoded properties | Its receipt supports closing those properties only; the owner closes |
| Choosing which properties to encode, and the dispositions below | **V5** (same assistant that wrote the plan) | Never |
| Clean-session blind review (§10) | **Not run.** No isolated model is reachable from this sandbox (models.github.ai returned no response on 2026-11-28). The prompt is ready in [`blind/BLIND_REVIEW_PROMPT_2026-11-28.md`](blind/BLIND_REVIEW_PROMPT_2026-11-28.md) | Would be V4: diagnostic only |

**What this is not:** peer review, independent validation, consensus or approval. It does not close D05 and does not reopen or confirm K3. Whether a restructure is *warranted* is a judgement no V1 check can make.

---

## 1. How the agent works

- **Isolation (§7B.6).** Each run copies 15 named inputs into a fresh scratch directory (`restructure_audit_agent_*`) and reads only those copies. A missing input stops the run (fail closed).
- **Separation from the L1 receipt.** The agent does not read the L1 receipt. It computes each fact from the frozen inputs, then labels the result with the receipt finding (F-01 … F-15) or protocol rule it tests. A wrong receipt claim therefore shows up as a failure.
- **Git checks.** G01: the protocol was committed before the receipt (pre-registration). G02: the L2 packet's bytes are unchanged since commit e20d915.
- **Non-vacuity (§3.6).** `--self-test` applies seven mutations to scratch copies: a banned word in KERNEL, a stale length target, an unknown ledger ID, a deleted outline field, a broken writing rule, a novelty claim, and a removed part-number mapping. Each targeted check must fail. All seven were detected.
- **Diagnostic checks.** D01 compares the F1 reading routes with the persona-to-chapter map frozen in the L2 packet. A difference is reported as DIFF, not FAIL, and needs a recorded disposition.
- **Receipt.** [`RESTRUCTURE_AUDIT_AGENT_RECEIPT.json`](RESTRUCTURE_AUDIT_AGENT_RECEIPT.json) holds the SHA-256 of every input and every check result.

## 2. Results

**First run** (inputs at HEAD 5dfea16): 24 PASS, 1 FAIL, 1 DIFF. All 15 receipt findings that could be encoded held except the two below.

**Rerun** after the fixes: 26 of 26 PASS. Self-test: 7 of 7 mutations detected. Unit tests have been added (`tests/test_restructure_audit_agent.py`).

## 3. Findings and dispositions

| ID | Check | Exact location | Finding | Disposition |
|---|---|---|---|---|
| AG-01 | A16 (spec §2 required fields) | `books/manuscript/en/DETAILED_OUTLINE_VOL1.md`, Chapter 5 table | The "Not answered here" field was missing. It is the only one of 81 required chapter fields that was absent. The L1 self-audit did not notice. | **Accepted; fixed.** Added: "What one reading means for this person (6); whether this person's aging slowed (7); distance to a threshold (9); whether to buy or repeat a test (29)". |
| AG-02 | D01 (routes against persona map) | VOL1 "Reading routes" table, against L2 packet §persona table | Three routes dropped chapters that the pre-registered map assigns to the persona. R1 dropped 2–4. R3 dropped 18–22, including both capacity-accounting chapters (H chapters 21–22). R4 dropped 26 (meaning), 27 (distribution) and 29 (decisions). | **Accepted in part.** R3 now reads 1–3 → 10–22 → 32–33. R4 now reads 1 → 23–30, then 9 and 22. R1: 2–4 marked optional rather than required, because the "My number" route deliberately starts with the reader's question (F1 design). Both are desk changes; there is still no reader evidence (MR-2 open). |

**Checks that passed and matter most:**

| Check | What held |
|---|---|
| A01, A02 | 33 chapters in order; Volume Ⅲ is 33.3% of chapters (≥ 28%) |
| A03, A04 | F1 and B1–B4 are slots, not chapters; B2 forbids thresholds |
| A09 | No stale length targets remain (DEC-017) |
| A10, A20 | No banned novelty words in KERNEL interpretation cells or new planning files |
| A13, A14, A18 | Ownership table names real chapters; every chapter owns something; Volume Ⅰ ownership matches the table |
| A17 | Every ledger ID cited in the outline exists |
| G01, G02 | Pre-registration order holds; packet unchanged |

## 4. What remains unaudited

- **Judgement.** Whether three volumes and 33 chapters fit the US/Canada market. Whether R1 stays with the book through Volume Ⅱ (MR-2). Whether the F1 scene works. None of these can be encoded as V1.
- **Correctness of the chosen properties.** The same assistant chose what to check, so blind spots shared with the L1 audit are likely.
- **Evidence content.** The agent checks that ledger IDs exist, not that they support the outline's use of them.

**Next steps.** Run the prepared clean-session prompt in a separate session, preferably on a different model family (V4). Ask a qualified human editor or agent to read the packet. Neither has happened.
