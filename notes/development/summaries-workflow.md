# Summary-page production loop

The resume protocol. Read this after a compaction: it carries state only. The method —
page format, the data-file convention, the normalizer contract, the measured quotation
traps, the batch workflow — lives in
`.qwen/skills/auto-skill-family-summary-citation-verified/`. Nothing here is a task list;
`bd ready` is the only tracker.

## Current state (rewritten at every batch boundary, 2026-10-23)

- **Live pages: 85** family pages in `notes/summaries/` plus the index `README.md`
  (86 files). The most recent addition is family 067; the highest-numbered family
  with a page is 362; the ledger's `summary` column is 1 for all 85. Both summaries
  checkers pass clean (verify_summaries 0 problems over 2341 quote specs;
  check_summary_manuscripts 0 off-family).
- **Data files: 85** in `notes/data/summaries/` (one per family page). The renderer
  is `build_summaries.py`; the skeleton is
  `notes/templates/summaries/summary.md.j2`.
- **Queue:** epic `math-cgv` (P2) and `math-vtj` (P3) closed. Epic `math-ckd` (P4)
  open with three children in progress — `math-ckd.3` (the remaining T0
  named-conjecture resolutions), `math-ckd.4` (Tier C group 1), `math-ckd.5`
  (Tier C group 2).
- **Git:** the batch is pushed; `origin/notes` is current (n5v closed 2026-10-23).
- **Loop:** `math-d73` closed and `math-n5v` closed as design-confirmed
  (2026-10-23). Continuation is human-driven; do not re-arm without a fresh
  instruction.

## Next batch

The P2 `math-cgv` epic and the P3 `math-vtj` are closed, so the next batch is the
P4 summary pages under `math-ckd`. Measured from the ledger 2026-10-23: **287**
families have `summary` 0 — 79 T0, 99 T2, 109 T3. Re-measure the per-group
populations from the skill's cost model before starting each of
`math-ckd.3` / `.4` / `.5`; the group boundaries come from that model, not from
this file.

## Gates (run at every batch boundary, quote numbers only from this run)

```
bash notes/scripts/gate_driver.sh                  # rows in dependency order; expect failures 0
python3 notes/scripts/verify_cache_promotion.py    # cached bytes == bytes on the tracked path
python3 notes/scripts/verify_summaries.py          # 0 problems over all pages
python3 notes/scripts/check_summary_manuscripts.py # 0 pages with an off-family manuscript
```

Reconciliation lines that must not move: 372 families, 719 manuscripts, 173 formalized,
242 scope notes, 416 challenges, 200 `main_results` over 189 configs, both
`overview.tex` ↔ `CONTENTS.md` cross-checks 0.

## Stop and escalate

- **Stop the batch** when a gate fails twice on the same page: two failures mean the
  checker or the format is wrong, not the page. Fix that first, in its own commit.
- **Stop the run** when a P1/P2 issue becomes ready.
- **Never write an ungroundable page.** Record the family and the reason, leave its
  `summary` row 0.
- **Ambiguity:** record the provisional choice and what would force a revisit, then
  keep going. If fixing it later means rewriting pages, claim a different bead and
  come back.

## Pointers

- Method, format, data-file convention, citation grammar, normalizer contract,
  quotation traps: `.qwen/skills/auto-skill-family-summary-citation-verified/`.
- Design decisions for the template renderer: the `math-cgv` epic body.
- Cost model, tier definitions, the page-format history: the skill.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.
