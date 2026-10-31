[Notes](../../README.md) / [Summaries](README.md) / [Functional analysis](../index/disciplines/functional-analysis.md) / [Family 326](../index/functional-analysis/326-cotype-cotype-conjecture-under-the-approximation-property.md)

# 326 — The cotype–cotype conjecture under the approximation property

[Index page](../index/functional-analysis/326-cotype-cotype-conjecture-under-the-approximation-property.md)

## Original CONTENTS.md summary

[S1:7963] (family entry):

> **326. The cotype–cotype conjecture under the approximation property.** Resolves the cotype–cotype conjecture for real Banach spaces with the approximation property. Such a nonzero space is *K*-convex if and only if both it and its dual have finite Rademacher cotype, with possibly different exponents. Equivalently, these cotype assumptions force nontrivial Rademacher type. ([Lean](../../../lean/docs/326.md))

[S2:750] carries the `\resultentry` with the single manuscript [S3:92, S3:94]. The abstract:

> We prove the cotype–cotype conjecture under the ordinary approximation
property. A nonzero real Banach space with this property is $`K`$-convex
if and only if both the space and its dual have finite Rademacher cotype,
possibly with different exponents. [S3:103–108]

## Undergraduate summary

Banach spaces — infinite-dimensional vector spaces equipped with a
distance (norm) — come in many geometric flavors. Two important
properties are **$`K`$-convexity** (a uniform control on how the space
handles oscillating sign patterns, related to type and cotype
inequalities) and **finite cotype** (a quantitative statement that the
space does not contain "too many" almost-orthogonal directions).

The **cotype–cotype problem** asks: if a Banach space and its dual both
have finite cotype, does the space have to be $`K`$-convex? The answer,
for spaces satisfying a mild technical assumption called the
**approximation property** (roughly, finite-dimensional subspaces can
approximate the whole space), is **yes**. The two exponents needed for
the space and its dual need not be the same. This is, in effect, a
**classification**: the cotype assumption on both sides picks out
exactly the $`K`$-convex spaces with the approximation property.

## Graduate summary

**Main theorem (formalized)** [S3:103–108, S2:750, S4:9].
Let $`X`$ be a nonzero real Banach space with the approximation
property. Then $`X`$ is $`K`$-convex if and only if both $`X`$ and
$`X^*`$ have finite Rademacher cotype, with possibly different
exponents. Equivalently, these cotype assumptions force nontrivial
Rademacher type.

**The approximation property hypothesis** [S4:9].
The formalization assumes the ordinary approximation property:
for every compact set and every tolerance, a finite-rank bounded linear
map approximates the identity on that set. This is the standard
class for which the equivalence was conjectured; the theorem does
not assert the result without this hypothesis.

**The formalization** [S4:9, S5, S6].
The scope note selects the cotype–cotype equivalence under the
approximation property. The comparator stub
`Cotype.lean` (60 lines) defines `KConvex`, `HasCotype q`,
`FiniteCotype`, `ApproximationProperty`, and `MainTarget`, and states
`theorem mainTarget_proved [Nontrivial X] : MainTarget X` at [S5:53]
with the body a `sorry` at [S5:54]. The proved OAI declaration is
`OAI.Cotype.mainTarget_proved` at `Main.lean` [S6:26], with a 125-file
OAI tree under `lean/OAI/Analysis/Cotype/` carrying 0 `sorry`.

## History of the conjecture

The **cotype–cotype conjecture** is a problem in Banach-space geometry
concerning the relationship between three properties: $`K`$-convexity,
finite cotype of the space, and finite cotype of the dual. The
approximation property is a standard hypothesis in Banach-space theory
that rules out pathological spaces (the famous Enflo space of 1973 was
the first Banach space without the approximation property).

The result resolves the conjecture in the affirmative for the class of
real Banach spaces with the approximation property. The equivalence is
a **classification** in the sense that it characterizes exactly which
spaces in this class are $`K`$-convex: those and only those whose dual
also has finite cotype.

**Prior (my training data, not this repo).** $`K`$-convexity, cotype, and
the approximation property are classical topics in Banach-space theory.
The partial results relating these properties for subclasses (Hilbert
spaces, $`L^p`$ spaces, spaces with unconditional bases) are known. A
full equivalence under the approximation property, with the
nontrivial-type consequence, is the novel contribution claimed here; I
cannot verify the cotype and $`K`$-convexity estimates independently from
training alone.

## Consequences

- **The cotype–cotype conjecture is resolved** [S3:103–108, S2:750,
  S4:9]: for a nonzero real Banach space with the approximation
  property, $`K`$-convexity is equivalent to finite cotype of both the
  space and its dual. This is the named resolution the ledger's
  `resolves_named` flag records.
- **A classification under the approximation property** [S3:103–108,
  S2:750]: the cotype-on-both-sides condition characterizes exactly the
  $`K`$-convex spaces with the approximation property.
- **Nontrivial Rademacher type follows** [S3:103–108, S2:750]: the
  cotype assumptions force nontrivial Rademacher type, an additional
  geometric consequence of the equivalence.
- **The exponents need not match** [S3:103–108, S2:750]: the space and
  its dual may have finite cotype with different exponents; no
  uniformity of exponent is required.

## Section skeleton

One manuscript [S3:103–108]. Root `build/main.tex` (117 lines;
`\documentclass` at [S3:1], an extensive glyph-mapping block through
[S3:62], inline preamble through [S3:92], title at [S3:92], date at
[S3:94]). Seven `input` files at the end: `introduction`,
`preliminaries`, `coefficient`, `walsh`, `approximation`,
`consequences`, `references`. **No verification bundle.**

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S4:9], one comparator stub [S5], one `main_results` entry, and a
proved OAI tree. The T3 shape is "scope note, comparator stub,
`main_results` entry, and proved OAI tree all present."

The scope note [S4:9] selects the cotype–cotype equivalence under the
approximation property: for every nonzero real Banach space with the
approximation property, $`X`$ is $`K`$-convex exactly when both
$`X`$ and $`X^*`$ have finite cotype.

The single comparator stub carries 1 `sorry`:
`Cotype.lean` (60 lines) with
`theorem mainTarget_proved [Nontrivial X] : MainTarget X` at [S5:53]
and the `sorry` at [S5:54]. The stub defines the key predicates:
`KConvex` (existence of a constant controlling the Rademacher
projection), `HasCotype q` (the $`q`$-cotype inequality for
Rademacher sums), `FiniteCotype` (existence of some
`HasCotype q`), `ApproximationProperty` (finite-rank approximation of
the identity on compact sets), and `MainTarget` (the equivalence
under the approximation property and nontriviality).

The proved OAI declaration is `OAI.Cotype.mainTarget_proved` at
`lean/OAI/Analysis/Cotype/Main.lean` [S6:26]. The OAI tree under
`lean/OAI/Analysis/Cotype/` comprises 125 `.lean` files with 0
`sorry` occurrences — the cotype–cotype equivalence is proved in the
OAI library. The reading is of source text only.

**Tree measurement (source-level).**

The `main_results` entry OAI.Cotype.mainTarget_proved resolves to `OAI/Analysis/Cotype/Main.lean` (34 lines); the top-level theorem is `theorem kConvex_of_nontrivialType (h`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 125 files, 651 theorems, 182 defs.

The preprint states 11 theorem environments; the tree carries 59× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=326` [S7] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=302`, `verification=0`, `trace=`. The T3
shape is "scope note, comparator stub, `main_results` entry, and proved
OAI tree." The single comparator stub carries 1 `sorry`; the proved
OAI tree carries 0. The shape flags are
`shapes=resolution|classification`, `resolves_named=1`,
`counterex_broad=0`, `covmd=0` — a resolution-and-classification
family recording the cotype–cotype equivalence, with no coverage
document in the manuscript directory.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7963] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 326 at [S2:750] |
| S3 | [`preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/build/main.tex`](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/build/main.tex) | 117 | manuscript; title [S3:92], date [S3:94], abstract [S3:103–108] |
| S4 | [`lean/docs/326.md`](../../../lean/docs/326.md) | 15 | scope note — Scope at [S4:9] and the comparator link `Cotype.lean` |
| S5 | [`lean/ComparatorChallenges/Cotype.lean`](../../../lean/ComparatorChallenges/Cotype.lean) | 60 | comparator stub — 60 lines, 1 `sorry` |
| S6 | [`lean/OAI/Analysis/Cotype/Main.lean`](../../../lean/OAI/Analysis/Cotype/Main.lean) | 34 | proved OAI declaration `OAI.Cotype.mainTarget_proved` [S6:26] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=326`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
