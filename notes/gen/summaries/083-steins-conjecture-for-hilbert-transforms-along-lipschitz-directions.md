[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 083](../index/real-and-complex-analysis/083-steins-conjecture-for-hilbert-transforms-along-lipschitz-directions.md)

# 083 — Stein's conjecture for Hilbert transforms along Lipschitz directions

[Index page](../index/real-and-complex-analysis/083-steins-conjecture-for-hilbert-transforms-along-lipschitz-directions.md)

## Original CONTENTS.md summary

The release's blurb [S1:2063] and the catalog abstract [S2:240] state the
family's claim: a uniform strong $`L^2`$ bound for the planar Hilbert
transform along any Lipschitz unit vector field, at integration lengths
bounded by an absolute multiple of the reciprocal Lipschitz constant,
uniform over inner truncations. This gives an affirmative answer to
Stein's weak-$`(2,2)`$ conjecture for the short-scale case. The
manuscript's abstract 

> We prove a uniform $`L^2`$ bound for the Hilbert transform along a
Lipschitz unit vector field in the plane, with integration restricted
to a fixed absolute multiple of the reciprocal Lipschitz seminorm.
The bound is uniform in the inner truncation and holds for fields
depending on both coordinates. This gives an affirmative answer to
Stein's weak-$`(2,2)`$ conjecture. [S3:7–14]

## Undergraduate summary

The classical Hilbert transform integrates a function against the kernel
$`1/t`$ along a line. The "directional" Hilbert transform generalizes this:
instead of integrating along a fixed direction, it integrates along a
curve determined by a *vector field* $`v(x)`$ at each point. The question is
whether the resulting operator is bounded on $`L^2`$.

Stein's conjecture (1979) asked whether directional Hilbert transforms
along Lipschitz (smooth enough) vector fields are $`L^2`$-bounded. The
difficulty is that the direction changes from point to point, so the
standard commutator estimates fail. The short-scale version \u2014
restricting the integration to a window of size proportional to the
reciprocal Lipschitz constant of the field \u2014 is the case treated
here. The full-scale question (allowing longer integration windows) is
open [S4:48–59].

The bound here is *uniform*: the same $`L^2`$ constant works for every
Lipschitz unit vector field, every inner truncation, and every Schwartz
input function. This is stronger than a pointwise estimate that
depends on the particular field.

## Graduate summary

**The theorem** [S4:17–35, `thm:main`]. There are absolute
constants $`a_*\in(0,1/2)`$ and $`C_*<\infty`$ such that every
1-Lipschitz unit vector field $`v:\mathbb R^2\to S^1`$ satisfies

> **theorem**
There are absolute constants $`a_*\in(0,1/2)`$ and $`C_*<\infty`$
such that every Lipschitz field $`v:\mathbb R^2\to S^1`$ with
$`\mathrm{Lip}(v)\le1`$ satisfies
$$\sup_{0<\epsilon<a_*}
 \left\|H_{v,a_*}^{\epsilon}f\right\|_{L^2(\mathbb R^2)}
 \le C_*\left\|f\right\|_{L^2(\mathbb R^2)}
 \qquad(f\in\mathcal S(\mathbb R^2)).$$
Its symmetric principal value therefore satisfies
$$\left\|H_{v,a_*}f\right\|_2\le C_*\norm f_2,
 \qquad
 \big|\{x:|H_{v,a_*}f(x)|>\lambda\}\big|
 \le C_*^2\lambda^{-2}\norm f_2^2
 \quad(\lambda>0).$$ [S4:17–35]

The estimate is uniform in the inner truncation $`\epsilon`$: the supremum
over $`0<\epsilon<a_*`$ is bounded by $`C_*\|f\|_2`$. The symmetric principal
value $`H_{v,a_*}f`$ therefore inherits an $`L^2`$ bound and a weak-$`(2,2)`$
estimate. The bound is also uniform in the reciprocal-Lipschitz scale
formulation, where the integration window is $`R\le 10^{-6}/\text{Lip}(v)`$.

**The proof structure.** The proof (11 sections, $`\sim`$ 7,950 lines of
LaTeX) proceeds through a time-frequency decomposition of the directional
kernel into ordinary and popular tiles, a concentration argument to
localize the interaction, a separated-count estimate to control the
overlap, a finite-phase argument to bound the oscillatory part, a
recursive hierarchy to pass from dyadic to continuous scales, and a
phase-prediction and residual argument to assemble the final bound
[S3:18–28].

**What is excluded.** The formalized result covers the short-scale form
($`R\le 10^{-6}/\text{Lip}(v)`$). The full-scale version, allowing
arbitrarily long integration windows, is not included in the formalization
[S5].

## History of the conjecture

Stein posed the directional Hilbert transform problem in 1979 [S4:48–59].
The $`L^p`$ theory for $`p\ne2`$ was developed by Lacey (2003) and others,
and the $`L^2`$ boundedness for $`C^\infty`$ vector fields was established
by Lacey and Li (2010). The Lipschitz case is the endpoint of the
smoothness range: below Lipschitz regularity, the direction changes too
rapidly for the known estimates to work.

The short-scale vs full-scale distinction is geometric: at short scales
the direction is approximately constant, so the standard Hilbert-transform
machinery applies with a uniform constant. At longer scales, the
accumulation of direction changes requires additional cancellation
structure that is not captured by the present proof.

**Prior (my training data, not this repo).** The directional Hilbert
transform and Stein's conjecture are well-studied in harmonic analysis.
I know the Lacey–Li theorem for $`C^\infty`$ fields and the partial
$`L^p`$ results for less smooth fields. A uniform $`L^2`$ bound for all
1-Lipschitz fields at the short scale is, to my knowledge, not
established in the literature I was trained on. I cannot independently
verify this 2026 manuscript's argument.

## Consequences

**Affirmative answer to Stein's weak-$`(2,2)`$ conjecture (short scale).**
For every 1-Lipschitz unit vector field $`v:\mathbb R^2\to S^1`$, the
directional Hilbert transform at the short scale is $`L^2`$-bounded with
a universal constant [S4:17–35].

**Uniform $`L^2`$ principal value.** The symmetric principal value
$`H_{v,a_*}f`$ is $`L^2`$-bounded uniformly in $`v`$, with a weak-$`(2,2)`$
estimate as a consequence [S4:27–34].

**Reciprocal-Lipschitz uniformity.** The bound extends to the
formulation where the integration window is $`R\le 10^{-6}/\text{Lip}(v)`$,
uniform over all Lipschitz constants $`K>0`$ [S5].

**Bounded extensions to all of $`L^2`$.** The Schwartz-function bound
extends to bounded operators on all of $`L^2(\mathbb R^2)`$ by density
[S5].

## Section skeleton

**Manuscript** [S3:7–14], eleven numbered sections under `build/sections/`:
introduction [S4:17–35], reductions, ordinary-tiles, popular-forest,
concentration, separated-count, finite-phase, hierarchy,
phase-prediction, residuals, assembly. Root is `build/main.tex` [S3:3],
with a title [S3:3], date [S3:5], two figures
(`build/figures/phase-scales.tex`, `build/figures/shifted-blocks.tex`),
and a 38-entry BibTeX bibliography `references.bib` [S8].

The manuscript ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5]. The formalization proves uniform $`L^2`$ bounds for
short Hilbert transforms along Lipschitz unit vector fields in the
plane, including fields depending on both coordinates, at the
reciprocal-Lipschitz truncation scale. At a fixed short scale for
1-Lipschitz fields, it also gives principal-value and weak-$`(2,2)`$
estimates and bounded extensions to all of $`L^2`$. These results
establish the stated short-scale form of Stein's question. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
zero `sorry` in the Lean source is not a comparator pass, and the
library has not been built here.

**The comparator stub** [S6] carries two target theorems, each with a
`sorry`. The short-scale uniform bound 

```lean
theorem main :
    ∃ a : ℝ, a∈Ioo 0 (1/2) ∧ ∃ C : ℝ≥0, 0<C ∧ ShortHilbertConclusion a C := by
  sorry
```
[S6:63–65]

The reciprocal-Lipschitz uniformity 

```lean
theorem uniform_truncation :
    ∃ C : ℝ, 0<C ∧ ∀ K : ℝ≥0, 0<K → ∀ epsilon R : ℝ,
      0<epsilon → epsilon≤R → R≤1/(1000000*(K:ℝ)) →
      ∀ v : Plane → Plane, LipschitzWith K v → (∀ x, ‖v x‖=1) →
      ∀ f : SchwartzMap Plane ℂ,
        eLpNorm (shortTransform v epsilon R f) 2 volume≤ENNReal.ofReal (C*‖f.toLp 2 volume‖) := by
  sorry
```
[S6:68–74]

**The OAI tree is present but unregistered.** The `formalization.yaml`
carries **no `main_results` entry** for this family: the config
`ComparatorChallenges/LipschitzHilbert.json` is not linked to any
declaration or file. This is a structural absence \u2014 the work is in
the Lean tree, unlinked from the release's checking workflow. The OAI
`LipschitzHilbert/` tree nonetheless **exists** (1910 `.lean` files over
185,580 lines with zero `sorry`) and **proves both statements**:
`theorem main` at 

```lean
theorem main :
    ∃ a : ℝ, a∈Ioo 0 (1/2) ∧ ∃ C : ℝ≥0, 0<C ∧ ShortHilbertConclusion a C :=
  main_of_laceyLi_input laceyLiInput_proved
```
[S7:17–19]

and `theorem uniform_truncation` at 

```lean
theorem uniform_truncation :
    ∃ C : ℝ, 0<C ∧ ∀ K : ℝ≥0, 0<K → ∀ epsilon R : ℝ,
      0<epsilon → epsilon≤R → R≤1/(1000000*(K:ℝ)) →
      ∀ v : Plane → Plane, LipschitzWith K v → (∀ x, ‖v x‖=1) →
      ∀ f : SchwartzMap Plane ℂ,
        eLpNorm (shortTransform v epsilon R f) 2 volume≤ENNReal.ofReal (C*‖f.toLp 2 volume‖) :=
  uniform_truncation_of_laceyLi_input laceyLiInput_proved
```
[S7:23–29]

Both close as thin applications of `main_of_laceyLi_input
laceyLiInput_proved` and `uniform_truncation_of_laceyLi_input
laceyLiInput_proved` respectively. The absence from `main_results` means
the release does not register this formalization in its checking
workflow; the ledger records `paps_form 0` and `mainres 0`.

## Coverage

T2: the family carries a scope note and one comparator challenge but no
`main_results` entry. The ledger row `fam=083` records `paps 1`,
`paps_form 0`, `tier T2`, `chal 1`, `mainres 0`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes bound|uniform`, `resolves_named 1`,
`summary 1`. The family ships one LaTeX manuscript (root `build/main.tex`,
11 `.tex` files under `build/sections/`, two figures, a 38-entry
`references.bib`), a scope note, and one comparator challenge with two
`sorry` theorems; a 1910-file OAI Lean tree with zero `sorry` exists and
proves both statements, but is not registered in `main_results`. The
family ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 083 at [S1:2063] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 083 at [S2:240] |
| S3 | [`preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/main.tex`](../../../preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/main.tex) | 31 | manuscript root; title [S3:3], date [S3:5], abstract [S3:7–14] |
| S4 | [`preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/sections/01-introduction.tex`](../../../preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/sections/01-introduction.tex) | 298 | introduction; the main theorem [S4:17–35], the Stein's-conjecture context [S4:48–59] |
| S5 | [`lean/docs/083.md`](../../../lean/docs/083.md) | 17 | the formalization scope note: the short-scale uniform L² bound and the excluded full-scale question |
| S6 | [`lean/ComparatorChallenges/LipschitzHilbert.lean`](../../../lean/ComparatorChallenges/LipschitzHilbert.lean) | 80 | comparator stub: the two target theorems, each with a `sorry` [S6:63–74] |
| S7 | [`lean/OAI/Analysis/LipschitzHilbert/Main.lean`](../../../lean/OAI/Analysis/LipschitzHilbert/Main.lean) | 35 | the OAI entry point: both statements proven [S7:17–29] |
| S8 | [`preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/references.bib`](../../../preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/build/references.bib) | 347 | 38-entry BibTeX bibliography |

## Bibliography

- Bateman, Michael, $`L^p`$ Estimates for Maximal Averages Along One-variable Vector Fields in $`\mathbb R^2`$ (2008)
- Bateman, Michael, Thiele, Christoph, $`L^p`$ estimates for the Hilbert transforms along a one-variable vector field (2013)
- Bateman, Michael, Single annulus $`L^p`$ estimates for Hilbert transforms along vector fields (2013)
- Bourgain, Jean, A remark on the maximal function associated to an analytic vector field (1989)
- Carleson, Lennart, On convergence and growth of partial sums of Fourier series (1966)
- Charalambides, Marcos, Christ, Michael, Near-extremizers of Young's inequality for discrete groups (2011)
- Coifman, Ronald R., Meyer, Yves, Commutateurs d'intégrales singuli{\`e}res et opérateurs multilinéaires (1978)
- Eisner, Tanja, Tao, Terence, Large values of the Gowers–Host–Kra seminorms (2012)
- Fournier, John J. F., Sharpness in Young's inequality for convolution (1977)
- Guo, Shaoming, Hilbert transform along measurable vector fields constant on Lipschitz curves: $`L^2`$ boundedness (2015)
- Guo, Shaoming, Hilbert transform along measurable vector fields constant on Lipschitz curves: $`L^p`$ boundedness (2017)
- Guo, Shaoming, Thiele, Christoph, Hilbert transforms along Lipschitz direction fields: A lacunary model (2017)
- Guo, Shaoming, Single annulus estimates for the variation-norm Hilbert transforms along Lipschitz vector fields (2017)
- Hajłasz, Piotr, Harmonic analysis (2012)
- John, Fritz, Nirenberg, Louis, On functions of bounded mean oscillation (1961)
- Jones, Roger L., Seeger, Andreas, Wright, James, Strong variational and jump inequalities in harmonic analysis (2008)
- Kinnunen, Juha, Harmonic analysis (2024)
- Lacey, Michael, Li, Xiaochun, On a Lipschitz Variant of the Kakeya Maximal Function (2006)
- Lacey, Michael T., Li, Xiaochun, Maximal theorems for the directional Hilbert transform on the plane (2006)
- Lacey, Michael, Li, Xiaochun, On a conjecture of E. M. Stein on the Hilbert transform on vector fields (2010)
- Lacey, Michael, Thiele, Christoph, A proof of boundedness of the Carleson operator (2000)
- Lerner, Andrei K., Nazarov, Fedor, Intuitive dyadic calculus: the basics (2019)
- Calderón, Alberto P., Commutators of singular integral operators (1965)
- Lépingle, Dominique, La variation d'ordre $`p`$ des semi-martingales (1976)
- Di Plinio, Francesco, Guo, Shaoming, Thiele, Christoph, Zorin-Kranich, Pavel, Square functions for bi-Lipschitz maps and directional operators (2018)
- Di Plinio, Francesco, Parissis, Ioannis, A sharp estimate for the Hilbert transform along finite order lacunary sets of directions (2018)
- Stein, Elias M., Problems in harmonic analysis related to curvature and oscillatory integrals (1987)
- Stein, Elias M., Street, Brian, Multi-parameter singular Radon transforms III: Real analytic surfaces (2012)
- Tao, Terence, Lecture notes 4 for 247A (2006)
- Tao, Terence, Lecture notes 6 for 247B (2007)
- Tao, Terence, Lecture notes 2 for 247A (2006)
- Tao, Terence, Lecture notes 1 for 247A (2006)
- Zorin-Kranich, Pavel, {Weighted {Lépingle inequality}} (2020)
