# 271 — Bloch's law and spontaneous ferromagnetic order (Mathematical physics, 4 manuscripts, tier T2)

## Original CONTENTS.md summary

**271. Bloch's law, its lattice correction, and the spherical magnetization law.** Proves Bloch's *T*^(3/2) law with its exact coefficient for three-dimensional quantum Heisenberg ferromagnets at every positive quantum spin, allowing nonnegative symmetric finite-range couplings whose support generates ℤ^3. The thermodynamic limit precedes the zero-field derivative and low-temperature limit. The family also proves spontaneous magnetization for nearest-neighbor models in every dimension *d* ≥ 3 and determines the first lattice correction for three-dimensional nearest-neighbor couplings. ([Lean](../../../lean/docs/271.md))

The blurb above is reproduced from [S1:6849]; the release sets the temperature and the dimension in italic markup and writes the lattice and the exponent as superscripts, and this page renders them as *T*^(3/2), ℤ^3, and *d* ≥ 3. The blurb names three of the family's four manuscripts; the fourth is the September-24 paper on spontaneous magnetization, and it is the only manuscript the scope note names [S56:5].

## Undergraduate summary

A quantum Heisenberg ferromagnet is a lattice of tiny quantum magnets: here a three-dimensional grid carrying one spin-*S* particle per site, with an energy that is lowest when neighbouring spins point the same way. Two questions about it are separate. The first asks how large the magnetization is at low temperature. Bloch's 1930 answer is that it falls short of saturation by a multiple of *T*^(3/2), the shortfall being the population of long-wavelength spin waves; making that counting rigorous means controlling an interacting quantum many-body system rather than a gas of independent waves. The second question asks whether the magnetization survives at all once the external field is switched off. Mermin and Wagner ruled out positive-temperature order for the isotropic model in one and two dimensions, which left the three-dimensional quantum ferromagnet as the case in question; Lieb posed it as an open problem in 1999, and accounts from 2025 and 2026 still described it as open [S4:101–110].

Family 271 answers both questions, plus a third that sits between them. The September-24 manuscript proves that the nearest-neighbour model does have an equilibrium state that magnetizes itself with no field applied, in every dimension *d* ≥ 3, at every spin, at every sufficiently low positive temperature [S43:43–50]. The first October-5 manuscript proves the *T*^(3/2) law with its exact leading coefficient for every nonnegative symmetric finite-range coupling whose support generates ℤ^3, anisotropic couplings included [S3:43–50]. The second October-5 manuscript sharpens that asymptotic for the nearest-neighbour case by one power of the temperature, producing the first lattice correction [S14:49–57]. The third proves the spherical magnetization law, which identifies the whole zero-field distribution of the magnetization vector rather than only its size [S29:53–61].

Two things tie the four manuscripts together. The first is a single representation: a spin-*S* particle is rewritten as 2*S* spin-½ slots sitting at one site, only their symmetric combinations are kept, and the quantum statistical mechanics becomes a gas of random exchange paths through space-time, so that questions about magnetization turn into probability estimates about those paths. The second is a fixed order of limits. Magnetization is defined as a derivative at zero field of the pressure of the infinite system, so the volume must go to infinity first, the field must be removed next, and the temperature may only then be taken to zero. Each manuscript states that order in its own introduction [S4:81–83].

**Proof sketch.** The September-24 paper is the root. It replaces each spin by 2*S* spin-½ slots, runs rate-½ Poisson transpositions between neighbouring sites, and reads the partition function as a gas of exchange cycles in which each cycle carries a weight of two spin colours. A pin is a slot-time point whose cycle is forced to be up, which cuts that cycle's weight to one. Pin the entire boundary for an entire time period and the question becomes: how likely is an interior slot to sit on a cycle that never touches the boundary? The answer is a downward induction on the number of pins, fed by a sparse-set test that converts the estimate into a return probability for one Markov walk, a local Nash inequality plus routed finite-energy flows that bound that walk's quadratic loss, and a final averaging step that turns the resulting macroscopic magnetization tail into a translation-invariant KMS state [S44:170–237]. The Bloch-law paper runs the same pin machinery at a fixed small field, identifies the ideal-walk return kernel with the magnon density, and controls arbitrarily late returns so that the coefficient is fixed by the full dispersion determinant and not by a sublattice approximation [S4:167–179]. The lattice-correction paper adds a finite-dimensional capacity criterion that keeps the whole Bose sum, and the spherical-law paper adds spatial comparison on periodic tori together with a zero-freeness argument for products of matrices that excludes coexisting magnetization lengths [S15:134–141] [S30:186–200].

## Graduate summary

Manuscript A fixes the observable before it fixes the asymptotics. Its magnetization is a right field derivative taken after the thermodynamic limit, and its coefficient is built from the quadratic part of the one-magnon dispersion [S4:42–52]:

> \begin{equation}
>  p_\beta(h)=\lim_{N\to\infty}\frac1{\beta|\Lambda_N|}
>        \log\Tr e^{-\beta(H^J_{S,N}-hM_{S,N})},
>  \qquad m_{S,J}(\beta)=\partial_h^+p_\beta(0).
>  \label{eq:pressure-magnetization}
> \end{equation}
> The finite-range pressure limit exists and is convex and $S$-Lipschitz;
> Section~\ref{sec:pressure} recalls the proof. Rotation by $\pi$ about
> the $x$-axis makes the pressure even, so $m_{S,J}(\beta)\in[0,S]$.
> The derivative selects the magnetization in a field tending to zero
> through positive values after the thermodynamic limit.

The theorem is then a sharp limit at fixed spin and fixed interaction [S4:68–77]:

> \begin{theorem}[Bloch's law]
> \label{thm:main}
> For every fixed $S\in\{\tfrac12,1,\tfrac32,\ldots\}$ and every
> interaction satisfying \eqref{eq:interaction},
> \begin{equation}
>  \lim_{\beta\to\infty}\beta^{3/2}\bigl(S-m_{S,J}(\beta)\bigr)
>    =\frac{\zeta(3/2)}{8\pi^{3/2}\sqrt{\det D_{S,J}}}.
>  \label{eq:bloch-law}
> \end{equation}
> \end{theorem}

The determinant of *D*_(S,J) is the whole content of the coefficient, so the theorem covers spatially anisotropic finite-range couplings, and the nearest-neighbour case is the specialization *D*_(S,J) = *SI*. The paper is explicit that the ordering of limits is part of the claim: "The order of limits is part of the assertion: first volume tends to infinity at fixed $\beta,h$, then $h\downarrow0$, and finally $\beta\to\infty$, with $S,J$ fixed." [S4:81–83] It is also explicit about why the existing free-energy results do not already give this: "A zero-field free-energy estimate does not by itself control the one-sided field derivative that defines spontaneous magnetization." [S4:120–122] The coefficient itself comes from the ideal walk on the full bond set, whose heat kernel satisfies "The ideal walk has site jump rates $SJ(z)$, and its heat kernel $p_t^{S,J}$ satisfies" a *t*^(-3/2) decay with constant κ = (4π)^(-3/2)(det *D*_(S,J))^(-1/2), and the paper adds that "the full jump kernel determines this coefficient." [S4:167–179] The field is handled as a mixture of extra pins, whose selection probability is bounded, so that at fixed β the relevant neighbourhood is pin-free with probability tending to one as *h* ↓ 0 [S4:203–206].

Manuscript B is the lattice correction: it compares the true deficit with the full ideal-magnon density built from the lattice dispersion, not with its continuum approximation [S15:45–63]:

> \begin{theorem}\label{thm:main}
> For every fixed $S\in\{\tfrac12,1,\tfrac32,\ldots\}$,
> \[
>  \lim_{\beta\to\infty}(\beta S)^{5/2}
>        \bigl[S-m_S(\beta)-n_S^{\mathrm{sw}}(\beta)\bigr]=0.
> \]
> \end{theorem}
>
> Expanding the lattice heat kernel gives the following explicit form.
> Here $\zeta$ denotes the Riemann zeta function.
> \begin{corollary}\label{cor:expansion}
> For every fixed positive half-integer $S$,
> \[
>  S-m_S(\beta)
>  =\frac{\zeta(3/2)}{8\pi^{3/2}}(\beta S)^{-3/2}
>   +\frac{3\zeta(5/2)}{128\pi^{3/2}}(\beta S)^{-5/2}
>   +o\bigl((\beta S)^{-5/2}\bigr).
> \]
> \end{corollary}

The mechanism that keeps the subleading term is a capacity criterion stated in finite dimensions: "It applies to nonselfadjoint contraction kernels, so no reversibility of the exposed environment is needed." and, because the trial potential sums returns over all positive periods, "the capacity comparison therefore retains the full Bose sum." [S15:138–141] Its magnetization definition is the same one-sided derivative, and it says so: "Thus the volume limit precedes the zero-field limit in the definition of $m_S$." [S15:33–34]

Manuscript C is the strongest of the three October-5 results in the sense that it identifies a distribution rather than a number [S30:45–64]:

> \begin{theorem}[Spherical magnetization law]\label{thm:main}
> For each fixed $S$ there is a finite $\beta_0(S)$ such that, for every
> fixed finite $\beta\ge\beta_0(S)$, one has $m=m_{S,\beta}>0$ and
> \begin{equation}\label{eq:spherical-law}
>  \lim_{\substack{L\to\infty\\L\text{ even}}}
>   \left\langle
>      \exp\!\left(\frac1V\sum_{a=1}^3t_aM_L^a\right)
>   \right\rangle_{\beta,L}
>    =\frac1{4\pi}\int_{\mathbb S^2}e^{m t\cdot n}\dd\sigma(n)
>    =\frac{\sinh(m|t|)}{m|t|}
>  \qquad(t\in\R^3).
> \end{equation}
> Here $\sigma$ is surface-area measure on $\mathbb S^2$, and the quotient
> at $t=0$ is interpreted as $1$. In addition,
> \begin{equation}\label{eq:second-moment-law}
>  \lim_{\substack{L\to\infty\\L\text{ even}}}
>    \frac1{V^2}\sum_{x,y\in\Lambda_L}
>           \langle S_x\cdot S_y\rangle_{\beta,L}=m^2.
> \end{equation}
> \end{theorem}

The test functions are self-adjoint linear combinations of the three spin components, so the statement is about a law of a noncommuting triple without measuring it jointly: "The statement uses self-adjoint linear combinations of the spin components. It requires no joint finite-volume measurement of these noncommuting operators." [S30:66–68] Its lower bound rests on two facts, "Two facts produce the lower bound." — local squared magnetization is controlled by the global squared magnetization, and "every translation-ergodic equilibrium state has magnetization vector of length $m$." [S30:142–147] The pressure step represents the perturbations as products of matrices on the 2*S* slots and uses that "For every realization, $Z(z)$ is nonzero on $\Rea z>0$." [S30:193–194]

The root paper's claim is the ordering statement itself [S44:64–73]:

> \begin{theorem}\label{thm:main}
> For every integer $d\geq3$ and every
> $S\in\{\frac12,1,\frac32,\ldots\}$, there is a finite
> $\beta_0(d,S)>0$ such that, for every finite $\beta\geq\beta_0(d,S)$,
> the dynamics associated with \eqref{eq:hamiltonian} has a
> translation-invariant $\beta$-KMS state $\omega$ satisfying
> \[
>                          \omega(S_0^z)\ge S/4.
> \]
> \end{theorem}

The bound is a property of the selected state, not of the model: "This magnetization is a property of the chosen state and need not be retained by a rotation-invariant average." [S44:77–78] The proof is a pin induction. Slots are created by "Replace a spin $S$ by $\ell=2S$ spin-$\frac12$ slots at its site and project onto their symmetric subspace." [S44:160–162] and the core estimate is proved "by downward induction on the number of grid pins" [S44:171] on sparse test sets. Adding the test set *T* to the existing pins *E* gives an avoidance probability of at most (2*r*)^m, where *r* is the mean fraction of test points whose lines return to *T* before reaching *E*, so "It therefore suffices to use the larger-pin induction hypothesis to prove $r\le p/2$." [S44:185–186] Identifying *r* requires exposing exactly the cycles that miss the enlarged pin set, and the paper is explicit that this step buys a Markov comparison without claiming independence: "The exposure itself is still averaged under its original $P$-law; no independence of the conditioned cycles is required." [S44:195–196] The comparison is a quadratic loss for a one-period kernel *U* [S44:202–204]:

> \[
>                  m(1-r)\ge\mathbb E_P\langle f,(I-U)f\rangle.
> \]

Bounding that loss is where the geometry enters: a local Nash inequality spreads the mass initially on *T*, routed decaying finite-energy flows control its pairing with the propagated part, and short portions at both ends of a period absorb the pairing into the dissipated energy, giving a loss of at least *m*(1 − ε(*p*)) with "with $\varepsilon(p)=o(p)$. Choose $p$ small enough that $2\varepsilon(p)\le p$" [S44:225–226], which closes the induction. The state is then produced from the resulting surface-order tail; the field is the explicit volume-dependent sequence *h*_*N* = *N*^(-1/2), translations are averaged, and every subsequential limit satisfies [S51:136–138]

> \begin{equation}\label{eq:positive-limit-magnetization}
>  \omega(S_0^z)\geq S/4.
> \end{equation}

The selection step is described as follows: the pin estimate yields a macroscopic magnetization tail in the free zero-field Gibbs state, and the KMS section "selects this tail with a homogeneous field tending to zero as the boxes grow, and averages translations" [S44:234–235], verifying both KMS strip boundaries for the same limiting state and the original zero-field dynamics.

The formalization covers this root paper and nothing else in the family. Its headline theorem is [S59:60–65]

> theorem spontaneous_magnetization (d ℓ : ℕ) (hd : 3≤d) (hℓ : 1≤ℓ) :
>     DynamicsConverges d ℓ ∧
>       ∃ β₀ : ℝ,0<β₀ ∧ ∀ β : ℝ,β₀≤β →
>         ∃ ω : State d ℓ,TranslationInvariant ω ∧ IsKMS β ω ∧
>           (ω.functional (spinZ d ℓ 0)).im=0 ∧
>           (ℓ:ℝ)/8≤(ω.functional (spinZ d ℓ 0)).re := by

The formalized statement is the manuscript's statement in the slot parameter: the site Hilbert space is built as `abbrev Level (ℓ : ℕ) := Fin (ℓ + 1)` [S60:55], so a spin-*S* system is ℓ = 2*S*, and the formal bound ℓ/8 is exactly the manuscript's *S*/4 rather than a weaker encoding of it. The formalized version adds that the selected observable has zero imaginary part, and it conjoins convergence of the finite-volume dynamics to the infinite-volume dynamics. The scope note states both [S56:9–11]:

> The formalization proves spontaneous magnetization for the nearest-neighbor isotropic quantum Heisenberg ferromagnet on $\mathbb Z^d$ for every $d\ge3$ and every spin $S\in\{\tfrac12,1,\tfrac32,\ldots\}$. At every sufficiently low positive temperature, it constructs a translation-invariant equilibrium state satisfying the KMS condition for the zero-field dynamics and having magnetization at least $S/4$.
> It also proves convergence of the finite-volume dynamics to the infinite-volume dynamics used in the KMS statement.

## History of the conjecture (if known)

The magnetization side begins with "Bloch derived the $T^{3/2}$ reduction from long-wavelength spin waves" in 1930, followed by the Holstein–Primakoff bosonic representation and Dyson's interaction expansion [S4:87–90]. Dyson's own numbers are the historical benchmark that manuscript B is calibrated against: in his expansion "the terms of orders \(T^{5/2}\) and \(T^{7/2}\) in the magnetization already arise from the lattice dispersion of independent magnons" and "the leading interaction contribution is of order \(T^4\)" [S15:73–76], and manuscript A records the limit of what Dyson claimed: "his estimates of the remaining higher-order terms were not a rigorous fixed-spin proof of the asymptotic law" [S4:92–93]. Effective-field-theory calculations retain the same distinction [S15:78–79].

The rigorous thermodynamic line is a separate sequence: "The free energy has a different rigorous history." [S4:116] Conlon and Solovej, then Tóth via a random-stirring representation, gave free-energy bounds, and Correggi, Giuliani, and Seiringer proved the leading spin-wave free-energy asymptotic on ℤ^3 at every fixed spin [S4:116–120] [S15:85–91]. Benedikter's interaction correction sits in a different regime, "Benedikter obtained an interaction correction as a free-energy upper bound in the different regime \(S\to\infty\) with \(\beta S\) fixed" [S15:92–94], and Klippel's 2026 result is the two-dimensional free-energy analogue: "the present result constructs an ordered state at a fixed positive temperature in $d\ge3$" [S44:144–145].

The ordering side is where the open problem sits. "Mermin and Wagner excluded positive-temperature spontaneous magnetic order for the one- and two-dimensional isotropic Heisenberg models under their finite-range hypotheses" [S4:101–104]; infrared bounds gave symmetry breaking for classical models and ordering for quantum antiferromagnets, results that "do not supply the isotropic ferromagnetic ordering input used here" [S30:76–79]. That leaves the isotropic three-dimensional quantum ferromagnet, "left the standard three-dimensional quantum ferromagnet as a separate problem, recorded by Lieb" in 1999 "and still discussed as open in recent accounts" [S4:107–110]. Manuscript D states the problem's provenance precisely: "Seiringer's 2025 account records it using a volume-averaged finite-volume two-point order parameter" [S44:148–150], and it states the form in which it is resolved: "Theorem 1 resolves the low-temperature ordering problem in the spontaneous-magnetization formulation stated here" [S44:150–152], adding that "the finite-volume correlation criterion in the cited account is a different formulation and is not used in this proof." [S44:155–156]

The spherical law has named antecedents. Ueltschi's survey of three-dimensional loop models derives the same sinh transform for the spin-½ ferromagnet, "conditional on a conjectured Poisson--Dirichlet law for macroscopic loops" [S30:87–89], and Björnberg, Fröhlich, and Ueltschi prove the spherical transform for the complete-graph model at arbitrary fixed spin. Manuscript C's contribution is the lattice case: "We prove its magnetization law without assuming a distribution for macroscopic loop lengths." [S30:93–94] The probabilistic machinery the family shares is older than any of it: Tóth's cycle representation for spin ½, Nachtergaele's realization of spin *S* inside the symmetric tensor product of 2*S* spin-½ spaces, the Borcea–Brändén–Liggett stable-polynomial approach to negative dependence, and Nash's energy method [S4:126–131] [S15:96–99]. Field selection goes back to Griffiths 1966 and the first section of Dyson–Lieb–Simon [S51:113–116], and the boson reading of the result follows Matsubara and Matsuda [S44:241].

## Consequences now that the proof has been found

The family's own stated consequence is a hard-core boson statement. The Matsubara–Matsuda correspondence "turns the ordered state into a state with averaged off-diagonal long-range order." [S44:242–243] For *S* = ½, writing *b*_*x* = *S*_*x*^− and *n*_*x* = *b*_*x*^†*b*_*x* = *S*_*x*^z + ½ makes the Hamiltonian "This is the particle--hole-symmetric attractive hard-core hopping model." [S44:254] Rotating the mean spin vector to the *x* direction commutes with the zero-field dynamics and with translations, so the rotated state ν is again translation-invariant and β-KMS, and "It satisfies $\nu(b_x)=r\ge1/8$ and $\nu(n_x)=1/2$, where $r$ is the length of the original mean-spin vector." [S44:260–262] Positivity then gives [S44:271–276]

> \[
>  \frac1{|\Lambda|^2}\sum_{x,y\in\Lambda}\nu(b_x^\dagger b_y)
>        \ge\frac1{64},
>  \qquad
>  \nu(a_\Lambda^\dagger a_\Lambda)\ge\frac{|\Lambda|}{64}.
> \]

so "The first bound gives averaged off-diagonal long-range order" [S44:277] and "the uniform-mode occupation is at least $1/32$ of the expected particle number." [S44:279–280] The paper marks the boundary of that claim: "These bounds concern restrictions of the chosen infinite-volume state, not finite-volume Gibbs states." [S44:281–282]

Internally, the family has a single root. Manuscript D's 36-entry bibliography contains no OpenAI self-citation [S54], while A cites D [S11:96–101], B cites both A and D [S26:77–89], and C cites both A and D [S40:146–160]. The three October-5 papers say what they take: B writes "Within this framework, two companion manuscripts provide the direct inputs." [S15:100] and C frames the division of labour as "The existence of spontaneous magnetization and the identification of its zero-field distribution are distinct questions." [S30:96–97], adding "We use finite exchange and geometric estimates from these works." [S30:104] So the ordering result is the load-bearing one, and the two asymptotic results and the distributional result are consequences of its estimates plus new arguments of their own.

Formalization coverage is confined to the root. The Lean tree for this family is 128 files and 25,400 lines with 0 `sorry` and 323 top-level theorems, and the headline theorem is the comparator target: the challenge file names `OAI.Heisenberg.spontaneous_magnetization` as its theorem, with the solution module `OAI.MathematicalPhysics.Heisenberg.Main` and the three standard permitted axioms [S58], pointing at the 218-line comparator statement [S57:14] and the 88-line KMS layer that Main.lean imports and nothing else [S59:1] [S61]. Grepping the tree for Bloch, magnon, spherical, and lattice-correction vocabulary returns nothing, so none of the three October-5 results is formalized in any form. The scope note is consistent with that: it links only the September-24 PDF [S56:5] and its Scope section names only the ordering statement and the dynamics convergence [S56:9] [S56:11], with no exclusion language.

Two ledger facts follow mechanically and should be read as index gaps, not as absences. The family has 4 manuscripts, tier T2, 1 comparator challenge, 1 scope note, and a published reasoning trace; its `paps_form` and `main_results` counts are 0 because `lean/formalization.yaml` contains no entry naming Heisenberg at all [S62], which is why the challenge is invisible to the release's own results index. Its `resolves_named` flag is 0, while manuscript D states an explicit resolution of a named problem posed by Lieb [S44:147–152]; the ledger's keyword rule did not see it.

The reasoning trace is the September-24 paper's trace and ships as a PDF only, with no LaTeX source, so its text is not quotable here [S63]. It runs six pages in six sections, from comparison attempts to a simultaneous pin test, through geometry and heat leakage, exposure separated from conditional first moments, precise routing and stopping rules, a trap-and-correlation check, and closing the estimates and selecting the state; it states the target as a nonzero mean-spin triple and reports that the *S*/4 constant comes from the field-selection estimate. Six of its nine references — Aizenman–Nachtergaele, Benjamini–Pemantle–Peres, Caputo–Liggett–Richthammer, Elboim–Sly, McBryan–Spencer, and Ueltschi 2013 — appear nowhere in the manuscript's 36-entry bibliography [S54], so the trace's reading path is wider than the paper's citation path.

## Sources

Manuscript root: `preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/`. Every path below is repo-relative; the four manuscript trees each ship a README with their bibtex entry [S2] [S13] [S28] [S42], a LaTeX source tree, and the compiled PDF, and the release links the PDFs from the family block [S1:6856] [S1:6865] [S1:6874] [S1:6883].

Section map, read from each manuscript's own include list. Manuscript A includes seven sections and a bibliography file [S3:53–60]: the introduction, then the slot and pin algebra [S5], the lattice geometry [S6], the finite-range pin bootstrap [S7], the bound on arbitrarily late returns [S8], the ideal kernel that fixes the coefficient [S9], the pressure step [S10], and the bibliography [S11]; its compiled PDF is [S12]. Manuscript B includes nine sections and a bibliography [S14:60–69]: the introduction, the exchange-loop representation [S16], the joint snapshot pin bounds and path estimates [S17], the capacity criterion [S18], the free trial potential [S19], the signed cancellation and Duhamel identities [S20], the scalar residual pairing [S21], the residuals against Dirichlet energy [S22], the pressure step and the expansion corollary [S23], and the bibliography [S26], with two figure sources [S24] [S25] and the compiled PDF [S27]. Manuscript C includes eight sections [S29:64–71]: the introduction, the exchange representation on the torus [S31], the sparse pin estimates [S32], the local-to-global squared-magnetization comparison [S33], the zero-field magnetization distribution [S34], the equilibrium and ergodic-state step [S35], the matrix-product perturbations and zero-freeness [S36], the global spin limit [S37], with two figure sources [S38] [S39], the bibliography [S40], and the compiled PDF [S41]. Manuscript D includes eight sections [S43:53–60]: the introduction, the exchange-path representation and spectral law [S45], the stable multiaffine pin test [S46], the exposure, determinant, and conditional first moment [S47], the sparse anchors and obstacle components [S48], the routed finite-energy flows [S49], the heat leakage and quadratic loss [S50], the vanishing-field selection and KMS verification [S51], with two figure sources [S52] [S53], the bibliography [S54], and the compiled PDF [S55].

| ID | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release contents: family 271 blurb and the four manuscript links |
| S2 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/README.md`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/README.md) | 18 | Manuscript A README and bibtex entry |
| S3 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/main.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/main.tex) | 61 | Manuscript A title, date, abstract, section list |
| S4 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/01-introduction.tex) | 210 | Manuscript A model, theorem, history, inputs |
| S5 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/02-pins.tex) | 719 | Slot and pin algebra |
| S6 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/03-geometry.tex) | 532 | Lattice geometry for the pin estimates |
| S7 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/04-bootstrap.tex) | 565 | Finite-range pin bootstrap |
| S8 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/05-returns.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/05-returns.tex) | 214 | Long-return bound |
| S9 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/06-ideal.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/06-ideal.tex) | 411 | Ideal kernel and the Bloch coefficient |
| S10 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/07-pressure.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/sections/07-pressure.tex) | 194 | Field as extra pins; pressure step |
| S11 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/references.tex`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/references.tex) | 117 | Manuscript A bibliography, including the companion entry |
| S12 | [`preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf) | — | Manuscript A compiled PDF |
| S13 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/README.md`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/README.md) | 18 | Manuscript B README and bibtex entry |
| S14 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/main.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/main.tex) | 70 | Manuscript B title, date, abstract, section list |
| S15 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/01-introduction.tex) | 156 | Manuscript B model, theorem, corollary, history, companions |
| S16 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/02-loops.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/02-loops.tex) | 198 | Exchange-loop representation |
| S17 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/03-geometry.tex) | 552 | Joint snapshot pin bounds; path and heat-kernel estimates |
| S18 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-capacity.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-capacity.tex) | 150 | Capacity criterion |
| S19 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-profiles.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/04-profiles.tex) | 239 | Free trial potential |
| S20 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/05-sources.tex) | 315 | Signed cancellation and Duhamel identities |
| S21 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/06-scalar.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/06-scalar.tex) | 337 | Scalar residual pairing |
| S22 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/07-energy.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/07-energy.tex) | 485 | Residuals against Dirichlet energy |
| S23 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/08-pressure.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/sections/08-pressure.tex) | 300 | Right derivative of the pressure; corollary |
| S24 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/figures/isolated-surgery.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/figures/isolated-surgery.tex) | 44 | Manuscript B figure source |
| S25 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/figures/period-averaging.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/figures/period-averaging.tex) | 32 | Manuscript B figure source |
| S26 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/references.tex`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/references.tex) | 98 | Manuscript B bibliography, including both companion entries |
| S27 | [`preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf) | — | Manuscript B compiled PDF |
| S28 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/README.md`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/README.md) | 18 | Manuscript C README and bibtex entry |
| S29 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/main.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/main.tex) | 74 | Manuscript C title, date, abstract, section list |
| S30 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/01-introduction.tex) | 223 | Manuscript C model, theorem, antecedents, strategy |
| S31 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/02-exchange.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/02-exchange.tex) | 480 | Exchange representation on the torus |
| S32 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/03-sparse-pins.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/03-sparse-pins.tex) | 693 | Sparse pin estimates |
| S33 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/04-spatial-comparison.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/04-spatial-comparison.tex) | 734 | Local-to-global squared-magnetization comparison |
| S34 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/05-zero-field.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/05-zero-field.tex) | 281 | Zero-field magnetization distribution |
| S35 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/06-equilibrium.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/06-equilibrium.tex) | 276 | Equilibrium and ergodic states |
| S36 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/07-pressure.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/07-pressure.tex) | 560 | Matrix-product perturbations; zero-freeness |
| S37 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/08-global-spin.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/sections/08-global-spin.tex) | 138 | Global spin and the spherical limit |
| S38 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/figures/holes-comparison.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/figures/holes-comparison.tex) | 72 | Manuscript C figure source |
| S39 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/figures/sparse-ghost.tex`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/figures/sparse-ghost.tex) | 19 | Manuscript C figure source |
| S40 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/references.bib`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/references.bib) | 275 | Manuscript C bibliography, including both companion entries |
| S41 | [`preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) | — | Manuscript C compiled PDF |
| S42 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/README.md`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/README.md) | 18 | Manuscript D README and bibtex entry |
| S43 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/main.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/main.tex) | 63 | Manuscript D title, date, abstract, section list |
| S44 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/00-introduction.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/00-introduction.tex) | 295 | Manuscript D theorem, history, strategy, boson consequence |
| S45 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/01-loops.tex) | 397 | Exchange-path representation and spectral law |
| S46 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/02-pin-test.tex) | 443 | Stable multiaffine pin test |
| S47 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/03-exposure.tex) | 644 | Exposure, determinant, conditional first moment |
| S48 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/04-sparse-geometry.tex) | 499 | Sparse anchors and obstacle components |
| S49 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/05-flows.tex) | 418 | Routed finite-energy flows |
| S50 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/06-leakage.tex) | 612 | Heat leakage and the quadratic loss |
| S51 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/sections/07-kms.tex) | 493 | Vanishing-field selection; KMS verification |
| S52 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/figures/exposure-first-moment.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/figures/exposure-first-moment.tex) | 38 | Manuscript D figure source |
| S53 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/figures/hull-routing.tex`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/figures/hull-routing.tex) | 91 | Manuscript D figure source |
| S54 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/references.bib`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/references.bib) | 382 | Manuscript D bibliography: 36 entries, no OpenAI self-citation |
| S55 | [`preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf) | — | Manuscript D compiled PDF, the one the scope note links |
| S56 | [`lean/docs/271.md`](../../../lean/docs/271.md) | 17 | Scope note: scope statement and comparator links |
| S57 | [`lean/ComparatorChallenges/Heisenberg.lean`](../../../lean/ComparatorChallenges/Heisenberg.lean) | 218 | Comparator challenge statement |
| S58 | [`lean/ComparatorChallenges/Heisenberg.json`](../../../lean/ComparatorChallenges/Heisenberg.json) | 14 | Challenge configuration: theorem, modules, axioms |
| S59 | [`lean/OAI/MathematicalPhysics/Heisenberg/Main.lean`](../../../lean/OAI/MathematicalPhysics/Heisenberg/Main.lean) | 75 | Formal headline theorem |
| S60 | [`lean/OAI/MathematicalPhysics/Heisenberg/Model.lean`](../../../lean/OAI/MathematicalPhysics/Heisenberg/Model.lean) | 261 | Slot model: site, level, configuration, operators |
| S61 | [`lean/OAI/MathematicalPhysics/Heisenberg/SpinAveragedKMS.lean`](../../../lean/OAI/MathematicalPhysics/Heisenberg/SpinAveragedKMS.lean) | 88 | KMS layer imported by the headline theorem |
| S62 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1,783 | Release results index: no entry naming Heisenberg |
| S63 | [`reasoning_traces/spontaneous-magnetization-quantum-heisenberg-ferromagnet.pdf`](../../../reasoning_traces/spontaneous-magnetization-quantum-heisenberg-ferromagnet.pdf) | — | Published reasoning trace for manuscript D |
