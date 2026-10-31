[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 114](../index/theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md)

# 114 — Approximate counting of common integer polymatroid bases

[Index page](../index/theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md)

## Original CONTENTS.md summary

[S1:2806] (family entry):

> **114. Approximate counting of common integer polymatroid bases.** Gives a fully polynomial randomized approximation scheme for counting common integer bases of two integral polymatroids of equal total rank, supplied by exact rank-value oracles. Capacities are binary-encoded, each integer vector counts once, and oracle calls and bit operations outside the oracles are polynomial on every execution. For matroids presented by independence oracles, the results also cover common independent sets of prescribed, unrestricted, or maximum cardinality, even when the ranks differ. (Lean)

[S1:2813] (the polymatroid manuscript entry, with its abstract at [S1:2815]):

> An FPRAS for Common Integer Polymatroid Bases with Binary Capacities

> We give a fully polynomial randomized approximation scheme for counting common integer bases of two polymatroids with the same total rank, supplied by exact rank-value oracles. The total rank and capacities are encoded in binary, and each integer vector is counted once. On every execution, the number of oracle calls and the bit work outside the oracles are bounded by a fixed polynomial in the ground-set size, the binary input length, the inverse relative-error tolerance, and the logarithm of the inverse failure probability. The algorithm handles binary capacities directly, without expanding them into labelled copies.

[S1:2822] (the matroid manuscript entry, with its abstract at [S1:2824]):

> Approximate counting of common bases of two matroids

> We give a fully polynomial randomized approximation scheme for counting the common bases of two arbitrary matroids of the same rank, supplied by independence oracles. The algorithm requires no explicit representation of either matroid and has polynomial bounds on both oracle calls and bit operations on every execution.

[S2:306] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **matroid** is a combinatorial structure that generalizes the notion of
linear independence: it is a collection of subsets of a finite set (called
*independent sets*) that is closed under taking subsets and satisfies an
augmentation property. A **basis** is a maximal independent set, and every
basis has the same size — the matroid's **rank**. Two matroids on the same
ground set can share bases: subsets that are independent in *both*. Counting
those shared bases is the problem this family tackles.

The difficulty is that the matroids are given only by **independence
oracles** — black boxes that answer "is this subset independent?" — with no
explicit list of independent sets. An **FPRAS** (fully polynomial randomized
approximation scheme) is the target: a randomized algorithm that approximates
the count within a prescribed relative error $`\varepsilon`$ with high
probability $`1-\delta`$, running in time polynomial in the input size,
$`\varepsilon^{-1}`$, and $`\log\delta^{-1}`$ [S3:50–54].

The second manuscript generalizes from matroids to **integer polymatroids**,
where the rank is replaced by a submodular capacity function and the bases are
integer vectors satisfying $`x(E)=R`$ and $`x(A)\le r_i(A)`$ for all subsets
$`A`$ [S5:33–38]. The counting problem is the same shape — count the common
feasible integer vectors — but the capacities are binary-encoded, so a large
capacity admits exponentially many coordinate values without inflating the
input size [S5:40–41].

## Graduate summary

**Matroid FPRAS** ([S3:86–104], `thm:main`). "There is a single randomized
oracle algorithm with the following guarantee. Given independence oracles for
arbitrary rank-$`r`$ matroids $`M_1,M_2`$ on $`[n]`$, and rational
$`\epsilon,\delta\in(0,1)`$, it outputs a nonnegative rational $`\widehat Z`$
such that $`\Pr[(1-\epsilon)Z(M_1,M_2)\le\widehat
Z\le(1+\epsilon)Z(M_1,M_2)]\ge1-\delta`$" [S3:87–90]. "If $`Z(M_1,M_2)=0`$,
its output is always zero. On every execution, the number of oracle calls and
the number of other bit operations are bounded by a fixed polynomial in
$`n,\ell,\epsilon^{-1},\log\delta^{-1}`$" [S3:95–97]. The polynomial bound is
on *every* execution, not only in expectation.

**Polymatroid FPRAS** ([S5:53–67], `thm:main`). "There is a single uniform
randomized algorithm which, for every input described above, outputs a
nonnegative rational $`\widehat Z`$ satisfying
$`\mathbb P((1-\varepsilon)Z\le\widehat Z\le(1+\varepsilon)Z)\ge1-\delta`$" [S5:54–57]. "If $`Z=0`$,
the algorithm outputs zero on every execution. On every execution, both its
number of oracle calls and its number of other bit operations are bounded by
one fixed polynomial in $`n,\ell,\varepsilon^{-1},\log(\delta^{-1})`$" [S5:58–61].

**Common independent sets** ([S3:1471–1477], `cor:intersection`). "The
equal-rank common-bases theorem also gives counting and sampling algorithms
for common independent sets when the input ranks differ. Truncation reduces
prescribed-cardinality counting to common bases; self-reduction then supplies
sampling" [S3:1474–1477]. For each of the three families $`\mathcal C_k`$
(prescribed cardinality), $`\mathcal C`$ (unrestricted), and $`\mathcal C_{\max}`$
(maximum cardinality), the corollary gives both an FPRAS and an
almost-uniform sampler with the same polynomial work bound [S3:1479–1535].

## History of the conjecture

The matroid manuscript situates the result in a line of work on approximate
counting and sampling for matroid-related objects. "Matroid intersection
admits a deterministic polynomial-time optimization algorithm in the
independence-oracle model" [S3:116–117]. "Jerrum, Sinclair, and Vigoda gave an
FPRAS for the permanent of a nonnegative matrix, which includes this
bipartite matching problem" [S3:125–127]. For single matroids, "Anari, Liu,
Oveis Gharan, and Vinzant removed such restrictions for single-matroid
counting by developing high-dimensional walks for log-concave polynomials,
obtaining an independence-oracle FPRAS" [S3:138–140]. For intersections, the
strongest prior result was a "$`2^{O(r)}`$-factor approximation for common bases
of arbitrary rank-$`r`$ independence-oracle matroids" [S3:154–156] — fully
polynomial only when $`r=O(\log n)`$. "The question of an FPRAS for two
arbitrary independence-oracle matroids is explicitly recorded in Liu's
dissertation" [S3:171–172].

The proof strategy is a **paired-ground-set reduction**: "We first replace
common bases by transversal bases of one matroid. This gives a single
rank-deficiency weight that can be evaluated using the two input oracles"
[S3:246–247]. The state space is a rank-$`n`$ matroid on $`2n`$ elements choosing
one from each of $`n`$ pairs, with a negative-weight annealing schedule
[S3:176–180]. The algebraic input is the Brändén–Huh homogeneous Tutte theorem,
which yields quadratic signature inequalities and a missing-slot transport
bound [S3:200–209]. A Metropolis chain on the augmented state space mixes
rapidly for the trace, and the variance bound closes the counting gap
[S3:218–228].

The polymatroid manuscript builds on the matroid framework. "The proof builds
on the common-matroid-base counting framework and its two-lift extension for
cell-bounded contingency tables" [S5:13–14]. The new reduction "keeps only
part totals with polynomially many possible values as discrete variables" and
"treats the remaining degrees of freedom by weighted volume approximation"
[S5:15–17].

**Prior (my training data, not this repo).** FPRAS for the permanent (bipartite
matching) was given by Jerrum, Sinclair, and Vigoda in 2004. The extension to
arbitrary two-matroid common bases was a natural open problem in the
approximate-counting community. The $`2^{O(r)}`$-factor bound of Anari, Oveis
Gharan, and Vinzant (2021) was the best known for unrestricted-rank
independence-oracle matroids before this work. I cannot confirm these
independently; the release ships both manuscripts as proofs.

## Consequences

- **Matroid FPRAS.** A randomized polynomial-time approximation for counting
  common bases of two arbitrary rank-$`r`$ independence-oracle matroids, with
  exact zero detection and a work bound on every execution [S3:86–104].
- **Polymatroid FPRAS.** The same guarantee for common integer bases of two
  integer polymatroids with binary-encoded capacities [S5:53–67].
- **Common independent sets.** Counting and sampling for prescribed,
  unrestricted, or maximum-cardinality common independent sets, even when the
  ranks differ [S3:1471–1535].
- **Almost-uniform sampling.** For each of the three families, an
  almost-uniform sampler with total-variation tolerance $`\theta`$ and
  polynomial dependence on $`\theta^{-1}`$ [S3:1500–1530].

## Section skeleton

The matroid manuscript [S3] is a single self-contained file of 1831 lines:
the preamble through line 56, the document body from `\begin{document}` at
[S3:48], the abstract at [S3:50–54], the introduction with its proof-strategy
subsection at [S3:57–241], the paired-ground-set reduction at [S3:244+], the
signature inequalities and transport bound, the chain and Poincaré bound,
the simulation and algorithm sections, the oracle implementation, and the
common-independent-sets corollary at [S3:1471+]. The shipped PDF [S6] is the
manuscript in the form the release distributes.

The polymatroid manuscript [S4] is an 89-line root that includes seven section
files under `build/sections/` [S4:75–81]: `introduction`, `polyhedra`,
`signatures`, `geometry`, `ports`, `evaluation`, `counting`. The shipped PDF
[S7] is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S8],
**one** comparator stub [S9], and **one** `main_results` entry [S11]. The
yaml `sources:` lists only the matroid manuscript [S11:287–289] — the
polymatroid manuscript is not a formalization source, so `paps_form=1` of 2.

The scope note's Scope section states: "The formalized result gives a fully
polynomial randomized approximation scheme for the number of common bases of
two equal-rank matroids on an enumerated finite ground set, using independence
oracles. For rational $`0<\varepsilon,\delta<1`$, the nonnegative rational
output has relative error at most $`\varepsilon`$ with probability at least
$`1-\delta`$. A zero count produces zero on every execution. Oracle calls and
bit operations have polynomial bounds on every random tape in the input size,
$`\varepsilon^{-1}`$, and $`\log(\delta^{-1})`$" [S8:9]. The note carries no
exclusions — the formalized statement *is* the FPRAS, and the scope is the
full machine-level guarantee, not a weakened bound.

The single `main_results` entry names `OAI.common_bases_fpras` in
`OAI/Combinatorics/MatroidCounting/CommonBases.lean` [S11:1085–1087]. The
formalized proof [S10:26093–26124] is a 32-line construction: it obtains a
frozen uniform safe parameter, computes the total resource polynomial, and
refines the existential into a concrete machine program `fprasBlock` with
coefficients and a degree bound. The proof body invokes `frozen_machine`,
`physical_accuracy`, and `monomial_bound` — 26,126 lines of definitions and
lemmas in the file above the theorem, zero `sorry`.

The comparator stub [S9] is the tree's own machine model with the proof
deleted: it defines `IndependenceOracle`, `commonBaseCount`, a
`MachineConfig` with registers and counters, a `machineStep` with five
instruction forms (`push`, `pop`, `coin`, `query`, `halt`), and the
`MainTheorem` as an existential over a program, coefficients, and resource
bound [S9:108–126]. The theorem `common_bases_fpras :
CommonBasesFPRAS.MainTheorem := by sorry` [S9:128–129] closes with the single
`sorry`.

The reading is of source text only — no `lake` or `lean` run elaborates the
proofs, so the claim here is that the proof body exists in the source, not
that the file compiles.

**Tree measurement (source-level).**

The `main_results` entry OAI.common_bases_fpras resolves to `OAI/Combinatorics/MatroidCounting/CommonBases.lean` (26126 lines); the top-level theorem is `theorem onePositive_of_nonpositive_kernel (B`.

A carrier `MainTheorem : Prop` at line 110 states the formalized claim.

The directory is small (1 files, 100 theorems, 867 defs).

The preprint states 37 theorem environments; the tree carries 3× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=114` [S12] records the tier and the counts: `tier=T3`,
`paps=2`, `paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`,
`verification=0`, `trace=`. This is a two-manuscript family in which only the
matroid manuscript is a formalization source [S11:287–289] — the polymatroid
manuscript is not named in the yaml `sources:`, so `paps_form=1` of 2. The
single comparator stub [S9] carries the one `main_results` entry [S11], so
the challenge has a proved copy under `lean/OAI/` [S10]. There is no
verification bundle and no reasoning trace; the two shipped PDFs [S6] [S7]
and the Lean layer [S8–S11] are the evidence surfaces.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2806], polymatroid link [S1:2813] and abstract [S1:2815], matroid link [S1:2822] and abstract [S1:2824] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 114 at [S2:306] |
| S3 | [`preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/main.tex`](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/main.tex) | 1831 | root (`\documentclass`); abstract [S3:50–54]; `thm:main` [S3:86–104]; history [S3:116–174]; reduction [S3:244+]; corollary [S3:1471+]; 1831 lines |
| S4 | [`preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/main.tex`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/main.tex) | 89 | root (`\documentclass`); abstract [S4:63–72]; seven `\input` directives [S4:75–81]; 89 lines |
| S5 | [`preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/sections/introduction.tex`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/sections/introduction.tex) | 216 | `thm:main` [S5:53–67]; the counting problem [S5:33–41]; context [S5:109+]; 216 lines |
| S6 | [`preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf`](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf) | 13323 | the matroid manuscript as shipped |
| S7 | [`preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) | 17454 | the polymatroid manuscript as shipped |
| S8 | [`lean/docs/114.md`](../../../lean/docs/114.md) | 15 | scope note — the Scope paragraph at [S8:9] and the comparator link at [S8:15] |
| S9 | [`lean/ComparatorChallenges/CommonBasesFPRAS.lean`](../../../lean/ComparatorChallenges/CommonBasesFPRAS.lean) | 131 | the comparator stub — `MainTheorem` at [S9:108]; `common_bases_fpras` at [S9:128–129] with its `sorry` |
| S10 | [`lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean`](../../../lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean) | 26126 | the formalized proof — `common_bases_fpras` proved at [S10:26093–26124]; 26,126 lines, zero `sorry` |
| S11 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `sources:` entry naming the matroid manuscript at [S11:287–289]; the `main_results` entry at [S11:1085–1087] |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=114`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- Peter G. Doyle and J. Laurie Snell.  Random Walks and Electric Networks. Web edition dated July 5, 2006, derived from the 1984 MAA book. .
- Yeganeh Alimohammadi, Nima Anari, Kirankumar Shiragur, and Thuy-Duong Vuong. Fractionally log-concave and sector-stable polynomials: Counting planar matchings and more. arXiv:2102.02708, version 3, April 3, 2023; first posted 2021. .
- Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant. Log-concave polynomials II: High-dimensional walks and an FPRAS for counting bases of a matroid.  Annals of Mathematics, 199(1):259–299, 2024. . Preprint locators refer to arXiv version 3, January 18, 2019: .
- Nima Anari, Shayan Oveis Gharan, and Alireza Rezaei. Monte Carlo Markov chain algorithms for sampling strongly Rayleigh distributions and determinantal point processes. In  29th Annual Conference on Learning Theory, volume 49 of  Proceedings of Machine Learning Research, pages 103–115. PMLR, 2016. .
- Nima Anari, Shayan Oveis Gharan, and Cynthia Vinzant. Log-concave polynomials, I: Entropy and a deterministic approximation algorithm for counting bases of matroids.  Duke Mathematical Journal, 170(16):3459–3504, 2021. . Preprint locators refer to arXiv version 2, November 5, 2018: .
- Damian Straszak and Nisheeth K. Vishnoi. Real stable polynomials and matroids: Optimization and counting. arXiv:1611.04548, version 1, November 14, 2016. .
- Nima Anari and Shayan Oveis Gharan. A generalization of permanent inequalities and applications in counting and optimization. arXiv:1702.02937, version 1, February 9, 2017. .
- Petter Brändén and June Huh. Hodge–Riemann relations for Potts model partition functions. arXiv:1811.01696, version 2, February 11, 2019; first posted 2018. .
- Xiaoyu Chen, Weiming Feng, Zhe Ju, Tianshun Miao, Yitong Yin, and Xinyuan Zhang. Faster mixing of the Jerrum–Sinclair chain. arXiv:2504.02740, version 1, April 3, 2025. .
- Xiaoyu Chen, Eric Vigoda, and Xiongxin Yang. Faster FPRAS for the permanent via restricted Poincaré inequalities and coupled flows. arXiv:2608.26599, version 1, August 27, 2026. .
- Tomás Feder and Milena Mihail. Balanced matroids. In  Proceedings of the Twenty-Fourth Annual ACM Symposium on Theory of Computing, pages 26–38. Association for Computing Machinery, 1992. .
- Mary Cryan, Heng Guo, and Giorgos Mousa. Modified log-Sobolev inequalities for strongly log-concave distributions.  Annals of Probability, 49(1):506–525, 2021. . Preprint locators refer to arXiv version 4, August 8, 2020: .
- Alexander Schrijver.  Combinatorial Optimization: Polyhedra and Efficiency, volume 24 of  Algorithms and Combinatorics. Springer, Berlin, 2003. .
- Jack Edmonds. Matroid intersection. In  Discrete Optimization I, volume 4 of  Annals of Discrete Mathematics, pages 39–49. North-Holland, 1979. .
- Mark Jerrum, Alistair Sinclair, and Eric Vigoda. A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries.  Journal of the ACM, 51(4):671–697, 2004. .
- Mark R. Jerrum, Leslie G. Valiant, and Vijay V. Vazirani. Random generation of combinatorial structures from a uniform distribution.  Theoretical Computer Science, 43(2–3):169–188, 1986. .
- Petter Brändén and June Huh. Lorentzian polynomials.  Annals of Mathematics, 192(3):821–891, 2020. .
- David Aldous and James Allen Fill.  Reversible Markov Chains and Random Walks on Graphs. Unfinished monograph, 2002, recompiled 2014. .
- Claude Kipnis and S. R. S. Varadhan. Central limit theorems for additive functionals of reversible Markov chains and applications. { Astérisque}, 132:65–70, 1985. .
- Kuikui Liu.  Spectral Independence: A New Tool to Analyze Markov Chains. PhD thesis, University of Washington, 2023. Section 13.2, Problem 1, p. 197. .
- Alexander Barvinok and Alex Samorodnitsky. Random weighting, asymptotic counting, and inverse isoperimetry.  Israel Journal of Mathematics, 158:159–191, 2007. . Preprint version 2, June 4, 2003: .
