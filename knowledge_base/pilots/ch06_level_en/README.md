# Ch6 English pilot (DEC-016) / 第 6 章英文试点

- **What it binds**: eight paragraph units of the English draft [CH06_level_draft_en.md](../../../books/manuscript/en/CH06_level_draft_en.md). Chapter 6 inherits no earlier chapter, so it was written in English first and has no Chinese lineage link.
- **Evidence**:
  - Verbatim abstract sentences in `evidence/`: Higgins-Chen 2022, including its competing-interests statement; Sugden 2020; Song 2026; Jonkman 2026; Oh 2025; Ye 2023.
  - One introduction passage from Borrus 2026, and the Results passages from Jonkman 2026 that give the ranges behind its abstract maxima.
  - The project's synthetic saturating-removal memo (formal claim).
  - Each file header records the PMID, the DOI, the fetch date and any declared conflicts of interest.
- **How**:
  - `build_project.py` reuses the ch5 builder's span-location and hashing helpers.
  - An edit to the chapter, an excerpt or the memo makes the affected claims stale.
- **Re-binding**: run `python knowledge_base/pilots/ch06_level_en/build_project.py` deliberately, after a reviewed change. `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - full-text reading, and the erratum to Song 2026;
  - an unconflicted test–retest study of a consumer-marketed clock (searched for, not found);
  - the bookkeeping paragraph on the two 2025 organ-age studies, which rests on ledger X81;
  - independent review. Formal release stays **blocked**.
- **Checks**: `tests/test_ch06_en_pilot.py`. These are bookkeeping checks only, not scientific validation.
