[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 352](../index/differential-geometry/352-finite-time-singularity-of-calabi-flow.md)

# 352 — Finite-time singularity of Calabi flow

[Index page](../index/differential-geometry/352-finite-time-singularity-of-calabi-flow.md)

## Headline theorem

The manuscript's main theorem is the counterexample itself [S8:20–28]:

> There is a smooth $U(10)$-invariant Kähler form $\omega_0$ on $\mathbb{CP}^{10}$, in the class $[\omega_{\mathrm{FS}}]$, whose maximal smooth Calabi flow has existence interval $[0,T_*)$ with $0<T_*<\infty$. There are a point $p\in\mathbb{CP}^{10}$ and a constant $a>0$ such that $$S(\omega(t))(p)\sim a(T_*-t)^{-1/2}\qquad\text{as }t\uparrow T_*.$$ [S8:21–27]

The corollary is the dimension statement [S8:40–57]:

> Let $\omega(t)$, $T_*$, $p$, and $a$ be as in Theorem , and let $(Y,\eta)$ be a compact connected Kähler manifold with $\eta$ of constant scalar curvature. With $\pi_X$ and $\pi_Y$ the projections from $\mathbb{CP}^{10}\times Y$, the maximal smooth Calabi flow from $\Omega_0=\pi_X^*\omega_0+\pi_Y^*\eta$ is $$\Omega(t)=\pi_X^*\omega(t)+\pi_Y^*\eta, \qquad 0\leq t<T_*.$$ For every $y\in Y$, $S(\Omega(t))(p,y)\sim a(T_*-t)^{-1/2}$. In particular, finite-time smooth Calabi-flow singularities occur in every complex dimension $n\geq10$, on $\mathbb{CP}^{10}\times\mathbb{CP}^{n-10}$, in a class containing a Kähler–Einstein metric. [S8:41–56]

The manuscript states what the construction does not presuppose: the spectral split that selects finitely many components from future forcing is available because the initial metric is still free, and it requires no stability or nondegeneracy theorem for the profile [S8:168–171].

## Undergraduate summary

The Calabi flow evolves a Kähler metric inside one fixed Kähler class. It is driven by “scalar curvature [S8:11]” — a single number at each point — measured against the average scalar curvature that the class itself determines 

> The Calabi flow is $$\omega(t)=\omega_0+i\partial\bar\partial\phi(t)>0, \qquad \phi(0)=0,\qquad \partial_t\phi=S(\omega(t))-\bar S,$$ where $\bar S$ is the average scalar curvature, determined by the Kähler class. [S8:5–11]

Chen's smooth long-time existence conjecture asserts that this flow exists for all positive times from arbitrary smooth Kähler initial data; the manuscript cites it as Conjecture 1.1 of He and Zeng [S8:13–15].

The manuscript is a counterexample. It builds a smooth `U(10)`-invariant Kähler form on complex projective space `CP^10`, in the Fubini–Study class, whose maximal smooth Calabi flow exists only on `[0, T*)` with `T*` finite, and whose scalar curvature at one point blows up like `a(T* − t)^{−1/2}` [S8:21–27]. The Fubini–Study metric has constant scalar curvature, so the class the counterexample lives in contains a constant-scalar-curvature metric — the conjecture fails even there [S8:30–33].

The corollary widens the dimension. Tensor the flow with any compact Kähler manifold whose metric has constant scalar curvature: the product flow is the product of the two flows, the singularity persists at every point of the product, and finite-time smooth Calabi-flow singularities occur in every complex dimension `n ≥ 10` on `CP^10 × CP^{n−10}`, in a class containing a Kähler–Einstein metric [S8:41–57].

The mechanism is one scalar function. Under a radial ansatz, the momentum coordinate `x ∈ (0,1)` carries the metric, and the whole flow reduces to a function `H` on `[0,1]` satisfying a fourth-order equation [S8:113–121]. At the fixed affine origin `p`, scalar curvature is read off one value: `S(t,p) = 110(1 − H(t,0))` [S8:128–132]. The construction builds a shrinking profile `G` with `G(0) = 1` and `G'(0) < 0`, sets `F(t,x) = ρ^{-1} h(x/ρ)` with `ρ = √(−t)`, and corrects `F` by a term `V` that is smaller than the leading term at the origin, `V(t,0) = O(ρ^{−1+δ})` for some `δ > 0` [S8:133–144]. The correction is what makes the solution live on the compact manifold, and the bound at the origin is what keeps the scalar curvature diverging.

## Graduate summary

The geometric reduction is the momentum formulation of Hwang and Singer, with Abreu's toric scalar-curvature formula inside Guillemin's symplectic-potential framework [S8:109–112]. The reduction proposition turns the Calabi flow into a scalar equation for `H` 

> Let $I$ be an open time interval, and let $H\in C^\infty(I\times[0,1])$ satisfy $$b(t,x):=1+v_*(x)H(t,x)>0.$$ Define $$v=v_*+v_*^2H=v_*b,\qquad K(H)=w^{-1}(wv_*^2H)'',\qquad \mathcal A H=\big[w^{-1}(wv_*^2H)''\big]''.$$ At each time these data, together with an affine choice in the Legendre [S9:34–45]

The operators lemma is the analytic input: the spatial operator is a bijection between smooth invariant functions on an auxiliary sphere and smooth functions on `[0,1]`, so the endpoint conditions become ordinary smooth invariance, and the flat model is the constant-coefficient operator `P0 = (D^2+9D+10)^2` acting on `L^2(R)` [S9:215–232].

The finite-time obstruction lemma is the geometric conclusion 

> Let $G\in C^\infty[0,\infty)$ satisfy $G(0)=1$ and $G'(0)\ne0$, and define $F$ by . Suppose that for some $T>0$ and $\delta>0$ there is a smooth invariant solution $H=F+V$ of on $(-T,0)\times\Sigma$ such that $1+v_*H>0$ and $$V(t,0)=O(\rho^{-1+\delta})\qquad(t\uparrow0).$$ Then a smooth $U(10)$-invariant metric $\omega_0\in[\omega_*]$ has maximal smooth Calabi-flow existence interval $[0,T_*)$, where $T_*=T/2<\infty$. At the fixed affine origin $p$, the scalar curvature of this flow satisfies $$S(\tau,p)=a(T_*-\tau)^{-1/2} +O\big(1+(T_*-\tau)^{(-1+\delta)/2}\big),\qquad a=-110G'(0)\ne0.$$ In particular $S(\tau,p)\sim a(T_*-\tau)^{-1/2}$, and $a>0$ when $G'(0)<0$. [S9:406–424]

The profile theorem builds `G` [S10:15–30]:

> There exist a constant $c>0$ and a function $G\in C^\infty([0,\infty))$ such that $$Q(y\partial_y)(G-1)=\frac{y^2}{2}\left(\frac1G-\frac1c\right), \qquad Q(D)=(D-1)(D+9)(D+10).$$ The function $G$ is bounded above and bounded away from zero, satisfies $G(0)=1$ and $G'(0)<0$, and is analytic near zero. There are real coefficients $g_j$, $j\ge1$, such that, for every $J,\ell\ge0$, $$\frac{\mathrm{d}^\ell}{\mathrm{d} y^\ell} \left(G(y)-c-\sum_{j=1}^{J}g_jy^{-2j}\right) =O\bigl(y^{-2(J+1)-\ell}\bigr)\qquad(y\longrightarrow\infty).$$ [S10:15–28]

The profile also yields the flat solution directly 

> Set $h(y)=(G(y)-1)/y$, with its smooth value at zero. For $t<0$, the function $$F(t,x)=\rho^{-1}h(x/\rho),\qquad \rho=\sqrt{-t},$$ solves $$F_t+(1+xF)^2\widehat{\mathcal A}F=0, \qquad \widehat{\mathcal A}=(x\partial_x^2+12\partial_x)^2.$$ [S10:32–41]

The profile is fixed by three numbers: `k_0 = 1/2`, `c_0 = 110/109`, `z_0 = (k_0, c_0)`, and the origin lemma gives a unique analytic germ `p(s)` with `p(0) = 0`, `p'(0) = k_0`, `c(0) = c_0`, and `p''(0) = c_0/2` [S10:92–122]. The certificate certifies that this germ extends to `s ≤ 56` and lands close to the target parameters.

The parabolic layer supplies the norms. Weighted Hölder spaces `X` and `Y` are built from a weight `p`, a parabolic exponent `α`, and the four spatial derivatives, with `|∂_t u| ≤ C [u]_{α;Q}` giving the full parabolic seminorm [S11:54–70]. The Schauder lemma upgrades a supremum bound to the full spatially weighted parabolic Hölder bound using a scale-invariant `L^2` bound integrable up to the singular time [S11:176–190], the `L^2` lemma is that integrable bound [S11:350–364], and the short-time lemma solves the linearized equation forward from a smooth source with the weight `p = −2 + 2δ` [S11:411–425].

The ancient flat right inverse is the core analytic object 

> There is a number $\delta\in(0,1)$ such that, for every fixed $\alpha\in(0,1)$, the operator has a bounded real linear right inverse $$\widehat D:Y\longrightarrow X,\qquad \widehat{\mathcal P}\widehat D f=f,\qquad \|\widehat D f\|_X\le C\|f\|_Y, \qquad p_0=-2+2\delta.$$ Here $Y$ has weight $p_0-4$ and parabolic exponent $\alpha$, and $X$ has weight $p_0$ and includes the parabolic $\alpha$ norms of all spatial derivatives through order four and of the first time [S12:24–35]

The compact realization theorem glues the ancient inverse to a short-time forward solution 

> Let $G$ be the profile of Theorem , put $$h(y)=\frac{G(y)-1}{y},\qquad F(t,x)=\rho^{-1}h(x/\rho),$$ and fix $0<\alpha<\alpha'<1$. Choose $\delta\in(0,1)$ and the ancient right inverse supplied by Theorem . For every sufficiently small $\varepsilon>0$, there are $T>0$ and a real invariant function $V\in X_\alpha$ on $\Sigma\times[-T,0)$ such that $\lVert V\rVert_{X'_\alpha}\le\varepsilon$ and $H=F+V$ satisfies $$H_t+(1+v_*H)^2\mathcal A H=0,\qquad v_*=x(1-x).$$ The function $H$ is smooth on $\Sigma\times(-T,0)$, and there are constants $0<c_1<c_2<\infty$, independent of $t$, such that $$c_1\le 1+v_*H\le c_2.$$ In particular, $H(t,\cdot)$ is smooth as a function of $x\in[0,1]$, and $$V(t,0)=O(\rho^{-1+\delta})\qquad(t\uparrow0).$$ [S13:22–43]

The nonlinear step is where the norm choice matters: the linearized operator is `P = P0 + E`, `E` is lower order with `E u = O(ρ^{-2} u)`, and the residual becomes small after applying the inverse in a norm controlling all four spatial derivatives and their temporal Hölder seminorms, with the time derivative omitted [S13:523–545]. The product corollary is proved by the identity `S(Ω(t)) = S(ω(t)) ∘ π_X + S(η)` and the fact that the product metric is a solution exactly when each factor is [S13:641–660].

The appendix is the finite-arithmetic certificate. The shooting proposition bounds the profile parameters [S14:12–25]:

> For every parameter $z_*\in[-R,R]^2$, where $R=5\cdot10^{-10}$, let $(k,d)$ be given by , and let $p$ be the origin solution of supplied by Lemma . This solution extends to $0\le s\le S_0=56$ and satisfies $$1+p(s)>0.$$ For the coordinates of its jet relative to $p_{\rm a}$, defined in , one has $$|q|\le .25R,\qquad \big\|(\Re\xi,\Im\xi)-z_*\big\|_\infty\le .13R.$$ [S14:12–24]

The method is interval arithmetic: the vector field is decomposed into a linear part `L` and a polynomial part `N`; `L` is applied by exact rational arithmetic, `N` by integer interval arithmetic, and the enclosure uses the scalar majorant `exp(Lt)`. The certificate is a finite computation over integer intervals, and the analytic interpretation is proved in the appendix [S14:27–55].

The provenance statement is explicit 

> The complete source printed in Appendix is \textttverification/certificate.py, comprising $6594$ UTF-8 bytes. Its SHA-256 digest is \begincenter\small\ttfamily 263389fd7217d84d0e5b66869797fc9f7998\\ 309d524a95f7ad7d3d0f538ea742 \endcenter where the line break is for typesetting only. It uses no imported libraries, floating-point operations, external data, or platform-dependent numerical routines. From the paper directory, the verification command is \beginquote\ttfamily python3 verification/certificate.py \endquote [S14:671–684]

## History of the conjecture

Calabi introduced the flow in 1982 to seek canonical metrics within a Kähler class [S8:12–13] [S16:1–11]. The surface theory is Chruściel 1991, Chen 2001, and Struwe 2002 [S8:62–66] [S16:152–171]. The higher-dimensional short-time theory is Chen–He 2008 and He–Zeng 2021, and the manuscript cites Chen's smooth long-time existence conjecture through He and Zeng's Conjecture 1.1 [S8:13–15] [S8:67–72] [S16:22–41]. Chen and Cheng's 2021 a priori estimates paper is where the manuscript locates the global-existence question for classes containing a constant-scalar-curvature metric, citing page 912 following their Conjecture 1.3 [S8:30–33] [S16:172–181]. The extension criteria the counterexample must evade are Chen–He 2008, Chen–Cheng 2021, Li–Zhang–Zheng 2024, and Li–Zhang 2025 [S8:74–82] [S16:22–41] [S16:72–83]. The weak-flow line is Streets 2014 and Berman–Darvas–Lu 2017 [S8:92–102] [S16:62–71] [S16:194–202]. The momentum and toric machinery is Calabi 1979, Hwang–Singer 2002, Guillemin 1994, and Abreu 1998 [S8:109–112] [S16:112–151]. The validated-integration framework the certificate uses is surveyed in Nedialkov–Jackson–Corliss 1999 [S8:154–157] [S16:183–192].

## Consequences

Chen's smooth long-time existence conjecture is false. The manuscript builds smooth initial data in a fixed Kähler class whose maximal smooth Calabi flow stops at a finite time with scalar curvature diverging like `(T* − t)^{−1/2}` at a point [S8:21–27]. Because the class is the Fubini–Study class, the failure happens in a class containing a constant-scalar-curvature metric, so no assertion of smooth global existence and subsequent smooth convergence modulo holomorphic automorphisms can hold for arbitrary smooth initial metrics in such a class — the obstruction occurs at a finite time [S8:30–37].

The product corollary removes the dimension restriction from above: finite-time smooth Calabi-flow singularities occur in every complex dimension `n ≥ 10`, on `CP^10 × CP^{n−10}`, in a class containing a Kähler–Einstein metric [S8:41–57]. The scalar-curvature rate is the quantitative content, and the finite-time obstruction lemma is what converts the analytic bound `V(t,0) = O(ρ^{−1+δ})` into it, with `a = −110G'(0) ≠ 0` [S9:406–425].

The result also fixes the boundary with the weak theory. Weak Calabi flows exist globally and converge in `d_1` when the class contains a constant-scalar-curvature metric, and the weak and classical flows agree for as long as the classical flow exists smoothly; the manuscript states that neither fact implies smooth continuation through every finite time [S8:92–102]. So the global weak trajectory does not extend this singularity smoothly.

Inside the release, the family is at tier T0 with no formalized manuscript, no scope note, no comparator, no `main_results` entry, and no reasoning trace [S3:348]. The manuscript is 3,859 lines of section text. The one verification bundle certifies the profile-matching inequalities by exact rational arithmetic; it does not formalize the geometric reduction, the parabolic estimates, the ancient inverse, or the compact gluing, and nothing in `lean/` names the manuscript.

## Coverage

The release records 1 manuscript for this family and 0 formalized paths, 0 comparator challenges, 0 `main_results` entries, 0 scope notes, 1 verification bundle, 0 inputs, and no reasoning trace [S3:348]. The overview entry is the family's only release-level statement [S2:802]. The manuscript abstract is the release's own claim [S1:8576]. The verification bundle's run command is named by the README's `## Verification` section [S4:19]. The bundle's three programs were read as documents, not executed, so no run output is recorded here.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb, manuscript link, manuscript abstract |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 352's `\resultentry`, at line 802 |
| S3 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Reading ledger row for family 352 |
| S4 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/README.md`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/README.md) | 44 | Manuscript README: date, bibtex title, `## Verification` run command |
| S5 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/paper.pdf`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/paper.pdf) | 21383 | Manuscript PDF |
| S6 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/main.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/main.tex) | 41 | Abstract, section order, appendix, bibliography inclusion |
| S7 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/preamble.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/preamble.tex) | 57 | Theorem environments and macro definitions |
| S8 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/introduction.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/introduction.tex) | 188 | Main theorem, product corollary, background, structure of the construction |
| S9 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/geometry.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/geometry.tex) | 499 | The geometric reduction, the operators lemma, the finite-time obstruction lemma |
| S10 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/profile.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/profile.tex) | 684 | The shrinking profile theorem, the parameters, the origin lemma |
| S11 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/parabolic.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/parabolic.tex) | 536 | Weighted Hölder spaces, the Schauder lemma, the `L^2` lemma, the short-time lemma |
| S12 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/flat.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/flat.tex) | 585 | The ancient flat right inverse theorem |
| S13 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/compact.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/compact.tex) | 666 | The compact realization theorem, the nonlinear correction, the product corollary proof |
| S14 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/certificate.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/sections/certificate.tex) | 701 | The shooting proposition, the interval method, the provenance statement |
| S15 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/figures/cutoff-support.tex`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/figures/cutoff-support.tex) | 28 | The cutoff-support figure |
| S16 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/references.bib`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/build/references.bib) | 202 | 21 bibliography entries |
| S17 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/certificate.py`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/certificate.py) | 158 | The interval-arithmetic certificate program |
| S18 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/arithmetic_allowances.py`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/arithmetic_allowances.py) | 95 | Independent exact-rational checks of the analytic allowances |
| S19 | [`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/tail-check.py`](../../../preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/verification/tail-check.py) | 180 | Supplementary exact rational checks for the half-line profile |

## Bibliography

- Abreu, Miguel, Kähler geometry of toric varieties and extremal metrics (1998)
- Berman, Robert J., Darvas, Tamás, Lu, Chinh H., Convexity of the extended $K$-energy and the large time behavior of the weak Calabi flow (2017)
- Calabi, Eugenio, Extremal Kähler metrics (1982)
- Calabi, Eugenio, Métriques kählériennes et fibrés holomorphes (1979)
- Chen, Xiuxiong, Calabi flow in Riemann surfaces revisited: a new point of view (2001)
- Chen, Xiuxiong, He, Weiyong, On the Calabi flow (2008)
- Chen, Xiuxiong, Cheng, Jingrui, On the constant scalar curvature Kähler metrics (I)—A priori estimates (2021)
- Chruściel, Piotr T., Semi-global existence and convergence of solutions of the Robinson–Trautman (2-dimensional Calabi) equation (1991)
- Dong, Hongjie, Zhang, Hong, Schauder estimates for higher-order parabolic systems with time irregular coefficients (2015)
- Guan, Daniel, Extremal solitons and exponential $C^\infty$ convergence of the modified Calabi flow on certain $\mathbb{CP}^1$ bundles (2007)
- Guillemin, Victor, Kaehler structures on toric varieties (1994)
- He, Weiyong, Zeng, Yu, The Calabi flow with rough initial data (2021)
- Huang, Hong, The Cauchy problem for fully nonlinear parabolic systems on manifolds (2026)
- Hwang, Andrew D., Singer, Michael A., A momentum construction for circle-invariant Kähler metrics (2002)
- Kato, Tosio, Perturbation Theory for Linear Operators (1995)
- Li, Haozhao, Zhang, Linwei, Zheng, Kai, Calabi flow with bounded $L^p$ scalar curvature (2024)
- Li, Haozhao, Zhang, Linwei, Calabi flow with bounded $L^p$ scalar curvature (II) (2025)
- Nedialkov, N. S., Jackson, K. R., Corliss, G. F., Validated solutions of initial value problems for ordinary differential equations (1999)
- Hörmander, Lars, Hypoelliptic differential operators (1961)
- Streets, Jeffrey, Long time existence of minimizing movement solutions of Calabi flow (2014)
- Struwe, Michael, Curvature flows on surfaces (2002)
