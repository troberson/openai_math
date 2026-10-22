# Summary-page production loop

The resume protocol. Read this after a compaction: it carries state only. The method —
page format, the data-file convention, the normalizer contract, the measured quotation
traps, the batch workflow — lives in
`.qwen/skills/auto-skill-family-summary-citation-verified/`. Nothing here is a task list;
`bd ready` is the only tracker.

## Current state (rewritten at every batch boundary, 2026-10-22)

- **Live pages: 60** family pages in `notes/summaries/` plus the index `README.md` (61
  files). The last page landed is family 362; the ledger's `summary` column is 1 for
  those 60.
- **Data files: 60** in `notes/data/summaries/` (one per family page). The renderer
  is `build_summaries.py`; the skeleton is
  `notes/templates/summaries/summary.md.j2`.
- **Queue:** epic `math-cgv` (P2) with `math-cgv.11` claimed (rewrite the skill and
  the resume protocol — this file). Epic `math-ckd` (P4) open — Tier C summary pages
  remain. `math-vtj` (P3) ready — retire transcribed corpus figures.
- **Git:** the batch is pushed; `origin/notes` is current.
- **Loop:** cleared 2026-10-15. Continuation is human-driven; do not re-arm without
  a fresh instruction.

## Next batch

When `math-cgv.11` closes, the next ready `math-cgv` child (if any) outranks the P4
summary pages. When no `math-cgv` child is ready, the next batch is Tier C summary
pages under `math-ckd`: 71 Tier C families in twelve disciplines, 23 landed, 48
remaining (measured from the ledger 2026-10-17; re-measure before starting).

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
