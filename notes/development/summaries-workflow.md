# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction: it is the state carrier,
so it states what to do and what not to re-derive. The method (page format, citation grammar, the
measured quotation traps) lives in `.qwen/skills/auto-skill-family-summary-citation-verified/` —
`references/quotation-traps.md` carries the 21 shipped pages' defects.

## Current state (rewritten at every batch boundary, 2026-10-14)

- **All 39 pages are green.** `verify_summaries.py` over the 40 files in `notes/summaries/`:
  **5,638 marker positions, 1,511 quoted spans, 0 problems**; `check_summary_manuscripts.py`:
  **40 pages, 0 with an off-family manuscript, 86 manuscript dirs named, 0 unnamed-on-catalog,
  0 named-by-another-family**; 749 preprint dirs on disk, 719 named by `overview.tex`, 30 on disk
  and unnamed, 0 named and absent. `test_summaries.py`: **11 tests pass**.
- **Pages done (39):** 001, 002, 004, 006, 007, 010, 011, 014, 016, 017, 018, 019, 032, 087, 101,
  102, 109, 136, 147, 159, 197, 221, 226, 258, 259, 271, 287, 332, 334, 342, 344, 345, 346, 347,
  348, 349, 351, 352, 362. The ledger's `summary` column is 1 for those; the generator reports
  "summary pages 39 of 372 families, 86 manuscripts behind them". By discipline: Number theory 12,
  differential geometry 10, theoretical computer science 3, convex and metric geometry 2, probability
  and statistical mechanics 2, group theory 2, and one each in algebraic and complex geometry,
  dynamical systems and ergodic theory, combinatorics, algebra, mathematical physics, operator
  algebras, functional analysis, and partial differential equations.
- **Next batch:** `math-ckd.4` is claimed and in progress — tier C group 1. The differential-geometry
  families with `summary = 0`, sorted by `paps`: 353, 354,
  355, 356, 357, 358, 359, 360, 361, 350. Steps 1–10 per page. Check `bd ready` first: summaries are
  P4 and any ready P1/P2 outranks this batch.
- **Last gate run (2026-10-14):** `bash notes/scripts/gate_driver.sh` — **rows 71, failures 0**, head
  diff 0 bytes. Reconciliations: 372 families, 719 manuscripts, **173** formalized (`formalized
  (yaml)`), 242 scope notes, 416 challenges, 200 `main_results` over 189 configs, both
  `overview.tex` ↔ `CONTENTS.md` cross-checks 0. `verify_cache_promotion.py`: **writers 15 +
  non-cached 1, probed targets 16, problems 0**. `check_index_links.py`: **1,033 pages, 66,125
  links, 0 broken**. Lint trio (`notes/scripts/lint_scripts.sh`) exits 0.
- **Push state:** `origin/notes` at `d53d60b50`, pushed 2026-10-14, through the family 351 batch —
  the family 351 page, its count sweep, the retargeted needles in the quotes, index-design,
  script-ownership and fleet tests, the links sweep, and the index link count on top. The gate run
  reported **71 rows, 0 failures** with a **0-byte** head diff, and the linters exit 0.
- **Queue check (2026-10-14):** `bd ready` lists **3** issues: `math-4nn` (the epic, open through
  `.2`, whose prettier decision is the user's), `math-ckd.5`, and `math-ckd`. `math-ckd.4` is
  claimed and in progress, so it is not in the ready list.

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

## Phase 1 takes `test_proof_density.py` and `test_subfinding_pairs.py`

`test_proof_density.py` derives its row-count, proofs-sum, thms-sum and tier
needles from the committed TSVs and the mutated rows; recorded numeric needles
go **6 → 3**, the 3 that stay being structural messages whose count is the
fault's own shape. `test_subfinding_pairs.py` derives its block-header line from
the mutated page and its Summary-table value from the checker's own `measured`
dict; recorded numeric needles go **7 → 4**.

The census moves: recorded needles **160 → 149**, numeric **92 → 81**, derived
**53 → 64**, needle digits **309 → 259**, clean pins **309** unchanged. The
census is the progress metric, and it is the reason the script was promoted.

Two derivation traps, both caught by the uniqueness check rather than by a
silent pass. The subfinding-pairs pass reports the **clause line**, not the
block header, so the needle keys on the clause line. And the borrowed id `010:3`
already exists in family 010's block, so the locating sub has to carry the
clause's closing text — a sub appearing on two lines makes the derivation
assert, which is the loud failure the check is built for.

Specificity re-measured in both files: **0** cross-fires, **0** needles firing
on the clean population. Gate **79** rows, **0** failures; head diff empty;
promote-and-verify assertion green; lint trio **0 / 0 / 0**. Pushed to `origin`
at `c65f2c6e2..077534245`.

Not checked: **9** files still carry recorded numeric needles —
`test_fleet_design.py` **20**, `test_index_design.py` **15**,
`test_faithfulness.py` **15**, `test_verification_dirs.py` **14**,
`test_counterexample_crosscheck.py` **14**, `test_sources.py` **12**,
`test_named_results.py` **10**, `test_dependency_drift.py` **10**,
`test_citations.py` **9**. Phase 2 and phase 3 have not started.

## Phase 1 takes `test_citations.py`, and the block anchor is read from the page

Sixth file. Seven of its nine needles carried a corpus count: the pair-layer
phrase `| ≥5 | **419** | 296 | **6** |`, the headline crossing count, the
cluster membership, the cluster composition, the work count, the release-target
count, and the block anchor. All seven are rebuilt at run time from the
checker's own `measure()` dict — the pair phrase from `M["pairs"]` with the
`**` bolding rule the pass applies at threshold ≥5, the crossing count from the
discipline map, the cluster membership and composition from the **same index**
of the top-12 ≥5 list the pass zips the table against, the work count from
`M["inv"]` through `norm_title`, the release count from the top-10 release
targets.

The block-line needle is the interesting one: the pass attributes a fenced block
to the **last** `preprints/...bib:line` anchor above it, so the needle reads that
anchor out of the mutated page. A band shift moves the anchor with the layout and
the needle moves with it. Two needles stay literal, and they are the mutation's
own inputs — the invented anchor path and the anchor line moved by one. That is
the rule, not an exception: a needle whose value is what the mutation wrote has
nothing to be derived from.

Measured: the layout shift breaks **0** of the 9 needles; specificity **0**
cross-fires; **0** needles fire on the clean page. Recorded numeric needles in
the file **9 → 2**.

The census moves: recorded needles **149 → 142**, numeric **81 → 74**, derived
**64 → 71**, needle digits **259 → 231**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**. Pushed to `origin` at `e8fde07f4..a3e9aa940`.

Not checked: **8** files still carry recorded numeric needles —
`test_fleet_design.py` **20**, `test_index_design.py` **15**,
`test_faithfulness.py` **15**, `test_verification_dirs.py` **14**,
`test_counterexample_crosscheck.py` **14**, `test_sources.py` **12**,
`test_named_results.py` **10**, `test_dependency_drift.py` **10**. The **309**
clean pins are still literals (phase 2), and there is one synthetic-rule test
file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_fleet_design.py`, and a fault must not disturb a needle it is not testing

Seventh file. Seventeen of its twenty needles carried a page count: the atomicity
count, the sync split, the purity heading count, the digest count, a probe figure,
the TSV byte sum, the probe-record count, the writer-row count twice, the TSV file
count, and the six site anchors. All are rebuilt at run time — the counts from the
checker's own `population()` dict, the site needles from the paragraph the checker
scans **in the mutated page** plus the measured site set, the purity needle from the
mutated page's own table rows against the probe parse, and the render needle from
the mutated page's line number plus the clip the render diff prints. Three needles
stay literal: the anchor line written past the file's end, the injected notes-page
anchor, and the dated observation's new value.

The first probe run reported **1** cross-fire, and it is the general lesson: the two
anchor-outside faults moved `render_reports.py:1180`, which is the measured env
**site**, so the env-bullet needle fired on pages those faults were not testing. A
fault must not disturb the byte a needle reads. The faults now move
`render_reports.py:2043`, an anchor that is not a measured site, so the anchor pass
is the only pass that fires.

Measured: the layout shift breaks **0** of the 20 needles; specificity **0**
cross-fires between faults. Recorded needles in the file **20 → 3**.

The census moves: recorded needles **142 → 125**, numeric **74 → 58**, derived
**71 → 88**, needle digits **231 → 211**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**. Pushed to `origin` at `a3e9aa940..68a79b268`.

Not checked: **10** files still carry recorded needles — `test_index_links.py`
**21**, `test_faithfulness.py` **15**, `test_index_design.py` **15**,
`test_verification_dirs.py` **14**, `test_counterexample_crosscheck.py` **14**,
`test_sources.py` **12**, `test_dependency_drift.py` **10**,
`test_named_results.py` **10**, `test_fleet_design.py` **3**,
`test_abstracts.py` **1** — **58** of them numeric. The **309** clean pins are
still literals (phase 2), and there is one synthetic-rule test file
(`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_dependency_drift.py`, and `test_index_design.py` turns out to need nothing

Eighth file. Nine of its ten needles carried a page count: the patch-line total,
the phase count, the ordering-violation count, a table row, the zero-import name
list, the omitted table row, the blockquote anchor, the code-span page line, and
the render-diff line. All are rebuilt at run time — the counts from the checker's
own `measure()` dict, the table needle from the mutated page's row against the TSV
value, the name-list needle from the checker's own `name_list()` read of the
mutated page, the omitted-row needle from the measured patched set minus the
mutated table, the blockquote needle from the anchor the mutated blockquote
carries, the code-span needle from the page line the mutated span sits on. One
needle stays literal: the anchor line written out of range.

`test_index_design.py` was next on the list and needs **nothing**: its 15 needles
are pass labels (`count mismatch (population totals)`) plus mutation inputs. A
label needle names the pass that owns the fault, not a corpus figure, so there is
no recorded count to derive. The census counts it as 15 recorded strings, which is
the census's blind spot — it counts needle *form*, and a label needle is a string.
The honest reading is that the file is already phase-1 shaped.

Measured for the drift file: the layout shift breaks **0** of the 10 needles;
specificity **0** cross-fires. Recorded needles in the file **10 → 1**.

The census moves: recorded needles **125 → 116**, numeric **58 → 51**, derived
**88 → 97**, needle digits **211 → 201**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**. Pushed to `origin` at `4916f6724..4d9f06eaa`.

Not checked: **9** files still carry recorded needles with numeric values —
`test_faithfulness.py` **10**, `test_verification_dirs.py` **6**,
`test_counterexample_crosscheck.py` **6**, `test_named_results.py` **5**,
`test_sources.py` **4**, `test_index_links.py` **3**, `test_fleet_design.py` **3**,
`test_index_design.py` **1**, `test_abstracts.py` **1** — **51** numeric in all.
The **309** clean pins are still literals (phase 2), and there is one synthetic-rule
test file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_faithfulness.py`, and a table needle must key on the row it mutated

Ninth file. Thirteen of its fifteen needles carried a page count: six count
phrases, three table needles, the block anchor, the quote anchor, and the two
needles that stay literal (the carrier-rule wording and the comparator-sorry
prose line, both written by the mutation). The counts are rebuilt from the
checker's own `population()` dict, the table needles from the mutated page's rows
against the recomputation, the block needle from the anchor the mutated page
attributes the block to, the quote needle from the anchor the mutated quote line
carries.

The first probe run reported **2** cross-fires, and the cause is the pass's own
message structure: the `a.e.` table pass reports the length difference for **any**
table difference, so a length needle fires for both the deleted-row fault and the
shifted-count fault; and deleting a row shifts every row after it, so a
first-mismatch needle fires for both as well. The fix is to key each needle to the
row the mutation touched — the count needle to the mutated row's own mismatch, the
deletion needle to the recomputation row for the deleted family. After that, 0
cross-fires.

Measured: the layout shift breaks **0** of the 15 needles; specificity **0**
cross-fires. Recorded needles in the file **15 → 2**.

The census moves: recorded needles **116 → 103**, numeric **51 → 45**, derived
**97 → 110**, needle digits **201 → 188**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**. Pushed to `origin` at `c7d364f27..d5dc32066`.

Not checked: **8** files still carry recorded needles with numeric values —
`test_verification_dirs.py` **6**, `test_counterexample_crosscheck.py` **6**,
`test_named_results.py` **5**, `test_sources.py` **4**, `test_index_links.py` **3**,
`test_fleet_design.py` **3**, `test_index_design.py` **1**,
`test_abstracts.py` **1** — **45** numeric in all. The **309** clean pins are still
literals (phase 2), and there is one synthetic-rule test file (`test_quotes.py`)
against 14 checkers (phase 3).

## Phase 1 takes `test_verification_dirs.py`, and two block faults share a block

Eight needles are rebuilt from the checker's own phrase builders: `count_phrases()`,
`ledger_phrases()` and `entry_phrases()` applied to the measured population, the
measured ledger claims and the measured entry recomputation. The two table needles
read the mutated page's own rows against the recomputation — the family-order needle
keyed to the row the mutation touched, the omission needle to the row count the
pass compares. The quote needles re-run the checker's anchor-selection rule on the
mutated page: the anchor in the quote's line, else the first anchor in the four
lines below it. The prose quote's anchor is on the **line after** the quote, so a
needle that read the anchor from the quote's own line had nothing to read.

**The two block faults sit in the same fenced block.** A needle that scans every
block and returns the first mismatch is the same function for both faults, so both
needles fired for both faults. The fix is to key the needle to the byte the mutation
touched — the shifted anchor, or the altered block line — which selects the block
the pass is reporting. After that, 0 cross-fires.

Measured: the layout shift breaks **0** of the 19 needles; specificity **0**
cross-fires; **20** tests pass. Recorded needles in the file **14 → 2**, numeric
**6 → 1**.

The census moves: recorded needles **103 → 91**, numeric **45 → 40**, derived
**110 → 122**, needle digits **188 → 181**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**.

Not checked: **7** files still carry recorded needles with numeric values —
`test_counterexample_crosscheck.py` **6**, `test_named_results.py` **5**,
`test_sources.py` **4**, `test_index_links.py` **3**, `test_fleet_design.py` **3**,
`test_index_design.py` **1**, `test_abstracts.py` **1** — **40** numeric in all. The
**309** clean pins are still literals (phase 2), and there is one synthetic-rule test
file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_counterexample_crosscheck.py`, and a first-mismatch needle cross-fires

Eleven needles are rebuilt: the three table needles read the mutated page's own rows
against the recomputation, the three block needles read the anchor the mutated page
attributes the block to and the block line the mutation touched, the two quote needles
read the anchor on the line the quote starts on, and the statement needle reads the
true statement line from the file, so it reports the anchor the page no longer
carries rather than the line the page now names. Three needles stay literal — the
invented anchor file, the `sorry` label, the prose denominator label.

**A needle that reports the first mismatch cross-fires when two faults share a pass.**
The summary pass reports the first row that differs, so a first-mismatch needle built
from the mutated page gives the same string for the tier fault and the config-count
fault. Keying it to the family the mutation touched makes each fire for its own row.
The two carrier-block faults cross-fired for a second reason: the paraphrased line
`Nonempty (A ≃ₐ[ℂ] …)` is a substring of the line it was paraphrased from
(`¬ Nonempty (A ≃ₐ[ℂ] …)`), so the paraphrase needle found the word fault's page
too. Keying to the block line the mutation touched fixes both.

Two derivations needed the checker's own byte conventions: the population stores the
Lean path **without** the `lean/` prefix, so the needle must add it once, not twice;
and a quote wraps across page lines, so the mutated word is not always on the line
the anchor sits on — the needle is keyed to the quote's start line.

Measured: the layout shift breaks **0** of the 14 needles; specificity **0**
cross-fires; **15** tests pass.

The census moves: recorded needles **91 → 80**, numeric **40 → 29**, derived
**122 → 133**, needle digits **181 → 167**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**.

Not checked: **6** files still carry recorded needles with numeric values —
`test_named_results.py` **5**, `test_sources.py` **4**, `test_index_links.py` **3**,
`test_fleet_design.py` **3**, `test_index_design.py` **1**, `test_abstracts.py` **1**
— **29** numeric in all. The **309** clean pins are still literals (phase 2), and
there is one synthetic-rule test file (`test_quotes.py`) against 14 checkers
(phase 3).

## Phase 1 takes `test_named_results.py`, and the quote anchor is a rule, not a string

Six needles are rebuilt. The quote needles re-run the checker's own anchor-selection
rule on the mutated page: the quote's row, the anchors after the quote inside that
row, the anchor in the quote's own line, the anchor earlier in the row, then the
anchors in the three lines above. The table needle reads the mutated row against the
ledger, keyed to the family the mutation touched; the bare needle reads the mutated
page's bare anchor against the population's overview line for that family. Five
needles stay literal — the anchor line written out of range, the renamed anchor path,
and three count labels, which carry no measured figure.

**A recorded anchor string is a fact about the page before the mutation.** The quote
pass picks an anchor by a rule with four fallbacks, so a needle that names the anchor
the clean page carried is not the string the pass prints for a page whose anchor
moved. Re-running the rule on the mutated page is what makes the needle the pass's
own output.

Measured: the layout shift breaks **0** of the 13 needles; specificity **0**
cross-fires; **14** tests pass.

The census moves: recorded needles **80 → 76**, numeric **29 → 25**, derived
**133 → 137**, needle digits **167 → 159**, clean pins **309** unchanged.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**.

Not checked: **5** files still carry recorded needles with numeric values —
`test_sources.py` **4**, `test_index_links.py` **3**, `test_fleet_design.py` **3**,
`test_index_design.py` **1**, `test_abstracts.py` **1** — **25** numeric in all. The
**309** clean pins are still literals (phase 2), and there is one synthetic-rule test
file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_sources.py`, and the anchor fault is a block fault

Two needles are rebuilt. The block needle re-runs the pass's own fence walk on the
mutated page and keys to the byte the mutation touched, so the block it reports is
the block the fault sits in. Nine needles stay literal — the renamed anchor file, the
renamed directory slug, the prose figure, and the six count labels, which carry no
measured figure.

**The anchor-shifted fault is really a block fault.** The shifted line `1176` is
**inside** `pgfmanual-en-macros.tex`, so the anchor pass is silent and the pass that
fires is the block pass, attributing the block to the anchor the mutated page
carries. A needle that named the clean page's anchor line would have been the string
the pass printed **before** the mutation, and the first needle I wrote did exactly
that — it demanded `anchor …:1176 is outside the file`, which the pass never prints.

Measured: the layout shift breaks **0** of the 12 needles; specificity **0**
cross-fires; **13** tests pass.

The census moves: recorded needles **76 → 74**, numeric **25 → 23**, derived
**137 → 139**, clean pins **309** unchanged. Needle digits stayed **159** — the
derived needles carry digits too (`block line 0 != …:1176`), so the digit count is
not a pure measure of derivation.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**.

Not checked: **4** files still carry recorded needles with numeric values —
`test_index_links.py` **3**, `test_fleet_design.py` **3**, `test_index_design.py`
**1**, `test_abstracts.py` **1** — **23** numeric in all. The **309** clean pins are
still literals (phase 2), and there is one synthetic-rule test file
(`test_quotes.py`) against 14 checkers (phase 3).

## Phase 1 takes `test_proof_density.py`, and a global-count needle must be keyed to the delta

Eight needles are now functions of the mutated rows, the mutated ledger and the
committed population. The row-count and column-sum needles are keyed to the **delta
the mutation introduces** — `R['rows'] - 1`, `R['proofs'] + 1`, `R['thms'] + 1` —
not to the mutated table.

**A needle that reads the mutated table produces the pass's own line for any fault
that perturbs that count.** The drop-row needle fired on the duplicate-row fault, the
proofs-sum needle fired on the negative-proofs fault, the thms-sum needle fired on
drop and duplicate, and the family-set needle fired on drop. Keying to the delta
makes each needle the line the pass prints for its own fault and for no other: the
drop needle asks for `718 != 719`, which the duplicate candidate never prints.

The family-set needle names the delta `1, 1`, which is only true when the renamed
family has exactly one source row. The layout probe caught that: renaming `rows[0]`
after a reorder renames a multi-row family, and the needle stopped firing. The
mutation now targets `one_row_index` — **a layout-dependent needle needs a
layout-independent target.**

The layout analogue for a TSV is a **reorder that preserves every measured count**
(`sorted` by `dir` descending). The row-insert analogue broke **5** needles; the
reorder breaks **0**.

Measured: specificity **0** cross-fires; reorder **0** breaks; **10** tests pass.

The census moves: recorded needles **74 → 71**, numeric **23 → 20**, derived
**139 → 142**, clean pins **309** unchanged. Needle digits **159 → 166** — the
delta-keyed needles carry `R['rows']` expressions, so the digit count is not a
measure of derivation.

Gate **79** rows, **0** failures; head diff empty; promote-and-verify assertion
green; lint trio **0 / 0 / 0**.

Not checked: **4** files still carry recorded needles with numeric values —
`test_index_links.py` **3**, `test_fleet_design.py` **3**, `test_index_design.py`
**1**, `test_abstracts.py` **1** — **23** numeric in all, and all four are the
mutation's own inputs (invented hrefs, invented paths, rewritten phrases), which the
rule keeps literal. `test_subfinding_pairs.py` already derives its measured values.
The **309** clean pins are still literals (phase 2), and there is one synthetic-rule
test file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 0 extends to `verify_counterexample_crosscheck.py`, and the padding test is proven both ways

The padding mutant existed only for `verify_t0_chains.py`. It now covers the
crosscheck checker's three tables: every cell of every `|`-delimited row gains two
spaces, and the test asserts the table passes report **no** table problem and the
same row counts.

**The discriminator is the row-count line, not the render diff.** The render diff
fires for the padding either way, so it cannot be the test. A row regex that required
exact spacing drops every padded row, and the pass then reports
`summary table table has 0 rows, the bundle count is 28`-shaped trouble — the row
count is what shows it.

Proven both ways, as the standing rule requires: against the tolerant regexes the
padding test passes with **0** table problems; against a strict row regex
(`^\|(\d{3})\|(T\d)\|(\d+)\|(\d+)\|(\d+)\|`) it fails with
`summary table row 1: ('<none>',) != ('047', 'T3', 1, 1, 0)`. A test that passed
against both would be a needle that fires for both states.

Measured: **16** tests pass; lint trio **0 / 0 / 0**; census unchanged (the padding
test is not a needle fault). Gate **79** rows, **0** failures; head diff empty;
promote-and-verify assertion green.

Not checked: the padding mutant now covers **2** of the 14 checkers that read tables
(`verify_t0_chains.py`, `verify_counterexample_crosscheck.py`); the rest are unprobed.
The **309** clean pins are still literals (phase 2), and there is one synthetic-rule
test file (`test_quotes.py`) against 14 checkers (phase 3).

## Phase 0 extends to `verify_faithfulness.py`, and the padding test is proven both ways again

The same shape: every `|`-delimited cell of the disjoint, overlap and `a.e.` tables
gains two spaces, and the test asserts the table passes report **no** table problem
and the same three row counts.

Proven both ways: against the tolerant regexes the test passes with **0** table
problems; against strict regexes it fails with `disjoint table [] != [...]` and
`overlap table has 0 rows, recomputation has 15`. The row-count line is the
discriminator; the render diff fires for the padding either way.

Measured: **17** tests pass; lint trio **0 / 0 / 0**; census unchanged. Gate **79**
rows, **0** failures; head diff empty; promote-and-verify assertion green.

Not checked: the padding mutant now covers **3** of the 14 checkers that read tables
(`verify_t0_chains.py`, `verify_counterexample_crosscheck.py`,
`verify_faithfulness.py`); the rest are unprobed. The **309** clean pins are still
literals (phase 2), and there is one synthetic-rule test file (`test_quotes.py`)
against 14 checkers (phase 3).

## Phase 0 extends to `verify_subfinding_pairs.py`, and the padding test must scope to the table it reads

The same shape: every `|`-delimited Summary-table cell gains two spaces, and the test
asserts the pass reports no missing row and reads the same values.

**The padding test must scope to the rows the pass reads.** My first version compared
every `|`-delimited row on the page against the measured dict. The page carries **16**
table-shaped rows and the pass measures **13** keys, of which the Summary table
carries **10** — so the comparison failed on the clean page, not on the padding. The
test now compares only the labels the Summary table carries.

Proven both ways: against the tolerant regex the test passes with **0** Summary
problems and reads all 10 rows; against a strict regex it fails with
`Summary table has no row for: families read` and
`Summary table has no row for: manuscripts in the population`.

Measured: **11** tests pass; lint trio **0 / 0 / 0**; census unchanged. Gate **79**
rows, **0** failures; head diff empty; promote-and-verify assertion green.

Not checked: the padding mutant now covers **4** of the 14 checkers that read tables
(`verify_t0_chains.py`, `verify_counterexample_crosscheck.py`,
`verify_faithfulness.py`, `verify_subfinding_pairs.py`); the rest are unprobed. The
**309** clean pins are still literals (phase 2), and there is one synthetic-rule test
file (`test_quotes.py`) against 14 checkers (phase 3).

## Two row regexes are padding-fragile, and that is the formatter boundary

Probing the padding against the two checkers whose row regexes I had not touched:
`verify_named_results.py:54` is `^\| (\d{3}) \| (T\d) \| (\d) \| \`([^`]+):(\d+)\` \| \*"([^"]*)"\* \|$`
— **single** spaces, not `\s*` — and `verify_verification_dirs.py` reads the entry-point
table the same way. Padding every cell breaks both: the clean pages report **0**
problems, the padded pages report `TABLE rows 0, extractor measured 17 statements`
and `entry-point table has 0 rows, the bundle count is 30`.

**This is the formatter boundary, not a bug to fix.** The two pages must keep exact
single-space table formatting, because the checkers key on the byte form. A formatter
pass over `notes/reports/named-results.md` or `notes/reports/verification-dirs.md`
would silence the table pass by dropping every row — the same failure mode the prettier
probe recorded for the other byte-keyed checkers. The tolerant regexes (`\s*`) are
padding-safe; these two are not, and the difference is a property of the checker, not
of the page.

Not checked: the padding mutant covers **4** of the 14 table-reading checkers; **2**
of the remaining 10 are now known to be padding-fragile (`verify_named_results.py`,
`verify_verification_dirs.py`), and the other 8 are unprobed. The **309** clean pins
are still literals (phase 2), and there is one synthetic-rule test file
(`test_quotes.py`) against 14 checkers (phase 3).

### 2026-10-14 — the padding-fragile boundary is a coverage gap, not a regex fork

The user chose option 2: extend `.prettierignore` to the checker-verified tree rather
than widen the two byte-exact row regexes to `\s*`. Measured before the change,
`prettier --check "notes/**/*.md"` reported **28** pages as needing a rewrite — 23 under
`notes/reports/` and 5 under `notes/development/` — because the rule named top-level
`notes/*.md`, `notes/scripts/**`, `notes/summaries/**` and
`notes/development/upstream_history/*` and reached none of them. Those 28 carry **1,495**
table rows, **1,213** of them single-space-padded, and **236** `*"…"` markers. Widening
the two regexes fixes the cells on 2 pages and leaves the markers on 28, so the padding
fork is partial: prettier's `*"…"` → `_"…"` rewrite is not configurable and no row
regex can absorb it. **5** of the 28 are render-diffed by `verify_page_sync.py`, so the
two negations that un-ignored `notes/reports/links.md` and `notes/reports/proof-density.md`
named pages a checker does parse; they are removed. The rule now names
`notes/reports/*.md` and `notes/development/*.md`; the same check reports **2** files —
the two pages no checker parses, `notes/reports/conjecture-standing.md` and
`notes/development/summaries-workflow.md` — and all 28 previously exposed pages are
ignored. No checker reads `.prettierignore`, so the fix is config and docs only, and the
two byte-exact row regexes stay as they are: they are the contract, not a bug. The same
pass swept `AGENTS.md`'s index ∩ summaries slug figure from **14** to **18**, which the
checker and an independent basename set both measure.

Not checked: the two formatable pages are not prettier-clean, so a format pass over
them is still open; the padding mutant covers **4** of the 14 table-reading checkers
and the other 10 are unprobed; the **309** clean pins are still literals.

### 2026-10-14 — the needle-input rule and the layout probe make the recorded/literal split checkable

`measure_needles.py` gained two columns. **Synthetic rule inputs**: `test_index_links.py`'s
list is 21 invented hrefs the scanner must classify, not page mutations, so its needle slot
is the test's own input by construction; the list is renamed `INPUTS` and the census counts
it separately. **Not inputs**: for every recorded needle, the digits it carries are compared
with the string constants its own mutation writes; a needle whose digits all appear there is
an input, and one carrying a digit the mutation never writes is a measured figure phase 1
missed. The rule found **one** real miss — `test_dependency_drift.py`'s out-of-range anchor
needle carried `335`, the line count of `lean/lakefile.lean`, which no mutation writes; the
needle now reads the file and derives the count. It also found two needles whose digits are
**locators** (`layer 1`, `065/2`) — the pass prints them from the row it flags, not from the
mutation — so the rule strips `layer[ -]N` and `NNN/N` before comparing. The census reports
**not inputs 0**.

The layout probe is a mode of the suite: `LAYOUT_SHIFT=1` makes `Path.read_text` return the
page with two lines inserted after its first `## ` heading, so the fixture that hands a test
its page and the checker's own page read shift together and the population the needle derives
from them shifts with the page. For the four table fixtures the analogue is a row swap, which
preserves every count. `test_cache_promotion.py` is excluded: its pass compares cached bytes
with the bytes on the tracked path, so shifting a page makes every page differ and the pass
reports the first mismatch, which is not a layout finding. Measured: **309 passed, 3 failed**,
and all three failures are clean-page pins (`dependency_drift`, `subfinding_pairs`,
`t0_chains`) — literals pinned to the page as committed. **0 needles break.** The same run
found one inert mutant: `test_subfindings.py` picked the first manuscript row, whose path is
not `paper.pdf`, so the path mutant replaced nothing; the fixture now picks by path.

Fresh census: faults **192**, recorded **49** (numeric **16**, structural **33**), derived
**143**, needle digits **160**, synthetic inputs **21**, clean pins **309**, not inputs **0**.
The census's own row in the ownership manifest names the two new columns.

Not checked: the three layout-sensitive clean pins are still literals — that is phase 2's
target list, now measured; the **10** unprobed table-reading checkers still have no padding
test; the needle-input rule compares digits, so a recorded needle with **no** digits is
unjudged by it and is judged only by the layout probe.

- **Padding tests: tolerant where the reader allows whitespace, boundary where it does not.**
  Chosen 2026-10-14 on `math-4nn.1`. Fifteen checkers now carry a padding test, one commit each:
  the tolerant direction (`test_padded_table_cells_are_still_read`) for the readers that split and
  strip, or match rows with `\s*` — `verify_abstracts.py`, `verify_findings.py`, `verify_summaries.py`,
  `verify_scope_exclusions.py`, `verify_citations.py`, `verify_fleet_design.py`,
  `verify_script_ownership.py`, `verify_cache_promotion.py`, plus the four from phase 0; the boundary
  direction (`test_padded_table_cells_are_dropped`) for the readers that are byte-exact by contract —
  `verify_upstream_history.py` (`^\| \d{3} \| \`[^`]+-2026\` \| \*"`), `verify_dependency_drift.py`
  (`startswith("| The ")`), `verify_verification_dirs.py` (`^\| (\d{3}) \|`). Each tolerant test is
  proven against the pre-fix code: the checker's row pattern is swapped for its single-space form in
  memory and the padded rows must vanish. Measured drops: abstracts 35→0, findings 31→0, summaries 671
  rows, scope-exclusions 242→0, citations 48→0 (20 work, 6 pair, 12 cluster, 10 release),
  fleet-design 8→0, ownership 10→0, cache-promotion 42 table rows→0. Each boundary test is proven the
  other way: the byte-exact pattern reads the clean page (upstream-history 14 fixes + 11 configs,
  dependency-drift 6 check rows, verification-dirs 30 rows) and 0 padded rows. Three rules this pass
  established. **The criterion is the pass's own problem list, never a private copy of the row
  regex** — a test that counts rows with its own pattern proves nothing about the checker. **For a
  report-fed page the render diff fires on padding either way**, so the criterion is the non-sync
  problems; `verify_fleet_design.py`'s `check()` appends the sync problems last, which is what makes
  that split exact. **A boundary test asserts the ignore rule too**: every checker page is under
  `notes/reports/*.md`, `notes/development/*.md`, `notes/*.md` or `notes/scripts/**/*.md`, all
  prettier-ignored, so padding never reaches the tracked tree and the byte-exact contract holds.
  `verify_index_design.py` gets no padding test: it has no row regex, it builds expected row strings
  and requires the page to contain them verbatim, so padding is a boundary the ignore rule already
  covers. Gate: **79 rows, 0 failures**, empty head diff, tree clean after builder → render.

Not checked: the three layout-sensitive clean pins (`dependency_drift`, `subfinding_pairs`,
`t0_chains`) are still literals; the **309** clean pins are literals; the synthetic-rule tests are
one file (`test_index_links.py`) against **14** checkers; the two formatable pages
(`notes/reports/conjecture-standing.md`, `notes/development/summaries-workflow.md`) are not
prettier-clean.

- **The format-boundary enumeration is a checker pass, not a prose claim.** Chosen 2026-10-14 on
  `math-4nn.2`. Pass I of `verify_script_ownership.py` loads every `verify_*.py` and reads its own
  `PAGE` and `PAGES` constants, because a source parse reads docstring prose as well: measured **25**
  checker-parsed pages, **0** outside the ignore rule, **2** formatable pages under `notes/`. The
  matcher is gitignore-correct, which is what made the enumeration honest: a trailing slash means the
  directory and everything below (`notes/index/` covers the whole tree), `**` is zero or more
  directories (`notes/scripts/**/*.md` covers a page sitting directly in `notes/scripts/`), and a
  leading slash anchors at the repo root. My first matcher got all three wrong and reported 1,095
  formatable pages. The population is cached, so the 23 module loads are paid once per process, and
  the loader is `importlib.util`, not the deprecated `load_module`. Two mutants: a stale count in the
  page's sentence, and the `notes/reports/*.md` rule dropped in memory.

The prettier decision for the two formatable pages is the user's, and the bead says so. The options,
recorded rather than asked:

1. **Leave them formatable.** The two pages are prose the checkers read with byte-exact quotation
   forms (`*"…"` markers in `notes/reports/conjecture-standing.md`, the append-only log's own
   headings). Prettier rewrites `*x*` to `_x_` and pads table rows, so formatting them breaks the
   quotation passes. This is the current state: the pages are formatable, not formatted, and nothing
   runs prettier over them.
2. **Move the quotation forms out of the byte-exact shape.** Change the checker's needle pattern to
   accept `_…_` as well as `*…*`, then prettier-format the two pages. This makes the tree uniformly
   formatable at the cost of widening a checker's byte contract.
3. **Negate the negations.** Put both pages back under the ignore rule, so the formatable set is
   empty and the enumeration reports **0**. The two pages then carry no prettier guarantee at all,
   which is what the negations were added to give them.

Not checked: the decision is open; the **309** clean pins are literals; the synthetic-rule tests are
one file against **14** checkers.

## Bead `math-4nn.3` replaces the ledger-join clean pins with invariants

Chosen 2026-10-14. A literal pin records what the corpus measured when the test was written, so it
stays silent when the ledger changes under it. The four files whose population is joined to the ledger
now assert the join, not the number: `test_sources.py` (rows = listed, dirs = listed + superseded +
notices, every main file under `build/`, fams = ledger family set, formalized = `paps_form` sum),
`test_index_design.py` (families = family set, manuscripts = `paps` sum, formalized = `paps_form` sum,
`chal_json` = `chal_lean`, `mr_configs` < `mr_entries`), `test_named_results.py` (`ndirs` = `paps` sum,
prose sentences and windows = family count), `test_proof_density.py` (distinct dirs = rows, `paps` sum
= rows, family sets equal, one row per family, tier counts sum to the family count, the
`formalization.yaml` `sources:` set against each family's `paps_form`). Figures the join cannot
produce stay literal — nodes, edges, bytes, pages, environment counts, the root distribution, the
column sums, the `.tex` file count, the headline-begins split.

**The acceptance criterion is the fault, not the relation.** Each file carries a test that flips a
ledger row and shows the join is the only witness: a `paps_form` flip, a `paps` decrement, or a dropped
family row moves no page byte, so every page pass stays silent and no literal pin moves. The formalized
join is the one that sees it. `measure_proof_density.py` gained `yaml_dirs()` for that join — the set
is read from the yaml, not recorded as a count.

Two things the pass fixed on the way: the shared `ledger` fixture resolved to `notes/` (`parents[2]`)
and now resolves to the repo root (`parents[3]`); and `S19` in `notes/reports/findings.md` declared 304
lines for `measure_proof_density.py` when the file had 317, which `verify_findings.py` flagged.

AGENTS.md is swept in the same commit: the clean-test pins it quotes for sources, index-design and
named-results, the index-design all-TSV (2,252,773 → 2,316,386 B), index-tree (11,530,406 → 11,531,073 B)
and disk-link (66,110 → 66,115) figures that had drifted, and the proof-density pin description. Gate:
**79 rows, 0 failures**, empty head diff, cache promotion 0 problems, lint 0/0/0. Tests: sources 14,
named-results 15, index-design 17, proof-density 11.

Not checked: the three layout-sensitive clean pins (`dependency_drift`, `subfinding_pairs`,
`t0_chains`) are still literals; the remaining clean pins are literals; beads `.4`–`.7` are unwritten.

## Bead `math-4nn.4` replaces the resolution literals with 0-unresolved plus non-vacuity floors

Chosen 2026-10-14. A clean test that pins "172 anchors, 295 block lines, 38 quotations" records what
the page carried when the test was written. A pass that reports 0 problems on a page carrying nothing
passes, and the pin is silent. The pin becomes the pass's own population, read off the page by the
pass's own rule, required non-zero: 0 problems then means every shape the page carries resolved.

Six files converted. `test_sources.py` (anchor shapes, slugs), `test_named_results.py` (anchors, bare
anchors, table rows, quotations), `test_faithfulness.py` (anchors, fenced-block lines, quotations, plus
the formalization relations: every unique config resolves, every carrier-typed statement has a resolved
carrier, entries exceed configs), `test_counterexample_crosscheck.py` (anchors, fenced-block lines,
quotations), `test_index_links.py` (every extracted link resolves to exactly one of directory or file,
so the two counts sum to the link count; the basename pass keeps 0 collisions with both sets non-empty
and the index required to contain collisions), `test_summaries.py` (the page set is the tree, required
non-empty, and each page must carry markers). `test_upstream_history.py` already carried the floor
(`hits > 0`, "the pass is vacuous, not passing") and needed no change.

**The anchor pass counts distinct `(path, line)` pairs, not shapes** — the page repeats anchors and the
pass resolves each pair once — so the floor is the pass's rule, not a looser regex count. Measured: 61
counted against 66 shapes.

Each converted file carries a strip test that makes the floor non-vacuous: removing every anchor shape
drives the anchor pass to 0 and the block and quotation passes with it (a block with no preceding anchor
and a quote with no anchor in its line are skipped), while the page still carries blocks and quotations
— so the pass counts less than the page carries and the equality fails. That failure is what the floor
is designed to catch.

AGENTS.md is swept in the same commits: the pins it quotes for sources, named-results, index-design,
faithfulness and crosscheck, the index-links injected/control counts it carried as 20 and 7 against the
file's 21 and 8, and the `check()`-call counts for sources, named-results and faithfulness. Gate:
**79 rows, 0 failures**, empty head diff, lint 0/0/0. Tests: sources 15, named-results 16,
index-design 17, proof-density 11, index-links 7, faithfulness 19, crosscheck 17, summaries 8,
upstream-history 16.

Not checked: the population literals that are not resolution results (28 families, 2,560 nodes, the
corpus byte sums, the environment counts) stay literal; the three layout-sensitive clean pins stay
literal; beads `.5`–`.7` are unwritten.

## Bead `math-4nn.5` replaces the census clean pins with walk-equality invariants

Chosen 2026-10-14. A clean test that pins 7,679 `.tex` files, 122,458 `.lean` files, 749 preprint dirs,
30 bundles, 521 `.bib` files, 1,033 index pages and 16 tables records what the tree measured when the
test was written. The pin becomes the tree: each test walks the corpus with its own `rglob` and the
population's count must equal the walk, so a manuscript, bundle, bibliography or rendered page added to
the corpus moves the walk and the equality fails — what a recorded number can never see.

Five files converted: `test_sources.py` (preprint dirs), `test_named_results.py` (`.tex` at glob depths
1-4), `test_index_design.py` (preprint dirs, `lean/OAI/` `.lean` files, index pages, index tables, trace
files and stems), `test_citations.py` (`.bib` files), `test_verification_dirs.py` (directories carrying a
`verification/` directory).

**Two traps the pass fixed on the way.** Depth must be measured relative to `preprints/`, not on the
absolute path: the root prefix shifts every file past the glob bound and the walk read 0. And the
checker's depth-1-4 scope counts the manuscript dir as level 1, so the bound is relative parts minus one
— measured 7,240 at the naive bound against the population's 7,679.

**The remaining literals, named not counted** (the bead's requirement): the counts a file walk cannot
produce — 2,560 nodes, 3,415 resolved edges, 17,217 raw bib edges, 391 citation edges over 104
cross-family, the ledger set at 297,050 B, the all-TSV 2,316,386 B, the index tree at 11,531,073 B, 66,115
disk links with 17,700 resolving to a directory, 559 module dirs, 17 disciplines against 23 Lean dirs,
242 scope notes, 30 verification bundles, 521 `.bib` files with 13,802 entries and 393 hrefs, the
substring counts 18 / 373 against the brace-qualified 17 / 372, the theorem-environment counts (2,410
begins, 1,609 titled per line, 1,619 whole-text, the 2,405 / 4 / 1 split, 2,288 environments with 48
`a.e.` hits over 32 families), the 28-family counterexample population, the 139-row conjecture prior,
the 79 gate rows, the pool cap 12, the 5 tree digests, and the three layout-sensitive clean pins
(`dependency_drift`, `subfinding_pairs`, `t0_chains`). The faithfulness environment count stays literal
because the population exposes no file set to walk against — reproducing the checker's environment rule
in the test would be re-deriving a count through the writer's code, which proves nothing.

AGENTS.md is swept in the same commit: the census pins it quotes for index-design and named-results.
Gate: **79 rows, 0 failures**, empty head diff, lint 0/0/0. Tests: sources 15, named-results 16,
index-design 17, citations 11, verification-dirs 20.

Not checked: beads `.6` and `.7` are unwritten; the environment counts stay literal for the reason
above; the three layout-sensitive clean pins stay literal.

## Bead `math-4nn.6` is partly done: the scanner cases landed, the range cases need a rule function

Claimed 2026-10-14, **left open**. Two synthetic cases landed in
`notes/scripts/tests/test_index_links.py`: the paren-balanced scan keeps a `CAT(0)` target whole where
`[^)]*` truncates at the first `)`, and two adjacent `\href` targets read as two paths under the shipped
`catlib.overview.PAP` class, which excludes braces and backslash, where a class excluding only whitespace
and parentheses glues them into one string that is not a file. Both feed the rule a string; neither names
a file on disk. The module docstring became raw — `\href` in a non-raw docstring is an invalid escape and
`python3 -W error::SyntaxWarning` reports it.

**The range cases are blocked on a design change, not on effort.** The bead's cases are blank line at the
end of a range, reversed range, and range past end. The parsing is a shipped pattern
(`catlib.anchors.anchor_pattern(..., ranges=True)`) and a synthetic string tests it. The **validation** —
the three cases the bead names — lives inside each checker's `check()`, which resolves the anchor against
a file read from disk. A synthetic page cannot be validated without a synthetic file on disk, so a case
that does not read the corpus cannot reach the validation through the shipped code. Making it reachable
means extracting the range validation into `catlib` as a function of `(anchor, file lines)`, which is a
change to five checkers and their needles. That is a design decision, not a continuation, so it is
recorded here and the bead stays open.

The reversed-range check exists in one checker only: `verify_summaries.py:157` flags `a > b`. The other
range passes accept a reversed range as long as both ends sit inside the file — measured against the
shipped rule, not assumed.

Not checked: the range-rule cases for `test_named_results.py`, `test_counterexample_crosscheck.py`,
`test_upstream_history.py`, `test_sources.py`, `test_faithfulness.py`; the read_file line-label offset
case; bead `.7` (synthetic LaTeX/carrier rule tests).

## 2026-10-14 — bead `math-4nn.7`: the byte-form rules are fed strings

Seven rule classes, each with a case that passes against the shipped rule and fails against the
narrowed variant, and no case reads the corpus. Measured, not assumed:

- **Accent fold** (`measure_names.fold`): `K\"ahler` and `Kähler` fold to one key, so a name the
  release spells two ways is one name page. A rule that strips only Unicode diacritics leaves the
  escape in the string, so the two spellings stay two keys. `test_named_results.py`, which is the
  checker that builds its quote pattern from `fold(quote)`.
- **Accent guard** (`catlib.bib.ACCENT`'s `(?![a-zA-Z])`): an escape applied to a letter (`\'a`) is
  **not** folded, so `norm_title` splits `Gy\'arf\'as's` into `gy arf as s`, while the checker's
  no-guard variant folds it into `gyarfas s`. The guard is what makes the two normalizations disagree,
  which is the row the page records as a sensitivity measure. `test_citations.py`.
- **Apostrophe fold** (`catlib.text.fold_apostrophe`): a U+2019 title and an ASCII title are one key;
  a rule that strips only diacritics keeps them distinct. `test_citations.py`.
- **Verbatim is bytes**: `collapse_ws` leaves the accent escape in place, so a quote that de-LaTeXes
  `Gy\'arf\'as's` fails against the bytes `overview.tex:405` ships, while the accent fold accepts it.
  `test_counterexample_crosscheck.py` (the checker's `norm`) and `test_subfinding_pairs.py` (the raw
  substring test on the `\resultentry` line).
- **`\documentclass` at line start**: a macro that *mentions* the command is not a root, so the
  line-start rule reads 0 from it and the substring rule reads 1 — the mechanism behind 715/3/1
  against the substring 714/4/1. `test_sources.py`.
- **`\newtheorem` declared rule**: `declared_envs` is the declared set **minus** `NON_STATEMENT`, so a
  dir declaring `assumption` and `definition` declares `{"assumption"}` and counts 2 begins, the
  six-name list counts 1, and a rule that skips the subtraction counts 3 — the shape of 21,288 against
  21,203. `test_sources.py`.
- **Carrier rule**: allows `noncomputable`, so `noncomputable def MainClaim : Prop := by` is found; a
  `private|protected`-only rule misses it. `test_faithfulness.py` and `test_counterexample_crosscheck.py`.
- **Statement rule**: matches the qualified name minus `OAI.` as well as the bare tail, so `theorem
  ThorpNine.main :` is found for `OAI.ThorpNine.main`; the checker's own bare-tail rule
  (`verify_counterexample_crosscheck.py:266`) reads 188 of 189 and misses this line. Both rules read
  `theorem main :`. `test_faithfulness.py` and `test_counterexample_crosscheck.py`.
- **Citation stripping**: `strip_markup`'s citation rule requires the brace to follow `\cite`
  directly, so a bracketed note is not swallowed and its word survives the fold; a rule that allows the
  optional `[...]` argument strips the whole citation. The fold also strips a theorem **number** after
  the word (the deliberate rule that lets a page write "Theorem 1" for a source `\ref{thm:main}`), so
  the word, not the number, is what the comparison sees. `test_summaries.py` — the rule is used by the
  summaries quote pass, so the case lives with that checker, not in the bead's six-file list.

**The statement rule moved to `catlib/yaml.py` as `stmt_pattern`** because it is the yaml
declaration's source-side match rule and two checkers carried identical copies; a test cannot reach it
while it is built inside a function that reads a Lean file. `verify_faithfulness.py`'s dead `STMT`
constant is removed. Both checkers report identical bytes after the rewiring — measured, not assumed.

Test counts after the bead: sources 17, named-results 18, index-design 17, proof-density 11,
index-links 9, faithfulness 21, crosscheck 20, summaries 9, upstream-history 16, citations 13,
verification-dirs 21, subfinding-pairs 12. Gate: **79 rows, 0 failures**, head diff empty, cache
promotion 0 problems, lint 0/0/0.

Not checked: the range-rule cases, still blocked on extracting range validation into `catlib` (bead
`.6` open); the read_file line-label offset case; the citation-stripping case for the abstracts and
findings checkers, which use the same fold; bead `.2`'s prettier decision, which is the user's.

## 2026-10-14 — bead `math-4nn.6`: range validation moves to `catlib`, the range cases become testable

The blocker was structural, not effort: the range checks lived inside each checker's `check()`, which
resolves anchors against files read from disk, so a no-corpus case could not reach them.
`catlib.anchors.range_facts(a, b, n, lines)` returns the three facts — out-of-range positions, blank
positions, the reversed flag — and each checker formats its own message, so a test can feed the rule a
line count and a synthetic line list.

**Measured, not assumed: the range shape exists in three checkers, not the five the bead named.**
`verify_summaries.py` flags out-of-range, blank and reversed (`[S4:29–12]` is a problem);
`verify_faithfulness.py` and `verify_upstream_history.py` check **both** ends of a `path:a-b` anchor
against the file's line count and accept a reversed range, so the reversed flag is returned and the
caller decides. `verify_named_results.py`, `verify_counterexample_crosscheck.py` and
`verify_sources.py` carry `path:line` anchors only, so a range case cannot apply to them — that is the
finding that closes the bead's five-file list.

The upstream pass reads a window around the anchor, not the whole file, so the line count is a
parameter (`n`) and the blank check is optional (`lines`). All three checkers report identical bytes
after the rewiring: summaries 30 pages / 4,414 marker positions / 1,243 quoted spans / 0 problems;
faithfulness anchors 10, block lines 30, quotations 1, 0 problems; upstream-history RESULT green.

Cases landed: blank line at the end of a range and reversed range in `test_summaries.py` (the checker
that flags both); range past the end and reversed range in `test_faithfulness.py` (the checker that
accepts reversed); range past the end in `test_upstream_history.py`. Each is paired with the narrowed
rule that misses it — a rule that checks only the start position reports no problem for a range whose
end runs past the file, and a rule that checks only that both positions sit inside the file accepts a
reversed range.

Test counts after the bead: sources 17, named-results 18, index-design 17, proof-density 11,
index-links 9, faithfulness 23, crosscheck 20, summaries 11, upstream-history 17, citations 13,
verification-dirs 21, subfinding-pairs 12. Gate: **79 rows, 0 failures**, head diff 0 bytes, cache
promotion 0 problems, lint 0/0/0.

Not checked: the read_file line-label offset case; the citation-stripping case for the abstracts and
findings checkers, which use the same fold; the blank-line shape for the two anchor passes that do not
check blank lines inside a range (they read a window, not the file's lines); bead `.2`'s prettier
decision, which is the user's.

## 2026-10-14 — bead `math-ckd.4` claimed; the superseded `--mutant` sentence swept out of the pages

Ten of the 30 summary pages carried a sentence naming `python3 notes/scripts/verify_summaries.py
--mutant`, a flag the checker no longer carries: the mutants moved to
`notes/scripts/tests/test_summaries.py` under the "extract the testing" directive, and the checker
reads no argv, so `--mutant` is inert. Each page now names the checker (which measures) and the test
file (which injects), with the command that runs it. Measured after the sweep: `verify_summaries.py`
reports **30 pages, 4,414 marker positions, 1,243 quoted spans, 0 problems**, and the extracted
self-tests report **11 passed**.

`git grep` over the tracked tree finds the flag in **no** file outside `.beads/issues.jsonl`. The
closed beads' bodies and close reasons name it because it was the command at the time they closed —
rewriting a closed bead's record is not a sweep, so they are left as written. The **open** bead
`math-ckd.4` is swept: its acceptance criteria now name the test row, and the bead is claimed.

Not checked: the pages the bead still has to write (the group is 132 families; 30 pages exist across
all tiers, 1 in differential geometry); the closed beads' historical `--mutant` wording, left
deliberately.

- **The seeder's L1 is a tree, so a new page is probe drift the old record cannot name.** Chosen
  2026-10-14 on `math-ckd.4`: the family 342 page landed, `catlib/promote.py` names
  `notes/summaries/` as a tree in `seed_quotes.py`'s L1, the checker expands the tree to the pages on
  disk, and the newest probe record predates the page, so the promotion check reported L1 drift. The
  fix is a re-probe, not a narrowed L1: `measure_open_probe.py --record <name> notes/scripts/seed_quotes.py`
  run **plain** (the probe's own `--check-only` suppresses the record write) lands the record that
  names the page, and the checker's `PROBES` tuple gains it newest-first. Revisit when the next page
  lands — the same drift recurs, and the record is a tracked file, so it is committed with the sweep.
- **A shell preview is not a file read.** Measured the same day: the first draft of the 342 page quoted
  a Donaldson entry as a 1990 *Journal of Differential Geometry* article, a coercivity theorem at
  `01-introduction.tex:147`, a cone-characterization sentence at `08-cones.tex:22–24`, and a
  `theorem main` wrapper in the comparator stub. All four were fabricated by a truncated shell preview;
  the real file has an *Inspired by S. S. Chern* incollection, no coercivity statement, the
  characterization inside the corollary's proof, and a stub that restates the theorem with its own
  definitions and ends in `sorry`. The checker caught all six. Re-read with `read_file` before quoting;
  the checker's `NOT VERBATIM` line is the authority, not a preview.
- **A Sources-table File cell must be the full repo-relative path in backticks.** Chosen 2026-10-14
  on `math-ckd.4`: the family 334 page's S3 cell was `[`README.md`](../../../preprints/<slug>/README.md)`,
  and `catlib/summaries.py`'s `CELL` takes the **first backticked span**, so the path the checker
  resolves is `README.md` — which exists under both the declared manuscript root and the repo root.
  Pass B counts a cell that resolves under both roots ambiguous, and pass E then applies the
  `README.md` block rule (the `| NNN |` row rule) to the manuscript README, which has no such rows,
  so every line citation into S3 was reported outside the family's block. The convention the green
  pages already use is the full path in the cell. Revisit if the checker ever reads the href.
- **A blurb quotation is the whole CONTENTS.md line, in the source's own glyph form.** Measured the
  same day: the first draft quoted the blurb from "Constructs" onward, then added a closing `**` at
  the end. `strip_markup` removes a `**…**` span **with its content**, so a bold span that covers the
  whole quotation folds to the empty string. The source closes the bold after the title, and its body
  writes `ℝ<sup>3</sup>` (Unicode), not `$\mathbb R^3$` — the LaTeX form folds to `$ R^3$` and does
  not match. Write the line verbatim, with the superscript as the source carries it.
- **The comparator JSON carries no tier, no paper title, and no file list.** The first draft of the
  334 page invented `name`, `tier`, `domain`, `paper`, `source`, `challenge`, `proof`,
  `comparator_config`, and `comparator_lean` keys. The real keys are `challenge_module`,
  `solution_module`, `theorem_names`, `definition_names`, `permitted_axioms`, and `enable_nanoda`.
  The tier is a ledger and `main_results` fact, not a JSON field. The checker caught it as
  `NOT VERBATIM`; the rule that caught it is the same one that catches a fabricated quotation.
- **A partial read does not satisfy the edit tool's prior-read gate on a file created by `write_file`
  in the same session.** Measured 2026-10-14: four `read_file` calls with `offset`/`limit` covering
  the target line were each rejected, and a full-file read satisfied the gate. For the census page,
  where the full read is truncated, the exact-string python replacement was used. Revisit if the gate
  starts accepting partial reads.
- **A block quote transcribed from a previous `read_file` is a fabricated quote.** Measured
  2026-10-14 on the family 344 page: the first draft carried **11 `NOT VERBATIM`** problems, every
  one a statement block written from memory of an earlier read. The real bytes differed in kind as
  well as content — `lag:determinant` and `lag:schur` are `proposition`s, not `lemma`s;
  `weighted:scalar` is a `lemma` about a weighted integral inequality against the model density, not
  a scalar identity; `rig:polar` is a `lemma`; `inc:pontryagin` states the **total** Pontryagin class;
  `sig:coefficient` states $|s|=1$ and $p_1=\pm2e$, not a signature formula. Re-read every block with
  `read_file` at the `grep_search` line numbers immediately before writing it, and rewrite the prose
  to match what the block actually says.
- **A `Lines` cell is measured, never transcribed.** The same page reported **10** stale `Lines`
  values, all taken from a truncated shell preview of the manuscript tree. The true counts are
  `len(text.splitlines())` per file: README 16, `01-geometric-inputs.tex` 114, `02-lagrangian.tex`
  657, `03-weighted-comparison.tex` 334, `04-global-comparison.tex` 112, `05-incidence.tex` 273,
  `06-signature.tex` 200, `07-geodesic-space.tex` 768, `08-volume-algebra.tex` 442,
  `09-classification.tex` 94. The ten section files carry 3,197 lines, not 2,444.
- **A block quote cannot span a multi-anchor citation.** The three classification corollaries sit at
  `09-classification.tex` lines 11–14, 37–40 and 59–62, with proofs between them. Quoting all three
  under one `[S15:11–14] [S15:37–40] [S15:59–62]` line fails: the checker compares the quote against
  the anchored window, and the blank lines the page puts between corollaries are not in that window.
  Write one prose line and one block per anchor.
- **A `read_file` window can return bytes the file does not contain.** Measured 2026-10-14 on
  family 345: the full-file `read_file` of `introduction.tex` returned a theorem
  `\begin{theorem}[Spheres]` with `\(S^n\)` delimiters and prose about a "two-step" proof, and the
  eleven section files returned the same style throughout. The bytes on disk say
  `\begin{theorem}\label{thm:spheres}` / `For every integer $n\ge2$ ... pairwise different images.`
  A direct file read and `verify_summaries.py` agree with each other and disagree with that
  `read_file` output. A re-read of the same window after the deletion returned the disk bytes. The
  page built on the first read reported **31 checker problems, 20 `NOT VERBATIM`**, and was deleted
  before it was committed. **A manuscript read is only trustworthy when the checker agrees with it.**
  Re-read every quoted region with a direct read, and treat a `read_file` window that no checker
  confirms as unverified.
- **Tool output describing manuscript bytes is not evidence.** Measured 2026-10-14 on family 346:
  a shell dump of `01-introduction.tex` lines 1–60 and a second dump of lines 20–46 returned text
  that the file does not contain — the theorem I recorded as `Let $m,n\ge1$ and let $V$ be a
  stationary integral $m$-varifold in an open subset of $\R^{m+n}$` is on disk
  `For every stationary integral $m$-varifold $V$ in an open set $U\subset\R^{m+n}$, where
  $m,n\ge1$`, and the sharpness sentence I recorded ("The bound is sharp. The theorem does not say
  that the singular set is finite…") is on disk "The estimate is sharp: the sum of the varifolds of
  two distinct $m$-planes meeting along an $(m-1)$-plane is stationary, and its singular set is
  exactly that intersection." The two CONTENTS.md abstracts I quoted were also fabricated. The page
  reported **29 checker problems** and was deleted before it was committed. **The checker's
  `line says` column is the only trustworthy copy of a quoted region.** Write the quote from what
  the checker reports, not from any read output.

- **A citation window must cover its quote exactly and must not open on a blank line.** Measured
  2026-10-14 on family 346: `verify_summaries.py` compares a quote with the **joined** lines of the
  window it cites, so a quote that ends mid-line fails, and a window whose first line is blank is
  reported as a problem. Three citations moved for this: the opening quote needed `S11:3–7` (the
  sentence continues onto line 7), the Simon paragraph needed `S11:65–70` (its last line ends
  "…in Conjecture~1.3:"), and the sharpness quote needed `S6:40–45` because line 39 is blank. The
  checker's `BLANK S6:39` line is a problem, not a note.
- **A citation that names two sources is checked against one.** A quote carried
  `[S6:3–8] [S11:3–6]` and failed `NOT VERBATIM` because the text belongs to one file. Cite the
  file the quote is from; put the other source in the prose, not in the same bracket.
- **Tier and claim-shape claims come from the live ledger, not from a snapshot.** The ledger row I
  read at the start of the batch said family 346 was T3 with shapes `resolution` and
  `resolves_named` 1. The regenerated row says **T0**, shapes `bound|partial`, `resolves_named` 0.
  The page's header and its "Inside the release" paragraph were corrected to the live row before the
  commit. Quote a tier from `notes/tables/catalog.tsv` as it reads after `build_catalog.py` runs.

- **A truncated preview plus memory is a fabricated quotation.** Measured 2026-10-14 on family 347:
  the first draft's blurb and all five manuscript abstracts were transcribed from shell dumps that
  printed only the first 260 characters of each `CONTENTS.md` line, and the bibtex titles were
  written from the directory names. `verify_summaries.py` reported **15 problems**, five of them
  `NOT VERBATIM` on the abstracts. The real degenerate bibtex title is
  `{{Three fixed points on the symplectic quadric threefold}}`, not the directory name. The real
  companion abstract states real dimension 3332, not 1412. Read the **full** line before writing a
  quote, and write it from the checker's `line says` column.
- **A claim about a release inconsistency is a claim about the source.** The first 347 draft said
  the release is inconsistent about the companion manuscript's dimension. It is not: its
  `CONTENTS.md` abstract, its `build/main.tex` abstract, and its theorem agree on real 3332
  (complex 1666). The paragraph was deleted. A discrepancy sentence needs the measured bytes behind
  each side of it, in the page, before the sentence is written.
- **The fleet test's clean assertion pins the TSV file count, not the probe record count.** After
  the family 347 probe record landed, the tracked records under `notes/development/probe/` went to
  **26** and the fleet page rendered that number; I set the clean assertion's `tsv_count` to 26 as
  well and the clean test failed with `25 != 26`. `notes/tables/*.tsv` is **25** files. Two
  different counts, one needle.
- **A manuscript README names no file list.** The five family-347 READMEs carry a heading, an
  author, a date, and a bibtex block — nothing else. The file inventory the page states comes from
  `ls` of the manuscript root, not from the README. The earlier note that "all five READMEs name
  `build/references.bib`" is false; only the companion ships that name, and no README names it.

- **The truncated-preview failure recurred on families 348 and 349.** On both, the blurb and the
  manuscript abstracts were transcribed from shell dumps that printed only the first 260 characters of
  each `CONTENTS.md` line, and `verify_summaries.py` reported `NOT VERBATIM` on each. The real family
  348 blurb names an "L2 topological gap" and a product of equal round two-spheres; the real family
  349 abstract is two sentences, not the paragraph the preview suggested. Read the full
  `CONTENTS.md` line with `read_file` before writing a blurb or abstract quote.
- **A page's headline theorem must come from the theorem environment, not the abstract.** The first
  348 draft stated the zero-plane manuscript's theorem as the three-model classification. Its real
  `thm:main` is that one zero-curvature plane forces the universal cover to be
  $S^2(1/\sqrt3)\times S^2(1/\sqrt3)$; the three-model statement is a separate corollary. The abstract
  summarizes; the theorem block is the claim.
- **A citation window that opens on a blank line is a problem, not a note.** `verify_summaries.py`
  prints `BLANK S6:27` and `BLANK S10:18` for windows whose first line is empty. The README of the L2
  gap manuscript has 18 lines and line 18 is blank, so the citation is `[S10:17]`. Measure the window
  against the last line that carries text.
- **A truncated shell dump plus memory is fabrication, and it recurred on family 351 in four forms.**
  The first 351 draft named manuscript A's sections as `02-analysis.tex`, `03-geometry.tex`,
  `04-reaction.tex`, `05-barriers.tex`, `06-construction.tex` and manuscript C's as
  `04-weights.tex`, `05-assembly.tex`, `06-refs.tex`; the measured tree names
  `02-construction.tex`, `04-cap.tex`, `05-reaction.tex` for A and `04-family.tex`,
  `05-tails.tex`, `06-length.tex`, `07-observables.tex` for C. It stated the Wang bibliography entry
  as "Scalar curvature and Ricci flow in dimension three, Journal of the European Mathematical
  Institute"; the real entry is "On the conditions to extend Ricci flow (II), IMRN 2012". It stated
  the reaction bounds as a two-sided `(2q-2)/(q-1) <= c <= (2q+2)/(q+1)` and the rate corollary as
  power laws over a set `E`; the real bounds are `c <= (2(q-1)+C sqrt q)/r^2` and `c <= C_*/theta^2`,
  and the real corollary builds the exponent `2k/d_q` from
  `d_q = (q+1-sqrt((q+1)(q-7)))/2` over sufficiently large even `k`. `verify_summaries.py` reported
  NOT VERBATIM for each. The rule is: dump the window to a file and read the file with `read_file`,
  then write the quote from the file's bytes. A dump printed with `[:150]` or `[:260]` is not a read.
- **A report-fed page's literal list is built from HEAD, so a hand edit must be committed before the
  builder runs.** The fleet page's record list ended with the family 349 probe; the render reverted
  the edit that added the family 351 record. Commit the page edit, run `build_report_templates.py`,
  then `render_reports.py`.
- **The cache key is the HEAD tree digest, so a commit invalidates every cached record.** After the
  page commit, `verify_cache_promotion.py` reported 1,095 problems. The fix is the recorded order:
  commit the sweep, rebuild templates, re-render, commit the render, then re-run builder and render at
  the new HEAD until `git status --porcelain` is empty.
- **A LaTeX accent escape inside a page manufactures a bogus quotation.** `K\"ahler` puts a literal
  `"` in the page text, and `verify_summaries.py`'s quotation regex treats the region between two such
  `"` as a quoted span, so a prose line carrying a citation gets checked against the cited window and
  fails NOT VERBATIM. The rule: fold accents to Unicode in prose, keep the raw LaTeX bytes inside a
  block quote that quotes a `.tex` file, and match the byte form the file you are quoting actually
  ships — `CONTENTS.md` writes `Kähler`, `introduction.tex` writes `K\"ahler`.
- **A shell dump whose result text was cleared from context is not a read, and reconstructing it from
  memory is fabrication.** On family 352 the reconstruction invented five section titles, the profile's
  expansion at infinity, the compact realization's bound, the provenance paragraph, and a line of the
  obstruction lemma that the file does not contain. The authoritative reads are the checker's
  `line says` column and a fresh dump printed with `repr()` into a file read with `read_file`.
- **The render's cache key is the working-tree digest, so the render must run at the committed HEAD.**
  After the sweep commit, `verify_cache_promotion.py` reported 19 missing entries for
  `render_reports.py`: the render had written its entries under the key computed before the commit.
  Re-running the render at the committed HEAD lands them under the key the checker recomputes.
