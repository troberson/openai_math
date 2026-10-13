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
