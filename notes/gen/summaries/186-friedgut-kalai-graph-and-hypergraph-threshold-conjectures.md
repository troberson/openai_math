[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 186](../index/combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md)

# 186 — The Friedgut–Kalai graph and hypergraph threshold conjectures

[Index page](../index/combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md)

## Original CONTENTS.md summary

The release's blurb [S1:4311] and the catalog abstract [S2:453]
state the family's claim: the Friedgut–Kalai
threshold-width conjectures for graphs and fixed-uniformity
hypergraphs. For fixed $`0 < \varepsilon < 1/2`$, every
nontrivial increasing relabeling-invariant property crosses
from probability $`\varepsilon`$ to $`1 - \varepsilon`$ within
width $`O((\log n)^{-2})`$ for graphs and
$`O_r((\log n)^{-r/(r-1)})`$ for $`r`$-uniform hypergraphs,
$`r \geq 3`$. The hypergraph influence bound also applies to
nonmonotone properties. The family ships two manuscripts
[S1:4311]:

- *A uniform influence bound for hypergraph properties*
  [S3:20, S3:22]
- *A Sharp Threshold Bound for Monotone Graph Properties*
  [S4:25, S4:27]

The graph-threshold abstract 

> We prove the Friedgut–Kalai sharp-threshold conjecture. For every integer $`n\ge2`$, every nontrivial increasing family of graphs on $`n`$ vertices invariant under all vertex permutations, and every $`0<\varepsilon<1/2`$, the edge probabilities at which its probability equals $`\varepsilon`$ and $`1-\varepsilon`$ differ by at most $`C\log(1/(2\varepsilon))/(\log n)^2`$, for a universal constant $`C`$. [S4:31]

## Undergraduate summary

Pick a random graph: give each possible edge a coin flip with
probability $`p`$, and accept the edge when the coin lands
heads. A **graph property** (being connected, having a large
independent set, being planar) either holds of the resulting
graph or it does not. As you slide $`p`$ from 0 to 1, the
property's probability jumps from near 0 to near 1. A
**sharp threshold** says that jump is **narrow** — the
property goes from, say, 1-in-1000 likely to 999-in-1000
likely within a tiny window of $`p`$-values. The Friedgut–
Kalai conjecture says that window has width on the order of
$`1/(\log n)^2`$ for graphs, and for $`r`$-uniform hypergraphs
the analogous bound carries the exponent
$`r/(r-1)`$ [S4:31, S3:26–34, S2:453]. The
"influence" behind the threshold is how much one edge's coin
flip changes the property's probability — and the
hypergraph result bounds that influence without assuming the
property is monotone [S3:26–34].

## Graduate summary

**The graph sharp-threshold bound** [S4:31, S5:9]. For every
$`n \geq 2`$, every nontrivial increasing family of graphs on
$`n`$ vertices invariant under all vertex permutations, and
every $`0 < \varepsilon < 1/2`$, the edge probabilities at
which its probability equals $`\varepsilon`$ and
$`1 - \varepsilon`$ differ by at most
$`C \log(1/(2\varepsilon)) / (\log n)^2`$, for a universal
constant $`C`$ [S4:31]. The scope note records the explicit
constant $`2^{19}`$ in place of the universal $`C`$, with the
bound uniform over the property, $`n`$, and
$`\varepsilon`$ [S5:9].

**The hypergraph influence bound** [S3:26–34, S2:453].
For every fixed integer $`r \geq 3`$, every relabeling-
invariant Boolean property $`f`$ of simple $`r`$-uniform
hypergraphs on $`n`$ vertices satisfies
$`\mathrm{Var}_p(f) \leq C_r I_p(f) / (\log n)^{r/(r-1)}`$,
where $`C_r`$ depends only on $`r`$ and the bound holds
**uniformly for all** $`0 < p < 1`$ without a monotonicity
assumption [S3:26–34]. For increasing properties it
gives the corresponding threshold-width bound with exponent
$`r/(r-1)`$, resolving the hypergraph threshold-width
conjecture of Friedgut and Kalai [S3:26–34].

**The scope of the formalization.** The scope note states the
formalization proves the **graph** sharp-threshold width
bound — the $`2^{19} \log(1/(2\varepsilon)) /
(\log n)^2`$ bound, uniform over the property, $`n`$, and
$`\varepsilon`$ [S5:9]. The scope note names one comparator
[S5:15]: `SharpThreshold.lean`.

## History of the conjecture

The Friedgut–Kalai sharp-threshold conjecture is a
central open problem in the theory of **random structures and
influence**. The classical **Kahn–Kalai** and
**Friedgut** threshold results give **qualitative** sharp
thresholds (the crossing width tends to 0 as $`n \to
\infty`$), but the **quantitative** question — how
wide is the crossing window — was open. The Friedgut–
Kalai conjecture asserts a specific polylogarithmic width,
and the $`(\log n)^{-2}`$ exponent for graphs is the
"right" one from the perspective of influence calculus: it
matches the bound obtainable from a variance–influence
inequality. The hypergraph generalization to
$`r`$-uniform hypergraphs with the $`r/(r-1)`$ exponent is the
analogue of the graph case at higher uniformity, and the
removal of the monotonicity assumption in the influence bound
is a strengthening. This manuscript pair closes both: the
graph bound with an explicit constant (formalized) and the
hypergraph bound with the uniform, nonmonotone influence
inequality
[S4:31, S3:26–34, S2:453].

**Prior (my training data, not this repo).** I know
Friedgut's sharp-threshold theorem and the Kahn–Kalai
influence machinery as classical results in the theory of
random structures, and that the quantitative threshold-width
question was open. A **specific proof of the
$`(\log n)^{-2}`$ bound via variance–influence
inequalities**, and the **uniform, nonmonotone** hypergraph
influence bound at the $`r/(r-1)`$ exponent, go beyond what I
can place from training alone; the `sharp_threshold_width_of_
variance_bound` and `variance_influence_bound` lemmas in
[S7:28–30] are not something I can independently verify from
memory.

## Consequences

**The Friedgut–Kalai graph sharp-threshold
conjecture is resolved.** Every nontrivial increasing
relabeling-invariant graph property has crossing width
$`O(\log(1/\varepsilon) / (\log n)^2)`$
[S4:31, S5:9, S2:453].

**The Friedgut–Kalai hypergraph threshold-width
conjecture is resolved.** $`r`$-uniform hypergraph properties
have crossing width
$`O_r((\log n)^{-r/(r-1)})`$ [S3:26–34, S2:453].

**The hypergraph influence bound is nonmonotone.** The
variance–influence inequality holds without a
monotonicity assumption [S3:26–34].

## Section skeleton

Two manuscripts: [S3] (title [S3:20], date [S3:22]) —
`main.tex` (42 lines) under `build/`; [S4:31] (title [S4:25],
date [S4:27]) — `main.tex` (39 lines) under `build/`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalization proves the
Friedgut–Kalai sharp-threshold width bound for the
**graph** case: for every $`n \geq 2`$, every nontrivial
increasing vertex-relabeling-invariant graph property, and
every $`0 < \varepsilon < 1/2`$, the edge-probability interval
between probabilities $`\varepsilon`$ and
$`1 - \varepsilon`$ has width at most
$`2^{19} \log(1/(2\varepsilon)) / (\log n)^2`$, uniform over
the property, $`n`$, and $`\varepsilon`$ [S5:9]. The scope note
names one comparator [S5:15]: `SharpThreshold.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscripts are **not** in its `sources:`
listing. The comparator `SharpThreshold.lean` restates the
target `theorem sharp_threshold_width` — the
$`2^{19}`$-prefixed width bound for nontrivial increasing
vertex-invariant graph properties — with a bare
`sorry` body 

```lean
theorem sharp_threshold_width :
    ∀ (n : ℕ) (f : GraphConfig n → Bool) (ε : ℝ),
      2 ≤ n → VertexInvariant f → IncreasingGraphProperty f →
      NontrivialGraphProperty f → 0 < ε → ε < (1 / 2 : ℝ) →
      graphQuantile (1 - ε) f - graphQuantile ε f ≤
        ((2 : ℝ) ^ 19 / (Real.log (n : ℝ)) ^ 2) * Real.log (1 / (2 * ε)) := by
  sorry
```
[S6:51–57]

**What the OAI tree does carry.** The
`OAI/Combinatorics/SharpThreshold` package (**78 files over
7,699 lines, zero `sorry`**) carries a **real, non-`sorry`**
proof of the comparator's target. The `Main.lean`
`theorem sharp_threshold_width` [S7:28–30] is a
one-line body: it discharges the width bound by
`sharp_threshold_width_of_variance_bound` applied to the
`variance_influence_bound` lemma 

```lean
theorem sharp_threshold_width :
    ∀ (n : ℕ) (f : GraphConfig n → Bool) (ε : ℝ), 2 ≤ n → VertexInvariant f → IncreasingGraphProperty f → NontrivialGraphProperty f → 0 < ε → ε < (1 / 2 : ℝ) → graphQuantile (1 - ε) f - graphQuantile ε f ≤ ((2 : ℝ) ^ 19 / (Real.log (n : ℝ)) ^ 2) * Real.log (1 / (2 * ε)) := by
  exact sharp_threshold_width_of_variance_bound variance_influence_bound
```
[S7:28–30]

The proof closes with
`exact sharp_threshold_width_of_variance_bound
variance_influence_bound` — the width bound reduces to
the variance–influence inequality, no `sorry`
[S7:28–30].

**The unregistered hypergraph result.** The hypergraph
influence manuscript [S3] proves the uniform, nonmonotone
variance–influence bound at the $`r/(r-1)`$ exponent
[S3:26–34], but it is **outside the scope note**
entirely — the scope note names only the graph
manuscript and the `SharpThreshold.lean` comparator
[S5:9, S5:15]. The hypergraph result has no comparator and
no registration. The release records `scope: "Partial
progress."` and `review: status: unchecked`; the
comparator's `sorry` is the target the release set for the
graph case, and the proved `sharp_threshold_width` in the
OAI tree is the result the tree carries without a ledger
entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 186 at [S1:4311] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{186} at [S2:453] |
| S3 | [`preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/build/main.tex`](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/build/main.tex) | 42 | manuscript 1 of 2: the uniform influence bound for hypergraph properties (outside the scope note); title [S3:20], date [S3:22], abstract [S3:26–34] |
| S4 | [`preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/build/main.tex`](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/build/main.tex) | 39 | manuscript 2 of 2: the sharp threshold bound for monotone graph properties (in the scope note); title [S4:25], date [S4:27], abstract [S4:31] |
| S5 | [`lean/docs/186.md`](../../../lean/docs/186.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:15] |
| S6 | [`lean/ComparatorChallenges/SharpThreshold.lean`](../../../lean/ComparatorChallenges/SharpThreshold.lean) | 63 | the comparator: the `sharp_threshold_width` theorem [S6:51–56] and the `sorry` [S6:57] |
| S7 | [`lean/OAI/Combinatorics/SharpThreshold/Main.lean`](../../../lean/OAI/Combinatorics/SharpThreshold/Main.lean) | 36 | the OAI tree (78 files, 7699 lines, 0 sorry): the real `sharp_threshold_width` proof [S7:28–30] via `sharp_threshold_width_of_variance_bound` and `variance_influence_bound` |
