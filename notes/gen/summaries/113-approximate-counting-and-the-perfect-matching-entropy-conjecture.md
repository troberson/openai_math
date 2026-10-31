[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 113](../index/theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md)

# 113 — Approximate counting and the perfect-matching entropy conjecture

[Index page](../index/theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md)

## Original CONTENTS.md summary

[S1:2777] (family entry):

> **113. Approximate counting and entropy of perfect matchings.** Gives a fully polynomial randomized approximation scheme for counting perfect matchings in arbitrary finite simple graphs, with exact detection of zero counts. Also proves the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant, bounding the maximum entropy of a matching law at every feasible edge-marginal vector in a loopless labelled multigraph, including boundary points. (Lean)

[S1:2784] (the FPRAS manuscript entry, with its abstract at [S1:2786]):

> A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs

> We give a fully polynomial randomized approximation scheme (FPRAS) for counting perfect matchings in arbitrary finite simple undirected graphs, resolving the general-graph perfect-matching approximation problem. The algorithm returns zero with certainty when no perfect matching exists. Otherwise, it achieves relative error *ε* with failure probability at most *δ* in worst-case bit time polynomial in the input length, $`\varepsilon ^{-1}`$, and $`\log\delta^{-1}`$.

[S1:2793] (the Entropy manuscript entry, with its abstract at [S1:2795–2799]):

> Entropy and Face Dimension of the Perfect-Matching Polytope

> We prove the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant. For every feasible vector *x* of perfect-matching edge marginals in a loopless labelled multigraph on $`2m\ge2`$ vertices, the maximum entropy $`H(x)`$ of a matching law with marginals *x* satisfies

[S2:304] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **perfect matching** in a finite undirected graph $`G=(V,E)`$ is a set of
edges that touches every vertex exactly once. Writing $`Z(G)`$ for the number
of such matchings, the finding is easy — Edmonds gave a polynomial-time
algorithm for a maximum matching [S3:153–154] — but the counting is hard:
Valiant showed exact counting is $`\\#`$P-complete even for bipartite graphs
[S3:155–156]. The **FPRAS** is the middle ground: a randomized algorithm
that approximates $`Z(G)`$ within a prescribed relative error, with a
prescribed success probability, in time polynomial in the input length and
the reciprocal error [S3:126–128].

The second manuscript attacks a different question about the same object.
The **perfect-matching polytope** $`P(G)`$ is the convex hull of the
incidence vectors of perfect matchings. A point $`x\in P(G)`$ is an
edge-marginal vector: $`x_e`$ is the probability that edge $`e`$ is in a
randomly drawn matching. The **entropy** $`H(x)`$ is the maximum entropy of a
matching law with those marginals. The conjecture of Anari, Oveis Gharan
and Vinzant asks how far $`H(x)`$ can deviate from the naive entropy
$`F(x)=-\sum_e x_e\log x_e`$ [S5:70–75].

## Graduate summary

**FPRAS** ([S3:132–143], `thm:main`). "There is a uniform classical
randomized algorithm which, given $`G`$ and rational parameters
$`0<\varepsilon<1`$ and $`0<\delta<1/2`$, returns a nonnegative rational number
$`\widehat Z`$ such that $`\Pr[(1-\varepsilon)Z(G)\le\widehat
Z\le(1+\varepsilon)Z(G)]\ge 1-\delta`$" [S3:133–139]. "If $`Z(G)=0`$, the
output is zero with certainty" [S3:140]. The worst-case bit running time is
polynomial in the input encoding length, $`\varepsilon^{-1}`$, and
$`\log\delta^{-1}`$ [S3:141–142].

The proof starts from the complete graph, where perfect matchings are easy
to count, and suppresses the nonedges of $`G`$ by decreasing their positive
activities [S3:246–248]. It estimates ratios of successive partition
functions and multiplies them, updating vertex scales from estimates of the
two-hole partition ratios [S3:248–253]. The sampler uses a product of
perfect-matching spaces on an enlarged colored graph, with exchanges of
alternating cycles between coordinates [S3:265–268]. The spectral gap
follows from an ordered orthogonal decomposition into coordinate
interactions [S3:277–282].

**Entropy bound** ([S5:33–40], `ent:main`). "Let $`G`$ be a loopless
multigraph on $`2m\ge2`$ vertices with at least one perfect matching. For
every $`x\in P(G)`$, $`F(x)-(2-2/m)B(x)\le H(x)\le F(x)`$" [S5:34–39]. The
upper bound $`H\le F`$ is a direct instance of Shearer's entropy inequality
[S5:48–51]. The lower comparison is the contribution: "obtained from a
geometric rank estimate followed by a covariance calculation, with no
assumption that the mean is interior to the full polytope" [S5:51–54].

**Counting consequences** ([S5:76–79]). The theorem gives the explicit
positive answer: $`\log N(G)\le\max_{x\in P(G)}(F(x)+B(x))
\le\log N(G)+3m-2`$ [S5:77–78]. For $`k\ge2`$ edge-disjoint perfect matchings,
the uniform mixture gives $`N(G)\ge e^{-2(m-1)}k^m`$ [S5:86–87].

**Deterministic counting** ([S5:201–212], `thm:main`). "There is one
uniform deterministic algorithm which, on a graph on $`n`$ vertices with
nonnegative binary integer pair multiplicities, returns an integer $`A\ge0`$
satisfying $`N(G)/512^n\le A\le N(G)`$" [S5:203–207]. "In particular, $`A=0`$
exactly when $`N(G)=0`$" [S5:210].

**Face dimension** ([S4:58–59]). "We also prove the sharp bound
$`|\mathrm{supp}\,x|-\dim F_x\le3m-2`$, where $`F_x`$ is the minimal face of
the perfect-matching polytope containing $`x`$" [S4:58–59].

## History of the conjecture

The FPRAS manuscript distinguishes three approximation problems: counting
all matchings, counting bipartite perfect matchings, and counting perfect
matchings in general graphs [S3:160–162]. Jerrum and Sinclair gave an FPRAS
for the total number of matchings [S3:163–166]. Jerrum, Sinclair, and
Vigoda removed the ratio restriction in the bipartite setting and obtained
an FPRAS for the permanent of every nonnegative matrix [S3:175–177].
"The general-graph question was explicitly raised by Jerrum and Sinclair
and remained a benchmark for approximate counting" [S3:180–182]. A direct
extension of the bipartite chain faces a precise
obstruction: "Štefankovič, Vigoda, and Wilmes constructed graphs on which
every JSV-type chain has either exponentially small stationary probability
of perfect matchings or exponentially slow mixing" [S3:189–192].

The entropy manuscript attributes the conjecture to Anari, Oveis Gharan
and Vinzant, who "proposed a convex-optimization framework for approximate
counting" [S5:70–71]. The bipartite setting admits a coefficient-one
comparison through Schrijver's inequality and the weighted Bethe inequality
of Gurvits [S5:56–60]. The manuscript gives "a simple eight-vertex
nonbipartite graph with a feasible mean for which $`H<F-B`$" [S5:61–63],
showing the odd cuts are load-bearing.

**Prior (my training data, not this repo).** The FPRAS for general-graph
perfect matchings was a long-standing open problem, explicitly listed in
Jerrum and Sinclair's 1989 paper. The entropy conjecture of Anari, Oveis
Gharan and Vinzant (FOCS 2018) was a natural extension of the Bethe /
Schrijver inequality from bipartite to general graphs. I cannot confirm
these independently; the release ships both manuscripts as proofs.

## Consequences

- **The FPRAS.** A randomized polynomial-time approximation for counting
  perfect matchings in any finite simple undirected graph, with exact zero
  detection [S3:132–143].
- **The entropy bound.** $`F(x)-(2-2/m)B(x)\le H(x)\le F(x)`$ for every
  feasible marginal in a loopless multigraph, including boundary points
  [S5:33–40].
- **The log-N bound.** $`\log N(G)\le\max_{x\in P(G)}(F(x)+B(x))
  \le\log N(G)+3m-2`$ [S5:76–79].
- **The deterministic approximation.** $`N(G)/512^n\le A\le N(G)`$ with
  exact zero detection [S5:201–212].
- **The face-dimension bound.** $`|\mathrm{supp}\,x|-\dim F_x\le3m-2`$ for
  the minimal face [S4:58–59] — not formalized.

## Section skeleton

The FPRAS is a single file [S3] of 3472 lines: the preamble through line
105, the document body from `\begin{document}` at [S3:106], the abstract at
[S3:109–115], the introduction with its history subsection at [S3:118–241],
the proof architecture at [S3:243+], and the remaining sections and
bibliography. The shipped PDF [S6] is the manuscript in the form the release
distributes.

The Entropy manuscript [S4] is a 78-line root that includes nine section
files and three appendix files [S4:61–74]. The section files sit under
`build/sections/` and `build/appendices/`. The shipped PDF [S7] is the
manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S8],
**six** comparator stubs [S9–S14], and **three** `main_results` entries
[S18]. The yaml `sources:` lists only the Entropy manuscript [S18:394] —
the FPRAS manuscript is not a formalization source, so `paps_form=1` of 2.

The scope note's Scope section states: "the formalization gives a fully
polynomial randomized approximation scheme for counting perfect matchings
in every finite simple undirected graph" [S8:10], and for the entropy
bound: "the formalization proves $`F(x)-(2-2/m)B(x)\le H(x)\le F(x)`$ for
$`m\ge1`$, including boundary points of the polytope" [S8:14]. The note is
explicit about what it does not carry: "It retains the earlier
coefficient-eight entropy bound and the deterministic counting
approximations with factors $`512^n`$ for loopless graphs and $`2^{18n}`$ with
singleton loops" [S8:14], and "the paper's sharp global face-dimension
bound is not part of that selected statement" [S8:16].

The three `main_results` entries name:

- `OAI.BinaryMatching.deterministic_approximate_counting` in
  `BinarySolve.lean` [S18:1013–1015]
- `OAI.MatchingEntropy.entropy_main` in `PerfectMatching/Main.lean`
  [S18:1385–1387]
- `OAI.LoopMatching.fullEndpoint` in `LoopMatching/Main.lean`
  [S18:1605–1607]

The formalized `entropy_main` [S15:85–89] proves the **coefficient-8**
bound: `marginalEntropy y - maxMatchingEntropy G y ≤ 8 * (m : ℝ) *
(1 - Real.exp (-marginalEntropy y / (m : ℝ)))` — not the paper's
coefficient-$`2-2/m`$ bound. The formalized
`deterministic_approximate_counting` [S16:143–149] proves the
$`2^{9n}`$-factor approximation with an existence-and-soundness statement
citing the raw witness: `Raw.InputData.deterministic_approximate_counting`.
The formalized `fullEndpoint` [S17:24–26] closes over the singleton-loop
machine's computational endpoint and correctness witness.

The **five unformalized** comparator stubs each carry exactly one `sorry`:
`thm_main` [S9:105–106], `Refined.pointwise_entropy` [S13:73–78],
`triangle_expansion_face` [S14:169–182], and the two that have `main_results`
entries are the ones proved under `lean/OAI/`. The FPRAS stub [S9:105–106] states
the full FPRAS as a `MainStatement` over a `RandomMachine` — a
finite-alphabet Post-Turing machine with a fixed-degree polynomial
time bound — and its `thm_main` closes in `sorry` [S9:106]. The
refined-entropy stub [S13:73–78] states the paper's exact coefficient-$`2-2/m`$
bound as a conjunction of the lower and upper comparisons, and its
`Refined.pointwise_entropy` closes in `sorry` [S13:78]. The triangle-face
stub [S14:169–174] states the face correspondence under triangle expansion with
the `minFace` carry-through, and its `triangle_expansion_face` closes in
`sorry` [S14:182+]. Zero `sorry` in the three formalized trees
(MatchingCount, PerfectMatching, LoopMatching).

The reading is of source text only — no `lake` or `lean` run elaborates
the proofs, so the claim here is that the proof bodies exist in the source,
not that the files compile.

**Tree measurement (source-level).**

The family registers 3 `main_results` declarations (`OAI.MatchingEntropy.entropy_main`; `OAI.BinaryMatching.deterministic_approximate_counting`; `OAI.LoopMatching.fullEndpoint`); the primary file `OAI/Combinatorics/PerfectMatching/Main.lean` carries 213 lines with top-level theorem `theorem entropy_barrier_ge_id {t`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 39 files with 230 theorems and 99 defs.

The preprint states 62 theorem environments; the tree carries 4× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=113` [S19] records the tier and the counts: `tier=T3`,
`paps=2`, `paps_form=1`, `chal=6`, `mainres=3`, `scope_note=1`,
`verification=0`, `trace=`. This is a two-manuscript family in which only
the Entropy manuscript is a formalization source [S18:394] — the FPRAS
manuscript is not named in the yaml `sources:`, so `paps_form=1` of 2.
The six comparator stubs [S9–S14] spread over three `main_results` entries
[S18] means three of the six have a proved copy under `lean/OAI/` and
three do not. The shape flags are `resolution|bound|uniform` with
`resolves_named=1`: the family title names both the FPRAS and the entropy
conjecture, and the ledger verb rule fires on the release blurb. There is
no verification bundle and no reasoning trace; the two shipped PDFs
[S6] [S7] and the Lean layer [S8–S18] are the evidence surfaces.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2777], the FPRAS manuscript link [S1:2784] and abstract [S1:2786], the Entropy manuscript link [S1:2793] and abstract [S1:2795–2799]. The release's inline code spans stay as backticked markdown, and the release's italic markup is folded to the plain word |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 113 at [S2:304] |
| S3 | [`preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/main.tex`](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/main.tex) | 3471 | root (`\documentclass`); `\newcommand{\eps}{\varepsilon}` at [S3:91]; abstract [S3:109–115]; `thm:main` [S3:132–143]; history [S3:151–241]; proof architecture [S3:243+] |
| S4 | [`preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/main.tex`](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/main.tex) | 77 | root (`\documentclass`); `\DeclareMathOperator{\supp}{supp}` at [S4:23]; abstract [S4:48–59]; include order [S4:61–70] |
| S5 | [`preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/sections/01-introduction.tex) | 287 | `ent:main` [S5:33–40]; the Shearer's-inequality paragraph [S5:48–54]; the Anari–Oveis Gharan–Vinzant conjecture [S5:70–79]; the $k$-disjoint consequence [S5:84–87]; the deterministic counting theorem [S5:201–212] |
| S6 | [`preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf`](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf) | 17626 | the FPRAS manuscript as shipped |
| S7 | [`preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf`](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf) | 18190 | the Entropy manuscript as shipped |
| S8 | [`lean/docs/113.md`](../../../lean/docs/113.md) | 27 | scope note — the four Scope paragraphs at [S8:10–16] and the six comparator links at [S8:22–27] |
| S9 | [`lean/ComparatorChallenges/MatchingFPRAS.lean`](../../../lean/ComparatorChallenges/MatchingFPRAS.lean) | 110 | the FPRAS comparator stub — `thm_main` at [S9:105–106] with its `sorry` |
| S10 | [`lean/ComparatorChallenges/MatchingEntropy.lean`](../../../lean/ComparatorChallenges/MatchingEntropy.lean) | 69 | the entropy comparator stub — `entropy_main` at [S10:58–63] with its `sorry` |
| S11 | [`lean/ComparatorChallenges/BinaryMatching.lean`](../../../lean/ComparatorChallenges/BinaryMatching.lean) | 76 | the deterministic-counting comparator stub — `deterministic_approximate_counting` at [S11:66–72] with its `sorry` |
| S12 | [`lean/ComparatorChallenges/SingletonLoopMatching.lean`](../../../lean/ComparatorChallenges/SingletonLoopMatching.lean) | 132 | the singleton-loop comparator stub — `fullEndpoint` at [S12:127–128] with its `sorry` |
| S13 | [`lean/ComparatorChallenges/MatchingEntropyBounds.lean`](../../../lean/ComparatorChallenges/MatchingEntropyBounds.lean) | 84 | the refined-entropy comparator stub — `Refined.pointwise_entropy` at [S13:73–78] with its `sorry` |
| S14 | [`lean/ComparatorChallenges/TriangleFace.lean`](../../../lean/ComparatorChallenges/TriangleFace.lean) | 190 | the triangle-face comparator stub — `triangle_expansion_face` at [S14:169–182] with its `sorry` |
| S15 | [`lean/OAI/Combinatorics/PerfectMatching/Main.lean`](../../../lean/OAI/Combinatorics/PerfectMatching/Main.lean) | 213 | the formalized entropy file — `entropy_main` proved at [S15:85–89] |
| S16 | [`lean/OAI/Computability/MatchingCount/BinarySolve.lean`](../../../lean/OAI/Computability/MatchingCount/BinarySolve.lean) | 153 | the formalized deterministic-counting file — `deterministic_approximate_counting` proved at [S16:143–149] |
| S17 | [`lean/OAI/Computability/LoopMatching/Main.lean`](../../../lean/OAI/Computability/LoopMatching/Main.lean) | 30 | the formalized singleton-loop file — `fullEndpoint` proved at [S17:24–26] |
| S18 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `sources:` entry naming the Entropy manuscript at [S18:394]; the three `main_results` entries at [S18:1013–1015], [S18:1385–1387], [S18:1605–1607] |
| S19 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=113`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- Wassily Hoeffding. Probability inequalities for sums of bounded random variables. _Journal of the American Statistical Association_, 58 (301): 13–30, 1963. doi:10.1080/01621459.1963.10500830.
- Ivona Bezáková, Daniel Štefankovič, Vijay V. Vazirani, and Eric Vigoda. Accelerating simulated annealing for the permanent and combinatorial counting problems. _SIAM Journal on Computing_, 37 (5): 1429–1454, 2008. doi:10.1137/050644033.
- W. K. Hastings. Monte Carlo sampling methods using Markov chains and their applications. _Biometrika_, 57 (1): 97–109, 1970. doi:10.1093/biomet/57.1.97.
- Xiaoyu Chen, Heng Guo, Eric Vigoda, and Xiongxin Yang. Fast FPRAS for the permanent. Preprint, arXiv:2609.20717v1, 2026. URL .
- Xiaoyu Chen, Eric Vigoda, and Xiongxin Yang. Faster FPRAS for the permanent via restricted Poincaré inequalities and coupled flows. Preprint, arXiv:2608.26599v1, 2026. URL .
- Alistair Sinclair. Improved bounds for mixing rates of Markov chains and multicommodity flow. _Combinatorics, Probability and Computing_, 1: 351–370, 1992. URL .
- Mark Jerrum and Alistair Sinclair. Approximating the permanent. _SIAM Journal on Computing_, 18 (6): 1149–1178, 1989. doi:10.1137/0218077.
- Jin-Yi Cai and Tianyu Liu. Counting perfect matchings and the eight-vertex model. In Artur Czumaj, Anuj Dawar, and Emanuela Merelli, editors, _47th International Colloquium on Automata, Languages, and Programming (ICALP 2020)_, volume 168 of _Leibniz International Proceedings in Informatics_, pages 23:1–23:18. Schloss Dagstuhl–Leibniz-Zentrum für Informatik, 2020. doi:10.4230/LIPIcs.ICALP.2020.23. URL .
- Yumou Fei, Leslie Ann Goldberg, and Pinyan Lu. Two-state spin systems with negative interactions. _Information and Computation_, 307: 105340, 2025. doi:10.1016/j.ic.2025.105340.
- Mark Jerrum, Alistair Sinclair, and Eric Vigoda. A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries. _Journal of the ACM_, 51 (4): 671–697, 2004. doi:10.1145/1008731.1008738.
- Mark R. Jerrum, Leslie G. Valiant, and Vijay V. Vazirani. Random generation of combinatorial structures from a uniform distribution. _Theoretical Computer Science_, 43: 169–188, 1986. doi:10.1016/0304-3975(86)90174-X.
- Robert H. Swendsen and Jian-Sheng Wang. Replica Monte Carlo simulation of spin-glasses. _Physical Review Letters_, 57 (21): 2607–2609, 1986. doi:10.1103/PhysRevLett.57.2607.
- W. T. Tutte. A short proof of the factor theorem for finite graphs. _Canadian Journal of Mathematics_, 6: 347–352, 1954. doi:10.4153/CJM-1954-033-3.
- Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller, and Edward Teller. Equation of state calculations by fast computing machines. _The Journal of Chemical Physics_, 21 (6): 1087–1092, 1953. doi:10.1063/1.1699114.
- Jack Edmonds. Paths, trees, and flowers. _Canadian Journal of Mathematics_, 17: 449–467, 1965. doi:10.4153/CJM-1965-045-4.
- P. W. Kasteleyn. Dimer statistics and phase transitions. _Journal of Mathematical Physics_, 4 (2): 287–293, 1963. doi:10.1063/1.1703953.
- Zihong Yi. Diffuse Gaussian truncation for deterministic approximate counting. Preprint, arXiv:2609.04079v1, 2026. URL .
- Leslie G. Valiant. The complexity of computing the permanent. _Theoretical Computer Science_, 8 (2): 189–201, 1979. doi:10.1016/0304-3975(79)90044-6.
- Bradley Efron and Charles Stein. The jackknife estimate of variance. _The Annals of Statistics_, 9 (3): 586–596, 1981. doi:10.1214/aos/1176345462.
- Jian-Sheng Wang and Robert H. Swendsen. Replica Monte Carlo simulation (revisited). _Progress of Theoretical Physics Supplement_, 157: 317–323, 2005. doi:10.1143/PTPS.157.317. Preprint version: .
- Daniel Štefankovič, Eric Vigoda, and John Wilmes. On counting perfect matchings in general graphs. In Michael A. Bender, Martín Farach-Colton, and Miguel A. Mosteiro, editors, _LATIN 2018: Theoretical Informatics_, volume 10807 of _Lecture Notes in Computer Science_, pages 873–885. Springer, 2018. doi:10.1007/978-3-319-77404-6_63. Full version: arXiv:1712.07504v1. URL .
