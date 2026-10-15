# 345 — Infinitely many closed geodesics on spheres and three-manifolds (Differential geometry, 1 manuscript, tier T0)

Manuscript root: `preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026` [S4]. The manuscript is dated September 24, 2026 [S3:5] and ships `build/paper.tex` [S5], eleven section files [S6–S16], and `build/references.bib` [S17]. The README carries no version note, so this is the release's first and only edition [S3:1–17]. The family is at tier T0: the release formalizes none of its manuscript, and ships no scope note, comparator challenge, `main_results` entry, verification bundle, or reasoning trace [S18:341].

## Original CONTENTS.md summary

The release's blurb for family 345 [S1:8356]:

> **345. Infinitely many closed geodesics on Riemannian spheres and closed three-manifolds.** Proves that every smooth Riemannian metric on Sn, n ≥ 2, has infinitely many prime closed geodesics with pairwise distinct images. The same conclusion holds on every closed manifold admitting a finite smooth spherical cover and on every closed three-manifold, without orientability or nondegeneracy restrictions.

The catalog abstract in `overview.tex` [S2:788] is the same sentence. The release's abstract for the manuscript [S1:8365]:

> We resolve the sphere case of the closed-geodesic infinitude problem: every smooth Riemannian metric on the standard sphere Sn, n ≥ 2, has infinitely many prime closed geodesics with pairwise distinct images. The two-sphere case is classical; the result in higher dimensions includes degenerate metrics. Using finite covers and theorems of Perelman and Rademacher–Taimanov, we also obtain the same conclusion for every smooth Riemannian metric on a nonempty closed smooth three-manifold.

The bibtex key the release ships [S3:10–13]:

> @misc{OAI:Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026,
>   author = {{OpenAI}},
>   title = {{Infinitely many closed geodesic images on every Riemannian sphere}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

A prime closed geodesic is a closed geodesic that is not an iterate of a shorter one, and its image is the set of points it traces. Counting images is the point: iterates of one prime geodesic share one image, so infinitely many prime images is a statement about distinct geometric curves, not about parametrized loops.

The main theorem is the sphere case [S6:11–15]:

> \begin{theorem}\label{thm:spheres}
> For every integer $n\ge2$ and every smooth Riemannian metric on the standard
> smooth sphere $S^n$, there are infinitely many prime closed geodesics with
> pairwise different images.
> \end{theorem}

The proof runs by contradiction, assuming finitely many prime images [S6:115–121]:

> Assume that a metric on $S^n$, $n\ge3$, has only finitely many prime geodesic
> images. Every nonconstant critical loop is then an iterate of one of finitely many
> oriented trajectories. Their local homology has uniformly bounded rank and
> lies near finitely many lines relating index to length. The difficulty is
> that sublevel homology can also contain classes that disappear at a later
> level. We first control these temporary classes and then use the symmetry
> of double loops to obtain a contradiction.

The first corollary descends along a finite cover, and it reaches the spherical space forms [S6:67–71] [S6:73]:

> \begin{corollary}\label{cor:finite-cover}
> Let $N$ be a closed manifold admitting a finite smooth cover diffeomorphic to
> a standard sphere $S^n$, where $n\ge2$. Every smooth Riemannian metric on $N$
> has infinitely many geometrically distinct prime closed geodesics.
> \end{corollary}

The corollary covers the spherical space forms [S6:73]:

> This includes real projective spaces and smooth spherical space forms.

The second corollary settles dimension three, using geometrization for the finite-fundamental-group case [S6:84–88]:

> \begin{corollary}[Closed three-manifolds]\label{cor:three-manifolds}
> Let $M$ be a nonempty closed smooth three-manifold, not necessarily orientable.
> Every smooth Riemannian metric on $M$ has infinitely many prime closed
> geodesics with pairwise distinct images.
> \end{corollary}

The proof splits on the fundamental group [S6:91–98]:

> It suffices to work on one connected component, so assume that $M$ is
> connected. If $\pi_1(M)$ is infinite, Rademacher and Taimanov
> \cite[Theorem~2]{RademacherTaimanov2018} give infinitely many geometrically
> distinct closed geodesics for the given metric. Their Riemannian convention
> identifies geodesics exactly when their images coincide
> \cite[Section~3]{RademacherTaimanov2018}. Taking the least positive period
> gives a prime representative with the same image. Their theorem includes
> the nonorientable case.

The corollary carries no length count in the finite case [S6:109–111]:

> This corollary uses only the infinitude conclusion from Rademacher--Taimanov.
> It carries no quantitative length-counting assertion for the
> finite-fundamental-group case.

## Graduate summary

The setting is the loop space. The energy is the integral of the squared speed, its square root is the $L^2$-norm of the velocity, and the length is the integral of the speed; the two sublevels are the loops with energy below a cut and the loops with length below the same cut [S7:10–21]:

> The energy, its square root, and length are
> \[
>  E(\gamma)=\int_0^1|\dot\gamma(t)|_g^2\dd t,
>  \qquad F(\gamma)=\sqrt{E(\gamma)},
>  \qquad \ell(\gamma)=\int_0^1|\dot\gamma(t)|_g\dd t.
> \]
> Then $\ell\le F$, with equality for constant-speed loops. Write
> \[
>  X_a=\{F<a\},\qquad \mathcal A_a=\{\ell<a\}\qquad(a\in\mathbb R).
> \]
> Both spaces are empty for $a\le0$; pairs relative to $M$ are used only
> for $a>0$.

The symmetry groups are the reflection and the half-translation, generating the Klein four-group [S7:28–36]:

> The orthogonal group $G=O(2)$ acts by changing the loop parameter. We single
> out reflection $r$ and half-translation $\tau$:
> \[
>  (r\gamma)(t)=\gamma(-t),\qquad
>  (\tau\gamma)(t)=\gamma(t+\tfrac12),\qquad
>  R=\langle r\rangle,\quad K=\langle r,\tau\rangle.
> \]
> Thus $K\cong C_2\times C_2$. The fixed locus of $\tau$ consists of double
> loops. The map

The analytic foundation is the Palais–Smale theory of the energy on the loop space [S9:14–20]:

> \begin{lemma}[Analytic foundations]\label{lem:local-analytic}
> The energy \(E\) is smooth on \(\Lambda=H^1(S^1,S^n)\), satisfies the
> Palais--Smale condition, and has precisely the smooth closed geodesics
> and the constants as critical points.  There is a complete strong
> Riemannian metric on \(\Lambda\), invariant under \(G=O(2)\), for which
> a bounded normalized negative gradient of \(E\) has a complete
> equivariant flow.  Sufficiently small energy sublevels retract

The counting lemma is what turns a homological statement into a count of images [S9:185–190]:

> \begin{lemma}[Counting prime images]\label{lem:local-prime-images}
> On any smooth Riemannian manifold, every nonconstant closed geodesic
> is an iterate of a prime geodesic.
> Two prime geodesics with the same image differ by phase and possibly
> reversal.  Reversal never preserves an oriented phase orbit.
> \end{lemma}

The local control theorem is the crossing analysis at a critical level, under the finite-prime assumption [S9:394–400]:

> \begin{theorem}[Uniform local control]\label{thm:local-control}
> Assume there are finitely many prime images.  There are constants
> \(A,B<\infty\) such that every sufficiently tight crossing of a
> positive critical level has the following properties.
> \begin{enumerate}[label=\textup{(\roman*)}]
> \item It decomposes into unoriented labels \((i,m)\) at that
> level.  Let \(\mathcal P_{i,m}\) be the ordinary pair for one

The ordinary death theorem is the uniform filling statement: a cycle below square-root energy $a$ that bounds in the full loop space already bounds below $a+D$ [S8:8–14] [S6:123–128]:

> \begin{theorem}[Uniform ordinary death]\label{thm:ordinary-death}
> For every smooth Riemannian metric on $S^n$, $n\ge3$, there is a constant
> $D>0$ such that, for every integer $j\ge0$ and every real $a>0$,
> \begin{align}
>  \ker\bigl(H_j(X_a)\longrightarrow H_j(\Lambda)\bigr)
>  &\subseteq
>  \ker\bigl(H_j(X_a)\longrightarrow H_j(X_{a+D})\bigr),

The introduction states the same input in prose [S6:123–128]:

> The ordinary homological input is a uniform filling statement for every
> metric, independent of the finite-prime assumption. Square-root energy
> is the $L^2$-norm of the velocity of a period-one loop.
> There is a constant $D$ such that a cycle below square-root energy $a$
> which bounds in the full loop space already bounds below $a+D$,
> in every degree (Theorem~\ref{thm:ordinary-death}).

The fixed-degree filling proposition is the degree-dependent version that the cut operation lowers into a fixed range [S14:351–356]:

> \begin{proposition}[Fixed-degree filling]\label{prop:fixed-degree-death}
> Let $M$ be compact and simply connected.  For every integer $j\ge0$
> there is $D_j>0$ such that, for every real $a>0$, each finite $j$-cycle
> in $\mathcal A_a$ which is null-homologous in $\Lambda$ bounds a finite
> chain in $\mathcal A_{a+D_j}$.
> \end{proposition}

The resonance proposition bounds how far the length of a homology class sits from a linear function of its degree [S12:24–30]:

> \begin{proposition}[Sphere powers and resonance]\label{prop:sphere-powers}
> There are constants $\alpha>0$ and $C_H$ depending on $g$ such that
> \begin{equation}\label{eq:cj-resonance}
>  \bigl|k-\alpha\operatorname{cr}(z)\bigr|\le C_H
> \end{equation}
> for every nonzero homogeneous ordinary homology or cohomology class $z$
> of degree $k$.  For homology, $\operatorname{cr}$ is the infimum of the

The filtered cut–join identity is the essential comparison [S12:303–310] [S6:151–158]:

> \begin{theorem}[Filtered interchange]\label{thm:filtered-interchange}
> Let $T$ be a normalized cocycle of degree $p\ge1$ vanishing on
> $\mathcal A_L$, where $L>0$, and put $q=n+p-1$.  Let $x$ and $y$ be
> arbitrary absolute cycles of respective degrees $j,N$ with
> \[
>  j>n+p,\qquad N>n+p,
> \]
> supported in $\mathcal A_a$ and $\mathcal A_b$.

The introduction names the same comparison as the essential step [S6:151–158]:

> The essential comparison is the filtered cut--join identity of
> Theorem~\ref{thm:filtered-interchange}. Its chain constructions build on
> the string-topology models of Hingston and Wahl~\cite{HingstonWahl2023}.
> The comparison uses an absolute cut with a diagonal-relative Thom cocycle;
> its value on a suitable power is the constant-loop fundamental class,
> the unit for the loop product (Proposition~\ref{prop:absolute-unit}).
> We prove both the identity and this unit statement, including their
> filtration bounds.

The absolute unit proposition says the cut of the power is the constant-loop fundamental class [S12:560–566]:

> \begin{proposition}[The cut of the power is the absolute unit]
> \label{prop:absolute-unit}
> For the choices $S,T,l,L$ in \eqref{eq:cj-thresholds},
> \begin{equation}\label{eq:cj-absolute-unit}
>  [D_TS]=[M]\quad\text{in }H_n(\Lambda).
> \end{equation}
> Moreover $D_TS$ is supported in $\mathcal A_{l-L+1}$, and there is a

The transient count $T(a)$ is the number of extra reflection classes at a sublevel, and it is uniformly bounded under the finite-prime assumption [S6:160–176] [S13:29–35]:

> The remaining argument uses reflection of loops and translation by half a
> period. With coefficients in $\mathbb F_2$, let $B_a$ denote
> reflection-equivariant cohomology below
> square-root energy $a$, relative to constant loops, and let $B_\infty$
> denote the corresponding global group. Define
> \[
>  T(a)=\dim\coker(B_\infty\longrightarrow B_a),
> \]
> where the dimension is summed over all degrees. Thus $T(a)$ counts the
> extra reflection classes at that sublevel. Theorem~\ref{thm:bounded-transients}
> shows that $T(a)$ is uniformly bounded under the finite-prime assumption.
> The proof compares two filtrations on the half-translation fixed locus:
> the actual equivariant degree and the degree of its half-length root.
> An exact-sequence calculation bounds their total discrepancy by $O(a)$
> (Theorem~\ref{thm:finite-cut-budget}). A long string of extra classes would
> give $\Omega(a^2)$ discrepancy. The ordinary filling estimate excludes the
> remaining possibilities.

The transient bound is the theorem that closes the count [S13:29–35]:

> \begin{theorem}[Bounded total transients]\label{thm:bounded-transients}
> Under the finite-prime-image assumption, there is a constant $C$,
> independent of the positive regular cut $a$, such that
> \begin{equation}\label{trans:total-bound}
>  T(a)\le C.
> \end{equation}
> \end{theorem}

The finite-cut defect bound is the $O(a)$ discrepancy [S11:149–154]:

> \begin{theorem}[Finite-cut defect bound]\label{thm:finite-cut-budget}
> There is a constant $C$ such that, whenever $2a>0$ is regular,
> \begin{equation}\label{bud:linear-budget}
>  \sum_{j\ge1}\Phi_j(a)\le C(1+a).
> \end{equation}
> \end{theorem}

The doubling inequality and its equality condition close the argument [S10:107–113] [S6:178–192]:

> \begin{theorem}[Doubling and its equality condition]\label{thm:doubling}
> For every regular $2L>0$,
> \begin{equation}\label{act:doubling}
>  T(2L)\ge T(L).
> \end{equation}
> If equality holds, then
> \begin{equation}\label{act:odd-equality}

The doubling inequality closes the argument [S6:178–192]:

> Finally, the full orthogonal-group action gives
> \[
>                          T(2a)\ge T(a).
> \]
> At each stage of the round-metric filtration, the global basis has a
> lower-degree family, called the bottoms, and a second family obtained by
> cup product with the sphere class pulled back by evaluation at time zero.
> The equality case requires every nonzero bottom restriction from an odd
> round-filtration stage to have a partner whose restriction is independent
> modulo all bottom restrictions in its degree
> (Theorem~\ref{thm:doubling}). Because $T$ is a bounded
> integer, an interval where it attains its maximum propagates to arbitrarily
> large intervals under doubling. A bottom generator must first appear at
> some crossing in such an interval. Evaluation cup vanishes on that local
> crossing, so its partner is still zero. This contradicts the equality case.

The global generators are the classes the filtration leaves behind [S16:151–157]:

> \begin{theorem}[Global generators and full-group lifts]
> \label{thm:global-generators}
> For \(n\ge3\), there are classes
> \[
>  X_m\in B_\infty^{a_m}=H_R^{a_m}(\Lambda,M),\qquad m\ge1,
> \]
> with the following properties.

The manuscript names the prior proofs it objects to, and says the objections are to the proofs, not to the conclusions [S6:56–65]:

> Earlier infinitude claims also require care. Asselle and
> Mazzucchelli~\cite[Introduction]{AsselleMazzucchelli2018} identify the proof in
> Klingenberg's monograph~\cite{Klingenberg1978} as erroneous.
> Charles~\cite[Theorem 6.14]{Charles2019} later claimed infinitude on every
> closed Riemannian manifold. We identify two unsupported steps in that argument:
> the boundary-rank equality in Equation~(53) requires maximal ranks not
> established there, and the constant-ball modification in Equation~(54)
> does not provide the nondegenerate Morse critical points used in the
> conclusion. These are objections to the proofs, not counterexamples to
> their conclusions.

## History of the conjecture

Birkhoff's minimax construction for surfaces of genus zero and the Lyusternik–Fet existence theorem are the classical starting points [S6:17–21] [S17:136–147] [S17:147–158]. Bott's iteration theory and the Gromoll–Meyer local Morse theory make the separation of new geodesics from repeated traversals quantitative; for a simply connected closed manifold, unbounded Betti numbers of the free loop space over a field force infinitely many geometrically distinct closed geodesics [S6:22–27]. Vigué-Poirrier and Sullivan showed that rational cohomology requiring at least two algebra generators supplies that growth — and spheres have one-generator cohomology, so the criterion does not settle the sphere case [S6:28–32].

The two-sphere case is classical, through Bangert with Franks or Hingston, extended by De Philippis–Marini–Mazzucchelli–Suhr to reversible Finsler two-spheres, with Albach's 2026 growth exponent of at least two [S6:34–41]. In higher dimensions Rademacher proved infinitude for strongly bumpy metrics and proved such metrics are generic; Long and Duan gave at least two geometrically distinct closed geodesics on every Riemannian three-sphere without genericity; Contreras and Mazzucchelli gave infinitude for generic metrics on manifolds with positive first Betti number [S6:43–53]. Hingston and Rademacher's resonance theorem makes the lengths removed and added by the cut operation differ by a bounded amount, and Cieliebak–Oancea–Shelukhin extend resonance to further compact rank-one symmetric spaces under dimension and coefficient restrictions [S6:131–133] [S6:145–149]. The chain constructions build on Hingston and Wahl's string-topology models [S6:151–153]. The loop product is Chas–Sullivan's, with the length filtration from Goresky–Hingston and the Thom-spectrum realization from Cohen–Jones; the fixed-degree additive filling estimate of Block–Manin–Weinberger is the manuscript's stated direct predecessor [S6:135–144].

**Prior (my training data, not this repo).** Infinitude of closed geodesics on $S^n$ for $n \ge 3$ was, as of my cutoff, known for strongly bumpy metrics (Rademacher) and for positively curved spheres, and the two-sphere case was settled by Bangert with Franks and Hingston. The statement for every smooth metric on every $S^n$ with $n \ge 3$, counted by distinct images, is what I recall as open, and the manuscript's own introduction says a Charles 2019 claim of infinitude on every closed manifold has unsupported steps. The prior is a training-data recollection at an early-2025 cutoff, self-rated, and the repo supplies only the manuscript's citations.

## Consequences now that the proof has been found

The direct consequence is the release's statement: every smooth metric on every sphere of dimension at least two has infinitely many prime closed geodesics with distinct images, and the same holds on every closed manifold with a finite smooth spherical cover and on every closed three-manifold, with no orientability or nondegeneracy restriction [S1:8356] [S2:788]. The corollary covers real projective spaces and smooth spherical space forms [S6:73], and the three-manifold case reaches outside the spherical-cover class through geometrization [S6:100–106].

The method's consequence is the treatment of degenerate metrics. The manuscript states that a limiting argument from generic metrics need not preserve distinct prime images [S6:49–50], and its uniform filling statement is independent of the finite-prime assumption [S6:123–124].

Inside the release, this family has no formalization. The ledger records tier T0, `paps_form` 0, `chal` 0, `mainres` 0, `scope_note` 0, `verification` 0, `inputs` 0, `covmd` 0, and no trace [S18:341]. The claim-shape column is `resolution` and the broad counterexample flag is 0. Nothing in `lean/` states the theorem, so no Lean or comparator run can confirm any part of it.

What has not been checked: no Lean, lake, or comparator run was performed, and for this family there is nothing in the release to run; the eleven section files carry 3,773 lines and were read at the statement level, not line by line, so a proof step inside `local.tex`, `cutjoin.tex`, `shortening.tex`, `transients.tex`, `budget.tex`, `activation.tex`, or `equivariant.tex` can be mis-stated here, and the statements quoted above are truncated at the block's opening — the `thm:ordinary-death` align, the `thm:local-control` enumerate items, the `thm:doubling` equality equation, the `prop:sphere-powers` continuation, the `thm:filtered-interchange` conclusion, the `prop:absolute-unit` continuation, and the `thm:global-generators` property list were not read past the quoted window; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 16 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| ID | File | Lines | What it carries |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release blurb, manuscript link, manuscript abstract |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 345's `\resultentry`, at line 788 |
| S3 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/README.md`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/README.md) | 18 | Manuscript README, date, bibtex key |
| S4 | [`paper.pdf`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf) | — | Manuscript PDF |
| S5 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/paper.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/paper.tex) | 69 | Preamble, theorem environments, section include list |
| S6 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/introduction.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/introduction.tex) | 211 | Main theorem, corollaries, proof idea, prior work, objections to prior proofs |
| S7 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/setup.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/setup.tex) | 69 | Energy, length, sublevels, the O(2) and Klein-group actions |
| S8 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/ordinary.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/ordinary.tex) | 159 | Uniform ordinary death theorem |
| S9 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/local.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/local.tex) | 767 | Analytic foundations, counting prime images, uniform local control |
| S10 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/activation.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/activation.tex) | 256 | Doubling and its equality condition |
| S11 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/budget.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/budget.tex) | 282 | Finite-cut defect bound |
| S12 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/cutjoin.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/cutjoin.tex) | 615 | Sphere powers and resonance, filtered interchange, absolute unit |
| S13 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/transients.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/transients.tex) | 339 | Bounded total transients |
| S14 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/shortening.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/shortening.tex) | 393 | Fixed-degree filling |
| S15 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/cover-proof.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/cover-proof.tex) | 36 | The finite-cover proof |
| S16 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/equivariant.tex`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/sections/equivariant.tex) | 646 | Global generators and full-group lifts |
| S17 | [`preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/references.bib`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/build/references.bib) | 320 | Bibliography |
| S18 | [`notes/tables/catalog.tsv`](../../../notes/tables/catalog.tsv) | 373 | Reading ledger row for family 345 |
