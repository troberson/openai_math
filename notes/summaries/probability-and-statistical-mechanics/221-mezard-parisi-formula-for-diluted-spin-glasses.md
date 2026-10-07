# 221 — The Mézard–Parisi formula for diluted spin glasses (Probability and statistical mechanics, 1 manuscript, tier T2)

## Original CONTENTS.md summary

**221. The Mézard–Parisi formula for diluted spin glasses.** Proves the Mézard–Parisi hierarchical cavity formula for Poisson-diluted even-arity Ising models satisfying the Panchenko–Talagrand factorization and positivity assumptions, with only first-moment integrability. The limiting free energy equals the infimum over finite-depth hierarchical trial laws. This includes the Viana–Bray model, symmetric diluted even-spin models, and weighted soft even-*K* satisfiability. ([Lean](../../../lean/docs/221.md))

The blurb above is reproduced from [S1:5247]; the release sets the clause size in italic markup and this page writes it as *K*.

## Undergraduate summary

The release abstract states the result in one paragraph [S1:5256]:

> We prove the Mézard–Parisi hierarchical cavity formula for diluted even-arity Ising models in the Panchenko–Talagrand class. This resolves the variational equality conjecture for that class: the limiting pressure equals the infimum of the trial functional over all finite hierarchy depths and trial laws. Only first moments of the interaction and external field are required.

A spin glass is a magnet whose couplings are frozen randomness. Take N spins, each equal to +1 or −1. Instead of connecting every pair of spins, constraints arrive at random: their number is Poisson with mean αN, and each constraint draws p spins uniformly at random, with replacement, and attaches a random coupling law to them [S8:12–20]. What the paper computes is the pressure F_N = (1/N) E log Z_N, the averaged logarithm of the partition function per spin; the physical free energy per spin is its negative divided by the inverse temperature β [S7:9–11]. Because the number of constraints is itself random, the interaction graph is sparse and looks locally like a tree with a random number of branches — the geometry the cavity method was built for.

Mézard and Parisi wrote down a recipe for the limit of F_N in 2001: choose a finite number r of hierarchy levels, choose a probability law for the messages that travel along the tree at each level, choose the breakpoints between them, evaluate a formula Φ_r, and take the smallest value the recipe can produce [S7:14–17]. For two decades the recipe was known to be an upper bound and known to be exact only in restricted cases [S7:17–19]. This manuscript proves the equality for every even arity and every positive density, under the assumptions Panchenko and Talagrand imposed when they posed the problem [S7:24–29]. The manuscript is dated 23 September 2026 [S2:5], and the release ships a reasoning trace for it [S29].

**Proof sketch.** The upper bound is classical: a Guerra–Toninelli interpolation shows F_N ≤ Φ_r for every admissible trial law, so the pressure is at most the infimum [S11:12–14]. The lower bound is the new part, and the paper splits it into four steps [S9:4–6]. First, compare the systems of size N and N+1 inside one common N-spin system, the reservoir, which turns the increment of the pressure into an average over the few constraints that were added [S12:3–4]. Second, prescribe the branching pattern of the tree those constraints form, so the identity to be proved is stated on a fixed finite tree [S13:451–470]. Third, prove that every multioverlap — the joint frequency with which a pattern of replica spins occurs — concentrates on average over branching depths, not at any single depth [S14:82–83]. Fourth, use that concentration to replace the replica system by independent cavity messages, which turns Φ_r into a lower bound for liminf F_N [S15:226–230]. The device that makes the third step close is a shift: every internal branching depth of the target tree is moved up one level [S7:79–81].

## Graduate summary

The model is fixed by an even arity p\ge2, a density α>0, i.i.d. interaction laws θ on {-1,1}^p, and an i.i.d. field law h, under \E B(θ)+\E\abs{h}<\infty where B(θ)=\max_s\abs{\theta(s)} [S8:3–8]. Constraints are sampled with replacement, and "All families in this definition are mutually independent." [S8:21–23] The interaction factorizes, the positivity condition is \E[(-b)^n]\ge0 for every n\ge1, and "no separate integrability of $\log a$ is assumed." [S8:35–44] A trial law is a finite tower of message spaces with a root law ζ and breakpoints 0<m_1<\cdots<m_r<1 [S8:68–71].

The trial functional is defined at [S8:112–117]

> \begin{equation}\label{model:functional}
>  \cB_r(\zeta,\mathbf m)
>  =\log2+\E\log T_0V_{\rm s}
>  -\alpha(p-1)\E\log T_0V_{\rm e},
>  \qquad \Phi_r=\inf_{\zeta,\,\mathbf m}\cB_r(\zeta,\mathbf m).
> \end{equation}

Here V_{\rm s} and V_{\rm e} are the site and edge messages built from one cavity insertion [S8:84–89], T_0 is the last of the power-mean operators T_dV=\left(\E[(T_{d+1}V)^{m_{d+1}}\mid\mathscr F_d]\right)^{1/m_{d+1}} running down the hierarchy from T_rV=V [S8:92–96], and at r=0 the operators are omitted so that the messages are independent [S8:118–120]. The main theorem is [S8:131–135]

> Under \eqref{model:integrability}--\eqref{model:positivity}, the thermodynamic limit exists and
> \begin{equation}\label{main:formula}
>  \lim_{N\to\infty}F_N=\inf_{r\ge0}\Phi_r.
> \end{equation}

"The right side is an infimum over finite hierarchies. The theorem does not assume that a trial law attains it or that a limiting infinite-depth Gibbs state has been constructed." [S8:138–140] The hierarchy is an artifact of the proof, not a claim about the physical Gibbs states: "Their branching is part of the construction; no ultrametric organization of the physical Gibbs states is assumed." [S7:75–77]

The obstruction is that replica computations on a diluted model are not controlled by pair overlaps. "The probability of each replica-spin pattern depends on products of every subset of those spins. The spatial average of such a product is a \emph{multioverlap}; pair overlaps alone do not determine all these patterns." [S7:66–70] Hence "we must control all finite multioverlaps before redrawing the message roots independently." [S7:71–73] The concentration theorem is stated with the averaging built in — "where only the $b(S)$ branching depths are averaged" [S14:63–75] — and the paper is explicit that "Averaging over depths is essential when combining the two estimates." [S14:82–83]

The lower bound is proved first for bounded laws, where "The error is taken to zero at fixed $L$, fixed tree, and fixed constraint, before any limit in $L$." [S13:468–469] and takes the form [S15:226–230]

> For every bounded permutation-invariant interaction law and bounded field law, with the functionals defined in \cref{model:section},
> \[
>  \liminf_{N\to\infty}F_N\ge\inf_{r\ge0}\Phi_r.
> \]

Boundedness is removed last: "The multiplier $a$ may depend asymmetrically on the labeled input functions, so the original interaction law need not be permutation invariant. We first remove this multiplier by an integrable scalar shift." [S16:46–48] The overview states the shape of that argument — "including a normalization that avoids assuming integrability of the multiplier $\log a$" [S9:3–6], "No uniform concentration in the depth is needed." [S9:45–46], and "Finally, normalization and estimates uniform over all trial laws remove boundedness and give \cref{main:theorem} under the stated first moment assumption" [S9:48–50]. The tree calculus underneath is derived from scratch rather than inherited: "Here we derive the needed identities directly for finite sequences of arbitrary probability kernels, without assuming an infinite hierarchy." [S10:10–12] The manuscript is one paper of sixteen LaTeX files built from `build/main.tex`, which inputs the eleven sections in proof order [S3:62–72], with a glyph-mapping file loaded so the PDF text stays extractable [S4:1–2].

## History of the conjecture

The model class predates the formula. Viana and Bray's diluted two-spin model is from 1985 [S7:13–14]; Mézard and Parisi derived the explicit one-step replica-symmetry-breaking functional for the diluted Bethe lattice in 2001 [S7:14–17]; Franz and Leone and, independently, Guerra obtained replica-symmetric and one-step bounds for even-arity models in 2003 [S7:17–19]. Panchenko and Talagrand then "proved the arbitrary finite-level hierarchical upper bounds considered here" [S7:20–22] and posed the matching equality as a conjecture. The manuscript states what it resolves: "This resolves the equality conjecture stated immediately after Theorem~4 of Panchenko--Talagrand~\cite{PT04}, for their Poisson, even-arity Ising model class with factorized interactions and the specified positivity condition. Only first moments of the interaction and external field are required." [S7:25–29] The reasoning trace records the conjecture in the form it was given: "This is the sharpness conjecture immediately following Theorem 4: the infimum runs over all finite replica-symmetry-breaking levels, all their hierarchical message laws, and all admissible breakpoints. No attainment at a fixed level or by a particular trial law is asserted." [S30:152]

Exact variational description and reduction to a prescribed trial class are separate problems, and the manuscript is explicit about its neighbours: the Aizenman–Sims–Starr cavity principle, De Sanctis's formulation over random multioverlap structures, Panchenko's spin-distribution formula, and the Coja-Oghlan–Perkins invariant-kernel formula for random regular factor graphs [S7:36–45]. "These results use different descriptions of the state from the finite hierarchy of message laws optimized here. The additional task is to recover the specific hierarchical cavity functional without losing the pressure." [S7:45–48] The closest recent results stop short of the equality: for the zero-field Ising spin glass with Rademacher couplings on random regular graphs, Concetti's full-replica-symmetry-breaking bound is only a bound, and "equality with that functional is conjectural in that work" [S7:58–61]; "The result here identifies the finite-depth Panchenko--Talagrand infimum at arbitrary density in its stated interaction class." [S7:61–63]

The trace shows the order in which the proof was found. The first move is a counterexample hunt: "Initial checks look for a counterexample in the assumptions: a nonintegrable factorization constant, asymmetric fields, interactions close to the positivity boundary, or messages tending to infinity. None yields one." [S30:157] Then the recursive cavity observation, "Aha recursive structure: overfitting shared variable can simulate original model at smaller scale." [S30:162]; then the shift that makes the induction close, "The change is to shift every internal branching depth of the target tree by one level." [S30:173] and "Great! Need carefully prove average error little with shifted depths not rare" [S30:176]; then the order of limits, "The order of limits matters: errors in fixed-depth identities disappear before the hierarchy is refined." [S30:178]. Its working bibliography is Barbier–Panchenko, Mourrat, Mourrat–Panchenko, Panchenko 2016, and Panchenko–Talagrand 2004 [S30:199–210]; the first three appear nowhere in the manuscript's reference list [S5]. This is the release's only reasoning trace shipped as LaTeX source, so its reasoning is quotable text rather than a PDF scan [S29].

## Consequences now that the proof has been found

Inside the manuscript the formula is evaluated on the named models immediately. The diluted even-spin corollary covers "this holds for the Viana--Bray model~\cite{VB85}, which is the case $p=2$" [S17:19–21], and the satisfiability corollary covers weighted soft clauses: "The choice $W=1$ is the soft random even-$K$ SAT model; $W$ gives an independent nonnegative clause weight." [S17:47–48] A zero-temperature limit follows: the ground-state energy per spin is the temperature limit of the same infimum, the approximation is bracketed in $[g,g+\log(2)/\beta]$, and "For unit-weight SAT, the limiting expected minimum number of violated clauses per variable is $-g$." [S17:93–100] The infimum there is taken "over all finite hierarchies separately at each positive temperature" and "does not require attainment or a limiting hierarchy" [S17:127–129].

Random 3-SAT is explicitly out of reach: "The even-arity hypothesis in \cref{models:sat} excludes random 3-SAT." [S17:131–138] The manuscript points to its companion for that model, whose Theorem 8.4 gives an exact soft-pressure formula over finite rational trials, noting that the companion's "trial functional differs from \eqref{model:functional}" [S17:131–138]. That companion is family 235, Random-SAT thresholds, sharp variance and computability [S28:23–26], and in the formalization the dependency runs the same way: 23 files in family 235's `SATComputability` tree import 17 distinct modules of the DilutedSpin tree, `InterpolationUpper.lean` among them [S27:1].

The formalization is large relative to the index that records it. The tree `lean/OAI/Probability/DilutedSpin/` holds 405 files and 56,285 lines with zero `sorry` and 824 `theorem` lines; the formal main statement is `Tendsto (pressure M) atTop (𝓝 (variationalValue M))` [S21:12–13], assembled from a boundedness lemma, an upper bound, and a lower bound [S23:23] [S24:54]. The comparator statement `OAI.DilutedSpinGlass.mezard_parisi` is the family's single challenge [S19:148–150], with admissibility spelled out as arity, parity, density, integrability, factorization, independence, and positivity [S19:29–51], and its config permits only `propext`, `Quot.sound`, and `Classical.choice` [S20]. The scope note states the result and its assumptions and lists no exclusions [S18:9]. The formal model file mirrors the manuscript's definitions [S22:27], and the largest module in the tree is `HistoryGeometry.lean` [S25:1].

Two gaps are worth recording. The ledger reports `paps_form 0` and `mainres 0` for 221 while reporting one challenge, and the mechanical cause is visible in the release index: `lean/formalization.yaml` carries no entry for this manuscript and no `comparator_config` for `DilutedSpin.json` [S26], so the index is behind the tree rather than the tree being absent. The second gap is coverage: the manuscript's three named corollaries — Viana–Bray, soft even-*K* SAT, and the zero-temperature limit — are not formalized in the DilutedSpin tree, where the words Viana, Bray, SAT, soft, temperature, and ground do not occur in any file. The published PDF remains the authoritative statement of those corollaries [S6].

## Sources

Manuscript root: `preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/`.

| ID | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9169 | Release contents listing: blurb and abstract |
| S2 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/README.md`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/README.md) | 18 | Manuscript README: date and citation key |
| S3 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/main.tex) | 75 | Manuscript main file: abstract and section order |
| S4 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/glyph-mappings.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/glyph-mappings.tex) | 40 | Build support: PDF glyph mappings |
| S5 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/references.bib`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/references.bib) | 233 | Manuscript bibliography |
| S6 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf) | — | Published manuscript PDF |
| S7 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/introduction.tex) | 86 | Model history, prior results, stated contribution |
| S8 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/model.tex) | 140 | Model, trial functional, main theorem |
| S9 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/overview.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/overview.tex) | 51 | Proof strategy overview |
| S10 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/trees.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/trees.tex) | 525 | Calculus on finite trees |
| S11 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/upper.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/upper.tex) | 128 | Interpolation upper bound |
| S12 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/cavity.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/cavity.tex) | 121 | Perturbed cavity reservoir |
| S13 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/perturbations.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/perturbations.tex) | 547 | Perturbation family and prescribed-tree identity |
| S14 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/decorrelation.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/decorrelation.tex) | 623 | Multioverlap concentration |
| S15 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/comparison.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/comparison.tex) | 246 | Cavity comparison and lower bound |
| S16 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/reduction.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/reduction.tex) | 87 | Normalization and completion of the proof |
| S17 | [`preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/consequences.tex`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/build/sections/consequences.tex) | 138 | Named models, zero-temperature limit, 3-SAT remark |
| S18 | [`lean/docs/221.md`](../../../lean/docs/221.md) | 15 | Scope note |
| S19 | [`lean/ComparatorChallenges/DilutedSpin.lean`](../../../lean/ComparatorChallenges/DilutedSpin.lean) | 154 | Comparator statement |
| S20 | [`lean/ComparatorChallenges/DilutedSpin.json`](../../../lean/ComparatorChallenges/DilutedSpin.json) | 14 | Comparator config |
| S21 | [`lean/OAI/Probability/DilutedSpin/Main.lean`](../../../lean/OAI/Probability/DilutedSpin/Main.lean) | 24 | Formal main theorem |
| S22 | [`lean/OAI/Probability/DilutedSpin/Model.lean`](../../../lean/OAI/Probability/DilutedSpin/Model.lean) | 148 | Formal model and admissibility |
| S23 | [`lean/OAI/Probability/DilutedSpin/ExactVariationalLower.lean`](../../../lean/OAI/Probability/DilutedSpin/ExactVariationalLower.lean) | 37 | Lower-bound interface |
| S24 | [`lean/OAI/Probability/DilutedSpin/ProxyRateIncrement.lean`](../../../lean/OAI/Probability/DilutedSpin/ProxyRateIncrement.lean) | 76 | Upper-bound interface |
| S25 | [`lean/OAI/Probability/DilutedSpin/HistoryGeometry.lean`](../../../lean/OAI/Probability/DilutedSpin/HistoryGeometry.lean) | 1125 | Largest module in the formalized tree |
| S26 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1668 | Release formalization index |
| S27 | [`lean/OAI/Probability/SATComputability/InterpolationUpper.lean`](../../../lean/OAI/Probability/SATComputability/InterpolationUpper.lean) | 1211 | Family 235 module importing DilutedSpin |
| S28 | [`lean/docs/235.md`](../../../lean/docs/235.md) | 26 | Companion scope note |
| S29 | [`reasoning_traces/mezard-parisi-formula.pdf`](../../../reasoning_traces/mezard-parisi-formula.pdf) | — | Published reasoning trace |
| S30 | [`reasoning_traces/mezard-parisi-formula.tex`](../../../reasoning_traces/mezard-parisi-formula.tex) | 211 | Reasoning trace source |
