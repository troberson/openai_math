[Notes](../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 344](../index/differential-geometry/344-metric-blaschke-conjecture.md)

# 344 — The metric Blaschke conjecture

[Index page](../index/differential-geometry/344-metric-blaschke-conjecture.md)

## Original CONTENTS.md summary

The release's blurb for family 344 

> **344. The metric Blaschke conjecture.** Proves the metric Blaschke conjecture: every closed connected Riemannian manifold of positive dimension whose injectivity radius equals its diameter is, up to scaling, a standard compact rank-one symmetric space. [S1:8340]

The catalog abstract in `overview.tex` [S2:786] is the same sentence. The manuscript's own abstract 

> We prove the metric Blaschke conjecture: every connected closed smooth Riemannian manifold of positive dimension whose global injectivity radius equals its diameter is, up to scale, a standard compact rank-one symmetric space. [S6:2–5]

The bibtex key the release ships [S3:9–12]:

> @misc{OAI:The-metric-Blaschke-theorem-September-23-2026,
>   author = {{OpenAI}},
>   title = {{The metric Blaschke theorem}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

The conjecture starts from a property the round sphere has, and that the standard projective spaces and the Cayley plane also have 

> On a round sphere, every geodesic minimizes from its starting point to the antipode, at a distance equal to the diameter. The standard real, complex and quaternionic projective spaces and the Cayley plane have the same common minimizing-distance property. The metric Blaschke conjecture asks whether this property characterizes these compact rank-one symmetric spaces. [S6:11–16]

The manuscript turns the property into a metric equality. For a connected closed smooth Riemannian manifold, the global injectivity radius is the infimum over points of the radius on whose open tangent balls the exponential map is a diffeomorphism, and the diameter is the largest distance between two points. A Blaschke manifold is one of positive dimension where the two are equal 

> For a connected closed smooth Riemannian manifold $(M,g)$, write \[ \mathrminj(M,g)=\inf_{p\in M}\mathrminj_p(M,g), \qquad \mathrmdiam(M,g)=\sup_{p,q\in M}d_g(p,q). \] Here $\mathrm{inj}_p(M,g)$ is the supremum of the radii on whose open tangent balls $\exp_p$ is a diffeomorphism onto its image. We call $M$ a _Blaschke manifold_ if it has positive dimension and $\mathrm{inj}(M,g)=\mathrm{diam}(M,g)$. The global equality implies that every unit-speed geodesic minimizes precisely up to the common diameter; we give the short deduction in Lemma  . [S6:18–29]

The main theorem is the classification 

> **theorem**
 [S6:31–37]

The proof is a volume argument in two directions. Every Blaschke manifold has volume at least its model's, and the quaternionic cases have volume at most their model's; the two bounds meet at the model, so equality forces isometry [S6:104–116]:

> \begin{theorem}[Sharp volume comparison]\label{thm:comparison}
> Every Blaschke manifold and its model at the same diameter satisfy
> \[
>  \Vol(M,g)\ge\Vol(M_0,g_0).
> \]
> Equality holds if and only if $(M,g)$ is isometric to $(M_0,g_0)$.
> \end{theorem}
>
> \begin{corollary}[Reduction to an upper volume bound]
> \label{thm:volume-reduction}
> If a Blaschke manifold has volume at most that of its model at the
> same diameter, then it is isometric to that model.
> \end{corollary}

The classification covers every quaternionic dimension, and the hypothesis is the global equality, not a curvature bound 

> The classification includes every quaternionic dimension. Its hypothesis is the global equality just defined. Classical Blaschke structure associates to $M$ a compact rank-one symmetric _model_ $M_0$ by its cut-locus and integral cohomology type. Throughout the volume comparisons, the standard metric $g_0$ on $M_0$ is scaled to have the same diameter as $(M,g)$. Prime geodesics have length twice the diameter, so fixing the diameter is equivalent to fixing their prime period. [S6:39–46]

## Graduate summary

The geometric input is the cut-time lemma, which turns the global equality into a pointwise statement: every geodesic is minimizing exactly up to the diameter, the cut locus of every point is the sphere at that distance, and the exponential map is a diffeomorphism on the open ball of that radius [S7:4–9]. Classical Blaschke structure then fixes the model: the prime geodesics form a locally trivial circle bundle over $M$ with fibre length twice the diameter, the cut locus of every point is a sphere, and the cohomology type is one of the compact rank-one symmetric models [S7:34–50].

The analytic comparison begins on one closed geodesic. The Lagrangian planes $L_x$ and $L_y$ of normal Jacobi fields give the determinant $f(x,y)$ as the absolute symplectic pairing of two orthonormal frames; where the plane is a graph over the initial coordinates, the same determinant is a quotient of the difference of the graph matrix by the square root of the product of its derivatives [S8:112–146]:

> \begin{proposition}[Jacobi determinant normalization]
> \label{lag:determinant}
> Choose $G_x$- and $G_y$-orthonormal frames
> $Z_x=(Z_{x,1},\ldots,Z_{x,d})$ and
> $Z_y=(Z_{y,1},\ldots,Z_{y,d})$ of $L_x$ and $L_y$.  Then
> \begin{equation}
>  f(x,y)=\left|\det\bigl(\omega(Z_{x,a},Z_{y,b})\bigr)_{a,b=1}^d\right|
>  \label{eq:lag-f}
> \end{equation}
> is independent of these choices.  It is continuous, symmetric in its
> arguments, and separately $T$-periodic.  It is the absolute normal
> Jacobi determinant at $y$ of fields vanishing at $x$ with orthonormal
> initial derivatives there.  In particular, for $0<y-x<D$ it is the
> polar volume density with respect to $dt$ and ordinary sphere area at
> $\gamma(x)$.
>
> Use the same orthonormal basis of $\dot\gamma(0)^\perp$ for the
> coordinates
> \[
>  (q,p)=(J(0),J'(0))\in\R^d\oplus\R^d,
> \]
> choosing its first $k$ vectors to be the initial derivatives of a basis
> of $L_0\cap L_D$.  On
> \[
>  \mathcal I=(0,D)\cup(D,T)
> \]
> there is a smooth symmetric matrix $A(t)$ such that
> $L_t=\{(q,A(t)q):q\in\mathbb R^d\}$, and $A'(t)>0$.  For $x,y\in\mathcal I$,
> \begin{equation}
>  f(x,y)=
>  \frac{|\det(A(y)-A(x))|}
>  {\sqrt{\det A'(x)\det A'(y)}}.
>  \label{eq:lag-graph-determinant}
> \end{equation}
> \end{proposition}

The Schur factorization splits the determinant into a regular factor and a Schur-complement factor, and the Schur factor is bounded below by integrals of the curvature matrix, uniformly over all four endpoint shifts [S8:419–448]:

> \begin{proposition}[Two Schur-complement bounds]
> \label{lag:schur}
> The matrix $Q(x,y)$ is symmetric and satisfies
> \begin{equation}
>  \det(\Delta A)=\det(\Delta H)\det Q(x,y),\qquad
>  Q(y,x)=-Q(x,y).
>  \label{eq:lag-Schur-factorization}
> \end{equation}
> It extends continuously by zero to $y=x\in\mathcal I$, and
> \begin{equation}
>  Q(u,u+D)=Q(u+D,u)=0\qquad(0<u<D).
>  \label{eq:lag-Q-zeros}
> \end{equation}
> Whenever its distinct endpoints remain in $\mathcal I$, it obeys the
> positive-semidefinite matrix inequalities
> \begin{equation}
>  \partial_yQ(x,y)\ge S(y),\qquad
>  -\partial_xQ(x,y)\ge S(x).
>  \label{eq:lag-Q-derivatives}
> \end{equation}
> Consequently, for every $0<u<v<D$ and $i,j\in\{0,1\}$,
> \begin{align}
>  Q(u+iD,v+jD)&\ge\int_u^v S(t+jD)\,dt,
>  \label{eq:lag-Q-bound-j}\\
>  Q(u+iD,v+jD)&\ge\int_u^v S(t+iD)\,dt.
>  \label{eq:lag-Q-bound-i}
> \end{align}
> In particular, this $Q$ is positive definite for all four choices of
> $i,j$, including $i=1,j=0$.
> \end{proposition}

The scalar estimate is a weighted integral inequality against the model density. Relative to $p_0$, the weighted average of the log-interval-average, minus the mean of the endpoint values, is nonnegative; the symmetry of the weight is what makes the endpoint terms cancel [S9:25–48]:

> \begin{lemma}[Weighted scalar identity]\label{weighted:scalar}
> Let $b>0$, $\lambda=\pi/b$, and
> \[
>  p_0(t)=\frac{\lambda^2}{\sin^2(\lambda t)},\qquad 0<t<b.
> \]
> Let $p:(0,b)\to(0,\infty)$ be continuous and suppose that
> $g=\log(p/p_0)$ is bounded.  Let $W$ be nonnegative and measurable on
> $(0,b)$, with $W(b-z)=W(z)$ almost everywhere and
> $W(z)/\sin(\lambda z)$ essentially bounded.  Write
> \[
>  \Delta_b=\{(x,y):0<x<y<b\},\qquad
>  d\nu_{xy}(t)=\frac{p_0(t)\,dt}{\int_x^y p_0},\quad x<t<y.
> \]
> Then all the following integrals are finite, and
> \begin{align}
>  &\int_{\Delta_b}W(y-x)
>  \left[\log\frac{\int_x^y p}{\int_x^y p_0}
>        -\frac{g(x)+g(y)}2\right]dx\,dy \notag\\
>  &\qquad=\int_{\Delta_b}W(y-x)
>  \left[\log\int_x^y e^{g(t)}\,d\nu_{xy}(t)
>        -\int_x^y g(t)\,d\nu_{xy}(t)\right]dx\,dy
>  \ \geq\ 0.\label{weighted:scalar-identity}
> \end{align}
> \end{lemma}

The comparison on each geodesic is the integral inequality over the square of two times along the geodesic 

> **theorem**
 [S9:126–143]

Integrating the radial density over the unit tangent bundle at each point gives the volume 

> **lemma**
 [S10:20–28]

The quaternionic upper bound comes from characteristic classes. Pairs of points at the cut distance form a smooth incidence manifold, and the rank of the complement of two direction planes forces the total Pontryagin class [S11:175–183]:

> \begin{theorem}\label{inc:pontryagin}
> The total Pontryagin class of $M$ is
> \begin{equation}\label{inc:pontryagin-formula}
>  p(TM)=\frac{(1+2su+u^2)^{r+1}}{1+4su}
>  \quad\text{in }H^*(M;\mathbb Q).
> \end{equation}
> The quotient means its power-series expansion truncated by
> $u^{r+1}=0$.
> \end{theorem}

The signature estimate fixes the sign of the coefficient [S12:9–13]:

> \begin{theorem}\label{sig:coefficient}
> In Proposition~\ref{inc:normal}, $|s|=1$. In particular, the
> actual tautological four-plane bundle of every tangent great-sphere
> fibration at a point of $M$ satisfies $p_1=\pm2e$.
> \end{theorem}

The geodesic space carries the arithmetic. The period-normalized contact form expresses volume as the top power of the Euler class of the geodesic-circle bundle, and the model's characteristic number is a binomial coefficient [S13:61–72]:

> \begin{proposition}[Contact volume]\label{geo:contact}
> With this orientation and Euler class,
> \begin{equation}\label{geo:contact-formula}
>  N:=\int_B e^{4r-1}
>    =\frac{(4r-1)!\,|S^{4r-1}|\,\Vol(M)}{T^{4r}}>0.
> \end{equation}
> For the standard quaternionic model at the same diameter, this
> number is
> \begin{equation}\label{geo:model-number}
>  N_0=\frac{1}{2r+1}\binom{4r}{2r}.
> \end{equation}
> \end{proposition}

The first negative bundle of the free-loop energy transfers the incidence coefficient to the geodesic space 

> **proposition**
 [S13:265–300]

The complete-intersection calculation turns the characteristic number into the sharp upper bound [S14:351–361]:

> \begin{theorem}
> \label{alg:upper}
> For a quaternionic-type Blaschke manifold of dimension $4r$, $r\ge2$,
> the contact characteristic number of Proposition~\ref{geo:contact}
> satisfies
> \begin{equation}
>  N=\int_{B}e^{4r-1}
>  \le \frac1{2r+1}\binom{4r}{2r}.
>  \label{alg:sharp-upper}
> \end{equation}
> \end{theorem}

Complex-projective type closes through Yang's volume theorem [S15:11–14]:

> \begin{corollary}[Complex-projective type]\label{rig:complex}
> A Blaschke manifold of complex-projective type is isometric
> to its equally scaled standard complex projective model.
> \end{corollary}

The projective planes close through the classification of smooth topological projective planes and the weak Blaschke volume theorem 

> **corollary**
 [S15:37–40]

Quaternionic type closes through the sharp bound and the contact formula [S15:59–62]:

> \begin{corollary}[Quaternionic type]\label{rig:quaternionic}
> A Blaschke manifold of quaternionic type is isometric to its
> standard quaternionic model at the same diameter.
> \end{corollary}

The manuscript states the route through the proof 

> After the circle, sphere and real-projective cases are separated, the analytic comparison in each remaining type starts along one closed geodesic. Normal Jacobi fields that vanish at a specified time form a Lagrangian plane in the symplectic space of Jacobi fields. A fixed graph chart separates the determinant of their endpoint pairing into a regular factor and a Schur-complement factor. The size of the Schur block is the dimension of the space of normal Jacobi fields vanishing at both the starting point and its cut point; the regular block has the complementary normal dimension. Both determinant factors can be bounded by scalar interval integrals, including when the actual endpoint order is reversed. This construction uses the cut-time intersection pattern; it does not require parallel eigenspaces of the curvature operator. [S6:118–130]

The arithmetic step is where the integral structure matters 

> Next consider the space of oriented geodesics, forgetting the marked starting point. The period-normalized contact form expresses volume as a top power of the Euler class of its geodesic-circle bundle. Integral Gysin sequences first determine the lattice of classes and the determinant of a middle pairing. The first negative bundle of the free-loop energy transfers the incidence coefficient to this space. This step uses the fixed-endpoint Morse index theorem of   and the equivariant negative-bundle attachment developed in closed-geodesic Morse theory; we use the formulation of \citet[Section 7]OttosenBokstedt2007, following  . The required primitive attaching coefficient is established over every prime field. The attaching map from the sphere bundle of the descended negative bundle to $M$ also pulls back its cohomology generator; the vanishing of the $(r+1)$st power supplies the relations for the final algebraic calculation. Finally, a complete-intersection calculation turns the middle determinant into the sharp upper volume bound. Rational cohomology alone would not retain the arithmetic that normalizes this bound. [S6:160–179]

## History of the conjecture

Blaschke posed the question for surfaces in 1921 [S16:92–102], and Green settled the surface case in 1963 [S16:204–214]. Besse's 1978 book carries the geometric formulation and the connection to closed geodesics, smooth cut loci, and fibrations of tangent spheres by great spheres; the topological restrictions of Bott and Samelson explain why the compact rank-one symmetric models appear [S6:50–59] [S16:1–11]. McKay's 2016 corrected account is the manuscript's reference for the development [S16:13–22].

The sphere and real-projective metric cases came through Berger, Kazdan, Weinstein and Yang. Berger's sphere argument combines the geometric volume problem with Kazdan's scalar integral inequality, and Berger's sharp isoembolic inequality uses a weighted comparison of Jacobi determinants and Jensen's inequality [S6:61–70] [S16:104–114] [S16:190–202]. Yang proved that a Blaschke manifold of complex projective homotopy type has the model volume at the same prime geodesic period [S6:82–84] [S16:24–33]. For the projective planes, smooth incidence geometry and the classification of Kramer–Stolz identify the point manifold diffeomorphically [S6:85–87] [S16:116–126]. Wilking records the equal-volume theorem for a manifold homeomorphic to a compact rank-one symmetric space whose unit geodesics all have the same least period, attributing it to Reznikov [S6:87–90] [S16:128–138]; Reznikov's earlier work on the quaternionic weak Blaschke conjecture is another predecessor [S6:90–93] [S16:35–45]. Szabo's classification of compact simply connected harmonic manifolds supplies the equality case [S6:145–147] [S16:59–69] [S16:71–80].

The manuscript names the hypotheses it does not use 

> There are also rigidity theorems with additional geometric hypotheses. Shankar, Spatzier and Wilking treat an upper sectional-curvature bound \citep[Proposition 2.1]ShankarSpatzierWilking2005, and Su, Sun and Wang prove the corresponding normalized lower-curvature result  . Connell, Islam, Nguyen and Spatzier obtain rigidity under curvature bounds and agreement with a model away from a prescribed convex set  . [S6:192–198]

It also names the nearest concurrent result 

> Song's September 2026 preprint proves Blaschke metric rigidity assuming an adapted complex structure on the entire tangent bundle \citep[Theorem 1.3]Song2026. This entire-extension hypothesis is additional to the Blaschke condition. [S6:200–203]

The entries are Shankar–Spatzier–Wilking 2005 [S16:309–319], Su–Sun–Wang 2016 [S16:331–341], Connell–Islam–Nguyen–Spatzier 2026 [S16:343–352], and Song 2026 [S16:354–361].

**Prior (my training data, not this repo).** The metric Blaschke conjecture is the conjecture that a Riemannian manifold whose injectivity radius equals its diameter is a compact rank-one symmetric space. The surface case is classical, and the higher-dimensional cases were open: the sphere case was settled by Berger's isoembolic inequality route, the complex projective case by Yang under a homotopy-type hypothesis, and the quaternionic cases by Reznikov and Wilking under homeomorphism and period hypotheses. The full metric classification, including every quaternionic dimension, is what I recall as open. The prior is a training-data recollection at an early-2025 cutoff, self-rated, and the repo supplies only the manuscript's citations.

## Consequences

The direct consequence is the classification the release states: the Blaschke condition characterizes the round sphere, the standard real, complex and quaternionic projective spaces, and the Cayley plane, up to scaling [S1:8340] [S2:786]. The manuscript's own statement covers every quaternionic dimension [S6:39–46], which is the part the earlier projective results did not reach.

The method has a consequence of its own. The quaternionic upper bound is proved from the manuscript's own incidence geometry, Pontryagin-class calculation, and integral Gysin sequences, not from a homeomorphism or homotopy-type hypothesis [S6:95–97] [S11:175–183] [S13:265–300]. The manuscript states that rational cohomology alone would not retain the arithmetic that normalizes the bound [S6:178–179].

The equality case is the other consequence: equality in the volume comparison forces metric isometry, not just volume equality [S6:104–110]. The lower bound is proved for every model type, so the reduction to an upper bound is a corollary, not a separate theorem [S6:112–116].

Inside the release, this family has no formalization. The ledger records tier T0, `paps_form` 0, `chal` 0, `mainres` 0, `scope_note` 0, `verification` 0, `inputs` 0, `covmd` 0, and no trace [S17:340]. The claim-shape column is `resolution` and the broad counterexample flag is 0. Nothing in `lean/` states the theorem, so no Lean or comparator run can confirm any part of it; the whole proof is manuscript mathematics.

What has not been checked: no Lean, lake, or comparator run was performed, and for this family there is nothing in the release to run; the ten section files were read at the statement level, not line by line across 3,197 lines, so a proof step inside `02-lagrangian.tex`, `07-geodesic-space.tex`, or `08-volume-algebra.tex` can be mis-stated here, and the statements quoted above are the manuscript's own captions, not proofs I verified; the section files' assumptions were not reconciled against the introduction's summary; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 17 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | Release blurb, manuscript link, manuscript abstract |
| S2 | [`overview.tex`](../../overview.tex) | 859 | Family 344's `\resultentry`, at line 786 |
| S3 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/README.md`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/README.md) | 16 | Manuscript README and bibtex key |
| S4 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf) | 16839 | Manuscript PDF |
| S5 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/paper.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/paper.tex) | 68 | Preamble, theorem environments, section include list |
| S6 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/00-introduction.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/00-introduction.tex) | 203 | Abstract, Blaschke definition, main theorem, predecessors, proof route |
| S7 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/01-geometric-inputs.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/01-geometric-inputs.tex) | 114 | Cut-time lemma, classical Blaschke structure |
| S8 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/02-lagrangian.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/02-lagrangian.tex) | 657 | Lagrangian setup, determinant normalization, Schur-complement bounds |
| S9 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/03-weighted-comparison.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/03-weighted-comparison.tex) | 334 | Weighted scalar identity, geodesic comparison |
| S10 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/04-global-comparison.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/04-global-comparison.tex) | 112 | Polar integration over a full period |
| S11 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/05-incidence.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/05-incidence.tex) | 273 | Incidence manifold, total Pontryagin class |
| S12 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/06-signature.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/06-signature.tex) | 200 | The signature coefficient and the sign of $s$ |
| S13 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/07-geodesic-space.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/07-geodesic-space.tex) | 768 | Contact volume, Gysin sequences, negative-bundle attachment |
| S14 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/08-volume-algebra.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/08-volume-algebra.tex) | 442 | Complete-intersection calculation, sharp upper bound |
| S15 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/09-classification.tex`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/sections/09-classification.tex) | 94 | The three rigidity corollaries |
| S16 | [`preprints/The-metric-Blaschke-theorem-September-23-2026/build/references.bib`](../../preprints/The-metric-Blaschke-theorem-September-23-2026/build/references.bib) | 369 | Bibliography |
| S17 | [`notes/gen/tables/catalog.tsv`](../../notes/gen/tables/catalog.tsv) | 373 | Reading ledger row for family 344 |

## Bibliography

- Berger, Marcel, Une borne inférieure pour le volume d'une variété riemannienne en fonction du rayon d'injectivité (1980)
- Berger, Marcel, Blaschke's Conjecture for Spheres (1978)
- Besse, Arthur L., Manifolds all of whose Geodesics are Closed (1978)
- Blaschke, Wilhelm, Vorlesungen über Differentialgeometrie und geometrische Grundlagen von Einsteins Relativitätstheorie. I: Elementare Differentialgeometrie (1921)
- Boyd, Stephen, Vandenberghe, Lieven, Convex Optimization (2004)
- Connell, Chris, Islam, Mitul, Nguyen, Thang, Spatzier, Ralf, Rigidity of compact rank one symmetric spaces (2026)
- Duistermaat, J. J., On the Morse index in variational calculus (1976)
- Green, Leon W., Auf Wiedersehensflächen (1963)
- Hatcher, Allen, Algebraic Topology (2002)
- Huneke, Craig, Hyman Bass and ubiquity: Gorenstein rings (1999)
- Kazdan, Jerry L., An Inequality Arising in Geometry (1978)
- Klingenberg, Wilhelm, Lectures on Closed Geodesics (1978)
- Kramer, Linus, Stolz, Stephan, A diffeomorphism classification of manifolds which are like projective planes (2007)
- Bökstedt, Marcel, Ottosen, Iver, String cohomology groups of complex projective spaces (2006)
- McKay, Benjamin, Summary of progress on the Blaschke conjecture (2016)
- Milnor, John W., Stasheff, James D., Characteristic Classes (1974)
- Milnor, John, Morse Theory (1963)
- Moore, John Douglas, Lecture Notes on Seiberg–Witten Invariants (2010)
- Ottosen, Iver, Bökstedt, Marcel, String cohomology groups of complex projective spaces (2007)
- Álvarez Paiva, Juan-Carlos, Asymmetry in Hilbert's fourth problem (2013)
- Reznikov, Alexander G., The weak Blaschke conjecture for $\mathbf{H}P^n$ (1985)
- Reznikov, Alexander G., The weak Blaschke conjecture for $\mathbf{C}P^n$ (1994)
- Rovenskii, Vladimir Y., Toponogov, Victor A., Great sphere foliations and manifolds with curvature bounded above (1996)
- Shankar, Krishnan, Spatzier, Ralf, Wilking, Burkhard, Spherical rank rigidity and Blaschke manifolds (2005)
- Song, Kyobeom, Blaschke conjecture and complex geometry (2026)
- Su, Xiaole, Sun, Hongwei, Wang, Yusheng, On Blaschke's conjecture (2016)
- Weinstein, Alan, On the volume of manifolds all of whose geodesics are closed (1974)
- Wilking, Burkhard, Index parity of closed geodesics and rigidity of Hopf fibrations (2001)
- Yang, Chung-Tao, Any Blaschke manifold of the homotopy type of $\mathbf{C}P^n$ has the right volume (1991)
- Zelditch, Steve, Eigenfunctions of the Laplacian of Riemannian manifolds (2017)
- Szabó, Zoltán I., The Lichnerowicz conjecture on harmonic manifolds (1990)
- Szabó, Zoltán I., Harmonic manifolds; the proof of the Lichnerowicz conjecture in the compact case (1988)
