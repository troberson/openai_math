[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 214](../index/probability-and-statistical-mechanics/214-benjamini-schramm-nonuniqueness-conjecture.md)

# 214 — The Benjamini–Schramm nonuniqueness conjecture

[Index page](../index/probability-and-statistical-mechanics/214-benjamini-schramm-nonuniqueness-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4943] and the catalog abstract [S2:513]
state the family's claim: the bond-percolation nonuniqueness
conjecture of Benjamini and Schramm is resolved. Every infinite
connected locally finite nonamenable quasi-transitive graph has
$p_c < p_u$: there is a nonempty range of probabilities with
infinitely many infinite clusters. A stronger operator bound
also establishes the critical triangle condition, giving
$p_c < p_{2\to 2} \le p_u$. The family ships one
manuscript [S1:4943]:

- *Nonuniqueness of percolation on nonamenable
  quasi-transitive graphs* [S3:127, S3:130]

The abstract 

> We prove the bond-percolation nonuniqueness conjecture of Benjamini and
Schramm: every infinite connected, locally finite, nonamenable quasi-transitive
graph has a nonempty interval of parameters for which Bernoulli bond
percolation almost surely has infinitely many infinite clusters. We also prove
Hutchcroft's stronger operator-threshold conjecture, establishing
$p_c<p_{2\to2}\le p_u$. [S3:135–140]

## Undergraduate summary

**Percolation** on a graph asks: if each edge is independently
"open" with probability $p$, what happens to the clusters of
connected open edges? On a "regular" infinite graph like
$\mathbb{Z}^d$ there is a sharp threshold: below a critical
probability $p_c$ all clusters are finite, above it one giant
infinite cluster appears. The **nonuniqueness conjecture**
(Benjamini and Schramm, 1996) asks about "irregular" graphs
that grow exponentially (nonamenable): can there be a range of
$p$ values where **more than one** infinite cluster appears
simultaneously? The answer is **yes** — on every such
graph, there is a range $(p_c, p_u)$ of probabilities with
infinitely many infinite clusters [S3:135–140,
S2:513].

## Graduate summary

**The main theorem** [S3:135–140, S2:513]. Every
infinite connected, locally finite, nonamenable
quasi-transitive graph has a nonempty interval of parameters
for which Bernoulli bond percolation almost surely has
infinitely many infinite clusters. The stronger
operator-threshold conjecture of Hutchcroft is also
established: $p_c < p_{2\to 2} \le p_u$. For Cayley
graphs, the result holds for every finite symmetric
generating set of a nonamenable finitely generated group.

**The scope of the formalization.** The scope note covers
the full result [S4:9]: the nonuniqueness phase conjecture
with $p_c < p_{2\to 2} \le p_u$ and a common nonempty
coupled interval. For Cayley graphs, the result holds for
every finite symmetric generating set. The critical
estimates include a finite triangle diagram, susceptibility
of order $(p_c - p)^{-1}$, percolation probability of order
$p - p_c$, cluster-volume tail of order $n^{-1/2}$, and
intrinsic and extrinsic radius tails of order $n^{-1}$
[S4:11]. Connection probabilities decay exponentially below
$p_{2\to 2}$ [S4:11]. The scope note names two
comparators [S4:17–18]: `BenjaminiSchramm.lean` and
`CayleyPercolation.lean`.

## History of the conjecture

**The nonuniqueness conjecture** was posed by Benjamini and
Schramm (1996) in their foundational paper on percolation on
graphs. They conjectured that on every nonamenable
transitive graph, the percolation process is not unique:
there exist probabilities with more than one infinite
cluster. The conjecture was known for specific graphs (tree
products, certain Cayley graphs) but the general
quasi-transitive case was open. The proof establishes the
**critical triangle condition** at $p_c$ for bond
percolation on every nonamenable quasi-transitive graph,
which implies $p_c < p_{2\to 2} \le p_u$ and hence
nonuniqueness. The Hutchcroft operator-threshold
conjecture is the stronger form: the $2 \to 2$ Sobolev
improvement constant is the right threshold
[S3:135–140, S2:513].

**Prior (my training data, not this repo).** I know the
Benjamini–Schramm conjecture as a named open problem,
the tree-product and some Cayley-graph positive cases, and
the critical triangle condition framework. The **general
quasi-transitive resolution** and the **Hutchcroft
operator-threshold proof** are results I cannot
independently verify from training alone.

## Consequences

**The Benjamini–Schramm nonuniqueness conjecture is
resolved** for bond percolation on every infinite connected
locally finite nonamenable quasi-transitive graph:
$p_c < p_u$ with infinitely many infinite clusters in
between [S3:135–140, S2:513].

**The Hutchcroft operator-threshold conjecture is
resolved**: $p_c < p_{2\to 2} \le p_u$ [S3:135–140,
S2:513].

**The critical triangle condition holds** at $p_c$ for bond
percolation on every nonamenable quasi-transitive graph
[S3:135–140, S2:513, S4:11].

## Section skeleton

One manuscript: [S3:135–140] (title [S3:127], date [S3:130])
— `main.tex` under `build/` with sections under
`build/sections/`. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The scope note covers the
nonuniqueness phase conjecture for Bernoulli bond
percolation on infinite connected locally finite
nonamenable quasi-transitive graphs. It establishes
$p_c < p_{2\to 2} \le p_u$ and a common nonempty coupled
interval with infinitely many infinite clusters almost
surely [S4:9]. For Cayley graphs, the result holds for
every finite symmetric generating set of a nonamenable
finitely generated group [S4:9]. The critical estimates
include a finite triangle diagram, susceptibility,
percolation probability, cluster-volume and radius tails,
and exponential decay below $p_{2\to 2}$ [S4:11]. The
scope note names two comparators [S4:17–18]:
`BenjaminiSchramm.lean` and `CayleyPercolation.lean`.

**The registration gap.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 1`. The
manuscript **is** in the yaml `sources:` listing, and the
scope note exists, but there is **no `main_results` entry**:
the result is not registered in `formalization.yaml`.

**What the OAI tree carries.** One OAI package carries a
real non-`sorry` proof:

- `OAI/Probability/BenjaminiSchramm` (**292 files over
  30,706 lines, zero `sorry`**).

The gap is registration: the proof exists in the OAI tree
but is not linked to a `main_results` entry in
`formalization.yaml`.

**The comparator stubs.** The `BenjaminiSchramm.lean`
comparator states `theorem full_main` [S5:217] with a bare
`sorry` body [S5:220]:

```lean
theorem full_main {V : Type u} {E : Type v} [Infinite V]
    (G : BondGraph V E) (hc : Connected G) (hl : LocallyFinite G)
    (hq : QuasiTransitive G) (hh : 0 < hV G) : MainConclusion G := by
  sorry
```
[S5:217–220]

The `CayleyPercolation.lean` comparator states
`theorem arbitrary_cayley` [S6:68] with a bare `sorry`
body [S6:80]:

```lean
theorem arbitrary_cayley {Λ : Type u} [Group Λ] [Group.FG Λ]
    (hna : ¬ AmenableGroup Λ) (S : Finset Λ)
    (hsym : ∀ s ∈ S, s⁻¹ ∈ S) (hgen : Subgroup.closure (S : Set Λ) = ⊤)
    (h1 : 1 ∉ S) :
    OperatorBounded (cayleyGraph S) (pc (cayleyGraph S)) ∧
    pc (cayleyGraph S) < ptwo (cayleyGraph S) ∧
    ptwo (cayleyGraph S) ≤ pu (cayleyGraph S) ∧
    (∃ p₁ p₂ : unitInterval, pc (cayleyGraph S) < p₁ ∧ p₁ < p₂ ∧ p₂ < 1 ∧
      ∀ᵐ labels ∂(labelLaw : Measure (CayleyEdge S → unitInterval)),
        ∀ p ∈ Set.Icc p₁ p₂, (infiniteClusters (cayleyGraph S) (openEdges labels p)).Infinite) ∧
    (∀ p : unitInterval, pc (cayleyGraph S) < p → p < pu (cayleyGraph S) →
      ∀ᵐ ω ∂law p, (infiniteClusters (cayleyGraph S) ω).Infinite) := by
  sorry
```
[S6:68–80]

The release records `scope: "Partial progress."` and
`review: status: unchecked`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 214 at [S1:4943] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{214} at [S2:513] |
| S3 | [`preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/main.tex`](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/main.tex) | 164 | the manuscript; title [S3:127], date [S3:130], abstract [S3:135–140] |
| S4 | [`lean/docs/214.md`](../../../lean/docs/214.md) | 18 | the formalization scope note: the scope paragraph [S4:9], the critical estimates [S4:11], and the comparator table [S4:17–18] |
| S5 | [`lean/ComparatorChallenges/BenjaminiSchramm.lean`](../../../lean/ComparatorChallenges/BenjaminiSchramm.lean) | 240 | comparator 1 of 2: the `theorem full_main` [S5:217] and the `sorry` [S5:220] |
| S6 | [`lean/ComparatorChallenges/CayleyPercolation.lean`](../../../lean/ComparatorChallenges/CayleyPercolation.lean) | 84 | comparator 2 of 2: the `theorem arbitrary_cayley` [S6:68] and the `sorry` [S6:80] |
