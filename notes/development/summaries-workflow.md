# Summary-page production loop

The resume protocol. Read this after a compaction: it carries state only. The method — page format,
citation grammar, the normalizer contract, the measured quotation traps — lives in
`.qwen/skills/auto-skill-family-summary-citation-verified/`. Nothing here is a task list; `bd ready` is
the only tracker.

## Current state (rewritten at every batch boundary, 2026-10-16)

- **Live pages: 61** in `notes/summaries/`. The last page landed is family 198, committed `d23b1fb74`;
  the ledger's `summary` column is 1 for those 61 families.
- **Queue:** epic `math-cgv` (P2, *Render summary pages from jinja2 templates with quotes resolved
  from `quotes.tsv`*) with 11 children in a linear dependency chain; `math-cgv.1` is the ready row.
  Epic `math-ckd` (P4) stays open; `math-ckd.5` is claimed and in progress — Tier C group 2, 100 pages
  scoped, 32 landed.
- **Git:** HEAD `0db3ba71a` (the beads store recording `math-cgv`), `origin/notes` at `7a3310c00` —
  `d23b1fb74` and `0db3ba71a` are unpushed.
- **Loop:** cleared 2026-10-15. Continuation is human-driven; do not re-arm without a fresh instruction.

## Next batch

`math-cgv.1` — the math-mode-aware normalizer. A P1/P2 issue outranks the P4 summary pages; when a
`math-cgv` child is ready, work it before any `math-ckd` page.

## Gates (run at every batch boundary, quote numbers only from this run)

```
bash notes/scripts/gate_driver.sh                  # rows in dependency order; expect failures 0
python3 notes/scripts/verify_cache_promotion.py    # cached bytes == bytes on the tracked path
python3 notes/scripts/verify_summaries.py          # 0 problems over all pages
python3 notes/scripts/check_summary_manuscripts.py # 0 pages with an off-family manuscript
```

Reconciliation lines that must not move: 372 families, 719 manuscripts, 173 formalized, 242 scope
notes, 416 challenges, 200 `main_results` over 189 configs, both `overview.tex` ↔ `CONTENTS.md`
cross-checks 0.

## Commit and push boundaries

Explicit paths, one purpose per commit, never `--no-verify`, never `git add -A`. The beads store
travels in the commit whose work it records; a pathspec commit excludes it, so export by hand and commit
the store on its own. Push to `origin` (the fork) at a bead boundary, not per commit; `upstream` is
read-only; confirm with `git push --dry-run`.

## Stop and escalate

- **Stop the batch** when a gate fails twice on the same page: two failures mean the checker or the
  format is wrong, not the page. Fix that first, in its own commit.
- **Stop the run** when a P1/P2 issue becomes ready.
- **Never write an ungroundable page.** Record the family and the reason, leave its `summary` row 0.
- **Ambiguity:** record the provisional choice and what would force a revisit, then keep going. If
  fixing it later means rewriting pages, claim a different bead and come back.

## Decision points

- **2026-10-15 — the Cost section is swept to one fresh 81-row run, not to the two dated sentences
  alone.** The measurement: **234.05 s** wall (23:43:07–23:47:01 local), **622.0 s** row-time sum,
  **37.6%** of the sum, 24 checker invocations summing **132.8 s**. Swept in one pass: the 24 Cost
  cells, the checker-invocation sum, the wall/sum/percentage, the writer tail, the page_sync
  "heaviest row" claim, and the 11 `run_tests.py` row figures. Kept as history: the `--mutant`
  comparisons, the "before the record" figures, and the pre-cache 65/64-invocation times. **Not
  swept, because the gate does not measure them:** the per-checker `check()`-call counts
  (six/seven/ten/eleven/fourteen/fifteen/sixteen/seventeen/twenty/nine/thirteen) and "the 59-script
  scan". A revisit needs a scan of `notes/scripts/tests/`, not a gate row.

## Pointers

- Method, format, citation grammar, quotation traps: `.qwen/skills/auto-skill-family-summary-citation-verified/`.
- Design decisions for the template renderer: `math-cgv`'s epic body.
- Cost model, tier definitions, the page-format history: the skill.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.
