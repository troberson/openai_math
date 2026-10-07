---
name: proof-triage
description: >-
  Categorize the proofs in the OpenAI Research Catalog by claim shape and by the evidence that
  ships with each result family, using the git-tracked ledger at notes/catalog.tsv. Use when
  asked what kind of result a family is (resolution, bound, counterexample, classification,
  conditional, undecidability), how much of a family is formalized, which families have scope
  notes, comparator challenges, reasoning traces, or verification dirs, how to triage the
  unformalized families, or any question about the formalization coverage gap. Triggers on
  "triage", "categorize these proofs", "claim shape", "tier", "coverage", "scope note",
  "comparator challenge", "reasoning trace", and family numbers NNN. Static reading only: never
  run lean, lake, or comparator.
compatibility: "python3 (stdlib only); no Lean toolchain, no network"
metadata:
  author: tamara
  version: "1.6"
---

# Proof triage

Router for working with the catalog ledger. Deep detail lives in `notes/README.md`; this body is
behaviour and rules only.

## When to activate

- A question about a family number (`003`, `197`, …): what it claims, how covered it is.
- Grouping, filtering, or counting results by claim type.
- Asking how much of the collection is formalized, or what the coverage gap means.
- Choosing which families deserve a manual reading pass.

## Standing rules (enforce these in every answer)

1. **Never run Lean.** No `lake`, `lean`, `comparator`, `cache get`. The library is 25.9M lines;
   a build is hours on a desktop and buys nothing for categorization. Regenerate the ledger with
   `python3 notes/scripts/build_catalog.py` (seconds).
2. **Source-level ≠ verified.** Quote `formalization.yaml` verbatim when making a verification
   claim: `scope: "Partial progress."`, `automation.methods: [agent]`, `review.status: unchecked`.
   Zero `sorry` in source is a source-level fact, not a comparator pass. Say which one you have.
3. **Four layers, never one percentage.** Manuscripts 162/722 · families with scope notes 235/372
   · challenges 405 · main_results 185 entries / 178 unique configs. Do not average them.
4. **Absence of formalization is not a red flag.** 560 of 722 manuscripts are unformalized.
5. **Claim shape is multi-label.** 66 families match ≥3 shapes, 57 match none. Never present the
   taxonomy as a partition; report the tag set.
6. **A tag is not a claim, and tags omit as well as mislabel.** Keyword tags need a reading pass
   before you call a family by them: the `conditional` tag flagged 9 families, 5 of which were not
   assumptions. In the other direction, 74 families use counterexample language and only 44 carry
   the `counterexample` tag — all 30 untagged flags are genuine on reading. Quote shape counts as
   floors. `notes/conditional.md` is the model — name the hypothesis, say where it sits, record the
   flags you dropped.
7. **A broad rule goes in a column, not a shape.** `triage_t0.py` assigns T0 buckets by **first
   match**, so widening a shape moves families between buckets and re-cuts the reading order. Both
   broad rules therefore ship as columns: named-target resolution as `resolves_named` (233 families
   against the `resolution` shape's 144 — complementary, not nested: 139 in both, 94 column-only, 5
   tag-only 003, 010, 082, 103, 261, union 238), and the counterexample phrase rule as
   `counterex_broad` (74 against the `counterexample` shape's 44 — a **strict superset**, tag-only 0).
   Widening `counterexample` would move 6 T0 families into bucket C, where first match currently
   leaves them. Quote both counts as floors; see `notes/resolution-tag.md` and
   `notes/counterexample-tag.md`.
8. **A prior is not a measurement.** `notes/conjecture-standing.tsv` records what the assistant's
   training data says about a conjecture's standing at an early-2025 cutoff, self-rated by
   `prior_confidence`. Quote it as the prior it is, pair every row with its confidence, and never
   present a surprise tier as a property of the result. No row may assert consequence: only 14 of 372
   family titles appear in the corpus's `.bib` files, so consequence is external by construction.
   Run `notes/scripts/verify_conjecture_standing.py` before quoting rows.

## Workflow

1. **Refresh** — run the generator; read its report. Every number quoted in `notes/README.md`
   comes from that report, so re-run before quoting counts.
2. **Look up** — filter `notes/catalog.tsv` by `fam`, `tier`, `shapes`, `resolves_named`,
   `counterex_broad`, `discipline`, `trace`. Parse with `csv.DictReader(..., delimiter='\t')`, not
   `split(',')`.
3. **Read the primary text** — the ledger is an index, not the evidence. For any claim about what
   a result *says*, open `lean/docs/<NNN>.md` (its `## Scope` section states exclusions) and the
   manuscript abstract in `CONTENTS.md`. Quote exclusions; they are the load-bearing part.
4. **Triage the silent families** — T0 (137 families, 255 manuscripts, 0 formalized) has no
   coverage signal at all. Run `notes/scripts/triage_t0.py` for the buckets and read
   `notes/t0-triage.md` before adding to the pass; `shapes` drives the buckets,
   `resolves_named` (88 of 137) is the second discriminator and `counterex_broad` (22 of 137) the
   third — 6 of those 22 sit outside bucket C, which is why the column exists. Two
   reading passes cover all 137 families at abstract level, and the 21 counterexample-shaped ones are
   recorded there with object, broken conjecture, and construction mode — new T0 work is checking
   those claims against manuscript source, not reading titles.
5. **Record manual findings in the repo**, not in chat: append to `notes/` as a tracked file
   (e.g. `notes/conditional.md`), one row per family, stating exactly what each assumes.
6. **State the ceiling** — end coverage answers with what has *not* been checked.

## Resource map

| Path | What it is | Read when |
|---|---|---|
| `notes/catalog.tsv` | 372-row ledger, 22 columns, one row per family | Any lookup, filter, or count |
| `notes/README.md` | Column definitions, tier defs, shape yields, discipline table, traps | Before quoting any number |
| `notes/scripts/build_catalog.py` | Generator (stdlib only, ~300 lines) | Regenerating, or adding a column |
| `notes/scripts/triage_t0.py` | Buckets the 137 T0 families by claim shape (reads the ledger, writes nothing) | Any T0 count, bucket, or priority question |
| `notes/t0-triage.md` | T0 buckets, two reading passes covering all 137 families, the 21-family counterexample record, scope qualifiers found in abstracts | Before triaging or discussing T0 families |
| `notes/conditional.md` | Manual pass: what each conditional family assumes, and dropped flags | Before calling any family conditional |
| `notes/resolution-tag.md` | Named-target rule: yield, the 94-family reading verdict, the `resolves_named` decision | Before quoting a resolution count or changing a tag |
| `notes/counterexample-tag.md` | Counterexample phrase rule: yield, the 30-family reading verdict, the `counterex_broad` decision | Before quoting a counterexample count, or checking a family the tag misses |
| `notes/conjecture-standing.tsv` | 139 rows: named conjecture, **training-data prior** on its standing as of early 2025, `prior_confidence`, the release claim, the gap, surprise tier, `overview.tex` anchor | Any "how surprising is this" or conjecture-standing question |
| `notes/conjecture-standing.md` | The tier scheme, the 139-vs-233 selection, the counts, the 145 conflict row, what the table cannot say | Before quoting a standing row as evidence |
| `notes/scripts/verify_conjecture_standing.py` | Proves the standing table: fam set, ledger discipline/tier, anchors against `\resultentry`, confidence vocabulary, abstract-name fidelity, no consequence language | Before quoting any standing row |
| `lean/docs/<NNN>.md` | Family scope note: what the formalization covers and excludes | Any claim about a formalized result |
| `lean/ComparatorChallenges/*.json` | Statement/solution pairs, `permitted_axioms` | Checking what a challenge permits |
| `lean/formalization.yaml` | `sources`, `status.main_results`, `automation`, `review` | Coverage and verification-ceiling claims |
| `README.md` (repo root) | Reasoning-trace → family table (authoritative) | Attributing traces; never guess from filenames |

## Known traps (each has produced a false number here once)

- Parenthesized paths — `preprints/…-CAT(0)-spaces-…/paper.pdf`. Regex must exclude
  whitespace, parens, `{}`, `\` and allow `(\d+)`: see `PAP` in the generator.
- Namespace-qualified declarations — `OAI.RowColumn.occupied_overlap` is declared as
  `theorem RowColumn.occupied_overlap` inside `namespace OAI`.
- `axiom` inside `/- … -/` doc-comments is English prose, not an axiom.
- `solution_module` is an import shim — a one-line file. Any `sorry` scan of a shim proves nothing;
  the proof is in the transitive import closure.
- `rg -f patterns.txt` with patterns ending in `\n` fails, even with `-U`.
- `conditional` in an abstract is often not a hypothesis: "conditional expectation",
  "conditional laws", "without assuming X", and "unconditionally" (no word boundary inside it) all
  matched the naive pattern. Guard with `ASSUME`/`NEG_BEFORE`/`TECH_AFTER` in the generator, then
  read the flagged abstracts.
- Tags omit as well as mislabel. The `counterexample` tag matches 44 families while 74 use
  counterexample language; reading the 30 untagged flags found all 30 genuine. The phrase rule that
  reproduces 74 excludes three false positives by requiring a phrase, not a stem: 348
  ("nonnegatively"), 339 ("strictly negative sectional curvature"), 355 ("at every negative time"). A
  tag count is a floor: check the untagged set before quoting a shape count as a census.
- A quoted count with no rule behind it. The 74 / 44 / 31 / 30 figures this repo quoted for a day came
  from a reading pass whose regex was never written down, and no variant of the vocabulary the prose
  quoted reproduces them (unbounded `negativ` → 90, `\bnegativ` → 75, abstract-only phrase rule → 72).
  Write the rule in code before quoting the count; see `notes/counterexample-tag.md`.
- `Path` vs `str` in a membership test. `verification`, `inputs`, and `covmd` read 0 for all 372
  rows because the reference sets held `Path` objects while the tested values were strings — a
  silently empty column, indistinguishable from a genuinely empty one. Key such sets on `.name`, and
  quote the repo-wide sum the generator prints (30 dirs / 22 families, 4, 2) rather than a row count.
- A coverage document is not coverage. Family 318's `SUPPORT-COVERAGE.md` names a `support/r-ce/`
  certificate bundle, `BUILDING.md`, and `SUPPORT-COVERAGE.json`; none exist on disk or in git. When
  a family ships a coverage statement, check that the artifacts it names are present before
  describing the family as having support.

## Related skills

For measuring coverage of a manuscript collection against a Lean library in general (import
closure, zero-`sorry` interpretation, comparator commands), see the
`auto-skill-lean-formalization-coverage-audit` skill. This skill is the working ledger for this
repo; that one is the measurement method.
