# Proof triage notes

Working ledger for categorizing the catalog's proofs by **what a result claims** and **what
kind of evidence ships with it**. This is a reading tool, not a verification tool.

Regenerate the ledger (a few seconds, no Lean):

```sh
python3 notes/scripts/build_catalog.py      # writes notes/catalog.tsv and prints the report
python3 notes/scripts/triage_t0.py          # buckets the 137 T0 families by claim shape
python3 notes/scripts/verify_summaries.py   # checks every citation in notes/summaries/ against the files it names
python3 notes/scripts/verify_summaries.py --mutant  # same, plus the injected-fault self-test
```

`notes/summaries-workflow.md` is the resume protocol for the summary-page batches: per-page steps,
the batch-boundary gates, stop and escalate rules, and the append-only decision-point record.

## Standing rules

1. **No Lean execution.** `lake`, `lean`, and `comparator` are not run for these notes — a full
   build of the 25.9M-line `OAI/` library is hours on a desktop. Everything here comes from
   static reading of the text metadata that ships in the repo.
2. **Source-level facts stay labeled source-level.** A ledger column records what a file says,
   not what has been checked. `formalization.yaml` states `review: status: unchecked` and
   `automation: methods: [agent]`; that ceiling applies to every coverage number below.
3. **Absence of formalization is not a red flag.** 560 of 722 manuscripts have no formalized
   main result; in a collection that size, "not formalized" carries almost no signal about
   correctness.
4. **Coverage is four layers, never one percentage.** Report them separately.

## The four coverage layers (they do not agree)

| Layer | Source | Count |
|---|---|---|
| Manuscripts with a formalized main result | `formalization.yaml` → `sources:` | 162 / 722 |
| Families with a scope note | `lean/docs/<NNN>.md` | 235 / 372 |
| Statement/solution pairs | `lean/ComparatorChallenges/*.json` | 405 |
| Catalogued main results | `formalization.yaml` → `status.main_results` | 185 entries / 178 unique configs |

Measured agreement worth knowing: **the manuscript layer and the main-results layer agree exactly
at family level.** 127 families have ≥1 formalized manuscript and exactly those 127 have ≥1
config listed in `main_results` — no family has one without the other. The 108 families at T2
have a scope note and comparator links, and zero formalized manuscripts.

## Tiers (`tier` column)

Assigned from the scope note's comparator links (`../ComparatorChallenges/X.lean`) crossed with
`status.main_results`:

| Tier | Meaning | Families |
|---|---|---|
| T3 | ≥1 linked config listed in `main_results` | 127 |
| T2 | linked configs exist, none listed in `main_results` (companion/secondary statements) | 108 |
| T1 | scope note with no comparator link | 0 |
| T0 | no scope note, no challenge, no main result | 137 |

T1 is empty in this catalog: every one of the 235 scope notes links at least one challenge file.
T2 is not a failure — those challenges are companion statements, still linked from a family note.
**All 137 T0 families have zero formalized manuscripts**, so T0 is triaged by claim shape: see
`notes/t0-triage.md`, where two reading passes now cover all 137 families at abstract level
(44 families / 134 manuscripts, then 93 families / 121 manuscripts). `resolves_named` is a second
discriminator there — 88 of the 137 are flagged, including 12 of the 20 families with no shape tag at
all.

## Claim shapes (`shapes` column)

Multi-label tags matched against the family abstract in `overview.tex`. **Not a partition** —
66 families match ≥3 shapes and 57 match none, so `shapes` is a pipe-joined list, not a class.

| Shape | Pattern gist | Families |
|---|---|---|
| uniform | "uniformly", "for every", "arbitrary" | 161 |
| resolution | resolves / proves the conjecture / answers the question / settles | 144 |
| bound | bound, sharp, power-saving, improvement, inequality | 139 |
| counterexample | counterexample, disprove, refute, fails, violation | 44 |
| partial | at most, restricted, in coranks, for fixed, unramified part | 42 |
| classification | if and only if, classified, characterization | 34 |
| density | density | 20 |
| conditional | assuming, we assume, under the … hypothesis, provided that | 5 |
| undecidability | no algorithm, undecidable, unsolvable, negative answer | 4 |

`conditional` families: **014, 125, 240, 244, 282.** The regex only flags them; what each one
actually assumes is read by hand and recorded in **`notes/conditional.md`**, which also lists the
five flags that reading removed. Read that file before calling a family conditional.

Tags omit as well as mislabel. Measured 2026-10-06 while reading the T0 abstracts, and written down as
a rule on 2026-10-07: **74 of 372** families use counterexample language in title or abstract and only
**44** carry the `counterexample` tag; all 30 untagged flags are genuine counterexamples in kind.
Treat every shape count in the table as a floor, not a census. The rule, the 30-family reading, and
the three false positives it excludes (348, 339, 355) are in **`notes/counterexample-tag.md`** — the
2026-10-06 counts were a reading result whose regex was never recorded, and no variant of the
vocabulary quoted in this file reproduces them.

**`counterex_broad` is a column, not a shape.** The phrase rule flags 74 families from title +
abstract, so it is carried in its own column and the `counterexample` shape stays at 44. Widening the
shape instead would move 30 families (6 of them in T0) between the first-match buckets in
`triage_t0.py`; measured, **0 of the 30 flag-only families sit in bucket C**, so first match hides
every one of them. Unlike `resolves_named`, this column is a **strict superset** of its tag (tag-only
0), so 44 and 74 are directly comparable floors. Method, the per-family verdicts, and the decision are
in **`notes/counterexample-tag.md`**.

**`resolves_named` is a column, not a shape.** The broad named-target rule (a target noun
*conjecture/question/problem* plus a resolution verb) flags 233 families, so it is carried in its own
column and the `resolution` shape stays at 144. Widening the shape instead would move families out of
the counterexample/bound/classification/undecidability/density buckets in `triage_t0.py`, which
assigns by first match. The two signals are complementary, not nested: 139 families are flagged by
both, 94 only by the column, and 5 only by the tag (003, 010, 082, 103, 261 — targets named as a
*hypothesis/case/estimate/contrast*), for a union of 238. Both are floors. Method, the 94-family
reading verdict, and the decision are in **`notes/resolution-tag.md`**.

## Columns

| Column | Source | Notes |
|---|---|---|
| `fam` | `overview.tex` `\resultentry{NNN}` | 3-digit family id |
| `discipline` | `\cataloguesection{…}{n}` order | 17 sections; a family belongs to the section above it |
| `title` | `\resultentry` arg 2 | |
| `paps` | `CONTENTS.md` links ∪ `overview.tex` `\href` links | The two mappings agree exactly: 722 links, 0 one-sided |
| `paps_form` | `formalization.yaml` `sources:` ids | Sums to 162 |
| `tier` | scope-note links × `main_results` | See tiers |
| `chal` | comparator links in `lean/docs/<NNN>.md` | |
| `mainres` | of those, count listed in `main_results` | |
| `scope_note` | file exists | 235 total |
| `scope_chars` | length of the `## Scope` section | Rough weight of the exclusions text |
| `verification` | manuscript dirs with a `verification/` subdir | 30 dirs over 22 families |
| `inputs` | manuscript dirs with `INPUTS.md` | 4 dirs over 4 families (057, 157, 251, 259) |
| `covmd` | dirs with `verification/COVERAGE.md` | 2 files, both in family 348 — these bound what a check covers |
| `trace` | `README.md` reasoning-trace table | 10 families; read from the release table, not guessed from filenames |
| `shapes` | abstract keyword match | Multi-label |
| `conditional` | 1 if `conditional` ∈ `shapes` | |
| `resolves_named` | abstract names a conjecture/question/problem **and** uses a resolution verb | 233 families; separate from the `resolution` shape (144) so the T0 buckets stay put |
| `counterex_broad` | title **or** abstract matches the counterexample phrase rule | 74 families; a strict superset of the `counterexample` shape (44), kept out of `shapes` so the T0 buckets stay put |
| `companions` | `result NNN` cross-refs in the abstract | |
| `companion_word` | abstract says "companion" | 10 families |
| `versions` | manuscripts sharing a date-stripped dir slug | 2 families, 4 dated re-issues (003, 056) |
| `summary` | a page exists at `notes/summaries/<discipline>/<NNN>-*.md` | Filesystem fact, not a derived claim; 12 of 372 families, 31 manuscripts behind them |

## Coverage tracks exposure, not importance

Per discipline (fams / scope notes / manuscripts / formalized manuscripts):

| Discipline | fams | notes | paps | form |
|---|---|---|---|---|
| Theoretical computer science | 40 | 32 | 73 | 29 |
| Combinatorics | 37 | 33 | 50 | 19 |
| Algebraic and complex geometry | 36 | 7 | 89 | 7 |
| Number theory | 31 | 16 | 58 | 7 |
| Probability and statistical mechanics | 29 | 19 | 105 | 11 |
| Differential geometry | 29 | 15 | 49 | 11 |
| Mathematical physics | 25 | 17 | 59 | 7 |
| Operator algebras | 19 | 14 | 31 | 6 |
| Algebra | 18 | 9 | 29 | 10 |
| Topology | 18 | 3 | 26 | 1 |
| Real and complex analysis | 16 | 9 | 26 | 7 |
| Partial differential equations | 16 | 11 | 29 | 3 |
| Convex and metric geometry | 15 | 13 | 30 | 13 |
| Group theory | 14 | 12 | 22 | 8 |
| Dynamical systems and ergodic theory | 12 | 9 | 19 | 2 |
| Functional analysis | 11 | 10 | 19 | 16 |
| Mathematical logic | 6 | 6 | 8 | 5 |

The columns sum to 372 / 235 / 722 / 162. Functional analysis (16/19 manuscripts) and mathematical
logic (5/8) are nearly covered; topology (1/26) and algebraic geometry (7/89) are nearly not.

The headline families show the same skew: **001, 002, 004, 006, 010, 011, 014, 016, 018, 019 have
no scope note at all**, while all 10 families with published reasoning traces (007, 017, 087, 102,
159, 197, 221, 271, 287, 362) do. Coverage follows what the release exposed to checking, not what
the community will scrutinize.

## Reading traps (all of these have produced false numbers here once)

- **Parenthesized paths.** `preprints/Sharp-integral-fillings-in-CAT(0)-spaces-…/paper.pdf`.
  Use `preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf`. Excluding `{}` and `\` matters too: a greedy
  match in `overview.tex` otherwise swallows the `}\enspace\textperiodcentered\enspace\href{`
  separator and invents a 723rd manuscript.
- **Namespace-qualified declarations.** `theorem RowColumn.occupied_overlap` inside
  `namespace OAI` is `OAI.RowColumn.occupied_overlap`. Match the qualified tail against file text.
- **`axiom` in prose.** `^\s*axiom\s` hits doc-comment English, not real axioms.
- **`solution_module` is an import shim.** A config's file can be a single `import` line; the
  proof lives in the transitive import closure. Any `sorry`/axiom scan over a shim is meaningless.
- **`rg -f` with patterns ending in `\n`** fails ("the literal `\n` is not allowed in a regex").
- **Keyword tags are not claims.** The `conditional` tag flagged 9 families; reading the abstracts
  showed 5 were not assumptions — "unconditionally" (word boundary), "conditional expectation" and
  "conditional laws" (technical nouns), and "without assuming uniform convexity" (a negation that
  is the theorem's point). Any shape tag needs a reading pass before it is quoted as a property of
  a family. See `notes/conditional.md`.
- **A quoted count with no rule behind it.** The counterexample numbers this file printed for a day
  (74 / 44 / 31 / 30) came from a reading pass whose regex was never written down, and no variant of
  the vocabulary the prose quoted reproduces them (unbounded `negativ` → 90; `\bnegativ` → 75;
  abstract-only phrase rule → 72). A count is only a measurement once the rule that yields it is in
  code. Fixed 2026-10-07 by writing `COUNTEREX_PHRASE` in the generator, which reproduces 74 / 30
  and excludes the three named false positives. See `notes/counterexample-tag.md`.
- **`Path` vs `str` in a membership test.** `verification`, `inputs`, and `covmd` read 0 for all 372
  rows: the reference sets held `Path` objects (`p.parent`) while the tested values were strings
  (`Path(p).parts[-2]`), and `str in {Path(...)}` is false for every family. A column that is
  silently zero is indistinguishable from a column that is genuinely empty unless the generator
  prints the repo-wide sum — which it now does. Fixed 2026-10-06 by keying the reference sets on
  `.name`; the sums are 30 / 4 / 2, and no basename collision exists (30/30, 4/4, 2/2 unique).
- **A coverage file is not coverage.** Family 318 ships `SUPPORT-COVERAGE.md`, which names
  `support/r-ce/ce_certificate.py`, its `.json`/`.txt` transcripts, `BUILDING.md`, and
  `SUPPORT-COVERAGE.json`. None of those paths exist on disk or in git. The ledger has no column for
  `SUPPORT-COVERAGE.md` (1 file repo-wide) and no way to express "named, not shipped".

## Open tasks

Tracked in bd, not in this file: `bd ready` is the live queue, `bd list --status=open` every open
issue, `bd list --status=closed` the completed ones. The checkbox list that used to sit here was a
second copy of the queue and it has been deleted; each completed item is a closed issue whose close
reason carries the outcome, and the detail lives in `notes/conditional.md`, `notes/t0-triage.md`,
and `notes/resolution-tag.md`.
