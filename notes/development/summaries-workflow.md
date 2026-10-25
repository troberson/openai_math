# Summary-page production loop

The resume protocol. Read this after a compaction: it carries state only. The method —
page format, the data-file convention, the normalizer contract, the measured quotation
traps, the batch workflow — lives in
`.qwen/skills/auto-skill-family-summary-citation-verified/`. Nothing here is a task list;
`bd ready` is the only tracker.

## Current state (rewritten at every batch boundary, 2026-10-25)

- **Live pages: 135** family pages in `notes/summaries/` (flat, no discipline
  subdirectory — bead `math-720` closed) plus the index `README.md` (136
  files). The ledger's `summary` column is 1 for all 135. Both summaries
  checkers pass clean (verify_summaries 0 problems over 136 pages;
  check_summary_manuscripts 0 off-family). Most recent additions: TCS families
  114 and 115.
- **Data files: 135** in `notes/data/summaries/` (one per family page, flat).
  The renderer is `build_summaries.py`; the skeleton is
  `notes/templates/summaries/summary.md.j2`.
- **Queue:** epics `math-cgv` (P2), `math-vtj` (P3) closed. `math-720`
  (flatten) closed. `math-ckd` (P4) pages are in flight; the TCS sub-queue has
  **28** families with `summary` 0 (measured 2026-10-25): 108 110 111 116 117
  118 119 120 121 122 124 125 126 127 128 129 130 131 132 133 134 135 137 138
  139 140 141 142. Family 116 is next.
- **Git:** `741e8655a` (family 115 summary) is pushed; `origin/notes` is
  current.
- **Loop:** standing `/loop` — work on the beads, commit and push between them.
  The `math-v5s` gen-folder reorganization (8 sub-beads) is tracked and deferred
  behind the TCS summary queue.

## Next batch

The next batch is the TCS summary sub-queue under `math-ckd`. Measured from the
ledger 2026-10-25: **30** TCS families carry `summary` 0 (listed above). The
gen-folder reorganization (`math-v5s`) is deferred behind it. Re-measure the
per-family tier and shape from the ledger row before writing each page; the
cost model in the skill bounds the source-row count per page.

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
