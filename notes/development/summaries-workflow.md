# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction: it is the state carrier,
so it states what to do and what not to re-derive. The method (page format, citation grammar, the
measured quotation traps) lives in `.qwen/skills/auto-skill-family-summary-citation-verified/` —
`references/quotation-traps.md` carries the 21 shipped pages' defects.

## Current state (rewritten at every batch boundary, 2026-10-12)

- **All 21 pages are green.** `math-n5d.1` (P1, sweep the current pages to the post-merge sources)
  closed 2026-10-09 at `bb4e81799`. `verify_summaries.py` over all 21 pages: **3,635 marker
  positions, 925 quoted spans, 0 problems**; `check_summary_manuscripts.py`: **21 pages, 0 with an
  off-family manuscript, 57 manuscript dirs named, 0 unnamed-on-catalog, 0 named-by-another-family**,
  749 preprint dirs on disk, 719 named by `overview.tex`, 30 on disk and unnamed, 0 named and absent.
- **Pages done (21):** 001, 002, 004, 006, 007, 010, 011, 014, 016, 017, 018, 019, 032, 087, 102,
  159, 197, 221, 271, 287, 362. The ledger's `summary` column is 1 for those; the generator reports
  "summary pages 21 of 372 families, 57 manuscripts behind them".
- **Next batch:** `math-ckd.3` — tier B, the 78 remaining T0 families with `resolves_named = 1`
  (118 manuscripts, re-measured from the current ledger 2026-10-12). `bd update math-ckd.3 --claim`,
  then steps 1–10 per page. Check `bd ready` first: summaries are P4 and any ready P1/P2 outranks
  this batch. `math-ckd.6` (the `notes/summaries/README.md` index page) is the cheapest single item.
- **Last gate run (2026-10-12):** `bash notes/scripts/gate_driver.sh` — **rows 78, failures 0**, wall
  1 min 25 s. Reconciliations: 372 families, 719 manuscripts, **173** formalized (`formalized (yaml)`),
  242 scope notes, 416 challenges, 200 `main_results` over 189 configs, both `overview.tex` ↔
  `CONTENTS.md` cross-checks 0. `verify_cache_promotion.py`: `writers 14 + non-cached 1 probed targets
  15 problems 0`. Lint trio (`notes/scripts/lint_scripts.sh`) exits 0.
- **Push state:** `origin/notes` at `651b373c2`, pushed 2026-10-12. Nothing unpushed.
- **Queue check (2026-10-12):** `bd ready` lists **11** issues, no P1. P2: `math-8su` (mypy
  strict-probe backlog), `math-faz.3` + epic `math-faz` (moving the development pages), `math-el4.9` +
  epic `math-el4`, `math-u41`. P4: `math-ckd.5`, `math-ckd.6`, `math-ckd.3`, `math-ckd.4`, `math-ckd`.

## Loop shape

One parent agent, sequential. **No subagents** — the box is a single GPU and a subagent turn is a
context switch on the same model instance. **No cron job**: continuation is human-driven, and this file
exists because of context compaction, not unattended cadence. A batch is one bd issue.

Per page, in this order:

1. `bd update <id> --claim` (once per batch).
2. `ls` the manuscript root, and confirm the release still names it:
   `python3 notes/scripts/check_summary_manuscripts.py <page.md>`. A superseded dir is on disk, so `ls`
   alone cannot tell you the family no longer ships it.
3. Read the manuscript, the scope note, the YAML block, the challenge JSON, the trace if any.
4. Write the page in the format fixed by the skill, after reading `references/quotation-traps.md`.
5. Self-verify: every quotation against the lines it cites, every count against the file.
6. `python3 notes/scripts/verify_summaries.py` — zero problems. The mutants are in
   `notes/scripts/tests/test_summaries.py` (7 tests, run by the gate's `run_tests.py` row); the checker
   measures, the test file injects, and no checker carries a `--mutant` branch.
7. Declare every Sources row, or delete it. Paths are repo-relative and in backticks.
8. Regenerate the ledger; the `summary` column must flip to 1 for this family.
9. Commit.
10. `bd close <id> --reason "<outcome>"`, then `bd export -o .beads/issues.jsonl` before the commit
   that records it.

## Gates (run at every batch boundary, quote numbers only from this run)

```
bash notes/scripts/gate_driver.sh          # 78 rows, dependency order; expect rows 78 failures 0
python3 notes/scripts/verify_cache_promotion.py    # cached bytes == bytes on the tracked path
python3 notes/scripts/verify_summaries.py          # 0 problems over all pages
python3 notes/scripts/check_summary_manuscripts.py # 0 pages with an off-family manuscript
```

The twice-run byte diff is not the gate: a writer's bytes are asserted against the cache entry under
its digest key, which is stronger than two runs agreeing. The report's wall times make a byte-identical
diff of two gate runs impossible.

Reconciliation lines that must not move: 372 families, 719 manuscripts, **173** formalized, 242 scope
notes, 416 challenges, 200 `main_results` over 189 configs, both cross-checks 0. The discipline table
sums 372 / 242 / 719 / 173.

## Commit and push boundaries

Commit when a batch's gates pass: explicit paths, one purpose per commit, never `--no-verify`, never
`git add -A`. The beads store travels in the commit whose work it records (the pre-commit hook
re-exports and stages it); a pathspec commit excludes it, so export by hand and commit the store on its
own.

Push to `origin` (the fork) at a batch boundary, not on every commit — authorized 2026-10-07. The
cadence is a batching rule, not a timer: never idle to reach an interval. `upstream` is read-only;
confirm the destination with `git push --dry-run`.

## Stop and escalate

- **Stop the batch** when a gate fails twice on the same page. Two failures mean the checker or the
  format is wrong, not the page; fix that first, in its own commit.
- **Stop the run** when a P1/P2 issue becomes ready. Summaries are P4 and rank below them.
- **Never write an ungroundable page.** Record the family in the Decision points section below with
  the specific reason (what the sources do not state) and leave its `summary` row 0.
- **Ambiguity:** record the decision point below with the provisional choice and what would force a
  revisit, then keep going. If it is critical, or fixing it later means rewriting pages, claim a
  different bead and come back.

## Tiers (re-measured from the current ledger, 2026-10-12)

| Tier | Families | Manuscripts | Definition |
|---|---|---|---|
| A | 21 | 57 | 10 trace families, 9 headline T0, plus 001 and 032 (done) |
| B | 78 | 118 | remaining T0 families with `resolves_named = 1` (the union title∪abstract scope) |
| C | 273 | 544 | everything else, split 132 families / 273 manuscripts (combinatorics, differential geometry, number theory, probability and statistical mechanics, theoretical computer science) and 141 families / 271 manuscripts (the remaining twelve) |

Tier counts on the ledger: T0 130 / 244 manuscripts, T2 106, T3 136, T1 0. T0 with
`resolves_named = 1` is 86 families / 139 manuscripts; the 11 tier-A T0 families take 11 / 35, leaving
B at 78 / 118. A + B + C = 372 families and 57 + 118 + 544 = 719 manuscripts.

Trace families: 007, 017, 087, 102, 159, 197, 221, 271, 287, 362. Headline T0: 002, 004, 006, 010,
011, 014, 016, 018, 019.

## What not to re-derive

- Page format, citation grammar, the repo-relative File cell, the block-quote rule, the PDF/quote rule,
  the measured traps: `.qwen/skills/auto-skill-family-summary-citation-verified/`.
- Cost model: 001 (1 manuscript → 15 sources, 173 markers, 9 spans), 032 (8 manuscripts → 32 sources,
  272 markers, 52 spans), 087 (3 manuscripts → 43 sources, 268 markers, 11 spans), 159 (1 manuscript →
  25 sources, 99 markers, 47 spans), 362 (1 manuscript → 23 sources, 109 markers, 38 spans). Sources ≈
  4 per manuscript; a large Lean tree raises the source count at the same manuscript count.
- `bd ready` is the only task tracker; nothing here is a task list.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.

## Decision points

Provisional choices, with what would force a revisit. Not tasks — a revisit that needs work gets a bd
issue.

- **History/Consequences depth.** Pages carry these only when grounded in the manuscript, the scope
  note, or the trace. A prior-based framing is labelled as a prior. Revisit if a page reads as empty;
  the fix is `math-el4.6`, not invention.
- **Tier C order within a batch.** Chosen by ascending manuscript count. Revisit if the small families
  turn out to be the expensive ones.
- **Companion families.** A page cites its companion by number and links the companion's page when one
  exists; it does not duplicate the companion's content. Revisit if cross-linking starts producing
  circular sources tables.
- **Dated re-issues** (`versions > 0`). One page per family; the Sources table lists the manuscript
  tree, not each dated copy. Revisit if a re-issued manuscript differs in content.
- **Cadence.** No cron job and no self-paced loop: the user drives continuation, because this is a
  one-time run and the stated concern is losing context to compaction, not stalling. Revisit if the run
  outgrows a sitting — then arm a prompt-only `/loop` whose prompt points here and stops when
  `bd ready` has no P4 issue.
- **Strict-probe fixes: rename before annotate.** Chosen 2026-10-12 on `math-8su`: a finding that came
  from one variable bound to two types in one function is fixed by renaming, because a rename keeps the
  line count and a line-count change moves the `path:line` anchors the notes pages carry. Revisit if a
  future pass needs a real annotation and the anchor sweep has to be paid.
- **Shared guards go in `catlib/text.py`.** `first_group` / `first_match` return `""` when a pattern
  does not fire, so a checker reports a missing report line instead of crashing with AttributeError on
  the defect it is hunting. The file carries no page anchors, so appending to it is anchor-safe.
  Revisit if a checker needs a guard the two helpers cannot carry.
- **Push cadence.** Push at bead boundaries, not per commit: the standing grant is "push to git after
  every batch of commits (approximately one bead)". Revisit if a bead's work spans several sittings —
  then push at each commit batch, not at the bead close.
- **Move ordering: `.3` → `.4` → `.6` → `.5`.** Chosen 2026-10-12. `math-faz.3` moves
  `index-design.md` and `index-links.md` (and `build_index.py`'s 137 + 1 links to them), `math-faz.4`
  moves `names.md` and `topics.md` (552 + 2 links), and `math-faz.6` — the index TSVs into
  `notes/tables/` — sweeps those same pages, so sweeping each page once at its final path requires the
  page moves first. `math-faz.5` rewrites the entry point, which names all three directories, so it
  runs last. Revisit if a move is found to be independent of the index render.
- **The summaries index page is link-only.** `notes/summaries/README.md` is a page under
  `notes/summaries/`, so `verify_summaries.py`'s pass D and `check_summary_manuscripts.py` see it; pass
  D maps a page to the catalog by the family number in its **filename**, so a README reports
  `NO FAMILY NUMBER` as a problem. Chosen 2026-10-12: the page is checked for link resolution and
  exempted from the family-keyed passes, in the same commit as the page. It also grows the
  shared-basename set index ∩ summaries from **13** to **14** (`notes/index/README.md` exists), so the
  same commit re-targets `verify_script_ownership.py`'s shared-basename rule. Revisit if the page gains
  prose that needs a family-keyed check.
- **Blocked families go in this log, not a page.** Chosen 2026-10-12 on `math-faz.3`: the stop rule
  named `notes/summaries-blocked.md`, which was never created — `git log` on that path is empty, so the
  rule pointed at a page that does not exist. The rule now records the blocked family here with the
  reason and leaves its `summary` row 0. Revisit if the blocked set grows past a few families and a
  table is cheaper than prose.
- **A checker that reads every writer's cache needs every writer's artifact.** Chosen 2026-10-12 on
  `math-faz.3`: the first gate pass after the move printed `cache entry missing: seed_quotes.py
  notes/tables/quotes.tsv`, because `verify_cache_promotion.py` compares cached bytes with disk bytes
  for all 14 writers while its `needs` named only the artifacts that existed before `seed_quotes.py`
  and `refresh_summary_line_counts.py` had run. The row now names `quotes` and `summaries`, so it
  starts after both writers. The gate prints rows 78 failures 0. Revisit if a writer lands a tracked
  artifact outside the ten artifacts the row names — the race is invisible until a record key changes,
  which is exactly what a directory move does.
- **The basename pass is scoped to the two trees, not to the index alone.** Chosen 2026-10-12 on
  `math-faz.6`. The invariant the table move needs is that `notes/index/` and `notes/tables/` share
  no file basename. Inside the index tree, 6 discipline names are also topic terms, so
  `disciplines/X.md` and `topics/X.md` share a basename; a pass over the index alone would report
  those as collisions. Revisit if a page ever links a table by bare basename rather than by relative
  path — that is the only shape where an intra-tree duplicate becomes ambiguous.
- **`render_reports.py`'s L1 names `notes/tables/` as a tree, not the eight TSVs it used to name.**
  Chosen 2026-10-12 on `math-faz.6`. The writer opens all 25 TSVs once the 16 generated tables land
  there, and the audit-hook record names exactly that set, so a tree entry is the honest L1 and the
  expanded set matches the record. Revisit if the writer stops opening the tables it does not need.
- **Two fresh probe records replace the two that named the 16 TSVs under the pre-move path.**
  Chosen 2026-10-12 on `math-faz.6`. The read surface genuinely shrank (the writers no longer open
  the 16 TSVs under `notes/index/`), so retargeting the strings inside the old records would have
  made them claim reads the writers do not make; `measure_open_probe.py` landed
  `2026-10-12_rr_tables.txt` and `2026-10-12_measure_templates_tables.txt` and `PROBES` names them as
  the newest for those targets. Revisit if a move leaves the read set identical and only the path
  string changes — then retargeting is the right move, as `.3` did.
- **The ownership rule reads the whole writer target list, not the first target.** Chosen 2026-10-12
  on `math-faz.6`. `build_index.py` stages the index pages and the 16 tables, so the derived target is
  the tables directory; the writers table takes the sorted first target and the TSV rule reads the
  list, which is what makes the 16 rendered tables count as generated. Revisit if a script gains a
  third write target — the writers table then needs two cells.
- **The bead's acceptance figures were re-measured, not carried.** Chosen 2026-10-12 on `math-faz.6`.
  The body recorded `all_tsv_bytes 2172679` and the index tree at `11513879`; the re-render moved both
  to 2,174,703 and 11,529,933, so the acceptance criteria now quote the fresh report. Revisit whenever
  a bead's acceptance names a byte figure: quote it from a fresh generator report, never from the
  estimate recorded when the bead was written.
- **The command block's counts are re-measured from the scripts, not carried forward.** Chosen
  2026-10-13 on `math-faz.5`. The command block is literal template text, so the count pass never
  reads it and a drift is invisible until the render diff names the page line. Measured from the test
  files and the gate array: `gate.py` 78 rows (the page said 77), `test_index_links.py` 21 injected
  hrefs over 18 categories with 8 controls (was 20 injected, 7 real), `test_upstream_history.py` 14
  faults (was 13), `test_fleet_design.py` 20 faults (was 16), `measure_proof_density.py` 8
  corruptions (the command block and the body prose both said 9), and the move-surface probe after the
  reorg reads 0 top-level, 304 in the new dirs, 26 stable (was 282, 0, 16). Revisit whenever a test
  file gains a mutant or the gate gains a row — the drift is silent, so the sweep has to be paid.
- **The gate row classes are counted from the `ROWS` array, not from the writers table.** Chosen
  2026-10-13 on `math-faz.5`. The array carries 11 writer rows, 44 report-only rows, and 23 checker
  invocations. The writers table lists 14 writers, so the page's "10 gated writers / 45 report-only"
  was arithmetically right and factually wrong: four writers are not writer rows
  (`build_report_templates.py` and `measure_open_probe.py` are not in the list at all;
  `measure_names.py` and `extract_named_results.py` run as `--check-only` rows), and
  `refresh_summary_line_counts.py` is a writer row the table lists as a checker. Revisit if a writer
  gains a gate row — the class counts have to be re-derived from the array, not from the table.
- **The census page is edited in place; the entry point goes through the promote cycle.** Chosen
  2026-10-13 on `math-faz.5`. `notes/scripts/README.md` has no template in the registry (the registry
  is 19 report templates and 5 index templates), so its counts are edited directly and proven by
  `verify_script_ownership.py`. `notes/README.md` is template-fed, so its sweep is edit page → commit →
  `build_report_templates.py` → `render_reports.py` → prove `git status --porcelain` empty, and the
  template commit and the re-rendered `notes/development/templates.md` commit are part of the same
  batch. Revisit if the census page gains a template.
- **The not-checked line is a measured slot, so a band split belongs in the writer.** Chosen
  2026-10-13 on `math-el4.9`. The pairing page's not-checked bullet is the `sp_notread` slot, so the
  manuscript counts the bullet carries must come from `population()` — the remaining set is
  `multi - pop`, split at 3-4 and 5+ manuscripts — not from prose. A hand-edited slot line makes the
  builder report `NOT FOUND` against the recorded wrap, so the slot and its recorded prefix in
  `SP_SPLIT` are updated together, then the template is rebuilt from HEAD. Revisit if the remaining
  set is read: the bullet shrinks and the split moves.
- **A bead acceptance that names an inert flag is rewritten, not left.** Chosen 2026-10-13 on
  `math-el4.9`. The acceptance read `verify_subfinding_pairs.py --mutant` reports 0 problems with all
  mutants caught; the checker reads no argv, so the flag does nothing and the criterion was
  unsatisfiable as written. It now names the two rows that actually measure the page: the checker's
  0 problems and the extracted test file's 9 passing tests. Revisit when a bead is written for a
  checker that still carries its own mutant branch.
