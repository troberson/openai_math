[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 077](../index/real-and-complex-analysis/077-fourier-restriction-for-positively-curved-surfaces.md)

# 077 — Fourier restriction for positively curved surfaces

[Index page](../index/real-and-complex-analysis/077-fourier-restriction-for-positively-curved-surfaces.md)

## Original CONTENTS.md summary

The release's blurb [S1:1922] and the catalog abstract [S2:228] state
the family's claim: the diagonal Fourier extension conjecture for
positively curved surfaces in three dimensions, in which the extension
operator is bounded from $`L^p(\Sigma)`$ to $`L^p(\mathbb R^3)`$ for every
$`p>3`$ and every compact smooth positively curved surface
$`\Sigma\subset\mathbb R^3`$, including surfaces with boundary. The two
manuscripts carry the statement on opposite sides of a single
dependence. The Diagonal paper proves the general-surface estimate
from two theorem inputs — the elliptic-capacity packet propagation
theorem and the Kakeya maximal theorem — while the Elliptic paper
proves both of those inputs together with the bounded-data sphere
estimate. Their abstract "We prove the bounded-data Fourier restriction conjecture for the sphere in
three dimensions: the Fourier extension operator maps $`L^\infty(S^2)`$
boundedly into $`L^p(\mathbb R^3)`$ for every $`p>3`$. This is the full conjectured
open range, and the threshold $`p=3`$ is sharp. [S6:2–5]"

## Undergraduate summary

The Fourier extension operator $`E_\Sigma`$ integrates a function
$`f`$ on a surface $`\Sigma`$ against the plane waves $`e^{2\pi i
x\cdot\xi}`$, producing a function on all of $`\mathbb R^3`$. The
diagonal restriction estimate asks for the exponents $`p`$ for which
$`E_\Sigma`$ is bounded on $`L^p`$: $`L^p(\Sigma)`$ to $`L^p(\mathbb R^3)`$.
The general-surface form of the conjecture [S4:18–27] holds for every
$`p>3`$:

> **theorem**
Let $`\Sigma\subset\mathbb R^3`$ be a compact smooth positively curved
surface, possibly with smooth boundary. For every $`3<p<\infty`$,
there is a finite constant $`C_{\Sigma,p}`$ such that
$$\|E_\Sigma f\|_{L^p(\mathbb R^3)}
 \le C_{\Sigma,p}\|f\|_{L^p(\Sigma)}$$
for every complex-valued $`f\in L^p(\Sigma)`$. [S4:18–27]

The companion paper states the bounded-data version for the sphere,
where the input is only required to be essentially bounded, and this
is the full conjectured open range 

> **theorem**
For every real $`p>3`$, there is a finite constant $`C_p`$, depending
only on $`p`$, such that
$$\|Eg\|_{L^p(\mathbb R^3)}
  \le C_p\|g\|_{L^\infty(S^2,\sigma)}$$
for every bounded measurable complex-valued function $`g`$ on $`S^2`$. [S6:21–29]

## Graduate summary

**Two manuscripts, one dependency.** The family ships as a pair that
meets at the Diagonal paper's two theorem inputs [S4:101–110]. The
Diagonal manuscript proves the estimate for a general positively
curved surface and consumes, as black boxes, the packet propagation
theorem and the Kakeya maximal theorem. The Elliptic manuscript is
where both of those inputs are proved, together with the sphere
result: it establishes the finite packet theorem, controls
coefficients through an elliptic capacity [S6:109–147], and states
the packet theorem in the full array form the Diagonal proof needs
[S6:193–306]. The Diagonal argument then converts the packet and the
maximal estimate into the surface bound through a dense
sparse-ball covering [S4:112–150].

**The two inputs and the transfer.** The packet theorem controls
arbitrary finite complex coefficient arrays through an elliptic
capacity with coordinate masks permitted; the Kakeya maximal theorem
controls nonnegative weighted tube concentration. The Diagonal proof
uses the former to control oscillatory coefficients and the latter,
by duality, to control their positive tube density, then removes the
spatial loss with a covering of each level set [S4:112–150]. The
dependence on the exponent is recorded explicitly [S4:152–174]: a
lower bound of order $`(p-3)^{-1/p}`$ is proved, while the loss the
proof produces is $`(p-3)^{-7/p}`$ times the two input constants, and
no polynomial rate in $`(p-3)^{-1}`$ is asserted for those constants.

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace for either manuscript; the LaTeX under `build/` is
the only source.

## History of the conjecture

The restriction problem originates in Stein's work. The
Tomas–Stein theory gives $`L^2(\Sigma)\to L^4(\mathbb R^3)`$ for
positively curved surfaces, and the bilinear framework of Tao,
Vargas, and Vega, Wolff's cone estimate, and Tao's paraboloid
estimate developed the role of wave packets and transverse
interactions. Bennett, Carbery, and Tao's multilinear estimates and
Bourgain–Guth's approach further connected those interactions to the
linear problem [S4:35–61].

Guth's polynomial-partitioning argument established the bounded-data
estimate for $`p>13/4`$, with diagonal estimates in that range from
Shayya and Kim, and Wang's broom method improving the truncated
paraboloid case. Wang and Wu proved the diagonal bound for
$`p>22/7`$ on compact positively curved surfaces, including surfaces
with boundary, using decoupling and two-ends Furstenberg
inequalities [S4:35–61]. For the sphere and quadratic graphs,
factorization gives a separate route from bounded-data to diagonal
estimates with an arbitrarily small increase in the exponent; the
argument here instead treats general smooth elliptic charts through
the packet theorem's full array formulation [S4:35–61].

## Consequences

**Diagonal: local smoothing and oscillatory integrals.** The compact
paraboloid case feeds a free Schrödinger local-smoothing
consequence, obtained from the Lee–Rogers–Seeger compact-frequency
transfer with both exponents equal to $`p`$ [S7:70–108]:

> **corollary**
For every $`3<p<\infty`$ and $`s>2-6/p`$, the free Schrödinger
propagator, initially defined on Schwartz functions, extends boundedly
from $`W^{s,p}(\mathbb R^2)`$ to $`L^p(\mathbb R^2\times[0,1])`$:
$$\|e^{it\Delta}f\|_{L^p(\mathbb R^2\times[0,1])}
 \le C_{p,s}\|f\|_{W^{s,p}(\mathbb R^2)}.$$ [S4:73–81]

Rogers's necessary condition shows the Sobolev threshold
$`s>2-6/p`$ cannot be lowered. A second consequence treats
translation-invariant oscillatory integrals whose curvature changes
only by a scalar multiple of itself, giving an $`L^p`$ estimate with
scaling factor $`N^{-3/p}`$ and no power loss in $`N`$ for every finite
$`p>3`$ [S7:110–224].

**Elliptic: Kakeya and the mixed-norm range.** The Kakeya maximal
consequence of the sphere estimate is, verbatim, the three-
dimensional Kakeya maximal theorem proved in family 074
[S8:9–101]:

> **corollary**
For every $`\varepsilon>0`$ there is a finite $`C_\varepsilon`$ such that,
for every $`0<\delta<1`$ and $`f\in L^3(\mathbb R^3)`$,
$$\|K_\delta f\|_{L^3(S^2,\sigma)}
 \le C_\varepsilon\delta^{-\varepsilon}\|f\|_{L^3(\mathbb R^3)}.$$ [S6:337–344]

Its proof uses sphere-specific factorization and does not invoke the
general-surface diagonal companion or the independent maximal
theorem. The diagonal sphere estimates also give the strict
mixed-norm range: for $`1<a\le\infty`$ and $`3<b<\infty`$ the
extension is bounded off the scaling line $`b=2a'`$ [S8:104–132].

## Section skeleton

**Diagonal manuscript** [S3], 7 sections under `build/sections/`:
introduction [S4], setup, packets, density, sparse, global, and
surfaces [S7].

**Elliptic manuscript** [S5], 9 sections under `build/sections/`:
introduction [S6], geometric, entropy, projection, aspect, packets,
extremal, global, and consequences [S8].

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts — 9 and 14 `.tex` files under their respective `build/`
trees — and no non-LaTeX evidence. The Diagonal manuscript cites the
Elliptic manuscript's results as theorem inputs, so its statement
depends on the companion, which the ledger's untyped citation edges
do not record as consequence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 077 at line 1922. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 228. |
| S3 | [`preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/paper.tex`](../../../preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/paper.tex) | 61 | Main file: title and section inputs (general positively curved surface). |
| S4 | [`preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/sections/00-introduction.tex) | 186 | The diagonal extension theorem, its background, the two theorem inputs, the argument, and the dependence on the exponent. |
| S5 | [`preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/paper.tex`](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/paper.tex) | 20 | Main file: title and section inputs (bounded-data sphere restriction and the packet theorem). |
| S6 | [`preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/sections/00-introduction.tex) | 490 | The sphere abstract and bounded theorem, the elliptic-capacity obstacle, the finite packet theorem, the Kakeya maximal consequence, and the argument. |
| S7 | [`preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/sections/06-surfaces.tex`](../../../preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/sections/06-surfaces.tex) | 224 | The free Schrödinger local-smoothing and translation-invariant oscillatory-integral consequences. |
| S8 | [`preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/sections/08-consequences.tex`](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/sections/08-consequences.tex) | 132 | The spherical consequences: the Kakeya maximal transfer and the open mixed-norm range. |
| S9 | [`preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/references.bib`](../../../preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/build/references.bib) | 228 | The Diagonal manuscript's bibliography. |
| S10 | [`preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/references.bib`](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/build/references.bib) | 585 | The Elliptic manuscript's bibliography. |

## Bibliography

- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- Bourgain, Jean, Besicovitch type maximal operators and applications to Fourier analysis (1991)
- Bourgain, Jean, Guth, Larry, Bounds on oscillatory integral operators based on multilinear estimates (2011)
- Bourgain, Jean, Besicovitch type maximal operators and applications to Fourier analysis (1991)
- Bourgain, Jean, The Discretized Sum-Product and Projection Theorems (2010)
- Bourgain, Jean, Demeter, Ciprian, The proof of the $`l^2`$ Decoupling Conjecture (2015)
- Bourgain, Jean, Guth, Larry, Bounds on oscillatory integral operators based on multilinear estimates (2011)
- Buschenhenke, Stefan, Factorization in Fourier restriction theory and near extremizers (2024)
- Buschenhenke, Stefan, Factorization in Fourier restriction theory and near extremizers (2024)
- Carleson, Lennart, Sjölin, Per, Oscillatory integrals and multiplier problem for the disc (1972)
- Fefferman, Charles, The multiplier problem for the ball (1971)
- Gao, Chuanwei, Liu, Diankun, Xi, Yakun, Curved Kakeya sets and Nikodym problems on manifolds (2025)
- Guo, Shaoming, Oh, Changkeun, Wang, Hong, Wu, Shukun, Zhang, Ruixiang, The Bochner–Riesz problem: an old approach revisited (2025)
- Guo, Shaoming, Oh, Changkeun, Wang, Hong, Wu, Shukun, Zhang, Ruixiang, The Bochner–Riesz problem: an old approach revisited (2025)
- Guth, Larry, A restriction estimate using polynomial partitioning (2016)
- Guth, Larry, Iosevich, Alex, Ou, Yumeng, Wang, Hong, On Falconer's distance set problem in the plane (2020)
- Guth, Larry, A restriction estimate using polynomial partitioning (2016)
- Guth, Larry, Wang, Hong, Zahl, Joshua, A streamlined proof of the Kakeya set conjecture in $`\mathbb{R}^{3}`$ (2026)
- Heinonen, Juha, Lectures on Lipschitz Analysis (2005)
- Hochman, Michael, On self-similar sets with overlaps and inverse theorems for entropy (2014)
- Hochman, Michael, Shmerkin, Pablo, Local entropy averages and projections of fractal measures (2012)
- Kaufman, Robert, On Hausdorff Dimension of Projections (1968)
- Kim, Jongchon, Some remarks on Fourier restriction estimates (2017)
- Kim, Jongchon, Some remarks on Fourier restriction estimates (2017)
- Lee, John M., Introduction to Smooth Manifolds (2013)
- Lee, Sanghyuk, Rogers, Keith M., Seeger, Andreas, On space–time estimates for the {Schrödinger} operator (2013)
- Marstrand, J. M., Some Fundamental Geometrical Properties of Plane Sets of Fractional Dimensions (1954)
- Mattila, Pertti, Lecture notes on the Fourier transform and Hausdorff dimension
- Oberlin, Daniel M., Restricted Radon Transforms and Projections of Planar Sets (2012)
- OpenAI, The Kakeya maximal conjecture in three dimensions (2026)
- OpenAI, Elliptic capacity propagation and Fourier restriction to the sphere (2026)
- OpenAI, Bochner–Riesz multipliers in three dimensions (2026)
- OpenAI, Diagonal Fourier extension for positively curved surfaces in three dimensions (2026)
- OpenAI, The Kakeya maximal conjecture in three dimensions (2026)
- Orponen, Tuomas, An improved bound on the packing dimension of Furstenberg sets in the plane (2020)
- Orponen, Tuomas, Shmerkin, Pablo, On the Hausdorff dimension of Furstenberg sets and orthogonal projections in the plane (2023)
- Orponen, Tuomas, Shmerkin, Pablo, Projections, Furstenberg sets, and the ABC sum-product problem (2026)
- Orponen, Tuomas, Shmerkin, Pablo, Wang, Hong, Kaufman and Falconer estimates for radial projections and a continuum version of Beck's theorem (2024)
- Córdoba, Antonio, A radial multiplier and a related Kakeya maximal function (1975)
- Ren, Kevin, Wang, Hong, Furstenberg sets estimate in the plane (2023)
- Rios, Cristian, Sawyer, Eric T., A smooth Alpert testing characterization of convolution type for the Fourier extension conjecture on paraboloids (2026)
- Hörmander, Lars, Oscillatory integrals and multipliers on $`FL^p`$ (1973)
- Rogers, Keith M., A local smoothing estimate for the {Schrödinger} equation (2008)
- Sawyer, Eric T., A comparison of trilinear testing conditions for the paraboloid Fourier extension and Kakeya conjectures in three dimensions (2026)
- Shannon, Claude E., A Mathematical Theory of Communication (1948)
- Shayya, Bassam, Weighted restriction estimates using polynomial partitioning (2017)
- Shayya, Bassam, Weighted restriction estimates using polynomial partitioning (2017)
- Shmerkin, Pablo, On the packing dimension of Furstenberg sets (2022)
- Shalender Singh, Vishnu Priya Singh Parmar, Repairing the refined-decoupling proof of the 5/4 planar pinned Falconer theorem (2026)
- Stein, Elias M., Some problems in harmonic analysis (1979)
- Stein, Elias M., Some problems in harmonic analysis (1979)
- Tao, Terence, The Bochner–Riesz conjecture implies the restriction conjecture (1999)
- Tao, Terence, A sharp bilinear restriction estimate for paraboloids (2003)
- Tao, Terence, Vargas, Ana, Vega, Luis, A bilinear approach to the restriction and Kakeya conjectures (1998)
- Tao, Terence, The Bochner–Riesz conjecture implies the restriction conjecture (1999)
- Tao, Terence, A sharp bilinear restriction estimate for paraboloids (2003)
- Tao, Terence, Sumset and inverse sumset theory for Shannon entropy (2010)
- Tao, Terence, An Introduction to Measure Theory (2011)
- Tao, Terence, Vargas, Ana, Vega, Luis, A bilinear approach to the restriction and Kakeya conjectures (1998)
- Tomas, Peter A., A restriction theorem for the Fourier transform (1975)
- Tomas, Peter A., A restriction theorem for the Fourier transform (1975)
- Tomas, Peter A., Restriction theorems for the Fourier transform (1979)
- Wang, Hong, A restriction estimate in $`\mathbb{R}^3`$ using brooms (2022)
- Wang, Hong, Wu, Shukun, Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities (2024)
- Wang, Hong, A restriction estimate in $`\mathbb{R}^3`$ using brooms (2022)
- Wang, Hong, Wu, Shukun, An improved restriction estimate in $`\mathbb{R}^3`$ (2022)
- Wang, Hong, Wu, Shukun, Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities (2024)
- Wang, Hong, Zahl, Joshua, Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions (2025)
- Wolff, Thomas, A sharp bilinear cone restriction estimate (2001)
- Wolff, Thomas H., An improved bound for Kakeya type maximal functions (1995)
- Wolff, Thomas, A sharp bilinear cone restriction estimate (2001)
