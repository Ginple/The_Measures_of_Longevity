# Clean-Session Blind Review — Prompt and Materials (prepared 2026-11-28, not yet run)

**Status: prepared, not run.** Playbook R3.8 §10 calls for a separate clean session that sees only frozen materials. This sandbox cannot reach an isolated model, and a session inside the same conversation is not clean. The owner, or someone the owner chooses, runs it. The result is **V4: diagnostic only**. It is not peer review, it does not close D05, and it cannot by itself trigger K3. A K3 finding is one of the DEC-018 reopen triggers: it makes the author reconsider, but does not decide.

## How to run

1. Open a new chat with no project history. Use a different model family from the one that drafted the project, if possible. Do not connect GitHub, Linear or other project apps.
2. **Stage A.** Paste the prompt below, then the full text of the frozen packet `review/MARKET_RESTRUCTURE_AUDIT_PACKET_L2_2026-11-27.md`. Its SHA-256 at commit e20d915 is recorded in `review/RESTRUCTURE_AUDIT_AGENT_RECEIPT.json`; check the hash before pasting.
3. **Stage B** (optional, after Stage A is saved). Paste `books/manuscript/en/DETAILED_OUTLINE_SPEC.md` and `books/manuscript/en/DETAILED_OUTLINE_VOL1.md`. Ask: "These were written after the packet was frozen. Do they resolve, leave open, or worsen each concern you raised? Cite locations."
4. **Do not provide** the L1 receipt, the audit agent report, MASTER, CLAIM_LEDGER, the market-positioning file's rationale sections, defense memos or this chat. Withholding them is the point (CGEE R5.5 E32).
5. Save the output verbatim as `review/blind/<YYYY-MM-DD>_<model-or-reviewer-category>/RECEIPT.md`, using a new folder for each run. Record the model name if known, the date, and the exact materials pasted.
6. The project assistant then gives each concern a disposition (accepted / rejected with reason / deferred) against its exact location, in the same folder. The dispositions are V5.

## Prompt (Stage A)

> You are a senior acquisitions editor at a US trade nonfiction publisher, and also a methodologist who reviews aging-biology books. You have no stake in this project.
>
> Below is a frozen audit packet for a long nonfiction book, *The Measures of Longevity*. Use only the packet. Take the harshest plausible stance a real editor or reviewer would take. Your job is to find what is wrong, not to confirm.
>
> 1. For each object O1–O7, give exactly one level (K0–K3, as the packet defines them). Give the single strongest reason, and cite the packet section.
> 2. Name the three biggest risks that would stop a US/Canada editor from acquiring this book. For each, give the location in the packet and the smallest change that would answer it.
> 3. Say whether any vetoes (V1–V5 in the packet) are triggered.
> 4. List what you could not judge from the packet alone.
> 5. State your category (model, or human role) and any interest you have in the outcome.
>
> Do not praise. Do not rewrite chapters. Do not invent market data. If you assume something, label it as an assumption.
