# Verification Levels, Tool Status and AI Disclosure

*Version 0.1, 2026-11-28 (DEC-019). English is the first language (DEC-016).*

**Purpose.** This page says how strongly any "passed", "audited" or "verified" statement in this repository can be read. It applies the two reference documents in the repository root:

- [Playbook R3.8 (EN)](../ARENA_AGENT_UNIVERSAL_P0_P8_PLAYBOOK_EN_2026-11-10_R3.8.md): §3.3, §7D, §7G, §10 and §11. The [Chinese edition](../ARENA_AGENT_UNIVERSAL_P0_P8_PLAYBOOK_ZH_2026-11-10_R3.8.md) has the same section numbers.
- [CGEE R5.5](../CGEE_R5.5.md): §2.3 and Appendix A.

Both are reference documents, not project rules. Where they conflict with an author decision in [MASTER](../knowledge_base/MASTER.md), MASTER governs.

---

## 1. One scale for every claim of checking

A statement cannot be stronger than the strongest verifier actually run (playbook §3.3).

| Level | Verifier | Examples in this repository | May close a gate? |
|---|---|---|---|
| V1 | Formal or deterministic | Unit tests; `scripts/run_validation.py`; ch5 binding `--check`; [`tools/restructure_audit_agent.py`](../tools/restructure_audit_agent.py); outline-to-corpus hash binding | Supports closing the encoded property; the owner closes |
| V2 | Executable check against an external record | PubMed and DOI lookups logged in `knowledge_base/search_logs/SEARCH_LOG_*.csv` | Supports closing that record match; the owner closes |
| V3 | Validated model judge | None exists | — |
| V4 | Unvalidated model judgement or role-play | RT-C reader walk-through; any clean-session blind review ([prepared prompt](../review/blind/BLIND_REVIEW_PROMPT_2026-11-28.md)) | Diagnostic only |
| V5 | Self-assessment by the producing assistant | L1 audits; dispositions; "fixed" in commit messages | Never |

**How the project's own labels map onto this scale:**

| Project label | Where defined | Highest V level it can reach | Notes |
|---|---|---|---|
| Audit L1 | [restructure protocol](../review/MARKET_RESTRUCTURE_AUDIT_PROTOCOL_2026-11-27.md) | V5, plus any V1 checks it ran | Same assistant wrote the plan |
| Audit L2 | same | V4 | External model, clean context. Declined by the author on 2026-11-28 |
| Audit L3 | same | Human; outside V1–V5 | Qualified editor, agent or domain expert. **Not done** |
| Audit agent (2026-11-28) | [report](../review/RESTRUCTURE_AUDIT_AGENT_REPORT_2026-11-28.md) | V1 for 26 encoded properties | Choice of properties is V5 |
| K0–K3 | restructure protocol | — | Size of change, not strength of evidence |
| D05 | [MASTER](../knowledge_base/MASTER.md) | — | Independent human external review. **Open.** Nothing on this scale closes it |
| CI green | `.github/workflows/ci.yml` | V1 | Software properties only. Not a scientific or editorial verdict |

## 2. Tool status

The [tool status register](TOOL_STATUS.tsv) lists every script in `tools/` with one of four states (CGEE §2.3):

| State | Meaning |
|---|---|
| planned | Does not exist yet |
| implemented | Exists, with no automated test |
| tested | Has an automated test that runs in CI |
| verified | Validated against known answers by someone other than the authoring assistant |

Two rules apply:

- A tool below `tested` must not be described as "in force".
- A tool below `verified` must not be a blocking gate for any scientific or release decision.

[`tests/test_tool_status.py`](../tests/test_tool_status.py) checks that the register lists every tool, uses only these states, backs every `tested` entry with a real test file, and marks nothing `verified`.

**Known tension.** CI does fail a pull request when a `tested` tool's tests fail. This is treated as a *software regression* gate. It says nothing about scientific or release readiness, which no `tested` tool may decide.

**Current state (2026-11-28):**

| State | Tools |
|---|---|
| tested | 8 |
| implemented | 4 (one of them disabled by design) |
| verified | 0 |

## 3. Prose style without hiding evidence

[`tools/prose_repetition.py`](../tools/prose_repetition.py) applies playbook §7G item 1. It reports the share of body sentences repeated verbatim in at least three other chapters.

**Current result:** 0% for the eight Chinese demonstration drafts, and not measurable for English, which has one chapter.

The playbook's 59% figure comes from another project; it is not a measurement of this one. Rules:

- The tool never blocks.
- It is not an AI detector. Detector scores are never used.
- Paraphrasing to lower the number is not a fix.
- Paragraph-level near-duplicate checks are not built yet (§7G item 6).

## 4. AI-assistance disclosure

### 4.1 Commit trailer

From 2026-11-28, every commit that changes prose or evidence carries an AI-assistance trailer:

```
AI-Assisted: Arena.ai Agent Mode (model not disclosed by the platform); human review: none
```

- Replace `none` with the reviewer's role once a person has read the change.
- Earlier commits have no trailer. The PR #4 history and its comments are the record for them.

### 4.2 Disclosure draft for the book and papers (playbook §7D; CGEE Appendix A)

> Drafting and research assistance: Arena.ai Agent Mode, 2026-11 onward. The platform does not disclose which model or models served each session, and the model may change within a session. Session records are kept in pull request #4 of the project repository. Human verification performed: [to be completed by the author: which chapters, claims and citations a person checked].

- **Before submission:** ask each venue's editor whether this disclosure is acceptable. Venues that require a model name and version may need text regenerated with a tool whose model is known.
- **Prompts and outputs:** keep them; some publishers ask for them.
- **Unedited machine text:** never present it as written without AI involvement.

### 4.3 Contribution log

[`governance/AGENT_CONTRIBUTION_LOG.tsv`](../governance/AGENT_CONTRIBUTION_LOG.tsv) records, for each text unit, the categories from playbook §11:

- agent-drafted/human-reviewed
- agent-drafted/not human-reviewed
- human-drafted/agent-verified
- human-only

Every assistant-written unit is currently `agent-drafted/not human-reviewed`. The author-supplied V6/V7 corpora are marked `author-supplied; drafting provenance not recorded`, because how they were drafted is not recorded in this repository.

## 5. Operational notes

- **Repository actions use the owner's account.** Pushes and comments are made under the owner's GitHub account (`Ginple`), not a separate agent account with Write-only permission. History therefore cannot distinguish the assistant's actions from the owner's (playbook §7E). This is recorded, not fixed.
- **Conflict-of-interest ledger.** Playbook §11 asks for a dated funding and conflict-of-interest ledger, and for commercial interests in products the book discusses to be stated identically wherever they appear. None exists yet. See [UNGROUNDED_RESIDUE](../review/UNGROUNDED_RESIDUE.md) item UR-09.
