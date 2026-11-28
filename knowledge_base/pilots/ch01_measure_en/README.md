# Ch1 English pilot (DEC-016) / 第 1 章英文试点

- **What it binds**: six paragraph units of the English draft [CH01_measure_draft_en.md](../../../books/manuscript/en/CH01_measure_draft_en.md). The chapter rewrites the Chinese demonstration draft CH01 v0.2 (V6-01); it is not a translation.
- **Evidence**:
  - Verbatim abstract sentences in `evidence/`, with competing-interests statements where declared:
    - Garmany and Terzic 2024 (healthspan–lifespan gap in 183 WHO member states);
    - CALERIE phase 2: Waziry 2023 (methylation pace and clocks; the same sentences as the ch7 pilot), Villareal 2016 (bone density) and Romashkan 2016 (safety);
    - Szanton 2019 (CAPABLE randomized trial; the inventors' fee interest is declared).
  - A verbatim copy of the project claim ledger rows X21 and X29 (`evidence/LEDGER_X21_X29_excerpt.txt`, so that later ledger rows do not make claims stale), cited as records of earlier full-text reading by the same assistant, not as primary sources.
  - One project synthetic source, bound as a formal claim: `synthetic_life_table.py` (three populations with the same life expectancy, health-adjusted life expectancy and gap, but different person-level distributions), with its output saved as `evidence/LIFE_TABLE_SYNTHETIC_output.json`. The test recomputes this output.
- **How**:
  - `build_project.py` reuses the ch5 builder's span-location and hashing helpers.
  - An edit to the chapter, an excerpt, the script, the saved output or the ledger excerpt makes the affected claims stale.
  - `tools/claim_token_scan.py` covers this pilot: every number and capitalised word in a bound claim is either in the bound evidence or has a reviewed reason.
- **Re-binding**: run `python knowledge_base/pilots/ch01_measure_en/build_project.py` deliberately, after a reviewed change. `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - full texts (the healthspan paper's aggregates, X21 and X61; CAPABLE's 12-month results; why CALERIE reports give 220 and 218);
  - the value paragraphs (two accounts, who decides), which make no source claim;
  - independent human review, waived by the owner (DEC-020); `tools/claim_audit_agent.py` checks encoded properties only. Formal release stays **blocked** by the depth debt and the incomplete claim inventory.
- **Checks**: `tests/test_ch01_en_pilot.py`. These are bookkeeping checks only, not scientific validation.
