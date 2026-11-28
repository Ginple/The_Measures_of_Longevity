# Ch3 English pilot (DEC-016) / 第 3 章英文试点

- **What it binds**: ten paragraph units of the English draft [CH03_four_links_draft_en.md](../../../books/manuscript/en/CH03_four_links_draft_en.md). The chapter is new writing that uses V6 §02–03 and V7 §02 (in `corpus/`) as leads; nothing is translated from them.
- **Evidence**:
  - Verbatim abstract sentences in `evidence/`, with competing-interests statements where declared:
    - `THEORIES_abstracts.txt`: Gladyshev 2026 (*PNAS*, "Simply aging"), Yücel, Molière and Gladyshev 2026 (*Nature* review; one author employed by Novartis) and Lemaître et al. 2024 (*PLoS Biol* Essay). The first two share an author.
    - `TRIALS_abstracts.txt`: CAST (Echt 1991), ILLUMINATE (Barter 2007), ACCORD (Gerstein 2008) and Voight 2012 (HDL mendelian randomisation; middle-dot decimals in the source).
  - A project record, cited as such and not as a primary source: a verbatim copy of ledger rows X28 and X85 (`evidence/LEDGER_X28_X85_excerpt.txt`, so that new ledger rows do not make claims stale).
  - One project synthetic source, bound as one formal claim: `confounded_marker.py` (a marker that predicts an event through a hidden condition but has no effect of its own), with its output saved as `evidence/CONFOUNDED_MARKER_SYNTHETIC_output.json`. The test recomputes this output.
- **How**:
  - `build_project.py` reuses the ch5 builder's span-location and hashing helpers.
  - An edit to the chapter, an excerpt, the script, the saved output or the ledger excerpt makes the affected claims stale.
  - `tools/claim_token_scan.py` covers this pilot.
- **Re-binding**: run `python knowledge_base/pilots/ch03_four_links_en/build_project.py` deliberately, after a reviewed change. `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - full texts. Two points the V6 corpus attributes to these papers are not in the abstracts and are not used: that "Simply aging" distinguishes the deleteriome from entropy and says the burden cannot yet be quantified, and the Lemaître "age-specific optimum" idea;
  - the ILLUMINATE protocol amendment (X28), disclosed in the chapter but unresolved;
  - the X85 prior-work search, which the ledger calls not exhaustive; the underlying papers were not re-read;
  - independent human review, waived by the owner (DEC-020); `tools/claim_audit_agent.py` checks encoded properties only. Formal release stays **blocked** by the depth debt and the incomplete claim inventory.
- **Checks**: `tests/test_ch03_en_pilot.py`. These are bookkeeping checks only, not scientific validation.
