# Ch10 English pilot (DEC-016) / 第 10 章英文试点

- **What it binds**: eight paragraph units of the English draft [CH10_routes_draft_en.md](../../../books/manuscript/en/CH10_routes_draft_en.md). The chapter is new writing that uses V6 §06–§07 (in `corpus/`) as leads; nothing is translated from them. The five-route table is the book's framework, not a source claim, and is not bound.
- **Evidence**:
  - Verbatim abstract sentences in `evidence/`, with competing-interests statements where declared:
    - `ROUTES_TRIALS_abstracts.txt`: SPRINT 2015 (blood-pressure targets; maintenance), Skou 2015 (knee replacement; replacement) and ACHIEVE 2023 (hearing intervention; compensation). Three independent groups;
    - `IMMUNE_SUPPORT_abstract.txt`: Friedrich 2025/2026 *Nature*, a **mouse** study (mRNA for DLL1, FLT3L and IL-7 delivered to liver cells; reversible after dosing ceased);
    - `CAPABLE_abstract.txt`: a copy of the chapter 1 excerpt (Szanton 2019). The test checks the copy is identical.
  - Project records, cited as such and not as primary sources: `evidence/LEDGER_X15_X79_excerpt.txt`, a verbatim copy of ledger rows X15 (withdrawn maintenance-capacity formula) and X79 (CAPABLE primary-outcome descriptions differ between documents). The test fails if a ledger row changes without a re-copy.
- **How**:
  - `build_project.py` reuses the ch5 builder's span-location and hashing helpers.
  - An edit to the chapter or to an excerpt makes the affected claims stale.
  - `tools/claim_token_scan.py` covers this pilot.
- **Re-binding**: run `python knowledge_base/pilots/ch10_routes_en/build_project.py` deliberately, after a reviewed change. `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - full texts, including how long the mice were followed after dosing and the ACHIEVE sensitivity analysis;
  - the CAPABLE registration history and dated protocol (X79);
  - the senolytic, social-prescribing and home-modification evidence listed in the outline (X99), left to chapters 19 and 23;
  - independent human review, waived by the owner (DEC-020); `tools/claim_audit_agent.py` checks encoded properties only. Formal release stays **blocked** by the depth debt and the incomplete claim inventory.
- **Checks**: `tests/test_ch10_en_pilot.py`. These are bookkeeping checks only, not scientific validation.
