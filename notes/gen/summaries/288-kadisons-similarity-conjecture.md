[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 288](../index/operator-algebras/288-kadisons-similarity-conjecture.md)

# 288 — Kadison's similarity conjecture

[Index page](../index/operator-algebras/288-kadisons-similarity-conjecture.md)

## Original CONTENTS.md summary

[S1:7184] (family entry):

> **288. Kadison's similarity conjecture.** Proves Kadison's similarity conjecture: every bounded complex-linear unital algebra homomorphism from a unital complex *C*^*-algebra to operators on a Hilbert space becomes a *$`*`$*-homomorphism after conjugation by a bounded invertible operator. ([Lean](../../../lean/docs/288.md))

[S2:670] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript [S3:3, S3:5]:

> We prove that every bounded complex-linear unital algebra homomorphism from a unital
complex $`C^*`$-algebra into the bounded operators on an arbitrary Hilbert
space is similar to a $`*`$-homomorphism. This resolves Kadison's similarity
conjecture positively. We also obtain one universal hyperreflexivity constant
for all unital von Neumann algebras on arbitrary complex Hilbert spaces. [S3:8–14]

## Undergraduate summary

A **C*-algebra** is a mathematical structure that generalizes the algebra of
operators on a Hilbert space and is the language of quantum mechanics. A
*homomorphism* between two such algebras is a map that preserves multiplication
and addition. A ***-homomorphism** is a homomorphism that also preserves the
*operation (the algebra's "adjoint" involution).

Kadison's similarity conjecture (1969) asked a deceptively simple question:
if a map between C*-algebras is a homomorphism but *not* a *-homomorphism,
can you always "straighten it out" — by conjugating with a suitable
invertible operator — to make it one? In other words, does every bounded
unital homomorphism look like a *-homomorphism up to a change of basis?

This paper answers **yes** for the full generality of arbitrary Hilbert
spaces [S3:8–14, S2:670]. The proof goes through a quantitative commutator
estimate: the deviation of a homomorphism from being a *-homomorphism is
controlled by a constant that is *uniform* across all matrix sizes — a
result the release also formalizes in Lean.

## Graduate summary

**Main theorem** [S3:8–14, S2:670].
Every bounded complex-linear unital algebra homomorphism
$`\pi: A \to B(H)`$ from a unital complex $`C^*`$-algebra $`A`$ into the bounded
operators on an arbitrary complex Hilbert space $`H`$ is similar to a
$`^*`$-homomorphism: there exists a bounded invertible operator
$`S \in B(H)^\times`$ such that
$`S\,\pi(\cdot)\,S^{-1}`$ is a $`^*`$-homomorphism. This resolves Kadison's
similarity conjecture (1969) positively in full generality. The proof also
yields one universal hyperreflexivity constant for all unital von Neumann
algebras on arbitrary complex Hilbert spaces.

**The quantitative estimate.** The proof goes through a uniform commutator
estimate: there is a constant $`C`$ such that for every unital von Neumann
algebra $`P`$, every operator $`Y`$, and every matrix amplification of size
$`h \geq 1`$,
$`\|\mathrm{diag}(Y) X_h - X_h \mathrm{diag}(Y)\|
\leq C \cdot \|Y a - a Y\|_{\infty} \cdot \|X_h\|`$
where the commutator seminorm is taken over the unit ball of $`P`$. The key
feature is that $`C`$ is *independent* of the algebra, the Hilbert space, and
the amplification size [S6:26–34]. This uniformity is what allows the local
estimates to propagate to the global similarity result.

**The method.** The manuscript builds the proof in stages: preliminaries on
operator algebras, tensor product estimates, propagation of local bounds to
global ones, Hankel-operator estimates, the finite-factor case, and the
global theorem [S3:15–28]. The finite-factor case is the technical core: it
establishes the similarity for matrix algebras with explicit constants, and
the global case follows by an approximation and limiting argument.

## History of the conjecture

Kadison posed the similarity problem in 1969. For decades it resisted
solution in full generality: it was known for abelian algebras, for nuclear
algebras, and under various additional hypotheses, but the arbitrary case
remained open. The problem is connected to the hyperreflexivity of von
Neumann algebras and to the structure of derivations. The quantitative
commutator estimate (uniform over amplifications) is the new ingredient that
closes the gap: it gives a *single* constant that works for all algebras and
all matrix sizes, which is what the propagation argument needs to pass from
finite to infinite dimension. The proof also yields the hyperreflexivity
constant as a byproduct [S3:8–14, S4:9].

**Prior (my training data, not this repo).** Kadison's similarity conjecture
(1969) is a classical open problem in operator algebras. Partial results for
nuclear and abelian algebras, and the connection to hyperreflexivity, are
standard. The full-resolution claim with the uniform commutator estimate is
the novel contribution; I cannot verify the technical estimates independently
from training alone.

## Consequences

- **Kadison's similarity conjecture is resolved** [S3:8–14, S2:670]: every
  bounded unital homomorphism from a unital $`C^*`$-algebra to operators on an
  arbitrary Hilbert space is similar to a $`^*`$-homomorphism. This is the named
  conjecture the ledger's `resolves_named` flag records.
- **A universal hyperreflexivity constant** [S3:8–14, S4:9]: one constant
  works for all unital von Neumann algebras on arbitrary complex Hilbert
  spaces, as a byproduct of the similarity proof.
- **A uniform commutator estimate** [S6:26–34]: the deviation of a homomorphism
  from $`^*`$-form is controlled by a constant independent of the algebra, the
  Hilbert space, and the amplification size — the quantitative backbone of
  the similarity result.

## Section skeleton

One manuscript [S3:8–14], 7 sections under `build/sections/`: introduction,
preliminaries, tensors, propagation, hankel, finite-factors, global. A
`preamble.tex` and a `unicode-map.tex` support file complete the tree. A
`references.bib` bibliography. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with one scope note [S4:9] and
two comparator stubs [S5, S6], but **no** `main_results` entry and **no** OAI
tree. The scope note [S4:9] states: "The formalization proves this for
arbitrary Hilbert spaces. It also gives one universal hyperreflexivity
constant for all unital von Neumann algebras." The comparator links [S4:17–18]
name `KadisonSimilarity.lean` and `UniformCommutator.lean`.

`KadisonSimilarity.lean` (122 lines) carries 3 `sorry` occurrences — the
similarity statement is set up with the `SimilarToStar` predicate (an
invertible $`S`$ conjugating $`\pi`$ to a $`^*`$-homomorphism) but the proof is
unfinished. `UniformCommutator.lean` (40 lines) states
`theorem uniform_commutator` at [S6:26] — the existence of a constant $`C`$
uniform over all algebras, Hilbert spaces, and amplification sizes — and ends
in `sorry` at [S6:34]. No proved copy exists under `lean/OAI/`. The gap is the
formalization itself: the release set the target and described the scope, but
shipped no proof. The reading is of source text only.

## Coverage

The ledger row `fam=288` [S7] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=2`, `mainres=0`,
`scope_note=1`, `scope_chars=574`, `verification=0`, `trace=`. The T2 shape
is "scope note and comparator stubs exist, no formalization": the release
identified the target theorem, wrote a scope note, and created two challenge
stubs with `sorry` (3 in `KadisonSimilarity.lean`, 1 in
`UniformCommutator.lean`), but did not produce a `main_results` entry or an
OAI proof. The shape flags are `bound`, `resolves_named=1`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7184] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 288 at [S2:670] |
| S3 | [`preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/build/main.tex`](../../../preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/build/main.tex) | 28 | the manuscript; title [S3:3], date [S3:5], abstract [S3:8–14] |
| S4 | [`lean/docs/288.md`](../../../lean/docs/288.md) | 18 | scope note — the formalization's Scope at [S4:9] and its comparator links at [S4:17–18] |
| S5 | [`lean/ComparatorChallenges/KadisonSimilarity.lean`](../../../lean/ComparatorChallenges/KadisonSimilarity.lean) | 122 | comparator stub 1 — the similarity statement; 3 `sorry` |
| S6 | [`lean/ComparatorChallenges/UniformCommutator.lean`](../../../lean/ComparatorChallenges/UniformCommutator.lean) | 40 | comparator stub 2 — `uniform_commutator` at [S6:26] with its `sorry` at [S6:34] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=288`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
