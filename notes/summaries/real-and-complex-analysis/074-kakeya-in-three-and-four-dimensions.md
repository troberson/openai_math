[Notes](../../README.md) / [Summaries](../README.md) / [Real and complex analysis](../../index/disciplines/real-and-complex-analysis.md) / [Family 074](../../index/real-and-complex-analysis/074-kakeya-in-three-and-four-dimensions.md)

# 074 — Kakeya in three and four dimensions

[Index page](../../index/real-and-complex-analysis/074-kakeya-in-three-and-four-dimensions.md)

## Original CONTENTS.md summary

The release's blurb [S1:1847] and the catalog abstract [S2:222] state
the family's claim together: it resolves the Kakeya maximal conjecture
in three dimensions and the Hausdorff-dimension Kakeya conjecture in
four. In three dimensions the radius-$\delta$ tube maximal operator
maps $L^3(\mathbb R^3)$ to $L^3(S^2)$ with norm
$O_\varepsilon(\delta^{-\varepsilon})$ for every $\varepsilon>0$; in
four dimensions every set containing a unit segment in every direction
has Hausdorff dimension four. The two manuscripts carry the
quantitative statements; their abstracts are quoted in the graduate
section.

## Undergraduate summary

A Kakeya set in $\mathbb R^n$ is a set that contains a unit line
segment in every direction. The question is how large such a set must
be. Besicovitch's constructions show a Kakeya set can have Lebesgue
measure zero, so measure is not the right lower bound; the dimension
conjecture asks instead for full Hausdorff dimension.

In three dimensions the paper takes the analytic route and bounds the
tube maximal operator. Given a unit $\delta$-tube, $K_\delta f$
records the largest average of $|f|$ over all such tubes in a fixed
direction. The theorem bounds this operator on $L^3$:

> For every \(\varepsilon>0\) there exists a finite constant
\(C_\varepsilon\) such that, for every \(0<\delta<1\) and every
\(f\in L^3(\R^3)\),
\[
\|K_\delta f\|_{L^3(S^2)}
\le C_\varepsilon\delta^{-\varepsilon}
     \|f\|_{L^3(\R^3)}.
\] [S4:17–26]

In four dimensions the paper states the dimension conjecture
directly, with no regularity hypothesis on the set or its witnessing
segments 

> **theorem**
Let \(K\subset\mathbb R^4\). Suppose that for every \(e\in S^3\) there is a point
\(a_e\in\mathbb R^4\) such that
\[
  \{a_e+te:0\leq t\leq1\}\subset K.
\]
Then \(\dim_H K=4\). [S6:8–15]

## Graduate summary

**Two manuscripts, one geometric problem.** The family ships as two
papers that meet the Kakeya problem from opposite sides. The
three-dimensional paper proves a maximal-operator estimate; the
four-dimensional paper states the Hausdorff-dimension conclusion
directly. The first abstract "We prove the Kakeya maximal conjecture in three dimensions. For every
\(\varepsilon>0\), the maximal average over unit tubes of radius \(\delta\)
maps \(L^3(\R^3)\) to \(L^3(S^2)\) with norm at most
\(C_\varepsilon\delta^{-\varepsilon}\). [S3:9–12]" The second 
"We prove the four-dimensional Hausdorff-dimension Kakeya conjecture:
every subset of \(\mathbb R^4\) containing a unit line segment in every
direction has Hausdorff dimension four. No compactness or regularity
assumption is imposed on the set or its witnessing line family. [S5:58–61]"

**The three-dimensional maximal estimate.** The operator $K_\delta f$
is the average of $|f|$ over unit $\delta$-tubes of radius $\delta$,
supremized over positions, recorded for each direction $\omega\in
S^2$. The essential quantitative feature is not the $L^3$ bound alone
but its *uniformity in the shading density*: the estimate holds for a
tube family weighted by an arbitrary measurable subset of each tube,
uniformly in the density $\lambda$ of that subset [S4:35–68]. The
proof builds a density-sensitive extremal problem, shows an equality
configuration forces full temporal branching on the initial logarithmic
scales, and closes the contradiction with a two-frame entropy and
radial-projection argument [S4:45–160].

**The four-dimensional Hausdorff statement.** The theorem is stated
for arbitrary subsets: neither the set nor the choice of witnessing
segments is required to be measurable, and no packing-dimension or
stickiness hypothesis is imposed on the family of witnessing lines
[S6:17–24]. The Hausdorff dimension is taken from the covering
definition, which needs no measurability. The proof turns a
hypothetical dimension deficit into a weighted line problem and rules
it out with quadratic local fits ("charts") nested across scales,
split over three geometric narrowness regimes [S6:140–260].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace for either manuscript; the LaTeX under
`build/` is the only source.

## History of the conjecture

The problem grows out of the classical needle question: how small a
planar region can be if a unit segment is to turn continuously within
it and return with its endpoints reversed. Besicovitch showed the area
can be arbitrarily small, and that a Kakeya set can have Lebesgue
measure zero; Davies proved full Hausdorff dimension in the plane, and
Córdoba's planar maximal estimates gave the analytic counterpart
[S4:35–68].

Wolff's hairbrush argument gave the maximal estimates implying the
Hausdorff-dimension bound $(n+2)/2$, which is $5/2$ in three
dimensions; Katz, Łaba, and Tao improved the upper Minkowski bound
past $5/2$ by identifying stickiness, planiness, and graininess in
near-extremal tube families, and Katz and Zahl improved the Hausdorff
bound over $5/2$ [S4:45–68].

The three-dimensional set problem was resolved through the Wang--Zahl
sequence — the sticky Kakeya theorem, then the full Assouad-dimension
theorem, then the Hausdorff- and Minkowski-dimension theorem for
arbitrary Kakeya sets — and the streamlined Guth--Wang--Zahl proof
supplies the set estimate used here [S4:68–90]. In four dimensions
the prior Hausdorff improvements addressed concentration near
algebraic sets — the polynomial Wolff bounds reaching $3+1/40$, the
Katz--Zahl planebrush reaching $3.059$ — and Rai Choudhuri proved
$13/4$ for compact sticky sets, a hypothesis that does not cover
arbitrary Kakeya sets [S6:26–120].

## Consequences

**Three dimensions: Nikodym and curved.** The maximal estimate feeds
the Kakeya-to-Nikodym transfer of Gao, Liu, and Xi, giving Nikodym
maximal estimates in $\mathbb R^3$ and locally on constant-curvature
three-manifolds [S7:14–39]. At the critical $p=q=3$ "In particular, at \(p=q=3\) the operator norms are bounded by
\(C_\varepsilon\delta^{-\varepsilon}\) in Euclidean space and
\(C_{\varepsilon,U,V,g}\delta^{-\varepsilon}\) in the fixed local
geometry. [S7:56–59]"
The same estimate also supplies a local curved Kakeya estimate for a
fixed nondegenerate translation-invariant phase satisfying Bourgain's
condition [S7:60–120].

**Four dimensions: dimension and curvature.** Beyond the Hausdorff
statement, every four-dimensional Kakeya set also has packing
dimension four, and a bounded one has both Minkowski dimensions four
[S8:11–21]. The result projects to a lower bound in dimension
$d\ge4$ [S8:25–35]; a Keleti--Máté transfer extends it to arbitrary
direction sets and gives a line-segment extension principle
[S8:40–63]. The Gao--Liu--Xi Kakeya-to-Nikodym implication gives the
four-dimensional Nikodym conclusion 

> **corollary**
Let \((M^4,g)\) be a Riemannian manifold of constant sectional
curvature in the preceding normalized setting. Every Nikodym set
\(\Omega\subset M\) has \(\dim_H\Omega=4\). [S8:105–110]

A fixed-chart curved Kakeya corollary and a three-dimensional
quadratic curved consequence (via Nadjimzadah's lifting) follow in the
same section [S8:110–260].

## Section skeleton

**Three-dimensional manuscript** [S3:9–12], 12 sections under
`build/sections/`: introduction [S4:17–26], critical, inputs, local,
stationary, estimates, entropy, projections, projection-proofs,
closure, and consequences [S7:56–59].

**Four-dimensional manuscript** [S5:58–61], 15 sections under
`build/sections/`: introduction [S6:8–15], framework, comparison,
critical-paths, scalar-tools, isotropic, retained-edge, finite-
narrowness, critical-rates, unbounded-narrowness, and consequences
[S8:105–110].

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts — 16 and 13 `.tex` files under their respective `build/`
trees — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 074 at line 1847. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 222. |
| S3 | [`preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/paper.tex`](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/paper.tex) | 28 | Main file: title, abstract, and section inputs (three dimensions). |
| S4 | [`preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/sections/introduction.tex) | 247 | The three-dimensional maximal theorem, the density feature, the set-vs-maximal distinction, and the proof geometry. |
| S5 | [`preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/paper.tex`](../../../preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/paper.tex) | 78 | Main file: title, abstract, and section inputs (four dimensions). |
| S6 | [`preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/01-introduction.tex) | 328 | The four-dimensional Hausdorff theorem, the no-regularity hypothesis, the input estimates, and the proof mechanisms. |
| S7 | [`preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/sections/80-consequences.tex`](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/sections/80-consequences.tex) | 166 | The three-dimensional Nikodym and curved Kakeya consequences via the Gao--Liu--Xi transfer. |
| S8 | [`preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/10-consequences.tex`](../../../preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/10-consequences.tex) | 347 | The four-dimensional packing, projection, direction-set, Nikodym, and curved consequences. |
| S9 | [`preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/references.bib`](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/build/references.bib) | 269 | The three-dimensional manuscript's bibliography. |
| S10 | [`preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/references.bib`](../../../preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/references.bib) | 440 | The four-dimensional manuscript's bibliography. |

## Bibliography

- {\L}aba, Izabella, Tao, Terence, An improved bound for the Minkowski dimension of Besicovitch sets in medium dimension (2001)
- Ambrosio, Luigi, Fusco, Nicola, Pallara, Diego, Functions of Bounded Variation and Free Discontinuity Problems (2000)
- Basu, Saugata, Pollack, Richard, Roy, Marie-Fran{ç}oise, Algorithms in Real Algebraic Geometry (2006)
- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- Besicovitch, A. S., On Kakeya's problem and a similar one (1928)
- Besicovitch, A. S., On Kakeya's problem and a similar one (1928)
- Borges, Tainara, Chan, Tiklung, Chen, Mingfeng, Liu, Diankun, Xi, Yakun, Zhan, Yufei, Restriction and Kakeya maximal estimates in $\mathbb{R}^4$ (2025)
- Bourgain, Jean, Besicovitch type maximal operators and applications to Fourier analysis (1991)
- Bourgain, Jean, Guth, Larry, Bounds on oscillatory integral operators based on multilinear estimates (2011)
- Bourgain, Jean, On the dimension of Kakeya sets and related maximal inequalities (1999)
- Carbery, Anthony, Valdimarsson, Stef{á}n Ingi, The endpoint multilinear Kakeya theorem via the Borsuk–Ulam theorem (2013)
- Rai Choudhuri, Mukul, An improved bound on the Hausdorff dimension of sticky Kakeya sets in $\mathbb{R}^4$ (2026)
- Christ, Michael, Quasiextremals for a Radon-like transform (2011)
- Cover, Thomas M., Thomas, Joy A., Elements of Information Theory (2006)
- Davies, Roy O., Some remarks on the Kakeya problem (1971)
- Davies, Roy O., Some remarks on the Kakeya problem (1971)
- Fefferman, Charles, The multiplier problem for the ball (1971)
- Fujiwara, M., Kakeya, S., On some Problems of Maxima and Minima for the Curve of Constant Breadth and the In-revolvable Curve of the Equilateral Triangle (1917)
- Gao, Chuanwei, Liu, Diankun, Xi, Yakun, Curved Kakeya sets and Nikodym problems on manifolds (2025)
- Gao, Chuanwei, Liu, Diankun, Xi, Yakun, Curved Kakeya sets and Nikodym problems on manifolds (2025)
- Guo, Shaoming, Wang, Hong, Zhang, Ruixiang, A dichotomy for {H{ö}rmander}-type oscillatory integral operators (2024)
- Guth, Larry, Wang, Hong, Zahl, Joshua, A streamlined proof of the Kakeya set conjecture in $\mathbb R^3$ (2026)
- Guth, Larry, The endpoint case of the Bennett–Carbery–Tao multilinear Kakeya conjecture (2010)
- Guth, Larry, Wang, Hong, Zahl, Joshua, A streamlined proof of the Kakeya set conjecture in $\mathbb{R}^3$ (2026)
- Guth, Larry, Zahl, Joshua, Polynomial Wolff axioms and Kakeya-type estimates in $\mathbb{R}^4$ (2018)
- Guth, Larry, The endpoint case of the Bennett–Carbery–Tao multilinear Kakeya conjecture (2010)
- Hochman, Michael, Shmerkin, Pablo, Local entropy averages and projections of fractal measures (2012)
- Katz, Nets Hawk, {\L}aba, Izabella, Tao, Terence, An improved bound on the Minkowski dimension of Besicovitch sets in $\mathbb R^3$ (2000)
- Katz, Nets Hawk, Zahl, Joshua, An improved bound on the Hausdorff dimension of Besicovitch sets in $\mathbb R^3$ (2019)
- Katz, Nets Hawk, Zahl, Joshua, A Kakeya maximal function estimate in four dimensions using planebrushes (2021)
- Katz, Nets Hawk, Rogers, Keith M., On the polynomial Wolff axioms (2018)
- Katz, Nets Hawk, {\L}aba, Izabella, Tao, Terence, An improved bound on the Minkowski dimension of Besicovitch sets in $\mathbb{R}^3$ (2000)
- Katz, Nets Hawk, Tao, Terence, New bounds for Kakeya problems (2002)
- Keleti, Tam{á}s, M{á}th{é}, Andr{á}s, Equivalences between different forms of the Kakeya
                   conjecture and duality of Hausdorff and packing
                   dimensions for additive complements (2023)
- Nadjimzadah, Arian, Bourgain's Condition, Sticky Kakeya, and New Examples (2026)
- Nadjimzadah, Arian, Lifting curved Kakeya sets to linear Kakeya sets (2026)
- OpenAI, Elliptic capacity propagation and Fourier restriction to the sphere (2026)
- OpenAI, The Kakeya maximal conjecture in three dimensions (2026)
- Orponen, Tuomas, Shmerkin, Pablo, Wang, Hong, Kaufman and Falconer estimates for radial projections and a continuum version of Beck's theorem (2024)
- Orponen, Tuomas, de Saxc{é}, Nicolas, Shmerkin, Pablo, On the Fourier decay of multiplicative convolutions (2024)
- C{ó}rdoba, Antonio, The Kakeya maximal function and the spherical summation multipliers (1977)
- Ren, Kevin, Wang, Hong, Furstenberg sets estimate in the plane (2025)
- Roytwarf, N., Yomdin, Y., Bernstein classes (1997)
- Shmerkin, Pablo, Wang, Hong, On the distance sets spanned by sets of dimension $d/2$ in $\mathbb R^d$ (2025)
- Sudakov, Benny, Szemer{é}di, Endre, Vu, Van H., On a question of {Erdős} and Moser (2005)
- Tao, Terence, Vu, Van H., Additive Combinatorics (2006)
- Wang, Hong, Zahl, Joshua, Sticky Kakeya sets and the sticky Kakeya conjecture (2026)
- Wang, Hong, Zahl, Joshua, Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions (2025)
- Wang, Hong, Wu, Shukun, Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities (2024)
- Wang, Hong, Zahl, Joshua, The Assouad dimension of Kakeya sets in $\mathbb R^3$ (2025)
- Wang, Hong, Zahl, Joshua, Sticky Kakeya sets and the sticky Kakeya conjecture (2026)
- Wang, Hong, Zakharov, Dmitrii, Kakeya and Furstenberg problems for sticky sets of tubes (2026)
- Wang, Hong, Zahl, Joshua, Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions (2025)
- Wolff, Thomas H., An improved bound for Kakeya type maximal functions (1995)
- Wolff, Thomas H., An improved bound for Kakeya type maximal functions (1995)
- Zahl, Joshua, A survey of the Kakeya conjecture, 2000–2025 (2025)
- Zahl, Joshua, A discretized Severi-type theorem with applications to harmonic analysis (2018)
