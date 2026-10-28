[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 025](../index/number-theory/025-erdoss-short-egyptian-fraction-conjecture.md)

# 025 — Erdős’s short Egyptian-fraction conjecture

[Index page](../index/number-theory/025-erdoss-short-egyptian-fraction-conjecture.md)

## Original CONTENTS.md summary

The release blurb 

> **025. Short Egyptian fractions.** Every rational $`a/b`$ with $`1\le a\lt b`$ is a sum of $`O(\log\log b)`$ distinct positive unit fractions. The worst-case minimum number of terms has the same order, resolving Erdős’s conjecture on short Egyptian fractions. [S1:634]

The manuscript abstract 

> We prove a conjecture of Erdős: for every sufficiently large integer
$b$, every rational number $a/b$ with $1\le a<b$ is a sum of
$O(\log\log b)$ distinct positive unit fractions, with an absolute implied
constant. This order is best possible when the numerator varies. We also
show that both the number of expansions of $1$ with exactly $k$ distinct
terms and the least integer at least $2$ that never occurs as a denominator
in such an expansion grow doubly exponentially in $k$: their double
logarithms have order $k$. [S2:39–48]

## Undergraduate summary

An "Egyptian fraction" writes a rational number as a sum of *distinct*
unit fractions — fractions with numerator 1. For example,
$1/2 + 1/3 + 1/6 = 1$. The old tradition of Egyptian mathematics used
exactly this form, and the modern question is how *short* such an
expansion can be.

Erdős conjectured that every rational $a/b$ (with $1 \le a < b$)
should be writable as a sum of only $O(\log\log b)$ distinct unit
fractions — a doubly logarithmic number of terms, which is far fewer
than what the classical greedy algorithm gives. This paper proves the
conjecture: every such rational has an expansion with
$O(\log\log b)$ terms, and that order is *best possible* when the
numerator is allowed to vary. It also shows that the number of
exact-$k$-term expansions of $1$ grows doubly exponentially in $k$.

The main statement 

> **Theorem 1.1**
There are absolute constants $c_1,c_2>0$ and $b_0$ such that, for every
integer $b\ge b_0$,
\[
 c_1\log\log b\le N(b)\le c_2\log\log b.
\]
In particular, the upper bound holds for every integer numerator
$1\le a<b$. [S3:16–24]

## Graduate summary

The theorem pins the worst-case minimum Egyptian-fraction length to
doubly logarithmic order in the denominator.

**Main theorem.** 

> **Theorem 1.1**
There are absolute constants $c_1,c_2>0$ and $b_0$ such that, for every
integer $b\ge b_0$,
\[
 c_1\log\log b\le N(b)\le c_2\log\log b.
\]
In particular, the upper bound holds for every integer numerator
$1\le a<b$. [S3:16–24]

There are absolute $c_1, c_2 > 0$ and $b_0$ such that for every integer
$b \ge b_0$, the worst-case minimum length $N(b)$ over numerators
$1 \le a < b$ satisfies
$c_1 \log\log b \le N(b) \le c_2 \log\log b$. The upper bound is the
shortness statement (every rational has a $\Theta(\log\log b)$-term
expansion); the lower bound is the matching order (some numerator
forces that many terms), so the worst case is exactly
$\Theta(\log\log b)$.

**Counting and prescribed denominators.** The scope note [S4:9]
records two further statements. If $F(k)$ counts the exact-$k$-term
expansions of $1$, then $\log\log F(k) = \Theta(k)$ — the count is
doubly exponential in $k$. And every integer $m \ge 2$ occurs as a
denominator in some expansion of $1$, with length eventually at most
$(257/\log 2 + \varepsilon)\log\log m$. The least integer $\ge 2$
absent from all exact-$k$-term expansions satisfies
$e^{e^{k/600}} \le v(k) \le 1 + k^{2^{k-1}}$ [S4:11].

## history of the conjecture

Prior (my training data, not this repo): the Egyptian-fraction
problem is classical, and the greedy (Fibonacci–Sylvester) algorithm
always terminates but gives a poor term bound — the length can be as
bad as $O(\log b)$ in the worst case over numerators. Erdős (1948)
asked for the sharp order of the *shortest* expansion, conjecturing
the $O(\log\log b)$ bound and that it is tight. The upper bound
(shortness) and the matching lower bound (best-possible order) together
are the content here; the counting and prescribed-denominator results
characterize the structure of the expansion set at fixed length.

## Consequences

**Every rational has a doubly-logarithmic Egyptian-fraction
expansion.** $a/b$ with $1 \le a < b$ is a sum of $O(\log\log b)$
distinct unit fractions, with a matching lower bound so the worst
case is $\Theta(\log\log b)$ [S3:16–24].

**Doubly-exponential count of exact-$k$-term expansions.** The number
of $k$-term expansions of $1$ has double logarithm of order $k$, and
every integer $\ge 2$ occurs as a denominator eventually within
$(257/\log 2 + \varepsilon)\log\log m$ terms [S4:9].

## section skeleton

Single main file [S2:39–48] with a unicode-mappings input [S2:13] and seven
section inputs [S2:50–56] (introduction, elementary, divisors,
residues, descent, counting, prescribed), one `.bib` file [S8].

**Sections** [S2:50–56]: Introduction (introduction.tex) with the main
theorem (line 16), the counting corollary (line 64), and the
prescribed-denominator corollary (line 102); elementary (elementary.tex);
divisors (divisors.tex); residues (residues.tex); descent (descent.tex);
counting (counting.tex); prescribed (prescribed.tex).

## Comparison with the formalized statement

The scope note states the formalization's reach: "An Egyptian-fraction expansion writes a rational number as a sum of distinct unit fractions. The formalization proves that every $a/b$ with $1\le a<b$ has such an expansion and that the largest minimum length at denominator $b$ is $\Theta(\log\log b)$. If $F(k)$ counts exact $k$-term expansions of $1$, it also proves $\log\log F(k)=\Theta(k)$ and bounds every denominator in such an expansion. [S4:9]" — the
existence of an $\Theta(\log\log b)$-term expansion for every
$1 \le a < b$, the matching worst-case order, the
$\log\log F(k) = \Theta(k)$ count of exact-$k$-term expansions of $1$,
and the prescribed-denominator bound.

The two comparator stubs state the targets. `EgyptianFractions.lean`
 is the double-log worst-case order:

> theorem main_double_log_order :
    ∃ c1 c2 : ℝ, 0 < c1 ∧ 0 < c2 ∧ ∃ b0 : ℕ,
  ∀ b : ℕ, b0 ≤ b →
    c1 * Real.log (Real.log (b : ℝ)) ≤ (maxEgyptianLength b : ℝ) ∧
    (maxEgyptianLength b : ℝ) ≤ c2 * Real.log (Real.log (b : ℝ)) := by
  sorry [S5:57–62]

`ShortEgyptianFractions.lean` [S6:17–23] is the existence-plus-order
statement:

> theorem main :
    (∀ a b : ℕ, 1 ≤ a → a < b → ∃ ns : List ℕ, IsExpansion a b ns) ∧
    ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ 0 < c₂ ∧ ∃ b₀ : ℕ, 2 ≤ b₀ ∧
      ∀ b : ℕ, b₀ ≤ b →
        c₁ * Real.log (Real.log (b : ℝ)) ≤ (maxMinLength b : ℝ) ∧
        (maxMinLength b : ℝ) ≤ c₂ * Real.log (Real.log (b : ℝ)) := by
  sorry [S6:17–23]

Both end in `sorry`. The proofs land in
`OAI/NumberTheory/EgyptianFractions/Main.lean` [S7], which carries
**zero** `sorry` occurrences; the three `main_results` entries
(`OAI.Problem337.main_double_log_order`,
`OAI.Problem337.counting_double_log_order`,
`OAI.Problem337.prescribed_denominator_corollary`) are all in that file
(ledger `paps_form 1`, `mainres 1`, `chal 2`), so the formalization is
landed, in contrast to a stub-only family.

## Coverage

T3: one manuscript, two comparator challenges, one `main_results`
block with three declarations, one scope note. The ledger reads `paps
1`, `paps_form 1`, `mainres 1`, `chal 2`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution`,
`resolves_named 1`. The family ships a ten-file LaTeX manuscript (main
file plus unicode-mappings plus seven sections plus `references.bib`
[S8]) and a compiled PDF [S9] at the directory top level. The catalog
entry [S10:126] names the single PDF. No `verification/` bundle, no
reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 025 at line 634) |
| S2 | [`preprints/Short-Egyptian-fractions-September-25-2026/build/main.tex`](../../../preprints/Short-Egyptian-fractions-September-25-2026/build/main.tex) | 62 | Main file: abstract, section inputs |
| S3 | [`preprints/Short-Egyptian-fractions-September-25-2026/build/introduction.tex`](../../../preprints/Short-Egyptian-fractions-September-25-2026/build/introduction.tex) | 242 | Main theorem (double-log worst-case length) |
| S4 | [`lean/docs/025.md`](../../../lean/docs/025.md) | 18 | Scope note |
| S5 | [`lean/ComparatorChallenges/EgyptianFractions.lean`](../../../lean/ComparatorChallenges/EgyptianFractions.lean) | 124 | Challenge stubs (double-log order, counting, prescribed, sorry) |
| S6 | [`lean/ComparatorChallenges/ShortEgyptianFractions.lean`](../../../lean/ComparatorChallenges/ShortEgyptianFractions.lean) | 27 | Challenge stub (existence + order, sorry) |
| S7 | [`lean/OAI/NumberTheory/EgyptianFractions/Main.lean`](../../../lean/OAI/NumberTheory/EgyptianFractions/Main.lean) | 135 | Proved version in the Lean tree (3 declarations, 0 sorry) |
| S8 | [`preprints/Short-Egyptian-fractions-September-25-2026/build/references.bib`](../../../preprints/Short-Egyptian-fractions-September-25-2026/build/references.bib) | 249 | Bibliography |
| S9 | [`preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf`](../../../preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) | 14975 | Compiled manuscript |
| S10 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 025 at line 126) |

## Bibliography

- Bloom, Thomas F., Erdős Problem 304
- Bloom, Thomas F., Erdős Problem 293
- Croot, III, Ernest S., On some questions of {Erdős} and Graham about Egyptian fractions (1999)
- van Doorn, Wouter, Tang, Quanyu, The smallest denominator not contained in a unit fraction decomposition of $1$ with fixed length (2026)
- Elsholtz, Christian, Egyptian fractions with odd denominators (2016)
- Elsholtz, Christian, Planitzer, Stefan, Sums of four and more unit fractions and approximate parametrizations (2021)
- Erdős, Paul, Az $1/x_1+1/x_2+\cdots+1/x_n=a/b$ egyenlet egész számú megoldásairól (1950)
- Erdős, Paul, Graham, Ronald L., Old and New Problems and Results in Combinatorial Number Theory (1980)
- Erdős, Paul, Turán, Pál, On a problem in the theory of uniform distribution. I, II (1948)
- Gallagher, P. X., A larger sieve (1971)
- Glibichuk, A. A., Konyagin, S. V., Additive properties of product sets in fields of prime order (2007)
- Graham, S. W., Kolesnik, G., Van der Corput's Method of Exponential Sums (1991)
- Hildebrand, Adolf, Tenenbaum, Gérald, Integers without large prime factors (1993)
- Konyagin, S. V., Double exponential lower bound for the number of representations of unity by Egyptian fractions (2014)
- Kumchev, Angel, On the Piatetski-Shapiro-Vinogradov theorem (1997)
- Kumchev, Angel V., Tolev, Dimitar I., An invitation to additive prime number theory (2005)
- Martin, Greg, Denser Egyptian fractions (2000)
- Nakayama, Masayosi, On the decomposition of a rational number into ``{Stammbrüche}'' (1940)
- Erdős, Paul, On the sum $\sum_{k=1}^{x}d(f(k))$ (1952)
- Selberg, Atle, An elementary proof of the prime-number theorem (1949)
- Takenouchi, Tanz{\^o}, On an indeterminate equation (1921)
- Tenenbaum, Gérald, Yokota, Hisashi, Length and denominators of Egyptian fractions, III (1990)
- Vose, Michael D., Egyptian fractions (1985)
