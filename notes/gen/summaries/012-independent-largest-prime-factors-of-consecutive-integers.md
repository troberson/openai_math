[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 012](../index/number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md)

# 012 — Independent largest prime factors of consecutive integers

[Index page](../index/number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md)

## Original CONTENTS.md summary

The release blurb 

> **012. Independent largest prime factors of consecutive integers.** Resolves the Erdős–Pomerance joint Dickman conjecture: the logarithmic sizes of the largest prime factors of n and $`n+1`$ are asymptotically independent in ordinary natural density. In particular, the integers satisfying $`P^+(n)\lt P^+(n+1)`$ have density 1/2. [S1:300]

The manuscript abstract 

> Let $P^+(n)$ denote the largest prime factor of $n$. We prove that
$\log P^+(n)/\log n$ and $\log P^+(n+1)/\log n$ are asymptotically
independent in ordinary natural density, with Dickman marginals. This resolves the Erdős–Pomerance
joint Dickman conjecture positively and implies that the ordering
$P^+(n)<P^+(n+1)$ has natural density $1/2$. [S2:8–14]

## Undergraduate summary

Write $P^+(n)$ for the largest prime factor of $n$. A "rough" integer
is one whose largest prime factor is small relative to itself: $P^+(n)
\le n^a$ for some $0 < a < 1$ means every prime factor of $n$ is at
most $n^a$, so $n$ has no very large prime factor. The Dickman
function $\rho$ is the classical object that counts how rough the
integers are: the density of $n \le X$ with $P^+(n) \le n^a$ tends to
$\rho(1/a)$ as $X \to \infty$.

The Erdős–Pomerance conjecture asked whether, for two *consecutive*
integers, the roughness of $n$ and the roughness of $n+1$ behave as if
they were independent. This paper proves that they are: the joint
density of the pairs where both are rough is the product of the two
marginal densities. A clean consequence is that the ordering $P^+(n)
< P^+(n+1)$ holds for exactly half the integers, with the reverse
ordering holding for the other half.

The main statement 

> **theorem**
For every fixed $a,b\in(0,1)$,
$$\lim_{X\to\infty}\frac1X
 \\\#\{2\leq n\leq X:P^+(n)\leq n^a,
                         \ P^+(n+1)\leq n^b\}
 =\rho(1/a)\rho(1/b).$$
Here the limit is taken over all real $X$, with ordinary, unweighted
counting. [S3:19–29]

## Graduate summary

The theorem is a joint large-deviation / limit statement for the pair
$(P^+(n), P^+(n+1))$.

**Joint Dickman law.** 

> **theorem**
For every fixed $a,b\in(0,1)$,
$$\lim_{X\to\infty}\frac1X
 \\\#\{2\leq n\leq X:P^+(n)\leq n^a,
                         \ P^+(n+1)\leq n^b\}
 =\rho(1/a)\rho(1/b).$$
Here the limit is taken over all real $X$, with ordinary, unweighted
counting. [S3:19–29]

For every fixed $a,b \in (0,1)$ the two-dimensional density of the
event $\{P^+(n) \le n^a \text{ and } P^+(n+1) \le n^b\}$ tends to
$\rho(1/a)\rho(1/b)$, the product of the one-dimensional Dickman
marginals. That the limit is a *product* is precisely the
independence assertion: the joint law factors into the marginals. The
limit is taken over all real $X$ with ordinary, unweighted counting —
no logarithmic weighting, so the statement is the "ordinary natural
density" form the conjecture asks for.

**Comparison corollary.** 

> **corollary**
One has
$$\lim_{X\to\infty}\frac1X
 \\\#\{2\leq n\leq X:P^+(n)<P^+(n+1)\}=\frac12.$$
The reverse ordering has the same natural density. [S3:43–50]

Setting $b$ just above $a$ (or vice versa) and letting the threshold
sweep past $n$ yields the ordering statement: the density of
$\{P^+(n) < P^+(n+1)\}$ is $1/2$, and by symmetry so is the reverse
ordering.

## history of the conjecture

Prior (my training data, not this repo): the one-dimensional Dickman
law is classical (Dickman 1930, de Bruijn 1951) and describes the
distribution of $\log P^+(n)/\log n$. The *joint* distribution for
consecutive integers was conjectured by Erdős and Pomerance, who
predicted asymptotic independence with the Dickman marginals. The
difficulty is the arithmetic correlation between $n$ and $n+1$ — they
are coprime, so one cannot read $P^+(n+1)$ off $P^+(n)$, and any
dependence has to come through the additive structure, not a shared
factor. The result places this joint law firmly in the positive
resolutions of the catalog.

## Consequences

**Positive resolution of the Erdős–Pomerance joint Dickman
conjecture.** The logarithmic sizes $\log P^+(n)/\log n$ and
$\log P^+(n+1)/\log n$ are asymptotically independent in ordinary
natural density, with the Dickman marginals, closing the conjecture.

**A 1/2 ordering density.** The comparison corollary
[S3:43–50] pins the density of $\{P^+(n) < P^+(n+1)\}$ at exactly
$1/2$, with the reverse ordering equal, a clean symmetry statement
with no effective constant.

## section skeleton

Single main file [S2:8–14] with a preamble input [S2:2] and eleven section
inputs under `sections/` [S2:17–27], one `.bib` file [S7].

**Sections** [S2:17–27]: Introduction (introduction.tex) with the
joint Dickman law (line 19) and the comparison corollary (line 43);
labels (labels.tex); arithmetic (arithmetic.tex); amplification
(amplification.tex); graph (graph.tex); moments (moments.tex);
channels (channels.tex); kernel (kernel.tex); sampling (sampling.tex);
conclusion (conclusion.tex); distribution (distribution.tex).

## Coverage

T2: one manuscript, one comparator challenge, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes resolution|density`. The family ships a thirteen-file
LaTeX manuscript (main file plus preamble plus eleven sections plus
`references.bib` [S7]) and a compiled `paper.pdf` [S6]. The catalog
entry [S8:100] names the single PDF. No `verification/` bundle, no
reasoning trace.

The comparator stub [S5:44–49] states the target and ends in
`sorry`:

```lean
theorem joint_law (a b : ℝ) (ha : 0 < a) (ha1 : a < 1) (hb : 0 < b) (hb1 : b < 1) :
 Tendsto (realDensity (fun n =>
 (n.maxPrimeFac : ℝ) ≤ (n : ℝ) ^ a ∧ ((n + 1).maxPrimeFac : ℝ) ≤ (n : ℝ) ^ b))
 atTop (𝓝 (Erdos970.NumberTheoryLean.Dickman.rho (1 / a) *
 Erdos970.NumberTheoryLean.Dickman.rho (1 / b))) := by
 sorry
```
[S5:44–49]

The scope note confirms the formalization's reach: "Let $P^+(n)$ be the largest prime factor of $n$. The formalization proves the joint Dickman law in ordinary natural density: for every $0<a,b<1$, the density of integers satisfying $P^+(n)\le n^a$ and $P^+(n+1)\le n^b$ tends to $\rho(1/a)\rho(1/b)$, where $\rho$ is the Dickman function. [S4:9]" and
[S4:11] states the ordering result ("It also proves that each of the
orderings $P^+(n)<P^+(n+1)$ and $P^+(n+1)<P^+(n)$ has natural density
$1/2$."). Note the ledger reads `paps_form 0` (no `main_results`
entry), so the scope note describes an intended target, not a landed
formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 012 at line 300) |
| S2 | [`preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/main.tex`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/main.tex) | 31 | Main file: abstract, section inputs |
| S3 | [`preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/sections/introduction.tex) | 304 | Joint Dickman law + comparison corollary |
| S4 | [`lean/docs/012.md`](../../../lean/docs/012.md) | 17 | Scope note |
| S5 | [`lean/ComparatorChallenges/JointDickman.lean`](../../../lean/ComparatorChallenges/JointDickman.lean) | 65 | Challenge stub (joint_law + sorry) |
| S6 | [`preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) | 16677 | Compiled manuscript |
| S7 | [`preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/references.bib`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/references.bib) | 338 | Bibliography |
| S8 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 012 at line 100) |

## Bibliography

- Alon, Noga, Fernandez de la Vega, W., Kannan, Ravi, Karpinski, Marek, Random sampling and approximation of MAX-CSPs (2003)
- Borgs, Christian, Chayes, Jennifer T., Lovász, László, Sós, Vera T., Vesztergombi, Katalin, Convergent sequences of dense graphs I: Subgraph frequencies, metric properties and testing (2008)
- de Bruijn, N. G., On the number of positive integers $\leq x$ and free of prime factors $>y$ (1951)
- Caputti, Telma, A note on the extension of Lipschitz functions (1984)
- {de la Bret{\`e}che}, Régis, Pomerance, Carl, Tenenbaum, Gérald, Products of ratios of consecutive integers (2005)
- Dickman, Karl, On the frequency of numbers containing prime factors of a certain relative magnitude (1930)
- Ford, Kevin, Sieve Methods Lecture Notes, Spring 2023 (2023)
- Ford, Kevin, Zero-free regions for the Riemann zeta function (2002)
- Frieze, Alan, Kannan, Ravi, Quick approximation to matrices and applications (1999)
- Granville, Andrew, Koukoulopoulos, Dimitris, Beyond the LSD method for the partial sums of multiplicative functions (2019)
- Helfgott, Harald Andrés, Radziwiłł, Maksym, Expansion, divisibility and parity (2021)
- Teräväinen, Joni, On binary correlations of multiplicative functions (2018)
- Jiang, Yujiao, Lü, Guangshi, Wang, Zhiwei, Averaged forms of two conjectures of {Erdős} and Pomerance, and their applications (2022)
- Matomäki, Kaisa, Radziwiłł, Maksym, Multiplicative functions in short intervals (2016)
- Matomäki, Kaisa, Radziwiłł, Maksym, Tao, Terence, An averaged form of Chowla's conjecture (2015)
- Koukoulopoulos, Dimitris, The Distribution of Prime Numbers (2019)
- McDiarmid, Colin, On the method of bounded differences (1989)
- McShane, E. J., Extension of range of functions (1934)
- Montgomery, H. L., Vaughan, R. C., Exponential sums with multiplicative coefficients (1977)
- Pilatte, Cédric, Improved bounds for the two-point logarithmic Chowla conjecture (2023)
- Ramaswami, V., On the number of positive integers less than $x$ and free of prime divisors greater than $x^c$ (1949)
- Erdős, Paul, Pomerance, Carl, On the largest prime factors of $n$ and $n+1$ (1978)
- Tao, Terence, Teräväinen, Joni, The structure of correlations of multiplicative functions at almost all scales, with applications to the Chowla and Elliott conjectures (2019)
- Tao, Terence, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations (2016)
- Tao, Terence, Teräväinen, Joni, Quantitative correlations and some problems on prime factors of consecutive integers (2026)
- Wang, Zhiwei, On the largest prime factors of consecutive integers in short intervals (2017)
- Wang, Zhiwei, Sur les plus grands facteurs premiers d'entiers consécutifs (2018)
- Wang, Zhiwei, Three conjectures on $P^+(n)$ and $P^+(n+1)$ hold under the Elliott–Halberstam conjecture for friable integers (2021)
- Yang, Zhiyuan, An improvement on the largest prime factors of consecutive integers (2026)
- Lü, Xiaodong, Wang, Zhiwei, On the largest prime factors of consecutive integers (2025)
