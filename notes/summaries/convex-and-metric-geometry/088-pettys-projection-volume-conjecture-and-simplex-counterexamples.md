[Notes](../../README.md) / [Summaries](../README.md) / [Convex and metric geometry](../../index/disciplines/convex-and-metric-geometry.md) / [Family 088](../../index/convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md)

# 088 — Petty's projection-volume conjecture and simplex counterexamples

[Index page](../../index/convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md)

## Original CONTENTS.md summary

[S1:252] carries the family entry:

> Proves Petty's projection-volume conjecture in the remaining dimensions $n\ge4$: ellipsoids uniquely minimize projection-body volume at fixed body volume. Also establishes the full Lutwak–Petty projection inequalities. In contrast, products of simplices exceed Brannen's proposed simplex maximum for normalized projection-body volume by an exponential factor in every sufficiently large dimension.

The entry links the two manuscripts as "Petty’s projection-volume conjecture"
and "Product counterexample to simplex maximum" [S1:252].

The first manuscript's title is "Petty’s projection-volume conjecture in dimensions at least four" [S2:1], dated [S2:5].

The second manuscript's title is "A product counterexample to the simplex maximum for projection-body volume" [S12:1], dated [S12:5].

## Undergraduate summary

The **projection body** $\Pi K$ of a convex body $K$ records the areas of its
shadows. [S4:4–6] defines it: "For a convex body $K\subset\R^n$, its
projection body $\Pi K$ is the origin-symmetric convex body whose support
function is" — the display gives the support function as the volume of the
shadow in each direction.

Petty's conjecture asks which body has the smallest projection-body volume at
a fixed volume. [S4:26–27] states it: "Petty's projection-volume conjecture
asserts, for $n\ge3$, that $R_n$ is minimized precisely by ellipsoids
\cite{Petty1971}." The functional $R_n$ is the projection-body volume divided
by the body's volume to the power $n-1$, so the comparison is scale-free.

The first manuscript settles the conjecture from dimension four up.
[S4:34–34] states the result: "We prove the unpolarized conjecture in every
dimension at least four." The theorem is at [S4:37–37]: "For every integer
$n\ge4$ and every convex body $K\subset\R^n$," — the display gives the
inequality, and [S4:42–43] gives the equality case: "Equality holds if and
only if $K=a+TB_2^n$ for some $a\in\R^n$ and some invertible linear map $T$."
The abstract says the same: [S3:48–50] gives "We prove that ellipsoids
uniquely minimize the volume of the projection body among convex bodies of
fixed volume in every dimension at least four. This proves Petty's
projection-volume conjecture in these dimensions."

The theorem carries no regularity hypothesis. [S4:46–46] says: "The theorem
includes bodies without symmetry or boundary regularity."

The second manuscript attacks a different extremal question, the maximum
rather than the minimum. [S13:63–65] names the conjecture: "Brannen
conjectured in 1996 that simplices maximize \(R_d\) among all convex
bodies~\cite{Brannen}." [S13:91–93] states the counterexample: "Let
\(T_{10}=\conv(0,e_1,\ldots,e_{10})\subset\R^{10}\), where the \(e_i\) are the
coordinate unit vectors, and let \(K=T_{10}\times T_{10}\subset\R^{20}\)."
[S13:99–99] gives the conclusion: "Thus \(K\) violates \eqref{eq:proposed-bound}
in dimension twenty." The abstract gives the same: [S13:33–35] says "The
product of two ten-dimensional simplices has larger normalized projection-body
volume than a twenty-dimensional simplex. This gives a counterexample to
Brannen's proposed simplex maximum."

## Graduate summary

The first manuscript's proof passes from a body to a measure. [S4:101–101]
states the move: "The proof passes from a body to a positive measure on
vectors." The gauge and projection-measure machinery is at [S6:1], the
spherical sign estimate at [S7:1], the strict inequality for norms at [S8:1],
the variational representation and affine position at [S9:1], and the bilinear
inequality and equality cases at [S10:1].

The strictness is the load-bearing part. [S4:124–125] says: "The estimate is
strict except for the Euclidean norm, and no smoothness is needed." The
obstacle is a degree-two term: [S4:131–133] states it: "The degree-two
component must be removed by choosing affine coordinates; it is not a zero
eigenspace of the sign-test operator."

The manuscript states what the theorem gives beyond the conjecture.
[S4:151–153] says: "The theorem also gives the sharp Holmes--Thompson
isoperimetric inequality in normed spaces, where equality requires an
ellipsoidal norm ball and a body homothetic to it."

The consequences section is [S11:1].

The second manuscript's mechanism is a product identity. [S13:107–107] names
it: "The useful mechanism is a product test: for full-dimensional polytopes"
— the display gives the projection-body volume of a product as a product of
lower-dimensional volumes. [S13:121–123] states the reach of the identity:
"Iterating our product identity gives an exponential excess over the simplex
benchmark" — the sentence continues into the dimension threshold.

The second manuscript places its result against the known history.
[S13:72–74] separates the two problems: "For \(d\ge3\), Petty's separate
minimum problem asks whether ellipsoids are the only minimizers of the same
functional \(R_d\)" — Petty's conjecture is the minimum, Brannen's the
maximum.

The three-dimensional state is recorded next. [S13:76–80] says: "In dimension
three, Chen, Feng, Li, Xi, and Xu settle the minimum problem and also prove
the bound \(R_3(K)\le18=c_3\) for all three-dimensional convex bodies, with
tetrahedra attaining equality" — the citation is to their Theorems 1.1 and
1.2.

The earlier counterexamples are cited separately. [S13:80–83] records them:
"Feng, Hu, Liu, and Xu give counterexamples to \eqref{eq:proposed-bound} in
every dimension \(d\ge9\), using polytopes with at most \(d+2\) facets" — the
citation is to their Theorem 1.3.

The scope note records what the formalization carries. [S15:14] gives the
conjecture as the formalization states it: "with equality exactly for
ellipsoids; here $\kappa_j$ is the volume of the Euclidean unit ball in
dimension $j$. The formalization establishes this for every convex body
$K\subset\mathbb R^n$ and every $n\ge4$."

The scope note names what the formalized projection family leaves out.
[S15:16] says: "Other inequalities in the projection-body family are not
included."

The counterexample paragraph names the witness and the gap. [S15:18] states
it: "Brannen's simplex-maximization conjecture predicts that a simplex
maximizes normalized projection-body volume $|\Pi K|/|K|^{n-1}$ in dimension
$n$. The formalized counterexample is the product of two ten-dimensional
simplices. Its normalized projection volume, divided by that of a
twenty-dimensional simplex, is" — the display gives the ratio.

The scope note's last paragraph states the limit. [S15:22] says: "Thus the
proposed maximum fails in dimension $20$. The paper's exponential-factor
result for every sufficiently large dimension is not included."

The three declarations are the quantified forms. `OAI.PettyProjectionVolume.petty_projection_volume` at [S16:11] is the minimum
theorem, typed for every $n\ge4$. `OAI.ProjectionCounterexample.universal_simplex_upper_bound_false`
at [S17:96] is the dimension-twenty counterexample.
`OAI.Paper092.product_counterexample` at [S18:31] is the product identity the
third comparator config targets.

The three comparator configs state the targets the release set itself, and
each is a stub. [S19:49] carries `sorry`; [S20:39] carries `sorry`;
[S21:55] carries `sorry`. The scope note's comparator table links
`PettyProjectionVolume.lean`, `ProjectionCounterexample.lean`, and
`ProjectionVolume.lean`, one per formalized claim.

## History of the conjecture

Petty's conjecture is dated to Petty's 1971 work, cited at the same line the
conjecture is stated [S4:26–27], and the first manuscript's bibliography
carries the entry [S5:1].

Brannen's simplex-maximization conjecture is from 1996 [S13:63–65], and the
second manuscript's bibliography carries the entry [S14:1]. The earlier
counterexamples from Feng, Hu, Liu and Xu in dimensions at least nine are
cited at [S13:80–83], and the three-dimensional results of Chen, Feng, Li,
Xi and Xu at [S13:76–80].

The second manuscript states what its counterexample does not settle.
[S13:102–105] says: "The exact witness in Theorem~\ref{thm:counterexample}
provides an elementary illustration of the failure of the simplex maximum. The
optimal upper constant and its maximizing bodies remain separate
questions."

`notes/tables/conjecture-standing.tsv` carries no row for family 088, so the
prior on Petty's conjecture's standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

Petty's conjecture is settled from dimension four up, with the equality case
named: the minimizers are exactly the ellipsoids [S4:42–43], and the theorem
carries no symmetry or regularity hypothesis [S4:46–46].

The simplex maximum fails, and the failure is not confined to dimension
twenty. [S13:121–123] states the iteration: "Iterating our product identity
gives an exponential excess over the simplex benchmark" — the scope note
records that the formalized counterexample is the dimension-twenty witness
only [S15:22].

The two results sit in one family because they use the same functional.
[S15:14] and [S15:18] describe the minimum and the maximum of the same
normalized projection-body volume, and the second manuscript separates the two
problems explicitly [S13:72–74].

The release's own record is source-level. The scope note says the formalized
claims exist and names their declarations; the three comparator configs carry
`sorry`; no Lean run in this repository proves any of them elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 252 |
| S2 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/README.md`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/README.md) | 18 | Manuscript 1 title, date, citation |
| S3 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/main.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/main.tex) | 60 | Abstract, lines 48–50 |
| S4 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/01_introduction.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/01_introduction.tex) | 183 | Definition, conjecture, theorem, proof outline |
| S5 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/bibliography.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/bibliography.tex) | 132 | Bibliography entries |
| S6 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/02_gauges.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/02_gauges.tex) | 281 | Gauges and projection measures |
| S7 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/03_spherical.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/03_spherical.tex) | 359 | The spherical sign estimate |
| S8 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/04_norm.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/04_norm.tex) | 498 | The strict inequality for norms |
| S9 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/05_position.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/05_position.tex) | 409 | Variational representation and affine position |
| S10 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/06_conclusion.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/06_conclusion.tex) | 160 | The bilinear inequality and equality cases |
| S11 | [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/07_consequences.tex`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/07_consequences.tex) | 240 | Consequences |
| S12 | [`preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/README.md`](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/README.md) | 18 | Manuscript 2 title, date, citation |
| S13 | [`preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/main.tex`](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/main.tex) | 487 | Abstract, theorem, history, product identity |
| S14 | [`preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/references.tex`](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/references.tex) | 48 | Bibliography entries |
| S15 | [`lean/docs/088.md`](../../../lean/docs/088.md) | 30 | Scope note |
| S16 | [`lean/OAI/Geometry/ProjectionBodies/Main.lean`](../../../lean/OAI/Geometry/ProjectionBodies/Main.lean) | 25 | `PettyProjectionVolume.main` |
| S17 | [`lean/OAI/Geometry/ProjectionBody/Counterexample.lean`](../../../lean/OAI/Geometry/ProjectionBody/Counterexample.lean) | 105 | `ProjectionBodyCounterexample.main` |
| S18 | [`lean/OAI/Geometry/ProjectionVolume/ProductCounterexample.lean`](../../../lean/OAI/Geometry/ProjectionVolume/ProductCounterexample.lean) | 62 | `Paper092.product_counterexample` |
| S19 | [`lean/ComparatorChallenges/PettyProjectionVolume.lean`](../../../lean/ComparatorChallenges/PettyProjectionVolume.lean) | 54 | Stub, `sorry` at line 49 |
| S20 | [`lean/ComparatorChallenges/ProjectionCounterexample.lean`](../../../lean/ComparatorChallenges/ProjectionCounterexample.lean) | 45 | Stub, `sorry` at line 39 |
| S21 | [`lean/ComparatorChallenges/ProjectionVolume.lean`](../../../lean/ComparatorChallenges/ProjectionVolume.lean) | 61 | Stub, `sorry` at line 55 |

## Bibliography

- N. S. Brannen, _Volumes of projection bodies_, Mathematika **43** (1996), no. 2, 255–264. doi:10.1112/S002557930001175X.
- L. E. J. Brouwer, Über Abbildung von Mannigfaltigkeiten, _Math. Ann._ **71** (1911), 97–115.  .
- S. Chen, Y. Feng, Y. Li, D. Xi, and L. Xu, _Petty's conjectured projection inequality in dimension three_, preprint, 7 August 2026, MathSciDoc:2608.23001, 20 pp.  .
- S. Chen, Y. Feng, Y. Li, D. Xi, and L. Xu, _Petty's conjectured projection inequality in dimension three_, preprint, 2026, MathSciDoc:2608.23001. Full text.
- Y. Feng, S. Hu, W. Liu, and L. Xu, _On the reverse projection inequality_, preprint, 2026, MathSciDoc:2608.23002. Full text.
- R. J. Gardner, The Brunn–Minkowski inequality, _Bull. Amer. Math. Soc. (N.S.)_ **39** (2002), no. 3, 355–405.  .
- J. E. Haddad, A convex body associated to the Busemann random simplex inequality and the Petty conjecture, _J. Funct. Anal._ **281** (2021), no. 7, 109118.  . Preprint: arXiv:1904.10427v6, 10 January 2020.  .
- M. Henk, _Note on projection bodies of zonotopes with \(n+1\) generators_, Acta Mathematica Scientia **45** (2025), 96–103. doi:10.1007/s10473-025-0107-9.
- Y. Huang, E. Lutwak, D. Yang, and G. Zhang, Geometric measures in the dual Brunn–Minkowski theory and their associated Minkowski problems, _Acta Math._ **216** (2016), 325–388.  .
- Y. Huang, E. Lutwak, D. Yang, and G. Zhang, The $L_p$-Aleksandrov problem for $L_p$-integral curvature, _J. Differential Geom._ **110** (2018), no. 1, 1–29.  .
- M. N. Ivaki, A local uniqueness theorem for minimizers of Petty's conjectured projection inequality, _Mathematika_ **64** (2018), no. 1, 1–19.  . Preprint:  .
- M. Ludwig, Projection bodies and valuations, _Adv. Math._ **172** (2002), no. 2, 158–168.  .
- M. Ludwig, _Projection bodies and valuations_, Advances in Mathematics **172** (2002), no. 2, 158–168. doi:10.1016/S0001-8708(02)00021-X.
- E. Lutwak, On quermassintegrals of mixed projection bodies, _Geom. Dedicata_ **33** (1990), no. 1, 51–58.  .
- E. Lutwak, On a conjectured projection inequality of Petty, in _Integral Geometry and Tomography_ (Arcata, CA, 1989), Contemporary Mathematics **113**, American Mathematical Society, Providence, RI, 1990, pp. 171–182.
- F. Mielke-Sulz, _The Petty conjecture for convex bodies of revolution_, preprint, arXiv:2609.13517v1, 11 September 2026.  .
- H. Martini and Z. Mustafaev, Extensions of a Bonnesen-style inequality to Minkowski spaces, _Math. Inequal. Appl._ **11** (2008), no. 4, 739–748.  .
- C. M. Petty, Isoperimetric problems, in _Proceedings of the Conference on Convexity and Combinatorial Geometry_ (University of Oklahoma, Norman, 1971), Department of Mathematics, University of Oklahoma, pp. 26–41.
- C. M. Petty, _Projection bodies_, in _Proceedings of the Colloquium on Convexity (Copenhagen, 1965)_, K\o benhavns Universitet Matematiske Institut, Copenhagen, 1967, pp. 234–241.
- C. Saroglou, On the shape of a convex body with respect to its second projection body, _Adv. Appl. Math._ **67** (2015), 55–74.  . Preprint:  .
- C. Saroglou, _On the shape of a convex body with respect to its second projection body_, Advances in Applied Mathematics **67** (2015), 55–74. doi:10.1016/j.aam.2015.03.004. Preprint: arXiv:1409.4347v2.
- O. Ortega-Moreno and F. E. Schuster, Fixed points of Minkowski valuations, _Adv. Math._ **392** (2021), 108017.  . Author version:  .
- D. Spector, Simple proofs of some results of Reshetnyak, _Proc. Amer. Math. Soc._ **139** (2011), no. 5, 1681–1690.  . Author version:  .
- G. Zhang, The affine Sobolev inequality, _J. Differential Geom._ **53** (1999), no. 1, 183–202.
- Y. Huang and Y. Zhao, On the $L_p$ dual Minkowski problem, _Adv. Math._ **332** (2018), 57–84.  .
- H. Wang and J. Zhou, Uniqueness and continuity of the solution to $L_p$ dual Minkowski problem, _Commun. Math. Stat._ **14** (2026), no. 1, 105–140.  . Preprint:  .
- C. Saroglou and A. Zvavitch, Iterations of the projection body operator and a remark on Petty's conjectured projection inequality, _J. Funct. Anal._ **272** (2017), no. 2, 613–630.  .
- G. Ólafsson, A. Pasquale, and B. Rubin, Analytic and group-theoretic aspects of the cosine transform, in _Geometric Analysis and Integral Geometry_, Contemporary Mathematics **598**, American Mathematical Society, Providence, RI, 2013, pp. 167–188.  . Preprint:  .
