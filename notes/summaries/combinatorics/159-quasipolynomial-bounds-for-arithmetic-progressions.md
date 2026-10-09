# 159 — Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds (Combinatorics, 1 manuscript, tier T2)

## Original CONTENTS.md summary

The release's blurb [S1:3784]:

> **159. Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds.** Proves Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. Quantitatively, for each fixed *k* ≥ 3, every subset of $`\{1,\ldots,N\}`$ with no nonconstant *k*-term progression has size at most $`C_kN\exp[-c_k(\log N)^{\varepsilon_k}]`$, with positive constants depending only on *k*. ([Lean](../../../lean/docs/159.md))

The manuscript's own abstract entry in the same table [S1:3793–3797]:

> We prove Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. More quantitatively, for every fixed *k* ≥ 3, we show
> $`\displaystyle r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr)`$
> with $`C_k,c_k,\varepsilon_k\gt 0`$, where $`r_k(N)`$ is the largest size of a subset of $`\{1,\ldots,N\}`$ with no nonconstant *k*-term arithmetic progression.

The same abstract as typeset in the manuscript source [S2:9–11]:

> We prove Erd\H{o}s's conjecture that every set of positive integers
> with divergent reciprocal sum contains arithmetic progressions of every
> finite length. More quantitatively, for every fixed $k\ge3$, we show

## Undergraduate summary

A set of integers is progression-free of length *k* if it contains no *k* equally spaced distinct elements. Szemerédi's theorem says that any set with positive upper density contains progressions of every length, so a progression-free set has to be thin; the quantitative question is how thin. Write *r_k(N)* for the largest size of a progression-free subset of {1, …, *N*}. Behrend's 1938 construction already shows *r_3(N)* is at least *N* exp(−*C*√(log *N*)), so the answer is much smaller than *N* but not smaller by a power of *N*.

Erdős's conjecture is much stronger than a density statement: if *A* is any set of positive integers whose reciprocal sum Σ 1/*a* diverges, then *A* contains progressions of every finite length. Divergent reciprocal sums are a very weak largeness condition — far larger and sparser sets qualify than the positive-density ones, the primes being the standard example — so this is a genuinely harder claim. The paper proves it, and proves it quantitatively: *r_k(N)* is at most *C_k N* exp(−*c_k*(log *N*)^*ε_k*), that is *N* divided by a stretched exponential in log *N*. A set whose reciprocals diverge cannot stay under that ceiling for every length at once.

The saving is the interesting part. It beats every fixed power of log *N*, which is what the polylogarithmic line achieved, while Behrend-type constructions rule out any power saving in *N* [S4:130–132], so this is the right order of magnitude to aim at. The constants depend on the length *k*, and the paper explicitly claims no improvement of the exponent for three-term progressions [S4:155–158].

**Proof sketch.** The argument is a density-increment scheme run for a bounded number of rounds, and the bookkeeping is the whole difficulty. At each round the current set is examined through a grid of local windows arranged as triangular cells: a window's constraints are generated one coordinate block at a time, each block constrained relative to the blocks before it [S4:172]. A certificate at a given density target either produces a window where the set is denser than before — an increment — or produces a progression. The increment is engineered so that the width it costs at one layer depends on data from strictly higher layers and never on that layer's own width [S5:305–307]; the paper draws this dependency as a triangle with no arrow from a layer's width back to its own loss. That triangular dependence is what keeps the total loss from compounding. A separate absolute step supplies a fixed number of fresh controlling coordinates at every round, bounded by a quantity that does not involve the ambient dimension [S5:198–200], so the number of rounds is bounded in terms of *k* and log(1/density) alone. Summing the bounded rounds gives the stretched-exponential bound, and a short dyadic comparison converts it into the reciprocal-sum statement [S9:44–47].

## Graduate summary

The main theorem (label `ap:main`) is [S4:13–18]:

> For each fixed integer $k\ge3$ there are constants
> $C_k,c_k,\varepsilon_k>0$ such that, for every $N\ge2$,
> \begin{equation}\label{ap:density-bound}
> r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr).
> \end{equation}

The introduction states the sharp edges [S4:28–29]:

> The constants may depend on the fixed length $k$; the exponent is
> not optimized.

The scheme is a triangular density increment, and the constraint that makes it hard is the budget rule [S5:265–269]:

> At layer $j$, the \emph{warm data} consist of $p$, forecasts for all
> dimensions and structural variable counts, gap parameters depending
> only on these data, and the widths and numerical budgets already
> chosen at layers strictly above $j$. A warm logarithmic bound is
> polynomial in these data and does not use any $Q_i$ with $i\le j$.

The dependency figure says the same thing geometrically [S5:305–307]:

> The allowed dependence is triangular. There is no arrow from
> the current width or its cold outputs back to its relative width loss.
> The full dependency schedule is proved in Section~\ref{ap:iteration}.}

The setup section is explicit about why the natural constructions fail [S5:152–155]:

> It remains to construct the increment with these particular
> dependencies. A bound polynomial in all current width logs would
> not suffice: repeated substitution could raise the polynomial degree
> at every round.

What replaces them is a patch-existence statement. A patch's rank is its slot count [S5:170]:

> Its \emph{rank} is the number $d$ of integer slots.

and the absolute starting rule bounds that count by data that excludes the ambient dimension [S5:198–200]:

> unless the hypotheses are impossible, $f$ admits a degree-$s$
> polynomial patch on a slice with positive score at target $(1+\xi)a$. The number of slots is at most
> $d_0=(2+p)^C$, independent of $n$.

The absolute rule then feeds a constant old region into the lifting theorem [S4:263–270]:

> The comparison and counting arguments first give the absolute
> rule in a fixed dimension. A relative lifting theorem extends
> it with only an additive number of new determining coordinates.
> Applied with the constant old region, this yields the
> dimension-independent fresh-coordinate bound in
> Lemma~\ref{ap:absolute}. This foundational lifting argument
> supplies the absolute rule; preservation of the old width
> budgets requires the separate return argument.

The forward-mass step advances the density target [S6:169–175]:

> For any sufficiently small fixed $\eta>0$, a prepared certificate at
> threshold $a$ gives a surviving set of terminal injective paths whose
> expected terminal input mean, with stopped paths counted as zero, is
> at least $(1-\eta)a$.

and it is deliberately stated so that it cannot import a higher-layer budget downwards [S6:180–182]:

> Thus this
> proposition does not require a lower-layer width in a higher-layer
> rank budget.

The iteration closes because the targets grow geometrically and a certificate at target 1 is impossible [S8:391–397]:

> If no impossibility occurs, the targets satisfy
> $a_t\ge(\alpha/2)(1+\eta_k)^t$, and hence $a_T\ge1$.
> But a certificate at any target $a\ge1$ is impossible, since
> \[
> fB^-\le B^+
> \]
> pointwise.

The appendices carry the analytic interface with degree parameters fixed and dimensions inside the stated budgets [S12:33–37]:

> Throughout the appendices, degree parameters are fixed, while dimensions
> are included in the stated logarithmic budgets. The polynomial notation
> of Section~\ref{ap:setup} is repeated where needed. The refined
> width estimates required for the triangular increment are proved in
> the main text; they are not hypotheses of these analytic results.

What the paper does not say. Its saving is not, by itself, what the earlier five-term argument needed [S4:152–153]:

> The resulting saving in $\log\log N$ does not give the dyadic
> summability above.

and its contribution is the all-length summable bound, not a sharper exponent [S4:155–158]:

> Theorem~\ref{ap:main} gives a stretched-exponential saving in
> $\log N$ for every fixed length. Its contribution to Erd\H{o}s's
> conjecture is this all-length, summable bound; no improvement of
> the three-term exponent is claimed.

Formalization status. The scope note states what the formalization proves [S14:9]:

> The formalization proves this statement: for every requested length, such a set contains a progression with positive common difference.

and what it excludes [S14:11]:

> The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement.

That exclusion is about the selected statement, not about the tree. The challenge is 36 lines asking for one term [S15:31–32]:

> theorem manuscriptReciprocalProgressionTheorem : ReciprocalProgressionTheorem := by
>   sorry

with metadata naming the solution module [S16:3]:

> "solution_module": "OAI.Combinatorics.Progressions.Main",

and the single theorem it selects [S16:4–6]:

> "theorem_names": [
> "OAI.Erdos3.manuscriptReciprocalProgressionTheorem"
> ],

The tree is `lean/OAI/Combinatorics/Progressions/`, entered through `Main.lean`, an imports-only file whose third import is the scalar dynamics layer [S17:3]:

> import OAI.Combinatorics.Progressions.Dynamics.CanonicalScalarLogBudget

It is the largest formalization measured here: 4,774 files and 1,122,983 Lean lines, with no file containing `sorry`. `Results/Statements.lean` is an empty namespace stub [S19:7–9]:

> namespace Erdos3
> end Erdos3

The content is in `Results/Basic.lean`, whose coloring consequence is [S18:84–86]:

> theorem monochromatic_hasAP_of_extremalNumber {k N r : ℕ}
> (hbound : r * extremalNumber k N < N) (color : ℕ → Fin r) :
> ∃ c : Fin r, HasAP {n : ℕ | n ∈ Finset.Icc 1 N ∧ color n = c} k := by

The quantitative side is formalized, in a weaker form than the manuscript's. `Model.lean` defines the density bound as [S20:31–35]:

> def QuantitativeDensityBound (k : ℕ) : Prop :=
> ∃ C c η : ℝ, 0 < C ∧ 0 < c ∧ 0 < η ∧
> ∀ N : ℕ, 3 ≤ N →
> (extremalNumber k N : ℝ) ≤
> C * N * Real.exp (-c * (Real.log (Real.log N)) ^ (1 + η))

That is a saving in log log *N*; the manuscript's Theorem `ap:main` is a saving in (log *N*)^*ε_k*. The bridge from the weaker form to the reciprocal conclusion is proved in `Estimates/UniformRelativePatchSource.lean` [S23:42–43]:

> ∃ C : ℝ, 0 < C ∧ ∀ᶠ N : ℕ in atTop,
> (extremalNumber k N : ℝ) ≤ C * N / (Real.log N) ^ B := by

for every fixed *B*, which is summable on dyadic scales once *B* > 1; `Results/Reciprocal.lean` then converts dyadic summability into the progression conclusion [S22:86–88]:

> theorem hasAP_of_not_summable_reciprocal {k : ℕ}
> (hseries : Summable fun m : ℕ ↦ (extremalNumber k (2 ^ m) : ℝ) / 2 ^ m)
> {A : Set ℕ} (hA : ¬ Summable (reciprocalTerm A)) : HasAP A k := by

and `Results/Conclusions.lean` proves the pair as a conjunction [S21:26–27]:

> theorem manuscript_main_theorems :
> QuantitativeDensityTheorem ∧ ReciprocalProgressionTheorem := by

So the tree proves a quantitative density theorem and the reciprocal-sum theorem together, and the scope note's exclusion is about the statement the comparator selected. The exponent is the part that matters: the manuscript says a saving in log log *N* is not enough [S4:152–153], and the formalized bound clears the dyadic threshold only because its exponent is 1 + *η* > 1. The ledger records `paps_form 0` and `mainres 0` for this family, and `lean/formalization.yaml` carries no entry naming this manuscript, this challenge, or this solution module — the index is behind the source, not the source behind the index.

## History of the conjecture

Prior (my training data, not repo text): the reciprocal-sum formulation comes out of Erdős's collected problems on arithmetic progressions, where he attached monetary rewards to the three-term case; Szemerédi's 1975 theorem settled the positive-density case, and the reciprocal-sum strengthening stayed open. The three-term case fell to Bloom and Sisask in 2020. Before this paper, the quantitative bounds for progression-free sets were the logarithmic-saving line of Bloom–Sisask and the polylogarithmic line of Leng–Sah–Sawhney.

The manuscript's own account is the citation trail. The dyadic threshold is the pivot [S4:113–116]:

> Their later bound
> $r_3(N)\ll N/(\log N)^{1+c}$, for an absolute $c>0$,
> crossed the dyadic summability threshold and established the
> three-term reciprocal-sum conjecture~\cite{BloomSisask2020}.

Kelley and Meka obtained the stronger bound [S4:118–121]:

> Kelley and Meka obtained the stronger bound
> \[
> r_3(N)\ll N\exp\bigl(-c(\log N)^{1/12}\bigr)
> \]

Bloom and Sisask then simplified it and Raghavan extended it [S4:124–126] [S4:128]: "Bloom and Sisask simplified the argument and then improved the exponent to $1/9$." and "$r_3(N)\le N\exp\bigl(-(\log N)^{1/6-o(1)}\bigr)$". The ceiling on what any such bound can be is Behrend's construction [S4:130–132]: "Behrend's construction already gives $r_3(N)\ge N\exp(-C\sqrt{\log N})$, so a fixed power saving in $N$ is impossible even in this case".

The polylogarithmic line reached five terms and stopped [S4:141–142]:

> Leng, Sah and Sawhney first treated five terms and then proved,
> for every fixed $k\ge5$,

and its method is [S4:148–151]:

> Their general argument combines a quasipolynomial inverse theorem
> with density increments. The inverse theorem controls the structured
> correlation obtained from a large uniformity norm; the cost of
> localizing and iterating that correlation remains a separate issue.

The published trace is the release's record of the search behind this result [S25]: it is in two parts, a first part on the reciprocal-sum problem whose stated target was a power-of-log saving, and a second part that asks for quasipolynomial bounds for all *k* ≥ 3 and proposes the triangular increment that became this paper.

The manuscript's bibliography names the companion paper [S10:197]:

> OpenAI, \emph{Quantitative Superexponential Bounds for van der Waerden Numbers},

which is family 160 in the same release [S24:401]: "Superexponential van der Waerden numbers". The ledger records no companion link for either family, because the companion column is computed from the CONTENTS.md blurb and that blurb does not name the companion.

## Consequences now that the proof has been found

The headline consequence is the uniform harmonic bound [S9:44–47]:

> There is $H_k<\infty$ such that every $k$-term-progression-free
> $A\subseteq\mathbb N$ satisfies
> \[
> \sum_{a\in A}\frac1a\le H_k.

So divergence of the reciprocal sum forces progressions of every length [S9:32–33]: "Consequently, whenever $S_k(w)<\infty$, divergence of the weighted sum forces a nonconstant $k$-term progression." The bound is stable under arbitrary logarithmic losses [S9:131–135]:

> The same comparison shows that, for each fixed $B>0$, there is a
> constant $C_{k,B}$ with
> \[
> r_k(N)\le C_{k,B}N(\log N)^{-B}\qquad(N\ge3).
> \]

The paper recovers a known theorem rather than replacing it [S9:138–139]: "Theorem also recovers the established dense-primes theorem of Green and Tao" and the tail estimate that makes the weighted sums converge is [S9:163–164]: "In particular, for every $0<a<c_k$, this tail is at most $C_{k,a}e^{-a(\log x)^{\varepsilon_k}}$."

Two structural pieces are reusable beyond this theorem. The extraction step preserves the determining weights exactly [S7:64–66]:

> At passive layers the absolute weights are unchanged.
> At active layers a fixed multiplicative increase of those weights
> suffices; determining weights remain exactly their original weights.

and the route diagram records the shape of the argument [S11:31–33]:

> The main proof route.  Preparation and extraction preserve the
> triangular dependence of the width losses; the absolute increment
> controls the number of fresh determining coordinates.

The same iteration yields the van der Waerden lower bound [S4:308–310]:

> gives the complementary lower bound
> $W_r(k)>\exp((\log r)^2/(64\log2))$ for all integers $r\ge256$
> and $k\ge3$.

The manuscript ships as a 37-line `main.tex` with ten sections and a seven-file foundations appendix — 15,569 lines of source across 29 files — plus a compiled [S13] `paper.pdf`.

Its README gives the release date [S3:5]: "Date: September 23, 2026".

## Sources

Manuscript root: `preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026`.

| ID | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release blurb and manuscript sub-entry |
| S2 | [`build/main.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/main.tex) | 37 | Manuscript source: title, abstract, section order |
| S3 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md) | 18 | Manuscript build notes and release date |
| S4 | [`build/sections/00-introduction.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/00-introduction.tex) | 343 | Theorem statement, prior work, proof outline |
| S5 | [`build/sections/01-setup.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/01-setup.tex) | 377 | Triangular cells, budget rule, patch rank |
| S6 | [`build/sections/04-scalar.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/04-scalar.tex) | 299 | Forward mass and rank-stop budget |
| S7 | [`build/sections/07-extraction.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/07-extraction.tex) | 535 | Extraction: weights preserved at passive layers |
| S8 | [`build/sections/08-iteration.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/08-iteration.tex) | 440 | Iteration closure and proof of the main theorem |
| S9 | [`build/sections/09-consequences.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/09-consequences.tex) | 192 | Weighted sums, polylog bound, Green–Tao recovery |
| S10 | [`build/references.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/references.tex) | 257 | Bibliography, including the companion paper |
| S11 | [`build/figures/proof-route.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/figures/proof-route.tex) | 35 | Proof-route diagram |
| S12 | [`build/foundations/00-preface.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/foundations/00-preface.tex) | 80 | Appendix preface and interface table |
| S13 | [`paper.pdf`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) | — | Compiled manuscript |
| S14 | [`lean/docs/159.md`](../../../lean/docs/159.md) | 17 | Scope note: comparator target and exclusion |
| S15 | [`lean/ComparatorChallenges/ErdosReciprocal.lean`](../../../lean/ComparatorChallenges/ErdosReciprocal.lean) | 36 | Challenge statement |
| S16 | [`lean/ComparatorChallenges/ErdosReciprocal.json`](../../../lean/ComparatorChallenges/ErdosReciprocal.json) | 14 | Challenge metadata: module, theorem names |
| S17 | [`lean/OAI/Combinatorics/Progressions/Main.lean`](../../../lean/OAI/Combinatorics/Progressions/Main.lean) | 98 | Tree entry point (imports only) |
| S18 | [`lean/OAI/Combinatorics/Progressions/Results/Basic.lean`](../../../lean/OAI/Combinatorics/Progressions/Results/Basic.lean) | 128 | Coloring consequence of the density bound |
| S19 | [`lean/OAI/Combinatorics/Progressions/Results/Statements.lean`](../../../lean/OAI/Combinatorics/Progressions/Results/Statements.lean) | 13 | Empty namespace stub |
| S20 | [`lean/OAI/Combinatorics/Progressions/Model.lean`](../../../lean/OAI/Combinatorics/Progressions/Model.lean) | 45 | Formalized density bound (log log form) |
| S21 | [`lean/OAI/Combinatorics/Progressions/Results/Conclusions.lean`](../../../lean/OAI/Combinatorics/Progressions/Results/Conclusions.lean) | 45 | Conjunction of both theorems |
| S22 | [`lean/OAI/Combinatorics/Progressions/Results/Reciprocal.lean`](../../../lean/OAI/Combinatorics/Progressions/Results/Reciprocal.lean) | 96 | Reciprocal-sum conclusion |
| S23 | [`lean/OAI/Combinatorics/Progressions/Estimates/UniformRelativePatchSource.lean`](../../../lean/OAI/Combinatorics/Progressions/Estimates/UniformRelativePatchSource.lean) | 561 | Log log → polylog → dyadic bridge |
| S24 | [`overview.tex`](../../../overview.tex) | 859 | Release entry list (family 159 at line 399) |
| S25 | [`reasoning_traces/quasipolynomial-arithmetic-progressions.pdf`](../../../reasoning_traces/quasipolynomial-arithmetic-progressions.pdf) | — | Published reasoning trace |
