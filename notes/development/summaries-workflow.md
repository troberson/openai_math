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
- **Pages done (24):** 001, 002, 004, 006, 007, 010, 011, 014, 016, 017, 018, 019, 032, 087, 101,
  102, 159, 197, 221, 226, 271, 287, 332, 362. The ledger's `summary` column is 1 for those; the
  generator reports "summary pages 24 of 372 families, 60 manuscripts behind them".
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
- **Band 2 is the same construction as band 1, so the rule keeps four conditions.** Chosen
  2026-10-13 on `math-el4.10`. The band is a manuscript-count window over the set the probe filter
  left, so `band2()` is 3-4 manuscripts and no probe word — 37 families, 119 manuscripts — and the
  population is the four-way union at 159 families over 468 manuscripts. The bead's own notes carried
  the split (37 at 3-4 = 119, 8 at 5+ = 46) and the measurement confirmed it; the handoff's 24/72 +
  21/111 did not. Revisit when band 3 is read: the rule gains a fifth condition or the remaining set
  closes.
- **A reading pass of this size is built by a verifier, not typed.** Chosen 2026-10-13 on
  `math-el4.10`. The 37 blocks were generated from a pair table under `.qwen/tmp/` that refuses to
  emit a block whose clause is not a verbatim substring of the parsed abstract or whose title is not
  the verbatim display title at that manuscript's seq. Typing 128 clauses and 119 titles by hand is
  where the U+2019 apostrophe errors came from in band 1. Revisit for band 3: the same shape, with
  more clauses per family.
- **A re-seed moves the byte figures the design pages quote, and the ledger set is the one that does
  not move.** Chosen 2026-10-13 on `math-el4.10`. `quotes.tsv` went to 333,196 B over 1,637 rows and
  the all-TSV sum to 2,228,751 B, but the ledger set stays 297,050 B because `quotes.tsv` is not one
  of the five TSVs `notes/development/index-design.md` tabulates. The two sums answer different
  questions, so sweep both with their own rule. Revisit when a re-seed touches one of the five.
- **Band 3 closes the population, and the band rule overlaps the named densest targets.** Chosen
  2026-10-13 on `math-el4.11`. Band 3 (`n >= 5` and no probe word) reads **17 families over 128
  manuscripts**, 10 of them already the bead's named densest targets, so the reading pass added **8
  families over 46 manuscripts**. The three bands together cover every multi-manuscript family, so the
  population is the whole multi set: **167 families, 514 manuscripts**. The noprobe slot must count band
  3 **minus** the densest targets, because the bullet names the densest separately — a naive
  `noprobe ∩ band3` read 14 where the correct disjoint count is 8.
- **A band block's pair lines are template slots fed by the quote table, so the re-seed must precede
  the template rebuild.** Chosen 2026-10-13 on `math-el4.11`. `render_reports.py` builds
  `sp_line_NNN_seq` from `notes/tables/quotes.tsv` rows parsed against the page, and the builder
  locates each slot's phrase in `git show HEAD:<page>`. A block that is not in HEAD has no slot, so the
  builder reports no NOT FOUND and the render silently drops the block: the template stayed at 159 blocks
  while the page had 167. Order is commit the page → re-seed → rebuild the template → render.
- **A generated page's row is committed before the builder can locate it.** Chosen 2026-10-13 on
  `math-el4.11`. `notes/development/templates.md` tabulates the template bytes, and the builder reads
  HEAD's page to build its template, so the row for a rebuilt template has to be committed first. The
  slot-count rule is `text.count("{{ ")` over the whole file, which includes the header comment's literal
  `{{ }}`, so the row carries 423 for a template the builder reports as 422 exprs.
- **The signalling-word filter's cost is measured, and it is the bulk of the page.** Chosen 2026-10-13
  on `math-el4.5`. The bead's "remaining 118 families / 311 manuscripts" is exactly the three bands
  minus the ten named densest targets. Reading it yields **141** accepted clause pairs, **118** headline
  pairs, **259** titles claimed, **52** unclaimed and **0** unmatched clauses — 141 of the page's 203.
  The families the filter left claim **83.2%** of their titles against the first pass's **53.7%**, so the
  probe vocabulary is not selecting the families that pair well; the ten densest targets are the outlier
  at 27%. Revisit if a new rule widens the population: the cost is a property of the filter, not of the
  page.
- **A prose needle names the mutated value, not the original.** Chosen 2026-10-13 on `math-el4.5`. The
  render-diff line reports the page's mutated line, so a needle keyed to the pre-mutation text never
  fires. The existing rejected-rule needle already names `(57)`, the value the mutation writes.
- **The FTS layer is cheap, and the TSV index is blunt exactly where the bead said it is.** Measured
  2026-10-13 on `math-u41.6` with `notes/scripts/build_index_db.py`: **8,007** `.tex` files
  (**135,108,224** B) plus the **372** abstracts build an FTS5 index of **8,379** rows in **1.65 s**,
  landing **202,760,192** B (193 MB) under the keyed record. Every probe term answers in under **1 ms**
  — `manifold` 727 hits, `eigenvalue` 666, `semidefinite` 325, `Schoenflies` 32, `Jiang-Su` 24,
  `Ricci flow` 22, `Laughlin` 12, `amenable` 61, `Landau-Siegel` 2, `Turan` 1. The index's four texts
  are title, abstract, scope note and derived Lean paths, so a body term is not reachable at all; the
  layer is worth recommending as routine. The wall times are a property of a run, not of the digest, so
  they are recorded here as a dated observation and the database stays untracked. Revisit if the corpus
  grows: the build is linear in bytes and the database is 1.5x the corpus.
- **The summaries index page is link-only, so the manuscript passes skip it.** Chosen 2026-10-13 on
  `math-ckd.6`. `notes/summaries/README.md` carries the coverage as four layers, a link per page, the
  cost model, the checker command and a Not checked ending. It names no manuscript directory and cites no
  family-keyed file, so `verify_summaries.py` skips pass D and pass E for a page named `README.md` and
  `check_summary_manuscripts.py` skips it entirely; passes B and C still run, so its links are checked.
  The shared-basename set grows to **14** because the index tree carries its own `README.md`, and the
  `seed_quotes.py` L1 (the summaries tree) needed a fresh probe record to name the new page.
- **A page that carries a quotation in a code span is a quotation.** Chosen 2026-10-13 on `math-ckd.6`.
  The summaries checker's pass C matched `scope: "Partial progress."` inside a backticked code span as a
  prose quotation needing a citation, and pass B read `<preprints-dir>` as stray HTML. A link-only page
  must carry neither angle brackets nor a quoted phrase.
- **`math-ckd.3`'s acceptance was re-measured, and its ordering rule is inert for this population.**
  Chosen 2026-10-13 on `math-ckd.3`. The acceptance read "All 83 pages pass `verify_summaries.py
  --mutant` with 0 problems and both mutants flagged"; the checker reads no argv, so the flag does nothing,
  and the page count is not 83. Measured from the current ledger: 86 T0 families with
  `resolves_named = 1` over 139 manuscripts, 8 of them already written (001, 004, 006, 011, 016, 018,
  019, 032), so the batch is **78 families over 118 manuscripts** and the tree ends at **99 family
  pages** plus the index page. The acceptance now names the checker's 0 problems, the 7 passing tests in
  `notes/scripts/tests/test_summaries.py`, the gate's 78 rows, and the cache assertion. The bead's
  ordering rule — "families with a scope note and with formalized manuscripts first" — selects nothing:
  every one of the 78 carries `scope_note 0`, `chal 0` and `paps_form 0`, because T0 is the tier with no
  Lean. Ordering inside a shard is by ascending manuscript count, the Tier C rule already recorded.
  Revisit if a family in this set gains a scope note, which means upstream formalized it and the tier
  moved.
- **The sweep family 101's page moved is landed, and the byte total is now measured.**
  Chosen 2026-10-13 on `math-ckd.3`. Family 101's page added one summaries page, so the
  census reads **23** pages (22 family pages), the seed probe classifies **990** spans
  (**922** raw-equal, **53** fold-equal, **15** not located, **314** single-line, **661**
  across 2 to 26 lines), the disk scan reads **66,108** links with **48,408**
  file-resolving, and the index tree carries **11,530,104** B over 1,033 pages. The head-rule
  probe re-measured: first-head-then-first-tail fails **6** of **754** pair-line specs
  (families 018, 114, 150, 247, 262, 336), shortest-span fails 0. The index-design checker
  gained the byte total as a measured count phrase (83 phrases, 15 mutants), the notes readme's
  four phrases became writer slots measured from the scan, the render report and the seed probe,
  and the index README template's baseline line was swept. Gate: **78 rows, 0 failures**, empty
  head diff, cache promotion 0 problems. `math-ckd.3`'s remaining set is **77 families over
  117 manuscripts**; the tree ends at **99** family pages plus the index page.
- **Family 226's page is landed and its sweep is landed; the needle list is the sweep's last surface.**
  Chosen 2026-10-13 on `math-ckd.3`. The page carries **48** marker positions and **30** quoted spans,
  `verify_summaries.py` reports **0** problems, and the tree reads **24** pages (**23** family pages)
  over **3,825** marker positions and **1,020** quoted spans with **0** problems. The counts the page
  moved are swept across the census (24 pages, 1,153 notes files, 15 probe records), the seed
  classification (1,020 spans: 949 raw, 56 folded, 15 not located, 324 single-line, 681 across 2 to 26
  lines), the disk scan (66,109 links, 48,409 file-resolving), the registry (48,014 links), the index
  tree (11,530,284 B), the all-TSV total (2,261,480 B over 25 TSVs), the pairings (23 of 372 families,
  59 manuscripts), the notes-doc targets (27), the family-page gap (949), and `quotes.tsv` (1,774 rows
  at 365,925 B). The lesson: a swept page is not enough. The writer's needle list, the hand-written
  index README template, and every mutant needle that keys on the swept figure must move in the same
  pass, because the builder locates the needle in HEAD, a render writes the template's literal back
  into the page, and a needle absent from the page is an inert mutant. `seed_quotes.py`'s tracked probe
  record also had to be re-taken: the L1 exactness pass compares the registry's summaries-tree entry
  against the newest record, and the record taken over 22 pages could not name the 23rd. Gate: **78
  rows, 0 failures**, empty head diff, cache promotion 0 problems. `math-ckd.3`'s remaining set is
  **76 families over 116 manuscripts**; the tree ends at **99** family pages plus the index page.
- **Family 332's page is landed and its sweep is landed.** Chosen 2026-10-13 on `math-ckd.3`, as the
  cheapest shard (Functional analysis, 1 manuscript). The page carries **35** marker positions and
  **18** quoted spans, `verify_summaries.py` reports **0** problems across passes B, C, D and E, and the
  tree reads **25** pages (**24** family pages) over **3,860** marker positions and **1,038** quoted
  spans with **0** problems. The counts the page moved are swept across the census (25 summaries pages,
  1,155 notes files, 16 probe records), the seed classification (1,038 spans: 966 raw, 57 folded, 15 not
  located, 335 single-line, 688 across 2 to 26 lines), the disk scan (66,110 links, 48,410
  file-resolving), the registry (48,015 links), the index tree (11,530,406 B), the all-TSV total
  (2,265,274 B over 25 TSVs), the pairings (24 of 372 families, 60 manuscripts), the notes-doc targets
  (28), the family-page gap (948), the typed-edge summary row (24), and `quotes.tsv` (1,792 rows at
  369,719 B). Two facts the page records: the release's blurb and the overview both say the extension
  reaches "the whole space", while the manuscript abstract names "the whole Hilbert space" — the page
  quotes each in its own words. And the blurb writes the target with the Unicode `ℓ1`, so a page that
  quotes `$\ell_1$` is not verbatim. Gate: **78 rows, 0 failures**, empty head diff, cache promotion 0
  problems. `math-ckd.3`'s remaining set is **75 families over 115 manuscripts**; the tree ends at
  **99** family pages plus the index page.

- **Pages are generated, not hand-swept.** Chosen 2026-10-13: the builder builds each template from
  `git show HEAD:<page>`, so a slot's number in HEAD is the previous measurement, and a needle matched
  on its exact number is NOT FOUND once a count moves — the template keeps HEAD's literal and the render
  writes that literal back, which is the manual sweep. `catlib.text.flex` now relaxes digit runs, and
  `apply_split` matches a line-break prefix flexibly and emits the measured span. Two constraints the
  first version violated, measured on the pages: a needle relaxes its digits only when it carries at
  least two literal characters and only for runs whose neighbours are not letters (the bare "719" needle
  matched "A 2-line ... 40-line construction"; "631M" matched "1740M" and "12M"), and a needle that
  fires on more than one distinct span is left literal and reported as a weak needle, because a slot is
  one place in the page. Revisit when the weak-needle list is non-empty: the fix is widening the writer's
  label value, not loosening the matcher.

- **The two Theoretical CS pages close the shard, and the sweep found two real defects.** Landed
  2026-10-13: families 109 (*Integer multiplication below $n\log n$*) and 136 (*The quasilinear
  PCP-for-PPAD conjecture*), one manuscript each. The tree moves 25 family pages to 27, the ledger's
  summary column to 27 families / 64 manuscripts, `quotes.tsv` to 1,906 specs, and the index gains two
  summary-pairing links (66,113 links, 48,413 file-resolving, 2,294,676 B over 25 TSVs, 11,530,829 B
  index tree). Two defects the sweep exposed, both fixed: the README's per-family page count had no
  writer label, so the render could not move it — it is a label now; and the fleet-design byte figure
  was a weak needle (a bare number plus "bytes" matched every `**N** bytes` phrase in HEAD's page), so
  the label gained the `cat notes/tables/*.tsv | wc -c` command that makes it one span. The weak-needle
  list is **not** empty: the builder reports weak needles for the table-row labels in
  `index-links.md`, `names.md`, `proof-density.md`, `subfinding-pairs.md`, `topics.md`,
  `verification-dirs.md`, `dependency-drift.md`, `abstracts.md` and `fleet-design.md`. Those rows are
  rendered from the writer, so HEAD's literal equals the measured value and the render is byte-identical;
  a future drift in one of them will not land, and the fix is widening the label, per the rule above.
  The lint trio was **not** green at HEAD as AGENTS.md claims: 16 ruff errors and one pylint
  redefinition, the load-bearing one being `build_report_templates.py` initializing `ambiguous` twice,
  so the second initialization wiped the weak-needle list the first collected and the builder printed 0
  for a page that had weak needles. All 17 are fixed; the driver exits 0 for all three tools. Gate:
  **78 rows, 0 failures**, empty head diff, cache promotion 0 problems, `verify_page_sync.py --both` 0
  problems with 5 of 5 mutants caught. `math-ckd.3`'s remaining set is **72 families over 111
  manuscripts**; the tree ends at **99** family pages plus the index page.

### 2026-10-13 — The group-theory page for 259 lands, and the sweep finds a stale list

The shard is Group theory, the bead's cheapest remaining. Family 259 (one
manuscript) is written first; family 258 (two manuscripts) is not yet read.

**The read_file line numbers are one below the checker's.** `verify_summaries.py`
resolves a marker against `len(text.splitlines())`, and `read_file` labels the same
line one lower for these manuscript files — its count includes the trailing newline.
Six markers were retargeted after the first verification run, and two quotations
were fabricated from truncated shell and `read_file` dumps: the planar lemma's
opening, the CONTENTS blurb's `rank $100$` (the release writes `rank 100`), and the
overview abstract, which says "answering the general fixed-price problem
negatively", not "giving a negative answer to Gaboriau's general fixed-price
problem". The rule the batch re-learned: quote only from a printed `splitlines()`
dump, and retarget every marker to that numbering. The page is green at 88 marker
positions, 32 quoted spans, 0 problems.

**The summaries index list was stale by seven pages.** `notes/summaries/README.md`
listed 21 pages while the tree held 28: 101, 109, 136, 147, 226, 259, 332 were
added by earlier batches that swept the counts but not the list. The list now
carries all 28 in discipline order and every link resolves. This is the sweep the
bead's body now names as part of each batch.

**A new page needs a fresh audit-hook record.** `seed_quotes.py`'s L1 names every
summaries page, so the new page made the registry's L1 wider than the newest record
naming the target; `verify_cache_promotion.py` reported the drift as
`registry names [the page]`. The re-probe lands
`notes/development/probe/2026-10-13_seed_quotes_259.txt`, which names the page in
its `notes/` bucket, and the checker takes it as the newest record for that target.
The tracked records move 18 to 19.

Counts the page moved: ledger summary column 27/64 → **28/65**; summaries tree 28 →
**29** files; `notes/` total 1,160 → **1,162**; index links 66,113 → **66,114** with
file-resolving 48,413 → **48,414**; all-TSV 2,294,676 → **2,301,027** B; index tree
11,530,829 → **11,530,936** B; `quotes.tsv` 1,906 → **1,938** specs. Six test pins
retargeted: the page count, the link and byte figures, the probe record count, the
quote population, and the ownership needle. Gate: **78 rows, 0 failures**, empty head
diff, cache promotion 0 problems, lint trio 0/0/0. `math-ckd.3`'s remaining set is
**71 families over 110 manuscripts**; the tree ends at **98** family pages plus the
index page.

### 2026-10-13 — Six pages named files without links; the Sources header has seven forms

The user noticed that some summary pages' file names are links and others
are not. Measured over the 28 family pages: **22** pages had every
Sources-table File cell as a backticked repo-relative path **with** a
relative href; **6** pages (109, 136, 147, 226, 259, 332 — the last three
batches) had the backticked path and **no href**, 62 rows in total, and
families 109 and 136 carried no markdown link anywhere on the page.

The skill fixes both rules, so the 22-page form is the authoritative one:
"Write every File cell as a repo-relative path, in backticks" **and**
"Every row gets a link, built with `os.path.relpath(target, page_dir)`".
The fix is mechanical — the paths were already repo-relative, so the href
is computed from the page directory. Two assertions: the target is on
disk, and the href carries no parenthesis, because `LINK` in
`catlib/summaries.py` is `]\(([^)\s]+)\)` — **not paren-balanced** — so a
path like `Sharp-integral-fillings-in-CAT(0)-spaces` would be truncated
into a reported dead link. No cell in the six pages has a parenthesis.

Pages with every source row linked: **22 → 28**. Markdown links in the
family pages: **706 → 768**. `verify_summaries.py` reports 0 problems on
all 29 pages; the gate runs 78 rows with 0 failures.

**Left open, not fixed:** the Sources-table header row has **seven** forms
across the 28 pages — first label `ID` (16), `#` (4), `S#` (3), `Src` (2),
`Source` (1), and last label `Role` (18), `What it carries` (7), `What it
is` (3). The skill fixes `| # | File | Lines | Role |`, which **4** pages
use. No checker parses the header, so normalizing it is a formatting pass
the user has not asked for.

## The group-theory page for 258 lands, and the sweep finds two stale figures

Family 258 — *Gersten's conjecture for one-relator groups* — is the second
Group theory page, so that shard is complete. The two manuscripts cite each
other: the hyperbolicity paper's `references.bib:295` names the specialness
paper, and the specialness paper's `references.tex:356` names the hyperbolicity
paper. The measured `.bib` layer records **1** intra-family edge, not 2,
because the second manuscript ships a `\bibitem` list, not a `.bib` file — the
known bibliography-shape trap, and the page states both directions.

**The overview anchor carried in the handoff was wrong.** The handoff recorded
`overview.tex:296` for family 258; that line is family 109's `\resultentry`.
The real anchor is **`overview.tex:603`**. A handoff anchor is a transcription,
not a measurement: locate the entry by its family key before quoting it.

**Two recorded figures were not reproducible.** The summaries README carried
**69** manuscript directories for the 28-page tree. The rule that yields the
12.4 MB LaTeX figure — the directories named by the pages, all `.tex` under
them — gives **65** for that tree, so 69 was a transcription error in the
previous sweep, not a different rule. Re-measured for 29 pages: **67**
directories, **13.2 MB**. The script census carried **17** shared page slugs;
the checker's intersection includes `README.md`, which each tree carries as its
own entry point, so the figure is **18**.

**A new page moves the coverage-signal framing.** `notes/reports/t0-chains.md`
says "no coverage signal" holds for 25 of the 27 second-pass families. The
signal includes the summary flag, so adding a page for 258 moves it to **24**,
and the exceptions are now 147, 258 and 268. `verify_findings.py` carries that
phrase as a needle in its records pass, so the needle retargets in the same
pass as the page.

Page: **30** declared sources, **179** marker positions, **59** quoted spans,
**0** problems. Tree: **29** family pages, **6,028** lines, **4,414** marker
positions, **1,243** quoted spans, median **21** sources, checker **1.14 s**.
Index links **66,114 → 66,115**, file-resolving **48,414 → 48,415**; all-TSV
**2,301,027 → 2,316,386** B; index tree **11,530,936 → 11,531,073** B;
`quotes.tsv` **1,938 → 1,997** specs; probe records **19 → 20**. Six test pins
retargeted. The gate runs **78** rows with **0** failures, the head diff is
empty, and the promote-and-verify assertion is green.

## The padded-table mutant lands, and the needle turns out not to be the discriminator

The question was whether a table-parsing checker can silently skip a table.
Measured: **14** pipe-anchored row patterns over **8** checkers, all tolerant
of padded cells after this pass. **7** of the 8 are table-row parsers and each
carries a guard that fires when rows are missing; `verify_summaries.py`'s
pattern is a family-block key rule, not a table parser, and has no row-count
guard. The real gap was narrower: the two t0-chains patterns required exactly
one space after each pipe, and **none of the 9** table-row mutants in the four
test files that carry them exercised padding.

`SUM_ROW` and `CHAIN_ROW` in `verify_t0_chains.py` now tolerate whitespace
around every cell. The first widening broke `CHAIN_ROW`: joining the seven
digit groups with `\s*\|\s*` left no `\s*` after the pipe closing `(T\d)`, so
the chain table read 0 rows on the clean page. The prefix has to end with
`\|\s*` too.

**The needle is not the discriminating assertion.** The padding mutant's needle
is the render-diff line, and the render diff fires against the pre-fix pattern
too — the padded page differs from the writer's render either way. I confirmed
the new tests fail against the pre-fix code by swapping in `git show HEAD:`'s
version: the padded page read **0** summary rows and **0** chain rows, against
**27 / 5** after the fix. The row-count test is what distinguishes the two
patterns; the needle alone would have printed a pass on the unfixed code. A
needle that fires for the fixed and the unfixed code cannot prove the fix, so
the padding fault carries a second test.

**The retarget burden is the measured cost of a page-line needle.** The sweep
added three lines to the page's checker section, and five needles moved by
three: the paraphrase quote 378→381, the title swap 367→370, the out-of-range
anchor 70→73, the fenced block 96→99, and the padded-table render line 51→54.
The findings Sources row declares the page's length, so S12 moved 541→544.
Nine hand-measured values for one paragraph edit — this is the number the
runtime-derived-needle pass is meant to remove.

**AGENTS.md carried a stale coverage-signal figure.** It read **26** families
with zero coverage signal; the fresh `extract_t0_chains.py` report reads **24**
with **3** exceptions (147 258 268), the figure the page carries after family
258's page landed. The `companion_word` figure (9 families, 0 edges) checks out.

Gate **78** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**; `test_t0_chains.py` **16** tests pass. Pushed to
`origin` at `c71c4c12b..1922ea951`.

Not checked: the padding mutant exists only for `verify_t0_chains.py`. The
other **6** table-row parsers are tolerant of padded cells but no mutant
exercises that, and `verify_summaries.py`'s block-key rule has no row-count
guard. The **110** numeric needles and the **184** clean-test corpus literals
were untouched at this point; phase 1 has since started, on that file.

## Phase 1 pilots on `test_t0_chains.py`, and the layout shift is the test

Every needle in that file is now a function of the mutated page and the
checker's cached `population()`: the page line is found in the mutated text,
the ledger tier and the recomputed citation-layer triple come from the
population, the count phrases come from `count_phrases()`. The runner accepts
a needle as a string **or** a callable, so the 22 structural needles stay as
strings.

**The discriminating measurement is a layout shift.** Inserting two lines into
the page in memory and running all 14 faults: the literal needles break on
**6** faults, the derived needles break on **0**. That is the property the pass
buys — a needle that quotes a page line is re-measured by hand every time the
page's layout moves, and the padded-table sweep had just shown that.

Numeric literals in the needles go **46 → 21**. The 21 that remain are the
mutation's own inputs — a family id, the value the mutation writes, a date
inside a manuscript path — not measured corpus figures.

Two derivations needed care. The fenced-block needle keys on the **opening
fence**, not the mutated line inside the block, because the pass reports the
fence line (measured: the mutated line is 103, the pass names 99). The quote
needle keys on the mutation's own byte plus the anchor on the same line,
because the prose the page repeats is not unique — the first version of the
title-swap needle asserted on a substring that appears on two lines.

Specificity is re-measured, not assumed: **0** needles fire on another fault's
page, **0** fire on the clean page. Gate **78** rows, **0** failures; head diff
empty; promote-and-verify assertion green; lint trio **0 / 0 / 0**. Pushed to
`origin` at `f67ac3d1b..9935c6761`.

Not checked: the **11** other test files that carry numeric needles are
untouched — `test_fleet_design.py` **19**, `test_index_design.py` **15**,
`test_faithfulness.py` **15**, `test_verification_dirs.py` **15**,
`test_counterexample_crosscheck.py` **14**, `test_script_ownership.py` **12**,
`test_sources.py` **12**, `test_upstream_history.py` **12**,
`test_named_results.py` **8**, `test_conditional.py` **6**,
`test_findings.py` **4**. The **184** clean-test corpus literals are untouched
— phase 2 has not started, and the pilot's own clean pins
(**120, 3, 61, 12, 0** and **27, 5, 27, 54, 4, 2**) are still literals.

## Phase 1 takes two more files, and the census is promoted

`test_findings.py` and `test_conditional.py` now derive their needles. In
findings, the ledger-count needle is the tier phrase `needles(measured())`
builds and the aged-line needle is the targeted row's real file length minus
one; the mutation is derived too, so `shift_tier` moves the counts the measured
phrase carries. In conditional, every needle asks the checker's own
`nearest_anchor` rule which anchor the pass attributes the mutated block, quote
or citation to. Recorded numeric needles go **4 → 0** in each file. Specificity
re-measured: **0** cross-fires, **0** needles firing on the clean page, and a
two-line layout shift breaks **0** needles in both files.

`measure_needles.py` is promoted to a gated report-only row, because phase 1
spans 11 files and the census is re-run at each step. Its baseline: **213**
faults, **160** recorded needles (**92** numeric, **68** structural), **53**
derived, **309** clean pins. The derived/recorded split is the honest progress
metric — the digit count inside a needle expression includes the strings a
derivation uses to locate its mutation, so counting digits overstates what a
needle records.

The sweep moves: scripts **67 → 68**, report-only **30 → 31**, write-nothing
**52 → 53**, non-importers **7 → 8** (the census parses test files with `ast`
and reads no corpus), gate rows **78 → 79**, the naming sentence to **34** of
**68**, and the gap list gains the census. The fleet pins retarget: scripts
**66 → 67**, gate rows **78 → 79**; the atomicity and writer censuses are
unaffected, because the new script imports no catlib and carries no write call.

**The trap is the generated page.** `notes/README.md` is rendered from a
template built at HEAD, so running `render_reports.py` before the commit
reverted the command-block edit and the commit landed 5 of the 6 staged files.
The re-applied edit had to be committed, then the template rebuilt from HEAD,
then the page re-rendered.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**. Pushed to `origin` at `a851febcf..fcb39763a`.

Not checked: **10** files still carry recorded numeric needles —
`test_fleet_design.py` **20**, `test_index_design.py` **15**,
`test_faithfulness.py` **15**, `test_verification_dirs.py` **14**,
`test_counterexample_crosscheck.py` **14**, `test_sources.py` **12**,
`test_named_results.py` **10**, `test_dependency_drift.py` **10**,
`test_citations.py` **9**, `test_subfinding_pairs.py` **9**,
`test_proof_density.py` **8**. Phase 2 (invariants for the **309** clean pins)
and phase 3 (synthetic rule tests) have not started.
