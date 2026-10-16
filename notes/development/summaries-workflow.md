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
  swept in that pass:** the per-checker `check()`-call counts and "the 59-script scan" — swept by
  the 2026-10-16 probe below.

- **2026-10-16 — the `check()`-call counts are swept by a probe, not by the gate.** The probe wraps
  `check` at load time (the conftest builds each checker through `spec_from_file_location`, so
  patching that function wraps the module the tests actually call) and counts real calls during each
  row's pytest run: findings 7→9, faithfulness 16→33, sources 13→15, index_design 15→16,
  fleet_design 17→23, verification_dirs 20→21, named_results 14→15, citations 10→12, t0_chains
  14→17, dependency_drift 11→12, subfinding_pairs 9→11, and the 59-script scan → 68. **These
  sentences are template literals with no checker**: the census checker does not measure them, so
  the sweep lands bytes the writer reproduces, not bytes any pass verifies. The probe is scratch
  under `.qwen/tmp/count_check_calls.py`; a revisit that wants the counts gated promotes it to
  `notes/scripts/` with a census row and a gate row.

- **2026-10-16 — the Cost section is swept again to the second 81-row run, and the builder sweep
  runs after the commit.** The gate run that fixed the cache-key ordering measured **230.69 s** wall
  (00:35:57–00:39:47 local), **582.4 s** row-time sum, **39.6%** of the sum, 24 checker invocations
  summing **115.9 s**. 18 of 23 Cost cells moved and every one is lower. The `check()`-count
  sentences stay swept: they are probe-measured, not gate-measured, so a gate run does not supersede
  them. **The ordering lesson:** `notes/development/templates.md` is in the builder's L1, so a commit
  that moves it moves HEAD; a builder sweep run *before* the commit lands records under a key the
  checker can no longer match — the gate's first run reported 18 `cache entry missing` problems for
  exactly that reason.

- **2026-10-16 — the Cost section is swept to the third run; the "sweep once" decision is
  superseded.** I argued the Cost column is a floor from one measurement, not a benchmark, so
  re-sweeping after every gate run is a treadmill; the direction was to sweep each green run. The
  third green run measured **244.54 s** wall (00:59:04–01:03:09 local), **610.8 s** row-time sum,
  **40.0%** of the sum, 24 checker invocations summing **122.6 s**. 10 of 23 Cost cells moved, the
  writer tail, the heaviest-row claim, and 9 of 11 `run_tests.py` figures; 13 cells, the
  `sources`/`verification_dirs` rows and the date stamp did not. **The Cost cells and the
  `check()`-count sentences are template literals with no checker** — the census checker does not
  measure them, so drift between runs is visible only by comparing the gate report with the page by
  hand. A sweep is now a per-green-run step, and the page's Cost section is the record of the last
  green run, not a stable benchmark.

## Pointers

- Method, format, citation grammar, quotation traps: `.qwen/skills/auto-skill-family-summary-citation-verified/`.
- Design decisions for the template renderer: `math-cgv`'s epic body.
- Cost model, tier definitions, the page-format history: the skill.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.
