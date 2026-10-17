# Summary-page production loop

The resume protocol. Read this after a compaction: it carries state only. The method — page format,
citation grammar, the normalizer contract, the measured quotation traps — lives in
`.qwen/skills/auto-skill-family-summary-citation-verified/`. Nothing here is a task list; `bd ready` is
the only tracker.

## Current state (rewritten at every batch boundary, 2026-10-17)

- **Live pages: 60** family pages in `notes/summaries/` plus the index `README.md` (61 files). The last
  page landed is family 198, committed `d23b1fb74`; the ledger's `summary` column is 1 for those 60.
- **Queue:** epic `math-rui` (P2, *Generate the census page's Cost and check()-count figures as writer
  slots*) — children `.1`–`.5` closed, `.6` claimed and in progress, `.7` open. Epic `math-cgv` (P2)
  with `math-cgv.1` ready. Epic `math-ckd` (P4) open; `math-ckd.5` claimed — Tier C group 2: **71** Tier C
  families in the twelve disciplines, **23 landed, 39 remaining** (measured from the ledger 2026-10-17;
  the bead body's 99 families / 179 manuscripts is stale).
- **Git:** HEAD `75dae5cea`, `origin/notes` at `75dae5cea` — the batch is pushed.
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
  the sweep lands bytes the writer reproduces, not bytes any pass verifies. The probe is promoted to
  `notes/scripts/measure_check_calls.py` (2026-10-16, bead `math-rui.2`): a gate row that starts
  after the render, a census writer row, and the record `check_calls.json` under the keyed store, so
  the baseline the script carries is re-measured every pass and a drift prints as a disagreement.

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

- **2026-10-16 — the Cost section is swept to the fourth green run, and the builder sweep runs
  after every commit that moves `templates.md`, not just after the page commit.** The fourth green
  run measured **239.30 s** wall (04:53:47–04:57:46 local), **604.9 s** row-time sum, **39.6%** of
  the sum, 24 checker invocations summing **125.0 s**. 11 of 23 Cost cells moved, the writer tail,
  the heaviest-row claim, and 7 of 11 `run_tests.py` figures. **The ordering refinement:** the
  earlier rule said "builder sweep after the commit", which covered only the page commit. The
  template commit also moves `notes/development/templates.md`, which is in the builder's L1, so the
  builder must run again after it. The gate's sixth run failed 2 rows — 21 `cache entry missing`
  for `build_report_templates.py` — for exactly that reason; the re-run took the promote checker to
  `problems 0`.

- **2026-10-16 — the Cost section is swept to the fifth green run, the first gate pass over a swept
  census page.** The fifth green run measured **232.97 s** wall (05:47:37–05:51:30 local), **594.7 s**
  row-time sum, **39.2%** of the sum, 24 checker invocations summing **121.7 s**. 9 of 23 Cost cells
  moved, the writer tail, the heaviest-row claim, and 7 of 11 `run_tests.py` figures. The sweep, the
  builder sweep after the page commit, the render, the census checker, its 20 self-tests, the template
  commit, the builder sweep after *that* commit, and the promote checker all ran in the recorded
  ordering and produced no diff on the page and `problems 0`. **The Cost cells and the `check()`-count
  sentences remain template literals with no checker** — beads `math-rui.3` and `.4` make them slots
  measured by the writer, which is the fix for the treadmill this sweep is.

- **2026-10-16 — `math-rui.1` lands the gate-row table, and the render has to run after the last
  commit that moves HEAD.** `notes/scripts/measure_gate_rows.py` reads the driver's report for the
  last completed run and lands `notes/tables/gate-rows.tsv` (81 rows: `spec`, `seconds`) through the
  promote registry, reconciled against `gate.py`'s `ROWS` block: 81 rows in list order, 594.7 s of
  row time, 0 non-zero exits, every spec once. It is not a gate row — the driver truncates the report
  at run start, so a gate row would read the previous run's bytes. Its `L1` names the report, outside
  the `notes/` bucket the probe record prints, so it joins `PROBE_EXEMPT`. **Two drifts the checker
  caught, not the page:** the render's cache key hashes the git tree digests, so a render run *before*
  a commit lands records under a key the checker can no longer match (21 `cache entry missing`); and
  the writer's `L1` expands `notes/tables/` to the nine TSVs, so the newest probe record for
  `render_reports.py` had to be re-landed and `PROBES` gained `2026-10-16_rr_fleet.txt`. The census
  page, `notes/README.md`, `index-design.md`'s TSV inventory (21 tracked, 2,567,565 B), the fleet page
  and `templates.md` all moved with the new table, and the promote checker ends at `problems 0`.

- **2026-10-16 — `math-rui.2` promotes the `check()`-count probe to a gate row, and a registry edit
  moves the render's key.** `notes/scripts/measure_check_calls.py` patches
  `importlib.util.spec_from_file_location` (the conftest's `load` fixture uses exactly that call),
  wraps each loaded checker's `check`, and runs one pytest row per checker: 11 checkers, 184 calls,
  every baseline reproduced. The record `check_calls.json` lands under the keyed store keyed by the
  script tree's git digest, so there is no tracked artifact and the census names the record. The gate
  row starts after the render, because each checker reads the pages its own self-tests verify. **Two
  drifts the checker caught, not the page:** the writer's `L1` names `notes/scripts/`, which the probe
  record's printed scope excludes, so the entry joins `PROBE_EXEMPT` — without the exemption the
  exactness pass reports a problem it cannot fix; and because the key hashes `notes/scripts/` from the
  working tree, editing `promote.py` moved `render_reports.py`'s key, so the render had to run again to
  land its records under the current key (21 `cache entry missing` before the re-render). The fleet
  page's gate paragraph moved to 82 invocations: the writer measures that count off `gate.py`'s `ROWS`
  block, so the row had to be committed before the render could measure it.

- **2026-10-16 — `math-rui.3` slots the Cost prose, and two figures stay literal because the gate
  driver prints no wall time.** The checker-invocation count and sum, the row-time sum, the heaviest
  row with a Cost cell, and the four writer tail times are all readable from
  `notes/tables/gate-rows.tsv`, so the writer renders each whole sentence: 24 checker invocations
  summing to 121.7 s, 81 row times summing to 594.7 s, the heaviest Cost row at 64.7 s. The gate wall
  and its percentage of the serial baseline are **not** in the TSV — the driver prints per-row times
  only, never a total — so those two stay template literals with no checker. **A generator expression
  cannot be split across two f-string literals:** the first `{` is never closed and all three linters
  report the same 47 syntax errors rooted at that line. The cost is not local: the broken writer makes
  the pytest rows that import it fail, so the probe read `total check calls 21` with 9 baseline
  disagreements instead of 184 with 0. **The record key moves with the writer:**
  `measure_check_calls.py`'s `L1` is the script tree, so editing `render_reports.py` invalidates the
  record the render reads, and the probe must run cold before the builder and render.

- `math-rui.4` (2026-10-16): the Cost pass measures the Cost cells, the self-test row figures, the
  `check()` counts, the two sums, the heaviest-row claim, and the tail figures from
  `notes/tables/gate-rows.tsv` and the keyed `check_calls.json` record; the checker carries none of
  them. **Pair a row figure with the closest preceding checker named in the paragraph, not the last
  name in Cost-table order:** the table is alphabetical, so `verify_verification_dirs.py` swallowed
  the five figures of the checkers named after it in the same paragraph. **Key a `check()` count to
  the paragraph that begins with the checker's own name:** the Cost prose is one blank-line block, so
  a block-level test let the sources paragraph's "the 15 `check()` calls" satisfy named_results.
  **The paragraph boundary is the next checker-name paragraph, not the next backtick** — a
  continuation line can begin with a backtick, and the first paragraph naming a checker is a
  writers-table row, not the Cost paragraph. **Read the "not a row above" exemption from the page's
  own declaration:** a page-wide test excused every checker row, so a deleted Cost row passed.
  Patterns for the sums tolerate line breaks; a claim that wraps across a newline matches zero times.

- `math-rui.5` (2026-10-16): the builder ran after the census page commit, so it read HEAD's bytes.
  The template is unchanged (49 slots, 164 literal bold phrases), the render produces no diff on
  `notes/scripts/README.md`, the promote checker reports `problems 0`, the census checker reports
  `sync problems 0`, and 30 self-tests pass. **The 164 literals stay because the writer supplies no
  value for them** — a slot exists only when the writer's value appears in HEAD's page bytes, so the
  literals become slots when the writer measures them, which is bead `.7`'s measuring pass, not a
  builder run.

- **2026-10-17 — the census checker's three problems were one row in the wrong table.** The checker
  keys table rows by `### ` heading, so the writers table is compared against the derived writer set
  and the report-only plus checkers tables form the non-writer partition. `check_gate_budget.py` writes
  nothing, so its row in the writers table was invisible to the partition (the checker reported it
  missing from the non-writers) and inflated the writers table; its 4 cells also mismatched the
  4-column writers header. The row now sits alphabetically first in the 3-cell report-only table, and
  the counts the checker measures swept: 71 to 72 scripts, 31 to 32 report-only, 54 to 55 write nothing,
  and the stale 81-row gate to the measured 82. The checker reports 0 problems, all reconciliations
  True, sync 0, and the probe's baseline disagreements 0.

- **2026-10-17 — the two self-test figure mutants were stale, not failing.** The Cost pass dropped the
  self-test row figures: a run-dependent time cannot live in a template keyed to HEAD, so the page
  carries no row figure and the needle `verify_findings.py: the page says` no longer exists. The two
  mutants keyed to that needle reported failures. Removing them and their three helpers leaves 28 tests,
  all passing.

- **2026-10-17 — the driver on disk had no post-gate section, so the Cost cells recorded the previous
  run.** The handoff claimed the wall, the row times, the render, the probe, the census checker, and the
  budget assertion were committed; the driver ended at `GATE_DONE`. The post-gate section now lands
  `gate-rows.tsv` from the report this run printed, renders the pages from it, commits the swept pages,
  rebuilds the templates from the committed pages, commits them, then runs the probe, the census checker,
  and the budget assertion. The probe runs after the builder because both write inside the tree the
  probe's key hashes. The driver stops before the sweep if the gate printed any failure, and commits the
  beads store on its own path so the tree ends clean.

- **2026-10-17 — the gate ran green for the first time: 82 rows, 0 failures.** The three failures the
  handoff carried were diagnosed individually. `verify_cache_promotion.py` reported 21 `cache entry
  missing` for `build_report_templates.py` because the commits moved HEAD and the builder's key hashes
  HEAD, so the builder had to run for all pages. `test_cache_promotion.py` passes 10 once the records are
  under the current key. `test_tsv_quoting.py`'s clean test asserted a stale literal 25 TSVs and 26727
  rows — `gate-rows.tsv` is the 26th table under `notes/tables/` and its 82 rows move the sum to 26809.
  The budget assertion ran green: wall 261.86 s inside the 300 s budget.

## Pointers

- Method, format, citation grammar, quotation traps: `.qwen/skills/auto-skill-family-summary-citation-verified/`.
- Design decisions for the template renderer: `math-cgv`'s epic body.
- Cost model, tier definitions, the page-format history: the skill.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.
