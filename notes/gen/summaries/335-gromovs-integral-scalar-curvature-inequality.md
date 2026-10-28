[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 335](../index/differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md)

# 335 — Gromov's integral scalar-curvature inequality

[Index page](../index/differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md)

## Original CONTENTS.md summary

The release's blurb [S1:8152] and the catalog abstract [S2:768] state
the family's claim: the integral scalar-curvature inequality for real
simplicial volume, plus the rational-inessentiality obstruction to
positive scalar curvature and its consequences. The family ships two
companion manuscripts. The first proves the integral bound
 "We prove the integral scalar-curvature inequality proposed by Gromov.
For every dimension \(n\ge3\), there is a constant \(a_n>0\), depending
only on \(n\), such that
$$\int_M(\mathrm{Scal}_g^-)^{n/2}\,dV_g\ge a_n\|M\|$$
for every closed connected oriented smooth \(n\)-manifold \(M\) and every
smooth Riemannian metric \(g\). Here
\(\mathrmScal_g^-:=\max\{0,-\mathrmScal_g\}\), and \(\|M\|\) is real simplicial volume.
The proof uses the nonnegative-scalar-curvature vanishing theorem of the
companion paper on rational inessentiality. [S3:49–61]"
The second proves the rational-inessentiality theorem on which the
first's proof depends [S5:113–123].

## Undergraduate summary

Simplicial volume measures the topological complexity of a manifold
through the $\ell^1$-seminorm of its real fundamental class. Gromov
connected this invariant with Riemannian volume under lower Ricci
curvature bounds, but a lower scalar curvature bound retains much less
directional information. In 1986 Gromov proposed that the integral of
the $n/2$-power of the negative part of scalar curvature still controls
simplicial volume, with a dimension-dependent constant [S4:4–65]:

> **Theorem 1.1**
For every integer \(n\ge3\), there is a constant \(a_n>0\), depending
only on \(n\), such that every closed connected oriented smooth
\(n\)-manifold \(M\) and every smooth Riemannian metric \(g\) on \(M\)
satisfy
$$\int_M(\mathrm{Scal}_g^-)^{n/2}\,dV_g\ge a_n\|M\|.$$ [S4:67–77]

The constant $a_n$ is uniform over the topology of $M$ and over all its
metrics, so the negative scalar curvature is permitted to be
concentrated in a small region. The companion manuscript proves the
qualitative input: every closed connected oriented smooth manifold
admitting a metric of nonnegative scalar curvature has zero real
simplicial volume [S5:113–123].

## Graduate summary

**The conformal reduction.** The proof of the integral bound begins
with a Yamabe reduction: if $\|M\|>0$, the vanishing input forces the
Yamabe minimizer in every conformal class to have negative scalar
curvature. Normalizing it to scalar curvature $-1$, Hölder's inequality
bounds the volume of this normalized metric by the integral for the
original metric, reducing the problem to proving
$\|M\|\le C_n\mathrm{Vol}_g(M)$ when $\mathrm{Scal}_g=-1$ [S4:90–203].

**The detector and the graph construction.** Bounded cohomology
supplies a cocycle of supremum norm at most one whose value on the
fundamental class is at least $\|M\|/2$, realized as a closed
differential form on a simplex of probability vectors. A graph
deformation enlarges the metric while preserving the weighted volume,
adapting the graph stabilization and prescribed-curvature method of the
companion manuscript. Iterating the construction produces a measured
equivariant family over $M$ with a density bounded by $dV_g$, a
deformed metric and weight, and a large energy coefficient satisfying a
leafwise inequality [S4:90–203].

**The degree estimate and the transfer.** A degree bound for maps from
a measured family of $d$-manifolds to a $d$-cube contains
$-\mathcal S/2$ and a penalty for the derivative of each coordinate, using
the $\mu$-bubble functional. In high dimensions the minimizing
boundaries can be singular; the residual map is moved away from the
target near the singular region. The final transfer construction
connects the cocycle integral to these degrees through Gaifullin's
reflected permutohedral realization, producing the bound
$I\le C_n\int\rho\le C_n\mathrm{Vol}_g(M)$ [S4:90–203].

**The rational-inessentiality proof.** The companion manuscript
converts a cohomology pairing into a local degree by adding a parameter
manifold, then changes the metric to contract the resulting map while
retaining positive scalar curvature. The four stages are: finite
comparison and local degree; a graph with one warped circle per
coordinate, whose fibre scalar loss is bounded by
$C(n+1)(2+\log q)L^2/w^2$; finite shortening with a summable cost; and
an obstruction independent of the circle count, using the local torical
theorem of Cecchini and Schick [S6:39–175].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` in each manuscript is the
only source.

## History of the conjecture

Simplicial volume was introduced by Gromov and connected to bounded
cohomology in the 1980s. His quantitative scalar-curvature/
simplicial-volume conjecture asks for a dimension-dependent upper bound
on simplicial volume in terms of Riemannian volume under a fixed
scalar-curvature lower bound. Braun and Sauer proved a macroscopic
counterpart when unit-ball volumes in the universal cover are uniformly
bounded. Ma, Wang, Xie, Yu, and Zhu proved the qualitative vanishing
for the spin case. Min, Zheng, and Zhu proved the integral estimate for
closed Kähler surfaces and an infinite family of symplectic
four-manifolds. The Gromov–Lawson aspherical conjecture, the
rational-inessentiality formulation of Hanke, and the homological
obstruction of Gromov and Yau all fall out of the companion
manuscript's theorem. Chodosh and Li established the aspherical
obstruction in dimensions four and five using generalized soap bubbles;
Gromov independently treated the closed five-dimensional case [S4:4–65].
The obstruction problem's earlier work includes the Schoen–Yau
minimal-surface method and the Gromov–Lawson Dirac-operator method [S6:258–331].

## Consequences

**Gromov's integral scalar-curvature inequality is proved.** For every
$n\ge3$ there is a constant $a_n>0$ such that
$\int_M(\mathrm{Scal}_g^-)^{n/2}\,dV_g\ge a_n\|M\|$ for every closed connected
oriented smooth $n$-manifold and every smooth metric [S4:67–77].

**The Gromov–Lawson aspherical conjecture is resolved.** No closed
smooth aspherical manifold, orientable or not, admits a Riemannian
metric of strictly positive scalar curvature [S6:22–30].

**Every nonnegative-scalar-curvature metric on a closed aspherical
manifold is flat.** This rigidifies the nonnegative case and applies
componentwise with no spin assumption [S6:193–197].

**Every closed oriented smooth manifold of positive dimension with
nonnegative scalar curvature has zero real simplicial volume.** This is
the qualitative vanishing consequence of Gromov's conjectural
comparison, proved without a spin hypothesis [S6:243–248].

**An oriented target-map obstruction.** If a continuous map
$f:M\to N$ of degree $d\ne0$ maps into a closed aspherical target $N$,
then $M$ admits no positive-scalar-curvature metric; in particular the
oriented connected sum $N\\#P$ admits no such metric [S6:215–225].

## Section skeleton

**Manuscript 1** [S3:49–61], 6 sections under `build/sections/`:
01-introduction [S4:67–77], 02-reduction-detector, 03-graphs, 04-entropy,
05-degree, 06-transfer. One figure (`build/figures/resolution.tex`).
Its root is `build/main.tex`, with a `references.tex` bibliography [S7].

**Manuscript 2** [S5], 8 sections under `build/sections/`:
01-introduction [S6], 02-reductions, 03-comparison, 04-graph-calculus,
05-graph-existence, 06-shortening, 07-obstruction, 08-proof. Two
figures (`build/figures/degree-triad.tex`,
`build/figures/direction-splitting.tex`). Its root is `build/main.tex`,
with a `references.bib` bibliography [S8].

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts: the first has a root `build/main.tex`, 6 `.tex` files
under `build/sections/`, one figure, and a `references.tex`
bibliography; the second has a root `build/main.tex`, 8 `.tex` files
under `build/sections/`, two figures, and a `references.bib`
bibliography. No non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 335 at line 8152. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 768. |
| S3 | [`preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/main.tex`](../../../preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/main.tex) | 73 | Manuscript 1 main file: title and abstract. |
| S4 | [`preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/sections/01-introduction.tex) | 203 | Manuscript 1 introduction: the simplicial volume setup, Gromov's 1986 conjecture, the main theorem, and the route to the estimate. |
| S5 | [`preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/main.tex`](../../../preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/main.tex) | 146 | Manuscript 2 main file: title and abstract. |
| S6 | [`preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/sections/01-introduction.tex) | 331 | Manuscript 2 introduction: the rational-inessentiality theorem, the four-stage construction, the four corollaries, and the obstruction problem. |
| S7 | [`preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/references.tex`](../../../preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/build/references.tex) | 164 | Manuscript 1 bibliography. |
| S8 | [`preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/references.bib`](../../../preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/build/references.bib) | 420 | Manuscript 2 bibliography. |

## Bibliography

- W. K. Allard, _On the first variation of a varifold_, Annals of Mathematics (2) **95** (1972), no. 3, 417–491. doi:10.2307/1970868.
- T. Aubin, _Équations différentielles non linéaires et probl\`eme de Yamabe concernant la courbure scalaire_, Journal de Mathématiques Pures et Appliquées (9) **55** (1976), no. 3, 269–296.
- Bi, Yuchen, Zhu, Jintian, Positive scalar curvature obstructions via singular dimension descent (2026)
- Bishop, R. L., O'Neill, B., Manifolds of negative curvature (1969)
- Braun, Sabine, Sauer, Roman, Volume and macroscopic scalar curvature (2021)
- Brunnbauer, Michael, Hanke, Bernhard, Large and small group homology (2010)
- Cairns, Stewart S., On the Triangulation of Regular Loci (1934)
- Cecchini, Simone, Schick, Thomas, Enlargeable metrics on nonspin manifolds (2021)
- Cheeger, Jeff, Gromoll, Detlef, The splitting theorem for manifolds of nonnegative Ricci curvature (1971)
- Chodosh, Otis, Li, Chao, Generalized soap bubbles and the topology of manifolds with positive scalar curvature (2024)
- Chodosh, Otis, Li, Chao, Recent results concerning topological obstructions to positive scalar curvature (2023)
- M. Eichmair, _The Plateau problem for marginally outer trapped surfaces_, Journal of Differential Geometry **83** (2009), no. 3, 551–583. doi:10.4310/jdg/1264601035.
- R. Frigerio, _Bounded cohomology of discrete groups_, preprint, 2016. arXiv:1610.08339v2.
- A. A. Gaifullin, _Realisation of cycles by aspherical manifolds_, Russian Mathematical Surveys **63** (2008), no. 3, 562–564. doi:10.1070/RM2008v063n03ABEH004540; arXiv:0806.3580.
- A. Gaifullin, _Universal realisators for homology classes_, Geometry & Topology **17** (2013), no. 3, 1745–1772. doi:10.2140/gt.2013.17.1745.
- Gilbarg, David, Trudinger, Neil S., Elliptic Partial Differential Equations of Second Order (2001)
- M. Gromov, _Volume and bounded cohomology_, Publications Mathématiques de l'IHÉS **56** (1982), 5–99. Numdam: PMIHES\_1982\_\_56\_\_5\_0.
- M. Gromov, _Large Riemannian manifolds_, in _Curvature and Topology of Riemannian Manifolds_, K. Shiohama, T. Sakai, and T. Sunada (eds.), Lecture Notes in Mathematics **1201**, Springer, Berlin, 1986, 108–121. doi:10.1007/BFb0075649.
- M. Gromov, _Positive curvature, macroscopic dimension, spectral gaps and higher signatures_, in _Functional Analysis on the Eve of the 21st Century, Volume II_, S. Gindikin, J. Lepowsky, and R. L. Wilson (eds.), Progress in Mathematics **132**, Birkhäuser, Boston, 1996, 1–213. doi:10.1007/978-1-4612-4098-3\_1.
- Gromov, Mikhael, Volume and bounded cohomology (1982)
- Gromov, Mikhael, Large Riemannian manifolds (1986)
- Gromov, Misha, Four lectures on scalar curvature (2023)
- Gromov, Mikhael, Lawson, Jr., H. Blaine, Positive scalar curvature and the Dirac operator on complete Riemannian manifolds (1983)
- Gromov, Misha, No metrics with positive scalar curvatures on aspherical 5-manifolds (2020)
- Gromov, Misha, A dozen problems, questions and conjectures about positive scalar curvature (2018)
- Guth, Larry, Volumes of balls in large Riemannian manifolds (2011)
- Hamilton, Richard S., Three-manifolds with positive Ricci curvature (1982)
- Hanke, Bernhard, Positive scalar curvature, $K$-area and essentialness (2012)
- Hatcher, Allen, Algebraic Topology (2002)
- N. V. Ivanov, _Notes on the bounded cohomology theory_, preprint, 2017, revised December 2020. arXiv:1708.05150v3.
- A. S. Kechris, _Classical Descriptive Set Theory_, Graduate Texts in Mathematics **156**, Springer, New York, 1995. doi:10.1007/978-1-4612-4190-4.
- O. Chodosh and C. Li, _Generalized soap bubbles and the topology of manifolds with positive scalar curvature_, Annals of Mathematics (2) **199** (2024), no. 2, 707–740. doi:10.4007/ annals.2024.199.2.3.
- Q. Ma, J. Wang, Z. Xie, G. Yu, and B. Zhu, _Gromov's simplicial volume vanishing conjecture for positive scalar curvature_, preprint, 2026. arXiv:2606.29135v4.
- Ma, Qiaochu, Wang, Jinmin, Xie, Zhizhang, Yu, Guoliang, Zhu, Bo, Gromov's simplicial volume vanishing conjecture for positive scalar curvature (2026)
- F. Maggi, _Sets of Finite Perimeter and Geometric Variational Problems: An Introduction to Geometric Measure Theory_, Cambridge Studies in Advanced Mathematics **135**, Cambridge University Press, Cambridge, 2012. doi:10.1017/CBO9781139108133.
- Milnor, John, A note on curvature and fundamental group (1968)
- J. Min, F. Zheng, and B. Zhu, _Simplicial volume and scalar curvature on closed Kähler surfaces_, preprint, 2026. arXiv:2608.17335v1.
- Munkres, James R., Elementary Differential Topology (1966)
- J. Nash, _The imbedding problem for Riemannian manifolds_, Annals of Mathematics (2) **63** (1956), no. 1, 20–63. doi:10.2307/1969989.
- OpenAI, _Positive scalar curvature forces rational inessentiality_, OpenAI Math Release preprint OAI:Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026, 2026.
- J. M. Lee and T. H. Parker, _The Yamabe problem_, Bulletin of the American Mathematical Society (N.S.) **17** (1987), no. 1, 37–91. doi:10.1090/S0273-0979-1987-15514-5.
- G. Perelman, _The entropy formula for the Ricci flow and its geometric applications_, preprint, 2002. arXiv:math/0211159.
- Yu. G. Reshetnyak, _Weak convergence of completely additive vector functions on a set_, Siberian Mathematical Journal **9** (1968), no. 6, 1039–1045. doi:10.1007/BF02196453.
- Sard, Arthur, The measure of the critical values of differentiable maps (1942)
- S. Braun and R. Sauer, _Volume and macroscopic scalar curvature_, Geometric and Functional Analysis **31** (2021), 1321–1376. doi:10.1007/s00039-021-00588-y.
- R. Schoen, _Conformal deformation of a Riemannian metric to constant scalar curvature_, Journal of Differential Geometry **20** (1984), no. 2, 479–495. doi:10.4310/jdg/1214439291.
- Schoen, Richard, Yau, Shing-Tung, Positive scalar curvature and minimal hypersurface singularities (2017)
- Schoen, Richard, Yau, Shing-Tung, On the structure of manifolds with positive scalar curvature (1979)
- Schoen, Richard, Yau, Shing-Tung, Existence of incompressible minimal surfaces and the topology of three dimensional manifolds with non-negative scalar curvature (1979)
- Schoen, Richard, Yau, Shing-Tung, Proof of the positive mass theorem. II (1981)
- Thom, René, Quelques propriétés globales des variétés différentiables (1954)
- Topping, Peter, Lectures on the Ricci Flow (2006)
- D. Gilbarg and N. S. Trudinger, _Elliptic Partial Differential Equations of Second Order_, second edition, Classics in Mathematics, Springer, Berlin, 2001. doi:10.1007/978-3-642-61798-0.
- N. S. Trudinger, _Remarks concerning the conformal deformation of Riemannian structures on compact manifolds_, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (3) **22** (1968), no. 2, 265–274. Numdam: ASNSP\_1968\_3\_22\_2\_265\_0.
- Wei, Guofang, Manifolds with a lower Ricci curvature bound (2007)
- Whitehead, J. H. C., On $C^1$-complexes (1940)
- H. Yamabe, _On a deformation of Riemannian structures on compact manifolds_, Osaka Mathematical Journal **12** (1960), no. 1, 21–37. doi:10.18910/8577.
- Yau, Shing-Tung, Review of geometry and analysis (2000)
