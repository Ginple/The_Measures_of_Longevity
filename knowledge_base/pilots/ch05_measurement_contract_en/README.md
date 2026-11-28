# Ch5 English pilot (DEC-016) / 第 5 章英文试点

- **What it binds**: five claim units of the English draft [CH05_measurement_contracts_draft_en.md](../../../books/manuscript/en/CH05_measurement_contracts_draft_en.md). They are the same five units registered in the [Chinese pilot](../ch05_measurement_contract/README.md) (CH5-C001…C005).
- **How**:
  - `build_project.py` imports the Chinese builder. Evidence spans, claim contexts and assessment states are reused, not retyped, so the two language versions cannot silently disagree about what a source says.
  - Each English claim also cites the Chinese paragraph it was rewritten from (evidence `E-ZH-C00x`). An edit to the English text, to the Chinese v0.3 text, or to a quoted excerpt therefore makes the affected English claims stale.
- **Re-binding**: run `python knowledge_base/pilots/ch05_measurement_contract_en/build_project.py` deliberately, after a reviewed change; `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - translation accuracy beyond the bound numbers and qualifiers;
  - the three unregistered evidence paragraphs (CALERIE methylation/bone, DO-HEALTH, Malagón microsimulation);
  - independent human review, waived by the owner (DEC-020); `tools/claim_audit_agent.py` checks encoded properties only.
  - Formal release stays **blocked** by the open debts and the incomplete claim inventory.
- **Checks**: `tests/test_ch05_en_pilot.py`. Bookkeeping only, not scientific validation.
