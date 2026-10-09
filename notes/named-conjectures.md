# Named-conjecture families: statement-level check

The 43 second-pass T0 families whose titles name a conjecture, problem, or question, each read
against the theorem its manuscript actually states. Follow-up 2 in the priority list at the end of
`notes/t0-triage.md`; tracked as bead `math-0h2`. The record it follows states these are claims,
not checked facts: no conjecture had been identified in the literature and no formalized statement
had been compared with the claim. This page does the statement comparison. It does not identify any
conjecture in the literature, and it does not compare against a formalized statement — see
"Not checked".

## Population

Derived from `notes/catalog.tsv` and `notes/scripts/triage_t0.py`, not copied:

- T0 rows: 130 families, 244 manuscripts.
- First pass (read in `notes/t0-triage.md`): bucket C ∪ `fam <= '031'` ∪ `paps >= 3` = 43 families,
  130 manuscripts.
- Second pass (remaining): 87 families, 114 manuscripts.
- Title-named: `re.search(r"conjectur|\bquestion|\bproblem", title)` over the second pass,
  case-insensitive — 43 families, 50 manuscripts. Case-sensitive gives the same 43.
- Manuscripts per family: 36 families with 1, 7 families with 2 (055, 080, 147, 203, 258, 300, 368).
- Buckets over the 43: R 24, N 8, B 5, U 4, K 2.

The population is keyed to the ledger's `tier` column, so it moves when upstream formalizes a family.
**075** and **195** were read in this pass as second-pass T0 families; the 2026-10-07 upstream merge
gave each a `main_results` entry, a scope note and a comparator challenge, which retiered both to T3,
so the rule above no longer includes them. Their reading records are kept, verbatim, under "Promoted
out of the population" — the statement comparison was done against the manuscript, and a retiering
does not undo it. The counts above exclude both; the entry counts below include them.

The bead's priority set is "the sharp-bound claims 038, 078, 079, 101, 202, 344, 346, 375". Seven of
those eight are in the 43. **346 is not**: its title is "Sharp singular-set bounds for stationary
integral varifolds", which contains no `conjectur`/`question`/`problem` token, so the title rule
excludes it. It is read here as a ninth entry because the bead names it. Entries in this page: 44
population entries plus 2 promoted.

## Conventions

- A statement is quoted from the manuscript's own LaTeX, from **every** `.tex` under the manuscript
  directory. Statements are not in the resolved main file: they sit in `build/sections/*.tex`
  (family 101 in `build/manuscript/*.tex`), pulled in by `\input{}`.
- An anchor is `[`path:line-line`]` covering one statement environment, from its `\begin{…}` line to
  its `\end{…}` line. The quotation is that line span verbatim, with runs of whitespace collapsed to
  single spaces and each line stripped. Formatting is not normalized — the LaTeX is quoted as it
  ships.
- A prose citation is `` `path:line-line` `` inside the reading text. It carries no quotation and is
  checked the same way: the path resolves (repo-relative, or against a manuscript directory named
  earlier in the same entry, or against the entry's own anchor when the path is omitted), the range
  sits inside the file, and if its first line opens a statement environment the range ends on that
  environment's `\end{…}`.
- Verdict vocabulary, one per family:
  - `match` — the manuscript's stated theorem is the blurb's claim.
  - `merge` — the blurb merges claims from more than one manuscript, and each clause is carried by a
    manuscript.
  - `narrower` — the blurb states less than the manuscript proves.
  - `wider` — the blurb states more than the manuscript proves.
- The blurb is the `overview.tex` paraphrase, not the manuscript abstract: 0 of 719 manuscript
  comparisons read identical (`notes/abstracts.md`), so a verdict compares the blurb's *claim* with
  the manuscript's *theorem*, not their wording.

## The bead's priority set (sharp-bound claims)

An off-by-one in an exponent is the whole result for these, so each exponent was checked against the
manuscript and, where the claim is a formula, recomputed. **No off-by-one was found in any of the
eight.**

### 038 - Fujita's freeness conjecture

- **Bucket**: B | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves Fujita's freeness conjecture at its sharp bound in every dimension: for a smooth
  projective complex variety $X$ of dimension $n$ and an ample line bundle $L$, the adjoint
  $K_X+mL$ is globally generated for every integer $m\ge n+1$.
- **Statement**: [`preprints/Fujitas-freeness-conjecture-September-23-2026/build/main.tex:70-77`]
  "\begin{theorem}\label{thm:main} Let $X$ be a smooth connected projective variety over $\C$ of
  dimension $n\geq 1$, and let $L$ be an ample line bundle on $X$. Then \[ K_X+(n+1)L \] is generated
  by its global sections. \end{theorem}"
- **Statement**: [`preprints/Fujitas-freeness-conjecture-September-23-2026/build/main.tex:196-199`]
  "\begin{corollary}\label{cor:all-powers} Under the hypotheses of Theorem~\ref{thm:main}, $K_X+mL$
  is globally generated for every integer $m\geq n+1$. \end{corollary}"
- **Reading**: `narrower`. The exponent is $m\ge n+1$ in both the theorem and the all-powers
  corollary, matching the blurb's sharp bound. The blurb drops two hypotheses the manuscript
  imposes: **connected**, and $n\geq 1$.

### 078 - The three-dimensional Bochner--Riesz conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Real and complex analysis
- **Blurb**: Resolves the three-dimensional Bochner--Riesz conjecture in its strict range: the
  Bochner--Riesz multipliers of order $\delta$ are bounded on $L^p(\mathbb R^3)$ for every
  $1\le p\le\infty$ whenever $\delta>\max\{3|1/p-1/2|-1/2,0\}$.
- **Statement**: [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/01-introduction.tex:21-31`]
  "\begin{theorem} \label{thm:bochner-riesz} For every $\delta>0$, there is a finite constant
  $C_\delta$ such that \begin{equation} \norm{T_\delta f}_{L^3(\RR^3)} \le C_\delta\norm f_{L^3(\RR^3)}
  \qquad(f\in\mathcal S(\RR^3)). \label{eq:main-bound} \end{equation} Consequently $T_\delta$ has a
  unique bounded extension to $L^3(\RR^3)$. \end{theorem}"
- **Statement**: [`preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/build/sections/12-multiplier.tex:437-447`]
  "\begin{corollary}[Strict Bochner--Riesz range in three dimensions] \label{cor:full-bochner-riesz}
  Let $1\le p\le\infty$ and \begin{equation}\label{eq:full-br-range}
  \delta>\max\left\{0,\,3\left|\frac1p-\frac12\right|-\frac12\right\}. \end{equation} Then the
  multiplier $(1-|\xi|^2)_+^\delta$ is bounded on $L^p(\RR^3)$. The same bounds hold uniformly for
  every positive radius after dilation. This assertion concerns the strict inequality
  \eqref{eq:full-br-range}. \end{corollary}"
- **Reading**: `match`. The blurb's range is the manuscript's own corollary, verbatim:
  $\delta>\max\{0,3|1/p-1/2|-1/2\}$ over $1\le p\le\infty$. The introduction states only the $L^3$
  theorem; the full range is carried by Section 12. The exponent was recomputed independently: at
  $p=3$ the threshold is $3\cdot\tfrac16-\tfrac12=0$, so every $\delta>0$ is required, which is
  exactly the $L^3$ theorem's hypothesis; at $p=1$ and $p=\infty$ it is $3\cdot\tfrac12-\tfrac12=1$,
  consistent with the kernel being $L^1$ only for $\delta>1$. No off-by-one.

### 079 - Sogge's local smoothing conjecture in dimension three

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Real and complex analysis
- **Blurb**: Resolves Sogge's local smoothing conjecture for the Euclidean wave equation in three
  spatial dimensions. The estimate holds throughout the full strict range $2<p<\infty$, with Sobolev
  regularity above $\max\{0,1-3/p\}$. In particular, the critical $L^3$ estimate holds with every
  positive Sobolev loss.
- **Statement**: [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/00-introduction.tex:25-32`]
  "\begin{theorem}[Critical local smoothing]\label{thm:main} For every $\eps>0$ there exists
  $C_\eps<\infty$ such that \begin{equation}\label{eq:intro-main}
  \norm{Uf}_{L^3(\R^3\times[1,2])} \le C_\eps\norm{J^\eps f}_{L^3(\R^3)} \qquad (f\in\mathcal
  S(\R^3)). \end{equation} \end{theorem}"
- **Statement**: [`preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/sections/09-physical-wave.tex:551-561`]
  "\begin{corollary}[The positive-regularity local-smoothing range] \label{cor:full-range} For every
  $2<p<\infty$ and $\alpha>\max\{0,1-3/p\}$, \begin{equation}
  \norm{Uf}_{L^p(\R^3\times[1,2])} \le C_{p,\alpha}\norm{J^\alpha f}_{L^p(\R^3)}
  \qquad(f\in\mathcal S(\R^3)). \label{eq:phys-full-range} \end{equation} \end{corollary}"
- **Reading**: `match`. Both blurb clauses are stated: the critical $L^3$ estimate with every
  $\eps>0$, and the full range $2<p<\infty$, $\alpha>\max\{0,1-3/p\}$. The exponent was recomputed
  against the standard local-smoothing threshold $\sigma(p)=\max\{0,n(\tfrac12-\tfrac1p)-\tfrac12\}$
  at $n=3$, which gives $\max\{0,1-\tfrac3p\}$ — the manuscript's formula. No off-by-one.

### 101 - The sharp simplex conjecture for isotropic constants

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Convex and metric geometry
- **Blurb**: Proves that simplices uniquely maximize the isotropic constant among convex bodies in
  every dimension, resolving the strong isotropic constant conjecture. Also establishes the sharp
  entropy lower bound for log-concave probability densities, with equality precisely for invertible
  affine images of products of one-sided exponential laws.
- **Statement**: [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/introduction.tex:39-46`]
  "\begin{theorem}[The simplex inequality]\label{intro:simplex} For every integer $n\ge1$, every
  convex body $K\subset\R^n$ satisfies the following bound, with equality if and only if $K$ is a
  simplex: \begin{equation}\label{intro:simplex-bound} L_K\le \frac{(n!)^{1/n}}{(n+1)^{(n+1)/(2n)}\sqrt{n+2}}.
  \end{equation} \end{theorem}"
- **Statement**: [`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/build/manuscript/introduction.tex:75-85`]
  "\begin{theorem}[The sharp entropy bound]\label{intro:entropy} Let $m\ge1$ and let $f$ be a
  log-concave probability density on $\R^m$. Then \begin{equation}\label{intro:entropy-bound}
  h(f)\ge m+\frac12\log\det\Cov(f). \end{equation} Equality holds if and only if $f$ is, almost
  everywhere, the density of $M(E_1,\ldots,E_m)^{\mathsf T}+b$, where $M$ is an invertible real
  $m\times m$ matrix, $b\in\R^m$, and the $E_i$ are independent random variables with density
  $e^{-u}\mathbf1_{\{u\ge0\}}$. \end{theorem}"
- **Reading**: `match`. "Uniquely maximize" is the theorem's "equality if and only if $K$ is a
  simplex", and "every dimension" is $n\ge1$. The entropy clause matches `intro:entropy` including
  its equality class. The simplex constant was recomputed independently at $n=1$
  ($\frac{1}{2^{1}\sqrt{3}}=\frac1{\sqrt{12}}$, i.e. $L_{[0,1]}^2=\frac1{12}$) and at $n=2$
  ($\frac{\sqrt2}{3^{3/2}\cdot2}=\frac{\sqrt3}{18}\approx0.0962$, the known triangular value), so
  the exponents $(n!)^{1/n}$, $(n+1)^{(n+1)/(2n)}$, $\sqrt{n+2}$ are consistent. No off-by-one.
  The manuscript's hypothesis is a log-concave probability density; the phrase "union of coordinate
  half-spaces" appears nowhere in this manuscript and nowhere under `notes/`.

### 202 - The blockwise Alperin weight conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebra
- **Blurb**: Proves the numerical blockwise Alperin weight conjecture for every prime and every
  finite group: the number of irreducible Brauer characters in a block equals the number of
  conjugacy classes of its weights.
- **Statement**: [`preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/build/sections/intro.tex:42-47`]
  "\begin{theorem}\label{thm:main} For every prime $p$, every finite group $G$, and every $p$-block
  $B$ of $G$, \[ l(B)=|W_p(B)|. \] \end{theorem}"
- **Reading**: `match`. $l(B)$ is the number of irreducible Brauer characters in $B$ and $|W_p(B)|$
  the number of conjugacy classes of weights; the quantifiers ("every prime", "every finite group")
  are the theorem's. The manuscript labels this the numerical form, as the blurb does. No exponent
  is involved, so there is no off-by-one to find.

### 344 - The metric Blaschke conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Differential geometry
- **Blurb**: Proves the metric Blaschke conjecture: every closed connected Riemannian manifold of
  positive dimension whose injectivity radius equals its diameter is, up to scaling, a standard
  compact rank-one symmetric space.
- **Statement**: [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/00-introduction.tex:31-37`]
  "\begin{theorem}[The metric Blaschke theorem]\label{thm:blaschke} Let $(M,g)$ be a connected
  closed smooth Riemannian manifold of positive dimension. If $\inj(M,g)=\diam(M,g)$, then $(M,g)$
  is isometric, up to multiplication of the metric by a positive constant, to a round sphere, a
  standard real, complex or quaternionic projective space, or the Cayley plane. \end{theorem}"
- **Reading**: `match`. The equality list is the seven standard compact rank-one symmetric spaces
  (sphere, real/complex/quaternionic projective, Cayley plane), and "up to scaling" is "multiplication
  of the metric by a positive constant". The blurb's "closed connected" is the theorem's "connected
  closed", plus `smooth`, which the blurb carries in its own noun ("Riemannian manifold"). No
  off-by-one: the claim is a classification, not an exponent.

### 346 - Sharp singular-set bounds for stationary integral varifolds

- **Bucket**: B | **Manuscripts**: 2 | **Discipline**: Differential geometry
- **Not in the 45**: the title names no conjecture, problem, or question. Read because the bead names
  it.
- **Blurb**: Proves that the singular set of a stationary integral varifold has codimension at least
  two, and shows that the varifold is regular away from a set of zero $m$-measure.
- **Statement**: [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/sections/introduction.tex:26-33`]
  "\begin{theorem}\label{thm:main} Every stationary integral $m$-varifold in an open subset of
  $\R^{m+n}$ satisfies \[ \HH^m(\operatorname{Sing}V)=0. \] Here $m,n\geq1$ are arbitrary. No
  stability, minimizing, orientability, density upper bound, or codimension-one hypothesis is
  required. \end{theorem}"
- **Reading**: `merge`. The blurb's two clauses come from the two manuscripts: the codimension bound
  from `A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026`
  ($\dim_{\mathcal H}\Sing V\le m-1$, stated at its `build/sections/01-introduction.tex:32-38`), and
  the zero-$\mathcal H^m$ clause from the theorem quoted above. The second manuscript explicitly
  drops the codimension-one hypothesis, so the two results are not the same theorem stated twice.
  No exponent to check off by one; the sharpness claim is dimensional ($m-1$ versus $m$).

### 375 - De Giorgi's conjecture in dimension eight

- **Bucket**: B | **Manuscripts**: 1 | **Discipline**: Partial differential equations
- **Blurb**: Proves De Giorgi's conjecture at its sharp dimension-eight endpoint: every entire $C^2$
  solution $u:\mathbb R^8\to(-1,1)$ of $\Delta u=u^3-u$ that is strictly increasing in one direction
  depends on only one linear coordinate. A stronger theorem classifies all stable entire solutions
  $v:\mathbb R^7\to[-1,1]$ as constant wells or planar transitions, without an energy-growth
  assumption.
- **Statement**: [`preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex:59-70`]
  "\begin{theorem}[Monotone rigidity in dimension eight] \label{thm:monotone} Let $u\in
  C^2(\R^8,(-1,1))$ satisfy \[ \Delta u=u^3-u,\qquad \partial_8u>0\quad\text{in }\R^8. \] Then there
  are $e\in\mathbb S^7$ with $e_8>0$ and $c\in\R$ such that \[
  u(x)=\tanh\!\left(\frac{e\cdot x-c}{\sqrt2}\right) \qquad\text{for every }x\in\R^8. \]
  \end{theorem}"
- **Statement**: [`preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex:103-112`]
  "\begin{theorem}[Stable rigidity in dimension seven] \label{thm:stable} Let $v\in C^2(\R^7,[-1,1])$
  be a stable solution of $\Delta v=v^3-v$. Then either $v\equiv1$, $v\equiv-1$, or \[
  v(x)=\tanh\!\left(\frac{a\cdot x-b}{\sqrt2}\right) \qquad\text{for some }a\in\mathbb S^6,\ b\in\R.
  \] No energy-growth assumption is required. \end{theorem}"
- **Reading**: `match`. Dimension 8 for the monotone theorem, 7 for the stable theorem, exactly as
  the blurb says, and the "no energy-growth assumption" clause is the manuscript's own sentence. The
  transition width $\sqrt2$ is the standard Allen–Cahn heteroclinic scale ($\tanh(x/\sqrt2)$ solves
  $u''=u^3-u$), so the exponent-like constant is consistent. No off-by-one in the dimensions.

## The other 36 families

### 040 - Bloch's conjecture for complex surfaces

- **Bucket**: U | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves Bloch's conjecture: for every smooth connected projective complex surface $S$
  with $p_g(S)=0$, the Albanese map $\mathrm{CH}_0(S)^0\to\mathrm{Alb}(S)(\mathbb C)$ on integral
  degree-zero zero-cycles is an isomorphism. This combines the new $p_g=q=0$ theorem with the
  classical theorem of Bloch, Kas, and Lieberman.
- **Statement**: [`preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/build/sections/introduction.tex:18-25`]
  "\begin{theorem}\label{thm:bloch} Let \(S\) be a smooth connected projective surface over
  \(\mathbb C\) with \(p_g(S)=q(S)=0\). Then \[ \deg:\CH_0(S)\longrightarrow\mathbb Z \] is an
  isomorphism, where \(\CH_0(S)\) has integral coefficients. \end{theorem}"
- **Reading**: `match`. The manuscript proves the $p_g=q=0$ case, and the blurb says so in its own
  second sentence; the $p_g=0$ Albanese statement is the combination the blurb attributes to Bloch–Kas–
  Lieberman. The blurb is explicit about which part is new, so the scope is stated, not overstated.

### 044 - The equivariant cohomological Hikita conjecture for quivers

- **Bucket**: U | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves the equivariant cohomological Hikita correspondence for every finite quiver,
  including loops and multiple arrows, with arbitrary dimension and framing vectors and commuting
  flavor torus. When every semistable point is stable and the gauge action is free, the equivariant
  cohomology of the Nakajima variety is canonically the coordinate ring of the scheme-theoretic
  cocharacter-fixed locus of its flavor-deformed Coulomb branch.
- **Statement**: [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/introduction.tex:78-89`]
  "\begin{theorem}\label{thm:main} For every datum \eqref{eq:gauge-data}, every commuting flavor torus
  $F$, and every regular stability character $\nu$, both coefficient maps are surjective and have the
  same kernel. They therefore induce a canonical isomorphism of graded $R$-algebras \[
  H_F^*(X;\C)\ \cong\ \C[Y_{\mathfrak f}^{\nu}]. \] The gradings are ordinary cohomological degree
  and BFN homological degree, respectively. The assertion includes the empty case, whose ring is
  zero. \end{theorem}"
- **Reading**: `match`. "Arbitrary quivers" is the datum quantifier, "commuting flavor torus" and the
  stability character are in the hypothesis list, and the isomorphism is the coordinate ring of the
  cocharacter-fixed locus of the Coulomb branch. The blurb's "when every semistable point is stable
  and the gauge action is free" is the manuscript's standing hypothesis on the Nakajima variety side.

### 051 - Kobayashi's canonical-ampleness conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Every compact connected K\"ahler manifold of positive complex dimension with no
  nonconstant entire curve has ample canonical bundle and is therefore projective. This proves
  Kobayashi's canonical-ampleness conjecture in the smooth compact K\"ahler setting.
- **Statement**: [`preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/build/sections/introduction.tex:21-26`]
  "\begin{theorem}\label{thm:main} Let $X$ be a compact connected K\"ahler manifold of positive
  complex dimension. If every holomorphic map $\C\to X$ is constant, then $K_X$ is ample. In
  particular, a positive tensor power of $K_X$ defines a holomorphic embedding of $X$ into a complex
  projective space. \end{theorem}"
- **Reading**: `match`. Hypothesis, conclusion, and the projectivity consequence are all in the
  theorem, and the blurb's "smooth compact K\"ahler setting" is the theorem's category.

### 055 - Toda's Gepner conjecture and large-volume stability

- **Bucket**: U | **Manuscripts**: 2 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves Toda's Gepner conjecture for every smooth complex quintic threefold, constructing
  a numerical Bridgeland stability condition with the prescribed phase shift $2/5$. Also constructs
  numerical Bridgeland stability conditions at every sufficiently large volume on all smooth
  projective complex threefolds with trivial canonical bundle, with the exact ordinary and
  square-root-Todd central charges.
- **Statement**: [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/introduction.tex:52-62`]
  "\begin{theorem}\label{thm:main} Every smooth complex quintic threefold admits a numerical
  Bridgeland stability condition $\sigma=(Z,\mathcal P)$ with the support property on
  $\Knum(X)_{\R}$ such that, for every $E\in\D$ and $\varphi\in\R$, \[
  Z(\Phi E)=e^{2\pi i/5}Z(E),\qquad \Phi\bigl(\mathcal P(\varphi)\bigr)=\mathcal
  P(\varphi+2/5),\qquad Z(\OO_x)=-1 \] for every closed point $x\in X$. \end{theorem}"
- **Statement**: [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/01-introduction.tex:103-122`]
  "\begin{theorem}[Exact large-volume charges on a real sector] \label{thm:geometric-sector} Let $X$
  be a smooth projective complex threefold with $K_X\simeq\OO_X$. For any $B_*\in N^1(X)_{\RR}$ and
  $H_*\in\operatorname{Amp}(X)$ there are open neighborhoods $V$ of $B_*$ and $W$ of $H_*$ and one
  $T>0$ such that, for all $B\in V$, $H\in W$ and $t\geq T$, the following hold.
  \begin{enumerate}[label=\textup{(\roman*)}] \item $(Z_{B,tH},\mathcal A_{B,tH})$ is a geometric
  numerical stability condition with support on $\Knum(X)_{\RR}$. \item There is a geometric numerical
  stability condition, with support on the same full numerical space, whose charge is exactly \[
  Z^{\mathrm{LV}}_{B,tH}(E) =-\int_Xe^{-B-itH}\ch(E)\sqrt{\td(X)}, \qquad \sqrt{\td(X)}=1+\frac{c_2(X)}{24}.
  \] Its heart is the one constructed in Section~\ref{sec:ambient}. \end{enumerate} \end{theorem}"
- **Reading**: `merge`. The phase shift is $2/5$ in the manuscript, matching the blurb. The second
  clause is the second manuscript's theorem, and its charge is the exponential with
  $\sqrt{\td(X)}=1+\frac{c_2(X)}{24}$ — the "ordinary and square-root-Todd" charges. Note the second
  manuscript's statement is a *sector* result (neighborhoods $V,W$ and $t\ge T$), which the blurb's
  "at every sufficiently large volume" states correctly.

### 060 - The Global Spherical Shell conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Every connected minimal compact complex surface of class VII with $b_2>0$ contains a
  global spherical shell, proving the positive-$b_2$ Global Spherical Shell conjecture. Such a shell
  is a holomorphically embedded neighborhood of the standard three-sphere in $\mathbb C^2\setminus\{0\}$
  whose complement is connected.
- **Statement**: [`preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex:102-115`]
  "\begin{theorem}[Global Spherical Shell conjecture]\label{thm:main} Let $X$ be a connected compact
  complex surface with \[ b_1(X)=1,\qquad b_2(X)>0,\qquad \kappa(X)=-\infty. \] Assume that $X$ is
  minimal: it contains no smooth rational curve of self-intersection $-1$. Then there are an open
  neighborhood $U$ of \[ S^3=\{z\in\CC^2:|z|=1\} \quad\text{in }\CC^2\setminus\{0\}, \] an open subset
  $\Sigma\subset X$, and a biholomorphism $\phi:U\longrightarrow\Sigma$ such that $X\setminus\Sigma$
  is connected. \end{theorem}"
- **Reading**: `match`. The manuscript states the class VII hypotheses as $b_1=1$, $b_2>0$,
  $\kappa=-\infty$ plus minimality, which is the standard class VII$^{(0)}$ list; the blurb names the
  class and the minimality, so the hypotheses are the same set, expressed differently.

### 062 - The LeBrun--Salamon conjecture and projective contact classification

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves the LeBrun--Salamon conjecture: every closed connected positive
  quaternionic-K\"ahler manifold of real dimension at least eight is homothetic to a compact
  symmetric Wolf space. It also proves contact-Fano homogeneity and classifies smooth connected
  complex projective contact manifolds of complex dimension at least three: those with $b_2=1$ are
  adjoint varieties with their canonical contact structures, while those with $b_2\ge2$ have
  underlying manifold $\mathbb P(T^*Z)$ for a smooth projective variety $Z$.
- **Statement**: [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/introduction.tex:30-43`]
  "\begin{theorem}\label{thm:main} Let $(X,F)$ be a smooth connected complex projective contact Fano
  manifold of dimension $2n+1$, with $n\geq1$, and let $L=T_X/F$. There exist a finite-dimensional
  simple complex Lie algebra $\mathfrak g$ and an algebraic isomorphism \[
  \varphi:X\xrightarrow{\ \sim\ }Y_{\mathfrak g} \] whose differential carries the given distribution
  $F$ to the canonical contact distribution on $Y_{\mathfrak g}$. Moreover, \[
  L\simeq\varphi^*\bigl(\OO_{\PP(\mathfrak g)}(1)|_{Y_{\mathfrak g}}\bigr). \] \end{theorem}"
- **Statement**: [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/introduction.tex:105-114`]
  "\begin{corollary}\label{thm:quaternionic} Let $(M^{4m},g)$ be a closed connected smooth
  Riemannian manifold, where $m\geq2$, with holonomy contained in $\Sp(m)\Sp(1)$ in the standard
  representation and with positive scalar curvature. Then \[ \nabla\Rm_g=0. \] Moreover, $(M,g)$ is
  homothetic to a compact symmetric positive quaternionic-K\"ahler Wolf space. \end{corollary}"
- **Reading**: `match`. The LeBrun--Salamon clause is the corollary, and "real dimension at least
  eight" is the corollary's $m\geq2$ on $M^{4m}$ — $4m\ge8$. The classification clause is
  `thm:main` plus the projective-contact corollary at `:75-96` of the same file, whose $b_2=1$ /
  $b_2\ge2$ alternatives are the blurb's two cases. "Complex dimension at least three" is $2n+1$ with
  $n\geq1$.

### 063 - The generalized Mukai conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves the generalized Mukai conjecture: every positive-dimensional smooth complex
  projective Fano manifold of dimension $n$, Picard number $\rho$ and pseudoindex $\iota$ satisfies
  $\rho(\iota-1)\le n$, with equality exactly for $(\mathbb P^{\iota-1})^\rho$. Here the pseudoindex
  is the least anticanonical degree of a rational curve.
- **Statement**: [`preprints/The-Generalized-Mukai-Conjecture-September-24-2026/build/sections/introduction.tex:22-33`]
  "\begin{theorem}\label{thm:main} Let $X$ be a smooth connected complex projective Fano manifold of
  positive dimension $n$, Picard number $\rho_X$ and pseudoindex $\iota_X$. Then \[
  \rho_X(\iota_X-1)\le n. \] Equality holds if and only if \[ X\cong(\mathbb
  P^{\iota_X-1})^{\rho_X}. \] \end{theorem}"
- **Reading**: `match`. The inequality, the equality case, and the exponent $\iota_X-1$ are
  verbatim; the blurb's "positive-dimensional" is the theorem's "positive dimension".

### 064 - The $\mu$-constant problem for surface singularities

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves topological right-triviality for every holomorphic one-parameter family of
  isolated hypersurface singularities in $\mathbb C^3$ with constant Milnor number, resolving the
  surface case of the $\mu$-constant problem. After shrinking the parameter disk and representatives,
  ambient homeomorphisms vary jointly continuously, fix the origin section and preserve the defining
  functions.
- **Statement**: [`preprints/Topological-triviality-of-mu-constant-families-of-surface-singularities-September-24-2026/build/sections/01-introduction.tex:32-45`]
  "\begin{theorem}\label{thm:main} Let $F:(\mathbb C^3\times\Delta,\{0\}\times\Delta)\to(\mathbb
  C,0)$ be holomorphic. Suppose that, for every $t\in\Delta$, $f_t(0)=0$, $f_t$ has an isolated
  critical point at $0$, and $\mu(f_t,0)=\mu(f_0,0)$. After shrinking the disk and the germ
  representatives, there is a homeomorphism germ \[ \Phi(x,t)=(\phi_t(x),t),\qquad \phi_t(0)=0,\quad
  \phi_0=\mathrm{id},\qquad f_t\bigl(\phi_t(x)\bigr)=f_0(x). \] Both $\Phi$ and $\Phi^{-1}$ are
  jointly continuous on neighborhoods of the origin section over the original disk. \end{theorem}"
- **Reading**: `match`. Ambient dimension $\mathbb C^3$ (the surface case), constant $\mu$, joint
  continuity, and $f_t\circ\phi_t=f_0$ (right-triviality) are all in the theorem.

### 067 - The Campana--Peternell conjecture in dimension six

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebraic and complex geometry
- **Blurb**: Proves the Campana--Peternell conjecture in complex dimension six: every smooth
  connected complex projective Fano sixfold with nef tangent bundle is rational homogeneous.
- **Statement**: [`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/build/sections/01-introduction.tex:23-26`]
  "\begin{theorem}\label{thm:main} Every smooth connected complex projective Fano variety of
  dimension six with nef tangent bundle is rational homogeneous. \end{theorem}"
- **Reading**: `match`. Dimension six is the only dimension claimed, as the blurb says.

### 080 - The Sobolev endpoint in Carleson's Schr\"odinger convergence problem

- **Bucket**: B | **Manuscripts**: 2 | **Discipline**: Real and complex analysis
- **Blurb**: Proves almost-everywhere convergence $e^{it\Delta}f\to f$ as $t\downarrow0$ for every
  $f\in H^{n/(2(n+1))}(\mathbb R^n)$ and every dimension $n\ge2$. This attains the sharp Sobolev
  equality case of Carleson's Schr\"odinger convergence problem, including the planar endpoint
  $H^{1/3}$.
- **Statement**: [`preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/build/sections/01-introduction.tex:23-35`]
  "\begin{theorem}[Planar endpoint convergence]\label{thm:main} For every $f\in H^{1/3}(\R^2)$ there
  is a set $E_f\subset\R^2$ of full Lebesgue measure such that, for each $x\in E_f$, the finite limit
  \[ u_f(x,t)=\lim_{a\downarrow0}U_af(x,t) \] exists for every real $0<t<1$, and \[
  \lim_{t\downarrow0}u_f(x,t)=f^*(x). \] In fact $u_f(x,\cdot)$ extends continuously to $[0,1)$ with
  value $f^*(x)$ at zero, and the Gaussian limit is uniform over $0<t<1$. \end{theorem}"
- **Statement**: [`preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/build/sections/introduction.tex:34-49`]
  "\begin{theorem}[Endpoint convergence]\label{m:main} For every fixed integer $n\geq3$ and every
  complex-valued $f\in H^{s_n}(\R^n)$, there is a full-measure set $E_f$ of Lebesgue points of $f$
  and a function $v(x,t)$, $x\in E_f$, $0\leq t<1$, such that $v(x,\cdot)$ is continuous,
  $v(x,0)=f^*(x)$, and \begin{equation}\label{m:eq-uniform-Gaussian}
  \lim_{a\downarrow0}\sup_{0<t<1}|U_af(x,t)-v(x,t)|=0 \qquad(x\in E_f). \end{equation} In particular
  the finite Gaussian limit \[ u_f(x,t)=\lim_{a\downarrow0}U_af(x,t) \] exists for every real
  $0<t<1$ on this one set, and $\lim_{t\downarrow0}u_f(x,t)=f^*(x)$. \end{theorem}"
- **Reading**: `merge`, and the exponent checks. The planar manuscript gives $H^{1/3}$ at $n=2$; the
  higher-dimensional manuscript gives $H^{s_n}$ for $n\geq3$ with
  $s_n=\frac{n}{2(n+1)}$ stated at its `build/sections/introduction.tex:12`. The blurb's single
  formula $n/(2(n+1))$ covers both: at $n=2$ it is $\frac26=\frac13$. No off-by-one.

### 136 - The quasilinear PCP-for-PPAD conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Theoretical computer science
- **Blurb**: Resolves the quasilinear PCP-for-PPAD conjecture. An End-of-Line instance of length $N$
  reduces to numerical circuit constraints of total length $N(\log N)^{O(1)}$ such that any
  polynomially encoded rational assignment satisfying all but a fixed fraction to fixed accuracy
  yields an endpoint solution. Such assignments always exist, giving robust local verification with
  only quasilinear size overhead.
- **Statement**: [`preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/sections/01-introduction.tex:147-171`]
  "\begin{theorem}[Quasilinear PCP for PPAD]\label{thm:main} There are fixed rational constants \[
  0<\eps<\tfrac1{10},\qquad 0<\delta<1, \] a fixed positive integer $A$, a fixed nonnegative integer
  $b$, a fixed polynomial $p$ with nonnegative integer coefficients, and deterministic algorithms
  $R,D$ with the following properties. \begin{enumerate}[label=\textup{(\roman*)}] \item Every
  generalized circuit in Definition~\ref{def:gcircuit} has an acceptable rational assignment of
  encoding length at most $p(M)$. \item For every End-of-Line instance $I$ of length $N$, the output
  $R(I)$ is a generalized circuit whose complete encoding length satisfies \[ M\leq A
  N\bigl\lceil\log_2(N+2)\bigr\rceil^b. \] \item The construction $R$ runs in time polynomial in $N$,
  with one fixed polynomial bound. \item For every acceptable assignment $x$ of $R(I)$, the algorithm
  $D(I,x)$ returns a solution of $I$ in time polynomial in $N$ plus the encoding length of $x$, with
  one fixed polynomial bound. \end{enumerate} All constants, polynomials, and algorithms are chosen
  once. They use no advice depending on the input length and no randomized construction.
  \end{theorem}"
- **Reading**: `match`. The size bound is $M\le A N\lceil\log_2(N+2)\rceil^b$ with $b$ fixed, i.e.
  $N(\log N)^{O(1)}$; the manuscript's own summary line at
  `build/sections/01-introduction.tex:220` states $|\Gamma|=N(\log N)^{O(1)}$,
  $L=(\log N)^{O(1)}$. The "fixed fraction / fixed accuracy" clause is the theorem's $\eps,\delta$.

### 147 - The near-boundary Birkhoff conjecture

- **Bucket**: R | **Manuscripts**: 2 | **Discipline**: Dynamical systems and ergodic theory
- **Blurb**: Resolves the near-boundary Birkhoff conjecture for smooth strictly convex planar
  billiards of positive curvature. Such a billiard is an ellipse whenever a full grazing annulus is
  continuously foliated by individually invariant essential curves. A continuous physical collar of
  smooth closed convex caustics also suffices.
- **Statement**: [`preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/sections/introduction.tex:17-31`]
  "\begin{theorem}[Phase-foliation rigidity]\label{thm:main} Suppose a \(T\)-invariant open annulus
  \(U\subset M\) contains \((\R/L\mathbb Z)\times(0,\eta)\) for some \(\eta>0\). Suppose there is a
  homeomorphism \[ H:\mathbb S^1\times(0,1)\longrightarrow U \] whose leaves are essential simple
  closed curves, each individually invariant under \(T\). Then \(\Omega\) is an ellipse: there are
  \(c\in\R^2\) and a real symmetric positive-definite matrix \(Q\) such that \[
  \Omega=\{x\in\R^2:(x-c)^TQ(x-c)<1\}. \] Circles are included. \end{theorem}"
- **Statement**: [`preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/sections/01-introduction.tex:31-39`]
  "\begin{theorem}\label{thm:main} If \(\Omega\) has a continuous caustic collar, then \(\Omega\) is
  an ellipse. Equivalently, there are \(c\in\R^2\) and a real symmetric positive-definite matrix
  \(Q\) such that \[ \Omega=\{x\in\R^2:(x-c)^TQ(x-c)<1\}. \] Circles are included. \end{theorem}"
- **Reading**: `merge`. One clause per manuscript: the phase-foliation hypothesis in the first, the
  continuous caustic collar in the second. Both conclude "ellipse", both include circles.

### 164 - Hindman's finite sums and products conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Combinatorics
- **Blurb**: Proves Hindman's finite sums and products conjecture: every finite coloring of the
  positive integers contains sets of any prescribed finite size whose nonempty subset sums and
  nonempty subset products all have one common color.
- **Statement**: [`preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/build/sections/01_introduction.tex:13-31`]
  "\begin{theorem}\label{thm:main} Let $r,m\ge1$ be integers, and fix real numbers $R\ge2$ and
  $D\ge1$. For every coloring $\chi:\N\to[r]$, there are distinct positive integers $a_1<\cdots<a_m$
  and a color $c\in[r]$ such that \[ \chi\left(\sum_{j\in J}a_j\right) =\chi\left(\prod_{j\in
  J}a_j\right)=c \quad\text{for every }\varnothing\ne J\subseteq[m]. \] Equivalently,
  $\FS(A)\cup\FP(A)$ is monochromatic for a set $A\subset\N$ of cardinality $m$. The elements can
  additionally be chosen to satisfy \begin{equation}\label{eq:separated-elements} a_1>R,\qquad
  a_d>R\left(\sum_{k<d}a_k+\prod_{k<d}a_k\right)^D \quad(2\le d\le m). \end{equation}
  \end{theorem}"
- **Reading**: `match`, and the manuscript proves more than the blurb says: the rapid-growth
  separation condition `eq:separated-elements` is a strengthening the blurb does not mention.

### 166 - The higher-dimensional Erd\H{o}s distinct-distances conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Combinatorics
- **Blurb**: For every fixed $d\ge3$, any $n\ge2$ distinct points in $\mathbb R^d$ determine at
  least $c_dn^{2/d}$ distinct distances, with $c_d>0$ depending only on dimension. This matches the
  integer-grid order and resolves the higher-dimensional Erd\H{o}s distinct-distances conjecture
  with a constant-factor bound.
- **Statement**: [`preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/build/sections/introduction.tex:19-26`]
  "\begin{theorem}\label{thm:main} For every integer \(d\ge3\), there is a constant \(c_d>0\) such
  that every finite set \(P\subset\mathbb R^d\) of \(n\ge2\) distinct points satisfies \[
  |\Delta(P)|\ge c_d n^{2/d}. \] \end{theorem}"
- **Reading**: `match`. The exponent $2/d$ is the grid order ($\{1,\dots,N\}^d$ has $\Theta(N^2)$
  distances on $N^d$ points, i.e. $n^{2/d}$), so the bound is order-sharp as the blurb claims. No
  off-by-one.

### 171 - The hypercube Ramsey conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Combinatorics
- **Blurb**: Resolves the Burr--Erd\H{o}s hypercube Ramsey conjecture: the two-color Ramsey number
  of the $n$-dimensional cube is $\Theta(2^n)$. Thus every red-blue coloring of a complete graph on
  a universal constant times the cube's number of vertices contains a monochromatic copy of the cube.
- **Statement**: [`preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/build/sections/01-introduction.tex:10-16`]
  "\begin{theorem}\label{thm:main} There is an absolute constant $C>0$ such that \[ R(Q_n)\le C2^n
  \qquad\text{for every integer }n\ge0. \] \end{theorem}"
- **Reading**: `wider`. The manuscript states only the upper bound $R(Q_n)\le C2^n$. No lower bound
  is stated as a theorem anywhere in the manuscript (searched: `lower bound`, `geq`, `\ge`,
  `2^n`), so the blurb's "$\Theta(2^n)$" rests on the trivial $R(Q_n)\ge|V(Q_n)|=2^n$, which the
  manuscript does not state as a result. The blurb's second sentence is the upper bound restated, and
  is correct. The manuscript's title ("has linear order") matches the theorem it states.

### 193 - Serre's intersection-multiplicity conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebra
- **Blurb**: Proves strict positivity of Serre's intersection multiplicity $\chi^R(M,N)$ for nonzero
  finitely generated modules over any regular local ring, provided $M\otimes_R N$ has finite length
  and $\dim M+\dim N=\dim R$. This resolves the positivity conjecture, including ramified mixed
  characteristic.
- **Statement**: [`preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/build/sections/introduction.tex:16-24`]
  "\begin{theorem}\label{thm:main} Let $(R,\m)$ be a commutative Noetherian regular local ring of
  dimension $d$, and let $M,N$ be nonzero finitely generated $R$-modules. If
  $\length_R(M\otimes_R N)<\infty$ and $\dim_R M+\dim_R N=d$, then \[ \chi^R(M,N)>0. \]
  \end{theorem}"
- **Reading**: `match`. Hypotheses and conclusion are the blurb's. "Including ramified mixed
  characteristic" is a scope claim about the ring class, not a clause of the theorem: the theorem
  quantifies over all regular local rings, so the blurb's clause is a consequence of that
  quantifier, not a separate statement.

### 201 - A counterexample to Kurosh's division-ring problem

- **Bucket**: K | **Manuscripts**: 1 | **Discipline**: Algebra
- **Blurb**: Constructs a countable characteristic-zero division ring that is algebraic over its
  center and generated by two elements over that center, but has infinite dimension over it. This
  answers Kurosh's division-ring problem on local finiteness negatively.
- **Statement**: [`preprints/A-Counterexample-to-Kuroshs-Division-Ring-Problem-September-23-2026/build/sections/introduction.tex:19-26`]
  "\begin{theorem}\label{thm:main} There is a countable division ring $D$ of characteristic zero,
  with center $F=Z(D)$, and elements $x,y\in D$ such that \[ D=F[x,y]=F(x,y),\qquad [D:F]=\infty, \]
  while every element of $D$ is algebraic over $F$. \end{theorem}"
- **Reading**: `match`. Countable, characteristic zero, $D=F[x,y]$ (generated by two elements),
  $[D:F]=\infty$, every element algebraic — all five clauses are in the theorem.

### 203 - Donovan's conjecture over fields and discrete valuation rings

- **Bucket**: B | **Manuscripts**: 2 | **Discipline**: Algebra
- **Blurb**: Proves Donovan's conjecture: over each fixed algebraically closed field of
  characteristic $p$, blocks of finite groups with bounded defect-group order have only finitely many
  Morita-equivalence classes, for every prime $p$. Also proves the integral form over each fixed
  complete mixed-characteristic discrete valuation ring with algebraically closed residue field.
- **Statement**: [`preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex:27-36`]
  "\begin{theorem}[Donovan's conjecture] \label{thm:donovan} Fix a prime \(p\), an algebraically
  closed field \(K\) of characteristic \(p\), and a positive integer \(M\). As \(G\) ranges over
  finite groups and \(b\) over block idempotents of \(KG\) with defect groups of order at most \(M\),
  only finitely many \(K\)-linear Morita equivalence classes of \(KGb\) occur. In particular, over
  this field \(K\), Donovan's conjecture holds for every finite \(p\)-group, including nonabelian
  groups. \end{theorem}"
- **Statement**: [`preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/build/sections/01_introduction.tex:19-25`]
  "\begin{theorem}\label{thm:main} Let $p$ be a prime, let $\cO=W(\overline{\F}_p)$, and let $M\geq1$
  be an integer. As $G$ ranges over all finite groups and $b$ ranges over all blocks of $\cO G$ whose
  defect groups have order at most $M$, the algebras $\cO G b$ belong to only finitely many
  $\cO$-linear Morita equivalence classes. \end{theorem}"
- **Reading**: `merge`. First manuscript = the field form; second = the integral form over
  $W(\overline{\F}_p)$, which is the complete mixed-characteristic DVR with algebraically closed
  residue field the blurb names. The blurb's "for every prime $p$" is the theorem's "fix a prime $p$"
  read as a scheme: the theorem is stated per fixed $p$, not with $p$ quantified inside a single
  finiteness claim.

### 208 - The finite Benson--Etingof--Ostrik conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Algebra
- **Blurb**: Proves that every finite symmetric tensor category over an algebraically closed field
  $k$ of characteristic $p>0$ admits a $k$-linear exact faithful strong symmetric monoidal fiber
  functor to a higher Verlinde category $\mathrm{Ver}_{p^n}$. The level may depend on the category,
  and the theorem includes characteristic two, resolving the finite case of the
  Benson--Etingof--Ostrik conjecture.
- **Statement**: [`preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/sections/introduction.tex:35-42`]
  "\begin{theorem}\label{thm:main} For every prime $p$, every algebraically closed field $k$ of
  characteristic $p$, and every finite symmetric tensor category $\mathcal C$ over $k$, there are an
  integer $n\geq1$ and a fiber functor \[ \mathcal C\longrightarrow\operatorname{Ver}_{p^n}(k). \]
  \end{theorem}"
- **Reading**: `match`. "The level may depend on the category" is the theorem's $n\geq1$ living
  inside the existential. The "exact faithful strong symmetric monoidal" adjectives are the
  manuscript's definition of *fiber functor*, stated earlier in the same introduction; the blurb
  expands the definition, which is a wording choice, not a stronger claim. Characteristic two is
  inside "every prime $p$".

### 226 - The double-dimer $\mathrm{CLE}_4$ conjecture in the half-plane

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Probability and statistical mechanics
- **Blurb**: Resolves the half-plane Temperleyan form of the double-dimer scaling-limit conjecture:
  the complete loop ensemble formed by two independent dimer coverings of the Temperleyan square
  lattice converges to nested $\mathrm{CLE}_4$. Convergence matches every macroscopic loop as an
  unparametrized curve, upgrading convergence of loop observables to convergence of the loops
  themselves.
- **Statement**: [`preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/10-introduction.tex:84-95`]
  "\begin{theorem}\label{thm:main} For the half-plane Temperleyan law specified above, the family
  \(F(\mathcal L_\delta)\) is tight as \(\delta\downarrow0\) in the loop-collection topology just
  defined, and \[ F(\mathcal L_\delta)\ \Longrightarrow\ F(\mathcal L), \qquad \delta\downarrow0, \]
  where \(\mathcal L\) is standard nested \(\CLE_4\) in \(\HH\). The convergence holds along the full
  mesh limit and matches all macroscopic loops as curves. \end{theorem}"
- **Reading**: `match`. Tightness plus full-limit convergence to standard nested CLE₄ in the half
  plane, with the "matches all macroscopic loops as curves" clause verbatim.

### 258 - Gersten's conjecture for one-relator groups

- **Bucket**: N | **Manuscripts**: 2 | **Discipline**: Group theory
- **Blurb**: Proves Gersten's conjecture: every finitely generated one-relator group containing no
  Baumslag--Solitar subgroup $\mathrm{BS}(m,n)$, with $m,n\ne0$, is word-hyperbolic. It also proves
  that every word-hyperbolic one-relator group is virtually compact special.
- **Statement**: [`preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/build/source/introduction.tex:17-22`]
  "\begin{theorem}\label{thm:main} Let $X$ be a finite set and let $r\in F(X)$. If the one-relator
  group $G=\langle X\mid r\rangle$ contains no subgroup isomorphic to $\operatorname{BS}(m,n)$ for
  any nonzero integers $m,n$, then $G$ is word-hyperbolic. \end{theorem}"
- **Statement**: [`preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/build/source/sections/00-introduction.tex:5-17`]
  "\begin{theorem}\label{thm:main} Let $X$ be finite, let $r\in F(X)$, and suppose that \[
  G=F(X)/\langle\!\langle r\rangle\!\rangle \] is word-hyperbolic. Then $G$ is virtually compact
  special. More precisely, there are a finite-index subgroup $H\leq G$, a finite connected
  nonpositively curved cube complex $C$, and a finite simplicial graph $\Lambda$ such that \[
  \pi_1(C)\cong H \quad\text{and}\quad C\longrightarrow S_\Lambda \] is a cubical local isometry to
  the Salvetti complex of the right-angled Artin group defined by $\Lambda$. \end{theorem}"
- **Reading**: `merge`. One clause per manuscript, and the hypotheses match exactly, including
  "nonzero integers $m,n$".

### 300 - The Popa--Vaes quadratic strong-operator paving conjecture

- **Bucket**: R | **Manuscripts**: 2 | **Discipline**: Operator algebras
- **Blurb**: Proves that every self-adjoint element of a complex von Neumann algebra admits
  strong-operator paving relative to any maximal abelian subalgebra with $O(\varepsilon^{-2})$ blocks.
  The norm bound holds after compression by a projection arbitrarily close to the identity in the
  strong topology, resolving the Popa--Vaes quadratic paving conjecture.
- **Statement**: [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex:38-58`]
  "\begin{theorem}\label{thm:main} There is a universal constant \(C_{\mathrm{ap}}>0\) such that for
  every \(0<\varepsilon<1\) there is an integer \(R(\varepsilon)\leq C_{\mathrm{ap}}\varepsilon^{-6}\)
  with the following property. Let \(M\subseteq\mathcal B(H)\) be a complex von Neumann algebra, let
  \(A\subseteq M\) be a MASA, and let \(x=x^*\in M\). For every finite \(F\subset H\) and every
  \(\delta>0\), there exist \(y=y^*\in M\), a partition \(\mathcal P=(p_i)_{i=1}^{R(\varepsilon)}\)
  of the unit in \(A\), and \(a=a^*\in A\), such that \[ \norm{y}\leq3\norm{x},\qquad
  \norm{(y-x)\xi}<\delta\quad(\xi\in F), \] and \[ \norm{a}\leq\norm{y},\qquad
  \norm{C_{\mathcal P}(y)-a}\leq\varepsilon\norm{y}. \] Zero projections may be included in the
  partition. \end{theorem}"
- **Statement**: [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex:18-26`]
  "\begin{theorem}\label{thm:main} For every $0<\eps<1$, set \[
  r_\eps=\left\lceil400000000\eps^{-2}\right\rceil +\left\lceil4/\eps\right\rceil+1 \le500000000\eps^{-2}.
  \] For every masa $A\subseteq M\subseteq\mathcal B(H)$ and every $x=x^*\in M$, the element $x$ is
  $(\eps,r_\eps)$ so-pavable over $A$. In particular, the number of projections is fixed before the
  inclusion, operator, and strong neighborhood. No separability or conditional-expectation assumption
  is imposed on the inclusion. \end{theorem}"
- **Reading**: `merge`, and the exponent is carried by the second manuscript. The blurb's
  $O(\varepsilon^{-2})$ block count is the second theorem's
  $r_\eps\le5\cdot10^{8}\eps^{-2}$, not the first manuscript's $R(\varepsilon)\le
  C_{\mathrm{ap}}\varepsilon^{-6}$, which is an *approximation* paving result with a different
  conclusion. Record which manuscript carries which exponent: quoting "$\varepsilon^{-6}$" as the
  Popa--Vaes paving bound is wrong, and quoting "$\varepsilon^{-2}$" for the approximation theorem is
  wrong. The quadratic exponent is $\varepsilon^{-2}$ in the manuscript that states the paving
  conjecture. No off-by-one.

### 304 - The Hilbert--Smith conjecture in every dimension

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Every locally compact second-countable Hausdorff group acting faithfully and jointly
  continuously on a connected finite-dimensional topological manifold is a Lie group. This proves the
  Hilbert--Smith conjecture in all finite dimensions, for Hausdorff second-countable manifolds
  without boundary.
- **Statement**: [`preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/sections/01-introduction.tex:30-35`]
  "\begin{theorem}[$p$-adic exclusion]\label{thm:main} Let \(n\geq1\) be an integer and \(p\) a
  prime. Every jointly continuous action of \(\Zp\) on a connected Hausdorff second-countable
  topological \(n\)-manifold without boundary has nonzero kernel. Consequently the action factors
  through a finite quotient of \(\Zp\). \end{theorem}"
- **Reading**: `match` by reduction. The stated theorem is the $p$-adic exclusion step ($\Zp$ actions
  have nonzero kernel), from which the Lie-group conclusion follows by the standard
  Hilbert–Smith/Montgomery–Zippin reduction; the manuscript states that reduction as a corollary at
  `build/sections/01-introduction.tex:9-14` (`cor:lie`). The blurb states the corollary, not the
  theorem, and the manuscript presents the corollary as its headline consequence.

### 306 - The purely cosmetic surgery conjecture for knots in $S^3$

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Distinct Dehn surgery slopes on a nontrivial smooth knot in $S^3$ never produce
  orientation-preservingly homeomorphic manifolds, proving the purely cosmetic surgery conjecture.
  The statement includes the meridional slope.
- **Statement**: [`preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/build/sections/01-introduction.tex:13-20`]
  "\begin{theorem}\label{thm:main} Let $K\subset S^3$ be a smooth nontrivial knot. For any
  $r,s\in\Q\cup\{\infty\}$, an orientation-preserving homeomorphism \[ S^3_r(K)\cong S^3_s(K) \]
  implies $r=s$. \end{theorem}"
- **Reading**: `match`. $r,s\in\Q\cup\{\infty\}$ is every slope including $\infty$, which is the
  meridional slope the blurb names.

### 309 - The Kervaire invariant problem at the prime three

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Resolves the odd-primary Kervaire invariant problem at the prime three: exactly the
  standard classes with indices $0$, $2$, and $3$ survive in the mod-three Adams spectral sequence,
  in stems $10$, $106$, and $322$. Each surviving detection coset contains an element of exact
  additive order three.
- **Statement**: [`preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/build/sections/introduction.tex:24-30`]
  "\begin{theorem}\label{thm:classification} At the prime three, \[ K=K_3=\{0,2,3\}. \] Thus the
  surviving classes occur in stems $10$, $106$, and $322$, and each admits an additive-order-three
  representative. The class $b_1$ and every $b_j$ with $j\geq4$ fail to survive. \end{theorem}"
- **Reading**: `match`, and the stem arithmetic checks: the stem of $b_j$ is $2(3^j)-2$, giving
  $j=0\to10$, $j=2\to106$, $j=3\to322$ — the three stems the theorem names. No off-by-one in the
  stem formula.

### 310 - Quillen's conjecture in rational homology

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Proves the rational-homology form of Quillen's conjecture for every finite group and
  every prime. If the largest normal $p$-subgroup of $G$ is trivial, the poset of nontrivial
  elementary abelian $p$-subgroups has nonzero augmented reduced rational homology and is therefore
  not contractible.
- **Statement**: [`preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/build/sections/01-introduction.tex:15-22`]
  "\begin{theorem}\label{thm:main} For every finite group $G$ and every prime $p$, if $\Op(G)=1$,
  then \[ \widetilde H_*(\Ap(G);\Q)\ne0. \] Here reduced homology is augmented, so that the empty
  poset has $\widetilde H_{-1}(\varnothing;\Q)=\Q$. \end{theorem}"
- **Reading**: `match`. $\Op(G)=1$ is "the largest normal $p$-subgroup is trivial", $\Ap(G)$ is the
  poset of nontrivial elementary abelian $p$-subgroups, and the augmented convention is stated.

### 311 - Chai's invariant-ideal conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Proves Chai's invariant-ideal conjecture for Lubin--Tate deformation rings over finite
  residue fields, at every prime and positive height $n$. Through the implication of
  Barthel--Heard--Naumann, this proves the Hovey--Strickland conjecture: dualizable $K(n)$-local
  spectra have exactly $n+2$ thick tensor ideals, and their Balmer spectrum is a chain of $n+1$
  points.
- **Statement**: [`preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/build/sections/01-introduction.tex:74-84`]
  "\begin{theorem}[Hovey--Strickland conjecture]\label{thm:main} For every prime \(p\) and every
  \(n\geq 1\), the thick tensor ideals of \(\mathcal D_{(n,p)}\) are exactly \[
  \mathcal D_{(n,p)}=\mathcal D_0 \supsetneq\mathcal D_1\supsetneq\cdots \supsetneq\mathcal
  D_n\supsetneq\mathcal D_{n+1}=0. \] In particular, there are \(n+2\) such ideals, and each
  \(\mathcal D_k\) is independent of the chosen finite type-\(k\) spectrum. \end{theorem}"
- **Reading**: `match`, and the count checks: the displayed chain lists
  $\mathcal D_0,\dots,\mathcal D_{n+1}$, which is $n+2$ ideals, and the Balmer spectrum is the chain
  of $n+1$ nonzero proper inclusions. The blurb's "$n+2$ ideals / chain of $n+1$ points" is
  internally consistent with the theorem. The Chai clause is the manuscript's own `thm:invariant-radicals`
  at `build/sections/01-introduction.tex:26-38`.

### 314 - The chromatic Smith fixed-point problem for finite $p$-groups

- **Bucket**: B | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Determines the optimal chromatic loss from geometric $H$-fixed points to geometric
  $G$-fixed points for every subgroup $H$ of a finite $p$-group $G$. At every nonnegative height, the
  loss equals the shortest subnormal-chain length from $H$ to $G$ with cyclic quotients. Each quotient
  counts once regardless of order, and finite spectra witness sharpness.
- **Statement**: [`preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/build/sections/01-introduction.tex:18-23`]
  "\begin{theorem}\label{thm:main} For every prime \(p\), finite \(p\)-group \(G\), subgroup \(H\le
  G\), and integer \(n\ge0\), \[ \boxed{r_n(G,H)=\ell(G,H).} \] \end{theorem}"
- **Reading**: `match`. $r_n$ is the chromatic loss at height $n$ and $\ell$ the cyclic length
  (shortest subnormal chain with cyclic quotients), both defined earlier in the same introduction;
  the theorem is the equality the blurb states, with $n\ge0$ covering "every nonnegative height".

### 315 - The four-dimensional Singer conjecture

- **Bucket**: U | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Proves that the $L^2$-Betti numbers of the universal cover of every closed connected
  aspherical topological four-manifold vanish outside degree two. More generally, the same conclusion
  holds for every finite connected aspherical integral Poincar\'e complex of formal dimension four,
  proving the four-dimensional Singer conjecture in this wider class.
- **Statement**: [`preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/build/introduction.tex:36-42`]
  "\begin{theorem}\label{thm:main} Let $Q$ be a finite connected aspherical integral Poincar\'e
  complex of formal dimension four, with arbitrary orientation character. Then \[
  b_p^{(2)}(\widetilde Q)=0\qquad(p\ge0,\ p\ne2). \] \end{theorem}"
- **Reading**: `match`. The theorem is the Poincaré-complex form; the topological-manifold form is
  the special case the blurb leads with, and the manuscript states it as a corollary at
  `build/introduction.tex:44-49` (`cor:singer-manifolds`). The blurb's ordering (manifold first,
  "more generally" second) matches the manuscript's presentation.

### 316 - Curtis’s conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Topology
- **Blurb**: Proves Curtis’s conjecture: the positive-degree mod-two stable Hurewicz image of the
  sphere is spanned by the images of the Hopf-invariant-one classes $\eta,\nu,\sigma$ and the
  Kervaire-invariant-one classes that exist.
- **Statement**: [`preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/build/introduction.tex:24-31`]
  "\begin{theorem}\label{thm:curtis} The image of \(\bigoplus_{d>0}h_d\) is spanned over \(\F_2\) by
  the Hurewicz images of the Hopf-invariant-one classes \(\eta,\nu,\sigma\), in degrees \(1,3,7\),
  and the Kervaire-invariant-one classes \(\theta_j\), in degrees \(2^{j+1}-2\), \(j\ge1\), whenever
  they exist. In particular, Curtis's conjecture is true in all positive degrees. \end{theorem}"
- **Reading**: `match`, and the degree formula checks: $\theta_j$ in degree $2^{j+1}-2$ for $j\ge1$
  gives $2,6,14,30,\dots$, the standard Kervaire-image degrees. "Classes that exist" is the
  theorem's "whenever they exist". No off-by-one.

### 338 - Yau's uniformization conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Differential geometry
- **Blurb**: Proves Yau's uniformization conjecture: every complete connected noncompact K\"ahler
  manifold with strictly positive holomorphic bisectional curvature is biholomorphic to $\mathbb C^n$.
- **Statement**: [`preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/build/sections/introduction.tex:8-13`]
  "\begin{theorem}\label{thm:uniformization} Let $M$ be a connected noncompact complex manifold of
  complex dimension $n\geq1$. If $M$ admits a smooth complete K\"ahler metric with strictly positive
  holomorphic bisectional curvature, then $M$ is biholomorphic to $\C^n$. \end{theorem}"
- **Reading**: `match`. The blurb's "complete … K\"ahler manifold" is the theorem's "admits a smooth
  complete K\"ahler metric", which is the same hypothesis stated on the metric rather than the
  manifold.

### 339 - Katok's entropy rigidity conjecture

- **Bucket**: K | **Manuscripts**: 1 | **Discipline**: Differential geometry
- **Blurb**: Proves Katok's entropy rigidity conjecture for closed connected Riemannian manifolds of
  dimension at least three with strictly negative sectional curvature: normalized Liouville measure
  maximizes entropy for the geodesic flow if and only if the metric is locally symmetric.
- **Statement**: [`preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/build/main.tex:89-100`]
  "\begin{theorem}\label{thm:main} Suppose $n\ge3$ and every sectional curvature of $g$ is strictly
  negative. Then \[ h_{m_L}(\phi_1)=\htop(\phi_1) \quad\Longleftrightarrow\quad \nabla^gR_g=0. \]
  Equivalently, equality holds precisely when the universal Riemannian cover is a rank-one symmetric
  space of noncompact type, at an arbitrary overall scale. \end{theorem}"
- **Reading**: `match`. $h_{m_L}=\htop$ is "normalized Liouville measure maximizes entropy" (the
  variational principle makes it an equality iff Liouville is the measure of maximal entropy), and
  $\nabla^gR_g=0$ is local symmetry. $n\ge3$ is "dimension at least three".

### 341 - Donaldson's hypersymplectic deformation conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Differential geometry
- **Blurb**: Proves Donaldson's hypersymplectic deformation conjecture in a cohomology-preserving
  form. Every positive triple of smooth closed two-forms on a closed connected oriented
  four-manifold, normalized by $\int\omega_i\wedge\omega_j=\delta_{ij}$, deforms through positive
  closed triples to a hyperk\"ahler triple while preserving all three cohomology classes. Any
  positive triple can first be normalized by a constant linear change.
- **Statement**: [`preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/build/sections/01-introduction.tex:11-29`]
  "\begin{theorem}\label{thm:main} Let $X$ be a closed connected oriented smooth four-manifold, and
  let $\omega=(\omega_1,\omega_2,\omega_3)$ be a smooth hypersymplectic structure normalized by
  \begin{equation}\label{eq:intro-normalization} \int_X\omega_i\wedge\omega_j=\delta_{ij}.
  \end{equation} There is a smooth family of hypersymplectic structures $\omega(t)$, $0\le t\le1$,
  such that \[ \omega(0)=\omega,\qquad [\omega_i(t)]=[\omega_i] \quad (i=1,2,3), \] and a positive
  volume form $\mu_1$ with \begin{equation}\label{eq:intro-endpoint}
  \omega_i(1)\wedge\omega_j(1)=2\delta_{ij}\mu_1. \end{equation} The endpoint forms are parallel and
  self-dual for a hyperk\"ahler metric. \end{theorem}"
- **Reading**: `match`. Cohomology preservation is $[\omega_i(t)]=[\omega_i]$, the endpoint is the
  hyperkähler triple, and the normalization is the blurb's equation. The "any positive triple can
  first be normalized" clause is the manuscript's corollary at
  `build/sections/01-introduction.tex:51-62` (`cor:individual-kahler`).

### 349 - The Solomon--Yau least-volume conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Differential geometry
- **Blurb**: Proves the Solomon--Yau least-volume conjecture for minimal hypersurfaces of round
  spheres. For every $m\ge2$, a closed connected minimal immersion into the unit sphere $S^{m+1}$
  with non-totally-geodesic image has volume at least that of the smallest minimal Clifford product,
  counting covering multiplicity.
- **Statement**: [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/introduction.tex:27-34`]
  "\begin{theorem}\label{thm:volume} Let \(m\ge2\), let \(M^m\) be a closed connected smooth
  manifold, and let \(F:M\to S^{m+1}\) be a smooth minimal immersion into the unit round sphere. If
  \(F(M)\) is not totally geodesic, then \[ \Vol\bigl(M,F^*g_{\mathrm{round}}\bigr)\ge a_m. \]
  \end{theorem}"
- **Reading**: `match`. $a_m$ is the volume of the smallest minimal Clifford product, defined
  earlier in the same introduction; "counting covering multiplicity" is carried by the theorem
  measuring the volume of the domain $M$ rather than of the image $F(M)$, which is how a covering
  enters.

### 366 - The planar Mumford--Shah regularity conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Partial differential equations
- **Blurb**: Resolves the interior regularity conjecture for reduced absolute planar Mumford--Shah
  minimizers with bounded fidelity data. Locally, the closed discontinuity set is a $C^{1,\alpha}$
  arc, a regular crack tip, or three arcs meeting at $120^\circ$; only finitely many global connected
  components meet any compact interior region.
- **Statement**: [`preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/build/sections/introduction.tex:46-63`]
  "\begin{theorem}\label{thm:main} Let $(u,K)$ be a reduced absolute minimizer of
  \eqref{eq:original-energy} in a bounded Lipschitz domain $\Omega\subset\mathbb R^2$, with
  $g\in L^\infty(\Omega)$. Every $x\in K$ has an interior neighborhood in which $K$ has one of the
  following forms, with $C^{1,\alpha}$ arcs for some $\alpha>0$: \begin{enumerate}[label=\textup{(\roman*)},nosep]
  \item a single embedded arc with $x$ in its interior; \item a single embedded arc ending at $x$;
  \item three embedded arcs meeting only at $x$, with pairwise angles $120$ degrees. \end{enumerate}
  Moreover, for every open $U\Subset\Omega$, \begin{equation}\label{eq:component-finiteness}
  \#\{C\in\pi_0(K):C\cap U\ne\varnothing\}<\infty, \end{equation} where $\pi_0(K)$ denotes the set of
  global connected components of $K$. \end{theorem}"
- **Reading**: `match`. All three local alternatives, the $120$-degree angle, the $C^{1,\alpha}$
  regularity, and the component-finiteness count are in the theorem; "bounded fidelity data" is
  $g\in L^\infty(\Omega)$.

### 368 - The three-dimensional Ball--Evans approximation problem

- **Bucket**: R | **Manuscripts**: 2 | **Discipline**: Partial differential equations
- **Blurb**: Resolves the three-dimensional Ball--Evans approximation problem: every $W^{1,p}$
  homeomorphism between arbitrary bounded domains in $\mathbb R^3$, for $1\le p<\infty$, is a strong
  $W^{1,p}$ limit of smooth diffeomorphisms onto the same target.
- **Statement**: [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/build/sections/01-introduction.tex:29-34`]
  "\begin{theorem}\label{main:theorem} Let $\Omega,\Lambda\subset\R^3$ be nonempty bounded connected
  open sets, let $1\le p\le2$, and let $f:\Omega\to\Lambda$ be a homeomorphism in
  $W^{1,p}(\Omega;\R^3)$. There exist $C^\infty$ diffeomorphisms $f_j:\Omega\to\Lambda$, each
  belonging to $W^{1,p}(\Omega;\R^3)$, such that \begin{equation}\label{main:convergence}
  \int_\Omega\bigl( |f_j-f|^p+|Df_j-Df|^p\bigr)\,dx\longrightarrow0. \end{equation} \end{theorem}"
- **Statement**: [`preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/build/sections/01-introduction.tex:25-34`]
  "\begin{theorem}\label{main:theorem}\label{ha:approximation} Let $\Omega,\Lambda\subset\R^3$ be
  bounded domains, let $2<p<\infty$, and let $f:\Omega\to\Lambda$ be a homeomorphism in
  $W^{1,p}(\Omega;\R^3)$. There exist $C^\infty$ diffeomorphisms $f_j:\Omega\to\Lambda$, each
  belonging to $W^{1,p}(\Omega;\R^3)$, such that \begin{equation}\label{main:convergence}
  \int_\Omega\bigl( |f_j-f|^p+|Df_j-Df|^p\bigr)\,dx\longrightarrow0. \end{equation} \end{theorem}"
- **Reading**: `merge`, and the range union checks: $1\le p\le2$ ∪ $2<p<\infty$ = $1\le p<\infty$,
  the blurb's range, with $p=2$ covered by the first manuscript. One scope difference between the two
  manuscripts: the first says "nonempty bounded connected open sets", the second says "bounded
  domains". The blurb's "arbitrary bounded domains" follows the second manuscript's wording.

## Promoted out of the population

Both were read in this pass as second-pass T0 families. The 2026-10-07 upstream merge gave each a
`main_results` entry, a scope note and a comparator challenge, which retiered both to T3, so the
title-named-second-pass-T0 rule no longer includes them. The entries below are the reading records as
written, with the manuscript text unchanged; a retiering does not undo a statement comparison. Their
anchors and quotations are checked exactly like the population entries. The checker requires each of
them to be title-named, outside the population, and no longer T0, and reports the count as
`promoted`.

#### 075 - The $L\log L$ Fourier-convergence conjecture

- **Bucket**: R | **Manuscripts**: 1 | **Discipline**: Real and complex analysis
- **Tier now**: T3, with a `main_results` entry, a scope note and a comparator challenge.
- **Blurb**: Proves that the ordinary symmetric Fourier partial sums of every complex-valued function
  in $L\log L(\mathbb T)$ converge almost everywhere along the full sequence. This resolves the
  classical sufficiency conjecture at the $L\log L$ scale.
- **Statement**: [`preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/sections/01-introduction.tex:17-26`]
  "\begin{theorem}[Almost-everywhere convergence in $L\log L$] \label{thm:main} For every
  complex-valued $f\in L\log L(\mathbb T)$, there is a measurable set $N_f$ of measure zero such that
  \[ \lim_{N\to\infty}S_Nf(x)=f(x) \qquad (x\in\mathbb T\setminus N_f). \] The limit is along the
  full sequence $N=0,1,2,\ldots$. \end{theorem}"
- **Reading**: `match`. Space, a.e. convergence, and the explicit "full sequence" clause are the
  blurb's three claims.

#### 195 - A counterexample to the small Cohen--Macaulay module conjecture

- **Bucket**: N | **Manuscripts**: 1 | **Discipline**: Algebra
- **Tier now**: T3, with a `main_results` entry, a scope note and a comparator challenge.
- **Blurb**: Constructs a three-dimensional complete Noetherian normal local domain over
  $\mathbb C$ with no nonzero finitely generated maximal Cohen--Macaulay module. A
  three-dimensional local domain essentially of finite type over $\mathbb C$ has the same property,
  disproving the domain form of the small Cohen--Macaulay module conjecture.
- **Statement**: [`preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/paper.tex:54-58`]
  "\begin{theorem}\label{thm:main} There exists a three-dimensional complete Noetherian normal local
  domain $R$ containing $\C$, with residue field $\C$, such that no nonzero finitely generated
  $R$-module has depth three. \end{theorem}"
- **Reading**: `match`. "No nonzero finitely generated module has depth three" is the domain form of
  "no maximal Cohen–Macaulay module" for a 3-dimensional local ring. The blurb's second clause (the
  essentially-of-finite-type example) is stated at `build/paper.tex:646-656` as `cor:affine-local`;
  the numerical obstruction its proof uses is `thm:obstruction` at `build/paper.tex:119-126`.

## Discrepancies

Four things this pass found. All are blurb-versus-manuscript scope statements, not mathematical
errors in the manuscript.

1. **171 — the blurb claims $\Theta(2^n)$, the manuscript proves $O(2^n)`.** The manuscript's only
   theorem is `R(Q_n)\le C2^n`. The matching lower bound is the trivial $R(Q_n)\ge 2^n$ and is not
   stated as a result in the manuscript. The blurb's "$\Theta(2^n)$" is therefore a claim the shipped
   manuscript does not carry as a theorem. The manuscript's own title ("The hypercube Ramsey number
   has linear order") states the upper bound only.
2. **300 — two exponents, two manuscripts.** The blurb's $O(\varepsilon^{-2})$ is the second
   manuscript's $r_\eps$; the first manuscript's bound is $\varepsilon^{-6}$ for a different
   (approximation) conclusion. A single-family blurb with one exponent invites the wrong attribution;
   record the exponent with its manuscript.
3. **038 — the blurb drops two hypotheses.** The manuscript requires $X$ **connected** and
   $n\geq 1$; the blurb says "a smooth projective complex variety $X$ of dimension $n$".
4. **346 is in the bead's priority list and not in the 43.** Its title names no conjecture, problem,
   or question, so the title rule that defines this population excludes it. A title-based named-
   conjecture screen misses results whose titles name a *theorem* instead of a conjecture — 346's
   overview merges two manuscripts and makes a sharp dimensional claim, exactly the shape the
   priority list targets.

## Not checked

- **No conjecture was identified in the literature.** Every statement above is the manuscript's claim
  compared with the release's own blurb. Whether the manuscript's theorem is the conjecture the title
  names — and whether the named conjecture is stated as the manuscript states it — is not checked,
  and this repo cannot check it.
- **No formalized statement was compared with any claim.** All 43 population families are T0: 0 of 43 have a
  `main_results` entry, 0 have a scope note, 0 have a comparator challenge. There is no Lean
  statement in this release to compare against. The two promoted families are the exception and are
  not covered by this bullet: each now carries all three, and their formalized statements were not
  read.
- **No manuscript was built, elaborated, or run.** Nothing here verifies the proofs; the pass reads
  statement text only.
- **Only the main-labelled statement of each manuscript was compared**, plus the specific companion
  statements quoted. Secondary theorems, hypotheses inside definitions, and the rest of each
  manuscript were not read.
- **The 44 remaining second-pass families** (87 − 43) have titles that name no conjecture, problem,
  or question and were not read in this pass.
- **Blurb wording was not compared with manuscript abstracts** — that comparison is
  `notes/abstracts.md`, which finds 0 of 719 identical.
- **The 43 first-pass families** were read in `notes/t0-triage.md` at claim-shape level, not at
  statement level.

## Measurements

Re-derived by `python3 notes/scripts/verify_named_conjectures.py` (report-only; it re-derives every
number below from `notes/catalog.tsv`, `notes/scripts/triage_t0.py`, and this page, and exits 1 on a
mismatch):

- `entries` 44
- `promoted` 2
- `pop_families` 43
- `pop_manuscripts` 50
- `second_families` 87
- `second_manuscripts` 114
- `first_families` 43
- `first_manuscripts` 130
- `t0_families` 130
- `t0_manuscripts` 244
- `two_pap_families` 7
- `verdict_match` 36
- `verdict_merge` 8
- `verdict_wider` 1
- `verdict_narrower` 1
- `priority_in_pop` 7
- `priority_outside_pop` 1
- `anchors` 59
- `citations` 10
- `bucket_R` 24
- `bucket_N` 8
- `bucket_B` 5
- `bucket_U` 4
- `bucket_K` 2
- `disciplines` Algebraic and complex geometry=10, Topology=8, Algebra=5, Differential geometry=5, Combinatorics=3, Partial differential equations=3, Real and complex analysis=3, Convex and metric geometry=1, Dynamical systems and ergodic theory=1, Group theory=1, Operator algebras=1, Probability and statistical mechanics=1, Theoretical computer science=1
