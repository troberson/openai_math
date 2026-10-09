# 362 — Global smoothness for relativistic Vlasov–Maxwell (Partial differential equations, 1 manuscript, tier T3)

## Original CONTENTS.md summary

**362. Global smoothness for relativistic Vlasov–Maxwell.** Proves large-data global existence and uniqueness for the three-dimensional, one-species relativistic Vlasov–Maxwell system. Smooth admissible initial data may be arbitrary provided the particle density is compactly supported and the electromagnetic fields have finite energy and bounded derivatives of every order; the solution remains smooth on every finite time interval. ([Lean](../../../lean/docs/362.md))

The blurb above is reproduced from [S1:8799], with the Lean link rewritten as a relative link from this page's directory. The release sets the family number and title in bold and renders the en dash in the title as an en dash; the entry's own manuscript link sits at [S1:8806] and the release's copy of the abstract at [S1:8808].

## Undergraduate summary

The relativistic Vlasov–Maxwell system is the standard kinetic model for a plasma in which collisions are ignored and every particle feels the same electromagnetic field that the particles themselves create. A state is a density `f(t, x, v)` of particles at position `x` moving with velocity `v`, plus an electric field `E(t, x)` and a magnetic field `B(t, x)`. Particles travel at the relativistic velocity `v / sqrt(1 + |v|²)` — always strictly below the speed of light — and are pushed by the Lorentz force `E + v × B`. The fields are not prescribed: charge density and current are velocity integrals of `f`, and Maxwell's equations determine how the fields evolve from them. This paper treats one species of particle in three spatial dimensions.

Two existence theories were long known for this system and neither was enough. DiPerna–Lions type theory gives global *weak* solutions for large data, but weak solutions need not be smooth and need not be unique. Classical (smooth, pointwise) solutions are known to exist locally in time, and the standard continuation criterion — going back to Glassey and Strauss — says a classical solution can be continued past a finite time as long as the particles' speeds stay bounded on that interval. So the whole problem collapses to one question: can a smooth solution accelerate particles to unbounded speeds in finite time? Every global classical result before this one answered that question under a restriction on the data — symmetry, reduced dimension, smallness, or a special reference solution.

This paper removes the restrictions. The initial data are any nonnegative smooth compactly supported particle density together with electric and magnetic fields of finite energy whose derivatives of every order are bounded, satisfying the two Gauss constraints. No smallness, no symmetry, no neutrality. The result is a unique global classical solution that stays smooth on every finite time interval, with the particle density confined to a compact region of phase space on each such interval.

**Proof sketch.** Follow one particle, labelled by its initial phase-space point, and look at the *signed* change of its momentum over a time interval: integrate the force first and take the norm afterwards, never the norm of the force at each instant. The main estimate bounds that signed change by `M·P·sqrt(Δt) + A·Δt·P²·log(2+P)/w`, where `P` tracks the largest particle energy, `w` is the dyadic energy scale of the particle, and `M`, `A`, `P` are fixed in advance and independent of how long the solution is run. Now suppose the maximum particle energy were doubling: reaching energy `2ⁿ` from energy `2ⁿ⁻¹` takes at least `c / log(2 + 1024·2ⁿ)` time, and the sum of those lower bounds over `n` diverges. Momentum therefore cannot blow up in finite time, the Glassey–Strauss criterion applies at every finite time, and the solution continues forever. The analytic work all goes into that one signed estimate, which is proved by a bootstrap: assume the bound, derive a strictly better version of it, and close by continuity.

## Graduate summary

The model is written in the one-species normalization with no background charge, so the fields are sourced entirely by the particle density.

The system and its charge and current, stated once and used throughout [S4:10–25]:

> \begin{equation}\label{eq:rvm}
> \begin{aligned}
>  \partial_t f+u(v)\cdot\nabla_x f+
>      (E+u(v)\times B)\cdot\nabla_v f&=0,\\
>  \partial_t E-\nabla_x\times B&=-j_f,
>  &\partial_t B+\nabla_x\times E&=0,\\
>  \nabla_x\cdot E&=\rho_f,
>  &\nabla_x\cdot B&=0,
> \end{aligned}
> \end{equation}
> where
> \[
>  \rho_f(t,x)=\int_{\R^3}f(t,x,v)\,dv,
>  \qquad j_f(t,x)=\int_{\R^3}u(v)f(t,x,v)\,dv.
> \]
> There is no background charge.

The field class is the load-bearing choice. `C_b^∞` bounds every spatial derivative but does not require square-integrable derivatives, which is what allows a nonzero total charge and its Coulomb tail.

The admissible datum, and the meaning of the field class [S4:27–35]:

> A \emph{smooth admissible datum} is a triple $(f_0,E_0,B_0)$ satisfying
> \begin{equation}\label{eq:data}
> \begin{gathered}
>  f_0\in C_c^\infty(\R^3_x\times\R^3_v),\qquad f_0\ge0,\\
>  E_0,B_0\in C_b^\infty(\R^3;\R^3)\cap L^2(\R^3;\R^3),\\
>  \nabla_x\cdot E_0=\rho_{f_0},\qquad \nabla_x\cdot B_0=0.
> \end{gathered}
> \end{equation}
> Here $C_b^\infty$ means that every spatial derivative is bounded.

The theorem, stated in full [S4:42–52]:

> \begin{theorem}\label{thm:global}
> Every smooth admissible datum \eqref{eq:data} generates a unique global
> classical solution of \eqref{eq:rvm}. For every finite $T$, this solution
> satisfies
> \[
>  f\in C^\infty([0,T]\times\R^3_x\times\R^3_v),\qquad
>  E,B\in C^\infty([0,T]\times\R^3_x;\R^3),
> \]
> and $f$ has compact phase-space support on $[0,T]$.
> The two divergence constraints hold for all time.
> \end{theorem}

What the theorem does not assume, from the paragraph immediately after it [S4:54–60]:

> Theorem~\ref{thm:global} resolves the large-data global classical
> regularity problem for this one-species model in three spatial and three momentum
> dimensions. The data have no size or symmetry restriction. The field
> assumptions allow a nonzero total charge and its Coulomb tail;
> they do not require square-integrability of all field derivatives.
> The momentum support bound is on each finite time interval and may
> grow with that interval.

The proof is split into a kinetic half and a PDE half. The kinetic half is a single bootstrap on signed momentum increments, uniform over all compact classical time intervals.

The bootstrap, with its two-scale structure [S5:35–47]:

> \begin{proposition}[Signed momentum increments]\label{prop:increment}
> For each smooth admissible datum and finite $T_0$, there are constants
> $M,A\ge1$ and $P_0$ with the following property. On every compact
> classical solution interval $[0,t_*]$ as above, for every dyadic
> $P\ge P_0$ satisfying \eqref{eq:P-range}, every supported receiver,
> every $w=2^k$, $k\ge0$, and every interval $[t_1,t_2]\subset[0,t_*]$
> on which $w/8\le q_X(t)\le8w$ throughout, one has
> \begin{equation}\label{eq:bootstrap}
>  |V_X(t_2)-V_X(t_1)|
>  \le MP\sqrt{t_2-t_1}+A(t_2-t_1)S(w).
> \end{equation}
> The constants are independent of $t_*$ and $P$.
> \end{proposition}

The `sqrt` term is what makes the argument quantitative: it is a square-root-in-time bound, so a doubling of momentum costs time proportional to the square of the momentum increment, and the `S(w) = P²L/w` term is linear in time with a coefficient that decays in the receiver energy. The PDE half is the continuation criterion, packaged for a field class that is not Sobolev.

The continuation half, stated as a proposition [S5:49–57]:

> \begin{proposition}[Local theory and continuation]\label{prop:continuation}
> Every smooth admissible datum has a unique maximal classical solution.
> It is smooth on each compact subinterval of its lifespan. If its
> maximal time $T_{\max}$ is finite and
> \[
>  \sup\{\,|v|:0\le t<T_{\max},\ (x,v)\in\supp f(t)\,\}<\infty,
> \]
> then the solution has a classical extension beyond $T_{\max}$.
> \end{proposition}

The Sobolev hypotheses of the cited criterion are manufactured rather than assumed, which is the reason the Coulomb tail is affordable.

The finite-horizon field modification, described where the proposition is introduced [S5:59–67]:

> The proof is given in the final section. It combines the Glassey--Strauss
> bounded-momentum criterion in the $H^5$ formulation quoted by Luk and
> Strain~\cite[Theorem~1.1 and Footnote~1, arXiv version]{LukStrain2014Continuation}
> with a finite-horizon modification of the initial fields. The modification retains the initial Coulomb field
> and cuts off vector potentials for the divergence-free remainders.
> The removed part evolves as a vacuum Maxwell field that vanishes
> throughout the particle region for the chosen horizon. This supplies
> Sobolev field data for the continuation theorem while preserving
> the original particle dynamics.

The criterion itself, quoted where it is used [S13:444–451]:

> The continuation input is the Glassey--Strauss criterion in
> \cite[Theorem~1.1 and Footnote~1, arXiv version]{LukStrain2014Continuation}.
> In its normalization, nonnegative compactly supported $H^5$ particle
> data and $H^5$ field data satisfying the constraints have the following
> property: a unique classical solution on $[0,T)$, $T<\infty$, extends
> uniquely as a $C^1$ solution past $T$ if there is a bounded continuous
> function $\kappa:[0,T)\to(0,\infty)$ such that $f(t,x,v)=0$ whenever
> $|v|\ge\kappa(t)$.

The kinetic estimate is a light-cone argument. Fields are represented by integrating the source along the backward light cone of the receiving particle, split into dyadic bins of momentum, distance, and angle; the force kernel carries the source acceleration evaluated at the retarded point.

The retarded representation and its kernel [S6:155–162]:

> \begin{proposition}[Retarded field representation]\label{ret:representation}
> Let $E^{\rm fr},B^{\rm fr}$ be the homogeneous wave solutions with data
> \[
>  (E^{\rm fr},\partial_tE^{\rm fr})|_{t=0}
>        =(E_0,\nabla\times B_0),\qquad
>  (B^{\rm fr},\partial_tB^{\rm fr})|_{t=0}
>        =(B_0,-\nabla\times E_0).
> \]

The kernel, whose denominator degenerates when the source moves along the light ray [S6:183–186]:

> \begin{equation}\label{ret:kernel}
>  \mathscr K=\frac{n-u}{r^2q^2d^3}
>        +\frac{(n-u)(n\cdot b)-db}{rd^3}.
> \end{equation}

Bin by bin, the direct estimates give the absolute force bound. This is where the difficulty is located: the absolute bound is a factor `sqrt(w)` worse than the signed bound the bootstrap needs.

The integrated force bounds, with the absolute estimate last [S8:18–31]:

> \begin{proposition}[Integrated force bounds]\label{dir:direct}
> Assume the bootstrap \eqref{eq:bootstrap}.  The bounded data term,
> $T_r$, $T_\perp$, $S_b$, and the remaining-sector part of $S_g$ have
> combined integral at most
> \begin{equation}\label{dir:baseline}
>  C\bigl[P\sqrt I+(M+\sqrt A)I S(w)\bigr].
> \end{equation}
> The integral of the full force satisfies
> \begin{equation}\label{dir:absolute}
>  \int_{\mathcal T}|K(t)|\,dt
>  \le C\sqrt w\bigl[P\sqrt I+(M+\sqrt A)I S(w)\bigr].
> \end{equation}
> The constant $C$ is independent of $P,w,I,M,A$.
> \end{proposition}

The paper names the loss and the geometry that produces it [S4:174–177]:

> At receiver energy comparable to $w$, the absolute-force bound has an
> extra factor $\sqrt w$ compared with the signed estimate we need.
> The loss occurs when the source velocity is much closer to the light-ray
> direction than the receiver velocity is.

The recovery is an integration-by-parts identity applied to the signed force, integrating along the source trajectory before taking absolute values. It converts the singular part into a total derivative plus less singular bulk terms, one of which contains the receiver's own acceleration — hence a coefficient multiplying the very force being estimated.

The weighted signed formula, as stated [S9:278–284]:

> \begin{proposition}[Weighted signed formula]\label{can:weighted-formula}
> Let $J=[t_1,t_2]$ lie in a compact classical time interval. Let
> $0\leq\psi\leq1$ be Lipschitz on $J$, vanish at its endpoints, and be
> extended by zero outside $J$. Let $\chi$ be a selected sum as in
> Lemma~\ref{can:cutoff-cancellation}. One may integrate
> \eqref{can:label-identity} labelwise against $\psi\chi$ and a bounded
> $C^1$ matrix $\Pi(t)$, including $\Pi=\Id$. More precisely,

The identity is used twice. The first use controls direction: under the bootstrap, a particle's direction of motion cannot change by a prescribed angular amount too many times, and that monotone crossing behaviour improves occupation at intermediate relative angles.

The direction-change lemma [S10:22–37]:

> \begin{lemma}[Direction changes]\label{ang:direction}
> Assume the signed increment bootstrap \eqref{eq:bootstrap} on $[0,\tau]$.
> Let $w$ be a dyad with $w\ge P^{3/5}$, and let $J\subset[0,\tau]$ be a closed
> interval of length at most $(w/P)^2$ on which a supported characteristic
> satisfies $w/8\le q_X\le8w$. Suppose
> \[
>  w^{-3/5}\le\delta\le w^{-1/10}.
> \]
> Starting at the left endpoint of $J$, stop whenever the direction
> $\xi=V_X/|V_X|$ first has chordal distance $\delta$ from its direction at
> the preceding stopping time. Include the last, possibly incomplete,
> interval. For sufficiently large $P$, the number of intervals is at most
> \begin{equation}\label{ang:count}
>  C(M,A)L^6/\delta.
> \end{equation}
> \end{lemma}

Occupation is where the constants become independent of the bootstrap parameters: a single energy budget is shared by all distance and source-angle bins.

The joint-energy-budget occupation bound [S7:353–371]:

> \begin{proposition}[Baseline occupation with a joint energy budget]\label{occ:refined-proposition}
> Suppose $h\leq I$, excluding only deficit bins with $h\leq\lambda$.
> Then
> \begin{equation}\label{occ:refined}
>  \mathsf M\leq C\frac{hk_1}{p}
>              \left(1+\frac I\lambda\mathcal E\right),
>  \qquad
>  \mathcal E=\begin{cases}
>   \mathcal E_{p\phi},&\text{small sector},\\
>   1,&\text{remaining sector}.
>  \end{cases}
> \end{equation}
> Consequently, with
> $R=1+\sqrt{I/\lambda}\sqrt{\mathcal E}$,
> \begin{equation}\label{occ:R-bound}
>  \mathsf M\leq C\frac{hk_1}{p}R^2
> \end{equation}
> for all $h$, except deficit bins with $h\leq\min(I,\lambda)$.
> \end{proposition}

The second use of the identity is the payoff. Selection keeps only the bins whose direct estimate exceeds a summable threshold; on those bins the coefficient of the receiver force is small after summation, and the unselected bins already satisfy the target bound.

The weighted signed estimate, with no `sqrt(w)` [S11:447–454]:

> \begin{proposition}\label{sel:bulk-impulse}
> For the weight $\psi$ above and $P\ge P_*(M,A)$,
> \begin{equation}\label{sel:bulk}
>  \left|\int_J\psi(t)K(t)\,dt\right|
>  \le C_\eta\big[P\sqrt I+(M+\sqrt A)I S(w)\big].
> \end{equation}
> The constant $C_\eta$ is independent of $M,A$.
> \end{proposition}

The coefficient bound that pays for the loss [S11:478–482]:

> For the receiver terms, Lemmas \ref{sel:weight-sum} and
> \ref{sel:exponents} give, at every receiver time,
> \[
>  \sum_{\mathrm{selected}}CU\le Cw^{-1/2}.
> \]

The strategy section says exactly what that factor buys [S4:205–207]:

> coefficient multiplying the receiver force is at most a constant times
> $w^{-1/2}$ after summation. This exactly compensates for the $\sqrt w$
> loss in the available absolute-force bound.

The weighted estimate vanishes at interval endpoints, so short endpoint intervals are restored from the bootstrap assumption itself, giving a strict improvement.

The uniform improvement, and the continuity argument that closes the bootstrap [S12:56–59]:

> Thus every bootstrap interval satisfies the uniform improvement
> \begin{equation}\label{eq:strict-improvement}
>  |V_X(t_2)-V_X(t_1)|\le\tfrac12\mathcal B_w(t_2-t_1).
> \end{equation}

The end of the continuity argument [S12:81–82]:

> This proves relative openness. Hence $\mathcal T=[0,t_*]$ and
> Proposition~\ref{prop:increment} follows.

The bookkeeping that keeps the bootstrap usable in the doubling argument [S12:84–87]:

> The compact-time force bound $C_*$ was used only to propagate the
> bootstrap for a fixed $P$. It does not enter $M,A$ or $P_0$.
> This distinction preserves the uniformity needed in the
> momentum-doubling argument of Section~\ref{sec:setup}.

With the bootstrap in hand, the conclusion is a divergent series. Doubling momentum from `2^(n-1)` to `2ⁿ` takes time at least `c / log(2 + 1024·2ⁿ)`, and the sum over `n` diverges, so the doubling times cannot accumulate below a finite `T_max`.

The momentum-doubling step, verbatim [S5:95–102]:

> At least one term on the right is at least $2^{n-2}$.
> Consequently
> \[
>  t_n-t_{n-1}\ge\Delta_n
>  \ge \frac{c}{\log(2+1024\cdot2^n)}
> \]
> for a fixed $c>0$. The sum of these lower bounds diverges,
> contradicting $t_n<T_{\max}$. Thus $T_{\max}=\infty$.

Smoothness is then propagated by restarting a Sobolev construction near an alleged first loss and identifying the restart with the classical solution by uniqueness; persistence at every Sobolev order follows on the same lifespan, and the equations give all time derivatives.

## History of the conjecture (if known)

The paper's own account of the problem starts from the gap between weak existence and classical regularity [S4:63–70]:

> The distinction between weak existence and classical regularity has
> shaped the Cauchy problem for Vlasov--Maxwell. Wollman established local
> existence and uniqueness for classical solutions~\cite{Wollman1984}.
> DiPerna and Lions developed global weak existence for large
> data~\cite{DiPernaLions1989}; a direct formulation for the relativistic
> one-species system is given by Rein~\cite{Rein2004Weak}.
> These weak existence results do not furnish the regularity and
> uniqueness asserted in Theorem~\ref{thm:global}.

The continuation criterion and the pre-existing global classical results, with the restrictions they used [S4:72–88]:

> For classical solutions, Glassey and Strauss identified bounded
> momentum support as a continuation condition~\cite{GlasseyStrauss1986}
> and proved global existence for initially dilute
> plasmas~\cite{GlasseyStrauss1987}.
> Global classical existence was also established by Glassey and
> Schaeffer in dimensional reductions: one and one-half dimensions,
> two and one-half dimensions, and the planar
> problem~\cite{GlasseySchaeffer1990OneHalf,GlasseySchaeffer1997TwoHalf,
> GlasseySchaeffer1998PlanarI,GlasseySchaeffer1998PlanarII}.
> For the spherically symmetric electrostatic reduction, Glassey and
> Schaeffer proved global classical existence for the repulsive relativistic
> Vlasov--Poisson system~\cite{GlasseySchaeffer1985Symmetric}.
> Rein proved persistence of global existence under small perturbations
> of suitably decaying global reference solutions, including nearly
> symmetric configurations~\cite{Rein1990Generic}.
> These results use restrictions on size, dimension, or the reference
> configuration.

The criterion's title in the literature it comes from [S14:30–41]:

> @article{GlasseyStrauss1986,
>   author  = {Glassey, Robert T. and Strauss, Walter A.},
>   title   = {Singularity formation in a collisionless plasma could
>              occur only at high velocities},
>   journal = {Archive for Rational Mechanics and Analysis},
>   volume  = {92},
>   number  = {1},
>   year    = {1986},
>   pages   = {59--90},

The continuation theory then generated its own methods, and the version used here is Luk–Strain's Theorem 1.1 [S4:90–104]:

> The continuation theory also led to new methods. Klainerman and
> Staffilani gave a Fourier-based proof of the bounded-momentum
> criterion~\cite{KlainermanStaffilani2002}, while Bouchut, Golse and
> Pallard gave a physical-space proof using a division lemma for wave
> kernels~\cite{BouchutGolsePallard2003}. Luk and Strain showed that it
> suffices to control the momentum support after projection onto a
> fixed two-dimensional plane~\cite[Theorem~1.2]{LukStrain2014Continuation}.
> Moment and spatial-density conditions for continuation were developed by
> Pallard~\cite{Pallard2005,Pallard2015Refined}, Sospedra--Alfonso and
> Illner~\cite{SospedraAlfonsoIllner2010}, and Luk and
> Strain~\cite{LukStrain2016Moments}.
> We use the Glassey--Strauss criterion as stated in Luk and
> Strain~\cite[Theorem~1.1]{LukStrain2014Continuation};
> Section~\ref{cont:continuation} verifies its hypotheses for the
> normalization and initial field class considered here.

The small-data line, which relaxes compact momentum support but keeps a particle-smallness hypothesis [S4:106–125]:

> Small-data theory also developed beyond compact momentum support.
> Schaeffer allowed a rapidly decaying momentum tail, retaining compact
> spatial support and a suitable smallness
> condition~\cite{Schaeffer2004}.
> Using a vector-field method with modified commutators, Bigorgne obtained
> global existence and sharp asymptotic estimates under weighted smallness
> assumptions~\cite{Bigorgne2020}.
> His result permits nonzero charge and noncompact particle data.
> Wang proved a small-data result without compact support using vector-field
> and Fourier methods~\cite{Wang2022SmallData}.
> Wei and Yang allow arbitrarily large Maxwell fields with suitable
> spatial decay while requiring a sufficiently small weighted particle
> density~\cite{WeiYang2021}. Bigorgne subsequently proved global
> existence and modified scattering with a small distribution function
> and a large Maxwell field~\cite{Bigorgne2025SmallDistribution}.
> These theorems preserve a particle-smallness hypothesis.
> By prescribing asymptotic data and choosing a sufficiently late starting
> time, Bigorgne also constructs particular global solutions with large
> particle and field norms~\cite{Bigorgne2023ScatteringMap}. This
> construction does not prescribe arbitrary Cauchy data.

The nearest concurrent work is a July 2026 pair of papers by Wang on cylindrically symmetric large data. The paper states the difference in data classes explicitly, and declines to identify the two results [S4:127–136]:

> Wang's July 2026 two-paper treatment establishes global existence for
> large cylindrically symmetric data~\cite{Wang2026I,Wang2026II}.
> The first paper develops an iterative smoothing construction and the
> second supplies pointwise estimates. Their Theorem~1.1 assumes
> $H^s$ fields, $s\ge6$, a weighted $H^s$ particle density, and covariance
> of the data under rotations about a fixed axis. It allows localized
> noncompact particle data and has no smallness requirement.
> The theorem here instead concerns arbitrary compatible compactly
> supported particle data, without symmetry, and fields in the class
> \eqref{eq:data}. Thus the two data classes should not be identified.

The two concurrent papers as the bibliography records them [S14:85–107]:

> @misc{Wang2026I,
>   author = {Wang, Xuecheng},
>   title = {Large Data Global Solution of the {3D RVM} System with
>            Cylindrical Symmetry {I}: Iterative Smoothing Scheme},
>   year = {2026},
>   eprint = {2203.01199},
>   archivePrefix = {arXiv},
>   primaryClass = {math.AP},
>   note = {\href{https://arxiv.org/abs/2203.01199v2}{arXiv:2203.01199v2, 16 July 2026; to appear in Annals of Mathematics}},
>   url = {https://arxiv.org/abs/2203.01199v2}
> }
>
> @misc{Wang2026II,
>   author = {Wang, Xuecheng},
>   title = {Large Data Global Solution of the {3D RVM} System with
>            Cylindrical Symmetry {II}: Pointwise Estimates},
>   year = {2026},
>   eprint = {2607.14685},
>   archivePrefix = {arXiv},
>   primaryClass = {math.AP},
>   note = {\href{https://arxiv.org/abs/2607.14685v1}{arXiv:2607.14685v1}, 16 July 2026},
>   url = {https://arxiv.org/abs/2607.14685v1}
> }

The antecedents of the formulas themselves, which are classical [S4:138–150]:

> The formulas used below have several classical antecedents.
> The retarded-field representation goes back to Glassey and Strauss
> \cite{GlasseyStrauss1986}. Luk and Strain organize its most singular
> terms using electromagnetic components controlled by energy flux
> through light cones~\cite[Proposition~2.2 and Section~3]{LukStrain2014Continuation};
> Pallard also uses the orthogonality of the acceleration kernel to the
> cone's spatial normal~\cite[Lemma~2.1 and Section~2.3]{Pallard2015Refined}.
> The change from retarded phase points to initial particle labels appears
> in Lazarovici~\cite[Lemma~9.2]{Lazarovici2016}.
> The moving-characteristic cone change of variables is used by Pallard
> \cite{Pallard2005}; its proof is also given by Luk and Strain
> \cite[Proposition~5.2]{LukStrain2014Continuation}.
> We derive the required formulas in the normalization~\eqref{eq:rvm}.

Prior (my training data, not repo text): as of my cutoff the open problem was stated as global classical solvability for the full three-dimensional relativistic Vlasov–Maxwell system with arbitrary smooth data of the standard class; Glassey–Strauss 1986 is the standard continuation criterion, Luk–Strain 2014 the standard modern formulation, and the known unconditional global classical results were restricted to symmetry reductions (notably the spherically symmetric Vlasov–Poisson case) plus small-data regimes. A full large-data, no-symmetry, no-smallness global classical theorem for the one-species Maxwell system would have been, at my cutoff, the headline open problem in kinetic PDE, so the claim as stated is a maximal-strength resolution of a long-standing problem rather than a refinement of an existing theorem.

## Consequences now that the proof has been found (if known)

The stated consequence is closure of the problem in the form the literature posed it. The abstract claims exactly that [S3:44–46]:

> The solution remains smooth on every finite time interval. This resolves the
> large-data global classical regularity problem for this model, without size or
> symmetry restrictions on the data.

The paper's own framing of the same claim, with the dimensional specification [S4:54–56]:

> Theorem~\ref{thm:global} resolves the large-data global classical
> regularity problem for this one-species model in three spatial and three momentum
> dimensions. The data have no size or symmetry restriction. The field

Two consequences are visible inside the release, and one is a caution.

The formalization is unusually large for this release and unusually thin at the top. The tree at `lean/OAI/Analysis/VlasovMaxwell/` measures 207 files and 89,993 lines with zero `sorry`, 3,423 `theorem` and `lemma` declarations, and 502 `def`, `abbrev`, `structure` and `class` declarations (measured by `find` and `grep` over that directory, not from a build). Its main file proves the comparator statement in two lines, from a single population-increment lemma.

The formalized main theorem, in full [S18:44–48]:

> theorem global_classical_solution (d : Datum) (hd : Admissible d) :
>     ∃ s : Solution, Classical d s ∧ SmoothOnFiniteHorizons s ∧
>       ∀ s' : Solution, Classical d s' → SameNonnegativeTime s s' := by
>   exact global_classical_of_uniform_physical_increment hd
>     (fun H _ => hd.uniform_physical_population_increment H)

The comparator file states the same theorem with a placeholder proof [S16:103–106]:

> theorem global_classical_solution (d : Datum) (hd : Admissible d) :
>     ∃ s : Solution, Classical d s ∧ SmoothOnFiniteHorizons s ∧
>       ∀ s' : Solution, Classical d s' → SameNonnegativeTime s s' := by
>   sorry

The 102 lines of scaffolding above that placeholder are a verbatim copy of the formalization's own model file: comparator lines 10–101 [S16:10–101] match `Model.lean` lines 13–104 [S19:13–104] line for line, so the challenge is stated in the same vocabulary the solution uses. The scope note states what the formalization covers [S15:9]:

> The formalized result gives global existence and uniqueness for the three-dimensional one-species relativistic Vlasov–Maxwell system. The initial particle density is nonnegative, smooth, and compactly supported; the initial fields have bounded derivatives of all orders, finite energy, and satisfy both Gauss constraints. The solution is smooth on every finite time interval, has compact particle phase support there, and is unique among classical solutions. No smallness, symmetry, or neutrality assumption is imposed.

The second consequence is ledger-visible and is the contrast case for the evidence columns. Family 362 is one of the families the release's own index does record: it appears as a bibliography entry [S20:392–395] and as a `main_results` entry [S20:1757–1759]:

>     - comparator_config: ComparatorChallenges/VlasovMaxwell.json
>       declaration: OAI.RVM.global_classical_solution
>       file: OAI/Analysis/VlasovMaxwell/Main.lean

That index entry is the mechanical reason the ledger reports one formalized manuscript and one `main_results` config for this family. The comparator configuration names the same declaration and solution module, with three permitted axioms and Nanoda disabled [S17:1–14]:

> {
>   "challenge_module": "ComparatorChallenges.VlasovMaxwell",
>   "solution_module": "OAI.Analysis.VlasovMaxwell.Main",
>   "theorem_names": [
>     "OAI.RVM.global_classical_solution"
>   ],
>   "definition_names": [],
>   "permitted_axioms": [
>     "propext",
>     "Quot.sound",
>     "Classical.choice"
>   ],
>   "enable_nanoda": false
> }

The ledger row for family 362 is [S21:358]: one manuscript, one formalized manuscript, tier T3, one comparator challenge, one `main_results` entry, a scope note of 519 characters, no verification directory, no coverage document, a reasoning trace named `relativistic-vlasov-maxwell`, claim-shape tags `bound`, `density` and `uniform`, no conditional tag, no named-conjecture resolution, and no summary page before this one.

The caution is the third consequence, and the paper raises it itself: the concurrent cylindrically symmetric large-data result of July 2026 covers a different data class, and the paper declines to identify the two theorems [S4:134–136]:

> The theorem here instead concerns arbitrary compatible compactly
> supported particle data, without symmetry, and fields in the class
> \eqref{eq:data}. Thus the two data classes should not be identified.

What has not been checked: nothing here is a machine-checked verification of the manuscript. The comparator file contains a `sorry` [S16:106], the release marks its formalizations as agent-generated and unchecked, and no build was run. The reasoning trace is a six-page PDF, so its content is not quotable from this page.

## Sources

Manuscript root: `preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026`.

The manuscript ships a `README.md` [S2:1–17] whose citation block gives the release bibtex key [S2:10–16]. The scope note [S15:1–15] links the manuscript PDF at [S15:5] and the comparator file at [S15:15]. The shipped PDF of the manuscript is [S23] and the shipped PDF of the reasoning trace is [S22]; both are binary and are cited here by whole-file marker only.

Section map, read from the manuscript's own include list [S3:49–58]:

- `build/sections/introduction.tex` — model, datum, theorem, history, strategy [S4]
- `build/sections/setup.tex` — bootstrap, doubling, proof of the theorem [S5]
- `build/sections/retarded.tex` — light-cone representation and kernels [S6]
- `build/sections/occupation.tex` — occupation of retarded bins [S7]
- `build/sections/direct.tex` — direct integrated force bounds [S8]
- `build/sections/cancellation.tex` — signed integration-by-parts identity [S9]
- `build/sections/direction.tex` — direction changes and improved occupation [S10]
- `build/sections/selection.tex` — selection and the weighted signed estimate [S11]
- `build/sections/closure.tex` — endpoint restoration and bootstrap closure [S12]
- `build/sections/continuation.tex` — local theory and the continuation criterion [S13]
- `build/references.bib` — the 32-entry bibliography [S14]

| ID | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release blurb, manuscript link, abstract |
| S2 | [`preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/README.md`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/README.md) | 18 | Manuscript README and bibtex key |
| S3 | [`build/main.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/main.tex) | 61 | Title, abstract, section include list |
| S4 | [`build/sections/introduction.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/introduction.tex) | 227 | Model, theorem, history, strategy |
| S5 | [`build/sections/setup.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/setup.tex) | 140 | Bootstrap and momentum doubling |
| S6 | [`build/sections/retarded.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/retarded.tex) | 428 | Retarded field representation |
| S7 | [`build/sections/occupation.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/occupation.tex) | 416 | Occupation of retarded bins |
| S8 | [`build/sections/direct.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/direct.tex) | 428 | Direct integrated force bounds |
| S9 | [`build/sections/cancellation.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/cancellation.tex) | 382 | Weighted signed formula |
| S10 | [`build/sections/direction.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/direction.tex) | 377 | Direction-change lemma |
| S11 | [`build/sections/selection.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/selection.tex) | 488 | Selection and weighted estimate |
| S12 | [`build/sections/closure.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/closure.tex) | 87 | Bootstrap closure |
| S13 | [`build/sections/continuation.tex`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/continuation.tex) | 490 | Local theory, continuation criterion |
| S14 | [`build/references.bib`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/references.bib) | 372 | Bibliography |
| S15 | [`lean/docs/362.md`](../../../lean/docs/362.md) | 15 | Scope note |
| S16 | [`lean/ComparatorChallenges/VlasovMaxwell.lean`](../../../lean/ComparatorChallenges/VlasovMaxwell.lean) | 112 | Comparator challenge |
| S17 | [`lean/ComparatorChallenges/VlasovMaxwell.json`](../../../lean/ComparatorChallenges/VlasovMaxwell.json) | 14 | Comparator configuration |
| S18 | [`lean/OAI/Analysis/VlasovMaxwell/Main.lean`](../../../lean/OAI/Analysis/VlasovMaxwell/Main.lean) | 54 | Formalized main theorem |
| S19 | [`lean/OAI/Analysis/VlasovMaxwell/Model.lean`](../../../lean/OAI/Analysis/VlasovMaxwell/Model.lean) | 109 | Formalized model scaffolding |
| S20 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1,783 | Release index of papers and results |
| S21 | [`notes/catalog.tsv`](../../../notes/catalog.tsv) | 373 | Reading ledger row for family 362 |
| S22 | [`reasoning_traces/relativistic-vlasov-maxwell.pdf`](../../../reasoning_traces/relativistic-vlasov-maxwell.pdf) | — | Published reasoning trace |
| S23 | [`paper.pdf`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf) | — | Manuscript PDF |
