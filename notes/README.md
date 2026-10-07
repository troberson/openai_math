# Proof triage notes

Working ledger for categorizing the catalog's proofs by **what a result claims** and **what
kind of evidence ships with it**. This is a reading tool, not a verification tool.

Regenerate the ledger (a few seconds, no Lean):

```sh
python3 notes/scripts/build_catalog.py      # writes notes/catalog.tsv and prints the report
```

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

## Claim shapes (`shapes` column)

Multi-label tags matched against the family abstract in `overview.tex`. **Not a partition** —
67 families match ≥3 shapes and 57 match none, so `shapes` is a pipe-joined list, not a class.

| Shape | Pattern gist | Families |
|---|---|---|
| uniform | "uniformly", "for every", "arbitrary" | 161 |
| resolution | resolves / proves the conjecture / answers the question / settles | 144 |
| bound | bound, sharp, power-saving, improvement, inequality | 139 |
| counterexample | counterexample, disprove, refute, fails, violation | 44 |
| partial | at most, restricted, in coranks, for fixed, unramified part | 42 |
| classification | if and only if, classified, characterization | 34 |
| density | density | 20 |
| conditional | assuming, we assume, under the … hypothesis, provided that | 9 |
| undecidability | no algorithm, undecidable, unsolvable, negative answer | 4 |

`conditional` families: **014, 023, 125, 133, 224, 240, 244, 290, 328.** The regex only flags
them; what each one actually assumes has to be read by hand (open task, below).

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
| `verification` | manuscript dirs with a `verification/` subdir | 30 repo-wide |
| `inputs` | manuscript dirs with `INPUTS.md` | 4 repo-wide |
| `covmd` | dirs with `verification/COVERAGE.md` | 2 repo-wide — these bound what a check covers |
| `trace` | `README.md` reasoning-trace table | 10 families; read from the release table, not guessed from filenames |
| `shapes` | abstract keyword match | Multi-label |
| `conditional` | 1 if `conditional` ∈ `shapes` | |
| `companions` | `result NNN` cross-refs in the abstract | |
| `companion_word` | abstract says "companion" | 10 families |
| `versions` | manuscripts sharing a date-stripped dir slug | 2 families, 4 dated re-issues (003, 056) |

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

## Open tasks

- [ ] Manual pass on the 9 conditional families — record exactly what each assumes, in a
      `notes/conditional.md` (regex flags them; only reading names the hypothesis).
- [ ] Read the 2 `verification/COVERAGE.md` limits files and record what each arithmetic check
      does *not* cover.
- [ ] Triage the 137 T0 families by claim shape — that is where the taxonomy earns its keep,
      since coverage signals are absent there.
- [ ] Cross-check the 44 counterexample families against `main_results`: a counterexample is the
      claim type most likely to be checkable cheaply and hardest to argue about.
