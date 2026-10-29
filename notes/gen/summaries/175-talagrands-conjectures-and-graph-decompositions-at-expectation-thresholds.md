[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 175](../index/combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md)

# 175 — Talagrand's conjectures and graph decompositions at expectation thresholds

[Index page](../index/combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md)

## Original CONTENTS.md summary

The release's blurb [S1:4090] and the catalog abstract [S2:431]
state a three-manuscript family. It **proves Talagrand's
expectation-threshold conjecture** (integral and fractional
thresholds differ by at most a universal factor) and **resolves
Talagrand's discrete-convexity conjecture**. An application proves
the **Ascoli–He–Park–Talagrand graph-
decomposition conjecture**: every graph's edges split into a
universally bounded number of fixed pieces, each with containment
threshold at most a universal constant times the original
graph's integral expectation threshold. Three manuscripts carry
the family. The first, *Graph Decompositions at the Integral
Expectation Threshold* [S3:31, S3:33], abstract [S3:39
–45]:

> We prove the graph-decomposition conjecture of Ascoli, He, Park,
and Talagrand. Every graph admits a partition into a universally
bounded number of fixed edge pieces, each having ordinary containment
threshold at most a universal constant times the original graph's
integral expectation threshold. The partition is chosen before
sampling the random host, and the separate embeddings of the pieces
need not agree on shared vertices. [S3:39–45]

The second, *Integral and fractional expectation thresholds are
equivalent* [S4:32, S4:34], abstract 

> We prove Talagrand's conjecture that integral and fractional expectation
thresholds are within a universal constant factor, with the same covering
budget. [S4:38–40]

The third, *Talagrand's discrete-convexity conjecture* [S5:28,
S5:30], abstract 

> We prove Talagrand's discrete-convexity conjecture.
There is a universal integer $`k`$ such that, whenever an arbitrary family has
Bernoulli product measure at least $`1-1/k`$, the sets not contained
in a union of $`k`$ members admit a cover of total cost at most $`1/2`$
at the same density. [S5:37–41]

## Undergraduate summary

An **increasing family** is a collection of subsets where adding
elements keeps you in the family. Given such a family, the
**expectation threshold** is the critical random density $`p`$ where
the family "appears" in a random $`p`$-subsample — below $`p`$ you
almost surely miss it, above $`p`$ you almost surely hit it. There
are two versions: the **integral** threshold (whole sets) and the
**fractional** threshold (allowing weighted covers). Talagrand
conjectured they differ only by a universal constant — the
fractional version is no cheaper than the integral one by more
than a fixed factor. This family proves it with the explicit
factor $`25 \cdot 512^4`$ [S4:38–40, S2:431]. The
graph-decomposition application uses this threshold to say: a
graph's edge set can be broken into a bounded number of
"pieces", each of which appears in a random subgraph no earlier
than a constant times the whole graph's threshold [S3:39
–45, S2:431].

## Graduate summary

**The expectation-threshold equivalence** [S4:38–40,
S6:10]. For every nonempty proper increasing family
$`\mathcal F`$ on a finite nonempty ground set, the fractional and
integral expectation thresholds satisfy
$`q_f(\mathcal F) \le 25 \cdot 512^4 \, q(\mathcal F)`$, where
both thresholds use cover budget $`1/2`$ and fractional covers may
assign weights to every subset including the empty set
[S6:10].

**The discrete-convexity conjecture** [S5:37–41, S6:12].
There is a universal integer $`k`$ — the formalization takes
$`k = 2^{75}`$ — such that if an arbitrary family
$`\mathcal D`$ of subsets of a finite ground set has Bernoulli-$`p`$
measure at least $`1 - 1/k`$, then the sets **not** contained in a
union of $`k`$ members of $`\mathcal D`$ form a $`p`$-small family:
they have a containment cover of total $`p`$-cost at most $`1/2`$.
This holds for every $`0 < p < 1`$, with repeated members allowed
in the union and no monotonicity assumption [S6:12].

**The graph-decomposition application** [S3:39–45,
S2:431]. Every graph admits a partition into a universally
bounded number of fixed edge pieces, each with ordinary
containment threshold at most a universal constant times the
original graph's integral expectation threshold. The partition
is chosen **before** sampling the random host, and the separate
embeddings of the pieces need not agree on shared vertices
[S3:39–45].

**The scope of the formalization.** The formalization proves the
expectation-threshold equivalence and the discrete-convexity
conjecture. The graph-decomposition application is a manuscript
theorem but is **not** in the formalization's `sources:`
listing — the scope note names only two comparators, both
for the two base results [S6:10, S6:12, S6:16–19].

## History of the conjecture

Talagrand's expectation-threshold program (1990s–2000s)
asked how the "fractional" (allowing probabilistic covers) and
"integral" (whole sets only) thresholds for monotone graph
properties compare. The conjecture that they are within a
universal constant was a standing open problem in the
Kahn--Koml\'os--Szab\'o / Frankl--R\'onyi threshold
program. The **discrete-convexity** conjecture is a companion
statement about the measure of families near saturation
($`1 - 1/k`$), asserting that the "exceptional" sets (not covered
by $`k`$ members) are uniformly small in a covering sense. The
**Ascoli–He–Park–Talagrand** graph-
decomposition conjecture applied these threshold tools to say a
graph's edges decompose into bounded pieces each with controlled
containment threshold. This family proves all three, with the
two base results formalized
[S4:38–40, S5:37–41, S3:39–45, S2:431].

**Prior (my training data, not this repo).** I know Talagrand's
threshold program and the integral-vs-fractional threshold
question, and the general shape of the discrete-convexity
statement. A proof of the threshold equivalence with the explicit
constant $`25 \cdot 512^4`$, the discrete-convexity result at
$`k = 2^{75}`$, and the Ascoli–He–Park–Talagrand
decomposition go beyond what I can verify from training alone;
the rounding/fractional-small lemmas in [S4:38–40] and the density
argument in [S5:37–41] are not something I can independently
reconstruct.

## Consequences

**The expectation-threshold conjecture is resolved.** Integral
and fractional expectation thresholds differ by at most
$`25 \cdot 512^4`$ for every nonempty proper increasing family
[S4:38–40, S6:10, S2:431].

**The discrete-convexity conjecture is resolved** at the
universal $`k = 2^{75}`$, uniformly over $`0 < p < 1`$ with
repeated members allowed and no monotonicity
[S5:37–41, S6:12, S2:431].

**The Ascoli–He–Park–Talagrand graph-
decomposition conjecture is proved.** Every graph's edges split
into a universally bounded number of pieces each with
containment threshold within a universal constant of the whole
graph's integral expectation threshold, the partition chosen
before sampling [S3:39–45, S2:431].

**The formalization covers the two base results.** The
graph-decomposition application is a manuscript theorem outside
the formalization's `sources:` listing
[S6:10, S6:12, S6:16–19].

## Section skeleton

Three manuscripts. Manuscript 1 [S3:39–45] (title [S3:31], date
[S3:33]) — `main.tex` (841 lines) under `build/`, the
graph-decomposition application. Manuscript 2 [S4:38–40] (title
[S4:32], date [S4:34]) — `main.tex` (47 lines) under
`build/source/`, the threshold equivalence. Manuscript 3 [S5:37–41]
(title [S5:28], date [S5:30]) — `main.tex` (49 lines)
under `build/source/`, the discrete-convexity conjecture. The
family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S6:10, S6:12]. The first paragraph formalizes the
expectation-threshold equivalence: $`q_f(\mathcal F) \le 25
\cdot 512^4 \, q(\mathcal F)`$ for every nonempty proper
increasing family, both thresholds at cover budget $`1/2`$ with
fractional covers weighted over all subsets including the empty
set [S6:10]. The second paragraph formalizes the
discrete-convexity result at $`k = 2^{75}`$: a family of
Bernoulli-$`p`$ measure at least $`1 - 1/k`$ has its exceptional
sets (not in a union of $`k`$ members) covered at total $`p`$-cost
at most $`1/2`$, for every $`0 < p < 1`$ [S6:12]. The scope note
names two comparators [S6:16–19]:
`TalagrandExpectationThreshold.lean` and
`TalagrandDiscreteConvexity.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 2` and `paps_form 2` (of 3). Two
`main_results` entries are registered:
`OAI.TalagrandThreshold.talagrand_expectation_threshold_equivalence`
at `OAI/Combinatorics/ExpectationThreshold/Main.lean`, and
`OAI.TalagrandDiscreteConvexity.talagrand_discrete_convexity` at
`OAI/Combinatorics/DiscreteConvexity/Main.lean`. Two manuscripts
(the threshold and discrete-convexity ones) are in the
`sources:` listing. The graph-decomposition manuscript is a
third, unformalized [S6:10, S6:12, S6:16–19].

**The comparator stubs.** The `TalagrandExpectationThreshold.lean`
comparator restates the equivalence with a bare `sorry`


```lean
theorem talagrand_expectation_threshold_equivalence [Nonempty α]
    (F : Family α) (_hF : F.Nonempty) (hproper : F ≠ Finset.univ)
    (hIncreasing : Increasing F) :
    qf F ≤ ((25 : ℝ) * (512 : ℝ) ^ 4) * q F := by
  sorry
```
[S7:52–56]

The `TalagrandDiscreteConvexity.lean` comparator restates the
discrete-convexity assertion with a bare `sorry`


```lean
theorem talagrand_discrete_convexity (N : ℕ) (_hN : 1 ≤ N)
    (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (D : Family (Fin N))
    (hD : 1 - 1 / (2 : ℝ) ^ 75 ≤ familyMeasure p D) :
    Small p (exceptional ((2 : ℕ) ^ 75) D) := by
  sorry
```
[S8:47–51]

**What the proofs do.** Both OAI trees carry **real, non-`sorry`**
proofs. The `OAI/Combinatorics/ExpectationThreshold` package (47
files, 4834 lines, zero `sorry`) proves the equivalence with the
explicit constant $`25 \cdot 512^4`$ — it rounds a
fractional-small certificate into an integral one
(`fractionalSmall_rounding`), derives an integral-small bound via
`le_q_of_small`, and clears the algebra with `div_le_iff` and
`mul_comm` 

```lean
theorem talagrand_expectation_threshold_equivalence [Nonempty α]
    (F : Family α) (_hF : F.Nonempty) (hproper : F ≠ Finset.univ)
    (hIncreasing : Increasing F) :
    qf F ≤ ((25 : ℝ) * (512 : ℝ) ^ 4) * q F := by
  have hempty : (∅ : Finset α) ∉ F := hIncreasing.empty_not_mem hproper
  have hqf0 : 0 ≤ qf F := qf_nonneg F hempty
  have hqf1 : qf F ≤ 1 := qf_le_one F hempty
  have hsmall : Small (qf F / ((25 : ℝ) * (512 : ℝ) ^ 4)) F :=
    fractionalSmall_rounding F hqf0 hqf1 (fractionalSmall_qf F hempty)
  have hscaled0 : 0 ≤ qf F / ((25 : ℝ) * (512 : ℝ) ^ 4) :=
    div_nonneg hqf0 rounding_constant_pos.le
  have hscaled1 : qf F / ((25 : ℝ) * (512 : ℝ) ^ 4) ≤ 1 :=
    (div_le_one rounding_constant_pos).mpr
      (hqf1.trans (by norm_num : (1 : ℝ) ≤ (25 : ℝ) * (512 : ℝ) ^ 4))
  have hle := le_q_of_small hscaled0 hscaled1 hsmall
  calc
    qf F ≤ q F * ((25 : ℝ) * (512 : ℝ) ^ 4) :=
      (div_le_iff₀ rounding_constant_pos).mp hle
    _ = ((25 : ℝ) * (512 : ℝ) ^ 4) * q F := mul_comm _ _
```
[S9:21–39]

The `OAI/Combinatorics/DiscreteConvexity` package (36 files,
4259 lines, zero `sorry`) proves the discrete-convexity result
at $`k = 2^{75}`$ by a single density lemma
`original_density_small`, which discharges the exceptional-set
cover bound 

```lean
theorem talagrand_discrete_convexity (N : ℕ) (_hN : 1 ≤ N)
    (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (D : Family (Fin N))
    (hD : 1 - 1 / (2 : ℝ) ^ 75 ≤ familyMeasure p D) :
    Small p (exceptional ((2 : ℕ) ^ 75) D) :=
  original_density_small p hp0 hp1 D hD
```
[S10:61–65]

The graph-decomposition application is stated and proved in
manuscript 1 [S3:39–45] but has no comparator and no
`main_results` entry — it is outside the formalization.
The release records `scope: "Partial progress."` and
`review: status: unchecked`; the two comparators' `sorry` bodies
are the targets the release set, and the two proved theorems in
the OAI tree are the registered results.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 175 at [S1:4090] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{175} at [S2:431] |
| S3 | [`preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/build/main.tex`](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/build/main.tex) | 841 | manuscript 1 (the graph-decomposition application, not formalized): title [S3:31], date [S3:33], abstract [S3:39–45] |
| S4 | [`preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/build/source/main.tex`](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/build/source/main.tex) | 47 | manuscript 2 (the expectation-threshold equivalence, formalized): title [S4:32], date [S4:34], abstract [S4:38–40] |
| S5 | [`preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/build/source/main.tex`](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/build/source/main.tex) | 49 | manuscript 3 (the discrete-convexity conjecture, formalized): title [S5:28], date [S5:30], abstract [S5:37–41] |
| S6 | [`lean/docs/175.md`](../../../lean/docs/175.md) | 19 | the formalization scope note: the threshold paragraph [S6:10], the discrete-convexity paragraph [S6:12], and the comparator table [S6:16–19] |
| S7 | [`lean/ComparatorChallenges/TalagrandExpectationThreshold.lean`](../../../lean/ComparatorChallenges/TalagrandExpectationThreshold.lean) | 60 | registered comparator 1: the `talagrand_expectation_threshold_equivalence` theorem [S7:52–55] and the `sorry` [S7:56] |
| S8 | [`lean/ComparatorChallenges/TalagrandDiscreteConvexity.lean`](../../../lean/ComparatorChallenges/TalagrandDiscreteConvexity.lean) | 57 | registered comparator 2: the `talagrand_discrete_convexity` theorem [S8:47–50] and the `sorry` [S8:51] |
| S9 | [`lean/OAI/Combinatorics/ExpectationThreshold/Main.lean`](../../../lean/OAI/Combinatorics/ExpectationThreshold/Main.lean) | 43 | OAI tree 1 (47 files, 4834 lines, 0 sorry): the real `talagrand_expectation_threshold_equivalence` proof [S9:21–39] with the constant 25 * 512^4 |
| S10 | [`lean/OAI/Combinatorics/DiscreteConvexity/Main.lean`](../../../lean/OAI/Combinatorics/DiscreteConvexity/Main.lean) | 69 | OAI tree 2 (36 files, 4259 lines, 0 sorry): the real `talagrand_discrete_convexity` proof [S10:61–65] with k = 2^75 |
