[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 378](../index/theoretical-computer-science/378-disproof-of-the-exponential-time-hypothesis.md)

# 378 — Disproof of the Exponential Time Hypothesis

[Index page](../index/theoretical-computer-science/378-disproof-of-the-exponential-time-hypothesis.md)

## Original CONTENTS.md summary

The release's blurb 

> We give a deterministic algorithm for exactly counting the satisfying assignments of an arbitrary $`k`$-CNF formula. For every fixed $`k\geqslant2`$, on a formula with $`n`$ variables and $`m`$ clauses, our algorithm uses space polynomial in $`n`$ and $`m`$ and runs in time $`(n+m)^{O_k(1)}2^{n/(\log n)^{1/2+o(1)}}`$. Our algorithm refutes the Exponential Time Hypothesis (ETH), which postulates that deciding 3-SAT on $`n`$ variables requires $`2^{\Omega(n)}`$ time in the worst case. [S1:9163]

The catalog entry [S11:363] restates the claim and adds the circuit
lower bound consequence: it "yields superlinear circuit lower bounds
for a language in $\mathsf{E}^{\mathsf{NP}}$ on infinitely many input
lengths." The manuscript abstract 

> We give a deterministic algorithm for exactly counting the satisfying assignments
of an arbitrary $k$-CNF formula.
For every fixed $k\geqslant2$, on a formula with $n$ variables and $m$ clauses,
our algorithm uses $\mathrm{poly}_k(n,m)$ space and runs in time
$(n+m)^{O_k(1)}2^{\,n/(\log n)^{\frac12+o(1)}}$.
Our algorithm refutes the Exponential Time Hypothesis (ETH), which
postulates that deciding $3$-SAT on $n$ variables requires
$2^{\Omega(n)}$ time in the worst case. [S2:30–39]

## Undergraduate summary

The Exponential Time Hypothesis (ETH) is the conjecture that $k$-SAT
requires $2^{\Omega(n)}$ time in the worst case. It underlies most
fine-grained complexity lower bounds: proving ETH false would break a
large body of conditional hardness results. The paper refutes ETH by
giving a deterministic algorithm that *counts* satisfying assignments
of a $k$-CNF in subexponential time. Counting is a priori harder than
deciding, but testing whether the count is positive decides
satisfiability, so the counting algorithm also decides $k$-SAT in
subexponential time.

The proof works in three stages. First, reduce to a bounded-occurrence
setting where each variable appears in at most three clauses, using
sparsification and a standard variable-copy reduction. Second, build a
polynomial whose constant term equals the count, and evaluate it at
$Q$ points using a group-separation scheme: at each point, the
variables are partitioned into $r$ groups, and a small set of shared
measurements lets each group be evaluated independently. Third, recover
the count from the evaluation points by polynomial interpolation. The
key new ingredient is a low-degree replacement for the original clause
polynomials that makes the group separation work with subexponential
cost.

The manuscript states the result 

> **theorem**
For each fixed $k\geqslant2$, there exists a deterministic algorithm that,
given a $k$-CNF $F$ on $n\geqslant20$ declared variables with $m$ clauses,
computes $\\\#F$ as defined in in
$$(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$$
bit operations and $(n+m)^{O_k(1)}$ bits of space.
For each fixed $D>0$, its running time on inputs with $m\leqslant Dn$ is
$$(n+m)^{O_{k,D}(1)}2^{O_{k,D}(n/\sqrt{\log n})}.$$ [S2:73–85]

The fixed-density case $m\leqslant Dn$ gives the sharper
$2^{O_{k,D}(n/\sqrt{\log n})}$ bound, which is what the circuit lower
bound and the graph-counting corollaries use.

## Graduate summary

The main result is Theorem `thm:main` 

> **theorem**
For each fixed $k\geqslant2$, there exists a deterministic algorithm that,
given a $k$-CNF $F$ on $n\geqslant20$ declared variables with $m$ clauses,
computes $\\\#F$ as defined in in
$$(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$$
bit operations and $(n+m)^{O_k(1)}$ bits of space.
For each fixed $D>0$, its running time on inputs with $m\leqslant Dn$ is
$$(n+m)^{O_{k,D}(1)}2^{O_{k,D}(n/\sqrt{\log n})}.$$ [S2:73–85]

The technique overview [S2:541–548] summarizes the three-stage argument
and notes that taking $k=3$ already refutes ETH. The bounded-occurrence
algorithm counts in $n^{O(1)}2^{O(n(\log\log n)^2/\sqrt{\log n})}$
time; the sharper $2^{O_k(n\log\log n/\sqrt{\log n})}$ bound for the
full theorem comes from a Boolean tensor-contraction argument in the
appendices. The tensor-contraction theorem is the workhorse:

> **theorem**
Fix positive constants $C,A,b$. Let $s\geqslant2$ be an integer, and let
$\mathcal L$ be the total length of the graph and tensor descriptions
of a bipartite tensor network with at most $Cs$ edges and maximum
degree at most $\lceil s^{9/10}\rceil$. Suppose that the number of
vertices is bounded by a fixed polynomial in $s$, and that the entries
belong to
$$\mathcal B_{P_0,\ell}
   =(\mathbb Z/2^{P_0}\mathbb Z)[V]/(V^\ell),
 \qquad 1\leqslant P_0,\ell\leqslant Cs.$$
Suppose, uniformly for every vertex and Boolean choice of its ports,
that its entry can be computed from the description in time
$(s+\mathcal L)^b2^{A s^{9/10}}$ and space $(s+\mathcal L)^b$.
Then the contraction can be computed deterministically in
$$(s+\mathcal L)^{O(1)}
  2^{O(s/\sqrt{\log s})}$$
bit operations and $(s+\mathcal L)^{O(1)}$ bits of space. Constants
depend only on the fixed bounds in the hypotheses. In particular,
$\ell=1$ is permitted. [S4:26–49]

It computes the contraction of a Boolean tensor network with $s$ edges
in $2^{O(s/\sqrt{\log s})}$ time. The fixed-density case has
$s=O_k(n)$ edges, giving $2^{O_k(n/\sqrt{\log n})}$.

Two consequences stand out. The graph-counting corollary [S2:151–157]
gives subexponential algorithms for counting independent sets,
$q$-colorings, and perfect matchings:

> **corollary**
On simple graphs with $v$ vertices and $e$ edges, the number of
independent sets and, for each fixed $q\geqslant2$, the number of proper
$q$-colorings can be computed deterministically in $2^{o(v)}$ time
and $\mathrm{poly}_q(v,e)$ space. The number of perfect matchings can be
computed deterministically in $2^{o(v+e)}$ time and $\mathrm{poly}(v,e)$ space. [S2:151–157]

The circuit lower bound [S2:183–191] is the first superlinear circuit
lower bound for a language in $\mathsf{E}^{\mathsf{NP}}$:

> **corollary**
Let $C_L(n)$ be the minimum number of noninput gates in a circuit
computing $L$ on $\{0,1\}^n$, allowing arbitrary Boolean gates of
fan-in at most two and unrestricted fan-out. There exist a language
$L\in\mathrm E^{\mathrm{NP}}$ and a constant $c>0$ such that
$$C_L(n)>c\,n\sqrt{\log n}\qquad\text{for infinitely many }n.$$ [S2:183–191]

The proof [S3] combines Williams's witness-circuit argument with the
local reduction of Jahanjou–Miles–Viola: a subexponential SAT solver
contradicts a nondeterministic time hierarchy.

## History of the conjecture

Prior (my training data, not repo text): ETH was proposed by Impagliazzo
and Paturi in 2001, alongside SETH. The best known upper bounds at the
time were the PPSZ algorithm (randomized $O(1.308^n)$ for 3-SAT) and
Schöning's local search. The bounded-occurrence reduction and
polynomial interpolation are standard tools in algebraic complexity;
what is new here is the low-degree replacement construction that makes
group separation work with subexponential cost.

The manuscript's related-work section (lines 197–459) surveys the
landscape. It notes that the deterministic algorithm refutes not just
ETH but SETH, Gap-ETH, and NSETH "Theorem refutes ETH, SETH, Gap-ETH, and NSETH.
Indeed, testing whether the exact count is positive or zero decides
both satisfiability and unsatisfiability in deterministic
$2^{o(n)}(n+m)^{O_k(1)}$ time for every fixed $k$; deciding
satisfiability also solves the Gap-ETH promise problem. [S2:289–293]" The
randomized versions of ETH and SETH are also refuted. The result does
not conflict with unconditional exponential lower bounds for restricted
proof systems such as regular resolution. In 2016, Ryan Williams
refuted the Merlin–Arthur version of SETH by giving a protocol that
certifies $k$-CNF unsatisfiability in $2^{n/2}\mathrm{poly}(n,m)$ time.

## Consequences

**ETH, SETH, Gap-ETH, and NSETH are all refuted.** The decisive
observation is that testing whether the count is positive decides
satisfiability, and testing whether it is zero decides unsatisfiability,
both in deterministic $2^{o(n)}(n+m)^{O_k(1)}$ time [S2:289–293].

**Subexponential counting for graph problems.** Independent sets,
$q$-colorings, and perfect matchings are countable in $2^{o(v)}$ time
on simple graphs [S2:151–157]. The proof is a counting-preserving
reduction to a $k$-CNF with $O(v+e)$ clauses.

**First superlinear circuit lower bound for $\mathsf{E}^{\mathsf{NP}}$.**
There exists a language in $\mathsf{E}^{\mathsf{NP}}$ with
$C_L(n)>cn\sqrt{\log n}$ gates for infinitely many $n$ [S2:183–191].
The argument uses only the decision version of the 3-SAT algorithm.

**Inversion of constant-locality Boolean maps.** Given a Boolean map
whose output bits each depend on at most $d$ input bits, the preimage
set can be counted and a preimage found in
$(n+m)^{O_d(1)}2^{O_d(\rho(n))}$ time [S2:4284–4292]. This applies to
constant-locality versions of Goldreich's candidate one-way functions.

## Section skeleton

The manuscript is a single main file with three input appendices, no
`build/sections/` directory, and an inline `thebibliography` (no
`.bib` file).

**Main file** [S2], 4,829 lines: Introduction (line 45) with Related
work (197) covering SAT algorithms, exact counting, fine-grained
implications, algebraic prior work, and sparsification; Notation (500);
Technique overview (540) with subsubsections from the bounded-occurrence
setting through the low-degree replacement construction and the general
$\\#k$-SAT reduction via sparse polynomial equations; then the three
appendices and the bibliography (line 4329).

**Appendices** (input at lines 4269–4327): `quantitative-circuits.tex`
[S3] (71 lines, the circuit lower bound proof),
`quantitative-reduction.tex` [S4:26–49] (369 lines, the sharper bound via
tensor contraction), `quantitative-contraction.tex` [S5] (619 lines,
the contraction theorem proof).

No `verification/` bundle ships with this manuscript.

## Comparison with the formalized statement

The scope note [S7:9] states what Lean proves: a deterministic machine
exactly counts satisfying assignments of a canonically encoded $k$-CNF
in time $(L+1)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$, where
$L$ is the encoding's bit length. The manuscript's bound is
$2^{O_k(n\log\log n/\sqrt{\log n})}$; the Lean bound carries an extra
factor of $\log\log n$ in the exponent.

The comparator stub [S8:194–218] states the target and ends in
`sorry`:

```lean
theorem exact_count_and_sat (k : ℕ) (hk : 2 ≤ k) :
    ∃ (machine : Computation.PrimitiveMachine)
      (countTape answerTape : Fin machine.tapeCount)
      (C A S : ℝ) (d e : ℕ),
      0 < C ∧ 0 < A ∧ 0 < S ∧ 0 < d ∧ 0 < e ∧
      ∀ (n : ℕ) (F : SAT.CNF (Fin n)), SAT.WidthAtMost k F →
        ∃ (time : ℕ) (final : LocatedCfg machine),
          Computation.Trace (locatedStep machine) time
            (locatedInit machine (Encoding.encodeCNF F)) final ∧
          final.config.tapes countTape =
            Turing.Tape.mk₁ ((countWord (SAT.count F)).map some) ∧
          final.config.tapes answerTape =
            Turing.Tape.mk₁ [some (decide (0 < SAT.count F))] ∧
          final.config.state = Sum.inl (decide (0 < SAT.count F)) ∧
          BinaryArithmetic.toNat (countWord (SAT.count F)) = SAT.count F ∧
          (countWord (SAT.count F)).length ≤ n + 1 ∧
          (time : ℝ) ≤ OAI.Algorithms.SubexponentialSAT.SqrtLog.Statement.runtimeBound C A d
            (Encoding.formulaBitLength F) n ∧
          ∀ (prefixSteps : ℕ) (intermediate : LocatedCfg machine),
            prefixSteps ≤ time →
            Computation.Trace (locatedStep machine) prefixSteps
              (locatedInit machine (Encoding.encodeCNF F)) intermediate →
            (visitedSpace intermediate : ℝ) ≤
              S * ((Encoding.formulaBitLength F : ℝ) + 1) ^ e := by
  sorry
```
[S8:194–218]

The proved version [S9:74–97] has the identical statement, with the
proof delegating to a `compiled_exact_count_and_sat` helper:

```lean
theorem exact_count_and_sat (k : ℕ) (hk : 2 ≤ k) :
    ∃ (machine : Computation.PrimitiveMachine)
      (countTape answerTape : Fin machine.tapeCount)
      (C A S : ℝ) (d e : ℕ),
      0 < C ∧ 0 < A ∧ 0 < S ∧ 0 < d ∧ 0 < e ∧
      ∀ (n : ℕ) (F : SAT.CNF (Fin n)), SAT.WidthAtMost k F →
        ∃ (time : ℕ) (final : LocatedCfg machine),
          Computation.Trace (locatedStep machine) time
            (locatedInit machine (Encoding.encodeCNF F)) final ∧
          final.config.tapes countTape =
            Turing.Tape.mk₁ ((countWord (SAT.count F)).map some) ∧
          final.config.tapes answerTape =
            Turing.Tape.mk₁ [some (decide (0 < SAT.count F))] ∧
          final.config.state = Sum.inl (decide (0 < SAT.count F)) ∧
          BinaryArithmetic.toNat (countWord (SAT.count F)) = SAT.count F ∧
          (countWord (SAT.count F)).length ≤ n + 1 ∧
          (time : ℝ) ≤ OAI.Algorithms.SubexponentialSAT.SqrtLog.Statement.runtimeBound C A d
            (Encoding.formulaBitLength F) n ∧
          ∀ (prefixSteps : ℕ) (intermediate : LocatedCfg machine),
            prefixSteps ≤ time →
            Computation.Trace (locatedStep machine) prefixSteps
              (locatedInit machine (Encoding.encodeCNF F)) intermediate →
            (visitedSpace intermediate : ℝ) ≤
              S * ((Encoding.formulaBitLength F : ℝ) + 1) ^ e := by
```
[S9:74–97]

The gap is the $(\log\log n)$ vs $(\log\log n)^2$ factor in the
exponent. Both are subexponential, so the formalization proves the
headline conclusion (ETH is false) even though it does not match the
manuscript's exponent. The scope note [S7:11] confirms the gap
explicitly: "the October 25 manuscript gives the sharper time bound
$(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$."

## Coverage

T3: one manuscript, one scope note, one comparator challenge, one
`main_results` entry. The ledger reads `paps 1`, `paps_form 1`,
`mainres 1`, `scope_note 1`, `chal 1`, `verification 0`, `trace`
empty. The family ships a four-file LaTeX manuscript (main file plus
three appendices), a compiled `paper.pdf` [S6], and a `README.md`
 "**Date:** October 25, 2026 [S10:5]". No `verification/` bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 378 at line 9163) |
| S2 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex) | 4829 | Main file: abstract, theorems, technique overview, related work |
| S3 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-circuits.tex`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-circuits.tex) | 71 | Circuit lower bound proof |
| S4 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex) | 369 | Sharper bound via Boolean tensor contraction |
| S5 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex) | 619 | Contraction theorem proof |
| S6 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) | 25150 | Compiled manuscript |
| S7 | [`lean/docs/378.md`](../../../lean/docs/378.md) | 17 | Scope note |
| S8 | [`lean/ComparatorChallenges/SubexponentialSAT.lean`](../../../lean/ComparatorChallenges/SubexponentialSAT.lean) | 220 | Challenge stub |
| S9 | [`lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean`](../../../lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean) | 201 | Proved version in the Lean tree |
| S10 | [`preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/README.md`](../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/README.md) | 17 | Release date |
| S11 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 378 at line 363) |

## Bibliography

- Mikko Koivisto. _Optimal 2-Constraint Satisfaction via Sum–Product Algorithms_. Information Processing Letters **98**(1), 2006, 24–28.
- Ioannis Koutis and Ryan Williams. _Algebraic Fingerprints for Faster Algorithms_. Communications of the ACM **59**(1), 2016, 98–105.
- Craig A. Tovey. _A Simplified NP-Complete Satisfiability Problem_. Discrete Applied Mathematics **8**(1), 1984, 85–89.
- Erwin H. Bareiss. _Sylvester's Identity and Multistep Integer-Preserving Gaussian Elimination_. Mathematics of Computation **22**(103), 1968, 565–578.
- Noga Alon and Yuval Roichman. _Random Cayley Graphs and Expanders_. Random Structures & Algorithms **5**(2), 1994, 271–284.
- Timon Hertli. _3-SAT Faster and Simpler—Unique-SAT Bounds for PPSZ Hold in General_. SIAM Journal on Computing **43**(2), 2014, 718–729. Conference version in FOCS 2011.
- Russell Impagliazzo and Ramamohan Paturi. _On the Complexity of $k$-SAT_. Journal of Computer and System Sciences **62**(2), 2001, 367–375.
- Prabhakar Raghavan. _Probabilistic Construction of Deterministic Algorithms: Approximating Packing Integer Programs_. Journal of Computer and System Sciences **37**(2), 1988, 130–143.
- Ryan Williams. _A New Algorithm for Optimal 2-Constraint Satisfaction and Its Implications_. Theoretical Computer Science **348**(2–3), 2005, 357–365.
- Zeev Dvir and Allen Liu. _Fourier and Circulant Matrices are Not Rigid_. Theory of Computing **16**(20), 2020, 1–48.
- Arturs Backurs and Piotr Indyk. _Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false)_. SIAM Journal on Computing **47**(3), 2018, 1087–1097. Conference version in STOC 2015.
- Leslie G. Valiant. _The Complexity of Enumeration and Reliability Problems_. SIAM Journal on Computing **8**(3), 1979, 410–421.
- Ryan Williams. _Improving Exhaustive Search Implies Superpolynomial Lower Bounds_. SIAM Journal on Computing **42**(3), 2013, 1218–1244. Conference version in STOC 2010. The numbering of Lemma 3.2 and Theorem 6.1 follows the author's full version.
- Stanislav Žák. _A Turing Machine Time Hierarchy_. Theoretical Computer Science **26**(3), 1983, 327–333.
- Richard Beigel and Jun Tarui. _On ACC_. Computational Complexity **4**(4), 1994, 350–366.
- Joseph Naor and Moni Naor. _Small-Bias Probability Spaces: Efficient Constructions and Applications_. SIAM Journal on Computing **22**(4), 1993, 838–856.
- David Woodruff and Sergey Yekhanin. _A Geometric Approach to Information-Theoretic Private Information Retrieval_. SIAM Journal on Computing **37**(4), 2007, 1046–1056.
- R. Michael Tanner. _A Recursive Approach to Low Complexity Codes_. IEEE Transactions on Information Theory **27**(5), 1981, 533–547.
- Michael Sipser and Daniel A. Spielman. _Expander Codes_. IEEE Transactions on Information Theory **42**(6), 1996, 1710–1722.
- Leslie G. Valiant. _Graph-Theoretic Arguments in Low-Level Complexity_. Mathematical Foundations of Computer Science 1977, Lecture Notes in Computer Science **53**, 1977, 162–176.
- Virginia Vassilevska Williams. _On Some Fine-Grained Questions in Algorithms and Complexity_. Proceedings of the International Congress of Mathematicians (ICM 2018), World Scientific, 2019, 3447–3487.
- Radu Curticapean. _Block Interpolation: A Framework for Tight Exponential-Time Counting Complexity_. Information and Computation **261**, Part 2, 2018, 265–280. Conference version in ICALP 2015.
- Dominik Scheder. _PPSZ is better than you think_. TheoretiCS **3**, Article 5, 2024, 1–37.
- Dániel Marx. _Can You Beat Treewidth?_ Theory of Computing **6**, 2010, 85–112.
- Nikhil Vyas and Ryan Williams. _On Super Strong ETH_. Journal of Artificial Intelligence Research **70**, 2021, 473–495.
- Amir Abboud, Karl Bringmann, Danny Hermelin, and Dvir Shabtay. _SETH-Based Lower Bounds for Subset Sum and Bicriteria Path_. 30th ACM–SIAM Symposium on Discrete Algorithms, 2019, 41–57.
- Josh Alman, Yunfeng Guan, and Ashwin Padaki. _Smaller Low-Depth Circuits for Kronecker Powers_. 34th ACM–SIAM Symposium on Discrete Algorithms, 2023, 4159–4187.
- Timothy M. Chan and R. Ryan Williams. _Deterministic APSP, Orthogonal Vectors, and More: Quickly Derandomizing Razborov–Smolensky_. ACM Transactions on Algorithms **17**(1), Article 2, 2021, 1–14. Authors' manuscript, Theorems 1.6 and 2.5.
- Tao Jiang and Shaowei Cai. _A Better Analysis For PPSZ For 3-SAT_. arXiv:2607.10697, 2026.
- Thore Husfeldt. _Invitation to Algorithmic Uses of Inclusion–Exclusion_. 38th International Colloquium on Automata, Languages, and Programming, Part II, Lecture Notes in Computer Science **6756**, 2011, 42–59.
- Pasin Manurangsi and Prasad Raghavendra. _A Birthday Repetition Theorem and Complexity of Approximating Dense CSPs_. 44th International Colloquium on Automata, Languages, and Programming, LIPIcs **80**, 2017, 78:1–78:15.
- Vishwas Bhargava, Sumanta Ghosh, Mrinal Kumar, and Chandra Kanta Mohapatra. _Fast, Algebraic Multivariate Multipoint Evaluation in Small Characteristic and Applications_. Journal of the ACM **70**(6), 2023, 42:1–42:46. Conference version in STOC 2022.
- Andreas Björklund, Petteri Kaski, and Ryan Williams. _Generalized Kakeya Sets for Polynomial Evaluation and Faster Computation of Fermionants_. Algorithmica **81**, 2019, 4010–4028. Conference version in IPEC 2017.
- Chris Calabro, Russell Impagliazzo, and Ramamohan Paturi. _A Duality between Clause Width and Clause Density for SAT_. 21st IEEE Conference on Computational Complexity, 2006, 252–260.
- Marco L. Carmosino, Jiawei Gao, Russell Impagliazzo, Ivan Mihajlin, Ramamohan Paturi, and Stefan Schneider. _Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility_. 7th Innovations in Theoretical Computer Science Conference, 2016, 261–270.
- Sixue Liu. _Chain, Generalization of Covering Code, and Deterministic Algorithm for $k$-SAT_. 45th International Colloquium on Automata, Languages, and Programming, LIPIcs **107**, 2018, 88:1–88:13.
- Parinya Chalermsook, Marek Cygan, Guy Kortsarz, Bundit Laekhanukit, Pasin Manurangsi, Danupon Nanongkai, and Luca Trevisan. _From Gap-Exponential Time Hypothesis to Fixed Parameter Tractable Inapproximability: Clique, Dominating Set, and More_. SIAM Journal on Computing **49**(4), 2020, 772–810. Conference version in FOCS 2017.
- Jianer Chen, Xiuzhen Huang, Iyad A. Kanj, and Ge Xia. _Strong Computational Lower Bounds via Parameterized Complexity_. Journal of Computer and System Sciences **72**(8), 2006, 1346–1367.
- Zongchen Chen, Aditya Lonkar, Chunyang Wang, Kuan Yang, and Yitong Yin. _Counting Random $k$-SAT near the Satisfiability Threshold_. 57th ACM Symposium on Theory of Computing, 2025, 867–878. Theorem 1.2 is numbered as in the authors' full version.
- Irit Dinur. _Mildly Exponential Reduction from Gap 3SAT to Polynomial-Gap Label-Cover_. Electronic Colloquium on Computational Complexity, Report TR16-128, 2016.
- Oded Goldreich. _Candidate One-Way Functions Based on Expander Graphs_. Electronic Colloquium on Computational Complexity, Report TR00-090, 2000.
- Richard Ryan Williams. _Strong ETH Breaks With Merlin and Arthur: Short Non-Interactive Proofs of Batch Evaluation_. 31st Conference on Computational Complexity, LIPIcs **50**, 2016, 2:1–2:17.
- Magnus Wahlström. _A Tighter Bound for Counting Max-Weight Solutions to 2SAT Instances_. 3rd International Workshop on Parameterized and Exact Computation, Lecture Notes in Computer Science **5018**, 2008, 202–213.
- Josh Alman and Ryan Williams. _Probabilistic Rank and Matrix Rigidity_. 49th ACM Symposium on Theory of Computing, 2017, 641–652.
- Chris Beck and Russell Impagliazzo. _Strong ETH Holds for Regular Resolution_. 45th ACM Symposium on Theory of Computing, 2013, 487–494.
- Stephen A. Cook. _The Complexity of Theorem-Proving Procedures_. 3rd ACM Symposium on Theory of Computing, 1971, 151–158.
- Ray Li. _Settling SETH vs. Approximate Sparse Directed Unweighted Diameter (up to (NU)NSETH)_. 53rd ACM Symposium on Theory of Computing, 2021, 1684–1696.
- Prasad Raghavendra. _Optimal Algorithms and Inapproximability Results for Every CSP?_ 40th ACM Symposium on Theory of Computing, 2008, 245–254.
- Liam Roditty and Virginia Vassilevska Williams. _Fast Approximation Algorithms for the Diameter and Radius of Sparse Graphs_. 45th ACM Symposium on Theory of Computing, 2013, 515–524.
- Marek Cygan, Holger Dell, Daniel Lokshtanov, Dániel Marx, Jesper Nederlof, Yoshio Okamoto, Ramamohan Paturi, Saket Saurabh, and Magnus Wahlström. _On Problems as Hard as CNF-SAT_. ACM Transactions on Algorithms **12**(3), Article 41, 2016, 1–24.
- Holger Dell, Thore Husfeldt, Dániel Marx, Nina Taslaman, and Martin Wahlén. _Exponential Time Complexity of the Permanent and the Tutte Polynomial_. ACM Transactions on Algorithms **10**(4), Article 21, 2014, 1–32.
- Chris Calabro. _The Exponential Complexity of Satisfiability Problems_. Ph.D. dissertation, University of California, San Diego, 2009. Chapter 5.
- Joachim von zur Gathen and Jürgen Gerhard. _Modern Computer Algebra_. 3rd edition, Cambridge University Press, 2013.
- Thomas Dueholm Hansen, Haim Kaplan, Or Zamir, and Uri Zwick. _Faster $k$-SAT Algorithms Using Biased-PPSZ_. 51st ACM Symposium on Theory of Computing, 2019, 578–589.
- Russell Impagliazzo, William Matthews, and Ramamohan Paturi. _A Satisfiability Algorithm for $AC^0$_. 23rd ACM–SIAM Symposium on Discrete Algorithms, 2012, 961–972. Publisher's version.
- Russell Impagliazzo, Ramamohan Paturi, and Francis Zane. _Which Problems Have Strongly Exponential Complexity?_ Journal of Computer and System Sciences **63**(4), 2001, 512–530.
- Konstantin Kutzkov. _Complementary Branching for #SAT: Bounded-Degree Bounds and Faster #3-SAT_. 35th International Joint Conference on Artificial Intelligence, 2026, 2282–2290.
- Hamid Jahanjou, Eric Miles, and Emanuele Viola. _Local Reductions_. Electronic Colloquium on Computational Complexity, Report TR13-099, revision 2, 2013. Conference version in ICALP 2015, 749–760.
- Mark R. Jerrum, Leslie G. Valiant, and Vijay V. Vazirani. _Random Generation of Combinatorial Structures from a Uniform Distribution_. Theoretical Computer Science **43**(2–3), 1986, 169–188.
- Swastik Kopparty, Shubhangi Saraf, and Sergey Yekhanin. _High-Rate Codes with Sublinear-Time Decoding_. Journal of the ACM **61**(5), 2014, 28:1–28:20.
- Daniel Lokshtanov, Dániel Marx, and Saket Saurabh. _Known Algorithms on Graphs of Bounded Treewidth Are Probably Optimal_. ACM Transactions on Algorithms **14**(2), Article 13, 2018, 1–30. Conference version in SODA 2011.
- OpenAI, _The Unique Games Theorem_, OpenAI Math Release preprint OAI:The-Unique-Games-Theorem-September-23-2026, 2026.
- Oded Goldreich. _P, NP, and NP-Completeness: The Basics of Computational Complexity_. Author's draft, June 14, 2008, Proposition 4.7. The Cambridge University Press edition appeared in 2010.
- Ramamohan Paturi, Pavel Pudlák, Michael E. Saks, and Francis Zane. _An Improved Exponential-Time Algorithm for $k$-SAT_. Journal of the ACM **52**(3), 2005, 337–364. Conference version in FOCS 1998.
- Alexander D. Scott and Gregory B. Sorkin. _Polynomial Constraint Satisfaction Problems, Graph Bisection, and the Ising Partition Function_. ACM Transactions on Algorithms **5**(4), 2009, 45:1–45:27.
- Amir Abboud and Virginia Vassilevska Williams. _Popular Conjectures Imply Strong Lower Bounds for Dynamic Problems_. 55th IEEE Symposium on Foundations of Computer Science, 2014, 434–443.
- Josh Alman and Ryan Williams. _Probabilistic Polynomials and Hamming Nearest Neighbors_. 56th IEEE Symposium on Foundations of Computer Science, 2015, 136–150.
- Arturs Backurs and Piotr Indyk. _Which Regular Expression Patterns Are Hard to Match?_ 57th IEEE Symposium on Foundations of Computer Science, 2016, 457–466.
- Karl Bringmann. _Why Walking the Dog Takes Time: Fréchet Distance Has No Strongly Subquadratic Algorithms Unless SETH Fails_. 55th IEEE Symposium on Foundations of Computer Science, 2014, 661–670.
- Karl Bringmann and Marvin Künnemann. _Quadratic Conditional Lower Bounds for String Problems and Dynamic Time Warping_. 56th IEEE Symposium on Foundations of Computer Science, 2015, 79–97.
- Uwe Schöning. _A Probabilistic Algorithm for $k$-SAT and Constraint Satisfaction Problems_. 40th IEEE Symposium on Foundations of Computer Science, 1999, 410–414.
- Richard Ryan Williams. _The Polynomial Method in Circuit Complexity Applied to Algorithm Design (Invited Talk)_. 34th International Conference on Foundation of Software Technology and Theoretical Computer Science, LIPIcs **29**, 2014, 47–60.
- Bart Selman, Henry A. Kautz, and Bram Cohen. _Noise Strategies for Improving Local Search_. 12th National Conference on Artificial Intelligence, 1994, 337–343.
- Boaz Barak. _Introduction to Theoretical Computer Science_. Online textbook, 2023. Chapter 15, Lemmas 15.9–15.10. Archived 2023 edition (v0.95).
- Andreas Björklund. _Below All Subsets for Some Permutational Counting Problems_. 15th Scandinavian Symposium and Workshops on Algorithm Theory, LIPIcs **53**, 2016, 17:1–17:11.
