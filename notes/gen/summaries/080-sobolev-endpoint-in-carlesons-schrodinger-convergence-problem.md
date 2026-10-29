[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 080](../index/real-and-complex-analysis/080-sobolev-endpoint-in-carlesons-schrodinger-convergence-problem.md)

# 080 — The Sobolev endpoint in Carleson's Schrödinger convergence problem

[Index page](../index/real-and-complex-analysis/080-sobolev-endpoint-in-carlesons-schrodinger-convergence-problem.md)

## Original CONTENTS.md summary

The release's blurb [S1:1979] and the catalog abstract [S2:234] state
the family's claim: it attains the sharp Sobolev equality case of
Carleson's Schrödinger convergence problem, in every dimension
$`n\ge2`$ — almost-everywhere convergence of the free evolution
$`e^{it\Delta}f`$ to $`f`$ as $`t\downarrow0`$ for every
$`f\in H^{n/[2(n+1)]}(\mathbb R^n)`$, including the planar endpoint
$`H^{1/3}`$. The family ships two manuscripts, a planar companion and a
higher-dimensional one, which share the Gaussian-limit-first
representative. The planar manuscript's abstract "We resolve the planar Sobolev endpoint of Carleson's convergence problem:
for initial data in $`H^{1/3}(\mathbb R^2)`$, the Schrödinger evolution converges
almost everywhere to the initial data as $`t\downarrow0`$. The evolution is
defined by taking the Gaussian regularization limit first; on one full-measure
spatial set, this limit exists for every $`0<t<1`$, and the resulting evolution
is continuous at $`t=0`$. [S3:39–44]"

## Undergraduate summary

The Schrödinger evolution $`e^{it\Delta}f`$ disperses initial data. The
pointwise convergence problem asks which Sobolev regularity $`H^s`$ is
enough for $`e^{it\Delta}f(x,t)\to f(x)`$ as $`t\downarrow0`$ for almost
every $`x`$. Carleson solved the one-dimensional case at $`s=1/4`$, and
each dimension has its own sharp threshold: in the plane that is
$`s=1/3`$, and in dimension $`n`$ it is $`s=n/[2(n+1)]`$.

The manuscripts prove the threshold exactly, not just a strict
inequality above it — the equality case is the hard endpoint. The
planar statement [S4:23–35] takes the Gaussian regularized evolution
$`U_af`$ for $`a>0`$, passes to the limit $`a\downarrow0`$ first on a
full-measure set $`E_f`$, and shows the resulting evolution is
continuous at $`t=0`$:

> **Theorem 1.1**
For every $`f\in H^{1/3}(\mathbb R^2)`$ there is a set $`E_f\subset\mathbb R^2`$ of full
Lebesgue measure such that, for each $`x\in E_f`$, the finite limit
$$u_f(x,t)=\lim_{a\downarrow0}U_af(x,t)$$
exists for every real $`0<t<1`$, and
$$\lim_{t\downarrow0}u_f(x,t)=f^*(x).$$
In fact $`u_f(x,\cdot)`$ extends continuously to $`[0,1)`$ with value $`f^*(x)`$
at zero, and the Gaussian limit is uniform over $`0<t<1`$. [S4:23–35]

The higher-dimensional companion [S6:34–49] makes the same
Gaussian-limit-first assertion for each fixed $`n\ge3`$:

> **theorem**
For every fixed integer $`n\geq3`$ and every complex-valued
$`f\in H^{s_n}(\mathbb R^n)`$, there is a full-measure set $`E_f`$ of Lebesgue
points of $`f`$ and a function $`v(x,t)`$, $`x\in E_f`$, $`0\leq t<1`$, such
that $`v(x,\cdot)`$ is continuous, $`v(x,0)=f^*(x)`$, and
$$\lim_{a\downarrow0}\sup_{0<t<1}|U_af(x,t)-v(x,t)|=0
 \qquad(x\in E_f).$$
In particular the finite Gaussian limit
$$u_f(x,t)=\lim_{a\downarrow0}U_af(x,t)$$
exists for every real $`0<t<1`$ on this one set, and
$`\lim_{t\downarrow0}u_f(x,t)=f^*(x)`$. [S6:34–49]

Both emphasize that the exceptional set is spatial, fixed once for all
times $`0<t<1`$ — the representative is not built by intersecting
time-dependent exceptional sets.

## Graduate summary

**Why the endpoint is hard.** The strict range above the threshold is
known by several routes, but an endpoint estimate cannot come from a
frequency argument that carries any growing loss: an arbitrarily small
uncompensated frequency loss does not prove the equality case [S6:87–95].
The planar manuscript makes the same point — its maximal estimate has
local $`L^1`$ output, and it does not assert the stronger endpoint local
$`L^3`$ maximal estimate [S4:71–75].

**Planar proof: three ingredients.** The main analytic conclusion is a
local maximal estimate at the exact Sobolev exponent, $`\int_{B(x_0,1)}
\sup_{0\le t<1}|S(t)f(x)|\,dx \le C\|f\|_{H^{1/3}}`$, uniform in center
and frequency bound [S4:78–93]. Three components produce it. First, a
transverse power saving: multilinear restriction and Du–Zhang's
refined fractal restriction reduce a saturated transverse configuration
to point–tube incidences, and a robust projection theorem forces the
additive profiles to be flat, closing the saving [S4:94–109]. Second, a
bilinear frame estimate for smooth packet arrays, uniform in the number
of scales [S4:111–119]. Third, square summation at the endpoint: a
short-time weak estimate with fixed $`p>2`$ and no growing loss is
combined by a binary time tree whose convexity deficit sums the
lighter-child masses across frequency scales [S4:121–134].

**Higher-dimensional proof: three principal steps.** The frame estimate
counts unit cubes where $`k+1`$ transverse packet fields are large
relative to their square envelopes [S6:127–143]. A geometric induction
in full dimension reduces a large level set to a polynomial wall via
codimension-two angular narrowing and a quadratic-sublevel narrow
estimate, and flattening along affine plates makes the frame estimate
applicable in dimension $`n-1`$ [S6:145–157]. A common time tree then
gives frequency square summation and the local $`H^{s_n}`$ bound, and
uniform-in-time approximation produces a common representative without
an uncountable intersection of exceptional sets [S6:159–186].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

Carleson introduced the pointwise convergence problem and proved the
one-dimensional result at $`s=1/4`$; Dahlberg and Kenig showed the
threshold is necessary. Sjölín and Vega independently obtained
convergence for $`s>1/2`$ in higher dimensions, and in the plane
Bourgain and Moyua–Vargas–Vega connected the problem to Fourier
restriction. The bilinear approach of Tao and Vargas gave $`s>15/32`$;
Tao's sharp bilinear restriction theorem improved this to $`s>2/5`$, and
Lee obtained $`s>3/8`$ [S4:37–55]. In dimensions $`n\ge3`$ Bourgain
obtained the sufficient range $`s>1/2-1/(4n)`$.

Bourgain's later counterexample forces $`s\ge n/[2(n+1)]`$ when
$`n\ge2`$ but does not rule out equality. Du, Guth and Li proved planar
convergence and a local $`L^3`$ maximal estimate for $`s>1/3`$; Du, Guth,
Li and Zhang obtained higher-dimensional convergence for
$`s>(n+1)/[2(n+2)]`$; and Du and Zhang established
$`s>n/[2(n+1)]`$ in higher dimensions [S4:56–74]. A recent
Bessel-potential extension still states its $`p=2`$ range with the strict
inequality [S6:74–86]. The choice of pointwise representative is itself
part of the history: Sjögren and Sjölín constructed, for $`s>1/2`$,
representatives continuous on the entire time line for almost every
spatial point.

## Consequences

**The sharp endpoint across all dimensions.** Taken together the two
manuscripts establish the equality case of Carleson's Schrödinger
convergence problem in every dimension $`n\ge2`$: the planar $`H^{1/3}`$
case and the higher-dimensional $`H^{n/[2(n+1)]}`$ case [S2:234].

**The planar companion feeds the higher-dimensional proof.** The
higher-dimensional manuscript uses the planar companion's lemmas
directly — its limiting-information calculus, block-comparison and
telescoping-cost lemmas, and its time-tree mechanism — while noting its
planar conclusion is not invoked as a higher-dimensional result
[S6:87–105].

**A stronger maximal estimate is not claimed.** Both manuscripts
deliberately stop at local $`L^1`$-output maximal bounds with the exact
endpoint exponent; the stronger endpoint local $`L^3`$ maximal estimate
is not asserted [S4:71–75].

## Section skeleton

**Planar manuscript** [S3:39–44], 9 sections under `build/sections/`:
introduction [S4:23–35], preliminaries, transverse, sparse, frame, flat,
geometry, dyadic, and endpoint. Its reference list is a
`thebibliography` block [S7], not a `.bib` file.

**Higher-dimensional manuscript** [S5:9–14], 8 input sections under
`build/sections/`: introduction [S6:34–49], packets, frame, fractal,
transverse, sparse, weak, and endpoint, with a `references.bib`
bibliography [S8]. Its root is `build/paper.tex`; the planar root is
`build/main.tex`.

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts — 14 `.tex` files under the planar `build/` and 16 under
the higher-dimensional `build/` — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 080 at line 1979. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 234. |
| S3 | [`preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/main.tex`](../../../preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/main.tex) | 60 | Planar main file: title and abstract. |
| S4 | [`preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/sections/01-introduction.tex) | 148 | Planar main theorem, history, and the three ingredients of the proof. |
| S5 | [`preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/paper.tex`](../../../preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/paper.tex) | 30 | Higher-dimensional main file: title and abstract. |
| S6 | [`preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/sections/introduction.tex`](../../../preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/sections/introduction.tex) | 187 | Higher-dimensional main theorem, history, and the three principal steps. |
| S7 | [`preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/bibliography.tex`](../../../preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/bibliography.tex) | 190 | The planar manuscript's bibliography (a thebibliography block). |
| S8 | [`preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/references.bib`](../../../preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/references.bib) | 401 | The higher-dimensional manuscript's bibliography. |

## Bibliography

- Basu, Saugata, Algorithms in real algebraic geometry: a survey (2014)
- J. Bennett, A. Carbery, and T. Tao, _On the multilinear restriction and Kakeya conjectures_, Acta Math. **196** (2006), no. 2, 261–302. doi:10.1007/s11511-006-0006-4. arXiv:math/0509262v1.
- Bennett, Jonathan, Carbery, Anthony, Tao, Terence, On the multilinear restriction and Kakeya conjectures (2006)
- J. Bourgain, _Some new estimates on oscillatory integrals_, in _Essays on Fourier Analysis in Honor of Elias M. Stein_ (C. Fefferman, R. Fefferman, and S. Wainger, eds.), Princeton Math. Ser., vol. 42, Princeton Univ. Press, 1995, pp. 83–112. Author preprint.
- J. Bourgain, _On the Schrödinger maximal function in higher dimension_, Proc. Steklov Inst. Math. **280** (2013), 46–60. doi:10.1134/S0081543813010045. arXiv:1201.3342.
- J. Bourgain, _A note on the Schrödinger maximal function_, J. Anal. Math. **130** (2016), 393–396. doi:10.1007/s11854-016-0042-8. arXiv:1609.05744.
- Bourgain, Jean, A note on the {Schrödinger} maximal function (2016)
- Bourgain, Jean, Demeter, Ciprian, The proof of the $`l^2`$ Decoupling Conjecture (2015)
- Bourgain, Jean, The discretized sum-product and projection theorems (2010)
- Bourgain, Jean, Guth, Larry, Bounds on oscillatory integral operators based on multilinear estimates (2011)
- Bourgain, Jean, Some new estimates on oscillatory integrals (1995)
- Bourgain, Jean, On the {Schrödinger} maximal function in higher dimension (2013)
- L. Carleson, _Some analytic problems related to statistical mechanics_, in _Euclidean Harmonic Analysis_ (J. J. Benedetto, ed.), Lecture Notes in Math., vol. 779, Springer, Berlin, 1980, pp. 5–45. doi:10.1007/BFb0087666.
- Carleson, Lennart, Some analytic problems related to statistical mechanics (1980)
- Chu, Rena, Counterexamples for generalizations of the non-elliptic {Schrödinger} maximal operator (2026)
- Dahlberg, Björn E. J., Kenig, Carlos E., A note on the almost everywhere behavior of solutions to the {Schrödinger} equation (1982)
- J. Bourgain and C. Demeter, _The proof of the $`l^2`$ Decoupling Conjecture_, Ann. of Math. (2) **182** (2015), no. 1, 351–389. doi:10.4007/annals.2015.182.1.9. arXiv:1403.5335v3.
- Y. Deng, C. Fan, S. Guo, Z. Guo, and Y. Luo, _Sharp Strichartz estimates on the one-dimensional torus_, arXiv:2609.18670v1 (2026). arXiv:2609.18670v1.
- X. Du, L. Guth, and X. Li, _A sharp Schrödinger maximal estimate in $`\mathbb R^2`$_, Ann. of Math. (2) **186** (2017), no. 2, 607–640. doi:10.4007/annals.2017.186.2.5.
- X. Du, L. Guth, X. Li, and R. Zhang, _Pointwise convergence of Schrödinger solutions and multilinear refined Strichartz estimates_, Forum Math. Sigma **6** (2018), e14, 18 pp. doi:10.1017/fms.2018.11. arXiv:1803.01720v2.
- Du, Xiumin, Guth, Larry, Li, Xiaochun, A sharp {Schrödinger} maximal estimate in $`\mathbb{R}^2`$ (2017)
- Du, Xiumin, Zhang, Ruixiang, Sharp $`L^2`$ estimates of the {Schrödinger} maximal function in higher dimensions (2019)
- Du, Xiumin, Iosevich, Alex, Ou, Yumeng, Wang, Hong, Zhang, Ruixiang, An improved result for Falconer's distance set problem in even dimensions (2021)
- Du, Xiumin, Guth, Larry, Li, Xiaochun, Zhang, Ruixiang, Pointwise convergence of {Schrödinger} solutions and multilinear refined Strichartz estimates (2018)
- Du, Xiumin, Li, Jianhui, $`L^p`$ estimates of the maximal {Schrödinger} operator in $`\mathbb R^n`$ (2025)
- Sjögren, Peter, Sjölin, Per, Convergence properties for the time-dependent {Schrödinger} equation (1989)
- S. Guo, Z. K. Li, and P.-L. Yung, _Improved discrete restriction for the parabola_, Math. Res. Lett. **30** (2023), no. 5, 1375–1409. arXiv:2103.09795v2.
- J. Bourgain and L. Guth, _Bounds on oscillatory integral operators based on multilinear estimates_, Geom. Funct. Anal. **21** (2011), no. 6, 1239–1295. doi:10.1007/s00039-011-0140-9. arXiv:1012.3760.
- L. Guth, D. Maldague, and H. Wang, _Improved decoupling for the parabola_, J. Eur. Math. Soc. (JEMS) **26** (2024), no. 3, 875–917. doi:10.4171/JEMS/1295. arXiv:2009.07953.
- Guth, Larry, Iosevich, Alex, Ou, Yumeng, Wang, Hong, On Falconer's distance set problem in the plane (2020)
- Guth, Larry, The endpoint case of the Bennett–Carbery–Tao multilinear Kakeya conjecture (2010)
- Guth, Larry, Katz, Nets Hawk, On the {Erdős} distinct distances problem in the plane (2015)
- Guth, Larry, A restriction estimate using polynomial partitioning (2016)
- Guth, Larry, Katz, Nets Hawk, Algebraic methods in discrete analogs of the Kakeya problem (2010)
- W. He, _Orthogonal projections of discretized sets_, J. Fractal Geom. **7** (2020), no. 3, 271–317. doi:10.4171/JFG/92. arXiv:1710.00795v2.
- He, Weikun, Orthogonal projections of discretized sets (2020)
- L. Guth and N. H. Katz, _On the Erdős distinct distances problem in the plane_, Ann. of Math. (2) **181** (2015), no. 1, 155–190. doi:10.4007/annals.2015.181.1.2. arXiv:1011.4105v3.
- B. E. J. Dahlberg and C. E. Kenig, _A note on the almost everywhere behavior of solutions to the Schrödinger equation_, in _Harmonic Analysis_ (F. Ricci and G. Weiss, eds.), Lecture Notes in Math., vol. 908, Springer, Berlin, 1982, pp. 205–209. doi:10.1007/BFb0093289.
- M. Christ and A. Kiselev, _Maximal functions associated to filtrations_, J. Funct. Anal. **179** (2001), no. 2, 409–425. doi:10.1006/jfan.2000.3687.
- S. Lee, _On pointwise convergence of the solutions to Schrödinger equations in $`\mathbb R^2`$_, Int. Math. Res. Not. (2006), Art. ID 32597, 21 pp. doi:10.1155/IMRN/2006/32597.
- Lee, Sanghyuk, On pointwise convergence of the solutions to {Schrödinger} equations in $`\mathbb R^2`$ (2006)
- Sjölin, Per, Regularity of solutions to the {Schrödinger} equation (1987)
- A. Moyua, A. Vargas, and L. Vega, _Schrödinger maximal function and restriction properties of the Fourier transform_, Int. Math. Res. Not. **1996** (1996), no. 16, 793–815. doi:10.1155/S1073792896000499.
- Moyua, A., Vargas, Ana, Vega, Luis, {Schrödinger} maximal function and restriction properties of the Fourier transform (1996)
- OpenAI, Endpoint convergence for the planar Schrödinger equation (2026)
- Y. Pan, W. Sun, and J. Tan, _Pointwise convergence of Schrödinger operators in Bessel potential spaces_, arXiv:2605.25833v2 (2026). arXiv:2605.25833v2.
- Pan, Yucheng, Sun, Wenchang, Tan, Jiheng, Pointwise convergence of {Schrödinger} operators in Bessel potential spaces (2026)
- Singh, Shalender, Singh Parmar, Vishnu Priya, Repairing the refined-decoupling proof of the 5/4 planar pinned Falconer theorem (2026)
- P. Sjögren and P. Sjölin, _Convergence properties for the time-dependent Schrödinger equation_, Ann. Acad. Sci. Fenn. Ser. A I Math. **14** (1989), 13–25. Journal PDF.
- P. Sjölin, _Regularity of solutions to the Schrödinger equation_, Duke Math. J. **55** (1987), no. 3, 699–715. doi:10.1215/S0012-7094-87-05535-9.
- T. Tao, _A sharp bilinear restriction estimate for paraboloids_, Geom. Funct. Anal. **13** (2003), no. 6, 1359–1384. doi:10.1007/s00039-003-0449-0. arXiv:math/0210084.
- Tao, Terence, Sharp bounds for multilinear curved Kakeya, restriction and oscillatory integral estimates away from the endpoint (2020)
- Tao, Terence, Vargas, Ana, A bilinear approach to cone multipliers. II. Applications (2000)
- Tao, Terence, A sharp bilinear restriction estimate for paraboloids (2003)
- T. Tao and A. Vargas, _A bilinear approach to cone multipliers. II. Applications_, Geom. Funct. Anal. **10** (2000), no. 1, 216–258. doi:10.1007/s000390050007.
- L. Vega, _Schrödinger equations: pointwise convergence to the initial data_, Proc. Amer. Math. Soc. **102** (1988), no. 4, 874–878. doi:10.1090/S0002-9939-1988-0934859-0.
- Vega, Luis, {Schrödinger} equations: pointwise convergence to the initial data (1988)
- R. Wongkew, _Volumes of tubular neighbourhoods of real algebraic varieties_, Pacific J. Math. **159** (1993), no. 1, 177–184. doi:10.2140/pjm.1993.159.177.
- Wongkew, Richard Alexander, Volumes of tubular neighbourhoods of real algebraic varieties (1993)
- Z. K. Li and P.-L. Yung, _An improved high-low method for the parabola_, arXiv:2609.33949v1 (2026).
- X. Du and R. Zhang, _Sharp $`L^2`$ estimates of the Schrödinger maximal function in higher dimensions_, Ann. of Math. (2) **189** (2019), no. 3, 837–861. doi:10.4007/annals.2019.189.3.4. arXiv:1805.02775v3.
