[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 218](../index/probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md)

# 218 — Conformal universality for weakly interacting and disordered Ising models

[Index page](../index/probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md)

## Original CONTENTS.md summary

The release's blurb [S1:5109] and the catalog abstract [S2:521]
state the family's claim: six results in the universality
theory of the weakly perturbed square-lattice Ising
model. Weak finite-range square-symmetric even
multispin perturbations preserve critical bulk spin and
energy limits. Weak square-symmetric contour
interactions yield chordal $`\mathrm{SLE}_3`$ interface
limits. iid bond disorder of any fixed bounded
nondegenerate mean-zero law preserves the same
$`\mathrm{SLE}_3`$ limit. The family ships six
manuscripts [S1:5109]:

- *Quenched $`\mathrm{SLE}_3`$ limits for general weak
  random-bond Ising models* [S3:42, S3:44]
- *Quenched $`\mathrm{SLE}_3`$ universality for the
  weak random-bond Ising model* [S4:37, S4:39]
- *Logarithmic relative fluctuations in the weakly
  disordered planar Ising model* [S5:38, S5:40]
- *Conformal universality of bulk Ising correlations
  under weak interactions* [S6:43, S6:45]
- *$`\mathrm{SLE}_3`$ universality for weak
  finite-range Ising interactions* [S7:51, S7:54]
- *Buffered comparison and stopping-band resolution
  in critical Ising* [S8:3, S8:5]

The quenched random-bond abstract 

> For the planar Ising model with bonds $`J_e=1+\varepsilon\xi_e`$, where the
$`\xi_e`$ have any fixed bounded, nondegenerate, mean-zero iid law, we prove
quenched chordal $`\mathrm{SLE}_3`$ convergence for sufficiently small
$`\varepsilon>0`$. The temperature is the spontaneous-magnetization threshold.
Convergence holds in probability over environments for the full oriented
curve law in deterministic Jordan-domain approximations. [S3:47–54]

The buffered-comparison abstract 

> We prove pointwise comparison and finite stopping-band approximation
theorems for the critical nearest-neighbor Ising model on the square
lattice. Arbitrary common pinned spins are allowed in the comparison:
the likelihood ratio is controlled by a zero-field FK connection
probability on the graph with those vertices deleted. For an interface
exploration across a band of fixed positive width, finitely many regular
signed barriers approximate every good conditional target law in total
variation, uniformly over bounded observables and sufficiently fine
meshes. [S8:8–18]

## Undergraduate summary

The **Ising model** is a mathematical model of
magnetism: each site of a grid carries a spin
(+1 or -1), and neighboring spins prefer to align.
At a critical temperature, the model exhibits
**universality**: the large-scale behavior is the
same across a whole family of models, not just the
nearest-neighbor one. The **SLE$`_3`$** (Schramm-
Loewner evolution) is a random fractal curve that
describes the interface between magnetized phases
at criticality. The family proves **universality
under disorder and perturbation**: even when the
bonds are weakened by random disorder, or the
interaction is perturbed by weak finite-range
terms, the critical behavior is unchanged — spin
correlations converge to the same conformal limits
and interfaces converge to the same SLE$`_3`$ curve
[S3:47–54, S6:48–56, S7:57–65,
S2:521].

## Graduate summary

**Quenched random-bond SLE$`_3`$** [S3:47–54,
S2:521]. For the planar Ising model with bonds
$`J_e = 1 + arepsilon \xi_e`$ where the $`\xi_e`$
have any fixed bounded, nondegenerate, mean-zero iid
law, quenched chordal $`\mathrm{SLE}_3`$ convergence
holds for sufficiently small $`arepsilon > 0`$,
in probability over environments.

**Two-valued random-bond SLE$`_3`$** [S4:42–48,
S2:521]. The same result for independent symmetric
two-valued ferromagnetic bonds.

**Logarithmic relative fluctuations**
[S5:43–51, S2:521]. The relative second
moment of the quenched critical spin correlation
grows as $`(\log r)^{1/4+o(1)}`$ for bonds
$`1 \pm arepsilon`$.

**Conformal universality of bulk correlations**
[S6:48–56, S2:521]. Mixed bulk spin and
energy correlations are conformally universal under
sufficiently small square-symmetric finite-range
even multispin perturbations.

**SLE$`_3`$ universality for contour interactions**
[S7:57–65, S2:521]. Every sufficiently small
square-symmetric finite-range perturbation of the
contour energy has a domain-independent inverse
temperature at which the spin interface converges
to chordal $`\mathrm{SLE}_3`$.

**Buffered comparison** [S8:8–18, S2:521].
Pointwise comparison and finite stopping-band
approximation theorems for the critical
nearest-neighbor Ising model, with arbitrary
common pinned spins.

**The scope of the formalization.** The scope note
covers the buffered comparison [S9:9]: the
pointwise likelihood-ratio comparison with
arbitrary common pinned spins, and the finite
stopping-band approximation. The full SLE$`_3`$
convergence and conformal universality results are
**outside** the formalized scope [S9:11]. The
scope note names one comparator [S9:17]:
`BufferedIsing.lean`.

## History of the conjecture

**The Ising universality class** is one of the
central results in statistical mechanics: at
criticality, the large-scale behavior of the
two-dimensional Ising model is described by
conformal field theory with central charge
$`c = 1/2`$ and interface curves given by
$`\mathrm{SLE}_3`$ (Schramm 2001, Smirnov 2001).
**Universality under perturbation** asks: does the
critical behavior survive weak modifications of
the interaction? The answer is yes for a broad
class of perturbations: finite-range even
multispin terms [S6:48–56], contour
energy perturbations [S7:57–65], and
random bond disorder [S3:47–54,
S4:42–48]. The **buffered comparison**
[S8:8–18] provides the technical tool: a
pointwise likelihood-ratio bound that controls
how pinned spins affect interface probabilities,
enabling the comparison between perturbed and
unperturbed models [S3:47–54,
S4:42–48, S6:48–56,
S7:57–65, S8:8–18, S2:521].

**Prior (my training data, not this repo).** I
know the Ising universality class, the
$`\mathrm{SLE}_3`$ interface theorem (Smirnov 2001),
and the conformal field theory with $`c = 1/2`$.
The **six universality results** — under general
random bond disorder, two-valued disorder,
multispin perturbations, contour perturbations,
and the buffered comparison tool — are results I
cannot independently verify from training alone.

## Consequences

**The SLE$`_3`$ interface limit is universal
under random bond disorder**: for any fixed
bounded nondegenerate mean-zero iid law,
quenched chordal $`\mathrm{SLE}_3`$ convergence
holds for sufficiently weak disorder
[S3:47–54, S4:42–48, S2:521].

**The SLE$`_3`$ interface limit is universal under
weak finite-range contour perturbations**
[S7:57–65, S2:521].

**Bulk spin and energy correlations are
conformally universal under weak multispin
perturbations** [S6:48–56, S2:521].

**The logarithmic fluctuation exponent is
$`1/4`$** for the quenched critical spin
correlation under weak random-bond disorder
[S5:43–51, S2:521].

## Section skeleton

Six manuscripts: [S3:47–54] (title [S3:42], date
[S3:44]), [S4] (title [S4:37], date [S4:39]),
[S5] (title [S5:38], date [S5:40]), [S6] (title
[S6:43], date [S6:45]), [S7] (title [S7:51],
date [S7:54]), [S8:8–18] (title [S8:3], date [S8:5])
— all with `main.tex` under `build/` and
sections under `build/sections/`. The family
ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S9:9]. The scope note covers
the pointwise likelihood-ratio comparison under
arbitrary common pinned spins, and the finite
stopping-band approximation: for fixed positive
band width, sufficiently fine meshes, and good
conditional target laws, finitely many regular
signed barriers control every bounded
observable and every comparison ratio in total
variation [S9:9]. The full SLE$`_3`$ convergence
and conformal universality results are outside
the formalized scope [S9:11]. The scope note
names one comparator [S9:17]:
`BufferedIsing.lean`.

**The registration gap.** The family is at tier
T2: the ledger row records `mainres 0` and
`paps_form 0`. No manuscript is in the yaml
`sources:` listing, and there is no
`main_results` entry in `formalization.yaml`.

**No OAI tree.** There is no `OAI/` package for
this family: `find lean/OAI -path
"*BufferedIsing*"` returns 0 files. The
comparator stub stands alone.

**The comparator stub.** The
`BufferedIsing.lean` comparator states
`theorem finite_graph_comparison` [S10:98] with
a bare `sorry` body [S10:109]:

```lean
theorem finite_graph_comparison {n m : ℕ} (G : FiniteGraph n m)
    (h : Fin n → ℝ) (I J F : Finset (Fin n))
    (hIJ : Disjoint I J) (hIF : Disjoint I F) (hJF : Disjoint J F)
    (i j : KeptVertex F) (hi : i.val ∈ I) (hj : j.val ∈ J)
    (a τ : Spins n) (mix mix' : Spins n → ℝ)
    (hmix : ∀ b, 0 ≤ mix b) (hmix' : ∀ b, 0 ≤ mix' b)
    (hmixsum : ∑ b, mix b = 1) (hmix'sum : ∑ b, mix' b = 1) :
    Real.exp (-4 * Real.artanh (qZero G I J F i j)) ≤
        mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ∧
      mixtureProb G h I J F a τ mix / mixtureProb G h I J F a τ mix' ≤
        Real.exp (4 * Real.artanh (qZero G I J F i j)) := by
  sorry
```
[S10:98–109]

The release records `scope: "Partial progress."`
and `review: status: unchecked`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 218 at [S1:5109] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{218} at [S2:521] |
| S3 | [`preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/build/main.tex`](../../../preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/build/main.tex) | 64 | manuscript 1 of 6; title [S3:42], date [S3:44], abstract [S3:47–54] |
| S4 | [`preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/build/main.tex`](../../../preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/build/main.tex) | 60 | manuscript 2 of 6; title [S4:37], date [S4:39], abstract [S4:42–48] |
| S5 | [`preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/build/main.tex`](../../../preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/build/main.tex) | 66 | manuscript 3 of 6; title [S5:38], date [S5:40], abstract [S5:43–51] |
| S6 | [`preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/main.tex`](../../../preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/build/main.tex) | 68 | manuscript 4 of 6; title [S6:43], date [S6:45], abstract [S6:48–56] |
| S7 | [`preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/build/main.tex`](../../../preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/build/main.tex) | 84 | manuscript 5 of 6; title [S7:51], date [S7:54], abstract [S7:57–65] |
| S8 | [`preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/build/main.tex`](../../../preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/build/main.tex) | 30 | manuscript 6 of 6; title [S8:3], date [S8:5], abstract [S8:8–18] |
| S9 | [`lean/docs/218.md`](../../../lean/docs/218.md) | 15 | scope note: scope paragraph [S9:9] and comparator table [S9:15] |
| S10 | [`lean/ComparatorChallenges/BufferedIsing.lean`](../../../lean/ComparatorChallenges/BufferedIsing.lean) | 113 | comparator: theorem finite_graph_comparison [S10:98], sorry [S10:109] |
