[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 213](../index/probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md)

# 213 — No infinite critical clusters on quasi-transitive graphs

[Index page](../index/probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md)

## Original CONTENTS.md summary

The release's blurb [S1:4918] and the catalog abstract [S2:511]
state the family's claim: the Benjamini–Schramm
criticality conjecture is resolved for bond percolation on
every infinite connected locally finite quasi-transitive graph
with $p_c < 1$: at the critical probability, there is almost
surely no infinite cluster. The family also establishes this
conclusion for both nearest-neighbor bond and site percolation
on $\mathbb{Z}^3$. The family ships two
manuscripts [S1:4918]:

- *Critical bond and site percolation on the cubic
  lattice* [S3:30, S3:32]
- *No percolation at criticality on quasi-transitive
  graphs* [S4:37, S4:39]

The cubic-lattice abstract 

> We prove that nearest-neighbor Bernoulli bond and site percolation on
$\mathbb Z^3$ have no infinite cluster at their respective critical parameters.
The proof combines a finite connection inequality for independent hyperedges
with a finite-scale extension estimate and an adaptive exploration. [S3:36–39]

The quasi-transitive abstract 

> We prove that critical Bernoulli bond percolation has no infinite
cluster on any infinite connected locally finite quasi-transitive graph
with critical probability less than one. This resolves the bond form of
the criticality conjecture of Benjamini and Schramm. [S4:43–46]

## Undergraduate summary

**Percolation** is a model of random growth on a network.
Imagine a grid of sites (or edges), where each one is
"open" with probability $p$ and "closed" with probability
$1-p$, independently. The **critical probability** $p_c$
is the threshold: below it, every connected cluster of
open sites is finite; above it, an infinite cluster
appears. The **criticality conjecture** (Benjamini and
Schramm, 1996) asks: exactly at $p_c$, does an infinite
cluster exist? For lattices like $\mathbb{Z}^2$ the
answer is known to be no (by planar duality), but for
$\mathbb{Z}^3$ and general graphs it was open. The two
manuscripts say **no** — at $p_c$ there is almost
surely no infinite cluster, on $\mathbb{Z}^3$ and on
every quasi-transitive graph [S3:36–39,
S4:43–46, S2:511].

## Graduate summary

**The cubic-lattice result** [S3:36–39, S2:511].
Nearest-neighbor Bernoulli bond and site percolation on
$\mathbb{Z}^3$ have no infinite cluster at their
respective critical parameters. The proof combines a
finite connection inequality for independent hyperedges
with a finite-scale extension estimate and an adaptive
exploration.

**The quasi-transitive result** [S4:43–46,
S2:511]. Critical Bernoulli bond percolation has no
infinite cluster on any infinite connected locally finite
quasi-transitive graph with critical probability less
than one. This resolves the bond form of the
Benjamini–Schramm criticality conjecture.

**The scope of the formalization.** The scope note
covers both results [S5:10, S5:12]: the Z3 bond and site
percolation absence, and the quasi-transitive bond
percolation absence. The graph model permits bond
multiplicities [S5:12]. The scope note names two
comparators [S5:18–19]: `CriticalZ3.lean` and
`CriticalPercolation.lean`.

## History of the conjecture

**The criticality conjecture** was posed by Benjamini and
Schramm (1996) in their study of percolation on
transitive graphs. In the planar case ($\mathbb{Z}^2$),
the absence of an infinite cluster at criticality follows
from the duality between the open and closed clusters.
In three dimensions and on non-planar graphs, no such
duality exists, and the problem required new ideas. The
**cubic-lattice proof** uses a finite connection
inequality (a bound on the probability that two distant
points are connected) combined with an extension
estimate that controls how clusters grow. The
**quasi-transitive proof** builds on the cubic-lattice
result and uses a two-cluster DFS-entropy argument,
interpolation, superpolynomial growth estimates, and a
gluing construction to extend the result from
$\mathbb{Z}^3$ to all quasi-transitive graphs
[S3:36–39, S4:43–46, S2:511].

**Prior (my training data, not this repo).** I know the
criticality conjecture as a named open problem in
percolation, the planar duality argument for
$\mathbb{Z}^2$, and the general framework of
quasi-transitive graphs. The **$\mathbb{Z}^3$ result**
and the **quasi-transitive extension** are results I
cannot independently verify from training alone.

## Consequences

**The Benjamini–Schramm criticality conjecture is
resolved for bond percolation** on every infinite
connected locally finite quasi-transitive graph with
$p_c < 1$: at criticality, there is almost surely no
infinite cluster [S4:43–46, S2:511].

**The $\mathbb{Z}^3$ case is resolved for both bond and
site percolation**: no infinite cluster at the
respective critical parameters [S3:36–39,
S2:511].

## Section skeleton

Two manuscripts: [S3:36–39] (title [S3:30], date [S3:32])
— `critical-percolation-z3.tex` under `build/`
with sections (`introduction`, `comparison`,
`preliminaries`, `extension`, `geometry`,
`exploration`) alongside the root file; [S4:43–46] (title
[S4:37], date [S4:39]) — `main.tex` under
`build/` with nine sections under `build/sections/`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:10, S5:12]. The scope note covers
both results: the Z3 bond and site percolation absence
of an infinite cluster at criticality [S5:10], and the
quasi-transitive bond percolation absence [S5:12].
The graph model permits bond multiplicities [S5:12].
The scope note names two comparators [S5:18–19]:
`CriticalZ3.lean` and `CriticalPercolation.lean`.

**The registration.** The family is at tier T3: the
ledger row records `mainres 1` and `paps_form 1`.
`formalization.yaml` registers one `main_results`
entry: `OAI.CriticalZ3.critical_no_infinite` at
`OAI/Probability/CriticalZ3/Main.lean`. The one
registered manuscript (M1, cubic lattice) is in the
`sources:` listing. The other manuscript (M2,
quasi-transitive graphs) is **not** in the yaml
`sources:` listing.

**The comparator stubs.** The `CriticalZ3.lean`
comparator states `theorem critical_no_infinite` [S6:56]
with a bare `sorry` body [S6:59]:

```lean
theorem critical_no_infinite :
    (∀ᵐ ω ∂bondLaw bondCritical, ∀ x : Vertex, (bondCluster ω x).Finite) ∧
    (∀ᵐ ω ∂siteLaw siteCritical, ∀ x : Vertex, (siteCluster ω x).Finite) := by
  sorry
```
[S6:56–59]

The `CriticalPercolation.lean` comparator states
`theorem no_percolation_at_criticality` [S7:52] with a
bare `sorry` body [S7:58]:

```lean
theorem no_percolation_at_criticality [Infinite V]
    (hconnected : G.fullGraph.Connected)
    (hlocal : G.LocallyFinite)
    (hquasi : G.QuasiTransitive)
    (hpc : G.criticalProbability < 1) :
    G.law G.criticalProbability G.percolates = 0 := by
  sorry
```
[S7:52–58]

**What the OAI tree carries.** One OAI package carries
a real non-`sorry` proof:

- `OAI/Probability/CriticalZ3` (**34 files over 10,358
  lines, zero `sorry`**): the `critical_no_infinite`
  theorem [S8:1].

The release records `scope: "Partial progress."` and
`review: status: unchecked`. The comparator `sorry`
stubs are answered by a real proof in the OAI tree.
The quasi-transitive manuscript (M2) is entirely
unregistered.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 213 at [S1:4918] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{213} at [S2:511] |
| S3 | [`preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/build/critical-percolation-z3.tex`](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/build/critical-percolation-z3.tex) | 50 | manuscript 1 of 2 (cubic lattice); title [S3:30], date [S3:32], abstract [S3:36–39] |
| S4 | [`preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/main.tex`](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/main.tex) | 61 | manuscript 2 of 2 (quasi-transitive graphs); title [S4:37], date [S4:39], abstract [S4:43–46] |
| S5 | [`lean/docs/213.md`](../../../lean/docs/213.md) | 19 | the formalization scope note: the Z3 scope [S5:10], the quasi-transitive scope [S5:12], and the comparator table [S5:18–19] |
| S6 | [`lean/ComparatorChallenges/CriticalZ3.lean`](../../../lean/ComparatorChallenges/CriticalZ3.lean) | 63 | comparator 1 of 2: the `theorem critical_no_infinite` [S6:56] and the `sorry` [S6:59] |
| S7 | [`lean/ComparatorChallenges/CriticalPercolation.lean`](../../../lean/ComparatorChallenges/CriticalPercolation.lean) | 63 | comparator 2 of 2: the `theorem no_percolation_at_criticality` [S7:52] and the `sorry` [S7:58] |
| S8 | [`lean/OAI/Probability/CriticalZ3/Main.lean`](../../../lean/OAI/Probability/CriticalZ3/Main.lean) | 114 | the registered declaration in the OAI tree (34 files, 10,358 lines, 0 sorry): the `critical_no_infinite` theorem |
