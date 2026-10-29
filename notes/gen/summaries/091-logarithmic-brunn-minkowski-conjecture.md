[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 091](../index/convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md)

# 091 — The logarithmic Brunn–Minkowski conjecture

[Index page](../index/convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:2263] and the catalog abstract [S2:258] state
the family's claim: the logarithmic Brunn–Minkowski inequality for
origin-symmetric convex bodies in every dimension, the scalar-dilation
$`B`$-conjecture for even log-concave Radon measures, and the symmetric
$`L_p`$ Brunn–Minkowski inequality for $`0<p<1`$. The manuscript's
abstract 

> We prove the logarithmic Brunn–Minkowski conjecture for arbitrary
origin-symmetric convex bodies in every dimension. The theorem also gives
the symmetric $`L_p`$ Brunn–Minkowski inequality for every $`0<p<1`$.
Combined with Saroglou's transfer theorem and a support-subspace reduction,
it yields the logarithmic inequality for every even log-concave Radon
measure and the scalar-dilation $`(B)`$-conjecture. [S3:36–43]

## Undergraduate summary

The classical Brunn–Minkowski inequality says that the volume of a
Minkowski average $`(1-\lambda)K+\lambda L`$ of two convex bodies is at
least the volume of the linear interpolation of the individual volumes.
The logarithmic version replaces the Minkowski sum with a *geometric*
average of the support functions: instead of averaging the bodies
themselves, one averages the distances from the origin to their
boundaries, then takes the intersection of the resulting half-spaces
[S4:4–19]. This is a strictly stronger statement in the
origin-symmetric setting, and it is what the conjecture asked for.

The proof reduces the volume inequality to a variance bound for sums of
even powers of linear forms, carried out in moment coordinates
[S4:122–168]. The key analytic input is a tensor calculation whose
remainder is a sum of explicit squares, closing the argument by two
Cauchy–Schwarz inequalities [S4:122–168].

## Graduate summary

**The main theorem** [S4:21–29, `thm:main`]. For
$`n\ge1`$, origin-symmetric convex bodies $`K,L\subset\mathbb R^n`$, and
$`0\le\lambda\le1`$,

> **Theorem 1.1**
Let $`n\ge1`$ and let $`K,L\subset\mathbb R^n`$ be convex bodies satisfying
$`K=-K`$ and $`L=-L`$. For every $`0\le\lambda\le1`$,
$$\left|\mathcal W[h_K^{1-\lambda}h_L^\lambda]\right|
 \ge |K|^{1-\lambda}|L|^\lambda.$$ [S4:21–29]

The interpolation takes the geometric mean of the support bounds before
intersecting the half-spaces; the Wulff-body intersection is essential
throughout the argument [S4:31–42].

**The $`L_p`$ corollary** [S4:55–65, `cor:lp`]. For $`0<p<1`$, the
logarithmic endpoint implies the full symmetric volume inequality in the
intermediate range, by the monotone implication of
B\H{o}r\H{o}czky–Lutwak–Yang–Zhang:

> **Theorem 1.2**
Let $`n\ge1`$, let $`K,L\subset\mathbb R^n`$ be full-dimensional origin-symmetric
convex bodies, and let $`0<p<1`$. For every $`0\le\lambda\le1`$,
$$\left|\mathcal W\!\left[
  \bigl((1-\lambda)h_K^p+\lambda h_L^p\bigr)^{1/p}
 \right]\right|^{p/n}
 \ge (1-\lambda)|K|^{p/n}+\lambda|L|^{p/n}.$$ [S4:55–65]

**The measure-theoretic transfer.** Saroglou's transfer theorem
[saroglou2016] gives the same Wulff inequality for every even log-concave
density $`e^{-V}\,dx`$ in the same dimension, and taking two scalar
dilates of one body yields the $`B`$-conjecture: $`t\mapsto\mu(e^tK)`$ is
log-concave on $`\mathbb R`$ [S4:71–82].

## History of the conjecture

The theorem resolves the origin-symmetric logarithmic
Brunn–Minkowski conjecture of B\H{o}r\H{o}czky, Lutwak, Yang
and Zhang (Problem 1.1 of their 2012 monograph) [S4:85–87].
Stancu announced the all-dimensional logarithmic Minkowski inequality
in 2018, concluding the equivalent Brunn–Minkowski form but
deferring the flow asymptotics [S4:88–91]. The $`L_p`$
Brunn–Minkowski theory was initiated by Firey's $`p`$-means and
developed by Lutwak through mixed volumes; the $`p\downarrow0`$
endpoint is the logarithmic inequality [S4:92–97].

Prior results covered special classes: the planar case (B\H{o}r\H{o}czky–Lutwak–Yang–Zhang), bodies
unconditional with respect to a fixed basis (Saroglou), and bodies
invariant under $`n`$ common reflections (B\H{o}r\H{o}czky–Kalantzopoulos).
Spectral and PDE approaches gave local or $`p`$-close-to-$`1`$ results
(Colesanti–Livshyts–Marsiglietti, Kolesnikov–Milman,
Chen–Huang–Li–Liu, Putterman, Van Handel, Milman,
Iffland, Lu, Xi) [S4:98–120].

**Prior (my training data, not this repo).** I know the
Brunn–Minkowski inequality, the $`L_p`$ Brunn–Minkowski theory,
the B\H{o}r\H{o}czky–Lutwak–Yang–Zhang conjecture,
the Stancu announcement, and the local/spectral results. An
all-dimensional origin-symmetric logarithmic Brunn–Minkowski
inequality, with the full $`L_p`$ and measure-theoretic consequences, is,
to my knowledge, not established in the literature I was trained on. I
cannot independently verify this 2026 manuscript's argument.

## Consequences

**Logarithmic Brunn–Minkowski resolved.** For every dimension
$`n\ge1`$ and origin-symmetric convex bodies $`K,L`$, the logarithmic Wulff
combination has volume at least $`|K|^{1-\lambda}|L|^\lambda`$
for all $`0\le\lambda\le1`$ [S4:21–29].

**Symmetric $`L_p`$ Brunn–Minkowski.** The full symmetric volume
inequality holds for every $`0<p<1`$, by the B\H{o}r\H{o}czky–Lutwak–Yang–Zhang
monotone implication [S4:55–65].

**Even log-concave measures.** By Saroglou's transfer, the logarithmic
inequality holds for every even log-concave Radon measure, and the
scalar-dilation $`B`$-conjecture follows [S4:71–82].

## Section skeleton

**Manuscript** [S3:36–43], ten `.tex` files under `build/` (flat, no
`sections/` subdirectory): introduction [S4], reduction, moment,
identities, density, tensor, variance, measure; one figure
(`figure-slabs.tex`); a 34-entry `references.bib` [S8]. Root is
`build/main.tex` [S3:31], with a title [S3:31], date [S3:33].

The manuscript ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalization proves the origin-symmetric
logarithmic Brunn–Minkowski inequality for every dimension
$`n\ge1`$, with no boundary-smoothness or coordinatewise-unconditionality
assumption 

> The logarithmic Brunn–Minkowski conjecture asserts that logarithmic interpolation of origin-symmetric convex bodies preserves the geometric-mean lower bound for volume. The formalized result proves, for every dimension $`n\ge1`$, such bodies $`K,L\subset\mathbb R^n`$, and $`0\le t\le1`$, that their logarithmic Wulff combination has volume at least $`|K|^{1-t}|L|^t`$. It assumes neither boundary smoothness nor coordinatewise unconditionality. [S5:9]

The scope note links the manuscript [S5:5] and names one comparator
[S5:13–15]. The release records `scope: "Partial progress."` and
`review: status: unchecked`; zero `sorry` in the Lean source is not a
comparator pass, and the library has not been built here.

**The comparator stub** [S6:30–35] carries the target with a
`sorry`:

```lean
theorem main (n : ℕ) (hn : 1 ≤ n) (K L : Set (Space n))
    (hK : IsConvexBody K) (hL : IsConvexBody L)
    (hsK : OriginSymmetric K) (hsL : OriginSymmetric L)
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    (volume K) ^ (1 - t) * (volume L) ^ t ≤ volume (logCombination K L t) := by
  sorry
```
[S6:30–35]

**The proved entry point the release registers.** The `main_results`
entry names `OAI.LogBrunnMinkowski.main` in
`OAI/Geometry/LogVolume/BrunnMinkowski.lean`, proved at line 24481


```lean
theorem main (n : ℕ) (hn : 1 ≤ n) (K L : Set (Space n))
    (hK : IsConvexBody K) (hL : IsConvexBody L)
    (hsK : OriginSymmetric K) (hsL : OriginSymmetric L)
    (t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    (volume K) ^ (1 - t) * (volume L) ^ t ≤ volume (logCombination K L t) := by
  exact main_of_softVariance softVariance n hn K L hK hL hsK hsL t ht0 ht1
```
[S7:24481–24486]

The proof closes as a single application of `main_of_softVariance`,
which is the theorem the 24,480 preceding lines of the file establish.
The `main_results` entry links the config
`ComparatorChallenges/LogBrunnMinkowski.json` to the declaration
`OAI.LogBrunnMinkowski.main` in `OAI/Geometry/LogVolume/
BrunnMinkowski.lean`.

## Coverage

T3: the family is formalized. The ledger row `fam=091` records `paps 1`,
`paps_form 1`, `tier T3`, `chal 1`, `mainres 1`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes bound`, `resolves_named 1`,
`summary 1`. The family ships one LaTeX manuscript (root `build/main.tex`,
nine section `.tex` files, one figure, a 34-entry `references.bib`), a
scope note, and one comparator challenge with one `sorry` theorem; the
`main_results` entry registers `OAI.LogBrunnMinkowski.main`, proven in
a 24,490-line OAI `Geometry/LogVolume/BrunnMinkowski.lean` file with
zero `sorry`. The family ships no verification bundle and no reasoning
trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 091 at [S1:2263] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{091} at [S2:258] |
| S3 | [`preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/main.tex`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/main.tex) | 57 | manuscript root; title [S3:31], date [S3:33], abstract [S3:36–43] |
| S4 | [`preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/introduction.tex`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/introduction.tex) | 226 | introduction; the Wulff-body setup [S4:4–19], the main theorem [S4:21–29], the $L_p$ corollary [S4:55–65], the measure-theoretic transfer [S4:71–82], the BLYZ resolution [S4:85–87], the prior-work survey [S4:88–120], the proof strategy [S4:122–168] |
| S5 | [`lean/docs/091.md`](../../../lean/docs/091.md) | 15 | the formalization scope note: the origin-symmetric Wulff inequality at [S5:9] and the comparator table at [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/LogBrunnMinkowski.lean`](../../../lean/ComparatorChallenges/LogBrunnMinkowski.lean) | 41 | comparator stub: the `main` theorem [S6:30–34] and the `sorry` [S6:35] |
| S7 | [`lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean`](../../../lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean) | 24490 | the OAI proven `main` [S7:24481–24486] |
| S8 | [`preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/references.bib`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/references.bib) | 369 | 34-entry BibTeX bibliography |

## Bibliography

- Bakry, Dominique, Émery, Michel, Diffusions hypercontractives (1985)
- Berman, Robert J., Berndtsson, Bo, Real {Monge–Amp\`ere} equations and Kähler–Ricci solitons on toric log Fano varieties (2013)
- Borell, Christer, Convex measures on locally convex spaces (1974)
- Brascamp, Herm Jan, Lieb, Elliott H., On extensions of the Brunn–Minkowski and {Prékopa–Leindler} theorems, including inequalities for log concave functions, and with an application to the diffusion equation (1976)
- Chen, Shibing, Huang, Yong, Li, Qi-Rui, Liu, Jiakun, The $`L_p`$-Brunn–Minkowski inequality for $`p<1`$ (2020)
- Colesanti, Andrea, Livshyts, Galyna V., Marsiglietti, Arnaud, On the stability of Brunn–Minkowski type inequalities (2017)
- Cordero-Erausquin, Dario, Klartag, Bo'az, Moment measures (2015)
- Cordero-Erausquin, Dario, Santaló's inequality on $`\mathbb C^n`$ by complex interpolation (2002)
- Cordero-Erausquin, D., Fradelizi, M., Maurey, B., The $`(B)`$-conjecture for the Gaussian measure of dilates of symmetric convex sets and related problems (2004)
- Böröczky, Károly J., Lutwak, Erwin, Yang, Deane, Zhang, Gaoyong, The log-Brunn–Minkowski inequality (2012)
- Böröczky, Károly J., Lutwak, Erwin, Yang, Deane, Zhang, Gaoyong, The logarithmic Minkowski problem (2013)
- Böröczky, Károly J., Kalantzopoulos, Pavlos, Log-Brunn–Minkowski inequality under symmetry (2022)
- Dyatlov, Semyon, Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs (2026)
- Fathi, Max, Stein kernels and moment maps (2019)
- Firey, William J., $`p`$-Means of Convex Bodies (1962)
- van Handel, Ramon, The local logarithmic Brunn–Minkowski inequality for zonoids (2023)
- Iffland, Luca, The local logarithmic Brunn–Minkowski inequality for bodies of revolution (2026)
- Klartag, Bo'az, Logarithmically-concave moment measures I (2013)
- Kolesnikov, Alexander, Livshyts, Galyna, Rotem, Liran, On $`p`$-Brunn–Minkowski and Brascamp–Lieb inequalities (2026)
- Kolesnikov, Alexander V., Milman, Emanuel, Local $`L^p`$-Brunn–Minkowski inequalities for $`p<1`$ (2022)
- Kolesnikov, Alexander V., Hessian metrics, $`CD(K,N)`$-spaces, and optimal transportation of log-concave measures (2014)
- Lu, XiaoRui, Logarithmic Brunn–Minkowski Inequality under $`n-2`$ Reflection Symmetries (2026)
- Lutwak, Erwin, The Brunn–Minkowski–Firey theory. I. Mixed volumes and the Minkowski problem (1993)
- Milman, Emanuel, Centro-affine differential geometry and the log-Minkowski problem (2025)
- Fernández-Real, Xavier, Ros-Oton, Xavier, Regularity Theory for Elliptic PDE (2023)
- Putterman, Eli, Equivalence of the local and global versions of the $`L^p`$-Brunn–Minkowski inequality (2021)
- Rotem, Liran, A letter: The log-Brunn–Minkowski inequality for complex bodies (2014)
- Bollobás, Béla, Leader, Imre, Products of unconditional bodies (1995)
- Saroglou, Christos, Remarks on the conjectured log-Brunn–Minkowski inequality (2015)
- Saroglou, Christos, More on logarithmic sums of convex bodies (2016)
- Stancu, Alina, A PDE approach to geometric inequalities (2018)
- Uhrin, B., Curvilinear extensions of the Brunn–Minkowski–Lusternik inequality (1994)
- Wang, Yu, On the $`C^{2,\alpha}`$-regularity of the complex {Monge–Amp\`ere} equation (2012)
- Xi, Dongmeng, A very short unified proof of Dar's conjecture and Log-Brunn–Minkowski in the plane (2026)
