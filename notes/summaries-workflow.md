# Summary-page production loop

The resume protocol for the `math-ckd` batches. Read this after a compaction; it is the state
carrier, so it states what to do and what not to re-derive.

## Loop shape

One parent agent, sequential. **No subagents** — the box is a single GPU and switching context
per subagent turn costs more than the parallelism buys.

A batch is one bd issue. Per page, in this order:

1. `bd update <id> --claim` (once per batch).
2. `ls` the manuscript root before the page says what it ships.
3. Read the manuscript, the scope note, the YAML block, the challenge JSON, the trace if any.
4. Write the page in the format fixed by the `family-summary` skill.
5. Self-verify: every quotation against the lines it cites, every count against the file.
6. `python3 notes/scripts/verify_summaries.py --mutant` — green, zero problems.
7. Declare every Sources row, or delete it.
8. Regenerate the ledger; the `summary` column must flip to 1 for this family.
9. Commit.
10. `bd close <id> --reason "<outcome>"` at the end of the batch.

## Gates (run at every batch boundary, quote numbers only from this run)

```
python3 notes/scripts/build_catalog.py > /tmp/r1.txt && cp notes/catalog.tsv /tmp/c1.tsv
python3 notes/scripts/build_catalog.py > /tmp/r2.txt && cp notes/catalog.tsv /tmp/c2.tsv
diff /tmp/c1.tsv /tmp/c2.tsv && diff /tmp/r1.txt /tmp/r2.txt     # must be byte-identical
python3 notes/scripts/verify_summaries.py --mutant                # zero problems
```

Reconciliation lines that must not move: 372 families, 722 manuscripts, 162 formalized,
405 challenges, 185 `main_results` entries over 178 configs, 235 scope notes, and both
`overview.tex` ↔ `CONTENTS.md` cross-checks reading 0. The discipline table must sum to
372 / 235 / 722 / 162.

## Stop and escalate

- **Stop the batch** when a gate fails twice on the same page. Two failures mean the checker or
  the format is wrong, not the page; fix that first, in its own commit.
- **Stop the run** when a P1/P2 issue becomes ready. Summaries are P4 and rank below them.
- **Never write an ungroundable page.** Record the family in `notes/summaries-blocked.md` with
  the specific reason (what the sources do not state) and leave its `summary` row 0.
- **Ambiguity:** record the decision point below with the provisional choice and what would force
  a revisit, then keep going. If it is critical, or fixing it later means rewriting pages,
  claim a different bead and come back.

## Tiers (measured from the ledger, 2026-10-07)

| Tier | Families | Manuscripts | Definition |
|---|---|---|---|
| A | 21 | 60 | 10 trace families, 9 headline T0 from `t0-triage.md`, plus 001 and 032 (done) |
| B | 80 | 120 | remaining T0 families with `resolves_named = 1` |
| C | 271 | 542 | everything else, split into 132 families / 273 manuscripts (five largest disciplines: algebraic and complex geometry, number theory, combinatorics, topology, differential geometry) and 139 families / 269 manuscripts (the remaining twelve) |

Trace families: 007, 017, 087, 102, 159, 197, 221, 271, 287, 362 (22 manuscripts).
Headline T0: 002, 004, 006, 010, 011, 014, 016, 018, 019 (29 manuscripts).
T0 is 137 families and 255 manuscripts, so tier C is 271 families: 137 − 11 + 127 + 108 − 10.

## What not to re-derive

- Page format, citation grammar, the repo-relative File cell, the block-quote rule, the
  PDF/quote rule: `.qwen/skills/auto-skill-family-summary-citation-verified/SKILL.md`.
- Cost model: 001 (1 manuscript → 15 sources, 173 markers, 9 quoted spans) and 032
  (8 manuscripts → 32 sources, 272 markers, 52 quoted spans). Sources ≈ 4 per manuscript.
- `bd ready` is the only task tracker; nothing here is a task list.
- Never run `lake`, `lean`, `lake exe cache get`, or `comparator`.

## Decision points

Provisional choices, with what would force a revisit. Not tasks — a revisit that needs work gets
a bd issue.

- **History/Consequences depth.** Pages carry these only when grounded in the manuscript, the
  scope note, or the trace. A prior-based framing is labelled as a prior. Revisit if a page reads
  as empty; the fix is `math-el4.6`, not invention.
- **Tier C order within a batch.** Chosen by ascending manuscript count. Revisit if the small
  families turn out to be the expensive ones.
- **Companion families.** A page cites its companion by number and links the companion's page
  when one exists; it does not duplicate the companion's content. Revisit if cross-linking
  starts producing circular sources tables.
- **Dated re-issues** (`versions > 0`). One page per family; the Sources table lists the
  manuscript tree, not each dated copy. Revisit if a re-issued manuscript differs in content.
