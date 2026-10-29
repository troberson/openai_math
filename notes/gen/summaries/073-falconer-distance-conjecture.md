[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 073](../index/real-and-complex-analysis/073-falconer-distance-conjecture.md)

# 073 — The Falconer distance conjecture

[Index page](../index/real-and-complex-analysis/073-falconer-distance-conjecture.md)

## Original CONTENTS.md summary

The release's blurb 

> **073. The Falconer distance conjecture.** Resolves the Falconer distance conjecture in every dimension d ≥ 2: every compact set $`E\subset\mathbb R^d`$ with Hausdorff dimension greater than $`d/2`$ determines a set of Euclidean distances of positive Lebesgue measure. (Lean) [S1:1831]

The catalog entry [S9:220] states the same. The manuscript abstract 

> We resolve the Falconer distance conjecture in every dimension. For every
integer $`d\ge2`$, a compact subset of $`\mathbb R^d`$ with Hausdorff dimension
greater than $`d/2`$ determines a set of Euclidean distances of positive
Lebesgue measure. [S2:7–12]

## Undergraduate summary

Take a collection of points $`E`$ in $`\mathbb R^d`$. Its **distance set** is the set of
all the distances between pairs of points in it, $`\Delta(E)=\{|x-y|:x,y\in
E\}`$. The question is how "large" $`E`$ must be to force that set of distances
to be large. One way to measure the size of $`E`$ is its **Hausdorff
dimension**: the familiar topological dimension of a line is $`1`$, of a plane
$`2`$, but a fractal can carry a fractional value such as $`1.5`$ even when it is
topologically much thinner. The Falconer distance conjecture asked: if a
compact set $`E`$ has Hausdorff dimension strictly larger than half the ambient
dimension $`d/2`$, must its distance set have **positive Lebesgue measure** —
that is, must the distances it realizes stretch over an interval of positive
length, rather than accumulating as a thin dust?

This manuscript answers yes, in every dimension $`d\ge2`$, and — importantly —
without assuming $`E`$ is smooth, has a regular measure on it, or has any
product structure. The theorem 

> **theorem**
Let $`d\ge2`$ be an integer and let $`E\subset\mathbb R^d`$ be compact. If
$`\dim_H E>d/2`$, then
$$\mathcal L^1(\Delta(E))>0.$$ [S3:11–17]

The point of the second sentence [S3:19–22] is that the only hypothesis is the
strict dimension bound.

## Graduate summary

The headline claim is Theorem `thm:main` 

> **theorem**
Let $`d\ge2`$ be an integer and let $`E\subset\mathbb R^d`$ be compact. If
$`\dim_H E>d/2`$, then
$$\mathcal L^1(\Delta(E))>0.$$ [S3:11–17]

and it carries no regularity beyond the strict Hausdorff-dimension assumption


> Theorem imposes no regularity beyond the strict Hausdorff
dimension assumption. In particular, it does not require equality of
Hausdorff and packing dimensions, an Ahlfors regular measure, product
structure, or Fourier decay. [S3:19–22]

The proof assembles a chain of analytic estimates that closes with a
monotone-measure shell principle: if a decreasing sequence of positive
measures converges to a limit and its successive increments have summable
Fourier mass in a shell, the limit is absolutely continuous. The argument
regularizes the set, extracts angular gain, controls oscillatory integral
estimates on the sphere, recurses through a graph structure over pairs, and
assembles the final monotone-measure argument in the assembly section. The
limiting measure is nonzero and supported on $`\Delta(E)`$, which is what gives
positive Lebesgue measure.

The setting has a long history 

> The problem originates in Falconer's work , which
established the sufficient threshold $`(d+1)/2`$. His lattice-type examples
at dimension $`d/2`$ explain the strict inequality in the positive-measure
formulation. Mattila's spherical-average criterion 
made Fourier $`L^2`$ estimates a central approach to the problem. [S3:29–33]

The threshold has been pushed from Falconer's sufficient $`(d+1)/2`$ down to the
conjectured $`d/2`$ over four decades; this manuscript is the one that reaches
the full $`d/2`$ in every dimension.

## History of the conjecture

Prior (my training data, not repo text): the problem is a distance analogue
of the distinct-distances question and sits with the Falconer–Bourgain
line of Fourier-analytic attacks. The manuscript's own history section
[S3:29–33] records the milestones: Falconer's $`(d+1)/2`$, Mattila's
spherical-average criterion, Bourgain's connection to restriction theory,
Wolff's planar $`4/3`$, and Erdoğan's $`d/2+1/3`$, with the most recent
pre-manuscript bounds coming from decoupling (Du–Guth–ou et al., Du–Zhang)
and the pinned-distance work of Liu and the Du–Iosevich–Ou–Wang family.
The endpoint question — what happens at dimension exactly $`d/2`$ — is
explicitly left open by the strict inequality in the statement; the
manuscript makes no endpoint assertion.

## Consequences

**The full Falconer threshold in every dimension.** The strict $`d/2`$ bound
is now settled across all $`d\ge2`$ for compact sets with no auxiliary
structure [S3:11–17].

**A monotone-measure shell principle.** The closing argument — a scalar
shell principle for decreasing measures with summable Fourier increments —
is stated as an independently usable lemma (Lemma `asm:monotone-shell` in
the manuscript's section 10) and could apply to other problems about
absolute continuity of limiting measures.

**Pinned distances follow.** The manuscript notes the pinned analogue,
$`\mathcal L^1(\Delta_y(E))>0`$ for some $`y\in E`$, as a corollary of the same
machinery in the range the prior restriction estimates already cover.

## Section skeleton

The manuscript is a short main file [S2:7–12] (31 lines) that inputs eleven
section files under `build/sections/`, plus a `references.bib` (no inline
`thebibliography`):

- `00_introduction.tex` [S3], 245 lines — statement, no-regularity remark, history and scope, proof map.
- `01_conventions.tex`, 160 lines — notation.
- `02_regularization.tex`, 207 lines — the regularization of the set.
- `03_angular_gain.tex`, 919 lines — the angular-gain estimate.
- `04_preparation.tex`, 837 lines — preparation, including the thin-tube upgrade.
- `05_profiles_tests.tex`, 549 lines — profile tests and the critical fractal angular Fourier estimate.
- `06_oscillatory.tex`, 520 lines — oscillatory integral estimates.
- `07_graph.tex`, 392 lines — the graph estimate over pairs.
- `08_recursion.tex`, 601 lines — the recursion.
- `09_ledger.tex`, 301 lines — bookkeeping.
- `10_assembly.tex`, 613 lines — the assembly, including the monotone-measure shell principle.

No `verification/` bundle ships with this manuscript.

## Comparison with the formalized statement

The scope note [S4:9] states the all-dimensional claim for the
formalization:

> The formalization proves the Falconer distance conjecture in every dimension. For every integer $`d\ge2`$ and compact set $`E\subset\mathbb R^d`$ with Hausdorff dimension greater than $`d/2`$, the set $`\{\lVert x-y\rVert:x,y\in E\}`$ has positive Lebesgue measure. The linked statements include both this all-dimensional result and the earlier planar case. [S4:9]

The tracked declaration is narrower. The single `main_results` entry names
`OAI.PlanarFalconer.mainTarget_proved`, whose file closes by aliasing the
planar theorem 

```lean
theorem mainTarget_proved : MainTarget := manuscript_main
```
[S7:50]

and `MainTarget` is the **planar** statement 

```lean
def MainTarget : Prop :=
  ∀ E : Set Plane, IsCompact E → 1 < dimH E → 0 < volume (distanceSet E)
```
[S6:13–14]

The all-dimensions comparator [S5:11–15] is a `sorry` stub with no
`main_results` entry:

```lean
theorem falconer_distance_conjecture :
    ∀ (d : ℕ), 2 ≤ d → ∀ E : Set (EuclideanSpace ℝ (Fin d)), IsCompact E →
      (d : ℝ≥0∞) / 2 < dimH E →
        0 < volume {r : ℝ | ∃ x ∈ E, ∃ y ∈ E, dist x y = r} := by
  sorry
```
[S5:11–15]

So the machine-checked Lean body proves the planar case; the all-dimension
conclusion in the scope note rests on the scope note's prose, not on a
tracked declaration. This is a claim-level gap, not a contradiction: the
manuscript proves the full all-dimension statement, the formalization
carries a proof for the planar slice, and the all-dimension comparator is
the unproved target.

## Coverage

T3: one manuscript, one scope note, two comparator challenges, one
`main_results` entry. The ledger reads `paps 1`, `paps_form 1`,
`mainres 1`, `scope_note 1`, `chal 2`, `verification 0`, `trace` empty.
The family ships an eleven-section LaTeX manuscript [S2:7–12], a
`references.bib`, and a `README.md` "**Date:** September 23, 2026 [S8:5]". No `verification/`
bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 073 at line 1831) |
| S2 | [`preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/paper.tex`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/paper.tex) | 31 | Main file: abstract, input chain |
| S3 | [`preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/sections/00_introduction.tex`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/sections/00_introduction.tex) | 245 | Introduction: main theorem, no-regularity remark, history |
| S4 | [`lean/docs/073.md`](../../../lean/docs/073.md) | 16 | Scope note |
| S5 | [`lean/ComparatorChallenges/FalconerAllDimensions.lean`](../../../lean/ComparatorChallenges/FalconerAllDimensions.lean) | 19 | All-dimensions challenge stub |
| S6 | [`lean/ComparatorChallenges/PlanarFalconer.lean`](../../../lean/ComparatorChallenges/PlanarFalconer.lean) | 25 | Planar challenge stub (MainTarget) |
| S7 | [`lean/OAI/MeasureTheory/Falconer/Main.lean`](../../../lean/OAI/MeasureTheory/Falconer/Main.lean) | 54 | Proved version in the Lean tree |
| S8 | [`preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/README.md`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/README.md) | 18 | Release date |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 073 at line 220) |
