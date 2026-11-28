# Ch8 English pilot (DEC-016) / 第 8 章英文试点

- **What it binds**: eight paragraph units of the English draft [CH08_recovery_draft_en.md](../../../books/manuscript/en/CH08_recovery_draft_en.md). V6 chapter 16 and V7 chapter 17 were used as source material. The English was written first, so there is no line-by-line lineage link.
- **Evidence**:
  - Verbatim abstract sentences in `evidence/`, with competing-interests statements where declared:
    - Varadhan 2008 and Manning 2026 (the resilience concept);
    - McCrory 2016 (heart-rate recovery on standing) and Schumock 2024 (glucose-tolerance curves);
    - Boyd 2008 (recovery after hospitalization);
    - Pyrkov 2021 (an extrapolated divergence point);
    - Wilding 2022 (weight regain after stopping semaglutide).
  - The project's synthetic saturating-removal memo (formal claim).
- **How**:
  - `build_project.py` reuses the ch5 builder's span-location and hashing helpers.
  - An edit to the chapter, an excerpt or the memo makes the affected claims stale.
- **Re-binding**: run `python knowledge_base/pilots/ch08_recovery_en/build_project.py` deliberately, after a reviewed change. `--check` exits 1 if `project.json` is out of date. Tests never re-bind.
- **Not covered**:
  - full texts, including the age-adjusted heart-rate recovery estimates (ledger X132);
  - a human study that measures level, rate and recovery before and after an intervention;
  - independent review. Formal release stays **blocked**.
- **Checks**: `tests/test_ch08_en_pilot.py`. These are bookkeeping checks only, not scientific validation.
