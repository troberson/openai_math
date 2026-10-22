Notes / Summaries / Algebraic and complex geometry / [Family 050](../../index/algebraic-and-complex-geometry/050-a-counterexample-to-griffiths-positivity-conjecture.md)

# 050 — A counterexample to Griffiths' positivity conjecture

[Index page](../../index/algebraic-and-complex-geometry/050-a-counterexample-to-griffiths-positivity-conjecture.md)

## Original CONTENTS.md summary

[S1:176] carries the family entry:

> Constructs ample rank-two bundles on $\mathbb P^1\times\mathbb P^1$ with no smooth Hermitian metric of strictly Griffiths-positive curvature, disproving Griffiths' positivity conjecture already on the quadric surface.

The entry links the manuscript as "Ample rank-two bundles on the quadric surface without Griffiths-positive metrics" [S1:176].

The manuscript's title is `Ample Rank-Two Bundles on the Quadric Surface Without Griffiths-Positive Metrics` [S2:1].

The README dates it September 24, 2026 [S2:4].

## Undergraduate summary

A holomorphic vector bundle is **ample** when its tautological quotient line bundle is ample. A smooth Hermitian metric on the bundle is **strictly Griffiths-positive** when its Chern curvature is positive in every pair of nonzero tangent and fiber directions. Griffiths' conjecture asks whether ampleness always produces such a metric.

The manuscript's abstract states the answer. [S3:43–47] says: "We give counterexamples to Griffiths' conjecture in rank two on the quadric surface $\mathbb P^1\times\mathbb P^1$. We construct an explicit bundle $G$ whose coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power, but admit no smooth strictly Griffiths-positive Hermitian metric for all sufficiently large powers."

The main theorem names the family. [S5:24–31] gives it: "There is an algebraic vector bundle $G$ of rank two on $S$ such that, for every positive integer $m$, the bundle \[ E_m=f_m^*G\otimes P \] is ample. There is an integer $m_0$ such that $E_m$ admits no smooth Hermitian metric with strictly Griffiths-positive Chern curvature for every $m\ge m_0$."

The bundle is given explicitly and the ampleness has a quantitative certificate. [S5:34–39] states it: "The bundle $G$ is given explicitly in Section~ . The ampleness assertion has a quantitative certificate: Proposition~  proves that $\mathcal O_{\mathbb P(E_m)}(n)$ is very ample for every even $n$ with $n-1\geq3m$. The threshold $m_0$ is obtained by compactness and is ineffective. Thus Griffiths' conjecture fails in rank two on the quadric surface."

## Graduate summary

The ampleness notion is defined. [S5:4–7] defines it: "A holomorphic vector bundle $E$ on a projective variety is ample when the tautological quotient line bundle $\mathcal O_{\mathbb P(E)}(1)$ is ample; here $\mathbb P(E)$ parametrizes one-dimensional quotients"

The conjecture is stated. [S5:8–12] states it: "A smooth Hermitian metric is strictly Griffiths-positive if its Chern curvature is positive in every pair of nonzero tangent and fiber directions. Such a metric implies ampleness. Griffiths' conjecture asks for the converse on smooth complex projective varieties"

The algebraic theory is recorded. [S5:43–45] records it: "Hartshorne developed the algebraic theory of ample vector bundles through symmetric powers, global generation, and the tautological line bundle"

The conjecture's significance is stated. [S5:49–52] states it: "The conjecture above is the modern formulation of that question. Its significance is the proposed passage from algebraic positivity to a Hermitian curvature condition on the bundle itself, which can then enter differential-geometric vanishing arguments."

For line bundles the notions agree. [S5:54–55] records it: "For line bundles the algebraic and curvature notions agree"

On curves ampleness is characterized by quotient degrees. [S5:55–57] records it: "On complex curves, Hartshorne characterized ampleness by positivity of the degrees of all nonzero"

Nakano positivity is stronger. [S5:65–68] states it: "Several positive results recover strong curvature after modifying the bundle. Nakano positivity is a stronger curvature condition than Griffiths positivity. Berndtsson proved Nakano positivity of $E\otimes\det E$ for ample $E$ through direct-image curvature"

The symmetric-power results are recorded. [S5:69–72] records them: "Liu--Sun--Yang established Nakano and dual-Nakano positivity for determinant-twisted symmetric powers and for sufficiently large symmetric powers of ample bundles"

The twists do not supply the metric. [S5:73–75] states it: "The determinant twists and symmetric powers are part of these conclusions; they do not supply a Griffiths-positive metric on $E$ itself."

Analytic approaches are named. [S5:77–79] names them: "Analytic approaches to that remaining question include Demailly's Hermitian--Yang--Mills system and subsequent curvature functionals"

The Hermitian requirement is essential. [S5:88–90] states it: "The requirement that the metric be Hermitian is essential to the problem. Kobayashi characterized ampleness of $E$ by negatively curved strongly pseudoconvex complex Finsler structures on $E^*$"

Lempert's failure is recorded. [S5:95–98] records it: "More recently, Lempert showed that an equivariant fiberwise rule applied to a prescribed positive tautological metric can fail to produce even a semipositive Hermitian metric"

The closest prior result is recorded. [S5:104–107] records it: "In a preprint posted on September 22, 2026, Du--Xie state the existence of a rank-two ample bundle on the abelian surface $C\times C$, where $C$ is the elliptic curve $y^2=x^3-x$, without a smooth Griffiths-semipositive metric"

The relation to that result is stated. [S5:112–116] states it: "The construction here is on the rational quadric and supplies a specified power-map family, an all-$m$ ampleness certificate, and the general limiting statement of Proposition~ . Its metric conclusion is the absence of smooth _strictly_ Griffiths-positive metrics for all sufficiently large $m$."

The construction begins with two projective transformations. [S5:132–138] begins it: "Choose two projective transformations $A,B$ of $\mathbb P^1$ with order three and no common fixed point, such that $AB$ is conjugate to $z\mapsto\lambda z$ with $|\lambda|>1$. Their chosen linear lifts, and the relative lift $A^{-1}B$, have finite order. The two properties serve different purposes: finite relative orders allow line maps to agree at graph intersections, whereas the expanding product will prevent a common invariant measure."

The bundle $G$ is defined. [S5:146–147] defines it: "Define $G$ by the pairs of local sections of $L_1\oplus L_2$ that agree under this identification on $D$."

The filtrations are stated. [S5:156–160] states them: "The two quotient sequences give two filtrations of symmetric powers. The product of the two kernel line bundles is positive in both rulings. Alternating the sequences groups the negative twists into powers of this product; each remaining quotient loses at most one additional copy of the graph divisor."

The averaging is stated. [S5:173–177] states it: "Suppose that infinitely many $E_m$ have positive metrics. Their dual squared norms are plurisubharmonic. Average these norms over $f_m$, using a local $m$th root of a pulled-back _twisting frame_ to absorb the factor $P$. Each average remains a Hermitian quadratic; the twisting transition factor tends to one as $m\to\infty$."

The maximum principle is applied. [S5:189–192] applies it: "Restricting $q$ to either line subbundle makes its squared seminorm independent of the other $\mathbb P^1$ coordinate, by the maximum principle. The graph relations give a single nonzero squared seminorm on $\mathcal O_{\mathbb P^1}(-b)$, invariant under the lifts of $A$ and $B$."

The fixed-point obstruction is stated. [S5:198–199] states it: "Invariance under $AB$ forces this measure to be supported on its two fixed points. Both $A$ and $B$ preserve this nonempty support."

The dual sign is recorded. [S5:227–229] records it: "The dual has the opposite Griffiths sign. In particular its squared norm is plurisubharmonic on the total bundle; this standard criterion is recalled where it is used."

## Section skeleton

- `build/paper.tex` [S3]
- `build/sections/01-introduction.tex` [S5]
- `build/sections/02-construction.tex` [S6]
- `build/sections/03-ampleness.tex` [S7]
- `build/sections/04-limit.tex` [S8]
- `build/sections/05-obstruction.tex` [S9]
- `build/sections/06-conclusion.tex` [S10]
- `build/references.bib` [S4]

## Comparison with the formalized statement

The scope note states the formalized claim. [S11:9] says: "Griffiths' positivity conjecture predicts that every ample holomorphic vector bundle on a smooth complex projective variety admits a smooth Hermitian metric with strictly Griffiths-positive curvature. The formalized counterexample starts with a rank-two algebraic bundle $G$ on $\mathbb P^1\times\mathbb P^1$. Its coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power but admit no such metric for all sufficiently large powers."

The scope note states what is not included. [S11:11] says: "The separate very-ampleness result for all admissible even exponents is not included."

The declaration is `OAI.QuadricCounterexample.main_theorem` [S12:10]. The comparator stub carries `sorry` at `QuadricBundles.lean:175` [S13:175].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 176 |
| S2 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/README.md`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/README.md) | 17 | Manuscript title, date |
| S3 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/paper.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/paper.tex) | 62 | Abstract, lines 43–47 |
| S4 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/references.bib`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/references.bib) | 239 | Bibliography entries |
| S5 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/01-introduction.tex) | 233 | Introduction: theorem, history, proof stages |
| S6 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/02-construction.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/02-construction.tex) | 202 | Construction |
| S7 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/03-ampleness.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/03-ampleness.tex) | 166 | Ampleness |
| S8 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/04-limit.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/04-limit.tex) | 314 | Limit |
| S9 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/05-obstruction.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/05-obstruction.tex) | 308 | Obstruction |
| S10 | [`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/06-conclusion.tex`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/06-conclusion.tex) | 25 | Conclusion |
| S11 | [`lean/docs/050.md`](../../../lean/docs/050.md) | 17 | Scope |
| S12 | [`lean/OAI/Geometry/QuadricBundles/Main.lean`](../../../lean/OAI/Geometry/QuadricBundles/Main.lean) | 35 | Declaration |
| S13 | [`lean/ComparatorChallenges/QuadricBundles.lean`](../../../lean/ComparatorChallenges/QuadricBundles.lean) | 181 | Comparator stub |

## Bibliography

**26 entries** from `references.bib`:
- Griffiths, Phillip A.. *Hermitian differential geometry, {Chern} classes, and positive vector bundles*. (1969) [Griffiths1969]
- Demailly, Jean-Pierre. *Hermitian--{Yang--Mills} approach to the conjecture of {Griffiths} on the positivity of ample vector bundles*. (2021) [Demailly2021]
- Demailly, Jean-Pierre. *Complex Analytic and Differential Geometry*. (2012) [DemaillyCADG]
- Forstneri{\v c}, Franc, Kusakabe, Yuta. *{Oka} tubes in holomorphic line bundles*. (2025) [ForstnericKusakabe]
- Umemura, Hiroshi. *Some results in the theory of vector bundles*. (1973) [Umemura1973]
- Hartshorne, Robin. *Ample vector bundles*. (1966) [Hartshorne1966]
- Hartshorne, Robin. *Ample vector bundles on curves*. (1971) [Hartshorne1971]
- Umemura, Hiroshi. *Fibr\'es vectoriels positifs sur une courbe elliptique*. (1972) [Umemura1972]
- Campana, Fr\'ed\'eric, Flenner, Hubert. *A characterization of ample vector bundles on a curve*. (1990) [CampanaFlenner1990]
- Kobayashi, Shoshichi. *Negative vector bundles and complex {Finsler} structures*. (1975) [Kobayashi1975]
- … and 16 more
