[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 145](../index/dynamical-systems-and-ergodic-theory/145-rokhlins-multiple-mixing-problem.md)

# 145 — Rokhlin's multiple-mixing problem

[Index page](../index/dynamical-systems-and-ergodic-theory/145-rokhlins-multiple-mixing-problem.md)

## Original CONTENTS.md summary

The release's blurb [S1:3493] and the catalog abstract [S2:371] state
the family's claim: every invertible mixing probability-preserving
transformation is mixing of all finite orders, resolving Rokhlin's
multiple-mixing problem for a single transformation — correlations
among any finite collection of measurable sets converge to the product
of their measures whenever all pairwise time separations diverge. The
manuscript's abstract 

> Every invertible mixing probability-preserving transformation is mixing of every finite order. Thus Rokhlin's multiple-mixing problem for a single transformation has an affirmative answer. [S3:14]

## Undergraduate summary

A measure-preserving map $T$ of a probability space *mixes* when two
measurable sets $A,B$ forget their correlation under iteration:
$\mu(T^{-n}A\cap B)\to\mu(A)\mu(B)$ as $n\to\infty$. *Mixing of
order $k$* generalizes this to $k$ sets at once: the joint
intersection $T^{-n_1}A_1\cap\cdots\cap T^{-n_k}A_k$ decouples into
the product of the individual measures as the times separate. Rokhlin
asked in the 1960s whether ordinary (second-order) mixing of a single
transformation already forces mixing of every finite order. This
manuscript answers that question affirmatively, for one transformation
[S3:14, S4:9].

## Graduate summary

**The multiple-mixing theorem** [S3:14, S4:9]. Let $T$ be an
invertible mixing probability-preserving transformation. Then $T$ is
mixing of every finite order: for each $k\ge3$ and every $k$
measurable sets $A_1,\ldots,A_k$, the measure of their translated
intersection $T^{-\vec n}(A_1\cap\cdots\cap A_k)$ in the
appropriate sense tends to
$\prod_{i=1}^k\mu(A_i)$ as all successive time gaps
$|n_{i+1}-n_i|$ tend to infinity [S4:9].

**The statement shape.** The comparator states it as an implication
from the hypotheses
$\mu$ a probability measure, $T$ a measure-preserving measure-space
isomorphism, and $T$ mixing, to the conclusion
$\mathrm{MixingOfOrder}\ \mu\ T\ k$ for every $k\ge3$
[S5:30–32]. The result is for a single $T$; it does not assert that
mixing is generic among all transformations, only that one mixing map
is mixing of all orders.

## History of the conjecture

Rokhlin posed the multiple-mixing question in the 1960s, asking
whether the standard (second-order) mixing property of a single
invertible measure-preserving transformation implies mixing of every
finite order. The question is delicate because higher-order mixing is
genuinely stronger in general — there exist mixing
transformations that are not mixing of some order — so the
affirmative answer for *one* transformation required a nontrivial
argument that the second-order condition, on its own, cascades to all
orders [S3:14, S4:9].

**Prior (my training data, not this repo).** I know the mixing
hierarchy (ergodic, weak mixing, mixing, mixing of order $k$, $K$-
and $C$-mixing) and that Rokhlin raised the question of whether
mixing implies mixing of all orders for a single map. The
affirmative resolution — that *every* invertible mixing map is
mixing of all finite orders — is, to my knowledge, not
established in the literature I was trained on; I recall the question
being treated as subtle and the higher-order implications as
delicate. I cannot independently verify this manuscript's argument.

## Consequences

**Rokhlin's multiple-mixing problem (one map, affirmative).** Every
invertible mixing probability-preserving transformation is mixing of
every finite order [S3:14, S4:9].

**Higher-order correlations decouple.** For any $k\ge3$ measurable
sets, the joint translated intersection tends to the product of the
measures as all pairwise time separations diverge
[S2:371, S4:9].

**Second order cascades.** The single mixing hypothesis implies
mixing at every finite order, not merely second order
[S5:30–32].

## Section skeleton

One manuscript [S3:14] (title [S3:3], date [S3:5]) — `main.tex`
under `build/` plus section files; 2,933 lines total; a
`thebibliography` block in `preamble.tex`. No manuscript ships a
`verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result proves the multiple-
mixing implication: for each $k\ge3$ and every $k$ measurable sets,
the measure of their translated intersection tends to the product of
their measures as all successive time gaps tend to infinity, for one
invertible mixing probability-preserving transformation [S4:9]. The
scope note names one comparator [S4:13–15].

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming a comparator theorem for this family, and
the manuscript is not in its `sources:` listing. The scope note and
one comparator stub exist, but the release has not registered a
single declaration as a family result. The `Rokhlin.lean` comparator
states the all-orders conclusion as a `sorry`-terminated theorem


```lean
theorem mixing_all_finite_orders (μ : Measure Ω) [IsProbabilityMeasure μ]
    (T : Ω ≃ᵐ Ω) (h_pres : MeasurePreserving T μ μ) (h_mix : IsMixing μ T) :
    ∀ k : ℕ, 3 ≤ k → MixingOfOrder μ T k := by
  sorry
```
[S5:30–33]

**What the OAI tree does carry.** Under the tree's
`OAI/Dynamics/` directory there is a `MultipleMixing` package (13
files over 27,889 lines, zero `sorry`) matching the comparator. A
`main_results` registration would link the scope note's comparator to
a declaration in this package, but none is registered. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
zero `sorry` in the Lean source is not a comparator pass, and the
library has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=145` records `paps 1`, `paps_form 0`,
`tier T2`, `chal 1`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes resolution`, `resolves_named 1`, `summary 1`.
The family ships one 2,933-line LaTeX manuscript, a scope note naming
one comparator, and one `sorry`-terminated comparator stub. The OAI
tree carries one unregistered formalization package
(`OAI/Dynamics/MultipleMixing`, 13 files over 27,889 lines, zero
`sorry`) matching the comparator, but no `main_results` entry links
it and the manuscript is not in `formalization.yaml`'s `sources:`.
The family ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 145 at [S1:3493] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{145} at [S2:371] |
| S3 | [`preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/build/main.tex`](../../../preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/build/main.tex) | 27 | the single manuscript root; title [S3:3], date [S3:5], abstract [S3:14] |
| S4 | [`lean/docs/145.md`](../../../lean/docs/145.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/Rokhlin.lean`](../../../lean/ComparatorChallenges/Rokhlin.lean) | 37 | comparator stub: the `mixing_all_finite_orders` theorem [S5:30–32] and the `sorry` [S5:33] |
| S6 | [`preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/build/preamble.tex`](../../../preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/build/preamble.tex) | 42 | the manuscript's `thebibliography` block |
