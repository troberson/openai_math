[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 103](../index/theoretical-computer-science/103-derandomization-of-logarithmic-space-l-rl-bpl.md)

# 103 — Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$

[Index page](../index/theoretical-computer-science/103-derandomization-of-logarithmic-space-l-rl-bpl.md)

## Original CONTENTS.md summary

[S1:2554] (family entry):

> **103. Exact derandomization of logarithmic space: $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$.** Proves $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$, resolving derandomization for bounded-error logarithmic-space computation. An effective compiler converts each randomized polynomial-time logarithmic-space machine deciding a language with one-sided or two-sided error into a deterministic logarithmic-space decider with explicit polynomial running-time bounds. ([Lean](../../lean/docs/103.md))

[S1:2561] (the manuscript entry under that family):

> [Exact derandomization of logarithmic space: L = RL = BPL](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf)

[S3:11–14] carries the manuscript's own abstract, and [S2:284] carries the
[S1:2554] text, so the release blurb and the `\resultentry` agree to the word.

## Undergraduate summary

A **logarithmic-space machine** can read its whole input, but it can only keep
a number of notes proportional to the *length of the input in bits* — for an
input of length $n$ that is $O(\log n)$ bits, enough to remember a handful of
positions, not a working copy of the input. Add a coin: the machine may flip
fair random bits, and on some inputs it is allowed to get the occasional one
wrong, so long as the answer is right with probability at least $2/3$ when the
right answer is "yes" and at most $1/3$ when it is "no". The
classes $\mathsf L$, $\mathsf{RL}$ and $\mathsf{BPL}$ are the languages such machines decide,
for the deterministic, one-sided-error, and two-sided-error cases
respectively. The three classes sit in the order
$\mathsf L \subseteq \mathsf{RL} \subseteq \mathsf{BPL}$ for free: a deterministic machine
ignores its coins, and running an $\mathsf{RL}$ machine twice and accepting if
either run accepts turns one-sided error into two-sided error without using
more space [S6:279–290].

The open question for decades was whether the inclusions are equalities.
The paper answers yes, and it answers the strong form: "The class $\mathsf L$ consists of languages decidable by deterministic [S4:19–21]"
([S4:19–21]) defines $\mathsf L$, and the main theorem is the
equality "**theorem**
 [S4:28–30]" () — in this machine model, fresh random
bits do not let a logarithmic-space machine decide anything a
deterministic logarithmic-space machine cannot.

The route is to **estimate the acceptance probability**. The proof never
tries to simulate the random coins; instead it builds a finite family of
deterministic estimates of the probability the machine accepts, indexed by
short descriptions, and shows that more than three quarters of the estimates
are accurate. Enumerating them and taking the median gives one accurate
deterministic answer, and comparing that answer with $1/2$ decides the
language [S4:34–38]. The estimate is a dyadic rational — a fraction whose
denominator is a power of two — produced in logarithmic space and
polynomial time, with an explicit error bound. That is the
"The proof approximates arbitrary acceptance probabilities. This gives [S4:34–35]" idea () the rest of the paper implements.

## Graduate summary

**Theorem 1** ([S4:28–32], `thm:main`). In the model of finite-control
machines with an endmarked read-only input, finitely many work tapes, and
fresh fair bits, with space counting every simultaneously live counter and
register in bits and the randomized classes using polynomial time,
$\mathsf L=\mathsf{RL}=\mathsf{BPL}$. Here $\mathsf{RL}$ accepts a no-instance with probability zero
and a yes-instance with probability at least $1/2$; $\mathsf{BPL}$ uses $2/3$ and
$1/3$ [S4:19–26].

The proof has two stages. The first stage builds an estimator
([S4:40–49], `thm:probability`): there is a uniform deterministic
algorithm which, on input $(x, 1^q)$, outputs a dyadic rational
$a2^{-(q+2)}$ satisfying
$|a2^{-(q+2)} - p_{\mathcal M}(x)| \le 2^{-q}$,
using $O(\log(n+2)+q)$ work space and
$(n+2)^{O(1)} 2^{O(q)}$ time. The second stage
([S6:18–27], `thm:fixed-precision`) specialises the unary
precision parameter $q$ to a fixed $d \ge 1$ and reads off the constant
$(n+2)^{-d}$ accuracy, $O(\log(n+2))$ space, and polynomial time, which is
enough for the bounded-error threshold.

The estimator is a **configuration-graph matrix inverse**. The
configuration-reduction lemma
([S5:18–33], `lem:model-reduction`) specifies, uniformly in logarithmic
space, a polynomial-size vertex set $V_0$, a strictly forward substochastic
matrix $S$, an accepting-configuration vector $e \in \{0,1\}^{V_0}$, and a
start $x_0$, such that
"$\item The coordinate$p_0(x_0)$is the acceptance probability of [S5:31–32]$"
([S5:31–32]) — the matrix model that the rest of the construction feeds on.
The hierarchy of [S4:197–250] replaces $S$ by a sequence of
correction-and-copy steps on enlarged vertex sets $V_l$, with a reward
$W_l \in [0,1]^{V_l}$ that converges to $p_0(x_0)$
at rate $2^{-(H-1)l}$; a fixed number $L = O(B)$ of stages gives
inverse-polynomial accuracy. The
finite random environment $\sigma$ then evaluates the final reward $W_L$ in
an integrated norm, the moment estimate
`thm:fp-estimators` controls the $8$th absolute moment of
the estimator's error over the retained environments, and the
conditioning lemma `lem:final-majority`
([S6:148]) spends a factor $N = 2^{C_NB}$ to pass
from the integrated bound to one specified start. The median of the
retained values then carries the $3\Delta/8$ error bound, and
[S6:279–290] closes the class equality:

> "$2/3-1/8=13/24$ on a yes input. Comparing this answer with $1/2$ [S6:286–287]"

**Derived consequences.** The promise corollary
([S6:307–311], `cor:promise-bpl`) states "$$\mathsf{PromiseBPL}=\mathsf{PromiseL}$. [S6:311]$",
so the same argument separates bounded-error promise problems in
logarithmic space. The variable-precision theorem
([S6:325–360]) handles an arbitrary requested accuracy $q$ by
padding: the input $(x, 1^q)$ is simulated on a longer virtual string,
the precision parameter $q$ moves into the input, and the running time
becomes $(n+2)^{O(1)} 2^{O(q)}$. The certified-search corollary
([S6:396–404], `cor:certified-search`) constructs an accepting
computation of $\mathcal M$ whenever
$p_{\mathcal M}(x) \ge (n+2)^{-c}$,
streaming the configurations through the first halting state; it is
the mechanism for turning the probability estimate into a witness.
The space bound is a telescoping
recursion (): "$The controller assigns each call a decreasing recursion allowance $w$, [S4:246–247]$"
and the digits requested at each recursive level telescope along
the call chain, so the total live work is $O(B)$
rather than $O(B)$ per level.

**Formalization status.** The release formalises this family at tier T3
with a scope note [S10] and a comparator stub [S11]. The scope note states
what the formalization does and, in one explicit exclusion, what it does
not do: it proves the class equality for binary languages in the explicit
Turing-machine model with logarithmic workspace, and it does **not**
separately state the paper's explicit compiler and its numerical
running-time bounds. The selected statement is the equality
$\Lclass=\RL=\BPL$ itself, and the comparator stub
[S11] carries the `sorry` for exactly that statement. The
certified-search corollary, the promise corollary, and the
variable-precision theorem of [S6:325–360] are not separately formalized.
The ledger row records the tier and the counts: `tier=T3`, `paps_form=1`,
`chal=1`, `mainres=1`, `scope_note=1`, `verification=0`, `trace=` [S12].

## History of the conjecture

The lineage runs from **Gill's** 1977 setup of time and tape measures for
probabilistic Turing machines [S4:74] through **Aleliunas, Karp, Lipton,
Lovász and Rackoff's** polynomial-time randomized walk for undirected
connectivity — which explicitly asked whether polynomial-time randomized
logarithmic space could be simulated in deterministic logarithmic space
[S4:76–78]. **Borodin, Cook and Pippenger** proved a quadratic-space
deterministic simulation for the unrestricted setting [S4:80].

The pseudorandom-generator line begins with **Ajtai, Komlós and
Szemerédi**'s small-space constructions [S4:91] and **Babai, Nisan and
Szegedy's** communication-based generators [S4:93]. **Nisan's** 1992
generator uses $O(S \log R)$ seed bits for a space-$S$ computation
reading $R$ random bits, giving
$O(\log^2 n)$ seed length in the
logarithmic-space case [S4:94–96]; his 1994 simultaneous simulation
achieves polynomial time and $O(\log^2 n)$ space with two-sided error
[S4:98–101]. **Nisan and Zuckerman** showed a space-$S$ computation
using $\mathrm{poly}(S)$ random bits can be simulated with
$O(S)$ random bits and $O(S)$ space [S4:102–104].

The space-containment line: **Saks and Zhou** reduced the deterministic
space for general bounded-error logarithmic-space computation to
$O(\log^{3/2} n)$ [S4:108]; **Cai, Chakaravarthy and van Melkebeek**
established a simultaneous time-space tradeoff
$n^{O(\log^{1/2-\alpha} n)}$ time with
$O(\log^{3/2+\alpha} n)$ space
for each fixed $0 \le \alpha \le 1/2$ [S4:112]. **Hoza** improved the
general space bound to
$O(\log^{3/2} n / \sqrt{\log\log n})$
and developed weighted pseudorandomness
[S4:117–122].

The structural line: **Nisan, Szemerédi and Wigderson**'s
$O(\log^{3/2} n)$ connectivity, improved to
$O(\log^{4/3} n)$ by **Armoni, Ta-Shma, Wigderson and Zhou**
[S4:139–141]; **Reingold's** logarithmic-space undirected-connectivity
algorithm [S4:143–144]; **Reingold, Trevisan and Vadhan's** oblivious
walks for Eulerian directed graphs [S4:145–147].
**Cheng and Hoza** proved that a uniformly logarithmic-space-enumerable
$1/2$-hitting-set family for all width-$n$, length-$n$ read-once branching
programs would yield $\mathsf L = \mathsf{BPL}$ [S4:158–161].

The recent line: **Chen, Cohen, Doron, Khaskelberg and Ta-Shma**'s
improved error reduction for weighted generators in the polynomial-width
regime [S4:168–170]; **Cheng and Wu**'s simultaneous polynomial-time and
polylogarithmic-space simulations for regular branching programs [S4:171];
**Pyne and Tell**'s survey of hardness-versus-randomness approaches [S4:179].

The effectivity line: **Pyne, Raz and Zhan** constructed a universal
deterministic estimator whose $O(S(n))$ space guarantee follows from
$\mathsf{prBPL} \subseteq \mathsf{SPACE}[O(S(n))]$
for space-constructible $S(n) \ge \log n$ [S4:183–185].
The compiler of [S4:187] uses a fixed separator established in
this paper and supplies explicit source-specific resource bounds —
its construction sits in this context of universal simulation, with
the source bounds supplied as part of the compiler input.

**Prior (my training data, not this repo).** $\mathsf L = \mathsf{RL} = \mathsf{BPL}$
is a central derandomization target in complexity theory. The one-sided
case $\mathsf L = \mathsf{RL}$ has been known since the AKSZ line and the bounded
randomness of **Chang** (for one-sided); the two-sided case is the harder
direction and is what this paper addresses. The pseudorandom-generator
route gives a small-space containment with a polynomially-iterated
seed-enumeration, but that route gives quasipolynomial time, not
polynomial time, in the general logarithmic-space case; the
acceptance-probability-estimation route this paper uses
(Ahmadinejad–Kelner–Murtagh–Peebles–Sidford–Vadhan,
Cohen–Doron–Sberlo–Ta-Shma) is the route that closes the gap to
polynomial time. I have not seen this result and cannot confirm
it independently; the release ships it as a proof, and the Lean
formalization records the class equality only.

## Consequences

- **The class equality.** $\mathsf L = \mathsf{RL} = \mathsf{BPL}$ in the
  explicit Turing-machine model with the stated space convention.
  The containment $\mathsf{BPL} \subseteq \mathsf L$ is proved directly from the
  $d = 3$ fixed-precision approximation and the threshold $1/2$
  [S6:279–290]. The reverse direction is the two free inclusions.
- **The promise version.** $\mathsf{PromiseBPL} = \mathsf{PromiseL}$
  [S6:307–311]. The same $d=3$ approximation and threshold separate
  the promise classes, and the approximating machine halts outside
  the promise as well, because the digit queries are total.
- **The variable-precision algorithm.** The unary precision parameter
  $q$ moves into the input via padding; the running time is
  $(n+2)^{O(1)} 2^{O(q)}$ and the space is
  $O(\log(n+2)+q)$ [S6:325–360]. A single algorithm serves every
  fixed inverse-polynomial accuracy.
- **The certified accepting computation.** Whenever
  $p_{\mathcal M}(x) \ge (n+2)^{-c}$, a deterministic
  logarithmic-space, polynomial-time transducer outputs an accepting
  computation of $\mathcal M$ [S6:396–404]. This is the witness
  mechanism: the estimation gives a greedy path through the
  configuration graph that reaches a terminal accepting state.
- **The effective compiler.** A terminating compiler that, given a
  source program and supplied polynomial-time and logarithmic-space
  bounds, produces a deterministic decider with explicit numerical
  space and time bounds. The paper's Section ~\ref{sec:compiler}
  specializes one fixed deterministic library to the source program
  [S4:40–42]. The scope note [S10] states that the formalization
  does **not** separately state this compiler.

**Prior (my training data, not this repo).** The consequence that matters
in the wider derandomization program is the first: the equality
$\mathsf L = \mathsf{BPL}$ closes a thirty-year gap in the space complexity
hierarchy. The certified-search corollary is the mechanism by which
the estimation produces a witness; the compiler is the effectivity
result that makes the simulation constructive. Both are
release-level claims read from the manuscript; the Lean
formalization records only the class equality.

## Section skeleton

The manuscript [S3] includes its sections in the order
[S3:16–28]: `introduction`, `model`, `environment`, `hierarchy`,
`atoms`, `averaging`, `estimation`, `compression`, `fingerprints`,
`arithmetic`, `implementation`, `conclusion`, `compiler`. The
conclusion [S6] carries the fixed-precision theorem
[S6:18–27], the class-equality proof [S6:279–290], the promise
corollary [S6:307–311], the variable-precision proof [S6:325–360],
and the certified-search corollary [S6:396–404]. The compiler
section is a separate application of the fixed-precision
approximation: one resource-capped universal interpreter yields a
fixed deterministic library, whose syntactic specialization supplies
explicit resource bounds for each source machine [S4:248–250].

## Coverage

The scope note [S10] states the formalization's scope and its one
explicit exclusion. It proves the class equality
$\mathsf L=\mathsf{RL}=\mathsf{BPL}$ for binary languages in the explicit
Turing-machine model with logarithmic workspace, and it does not
separately state the paper's explicit compiler or its numerical
running-time bounds. The comparator stub [S11] carries the
`sorry` for the equality statement. The variable-precision
theorem, the promise corollary, the certified-search corollary, and
the effectivity compiler of the manuscript are not separately
formalized. The ledger row `fam=103` records tier T3, one
formalized manuscript, one challenge, one `main_results` entry, one
scope note, and no verification bundle or reasoning trace [S12].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:2554] and its manuscript entry [S1:2561]. Quoted word-for-word; the release's inline code spans stay as backticked markdown |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 103 at [S2:284] |
| S3 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/main.tex`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/main.tex) | 34 | root (`\documentclass`); abstract at [S3:11–14]; the section include order [S3:16–28] |
| S4 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/introduction.tex`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/introduction.tex) | 366 | class definitions [S4:19–26]; the two theorems [S4:28–32], [S4:40–49]; proof strategy [S4:197–250]; historical context [S4:66–189] |
| S5 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/model.tex`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/model.tex) | 148 | configuration-reduction lemma [S5:18–33]; the matrix model [S5:11–16] |
| S6 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/conclusion.tex`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/sections/conclusion.tex) | 463 | fixed-precision theorem [S6:18–27]; the class-equality proof [S6:279–290]; the promise corollary [S6:307–311]; the variable-precision proof [S6:325–360]; the certified-search corollary [S6:396–404] |
| S7 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/references.bib`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/references.bib) | 425 | 39 `\bibitem`s; Nisan 1992 [S7:1], Saks–Zhou [S7:~110], Reingold [S7:~210], Pyne–Raz–Zhan [S7:~290] |
| S8 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/README.md`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/README.md) | 19 | title, author, date, bibtex citation stub |
| S9 | [`preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf`](../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf) | 28682 | the manuscript as shipped |
| S10 | [`lean/docs/103.md`](../../lean/docs/103.md) | 17 | scope note — the formalization's Scope and the comparator link |
| S11 | [`lean/ComparatorChallenges/LogspaceEquality.lean`](../../lean/ComparatorChallenges/LogspaceEquality.lean) | 142 | the comparator stub — the selected equality statement with its `sorry` |
| S12 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=103`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- Ahmadinejad, AmirMahdi, Kelner, Jonathan, Murtagh, Jack, Peebles, John, Sidford, Aaron, Vadhan, Salil, High-precision estimation of random walks in small space (2020)
- Ajtai, Miklós, Komlós, János, Szemerédi, Endre, Deterministic simulation in LOGSPACE (1987)
- Aleliunas, Romas, Karp, Richard M., Lipton, Richard J., Lovász, László, Rackoff, Charles, Random Walks, Universal Traversal Sequences, and the Complexity of Maze Problems (1979)
- Roy Armoni, Amnon Ta-Shma, Avi Wigderson, Shiyu Zhou, An $O(\log(n)^{4/3})$ space algorithm for $(s,t)$ connectivity in undirected graphs (2000)
- Avizienis, Algirdas, On a Flexible Implementation of Digital Computer Arithmetic (1963)
- Babai, László, Nisan, Noam, Szegedy, Márió, Multiparty protocols, pseudorandom generators for logspace, and time-space trade-offs (1992)
- Bekka, Bachir, de la Harpe, Pierre, Valette, Alain, Kazhdan's property (T) (2008)
- Borodin, Allan, Cook, Stephen, Pippenger, Nicholas, Parallel Computation for Well-Endowed Rings and Space-Bounded Probabilistic Machines (1983)
- Braverman, Mark, Cohen, Gil, Garg, Sumegha, Pseudorandom Pseudo-distributions with Near-Optimal Error for Read-Once Branching Programs (2020)
- Buhrman, Harry, Cleve, Richard, Koucký, Michal, Loff, Bruno, Speelman, Florian, Computing with a Full Memory: Catalytic Space (2014)
- Cai, Jin-Yi, Chakaravarthy, Venkatesan T., van Melkebeek, Dieter, Time-Space Tradeoff in Derandomizing Probabilistic Logspace (2006)
- Carter, J. Lawrence, Wegman, Mark N., Universal Classes of Hash Functions (1979)
- Chen, Ben, Cohen, Gil, Doron, Dean, Khaskelberg, Yuval, Ta-Shma, Amnon, Improved Error Reduction for Weighted PRGs (2026)
- Cheng, Kuan, Hoza, William M., Hitting Sets Give Two-Sided Derandomization of Small Space (2022)
- Cheng, Kuan, Wu, Ruiyang, SC Derandomization for Regular ROBPs and Models Beyond BPL (2026)
- Cohen, Gil, Doron, Dean, Renard, Oren, Sberlo, Ori, Ta-Shma, Amnon, Error Reduction for Weighted PRGs Against Read Once Branching Programs (2021)
- Cohen, Gil, Doron, Dean, Sberlo, Ori, Ta-Shma, Amnon, Approximating Iterated Multiplication of Stochastic Matrices in Small Space (2023)
- Cook, Stephen A., McKenzie, Pierre, Problems Complete for Deterministic Logarithmic Space (1987)
- Gill, John, Computational Complexity of Probabilistic Turing Machines (1977)
- Hoza, William M., Better pseudodistributions and derandomization for space-bounded computation (2021)
- Kassabov, Martin, Kazhdan constants for $\mathrm{SL}_n(\mathbb Z)$ (2005)
- Lange, Klaus-Jörn, McKenzie, Pierre, Tapp, Alain, Reversible space equals deterministic space (2000)
- Nisan, Noam, Pseudorandom generators for space-bounded computation (1992)
- Nisan, Noam, Zuckerman, David, Randomness is linear in space (1996)
- Nisan, Noam, $\mathrm{RL}\subseteq\mathrm{SC}$ (1994)
- Noam Nisan, Endre Szemerédi, Avi Wigderson, Undirected connectivity in $O(\log^{1.5} n)$ space (1992)
- Pyne, Edward, Tell, Roei, Using Hardness vs Randomness to Design Low-Space Algorithms (2026)
- Pyne, Edward, Raz, Ran, Zhan, Wei, Certified Hardness vs. Randomness for Log-Space (2023)
- Reingold, Omer, Undirected connectivity in log-space (2008)
- Reingold, Omer, Trevisan, Luca, Vadhan, Salil, Pseudorandom walks on regular digraphs and the RL vs. L problem (2006)
- Omer Reingold, Undirected ST-connectivity in log-space (2005)
- Riesz, Marcel, Sur les maxima des formes bilinéaires et sur les fonctionnelles linéaires (1927)
- Saks, Michael, Zhou, Shiyu, $\mathrm{BP}_{\mathrm H}\mathrm{SPACE}(S)\subseteq \mathrm{DSPACE}(S^{3/2})$ (1999)
- Savitch, Walter J., Relationships between nondeterministic and deterministic tape complexities (1970)
- Schwartz, Jacob T., Fast Probabilistic Algorithms for Verification of Polynomial Identities (1980)
- Shalom, Yehuda, Bounded generation and Kazhdan's property (T) (1999)
- Simon, Janos, On tape-bounded probabilistic Turing machine acceptors (1981)
- Stockmeyer, Larry J., Meyer, Albert R., Word Problems Requiring Exponential Time (Preliminary Report) (1973)
- Thorin, G. O., Convexity theorems generalizing those of M. Riesz and Hadamard with some applications (1948)
