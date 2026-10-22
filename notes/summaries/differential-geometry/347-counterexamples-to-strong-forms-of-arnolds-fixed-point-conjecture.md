Notes / Summaries / Differential geometry / [Family 347](../../index/differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md)

# 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

## Original CONTENTS.md summary

The release's blurb for family 347 [S1:8397]:

> **347. Counterexamples to stable-Morse and strong Arnold fixed-point bounds.** Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed Kähler manifolds of real dimension 22, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function.

The dimension-twenty-two manuscript's abstract [S1:8406]:

> We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points by constructing a simply connected closed Kähler manifold with sixteen fewer fixed points than its stable Morse number. All the corresponding periodic orbits are contractible. The construction combines a Hamiltonian involution with integral homology torsion at two different primes; its proof uses finite-dimensional Morse theory and complex blowups.

The companion manuscript's abstract [S1:8415]:

> We construct a simply connected closed Kähler manifold of real dimension 3332 and minimal Chern number one whose Hamiltonian fixed-point count attains the cyclic integral Floer bound while falling below the stable Morse number. The Hamiltonian diffeomorphism has exactly $1\,872\,232$ fixed points, all nondegenerate and with contractible orbit loops, whereas the stable Morse number is $1\,872\,264$. Thus the stronger stable Morse bound fails by exactly 32, even when the cyclic integral bound is sharp.

The October 5, 2026 base manuscript's abstract [S1:8424]:

> We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points with examples in fixed real dimension twenty-two. For every integer m ≥ 1, we construct a simply connected closed Kähler manifold with stable Morse number $80+1968m$ and a Hamiltonian diffeomorphism with exactly $80+1952m$ fixed points, all nondegenerate and with contractible orbit loops. The deficit is therefore unbounded, and the fixed-point count is at most 127/128 of the stable Morse number.

The nondegenerate manuscript's abstract [S1:8433]:

> We construct a smooth Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, at least one of which is degenerate. The critical number and the unit-inclusive rational cup length of this manifold are both four. Thus the example disproves the unrestricted critical-number and rational cup-length forms of the Arnold conjecture.

The degenerate manuscript's abstract [S1:8442]:

> We construct a smooth one-periodic Hamiltonian on a closed symplectic twelve-manifold whose time-one map has fewer fixed points than the manifold's ordinary Morse number. Every fixed point is nondegenerate and has a contractible Hamiltonian trajectory. This disproves the Morse-number form of the Arnold conjecture. The deficit can be arbitrarily large among twelve-dimensional examples.

The catalog abstract in `overview.tex` is the blurb quoted above [S2:792]. The bibtex key the degenerate manuscript ships [S3:10–13]:

> @misc{OAI:A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026,
>   author = {{OpenAI}},
>   title = {{Three fixed points on the symplectic quadric threefold}},
>   howpublished = {OpenAI Math Release preprint

and [S8:10–13]:

> @misc{OAI:A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026,
>   author = {{OpenAI}},
>   title = {{A nondegenerate counterexample to the Morse-number Arnold bound}},
>   howpublished = {OpenAI Math Release preprint

and [S13:10–13]:

> @misc{OAI:Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026,
>   author = {{OpenAI}},
>   title = {{Hamiltonian Fixed Points Below the Stable Morse Number}},
>   howpublished = {OpenAI Math Release preprint

and [S18:10–13]:

> @misc{OAI:Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026,
>   author = {{OpenAI}},
>   title = {{Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two}},
>   howpublished = {OpenAI Math Release preprint

and [S23:10–13]:

> @misc{OAI:Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026,
>   author = {{OpenAI}},
>   title = {{Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

The Arnold fixed-point problem asks how many fixed points a Hamiltonian diffeomorphism must have. A proposed integral answer is the **stable Morse number**: the fewest critical points a Morse function on the manifold can have once you are allowed to add auxiliary quadratic variables [S16:6–12]:

> \begin{definition}
> Let $W$ be a connected closed smooth manifold. Its \emph{stable Morse number} $\SM(W)$ is the minimum of $\#\Crit(F)$ over all integers $k\geq0$ and smooth Morse functions
> \[
>  F:W\times\R^k\longrightarrow\R
> \]
> such that, when $k>0$, there are a nondegenerate quadratic form $Q$ on $\R^k$ and $R>0$ with $F(x,z)=Q(z)$ for every $x\in W$ and $|z|\geq R$. The signature of $Q$ is unrestricted. For $k=0$, there is no condition at infinity. The ordinary Morse number $\Morse(W)$ is the same minimum restricted to $k=0$.
> \end{definition}

The proposed bound is that a Hamiltonian whose fixed points are all nondegenerate must have at least that many fixed points [S16:20–24]:

> This counts distinct initial points, with no multiplicity from choices of capping disks. The stable Morse version of the fixed-point bound asks whether \begin{equation}  #\Fix_0(\phi_H^1;H)\geq\SM(M) \end{equation} holds whenever every fixed point is nondegenerate. The following theorem disproves this unrestricted assertion.

The base manuscript disproves it in real dimension 1412 [S16:26–32]:

> \begin{theorem}\label{thm:main}
> There exist a simply connected closed Kähler manifold $(M,\omega)$ and a smooth one-periodic Hamiltonian $H$ such that every fixed point of $\phi_H^1$ is nondegenerate and
> \[
>  \#\Fix_0(\phi_H^1;H)=\#\Fix(\phi_H^1)=\SM(M)-16.
> \]
> One may take $\dim_{\R}M=1412$, with $\SM(M)=318968$ and $\#\Fix(\phi_H^1)=318952$.
> \end{theorem}

The dimension-twenty-two manuscript makes the deficit a fixed proportion in a fixed dimension [S21:37–53]:

> \begin{theorem}\label{thm:main}
> For every integer $m\geq1$, there exist a simply connected closed Kähler manifold $(M_m,\omega_m)$ of real dimension $22$ and a smooth one-periodic Hamiltonian $H_m$ such that all fixed points of $\phi_{H_m}^1$ are nondegenerate and
> \begin{align*}
>  \SM(M_m)&=80+1968m,\\
>  \#\Fix(\phi_{H_m}^1)
>  &=\#\Fix_0(\phi_{H_m}^1;H_m)=80+1952m.
> \end{align*}
> Consequently, with $\delta=1/128$, for every $R>0$ some member of this family satisfies
> \[
>  \SM(M_m)\geq R,\qquad
>  \#\Fix(\phi_{H_m}^1)\leq(1-\delta)\SM(M_m).
> \]
> \end{theorem}

The nondegenerate manuscript works in real dimension twelve and beats the **ordinary** Morse number [S11:32–40]:

> \begin{theorem}\label{thm:main}
> There exist a closed connected symplectic manifold $(M,\omega)$ of real
> dimension twelve and a smooth one-periodic Hamiltonian $H$ such that every
> fixed point of $\phi_H^1$ is nondegenerate and
> \[
> \#\Fix_0(\phi_H^1;H)=\#\Fix(\phi_H^1)
>                    =\chi(M)+128<\Morse(M).
> \]
> \end{theorem}

The companion manuscript shows the cyclic integral Floer bound is sharp while the stable Morse number is not [S26:52–67]:

> \begin{theorem}
> \label{thm:main}
> There exist a simply connected closed K\"ahler manifold $(M,\omega)$
> of complex dimension $1666$ and a smooth one-periodic Hamiltonian $H$
> such that
> \[
>  c_1(TM)(\pi_2(M))=\Z,
> \]
> every fixed point of $\phi_H^1$ is nondegenerate, and
> \begin{align*}
>  \#\Fix(\phi_H^1)
>  &=\#\Fix_0(\phi_H^1;H)
>   =\beta_{\Z}^{\mathrm{cyc}}(M)=1\,872\,232,\\
>  \SM(M)&=\beta_{\Z}^{\mathrm{cyc}}(M)+32=1\,872\,264.
> \end{align*}
> \end{theorem}

The degenerate manuscript is the smallest example, and its theorem sets the fixed-point count against the critical number and the rational cup length [S6:56–64]:

> \begin{theorem}\label{thm:counterexample}
> There is a smooth Hamiltonian diffeomorphism $\phi$ of the closed connected
> symplectic six-manifold $Q^3$ such that
> \begin{equation}\label{eq:counterexample}
>  \#\Fix(\phi)=3<4=\Crit(Q^3)
>                   =\operatorname{cuplength}(Q^3;\mathbb Q).
> \end{equation}
> At least one fixed point of $\phi$ is degenerate.
> \end{theorem}

The count of three is sharp: Gong proved that a Hamiltonian involution on a closed symplectic manifold with a positive-dimensional fixed component has at least three fixed points [S6:74–77].

## Graduate summary

The stable Morse number is a minimum over actual smooth functions, and the base manuscript states the algebraic caveat [S16:14]:

> These functions have finitely many critical points, and $\SM(W)\leq\Morse(W)$. The definition is a minimum over actual smooth functions; an algebraic complex of small rank alone does not provide an upper bound.

The geometric lower bound is $\lambda(W)=b(W)+2\sum_i t_i(W)$, where $b$ is the total integral homology rank and $t_i$ is the minimum number of generators of the torsion in degree $i$ [S16:37–41]:

> For a closed manifold $W$, let $b(W)$ be its total integral homology rank, and let $t_i(W)$ be the minimum number of generators of $\Tor H_i(W;\mathbb Z)$. The quantity \[ \lambda(W)=b(W)+2\sum_i t_i(W) \] is a lower bound for $\SM(W)$. For simply connected manifolds of the dimensions used here, Smale's theorem gives an ordinary Morse function attaining this bound. We prove the geometric lower bound in Section~  and recall a handle proof of attainment in Appendix~ .

The dynamical ingredient is the same in the three October 5 manuscripts: a Kähler surface $Y$ obtained by blowing up the four points $\{0,\infty\}\times\{0,\infty\}$ of $\CP^1\times\CP^1$, whose half-turn diagonal circle action lifts to a Hamiltonian involution with four exceptional projective lines as its fixed set [S16:43]:

> The dynamical ingredient is a Kähler surface $Y$, obtained by blowing up the four points $\{0,\infty\}\times\{0,\infty\}$ of $\mathbb{CP}^1\times\mathbb{CP}^1$. A half-turn of the diagonal circle action lifts to a Hamiltonian involution whose fixed set consists of four exceptional projective lines. For the high-dimensional simply connected Kähler manifold $X$ constructed below, the product involution $g$ on $M=X\times Y$ has four fixed components, each diffeomorphic to $C=X\times\mathbb{CP}^1$. Smale's theorem supplies a Morse function on $C$ with $\lambda(C)$ critical points.

The companion manuscript states the same mechanism as a construction plan, continuing its paragraph on the cyclic bound [S26:110–119]:

> needed geometric arguments. A rational surface $Y$ admits a Hamiltonian involution whose fixed set is the disjoint union of four projective lines. For a simply connected Kähler manifold $X$, the product $M=X\times Y$ therefore has an involution with four fixed components $C=X\times\mathbb {CP}^1$. A small invariant Hamiltonian perturbation replaces each component by the critical points of a Morse function on $C$. In the dimensions used below, Smale's theorem supplies such a function with $\lambda(C)$ critical points. The dynamical construction therefore gives $4\lambda(C)$ nondegenerate fixed points.

The dimension-twenty-two manuscript's generator count combines primes by a maximum, not a sum [S21:118–126]:

> The generator count combines different primes by a maximum rather than a sum. For example, \[ d\bigl((\mathbf Z/2)^a\oplus(\mathbf Z/3)^q\bigr)=\max(a,q). \] We will arrange that the prime contributing the larger multiplicity changes with the homological degree. Redistributing those degrees by taking products can then change the generator count in a way that the free ranks do not detect.

It embeds $m$ copies of two projective surfaces, with torsion $(\Z/2)^2$ and $\Z/3$ in degrees 1 and 2, disjointly into $\CP^9$ and blows them up [S21:128–136]:

> To arrange the needed homology, take two projective surfaces whose torsion groups are respectively $(\mathbf Z/2)^2$ and $\mathbf Z/3$ in degrees $1$ and $2$. The blow-up centers are the first surface and the product of the second with $\mathbf{CP}^1\times\mathbf{CP}^1$, of complex dimensions $2$ and $4$. Section~  embeds $m$ copies of each disjointly into $\mathbf{CP}^9$ and blows them up to obtain a simply connected Kähler manifold $X_m$. The projection argument applies more generally to every finite collection of smooth projective varieties of dimension at most $d$, using one ambient $\mathbf{CP}^{2d+1}$.

The count that separates the two numbers is $\lambda(X_m\times Y)-4\lambda(X_m\times\CP^1)=16m$ [S21:148–157]:

> Products with $\mathbf{CP}^1$ and $Y$ combine the torsion in nearby degrees with different multiplicities. Taking the maximum of the two primary multiplicities in each degree then gives different savings in the number of generators. Section~  computes \[ \lambda(X_m\times Y)-4\lambda(X_m\times\mathbf{CP}^1)=16m \] and completes the proof. This separates the stable Morse count from the Hamiltonian count without any distinction between ordinary and stable Morse theory on the simply connected manifolds in the construction.

The companion manuscript's mechanism is degree-sensitive: the 3-primary multiplicities dominate the 2-primary after convolution with the free ranks of $\CP^1$ (1,1), but not after convolution with those of $Y$ (1,6,1) [S26:121–136]:

> It remains to arrange \[ 4\lambda(C)=\beta_{\mathbb Z}^{\mathrm{cyc}}(M) <\lambda(M). \] The free even homology of $\mathbb {CP}^1$ and $Y$ has ranks $(1,1)$ and $(1,6,1)$, respectively. Multiplication by these spaces convolves the torsion multiplicities of $X$ with these two sequences. We choose $X$ so that the $3$-primary multiplicities dominate the $2$-primary multiplicities after convolution with $(1,1)$, but not after convolution with $(1,6,1)$. Blow-ups along seven disjoint products of elliptic-curve quotients and projective spaces realize the required multiplicities. This degree-sensitive choice is the mechanism that makes the cyclic count sharp while preserving a positive degreewise gap. It is expressed entirely in finite sequences and can be separated from the geometric realization.

The nondegenerate manuscript's mechanism is algebraic: generation of a group versus generation of a module over its group ring. Cossey, Gruenberg and Kovács proved that the augmentation-ideal generator number stays constant under direct powers of nontrivial perfect finite groups while the group generator number is unbounded [S11:85–90]:

> The algebraic distinction used here is classical and particularly sharp for direct powers of nontrivial perfect finite groups. Cossey, Gruenberg and Kovács proved that the augmentation-ideal generator number remains constant under these direct powers, while the group generator number is unbounded~\cite[Theorems~1--2]{CGK1974}; see also \cite[Sections~1--2]{GruenbergLinnell}.

The construction places the same small-time return map in sixteen caps of a product of four spheres, and the two counts separate [S11:149–159] [S11:161–169]:

> The closed symplectic manifold is $M=X\times(S^2)^4$. Sixteen disjoint product-cap neighborhoods correspond to the north/south choices on the four sphere factors. We place the same small-time return map of the constructed Morse function in each cap. The main gluing issue is to match the local _endpoint_ with product rotations at both poles while excluding fixed points outside the caps. The resulting smooth one-periodic Hamiltonian satisfies \begin{equation}  #\Fix(\phi_H^1)=16\bigl(\chi(X)+4b\bigr) =\chi(M)+128. \end{equation}

On the other side of the inequality, the fundamental group bounds every Morse function [S11:161–169]:

> On the other hand, the fundamental group forces every Morse function on $M$ to have at least $d(G)$ critical points in each of indices one and eleven. Euler's identity gives \begin{equation}  \Morse(M)\ge\chi(M)+4d(G). \end{equation} Since $d(A_5^k)$ is unbounded while $b$ is fixed, these two estimates give the strict inequality and the arbitrary deficits. Figure~  separates the two roles of the fundamental group.

The manuscript names the claim it contradicts: Ma's preprint asserts that the minimum number of fixed points of a nondegenerate Hamiltonian diffeomorphism always equals the ordinary Morse number [S11:118–121]:

> Ma's preprint asserts that the minimum number of fixed points of a nondegenerate Hamiltonian diffeomorphism always equals the ordinary Morse number~\cite[Theorem~1.5]{Ma2013}. Theorem~  contradicts that unrestricted assertion.

The positive results the manuscripts cite are conditional. Dimitroglou Rizell and Golovko prove the stable Morse number as a lower bound for nondegenerate Hamiltonian fixed points on closed symplectic manifolds where both the symplectic area class and the first Chern class vanish on $\pi_2(M)$ [S11:100–103]:

> For closed symplectic manifolds on which both $[\omega]$ and $c_1(TM)$ vanish on $\pi_2(M)$, Dimitroglou Rizell and Golovko prove the stable Morse number as a lower bound for nondegenerate Hamiltonian fixed points~\cite[Corollary~1.3]{DRG2017}.

The dimension-22 manuscript names the conjecture, the positive results, and why its examples escape the hypothesis [S21:75–84]:

> The stable Morse formulation is stated explicitly in \cite[Conjecture~1.2]{Golovko2020}. Damian showed that ordinary and stable Morse numbers need not agree~ . Positive results for the stable bound include the theorem of Dimitroglou Rizell and Golovko for generic Hamiltonians when both the symplectic area class and the first Chern class vanish on $\pi_2(M)$~\cite[Corollary~1.4]{DRG2017}; Pöder Balkest\aa hl obtained an independent proof using the simple homotopy type of the Hamiltonian Floer complex~\cite[Corollary~1.2]{PoderBalkestahl2021}. These hypotheses do not hold for the projective blow-ups used here.

The dimension-22 manuscript contrasts the two bounds directly [S21:68–73]:

> More recent work gives lower bounds over arbitrary fields and over the integers~ . The integral Floer bound uses homology with a cyclic grading determined by the first Chern class. The stable Morse number retains the integer grading, and these yield different bounds for the examples below; the comparison is computed in Remark~ .

The degenerate manuscript's argument is a finite-order transfer that turns a critical-point count on a fixed submanifold into a fixed-point count [S6:116–136]:

> \paragraph{Proof mechanism.}
> The key is to transfer a critical-point count from a fixed submanifold
> to the fixed-point count of a nearby Hamiltonian map. Let $A$ be a
> finite-order Hamiltonian map with fixed submanifold $F$, whose fixed
> tangent vectors are exactly those tangent to $F$. Extend a function
> $f$ on $F$ to an $A$-invariant function $K$ on the ambient manifold,
> and let $B_s$ be its Hamiltonian flow. If $A^m=\id$, invariance gives
> \[
>  (A\circ B_\varepsilon)^m=B_{m\varepsilon}.
> \]
> For sufficiently small $\varepsilon>0$, the right side has only
> stationary fixed points. Any fixed point of $A\circ B_\varepsilon$
> is therefore a critical point of $K$ fixed by $A$. Finite-group
> averaging makes ambient criticality on $F$ equivalent to criticality
> of $f$, giving
> \[
>  \Fix(A\circ B_\varepsilon)=\CritSet(f).
> \]
> This criticality step is the finite-group case of Palais's principle
> of symmetric criticality~\cite[Section~5]{Palais1979}; the power identity
> excludes additional fixed points away from $F$.

**Prior (my training data, not this repo).** As of my early-2025 cutoff, the Arnold conjecture for nondegenerate Hamiltonian diffeomorphisms on closed symplectic manifolds is a theorem with a lower bound given by the sum of Betti numbers over a field, and the stable Morse number was proposed by Golovko as a stronger, integral bound. I recall the stable Morse bound as open, with positive results under the $\pi_2$-vanishing hypothesis. A counterexample with a uniform relative deficit in a fixed dimension, and a degenerate example with three fixed points on the quadric threefold, are not things I recall from the literature. The prior is a training-data recollection, self-rated, and the repo supplies only the manuscripts' citations.

## Consequences

The direct consequence is that the stable Morse number is not a lower bound for Hamiltonian fixed points in the nondegenerate case [S16:26–32], and that the unrestricted critical-number and rational cup-length forms fail in the degenerate case [S6:56–64]. The dimension-twenty-two family makes the failure proportional: the ratio of fixed points to stable Morse number is at most 127/128 along a family whose stable Morse number is unbounded [S21:37–53]. The companion manuscript shows the cyclic integral Floer bound is sharp on the same kind of manifold while the stable Morse number exceeds the fixed-point count by 32 [S26:52–67].

The two manuscripts cite the same positive result under different corollary numbers: the nondegenerate one cites Corollary 1.3 of Dimitroglou Rizell and Golovko [S11:100–103], the dimension-22 one cites Corollary 1.4 [S21:75–84].

The consequence for the field is that the integral, homological bound and the geometric Morse bound are genuinely different assertions. The dimension-22 manuscript states that the cyclic integral Floer bound and the stable Morse number yield different bounds for the same examples [S21:68–73], and the base manuscript states that the definition is a minimum over actual smooth functions, so an algebraic complex of small rank alone does not provide an upper bound [S16:14].

Inside the release, the family is at tier T3 with one formalized manuscript. The scope note covers only the degenerate counterexample, the comparator names one config, and the `main_results` entry names `OAI.ArnoldCounterexample.main` [S28:9] [S28:11] [S31:343]. The formalized statement is a conjunction of five facts about the quadric threefold — a Hamiltonian self-equivalence, three fixed points, all degenerate, the critical number at least 4, and a degenerate fixed point [S30:12–19]. The comparator stub carries `sorry` [S29:109–114]. The four other manuscripts are not formalized, so no Lean or comparator run can confirm the dimension-1412, dimension-22, dimension-12, or cyclic-Floer claims.

The companion manuscript's dimension is stated consistently: real dimension 3332 in its `CONTENTS.md` abstract [S1:8415] and its `build/main.tex` abstract [S25:43–49], complex dimension 1666 in its theorem, which is real 3332 [S26:52–67]. The base manuscript's manifold is real dimension 1412 [S16:26–32]. The two are different manifolds, not two readings of one.

What has not been checked: no Lean, lake, or comparator run was performed, and the comparator stub carries `sorry`, so the proved version under `lean/OAI/Geometry/Arnold/` was read as source text, not elaborated; the five manuscripts carry 762, 1,496, 1,080, 1,222 and 1,120 lines in their section files, and I read only the five introductions line by line, so every section-file claim in the machinery paragraphs is a section name the introduction names, not a statement read in the section file; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 14 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `CONTENTS.md` | 9142 | Release blurb, five manuscript links, five manuscript abstracts |
| S2 | `overview.tex` | 859 | Family 347's `\resultentry`, at line 792 |
| S3 | `preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md` | 18 | Degenerate manuscript README, date, bibtex key |
| S4 | `preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf` | 9626 | Degenerate manuscript PDF |
| S5 | `preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex` | 46 | Degenerate manuscript preamble, theorem environments, abstract |
| S6 | `preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex` | 159 | Main theorem, the involution, the count, the organization |
| S7 | `preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/references.tex` | 124 | Degenerate manuscript bibliography |
| S8 | `preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md` | 18 | Nondegenerate manuscript README, date, bibtex key |
| S9 | `preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf` | 12033 | Nondegenerate manuscript PDF |
| S10 | `preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex` | 57 | Nondegenerate manuscript preamble, theorem environments, abstract |
| S11 | `preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/sections/01-introduction.tex` | 207 | Main theorem, the algebraic distinction, the cap construction, the two counts |
| S12 | `preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/refs.bib` | 307 | Nondegenerate manuscript bibliography |
| S13 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md` | 18 | Base manuscript README, date, bibtex key |
| S14 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf` | 12131 | Base manuscript PDF |
| S15 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex` | 49 | Base manuscript preamble, theorem environments, abstract |
| S16 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex` | 55 | Stable Morse definition, the proposed bound, main theorem, the mechanism |
| S17 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/references.tex` | 146 | Base manuscript bibliography |
| S18 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md` | 18 | Dimension-22 manuscript README, date, bibtex key |
| S19 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf` | 12464 | Dimension-22 manuscript PDF |
| S20 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/main.tex` | 59 | Dimension-22 manuscript preamble, theorem environments, abstract |
| S21 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/sections/introduction.tex` | 157 | Main theorem, the generator maximum, the blow-up construction, the count |
| S22 | `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/references.tex` | 148 | Dimension-22 manuscript bibliography |
| S23 | `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md` | 17 | Companion manuscript README, date, bibtex key |
| S24 | `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf` | 9750 | Companion manuscript PDF |
| S25 | `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex` | 58 | Companion manuscript preamble, theorem environments, abstract |
| S26 | `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex` | 143 | Main theorem, the cyclic bound, the degree-sensitive convolution |
| S27 | `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/references.bib` | 190 | Companion manuscript bibliography |
| S28 | `lean/docs/347.md` | 15 | Scope note: what the formalization covers, the comparator, the status |
| S29 | `lean/ComparatorChallenges/ArnoldCounterexample.lean` | 120 | Comparator stub: the target the release set, with `sorry` |
| S30 | `lean/OAI/Geometry/Arnold/Main.lean` | 25 | The proved declaration: the five-fact conjunction |
| S31 | `notes/tables/catalog.tsv` | 373 | Reading ledger row for family 347 |

## Links

- [S1](../../../CONTENTS.md)
- [S2](../../../overview.tex)
- [S3](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md)
- [S4](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf)
- [S5](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex)
- [S6](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex)
- [S7](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/references.tex)
- [S8](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md)
- [S9](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf)
- [S10](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex)
- [S11](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/sections/01-introduction.tex)
- [S12](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/refs.bib)
- [S13](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md)
- [S14](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf)
- [S15](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex)
- [S16](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex)
- [S17](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/references.tex)
- [S18](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md)
- [S19](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf)
- [S20](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/main.tex)
- [S21](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/sections/introduction.tex)
- [S22](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/references.tex)
- [S23](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md)
- [S24](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf)
- [S25](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex)
- [S26](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex)
- [S27](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/references.bib)
- [S28](../../../lean/docs/347.md)
- [S29](../../../lean/ComparatorChallenges/ArnoldCounterexample.lean)
- [S30](../../../lean/OAI/Geometry/Arnold/Main.lean)
- [S31](../../../notes/tables/catalog.tsv)
