[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 347](../index/differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md)

# 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

[Index page](../index/differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md)

## Original CONTENTS.md summary

The release's blurb for family 347 

> **347. Counterexamples to stable-Morse and strong Arnold fixed-point bounds.** Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed Kähler manifolds of real dimension 22, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function. [S1:8397]

The dimension-twenty-two manuscript's abstract 

> We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points by constructing a simply connected closed Kähler manifold with sixteen fewer fixed points than its stable Morse number. All the corresponding periodic orbits are contractible. The construction combines a Hamiltonian involution with integral homology torsion at two different primes; its proof uses finite-dimensional Morse theory and complex blowups. [S1:8424]

The companion manuscript's abstract 

> We construct a simply connected closed Kähler manifold of real dimension 3332 and minimal Chern number one whose Hamiltonian fixed-point count attains the cyclic integral Floer bound while falling below the stable Morse number. The Hamiltonian diffeomorphism has exactly $1\,872\,232$ fixed points, all nondegenerate and with contractible orbit loops, whereas the stable Morse number is $1\,872\,264$. Thus the stronger stable Morse bound fails by exactly 32, even when the cyclic integral bound is sharp. [S1:8415]

The October 5, 2026 base manuscript's abstract 

> We disprove the stable Morse lower bound for nondegenerate Hamiltonian fixed points with examples in fixed real dimension twenty-two. For every integer m ≥ 1, we construct a simply connected closed Kähler manifold with stable Morse number $80+1968m$ and a Hamiltonian diffeomorphism with exactly $80+1952m$ fixed points, all nondegenerate and with contractible orbit loops. The deficit is therefore unbounded, and the fixed-point count is at most 127/128 of the stable Morse number. [S1:8406]

The nondegenerate manuscript's abstract 

> We construct a smooth Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, at least one of which is degenerate. The critical number and the unit-inclusive rational cup length of this manifold are both four. Thus the example disproves the unrestricted critical-number and rational cup-length forms of the Arnold conjecture. [S1:8442]

The degenerate manuscript's abstract 

> We construct a smooth one-periodic Hamiltonian on a closed symplectic twelve-manifold whose time-one map has fewer fixed points than the manifold's ordinary Morse number. Every fixed point is nondegenerate and has a contractible Hamiltonian trajectory. This disproves the Morse-number form of the Arnold conjecture. The deficit can be arbitrarily large among twelve-dimensional examples. [S1:8433]

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
> Let $W$ be a connected closed smooth manifold. Its \emph{stable Morse number} $\mathrm{SM}(W)$ is the minimum of $\#\mathrm{Crit}(F)$ over all integers $k\geq0$ and smooth Morse functions
> \[
>  F:W\times\R^k\longrightarrow\R
> \]
> such that, when $k>0$, there are a nondegenerate quadratic form $Q$ on $\mathbb R^k$ and $R>0$ with $F(x,z)=Q(z)$ for every $x\in W$ and $|z|\geq R$. The signature of $Q$ is unrestricted. For $k=0$, there is no condition at infinity. The ordinary Morse number $\mathrm{Morse}(W)$ is the same minimum restricted to $k=0$.
> \end{definition}

The proposed bound is that a Hamiltonian whose fixed points are all nondegenerate must have at least that many fixed points 

> This counts distinct initial points, with no multiplicity from choices of capping disks. The stable Morse version of the fixed-point bound asks whether $$\label{eq:proposed-bound} \#\mathrm{Fix}_0(\phi_H^1;H)\geq\mathrm{SM}(M)$$ holds whenever every fixed point is nondegenerate. The following theorem disproves this unrestricted assertion. [S16:20–24]

The base manuscript disproves it in real dimension 1412 [S16:26–32]:

> \begin{theorem}\label{thm:main}
> There exist a simply connected closed Kähler manifold $(M,\omega)$ and a smooth one-periodic Hamiltonian $H$ such that every fixed point of $\phi_H^1$ is nondegenerate and
> \[
>  \#\Fix_0(\phi_H^1;H)=\#\Fix(\phi_H^1)=\SM(M)-16.
> \]
> One may take $\dim_{\mathbb R}M=1412$, with $\mathrm{SM}(M)=318968$ and $\#\mathrm{Fix}(\phi_H^1)=318952$.
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

The stable Morse number is a minimum over actual smooth functions, and the base manuscript states the algebraic caveat 

> These functions have finitely many critical points, and $\mathrm{SM}(W)\leq\mathrm{Morse}(W)$. The definition is a minimum over actual smooth functions; an algebraic complex of small rank alone does not provide an upper bound. [S16:14]

The geometric lower bound is $\lambda(W)=b(W)+2\sum_i t_i(W)$, where $b$ is the total integral homology rank and $t_i$ is the minimum number of generators of the torsion in degree $i$ 

> For a closed manifold $W$, let $b(W)$ be its total integral homology rank, and let $t_i(W)$ be the minimum number of generators of $\mathrm{Tor} H_i(W;\mathbb Z)$. The quantity \[ \lambda(W)=b(W)+2\sum_i t_i(W) \] is a lower bound for $\mathrm{SM}(W)$. For simply connected manifolds of the dimensions used here, Smale's theorem gives an ordinary Morse function attaining this bound. We prove the geometric lower bound in Section   and recall a handle proof of attainment in Appendix  . [S16:37–41]

The dynamical ingredient is the same in the three October 5 manuscripts: a Kähler surface $Y$ obtained by blowing up the four points $\{0,\infty\}\times\{0,\infty\}$ of $\mathbb {CP}^1\times\mathbb {CP}^1$, whose half-turn diagonal circle action lifts to a Hamiltonian involution with four exceptional projective lines as its fixed set 

> The dynamical ingredient is a Kähler surface $Y$, obtained by blowing up the four points $\{0,\infty\}\times\{0,\infty\}$ of $\mathbb{CP}^1\times\mathbb{CP}^1$. A half-turn of the diagonal circle action lifts to a Hamiltonian involution whose fixed set consists of four exceptional projective lines. For the high-dimensional simply connected Kähler manifold $X$ constructed below, the product involution $g$ on $M=X\times Y$ has four fixed components, each diffeomorphic to $C=X\times\mathbb{CP}^1$. Smale's theorem supplies a Morse function on $C$ with $\lambda(C)$ critical points. [S16:43]

The companion manuscript states the same mechanism as a construction plan, continuing its paragraph on the cyclic bound 

> needed geometric arguments. A rational surface $Y$ admits a Hamiltonian involution whose fixed set is the disjoint union of four projective lines. For a simply connected Kähler manifold $X$, the product $M=X\times Y$ therefore has an involution with four fixed components $C=X\times\mathbb {CP}^1$. A small invariant Hamiltonian perturbation replaces each component by the critical points of a Morse function on $C$. In the dimensions used below, Smale's theorem supplies such a function with $\lambda(C)$ critical points. The dynamical construction therefore gives $4\lambda(C)$ nondegenerate fixed points. [S26:110–119]

The dimension-twenty-two manuscript's generator count combines primes by a maximum, not a sum 

> The generator count combines different primes by a maximum rather than a sum. For example, \[ d\bigl((\mathbf Z/2)^a\oplus(\mathbf Z/3)^q\bigr)=\max(a,q). \] We will arrange that the prime contributing the larger multiplicity changes with the homological degree. Redistributing those degrees by taking products can then change the generator count in a way that the free ranks do not detect. [S21:118–126]

It embeds $m$ copies of two projective surfaces, with torsion $(\mathbb Z/2)^2$ and $\mathbb Z/3$ in degrees 1 and 2, disjointly into $\mathbb {CP}^9$ and blows them up 

> To arrange the needed homology, take two projective surfaces whose torsion groups are respectively $(\mathbf Z/2)^2$ and $\mathbf Z/3$ in degrees $1$ and $2$. The blow-up centers are the first surface and the product of the second with $\mathbf{CP}^1\times\mathbf{CP}^1$, of complex dimensions $2$ and $4$. Section   embeds $m$ copies of each disjointly into $\mathbf{CP}^9$ and blows them up to obtain a simply connected Kähler manifold $X_m$. The projection argument applies more generally to every finite collection of smooth projective varieties of dimension at most $d$, using one ambient $\mathbf{CP}^{2d+1}$. [S21:128–136]

The count that separates the two numbers is $\lambda(X_m\times Y)-4\lambda(X_m\times\mathbb {CP}^1)=16m$ 

> Products with $\mathbf{CP}^1$ and $Y$ combine the torsion in nearby degrees with different multiplicities. Taking the maximum of the two primary multiplicities in each degree then gives different savings in the number of generators. Section   computes \[ \lambda(X_m\times Y)-4\lambda(X_m\times\mathbfCP^1)=16m \] and completes the proof. This separates the stable Morse count from the Hamiltonian count without any distinction between ordinary and stable Morse theory on the simply connected manifolds in the construction. [S21:148–157]

The companion manuscript's mechanism is degree-sensitive: the 3-primary multiplicities dominate the 2-primary after convolution with the free ranks of $\mathbb {CP}^1$ (1,1), but not after convolution with those of $Y$ (1,6,1) 

> It remains to arrange \[ 4\lambda(C)=\beta_{\mathbb Z}^{\mathrmcyc}(M) <\lambda(M). \] The free even homology of $\mathbb {CP}^1$ and $Y$ has ranks $(1,1)$ and $(1,6,1)$, respectively. Multiplication by these spaces convolves the torsion multiplicities of $X$ with these two sequences. We choose $X$ so that the $3$-primary multiplicities dominate the $2$-primary multiplicities after convolution with $(1,1)$, but not after convolution with $(1,6,1)$. Blow-ups along seven disjoint products of elliptic-curve quotients and projective spaces realize the required multiplicities. This degree-sensitive choice is the mechanism that makes the cyclic count sharp while preserving a positive degreewise gap. It is expressed entirely in finite sequences and can be separated from the geometric realization. [S26:121–136]

The nondegenerate manuscript's mechanism is algebraic: generation of a group versus generation of a module over its group ring. Cossey, Gruenberg and Kovács proved that the augmentation-ideal generator number stays constant under direct powers of nontrivial perfect finite groups while the group generator number is unbounded 

> The algebraic distinction used here is classical and particularly sharp for direct powers of nontrivial perfect finite groups. Cossey, Gruenberg and Kovács proved that the augmentation-ideal generator number remains constant under these direct powers, while the group generator number is unbounded \cite[Theorems 1–2]CGK1974; see also \cite[Sections 1–2]GruenbergLinnell. [S11:85–90]

The construction places the same small-time return map in sixteen caps of a product of four spheres, and the two counts separate 

> The closed symplectic manifold is $M=X\times(S^2)^4$. Sixteen disjoint product-cap neighborhoods correspond to the north/south choices on the four sphere factors. We place the same small-time return map of the constructed Morse function in each cap. The main gluing issue is to match the local _endpoint_ with product rotations at both poles while excluding fixed points outside the caps. The resulting smooth one-periodic Hamiltonian satisfies $$\label{eq:overview-fixed-count} \#\mathrm{Fix}(\phi_H^1)=16\bigl(\chi(X)+4b\bigr) =\chi(M)+128.$$ [S11:149–159]

On the other side of the inequality, the fundamental group bounds every Morse function 

> On the other hand, the fundamental group forces every Morse function on $M$ to have at least $d(G)$ critical points in each of indices one and eleven. Euler's identity gives $$\label{eq:overview-morse-bound} \mathrm{Morse}(M)\ge\chi(M)+4d(G).$$ Since $d(A_5^k)$ is unbounded while $b$ is fixed, these two estimates give the strict inequality and the arbitrary deficits. Figure   separates the two roles of the fundamental group. [S11:161–169]

The manuscript names the claim it contradicts: Ma's preprint asserts that the minimum number of fixed points of a nondegenerate Hamiltonian diffeomorphism always equals the ordinary Morse number 

> Ma's preprint asserts that the minimum number of fixed points of a nondegenerate Hamiltonian diffeomorphism always equals the ordinary Morse number \cite[Theorem 1.5]Ma2013. Theorem   contradicts that unrestricted assertion. [S11:118–121]

The positive results the manuscripts cite are conditional. Dimitroglou Rizell and Golovko prove the stable Morse number as a lower bound for nondegenerate Hamiltonian fixed points on closed symplectic manifolds where both the symplectic area class and the first Chern class vanish on $\pi_2(M)$ 

> For closed symplectic manifolds on which both $[\omega]$ and $c_1(TM)$ vanish on $\pi_2(M)$, Dimitroglou Rizell and Golovko prove the stable Morse number as a lower bound for nondegenerate Hamiltonian fixed points \cite[Corollary 1.3]DRG2017. [S11:100–103]

The dimension-22 manuscript names the conjecture, the positive results, and why its examples escape the hypothesis 

> The stable Morse formulation is stated explicitly in \cite[Conjecture 1.2]Golovko2020. Damian showed that ordinary and stable Morse numbers need not agree  . Positive results for the stable bound include the theorem of Dimitroglou Rizell and Golovko for generic Hamiltonians when both the symplectic area class and the first Chern class vanish on $\pi_2(M)$ \cite[Corollary 1.4]DRG2017; Pöder Balkestå hl obtained an independent proof using the simple homotopy type of the Hamiltonian Floer complex \cite[Corollary 1.2]PoderBalkestahl2021. These hypotheses do not hold for the projective blow-ups used here. [S21:75–84]

The dimension-22 manuscript contrasts the two bounds directly 

> More recent work gives lower bounds over arbitrary fields and over the integers  . The integral Floer bound uses homology with a cyclic grading determined by the first Chern class. The stable Morse number retains the integer grading, and these yield different bounds for the examples below; the comparison is computed in Remark  . [S21:68–73]

The degenerate manuscript's argument is a finite-order transfer that turns a critical-point count on a fixed submanifold into a fixed-point count [S6:116–136]:

> \paragraph{Proof mechanism.}
> The key is to transfer a critical-point count from a fixed submanifold
> to the fixed-point count of a nearby Hamiltonian map. Let $A$ be a
> finite-order Hamiltonian map with fixed submanifold $F$, whose fixed
> tangent vectors are exactly those tangent to $F$. Extend a function
> $f$ on $F$ to an $A$-invariant function $K$ on the ambient manifold,
> and let $B_s$ be its Hamiltonian flow. If $A^m=\mathrm{id}$, invariance gives
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
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb, five manuscript links, five manuscript abstracts |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 347's `\resultentry`, at line 792 |
| S3 | [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md) | 18 | Degenerate manuscript README, date, bibtex key |
| S4 | [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf) | 9626 | Degenerate manuscript PDF |
| S5 | [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex) | 46 | Degenerate manuscript preamble, theorem environments, abstract |
| S6 | [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex) | 159 | Main theorem, the involution, the count, the organization |
| S7 | [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/references.tex`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/references.tex) | 124 | Degenerate manuscript bibliography |
| S8 | [`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md) | 18 | Nondegenerate manuscript README, date, bibtex key |
| S9 | [`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf) | 12033 | Nondegenerate manuscript PDF |
| S10 | [`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex) | 57 | Nondegenerate manuscript preamble, theorem environments, abstract |
| S11 | [`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/sections/01-introduction.tex) | 207 | Main theorem, the algebraic distinction, the cap construction, the two counts |
| S12 | [`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/refs.bib`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/refs.bib) | 307 | Nondegenerate manuscript bibliography |
| S13 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md) | 18 | Base manuscript README, date, bibtex key |
| S14 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) | 12131 | Base manuscript PDF |
| S15 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex) | 49 | Base manuscript preamble, theorem environments, abstract |
| S16 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex) | 55 | Stable Morse definition, the proposed bound, main theorem, the mechanism |
| S17 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/references.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/references.tex) | 146 | Base manuscript bibliography |
| S18 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md) | 18 | Dimension-22 manuscript README, date, bibtex key |
| S19 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) | 12464 | Dimension-22 manuscript PDF |
| S20 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/main.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/main.tex) | 59 | Dimension-22 manuscript preamble, theorem environments, abstract |
| S21 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/sections/introduction.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/sections/introduction.tex) | 157 | Main theorem, the generator maximum, the blow-up construction, the count |
| S22 | [`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/references.tex`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/references.tex) | 148 | Dimension-22 manuscript bibliography |
| S23 | [`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md) | 17 | Companion manuscript README, date, bibtex key |
| S24 | [`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf) | 9750 | Companion manuscript PDF |
| S25 | [`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex) | 58 | Companion manuscript preamble, theorem environments, abstract |
| S26 | [`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex) | 143 | Main theorem, the cyclic bound, the degree-sensitive convolution |
| S27 | [`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/references.bib`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/references.bib) | 190 | Companion manuscript bibliography |
| S28 | [`lean/docs/347.md`](../../../lean/docs/347.md) | 15 | Scope note: what the formalization covers, the comparator, the status |
| S29 | [`lean/ComparatorChallenges/ArnoldCounterexample.lean`](../../../lean/ComparatorChallenges/ArnoldCounterexample.lean) | 120 | Comparator stub: the target the release set, with `sorry` |
| S30 | [`lean/OAI/Geometry/Arnold/Main.lean`](../../../lean/OAI/Geometry/Arnold/Main.lean) | 25 | The proved declaration: the five-fact conjunction |
| S31 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Reading ledger row for family 347 |

## Bibliography

- Abouzaid, Mohammed, Blumberg, Andrew J., Arnold conjecture and Morava $K$-theory (2021)
- Bai, Shaoyun, Xu, Guangbo, Arnold conjecture over integers (2022)
- Bai, Shaoyun, Xu, Guangbo, Integral Hamiltonian Floer theory: Foundations (2026)
- Bai, Shaoyun, Xu, Guangbo, Arnold conjecture over integers (2022)
- Bai, Shaoyun, Xu, Guangbo, Integral Hamiltonian Floer theory: Foundations (2026)
- {Pöder Balkeståhl}, Sebastian, Simple homotopy type of the Hamiltonian Floer complex (2021)
- Barraud, Jean-François, A Floer fundamental group (2018)
- Bass, Hyman, $K$-theory and stable algebra (1964)
- T. Blomme, _Gromov–Witten invariants of bielliptic surfaces_, J. London Math. Soc. (2) **111** (2025), no. 2, e70081. doi:10.1112/jlms.70081.
- T. Blomme, _Gromov–Witten invariants of bielliptic surfaces_, J. London Math. Soc. (2) **111** (2025), no. 2, e70081. doi:10.1112/jlms.70081.
- Blomme, Thomas, Gromov–Witten invariants of bielliptic surfaces (2025)
- M. Abouzaid and A. J. Blumberg, _Arnold conjecture and Morava $K$-theory_, preprint (2021), arXiv:2103.01507.
- M. Abouzaid and A. J. Blumberg, _Arnold conjecture and Morava $K$-theory_, preprint (2021), arXiv:2103.01507.
- L. Buhovsky, V. Humili\`ere, and S. Seyfaddini, _A $C^0$ counterexample to the Arnold conjecture_, Inventiones Mathematicae **213** (2018), no. 2, 759–809. doi:10.1007/s00222-018-0797-x.
- Cerf, Jean, Travaux de Smale sur la structure des variétés (1962)
- Conley, Charles C., Zehnder, Eduard, The Birkhoff–Lewis fixed point theorem and a conjecture of V. I. Arnold (1983)
- Conley, Charles C., Zehnder, Eduard, The Birkhoff–Lewis fixed point theorem and a conjecture of V. I. Arnold (1983)
- Cossey, John, Gruenberg, Karl W., Kovács, L. G., The presentation rank of a direct product of finite groups (1974)
- V. I. Arnol'd, _First steps in symplectic topology_, Russian Mathematical Surveys **41** (1986), no. 6, 1–21. doi:10.1070/RM1986v041n06ABEH004221.
- Arnol'd, Vladimir I., First steps in symplectic topology (1986)
- V. I. Arnol'd, _First steps in symplectic topology_, Russian Math. Surveys **41** (1986), no. 6, 1–21. doi:10.1070/RM1986v041n06ABEH004221.
- V. I. Arnol'd, _First steps in symplectic topology_, Russian Math. Surveys **41** (1986), no. 6, 1–21. doi:10.1070/RM1986v041n06ABEH004221.
- Arnol'd, Vladimir I., First steps in symplectic topology (1986)
- Damian, Mihai, On the stable Morse number of a closed manifold (2002)
- M. Damian, _On the stable Morse number of a closed manifold_, Bull. London Math. Soc. **34** (2002), no. 4, 420–430. doi:10.1112/S0024609301008955.
- M. Damian, _On the stable Morse number of a closed manifold_, Bull. London Math. Soc. **34** (2002), no. 4, 420–430. doi:10.1112/S0024609301008955.
- Damian, Mihai, On the stable Morse number of a closed manifold (2002)
- Duan, Haibao, Li, Banghe, Topology of blow-ups and enumerative geometry (2009)
- Eliashberg, Yakov, Gromov, Mikhail, Lagrangian intersection theory: finite-dimensional approach (1998)
- A. Floer, _Symplectic fixed points and holomorphic spheres_, Communications in Mathematical Physics **120** (1989), no. 4, 575–611. doi:10.1007/BF01260388.
- Floer, Andreas, Symplectic fixed points and holomorphic spheres (1989)
- A. Floer, _Symplectic fixed points and holomorphic spheres_, Comm. Math. Phys. **120** (1989), no. 4, 575–611. doi:10.1007/BF01260388.
- A. Floer, _Symplectic fixed points and holomorphic spheres_, Comm. Math. Phys. **120** (1989), no. 4, 575–611. doi:10.1007/BF01260388.
- Floer, Andreas, Symplectic fixed points and holomorphic spheres (1989)
- B. Fortune, _A symplectic fixed point theorem for $\CP^n$_, Inventiones Mathematicae **81** (1985), no. 1, 29–46. doi:10.1007/BF01388770.
- Fukaya, Kenji, Ono, Kaoru, Arnold conjecture and Gromov–Witten invariant (1999)
- R. Golovko, _On variants of Arnold conjecture_, Archivum Mathematicum **56** (2020), no. 5, 277–286. doi:10.5817/AM2020-5-277.
- Golovko, Roman, On variants of Arnold conjecture (2020)
- G. Dimitroglou Rizell and R. Golovko, _The number of Hamiltonian fixed points on symplectically aspherical manifolds_, in _Proceedings of the Gökova Geometry-Topology Conference 2016_, International Press, 2017, pp. 138–150. arXiv:1609.04776v2.
- R. Golovko, _On variants of Arnold conjecture_, Arch. Math. (Brno) **56** (2020), no. 5, 277–286. doi:10.5817/AM2020-5-277.
- G. Dimitroglou Rizell and R. Golovko, _The number of Hamiltonian fixed points on symplectically aspherical manifolds_, in _Proceedings of the Gökova Geometry-Topology Conference 2016_, Gökova Geometry-Topology Conference (GGT), Gökova, 2017, pp. 138–150. arXiv:1609.04776v2.
- R. Golovko, _On variants of Arnold conjecture_, Arch. Math. (Brno) **56** (2020), no. 5, 277–286. doi:10.5817/AM2020-5-277.
- Golovko, Roman, On variants of Arnold conjecture (2020)
- Gompf, Robert E., Some new symplectic 4-manifolds (1992)
- Gompf, Robert E., A new construction of symplectic manifolds (1995)
- W. Gong, _Degenerate symplectic fixed points and Gromov–Witten invariants_, arXiv:2507.04191v5, December 21, 2025.
- Gruenberg, Karl W., Linnell, Peter A., Generation gaps and abelianized defects of free products (2008)
- R. Hartshorne, _Algebraic Geometry_, Graduate Texts in Mathematics, vol. 52, Springer-Verlag, New York–Heidelberg, 1977. doi:10.1007/978-1-4757-3849-0.
- S. Pöder Balkestå hl, _Simple homotopy type of the Hamiltonian Floer complex_, preprint (2021), arXiv:2110.10592.
- S. Pöder Balkestå hl, _Simple homotopy type of the Hamiltonian Floer complex_, preprint (2021), arXiv:2110.10592.
- H. Hofer, _Lusternik–Schnirelman-theory for Lagrangian intersections_, Annales de l'Institut Henri Poincaré C, Analyse non linéaire **5** (1988), no. 5, 465–499. doi:10.1016/S0294-1449(16)30339-0.
- H. Jiao, _A smooth Hamiltonian diffeomorphism with two fixed points on $S^2\times S^2$_, arXiv:2609.33626v1, September 27, 2026.
- Laudenbach, François, A proof of Morse's theorem about the cancellation of critical points (2013)
- H. Duan and B. Li, _Topology of blow-ups and enumerative geometry_, preprint (2009), revised 2016, arXiv:0906.4152v7.
- H. Duan and B. Li, _Topology of blow-ups and enumerative geometry_, preprint (2009), revised 2016, arXiv:0906.4152v7.
- Liu, Gang, Tian, Gang, Floer homology and Arnold conjecture (1998)
- R. Ma, _Proofs on Arnold conjectures_, arXiv:0808.0613v7, July 5, 2013.
- Ma, Renyi, Proofs on Arnold conjectures (2013)
- A.-L. Mare, _Topology of isotropy orbits_, doctoral dissertation, Universität Augsburg, 1997. Author-hosted text.
- Milnor, John, Lectures on the $h$-Cobordism Theorem (1965)
- J. Milnor, _Morse Theory_, Annals of Mathematics Studies, vol. 51, Princeton University Press, Princeton, NJ, 1963.
- J. Milnor, _Lectures on the $h$-Cobordism Theorem_, notes by L. Siebenmann and J. Sondow, Princeton University Press, Princeton, NJ, 1965.
- J. Milnor, _Morse Theory_, Annals of Mathematics Studies, vol. 51, Princeton University Press, Princeton, NJ, 1963.
- J. Milnor, _Lectures on the $h$-Cobordism Theorem_, notes by L. Siebenmann and J. Sondow, Princeton University Press, Princeton, NJ, 1965.
- Milnor, John, Morse Theory (1963)
- Milnor, John, Lectures on the $h$-Cobordism Theorem (1965)
- Morgan, John, Lecture IV: $K_0$, $K_1$, Whitehead torsion, and the $s$-cobordism theorem (2020)
- K. Fukaya and K. Ono, _Arnold conjecture and Gromov–Witten invariant_, Topology **38** (1999), no. 5, 933–1048. doi:10.1016/S0040-9383(98)00042-1.
- Ono, Kaoru, Pajitnov, Andrei, On the fixed points of a Hamiltonian diffeomorphism in presence of fundamental group (2016)
- K. Fukaya and K. Ono, _Arnold conjecture and Gromov–Witten invariant_, Topology **38** (1999), no. 5, 933–1048. doi:10.1016/S0040-9383(98)00042-1.
- K. Ono, _On the Arnold conjecture for weakly monotone symplectic manifolds_, Invent. Math. **119** (1995), 519–537. doi:10.1007/BF01245191.
- K. Fukaya and K. Ono, _Arnold conjecture and Gromov–Witten invariant_, Topology **38** (1999), no. 5, 933–1048. doi:10.1016/S0040-9383(98)00042-1.
- K. Ono, _On the Arnold conjecture for weakly monotone symplectic manifolds_, Invent. Math. **119** (1995), 519–537. doi:10.1007/BF01245191.
- OpenAI, _A nondegenerate counterexample to the Morse-number Arnold bound_, OpenAI Math Release preprint OAI:A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026, 2026.
- OpenAI, _Hamiltonian Fixed Points Below the Stable Morse Number_, OpenAI Math Release preprint OAI:Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026, 2026.
- OpenAI, Hamiltonian Fixed Points Below the Stable Morse Number (2026)
- Y. B. Rudyak and J. Oprea, _On the Lusternik–Schnirelmann category of symplectic manifolds and the Arnold conjecture_, Mathematische Zeitschrift **230** (1999), no. 4, 673–678. doi:10.1007/PL00004709.
- R. S. Palais, _The principle of symmetric criticality_, Communications in Mathematical Physics **69** (1979), no. 1, 19–30. doi:10.1007/BF01941322.
- Ranicki, Andrew, Algebraic and Geometric Surgery (2002)
- Dimitroglou Rizell, Georgios, Golovko, Roman, The number of Hamiltonian fixed points on symplectically aspherical manifolds (2017)
- Dimitroglou Rizell, Georgios, Golovko, Roman, The stable Morse number as a lower bound for the number of Reeb chords (2018)
- Dimitroglou Rizell, Georgios, Golovko, Roman, The number of Hamiltonian fixed points on symplectically aspherical manifolds (2017)
- Y. Ruan, _Virtual neighborhoods and pseudo-holomorphic curves_, Turkish Journal of Mathematics **23** (1999), no. 1, 161–232. Publisher record; arXiv:alg-geom/9611021v2.
- Ruan, Yongbin, Virtual neighborhoods and pseudo-holomorphic curves (1999)
- Y. Ruan, _Virtual neighborhoods and pseudo-holomorphic curves_, Turkish J. Math. **23** (1999), no. 1, 161–232.
- Y. Ruan, _Virtual neighborhoods and pseudo-holomorphic curves_, Turkish J. Math. **23** (1999), no. 1, 161–232.
- H. Hofer and D. A. Salamon, _Floer homology and Novikov rings_, in _The Floer Memorial Volume_, H. Hofer, C. H. Taubes, A. Weinstein, and E. Zehnder (eds.), Progress in Mathematics, vol. 133, Birkhäuser, Basel, 1995, pp. 483–524. doi:10.1007/978-3-0348-9217-9\_20.
- D. McDuff and D. Salamon, _Introduction to Symplectic Topology_, third edition, Oxford Graduate Texts in Mathematics, vol. 27, Oxford University Press, Oxford, 2017.
- H. Hofer and D. A. Salamon, _Floer homology and Novikov rings_, in _The Floer Memorial Volume_, H. Hofer, C. H. Taubes, A. Weinstein, and E. Zehnder (eds.), Progress in Mathematics, vol. 133, Birkhäuser, Basel, 1995, pp. 483–524. doi:10.1007/978-3-0348-9217-9\_20.
- L. Lusternik and L. Schnirelmann, _Méthodes topologiques dans les probl\`emes variationnels. I. Espaces \`a un nombre fini de dimensions_, Actualités scientifiques et industrielles 188, Hermann, Paris, 1934.
- F. Serrano, _The Picard group of a quasi-bundle_, Manuscripta Math. **73** (1991), no. 1, 63–82.
- F. Serrano, _The Picard group of a quasi-bundle_, Manuscripta Math. **73** (1991), no. 1, 63–82.
- S. Smale, _A survey of some recent developments in differential topology_, Bull. Amer. Math. Soc. **69** (1963), 131–145. doi:10.1090/S0002-9904-1963-10901-5.
- S. Smale, _A survey of some recent developments in differential topology_, Bull. Amer. Math. Soc. **69** (1963), 131–145. doi:10.1090/S0002-9904-1963-10901-5.
- Smale, Stephen, A survey of some recent developments in differential topology (1963)
- F. Takens, _The minimal number of critical points of a function on a compact manifold and the Lusternik–Schnirelman category_, Inventiones Mathematicae **6** (1968), no. 3, 197–244. doi:10.1007/BF01404825.
- G. Liu and G. Tian, _Floer homology and Arnold conjecture_, Journal of Differential Geometry **49** (1998), no. 1, 1–74. doi:10.4310/jdg/1214460936.
- G. Liu and G. Tian, _Floer homology and Arnold conjecture_, J. Differential Geom. **49** (1998), no. 1, 1–74. doi:10.4310/jdg/1214460936.
- G. Liu and G. Tian, _Floer homology and Arnold conjecture_, J. Differential Geom. **49** (1998), no. 1, 1–74. doi:10.4310/jdg/1214460936.
- J. Weber, _Conley pairs in geometry—Lusternik–Schnirelmann theory and more_, Expositiones Mathematicae **37** (2019), no. 1, 25–47. doi:10.1016/j.exmath.2017.10.003.
- S. Bai and G. Xu, _Arnold conjecture over integers_, preprint (2022), arXiv:2209.08599.
- S. Bai and G. Xu, _Integral Hamiltonian Floer theory: Foundations_, preprint (2026), arXiv:2606.15847.
- S. Bai and G. Xu, _Arnold conjecture over integers_, preprint (2022), arXiv:2209.08599.
- S. Bai and G. Xu, _Integral Hamiltonian Floer theory: Foundations_, preprint (2026), arXiv:2606.15847.
- J. A. Yorke, _Periods of periodic solutions and the Lipschitz constant_, Proceedings of the American Mathematical Society **22** (1969), no. 2, 509–512. doi:10.1090/S0002-9939-1969-0245916-7.
- Yorke, James A., Periods of periodic solutions and the Lipschitz constant (1969)
- J. A. Yorke, _Periods of periodic solutions and the Lipschitz constant_, Proc. Amer. Math. Soc. **22** (1969), no. 2, 509–512. doi:10.1090/S0002-9939-1969-0245916-7.
- J. A. Yorke, _Periods of periodic solutions and the Lipschitz constant_, Proc. Amer. Math. Soc. **22** (1969), no. 2, 509–512. doi:10.1090/S0002-9939-1969-0245916-7.
- Yorke, James A., Periods of periodic solutions and the Lipschitz constant (1969)
- C. C. Conley and E. Zehnder, _The Birkhoff–Lewis fixed point theorem and a conjecture of V. I. Arnold_, Inventiones Mathematicae **73** (1983), 33–49. doi:10.1007/BF01393824.
- C. C. Conley and E. Zehnder, _The Birkhoff–Lewis fixed point theorem and a conjecture of V. I. Arnold_, Invent. Math. **73** (1983), no. 1, 33–49. doi:10.1007/BF01393824.
- C. C. Conley and E. Zehnder, _The Birkhoff–Lewis fixed point theorem and a conjecture of V. I. Arnold_, Invent. Math. **73** (1983), no. 1, 33–49. doi:10.1007/BF01393824.
