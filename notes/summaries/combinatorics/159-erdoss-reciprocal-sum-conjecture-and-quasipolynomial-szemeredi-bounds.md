[Notes](../../README.md) / [Summaries](../README.md) / [Combinatorics](../../index/disciplines/combinatorics.md) / [Family 159](../../index/combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemeredi-bounds.md)

# 159 — Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds

[Index page](../../index/combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemeredi-bounds.md)

## Original CONTENTS.md summary

The release's blurb [S1:3784]:

> **159. Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds.** Proves Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. Quantitatively, for each fixed *k* ≥ 3, every subset of $`\{1,\ldots,N\}`$ with no nonconstant *k*-term progression has size at most $`C_kN\exp[-c_k(\log N)^{\varepsilon_k}]`$, with positive constants depending only on *k*. ([Lean](../../../lean/docs/159.md))

The manuscript's own abstract entry in the same table 

> We prove Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. More quantitatively, for every fixed *k* ≥ 3, we show $`\displaystyle r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr)`$ with $`C_k,c_k,\varepsilon_k\gt 0`$, where $`r_k(N)`$ is the largest size of a subset of $`\{1,\ldots,N\}`$ with no nonconstant *k*-term arithmetic progression. [S1:3793–3797]

The same abstract as typeset in the manuscript source 

> We prove Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. More quantitatively, for every fixed $k\ge3$, we show [S2:9–11]

## Undergraduate summary

A set of integers is progression-free of length *k* if it contains no *k* equally spaced distinct elements. Szemerédi's theorem says that any set with positive upper density contains progressions of every length, so a progression-free set has to be thin; the quantitative question is how thin. Write *r_k(N)* for the largest size of a progression-free subset of {1, …, *N*}. Behrend's 1938 construction already shows *r_3(N)* is at least *N* exp(−*C*√(log *N*)), so the answer is much smaller than *N* but not smaller by a power of *N*.

Erdős's conjecture is much stronger than a density statement: if *A* is any set of positive integers whose reciprocal sum Σ 1/*a* diverges, then *A* contains progressions of every finite length. Divergent reciprocal sums are a very weak largeness condition — far larger and sparser sets qualify than the positive-density ones, the primes being the standard example — so this is a genuinely harder claim. The paper proves it, and proves it quantitatively: *r_k(N)* is at most *C_k N* exp(−*c_k*(log *N*)^*ε_k*), that is *N* divided by a stretched exponential in log *N*. A set whose reciprocals diverge cannot stay under that ceiling for every length at once.

The saving is the interesting part. It beats every fixed power of log *N*, which is what the polylogarithmic line achieved, while Behrend-type constructions rule out any power saving in *N* [S4:130–132], so this is the right order of magnitude to aim at. The constants depend on the length *k*, and the paper explicitly claims no improvement of the exponent for three-term progressions [S4:155–158].

**Proof sketch.** The argument is a density-increment scheme run for a bounded number of rounds, and the bookkeeping is the whole difficulty. At each round the current set is examined through a grid of local windows arranged as triangular cells: a window's constraints are generated one coordinate block at a time, each block constrained relative to the blocks before it [S4:172]. A certificate at a given density target either produces a window where the set is denser than before — an increment — or produces a progression. The increment is engineered so that the width it costs at one layer depends on data from strictly higher layers and never on that layer's own width [S5:305–307]; the paper draws this dependency as a triangle with no arrow from a layer's width back to its own loss. That triangular dependence is what keeps the total loss from compounding. A separate absolute step supplies a fixed number of fresh controlling coordinates at every round, bounded by a quantity that does not involve the ambient dimension [S5:198–200], so the number of rounds is bounded in terms of *k* and log(1/density) alone. Summing the bounded rounds gives the stretched-exponential bound, and a short dyadic comparison converts it into the reciprocal-sum statement [S9:44–47].

## Graduate summary

The main theorem (label `ap:main`) is [S4:13–18]:

> For each fixed integer $k\ge3$ there are constants $C_k,c_k,\varepsilon_k>0$ such that, for every $N\ge2$, $$\label{ap:density-bound} r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr).$$ [S4:14–18]

The introduction states the sharp edges 

> The constants may depend on the fixed length $k$; the exponent is not optimized. [S4:28–29]

The scheme is a triangular density increment, and the constraint that makes it hard is the budget rule 

> At layer $j$, the _warm data_ consist of $p$, forecasts for all dimensions and structural variable counts, gap parameters depending only on these data, and the widths and numerical budgets already chosen at layers strictly above $j$. A warm logarithmic bound is polynomial in these data and does not use any $Q_i$ with $i\le j$. [S5:265–269]

The dependency figure says the same thing geometrically 

> The allowed dependence is triangular. There is no arrow from the current width or its cold outputs back to its relative width loss. The full dependency schedule is proved in Section  .} [S5:305–307]

The setup section is explicit about why the natural constructions fail 

> It remains to construct the increment with these particular dependencies. A bound polynomial in all current width logs would not suffice: repeated substitution could raise the polynomial degree at every round. [S5:152–155]

What replaces them is a patch-existence statement. A patch's rank is its slot count 

> Its _rank_ is the number $d$ of integer slots. [S5:170]

and the absolute starting rule bounds that count by data that excludes the ambient dimension 

> unless the hypotheses are impossible, $f$ admits a degree-$s$ polynomial patch on a slice with positive score at target $(1+\xi)a$. The number of slots is at most $d_0=(2+p)^C$, independent of $n$. [S5:198–200]

The absolute rule then feeds a constant old region into the lifting theorem 

> The comparison and counting arguments first give the absolute rule in a fixed dimension. A relative lifting theorem extends it with only an additive number of new determining coordinates. Applied with the constant old region, this yields the dimension-independent fresh-coordinate bound in Lemma  . This foundational lifting argument supplies the absolute rule; preservation of the old width budgets requires the separate return argument. [S4:263–270]

The forward-mass step advances the density target [S6:169–175]:

> For any sufficiently small fixed $\eta>0$, a prepared certificate at threshold $a$ gives a surviving set of terminal injective paths whose expected terminal input mean, with stopped paths counted as zero, is at least $(1-\eta)a$. [S6:169–172]

and it is deliberately stated so that it cannot import a higher-layer budget downwards [S6:180–182]:

> Thus this
> proposition does not require a lower-layer width in a higher-layer
> rank budget.

The iteration closes because the targets grow geometrically and a certificate at target 1 is impossible 

> If no impossibility occurs, the targets satisfy $a_t\ge(\alpha/2)(1+\eta_k)^t$, and hence $a_T\ge1$. But a certificate at any target $a\ge1$ is impossible, since \[ fB^-\le B^+ \] pointwise. [S8:391–397]

The appendices carry the analytic interface with degree parameters fixed and dimensions inside the stated budgets 

> Throughout the appendices, degree parameters are fixed, while dimensions are included in the stated logarithmic budgets. The polynomial notation of Section   is repeated where needed. The refined width estimates required for the triangular increment are proved in the main text; they are not hypotheses of these analytic results. [S12:33–37]

What the paper does not say. Its saving is not, by itself, what the earlier five-term argument needed 

> The resulting saving in $\log\log N$ does not give the dyadic summability above. [S4:152–153]

and its contribution is the all-length summable bound, not a sharper exponent 

> Theorem   gives a stretched-exponential saving in $\log N$ for every fixed length. Its contribution to Erdős's conjecture is this all-length, summable bound; no improvement of the three-term exponent is claimed. [S4:155–158]

Formalization status. The scope note states what the formalization proves 

> The formalization proves this statement: for every requested length, such a set contains a progression with positive common difference. [S14:9]

and what it excludes 

> The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement. [S14:11]

That exclusion is about the selected statement, not about the tree. The challenge is 36 lines asking for one term 

> theorem manuscriptReciprocalProgressionTheorem : ReciprocalProgressionTheorem := by sorry [S15:31–32]

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

The content is in `Results/Basic.lean`, whose coloring consequence is 

> theorem monochromatic_hasAP_of_extremalNumber {k N r : ℕ} (hbound : r * extremalNumber k N < N) (color : ℕ → Fin r) : ∃ c : Fin r, HasAP {n : ℕ | n ∈ Finset.Icc 1 N ∧ color n = c} k := by [S18:84–86]

The quantitative side is formalized, in a weaker form than the manuscript's. `Model.lean` defines the density bound as 

> def QuantitativeDensityBound (k : ℕ) : Prop := ∃ C c η : ℝ, 0 < C ∧ 0 < c ∧ 0 < η ∧ ∀ N : ℕ, 3 ≤ N → (extremalNumber k N : ℝ) ≤ C * N * Real.exp (-c * (Real.log (Real.log N)) ^ (1 + η)) [S20:31–35]

That is a saving in log log *N*; the manuscript's Theorem `ap:main` is a saving in (log *N*)^*ε_k*. The bridge from the weaker form to the reciprocal conclusion is proved in `Estimates/UniformRelativePatchSource.lean` 

> ∃ C : ℝ, 0 < C ∧ ∀ᶠ N : ℕ in atTop, (extremalNumber k N : ℝ) ≤ C * N / (Real.log N) ^ B := by [S23:42–43]

for every fixed *B*, which is summable on dyadic scales once *B* > 1; `Results/Reciprocal.lean` then converts dyadic summability into the progression conclusion 

> theorem hasAP_of_not_summable_reciprocal {k : ℕ} (hseries : Summable fun m : ℕ ↦ (extremalNumber k (2 ^ m) : ℝ) / 2 ^ m) {A : Set ℕ} (hA : ¬ Summable (reciprocalTerm A)) : HasAP A k := by [S22:86–88]

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

Kelley and Meka obtained the stronger bound 

> Kelley and Meka obtained the stronger bound \[ r_3(N)\ll N\exp\bigl(-c(\log N)^{1/12}\bigr) \] [S4:118–121]

Bloom and Sisask then simplified it and Raghavan extended it "Bloom and Sisask simplified the argument and then improved the exponent to $1/9$. [S4:124–126]" and "$r_3(N)\le N\exp\bigl(-(\log N)^{1/6-o(1)}\bigr)$ [S4:128]". The ceiling on what any such bound can be is Behrend's construction "Behrend's construction already gives $r_3(N)\ge N\exp(-C\sqrt{\log N})$, so a fixed power saving in $N$ is impossible even in this case [S4:130–132]".

The polylogarithmic line reached five terms and stopped 

> Leng, Sah and Sawhney first treated five terms and then proved, for every fixed $k\ge5$, [S4:141–142]

and its method is 

> Their general argument combines a quasipolynomial inverse theorem with density increments. The inverse theorem controls the structured correlation obtained from a large uniformity norm; the cost of localizing and iterating that correlation remains a separate issue. [S4:148–151]

The published trace is the release's record of the search behind this result [S25]: it is in two parts, a first part on the reciprocal-sum problem whose stated target was a power-of-log saving, and a second part that asks for quasipolynomial bounds for all *k* ≥ 3 and proposes the triangular increment that became this paper.

The manuscript's bibliography names the companion paper 

> OpenAI, _Quantitative Superexponential Bounds for van der Waerden Numbers_, [S10:197]

which is family 160 in the same release "Superexponential van der Waerden numbers [S24:401]". The ledger records no companion link for either family, because the companion column is computed from the CONTENTS.md blurb and that blurb does not name the companion.

## Consequences

The headline consequence is the uniform harmonic bound 

> There is $H_k<\infty$ such that every $k$-term-progression-free $A\subseteq\mathbb N$ satisfies \[ \sum_{a\in A}\frac1a\le H_k. [S9:44–47]

So divergence of the reciprocal sum forces progressions of every length "Consequently, whenever $S_k(w)<\infty$, divergence of the weighted sum forces a nonconstant $k$-term progression. [S9:32–33]" The bound is stable under arbitrary logarithmic losses 

> The same comparison shows that, for each fixed $B>0$, there is a constant $C_{k,B}$ with \[ r_k(N)\le C_{k,B}N(\log N)^{-B}\qquad(N\ge3). \] [S9:131–135]

The paper recovers a known theorem rather than replacing it "Theorem also recovers the established dense-primes theorem of Green and Tao [S9:138–139]" and the tail estimate that makes the weighted sums converge is "In particular, for every $0<a<c_k$, this tail is at most $C_{k,a}e^{-a(\log x)^{\varepsilon_k}}$. [S9:163–164]"

Two structural pieces are reusable beyond this theorem. The extraction step preserves the determining weights exactly 

> At passive layers the absolute weights are unchanged. At active layers a fixed multiplicative increase of those weights suffices; determining weights remain exactly their original weights. [S7:64–66]

and the route diagram records the shape of the argument 

> The main proof route.  Preparation and extraction preserve the triangular dependence of the width losses; the absolute increment controls the number of fresh determining coordinates. [S11:31–33]

The same iteration yields the van der Waerden lower bound 

> gives the complementary lower bound $W_r(k)>\exp((\log r)^2/(64\log2))$ for all integers $r\ge256$ and $k\ge3$. [S4:308–310]

The manuscript ships as a 37-line `main.tex` with ten sections and a seven-file foundations appendix — 15,569 lines of source across 29 files — plus a compiled [S13] `paper.pdf`.

Its README gives the release date "Date: September 23, 2026 [S3:5]".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Release blurb and manuscript sub-entry |
| S2 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/main.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/main.tex) | 37 | Manuscript source: title, abstract, section order |
| S3 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md) | 18 | Manuscript build notes and release date |
| S4 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/00-introduction.tex) | 343 | Theorem statement, prior work, proof outline |
| S5 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/01-setup.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/01-setup.tex) | 377 | Triangular cells, budget rule, patch rank |
| S6 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/04-scalar.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/04-scalar.tex) | 299 | Forward mass and rank-stop budget |
| S7 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/07-extraction.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/07-extraction.tex) | 535 | Extraction: weights preserved at passive layers |
| S8 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/08-iteration.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/08-iteration.tex) | 440 | Iteration closure and proof of the main theorem |
| S9 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/09-consequences.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/09-consequences.tex) | 192 | Weighted sums, polylog bound, Green–Tao recovery |
| S10 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/references.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/references.tex) | 257 | Bibliography, including the companion paper |
| S11 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/figures/proof-route.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/figures/proof-route.tex) | 35 | Proof-route diagram |
| S12 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/foundations/00-preface.tex`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/foundations/00-preface.tex) | 80 | Appendix preface and interface table |
| S13 | [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) | 43640 | Compiled manuscript |
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
| S25 | [`reasoning_traces/quasipolynomial-arithmetic-progressions.pdf`](../../../reasoning_traces/quasipolynomial-arithmetic-progressions.pdf) | 7552 | Published reasoning trace |

## Bibliography

- F. A. Behrend, _On sets of integers which contain no three terms in arithmetical progression_, Proc. Nat. Acad. Sci. U.S.A. **32** (1946), 331–332.  .
- V. Bergelson, B. Host and B. Kra, _Multiple recurrence and nilsequences_, with an appendix by I. Z. Ruzsa, Invent. Math. **160** (2005), no. 2, 261–303. doi:10.1007/s00222-004-0428-6.
- T. F. Bloom, _A quantitative improvement for Roth's theorem on arithmetic progressions_, J. London Math. Soc. (2) **93** (2016), no. 3, 643–663.  .
- J. Bourgain, _On triples in arithmetic progression_, Geom. Funct. Anal. **9** (1999), no. 5, 968–984.  .
- J. Bourgain, _Roth's theorem on progressions revisited_, J. Anal. Math. **104** (2008), 155–192.  .
- D. Conlon, J. Fox and Y. Zhao, _A relative Szemerédi theorem_, Geom. Funct. Anal. **25** (2015), no. 3, 733–762.  .
- P. Erdős, _Some unsolved problems_, Magyar Tud. Akad. Mat. Kutató Int. Közl. **6** (1961), 221–254.
- P. Erdős, _Problems_, Math. Balkanica **4** (1974), 203–204, Problem 4.33.6.  .
- H. Furstenberg, _Ergodic behavior of diagonal measures and a theorem of Szemerédi on arithmetic progressions_, J. Analyse Math. **31** (1977), 204–256.  .
- W. T. Gowers, _A new proof of Szemerédi's theorem for arithmetic progressions of length four_, Geom. Funct. Anal. **8** (1998), 529–551.  .
- W. T. Gowers, _A new proof of Szemerédi's theorem_, Geom. Funct. Anal. **11** (2001), 465–588.  .
- W. T. Gowers, _Decompositions, approximate structure, transference, and the Hahn–Banach theorem_, Bull. London Math. Soc. **42** (2010), no. 4, 573–606.  .
- B. Green, T. Tao and T. Ziegler, _An inverse theorem for the Gowers $U^{s+1}[N]$-norm_, Ann. of Math. (2) **176** (2012), no. 2, 1231–1372. doi:10.4007/annals.2012.176.2.11.
- D. R. Heath-Brown, _Integer sets containing no arithmetic progressions_, J. London Math. Soc. (2) **35** (1987), 385–394.  .
- P. Keevash, N. Lifshitz, E. Long and D. Minzer, _Global hypercontractivity and its applications_, arXiv:2103.04604 (2021).  .
- N. Keller, N. Lifshitz and O. Marcus, _Sharp hypercontractivity for global functions_, J. Eur. Math. Soc., published online January 9, 2026.  ; arXiv:2307.01356v2.
- B. Host and B. Kra, _Nonconventional ergodic averages and nilmanifolds_, Ann. of Math. (2) **161** (2005), no. 1, 397–488. doi:10.4007/annals.2005.161.397.
- V. Bergelson and A. Leibman, _Distribution of values of bounded generalized polynomials_, Acta Math. **198** (2007), 155–230.
- A. Leibman, _Pointwise convergence of ergodic averages for polynomial sequences of translations on a nilmanifold_, Ergodic Theory Dynam. Systems **25** (2005), no. 1, 201–213. doi:10.1017/S0143385704000215.
- J. Leng, _Efficient equidistribution of nilsequences_, arXiv:2312.10772v5, 2023, revised 2024.
- J. Leng, A. Sah and M. Sawhney, _Improved bounds for five-term arithmetic progressions_, Math. Proc. Cambridge Philos. Soc. **177** (2024), no. 3, 371–413.  .
- J. Leng, A. Sah and M. Sawhney, _Improved Bounds for Szemerédi's Theorem_, arXiv:2402.17995 (2024).  .
- J. Leng, A. Sah, and M. Sawhney, _Quasipolynomial bounds on the inverse theorem for the Gowers $U^{s+1}[N]$-norm_, arXiv:2402.17994v3, 2024.
- F. Manners, _Quantitative bounds in the inverse theorem for the Gowers $U^{s+1}$-norms over cyclic groups_, arXiv:1811.00718v2, 2018, revised 2024.
- Z. Kelley and R. Meka, _Strong bounds for 3-progressions_, in _2023 IEEE 64th Annual Symposium on Foundations of Computer Science (FOCS)_, IEEE, 2023, 933–973. doi:10.1109/FOCS57990.2023.00059; revised version arXiv:2302.05537v6 (2024).
- OpenAI, _Quantitative Superexponential Bounds for van der Waerden Numbers_, OpenAI Math Release preprint OAI:Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026, 2026.
- R. Raghavan, _Improved Bounds for 3-Progressions_, arXiv:2603.27045v3 (May 15, 2026).  .
- K. F. Roth, _On certain sets of integers_, J. London Math. Soc. **28** (1953), 104–109.  .
- T. Sanders, _Additive structures in sumsets_, Math. Proc. Cambridge Philos. Soc. **144** (2008), no. 2, 289–316. doi:10.1017/S030500410700093X.
- T. Sanders, _On Roth's theorem on progressions_, Ann. of Math. (2) **174** (2011), no. 1, 619–636.  .
- T. Sanders, _On the Bogolyubov–Ruzsa lemma_, Anal. PDE **5** (2012), no. 3, 627–655. doi:10.2140/apde.2012.5.627.
- T. F. Bloom and O. Sisask, _Logarithmic bounds for Roth's theorem via almost-periodicity_, Discrete Anal. **2019**, Paper No. 4, 20 pp.  .
- T. F. Bloom and O. Sisask, _Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions_, arXiv:2007.03528 (2020), revised 2021.  .
- T. F. Bloom and O. Sisask, _An improvement to the Kelley–Meka bounds on three-term arithmetic progressions_, arXiv:2309.02353 (2023).  .
- T. F. Bloom and O. Sisask, _The Kelley–Meka bounds for sets free of three-term arithmetic progressions_, Essential Number Theory **2** (2023), no. 1, 15–44.  ; revised version arXiv:2302.07211v3 (May 13, 2025).
- E. Croot and O. Sisask, _A probabilistic technique for finding almost-periods of convolutions_, Geom. Funct. Anal. **20** (2010), no. 6, 1367–1396. doi:10.1007/s00039-010-0101-8.
- T. Schoen and O. Sisask, _Roth's theorem for four variables and additive structures in sums of sparse sets_, Forum Math. Sigma **4** (2016), e5. doi:10.1017/fms.2016.2; arXiv:1408.2568.
- E. Szemerédi, _On sets of integers containing no four elements in arithmetic progression_, Acta Math. Acad. Sci. Hungar. **20** (1969), 89–104.  .
- E. Szemerédi, _On sets of integers containing no $k$ elements in arithmetic progression_, Acta Arith. **27** (1975), 199–245. doi:10.4064/aa-27-1-199-245.
- E. Szemerédi, _Integer sets containing no arithmetic progressions_, Acta Math. Hungar. **56** (1990), 155–158.  .
- B. Green and T. Tao, _An inverse theorem for the Gowers $U^3(G)$ norm_, Proc. Edinb. Math. Soc. (2) **51** (2008), no. 1, 73–153. doi:10.1017/S0013091505000325.
- B. Green and T. Tao, _The primes contain arbitrarily long arithmetic progressions_, Ann. of Math. (2) **167** (2008), no. 2, 481–547.  .
- B. Green and T. Tao, _Yet another proof of Szemerédi's theorem_, in _An Irregular Mind: Szemerédi is 70_, Bolyai Soc. Math. Stud. **21**, Springer, 2010, 335–342. doi:10.1007/978-3-642-14444-8\_8.
- B. Green and T. Tao, _The quantitative behaviour of polynomial orbits on nilmanifolds_, Ann. of Math. (2) **175** (2012), no. 2, 465–540. doi:10.4007/annals.2012.175.2.2.
- B. Green and T. Tao, _New bounds for Szemerédi's theorem, III: A polylogarithmic bound for $r_4(N)$_, Mathematika **63** (2017), no. 3, 944–1040.  .
- P. Erdős and P. Turán, _On some sequences of integers_, J. London Math. Soc. **11** (1936), 261–264.  .
- B. L. van der Waerden, _Beweis einer Baudetschen Vermutung_, Nieuw Arch. Wisk. (2) **15** (1927), 212–216.
- T. Ziegler, _Universal characteristic factors and Furstenberg averages_, J. Amer. Math. Soc. **20** (2007), no. 1, 53–97. doi:10.1090/S0894-0347-06-00532-7.
