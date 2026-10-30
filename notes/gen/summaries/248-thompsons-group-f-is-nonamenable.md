[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 248](../index/group-theory/248-thompsons-group-f-is-nonamenable.md)

# 248 — Thompson's group $F$ is nonamenable

[Index page](../index/group-theory/248-thompsons-group-f-is-nonamenable.md)

## Original CONTENTS.md summary

[S1:6144] (family entry):

> **248. Thompson's group $`F`$ is nonamenable.** Proves that Thompson's group $`F`$, the group of dyadic piecewise linear homeomorphisms of the interval, is nonamenable, resolving its longstanding amenability problem. ([Lean](../../../lean/docs/248.md))

[S2:585] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**Thompson's group $`F`$ is nonamenable** [S3:4, S3:6]:

> We prove that Thompson's group $`F`$ is nonamenable. This confirms
Geoghegan's conjecture and resolves the amenability problem for $`F`$. [S3:10–13]

## Undergraduate summary

**Thompson's group** $`F`$ is a group of transformations of the unit
interval: you cut the interval into subintervals whose endpoints
are dyadic rationals (fractions like $`1/2`$, $`1/4`$, $`3/8`$), and
slide each subinterval to a new position using a linear map. The
result is a new piecewise-linear function. Composing two such
functions gives a third, and the set of all such functions forms
a group under composition. **Amenability** is a property of
groups that measures whether the group "admits an averaging
process" — informally, whether you can assign a fair
average to every bounded function on the group in a way that
respects the group's symmetry. The result proves that $`F`$
is **not** amenable [S3:10–13, S2:585].

## Graduate summary

**Nonamenability of Thompson's group $`F`$**
[S3:10–13, S2:585]. Thompson's
group $`F`$, the group of dyadic piecewise-linear homeomorphisms of
$`[0,1]`$, is nonamenable: it does not admit a positive normalized left-
invariant mean on bounded real functions. This confirms Geoghegan's
conjecture and resolves the amenability problem for $`F`$.

## History of the conjecture

**Thompson's groups**
$`F`$, $`T`$, and $`V`$ were introduced by Thompson in 1965 as examples of
groups with unusual properties. $`F`$ is the smallest of the three and has
been one of the most studied groups in geometric group theory. The
**amenability problem** for $`F`$ — whether $`F`$ admits a left-invariant
mean — was a long-standing open question. $`F`$ is torsion-free, has a
finite presentation, is simple in its commutator subgroup, and has many
other exotic properties, yet its amenability status remained unknown.
**Geoghegan's conjecture** predicted that $`F`$ is nonamenable. The result
[S3:10–13] confirms this conjecture, resolving the amenability problem.

**Prior (my training data, not this repo).** Thompson's group $`F`$, its
definition as piecewise-linear homeomorphisms, and the general question
of amenability for finitely presented groups are standard. The proof of
nonamenability for $`F`$, confirming Geoghegan's conjecture, is the novel
contribution. I cannot confirm this independently from training alone.

## Consequences

- **Nonamenability
of $`F`$** [S3:10–13]: Thompson's group $`F`$ does not admit a positive
normalized left-invariant mean on bounded real functions.
- **Geoghegan's
conjecture confirmed** [S3:10–13]: the 1990s conjecture that $`F`$ is
nonamenable is proved, resolving the amenability problem for $`F`$.

## Section skeleton

One manuscript: [S3:10–13] (title [S3:4], date [S3:6]) — `main.tex` under
`build/`. The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S4],
one comparator stub [S5], and one `main_results` entry [S7]. The scope
note [S4:9] states the target: the amenability problem for Thompson's
group $`F`$ — whether it admits a positive normalized left-invariant mean
on bounded real functions. The formalized result rules out such a mean
for the standard group of dyadic piecewise-linear homeomorphisms of the
interval, proving nonamenability. No explicit boundary constant or
prescribed generating set is given.

The `main_results` entry [S7:1731–1733] names
`OAI.ThompsonNonamenability.thompson_F_nonamenable_composition` in
`lean/OAI/GroupTheory/Thompson/Main.lean`. In the source, the theorem
`thompson_F_not_amenable` [S6:65] states the negation of amenability
directly, and `thompson_F_nonamenable_composition` [S6:69] is the
composition form named by the `main_results` entry. `grep` finds
**zero** `sorry` in the whole `lean/OAI/GroupTheory/Thompson/` tree.

The one comparator stub [S5] states the nonamenability target and ends
in `sorry`. The proved copy lives under `lean/OAI/`. A comparator stub
is a target the release set itself; the proved version, where it exists,
lives under `lean/OAI/`. The reading is of source text only — no `lake`
or `lean` run elaborates the proof.

## Coverage

The ledger row `fam=248` [S8] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `verification=0`, `trace=`. The `paps_form=1` against
`paps=1` is the coverage signature: the single manuscript is named as a
formalization source, and the single `main_results` entry over that
config reaches the full nonamenability claim. The comparator stub names
the same target, and the proved copy lives under `lean/OAI/`. There is
no verification bundle and no reasoning trace. The shape flags are
`resolution`, and `resolves_named=1` — the blurb names the amenability
problem with "resolving".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6144] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 248 at [S2:585] |
| S3 | [`preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/main.tex`](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/main.tex) | 24 | manuscript 1 of 1; title [S3:4], date [S3:6], abstract [S3:10–13] |
| S4 | [`lean/docs/248.md`](../../../lean/docs/248.md) | 15 | scope note — the formalization's Scope at [S4:9] and its one comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/ThompsonNonamenability.lean`](../../../lean/ComparatorChallenges/ThompsonNonamenability.lean) | 89 | comparator stub — the nonamenability target with its `sorry` |
| S6 | [`lean/OAI/GroupTheory/Thompson/Main.lean`](../../../lean/OAI/GroupTheory/Thompson/Main.lean) | 82 | the formalized file — `thompson_F_nonamenable_composition` at [S6:69] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.ThompsonNonamenability.thompson_F_nonamenable_composition`, at [S7:1731–1733] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=248`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
