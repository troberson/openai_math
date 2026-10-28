[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 079](../index/real-and-complex-analysis/079-local-smoothing-for-the-euclidean-wave-equation.md)

# 079 — Local smoothing for the Euclidean wave equation

[Index page](../index/real-and-complex-analysis/079-local-smoothing-for-the-euclidean-wave-equation.md)

## Original CONTENTS.md summary

The release's blurb [S1:1963] and the catalog abstract [S2:232]
state the family's claim: it resolves Sogge's Euclidean local
smoothing conjecture for the wave equation in three spatial
dimensions, with the full strict range $2<p<\infty$ and Sobolev
regularity above $\max\{0,1-3/p\}$. The critical $L^3$ estimate
holds with every positive Sobolev loss; the lossless $\varepsilon=0$
estimate is not addressed. The manuscript's abstract [S4:2–4]:
"We prove the critical $L^3$ local smoothing estimate for the wave equation
in three spatial dimensions, with every positive Sobolev loss. This resolves
Sogge's Euclidean local smoothing conjecture in dimension three. [S4:2–4]"

## Undergraduate summary

The wave evolution $Uf$ maps initial data to a spacetime solution.
The local smoothing estimate asks how much extra regularity
$J^\alpha$ in the data is needed to bound $Uf$ in a spacetime $L^p$
norm. The sharp fixed-time estimate loses $2(1/2-1/p)$ derivatives;
time integration recovers part of that loss. Sogge's conjecture
predicts the full strict range, and the critical exponent is
$p=3$ [S4:9–23]. The manuscript proves that critical case for every
positive loss 

> **Theorem 1.1**
For every $\varepsilon>0$ there exists $C_\varepsilon<\infty$ such that
$$\label{eq:intro-main}
 \lVert Uf\rVert_{L^3(\mathbb R^3\times[1,2])}
 \le C_\varepsilon\lVert J^\varepsilon f\rVert_{L^3(\mathbb R^3)}
 \qquad (f\in\mathcal S(\mathbb R^3)).$$ [S4:25–32]

Interpolating with the $L^2$ energy estimate and an $L^\infty$
kernel bound gives the complete range [S4:34–46]: "$$\label{eq:intro-full}
 \lVert Uf\rVert_{L^p(\mathbb R^3\times[1,2])}
 \le C_{p,\alpha}\lVert J^\alpha f\rVert_{L^p(\mathbb R^3)},
 \qquad
 2<p<\infty,\quad \alpha>\max\{0,1-3/p\}.$$ [S4:38–43]"

## Graduate summary

**From one annulus to the full estimate.** The proof proceeds on a
single frequency annulus $|\xi|\asymp H^{-1}$: the physical half-wave
should map $L^3$ to spacetime $L^3$ with loss at most $H^{-\delta}$
for every $\delta>0$, and summing over annuli gives the full
estimate [S4:209–226]. On a fixed angular chart, null coordinates
turn the light rays into parabola-like trajectories, and the wave is
analyzed into packets whose energy is measured by squared $L^2$
norms.

**The cubic functional and the round/cylinder models.** The
intermediate scales use round and cylinder test windows with
different aspect penalties: $r^4f^{1-\eta}$ in the round model and
$r^{3+\eta}f^{1-\eta}$ in the cylinder, where $r$ is the angular
radius and $f$ the normal thickness. A normalized cubic sum
$\mathcal B_s$ of packet masses is the main object, bounded with a
scale loss tending to zero as $\eta\to0$ and through controlled
errors [S4:228–255].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Sogge introduced local smoothing in his study of circular maximal
operators, proving a positive gain from time averaging in two
spatial dimensions and proposing the critical higher-dimensional
formulation [S4:89–205]. In three dimensions the conjecture asks to
recover almost $1/p$ derivatives when $p\ge3$; at $p=3$ the time
averaging should remove all but an arbitrarily small part of the
fixed-time loss of $1/3$. The connection with Fourier summation was
part of the original formulation: Sogge showed how critical smoothing
implies Bochner–Riesz bounds.

One approach separates the angular decomposition from the geometry
of rays: Mockenhaupt–Seeger–Sogge developed square-function
estimates, Wolff obtained the conjectured gain for large $p$ in two
dimensions, and $\L$aba–Wolff extended the decoupling method to
higher dimensions. Bourgain–Demeter's prism decoupling theorem and
Burr–Demeter's local smoothing consequence gave a broad-narrow
framework. More recently, Gao, Liu, Miao, and Xi established the
strict-order range for $\max\{p,p'\}\ge22/7$, and Gan, He, Li, and
Wu developed packet-density methods [S4:89–205].

## Consequences

**Bochner–Riesz summation.** The local-smoothing estimate feeds the
established Beltran–Hickman–Sogge implications: the maximal result
bounds the Bochner–Riesz maximal operator strongly on $L^p$ and
gives almost-everywhere convergence for $3\le p<\infty$ and
$\delta>1-3/p$, while the nonmaximal result gives uniform bounds for
the individual means throughout the strict range
$\delta>\max\{3|1/p-1/2|-1/2,0\}$ "We apply the established local-smoothing implications of
Beltran–Hickman–Sogge to Corollary . The maximal
result concerns the family in ; the subsequent
nonmaximal result concerns the individual linear means.
These means recover a function by gradually admitting higher
frequencies, with order $\delta$ smoothing the boundary of the Fourier [S5:3–8]"

**The spherical restriction and Kakeya link.** The final subsection
connects the local-smoothing estimate to the three-dimensional
spherical restriction conjecture and the Kakeya maximal estimate,
noting that the full Bochner–Riesz range at $p=3$ is the
three-dimensional result from family 078 [S5:143–193].

**A pointwise wave consequence.** The maximal half-wave
$U_*f=\sup_{0<t<1}|Uf(x,t)|$ is bounded on $L^p$ for
$3\le p<\infty$ and $s>1-2/p$, giving almost-everywhere convergence
$Uf(x,t)\to f(x)$ as $t\downarrow0$ for data with $J^s f\in L^p$
[S4:48–57].

## Section skeleton

**Manuscript** [S3], 11 sections under `build/sections/`:
introduction [S4], framework, cylinder, lower-dimensional, canonical
names, interior, cylinder actions, round transfer, round entropy,
physical wave, and Bochner–Riesz [S5:3–8].

The manuscript's root is `build/main.tex`, not `build/paper.tex`.
Neither the manuscript nor the release ships a `verification/`
bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 12 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 079 at line 1963. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 232. |
| S3 | [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/main.tex`](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/main.tex) | 59 | Main file: title and section inputs. |
| S4 | [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/00-introduction.tex) | 352 | The abstract, the critical L3 theorem, the full range, the history, and the two-stage argument. |
| S5 | [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/10-bochner-riesz.tex`](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/10-bochner-riesz.tex) | 193 | The Bochner--Riesz consequences and the spherical restriction and Kakeya maximal estimates. |
| S6 | [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/references.bib`](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/references.bib) | 302 | The manuscript's bibliography. |

## Bibliography

- Bateman, Harry, The conformal transformations of a space of four dimensions and their applications to geometrical optics (1909)
- Beltran, David, Hickman, Jonathan, Sogge, Christopher D., Variable coefficient Wolff-type inequalities and sharp local smoothing estimates for wave equations on manifolds (2020)
- Beltran, David, Hickman, Jonathan, Sogge, Christopher D., Sharp local smoothing estimates for Fourier integral operators (2019)
- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- Bertsekas, Dimitri P., Shreve, Steven E., Mathematical issues in dynamic programming
- Bourgain, Jean, Demeter, Ciprian, The proof of the $\ell^2$ decoupling conjecture (2015)
- Bourgain, Jean, Guth, Larry, Bounds on oscillatory integral operators based on multilinear estimates (2011)
- Gan, Shengwen, He, Danqing, Li, Xiaochun, Wu, Shukun, On local smoothing estimates for wave equations (2026)
- Gao, Chuanwei, Liu, Bochen, Miao, Changxing, Xi, Yakun, Improved local smoothing estimate for the wave equation in higher dimensions (2023)
- Guth, Larry, Wang, Hong, Zhang, Ruixiang, A sharp square function estimate for the cone in $\mathbb R^3$ (2020)
- Guth, Larry, Restriction estimates using polynomial partitioning II (2018)
- Hochman, Michael, Shmerkin, Pablo, Local entropy averages and projections of fractal measures (2012)
- Katz, Nets Hawk, Tao, Terence, Some connections between Falconer's distance set conjecture and sets of Furstenburg type (2001)
- Minicozzi, II, William P., Sogge, Christopher D., Negative results for Nikodym maximal functions and related oscillatory integrals in curved space (1997)
- Miyachi, Akihiko, On some estimates for the wave equation in $L^p$ and $H^p$ (1980)
- Mockenhaupt, Gerd, Seeger, Andreas, Sogge, Christopher D., Wave front sets, local smoothing and Bourgain's circular maximal theorem (1992)
- Mockenhaupt, Gerd, Seeger, Andreas, Sogge, Christopher D., Local smoothing of Fourier integral operators and Carleson–Sjolin estimates (1993)
- OpenAI, Bochner–Riesz multipliers in three dimensions (2026)
- Orponen, Tuomas, Shmerkin, Pablo, On the Hausdorff dimension of Furstenberg sets and orthogonal projections in the plane (2023)
- Ou, Yumeng, Wang, Hong, A cone restriction estimate using polynomial partitioning (2022)
- Peral, Juan C., $L^p$ estimates for the wave equation (1980)
- Ramsey, F. P., On a Problem of Formal Logic (1930)
- Ren, Kevin, Wang, Hong, Furstenberg sets estimate in the plane (2025)
- Rozendaal, Jan, Schippa, Robert, Local smoothing for rough wave equations (2026)
- Garrigós, Gustavo, Seeger, Andreas, On plate decompositions of cone multipliers (2009)
- Shmerkin, Pablo, Wang, Hong, Dimensions of Furstenberg sets and an extension of Bourgain's projection theorem (2025)
- Sogge, Christopher D., Propagation of singularities and maximal functions in the plane (1991)
- Tao, Terence, The Bochner–Riesz conjecture implies the restriction conjecture (1999)
- Wang, Hong, Zahl, Joshua, Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions (2025)
- Wolff, Thomas, Local smoothing type estimates on $L^p$ for large $p$ (2000)
- Wolff, Thomas, Recent work connected with the Kakeya problem (1999)
- Łaba, Izabella, Wolff, Thomas, A local smoothing estimate in higher dimensions (2002)
