# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction: it is the state carrier,
so it states what to do and what not to re-derive. The method (page format, citation grammar, the
measured quotation traps) lives in `.qwen/skills/auto-skill-family-summary-citation-verified/` —
`references/quotation-traps.md` carries the 39 shipped pages' defects, the last section being the
2026-10-14 batch.

## Current state (rewritten at every batch boundary, 2026-10-15)

- **All 42 pages are green.** `verify_summaries.py` over the 43 files in `notes/summaries/`: **5,816 marker positions, 1,530 quoted spans, 0 problems**; `check_summary_manuscripts.py`: **43 pages, 0 with an off-family manuscript, 98 manuscript dirs named, 0 unnamed-on-catalog, 0 named-by-another-family**; 749 preprint dirs on disk, 719 named by `overview.tex`, 30 on disk and unnamed, 0 named and absent. `test_summaries.py`: **12 tests pass**.
- **Pages done (42):** 001, 002, 004, 006, 007, 010, 011, 014, 016, 017, 018, 019, 032, 039, 042, 087, 101, 102, 109, 136, 147, 159, 197, 221, 226, 258, 259, 271, 287, 331, 332, 334, 342, 344, 345, 346, 347, 348, 349, 351, 352, 362. The ledger's `summary` column is 1 for those; the generator reports "summary pages 42 of 372 families, 98 manuscripts behind them". By discipline: Number theory 12, differential geometry 10, algebraic and complex geometry 3, theoretical computer science 3, convex and metric geometry 2, probability and statistical mechanics 2, group theory 2, functional analysis 2, and one each in dynamical systems and ergodic theory, combinatorics, algebra, mathematical physics, operator algebras, and partial differential equations.
- **Next batch:** `math-ckd.4` is claimed and in progress — tier C group 1. The differential-geometry families with `summary = 0`, sorted by `paps`: 353, 354, 355, 356, 357, 358, 359, 360, 361, 350. Steps 1–10 per page. Check `bd ready` first: summaries are P4 and any ready P1/P2 outranks this batch.
- **Last gate run (2026-10-15):** `bash notes/scripts/gate_driver.sh` — **rows 79, failures 0**, head diff 0 bytes. Reconciliations: 372 families, 719 manuscripts, **173** formalized (`formalized (yaml)`), 242 scope notes, 416 challenges, 200 `main_results` over 189 configs, both `overview.tex` ↔ `CONTENTS.md` cross-checks 0. `verify_cache_promotion.py`: **writers 15 + non-cached 1, probed targets 16, problems 0**. `check_index_links.py`: **1,033 pages, 66,131 links, 0 broken**. The gate does not run the lint trio; `bash notes/scripts/lint_scripts.sh` measured separately at HEAD: **ruff exit 0, mypy exit 0, pylint exit 0**.
- **Push state:** `origin/notes` at `4f3ce3c8e`, pushed 2026-10-15 — the ruff gate made green (10 autofixes, 11 `pad_cells` rewrites for PLW2901, 7 ISC001 joins, 1 `noqa` move, ISC002 exempted with its 9 sites and the reason), the env site anchor the ruff fix moved landed at `render_reports.py:1221`, and the beads store close of `math-95a`. The gate run reported **79 rows, 0 failures**, `verify_cache_promotion.py` reported **0 problems** at the pushed HEAD, and the lint trio measured separately exits 0 on all three tools.
- **Queue check (2026-10-15):** `bd ready` lists **1** issues: `math-ckd.5` and `math-ckd`.
  `math-95a`, `math-4nn` and `math-6wg` (the lint trio) are closed, so none is in the ready list;
  `math-ckd.4` is claimed and in progress. Bead `.2`'s prettier
  decision is resolved: prettier is dropped from the repo, so the formatable set is gone.

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

**The cache key is the HEAD tree digest, so a commit invalidates every record.** Run
`build_report_templates.py` after every commit, then `render_reports.py`, then prove
`git status --porcelain` is empty. A render at the pre-commit HEAD lands its entries under a key the
checker no longer recomputes, and `verify_cache_promotion.py` reports the mismatch. A report-fed page's
literal list is built from HEAD, so a hand edit to a template-fed page is reverted by the render: commit
the page edit, rebuild the template, re-render.

**A new page drifts the seeder's L1 tree.** `seed_quotes.py`'s L1 is the `notes/summaries` tree, so a
new page makes the newest record stale. Re-probe `seed_quotes.py` after a page lands, and add the record
to `verify_cache_promotion.py`'s `PROBES` list, newest first.

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