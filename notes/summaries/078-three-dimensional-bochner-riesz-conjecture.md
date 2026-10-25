[Notes](../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 078](../index/real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md)

# 078 — The three-dimensional Bochner–Riesz conjecture

[Index page](../index/real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1947] and the catalog abstract [S2:230] state
the family's claim: it resolves the three-dimensional Bochner–Riesz
conjecture in its strict range, in which the multipliers of order
$\delta$ are bounded on $L^p(\mathbb R^3)$ for every $1\le p\le\infty$
whenever $\delta>\max\{3|1/p-1/2|-1/2,0\}$. The manuscript proves the
estimate at $L^3$ for every positive order and reaches the full range
by interpolation and duality. Its abstract "We prove the three-dimensional Bochner–Riesz conjecture in its
strict-order formulation. The main result is boundedness of the
Bochner–Riesz multipliers on $L^3(\RR^3)$ for every positive order.
Interpolation and duality then give the full conjectured strict range. [S3:46–49]"

## Undergraduate summary

The Bochner–Riesz multiplier $T_\delta$ has multiplier
$(1-|\xi|^2)_+^\delta$, which softens the boundary of the frequency
ball. The question is how much smoothing — an order $\delta$ — is
needed to keep an $L^p$ norm. The manuscript's central estimate is
boundedness at $L^3$ for every positive order 

> **theorem**
For every $\delta>0$, there is a finite constant $C_\delta$ such that
$$\norm{T_\delta f}_{L^3(\RR^3)}
 \le C_\delta\norm f_{L^3(\RR^3)}
 \qquad(f\in\mathcal S(\RR^3)).
 \label{eq:main-bound}$$
Consequently $T_\delta$ has a unique bounded extension to $L^3(\RR^3)$. [S4:21–31]

Interpolating this with the $L^2$ bound and applying duality gives
the full conjugate range, the conjectured strict order [S4:33–40]:
"Theorem   gives
$$\norm{T_\delta f}_{L^p(\RR^3)}
 \lesssim_{p,\delta}\norm f_{L^p(\RR^3)},\qquad
 \delta>\max\left\{3\left|\frac1p-\frac12\right|-\frac12,0\right\},
 \quad 1\le p\le\infty .
 \label{eq:intro-full-range}$$ [S4:33–40]"

## Graduate summary

**Two stages: masses on lines, then wave packets.** The proof has two
stages [S4:147–220]. It first controls the information gained by
observing positive masses moving along lines, then transfers that
control to wave packets, whose squared amplitudes are positive but
whose superposition is oscillatory. The main obstruction sits at the
uncertainty boundary, where an earlier packet cannot be assigned a
position as precisely as a later observation requires.

In the first stage, aperture observations record velocity and
position of particles carrying bounded kinematic data, and a score
rewards fine resolution while penalizing eccentricity [S4:156–197].
Assuming excessive growth and localizing a sequence that reaches the
largest rate produces a saturated path; an isotropic extremizer is
excluded by a time-fiber, planar-projection, and Loomis–Whitney
argument, and the remaining case gives four data coordinates whose
resolution speeds are $0,1,m,1+m$. Matched clocks and planar
projections then transfer the lower bounds to a contradiction.

The second stage records the discrepancy at the boundary as fine
velocity information [S4:199–220]. Finite packet decompositions and
their tails show that too much growth — a rate above half the
positive-mass rate — would make that information exceed its finite
capacity, closing the contradiction.

**To the multiplier.** Packet growth gives an oscillatory-integral
estimate with arbitrarily small positive power loss; a
distance-phase change of variables puts a physical shell into the
required phase class, and choosing the loss below the order makes the
dyadic shell sum converge. A beta-integral representation supplies
the complex-order bounds used in Stein's analytic interpolation,
completing the full range [S4:222–235].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The problem belongs to the theory of summability of Fourier
expansions. Riesz's one-dimensional summation methods preceded
Bochner's spherical means for multiple Fourier series, and radial
inversion and summability were studied by Herz and Welland [S4:51–98].
For general functions the geometry of frequency directions is
essential: using a Kakeya construction, Fefferman proved the order-
zero ball multiplier unbounded on $L^p$ for $p\ne2$ in dimension at
least two, while Carleson and Sjölin established the conjectured
positive-order range in the plane.

Córdoba's work on radial multipliers and Kakeya maximal functions
connected the problem to the arrangement of long thin tubes and to
Fourier restriction; Bourgain combined geometric maximal-function
estimates with improved restriction and multiplier bounds in three
dimensions. The bilinear restriction theorems of Wolff and Tao led,
through Lee's multiplier reduction, to sharp-order estimates for
$\max\{p,p'\}\ge10/3$. More recently Wu obtained the strict-order
range for $\max\{p,p'\}\ge13/4$, and Gao, Wu, and Xi established the
range $\max\{p,p'\}\ge22/7$ [S4:51–98]. The connection runs in the
other direction as well: Tao showed the Bochner–Riesz conjecture
implies the spherical restriction conjecture, and Zipeng Wang has
proposed a proof in all dimensions.

## Consequences

**The full strict range.** The $L^3$ estimate yields the complete
strict-order range for $1\le p\le\infty$ 

> **corollary**
Let $1\le p\le\infty$ and
$$\label{eq:full-br-range}
 \delta>\max\left\{0,\,3\left|\frac1p-\frac12\right|-\frac12\right\}.$$
Then the multiplier $(1-|\xi|^2)_+^\delta$ is bounded on
$L^p(\RR^3)$.  The same bounds hold uniformly for every positive
radius after dilation.  This assertion concerns the strict
inequality  . [S5:437–447]

Its proof applies the positive-order theorem at arbitrarily small,
fixed orders, combines it with the beta-integral complex-order lemma,
and uses Stein's interpolation over the strip between $L^3$ and
$L^\infty$ [S5:449–470].

**Fourier inversion by mild smoothing.** For finite $p$ in the range,
the dilated multipliers converge to $f$ in $L^p$ as the radius tends
to infinity, recovering Fourier inversion by arbitrarily mild
spherical smoothing at the central exponents $3/2\le p\le3$
[S4:41–47].

**The multiplier section.** The final section turns the packet
growth into the operator bound, first establishing an oscillatory-
integral estimate with loss $\lambda^\nu$ for every $\nu>0$, uniform
over fixed phase and amplitude classes [S5:4–11].

## Section skeleton

**Manuscript** [S3:46–49], 12 sections under `build/sections/`:
introduction [S4], entropy, planar projection, classical extremality,
isotropic, characteristic plane, rate transfer, classical closure,
packet structure, packet composition, packet repayment, and
multiplier [S5:437–447].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 18 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | The release's blurb for family 078 at line 1947. |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The catalog abstract at line 230. |
| S3 | [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/paper.tex`](../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/paper.tex) | 71 | Main file: title, abstract, and section inputs. |
| S4 | [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/01-introduction.tex`](../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/01-introduction.tex) | 273 | The main L3 theorem, the full-range consequence, the development, and the two-stage argument. |
| S5 | [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/12-multiplier.tex`](../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/12-multiplier.tex) | 511 | The oscillatory-integral setup, the beta-integral complex-order lemma, and the full strict-range corollary. |
| S6 | [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/references.bib`](../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/references.bib) | 524 | The manuscript's bibliography. |

## Bibliography

- Bochner, Salomon, Summation of Multiple Fourier Series by Spherical Means (1935)
- Bochner, Salomon, Summation of Multiple Fourier Series by Spherical Means (1936)
- Bourgain, Jean, On the restriction and multiplier problems in $\mathbb{R}^3$ (1991)
- Bourgain, Jean, The Discretized Sum-Product and Projection Theorems (2010)
- Carleson, Lennart, Sjölin, Per, Oscillatory Integrals and Multiplier Problem for the Disc (1972)
- Fefferman, Charles, The Multiplier Problem for the Ball (1971)
- Gao, Chuanwei, Wu, Shukun, Xi, Yakun, Sharp microlocal Kakeya–Nikodym estimates for eigenfunctions with applications (2026)
- Guo, Shaoming, Oh, Changkeun, Wang, Hong, Wu, Shukun, Zhang, Ruixiang, The Bochner–Riesz Problem: An Old Approach Revisited (2025)
- Guth, Larry, A restriction estimate using polynomial partitioning (2016)
- Herz, Carl S., On the Mean Inversion of Fourier and Hankel Transforms (1954)
- Hochman, Michael, Shmerkin, Pablo, Local Entropy Averages and Projections of Fractal Measures (2012)
- Hochman, Michael, On Self-Similar Sets with Overlaps and Inverse Theorems for Entropy (2014)
- Kaufman, Robert, On Hausdorff Dimension of Projections (1968)
- Kullback, Solomon, Leibler, Richard A., On Information and Sufficiency (1951)
- Lee, Sanghyuk, Improved bounds for Bochner–Riesz and maximal Bochner–Riesz operators (2004)
- Loomis, L. H., Whitney, H., An inequality related to the isoperimetric inequality (1949)
- Marstrand, J. M., Some Fundamental Geometrical Properties of Plane Sets of Fractional Dimensions (1954)
- Oberlin, Daniel M., Restricted Radon Transforms and Projections of Planar Sets (2012)
- OpenAI, Elliptic capacity propagation and Fourier restriction to the sphere (2026)
- OpenAI, Diagonal Fourier extension for positively curved surfaces in three dimensions (2026)
- OpenAI, Critical local smoothing for the three-dimensional wave equation (2026)
- Orponen, Tuomas, Shmerkin, Pablo, Wang, Hong, Kaufman and Falconer Estimates for Radial Projections and a Continuum Version of Beck's Theorem (2024)
- Orponen, Tuomas, An improved bound on the packing dimension of Furstenberg sets in the plane (2020)
- Orponen, Tuomas, Shmerkin, Pablo, On the Hausdorff dimension of Furstenberg sets and orthogonal projections in the plane (2023)
- Orponen, Tuomas, Shmerkin, Pablo, Projections, Furstenberg sets, and the ABC sum-product problem (2026)
- Córdoba, Antonio, A Radial Multiplier and a Related Kakeya Maximal Function (1975)
- Córdoba, Antonio, The Kakeya Maximal Function and the Spherical Summation Multipliers (1977)
- Ren, Kevin, Wang, Hong, Furstenberg Sets Estimate in the Plane (2025)
- Riesz, Marcel, Sur la sommation des séries de Fourier (1923)
- Shannon, Claude E., A Mathematical Theory of Communication (1948)
- Shmerkin, Pablo, Wang, Hong, On the distance sets spanned by sets of dimension $d/2$ in $\mathbb{R}^d$ (2025)
- Shmerkin, Pablo, On the packing dimension of Furstenberg sets (2022)
- Stein, Elias M., Interpolation of Linear Operators (1956)
- Tao, Terence, The Bochner–Riesz Conjecture Implies the Restriction Conjecture (1999)
- Tao, Terence, A sharp bilinear restriction estimate for paraboloids (2003)
- Tao, Terence, Sumset and Inverse Sumset Theory for Shannon Entropy (2010)
- Wang, Hong, Wu, Shukun, Restriction Estimates Using Decoupling Theorems and Two-Ends Furstenberg Inequalities (2024)
- Wang, Hong, A restriction estimate in $\mathbb{R}^3$ using brooms (2022)
- Wang, Zipeng, $L^p$-boundedness of the Bochner–Riesz operator (2026)
- Welland, G. V., Norm Convergence of Riesz-Bochner Means for Radial Functions (1975)
- Wolff, Thomas, A sharp bilinear cone restriction estimate (2001)
- Wu, Shukun, {On the Bochner–Riesz Operator in $\mathbb{R}^{3}$} (2023)
