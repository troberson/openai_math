[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 026](../index/number-theory/026-positive-lower-density-of-large-prime-gaps.md)

# 026 — Positive lower density of large prime gaps

[Index page](../index/number-theory/026-positive-lower-density-of-large-prime-gaps.md)

## Original CONTENTS.md summary

The release blurb 

> **026. Positive lower density of large prime gaps.** For every fixed *C* > 0, a positive proportion of consecutive prime gaps exceed $`C\log p_n`$, throughout every sufficiently large initial segment of the primes. The proportion may depend on *C*. Consequently, the indices where $`p_n/n`$ increases have positive lower density, answering Erdős and Prachar. [S1:650]

The manuscript abstract 

> For every fixed $`C>0`$, we prove that a positive proportion of consecutive
prime gaps exceed $`C\log p`$, where $`p`$ is the smaller prime. The proportion
is bounded below for every sufficiently large initial segment of the
prime sequence, with a constant depending on $`C`$. It follows that the
indices at which $`p_n/n`$ increases have positive lower asymptotic density,
answering a question of Erdős and Prachar. [S2:28–35]

## Undergraduate summary

A "prime gap" is the difference between two consecutive primes. The
prime number theorem says the *average* gap near $`p`$ is about
$`\log p`$ — the primes thin out at exactly that rate. But individual
gaps can be far larger than average: Westzynthius showed the ratio
of a gap to $`\log p`$ is unbounded, and later work (Erdős–Rankin, and
more recently Ford–Green–Konyagin–Tao and Maynard) pushed how large a
single gap can be.

The question here is not about the *largest* gap, but about
*frequency*: for a fixed multiple $`C`$ of the average, what proportion
of primes have a *next* gap larger than $`C\log p`$? The paper proves that
for every such $`C > 0`$, a strictly positive proportion of primes are
followed by such a large gap — and the bound holds uniformly across
every sufficiently large initial segment of the prime list, not just
on average. A clean consequence answers a question of Erdős and
Prachar: the indices at which the ratio $`p_n/n`$ increases have
positive lower density.

The main statement 

> **Theorem 1.1**
For every fixed real $`C>0`$, there are constants $`c(C)>0`$ and $`N_0(C)`$
such that, for every integer $`N\ge N_0(C)`$,
$$\\\#\{1\le n\le N:p_{n+1}-p_n>C\log p_n\}\ge c(C)N.$$ [S3:22–28]

## Graduate summary

The theorem is an ordinary (lower) density statement for the set of
primes whose next gap exceeds a fixed multiple of the log scale.

**Main theorem.** 

> **Theorem 1.1**
For every fixed real $`C>0`$, there are constants $`c(C)>0`$ and $`N_0(C)`$
such that, for every integer $`N\ge N_0(C)`$,
$$\\\#\{1\le n\le N:p_{n+1}-p_n>C\log p_n\}\ge c(C)N.$$ [S3:22–28]

For every fixed real $`C > 0`$ there are constants $`c(C) > 0`$ and
$`N_0(C)`$ such that, for every integer $`N \ge N_0(C)`$, at least $`c(C)N`$
of the first $`N`$ primes satisfy $`p_{n+1} - p_n > C\log p_n`$. The content
is the uniformity in the "lower density" sense: the positive proportion
is a floor on the initial-segment count, so it cannot be produced by a
sparse set of exceptionally large gaps, and both constants may depend
on the threshold $`C`$.

**The prime-ratio corollary.** [S3:38–45]: the set of indices $`n`$ with
$`p_n/n < p_{n+1}/(n+1)`$ has positive lower asymptotic density. The
displayed inequality is the large-gap condition repackaged: since
$`p_n/n \sim \log p_n`$, an increase in the ratio is driven precisely by
a gap that beats the log scale, so the corollary follows from the
theorem. This is the statement the formalization lands , "The formalized supplement proves that the indices $`n`$ for which $`p_n/n<p_{n+1}/(n+1)`$ have positive lower asymptotic density, where $`p_n`$ is the $`n`$th prime. Thus the normalized prime sequence has a positive-density set of increases. This is the prime-ratio corollary associated with the paper's theorem on a positive lower density of large prime gaps. [S4:9]".

## history of the conjecture

Prior (my training data, not this repo): the existence of unbounded
normalized gaps is classical — Westzynthius (1931) proved
$`d_n / \log p_n`$ is unbounded, and the Erdős–Rankin construction gave
gaps of order $`\log p \cdot \log\log p \cdot \log\log\log\log p /
(\log\log\log p)^2`$. The Ford–Green–Konyagin–Tao and Maynard
refinements (2015–2016) removed the extra iterated-log factors, so the
largest gaps are within a constant of the best possible
$`\asymp \log p \cdot \log\log p`$ order. A large-gap *upper* bound,
however, says nothing about *how often* large gaps occur; proving a
positive proportion of gaps exceed $`C\log p`$ is a distinct, frequency
statement. The $`p_n/n`$-increase question of Erdős and Prachar (1962)
had remained open, and the corollary resolves it.

## Consequences

**A positive lower density of large prime gaps, uniformly in the
initial segment.** For every fixed $`C > 0`$, at least $`c(C)N`$ of the
first $`N`$ primes have a next gap exceeding $`C\log p_n`$ [S3:22–28].

**A positive lower density of prime-ratio increases.** The set of
indices $`n`$ with $`p_n/n < p_{n+1}/(n+1)`$ has positive lower
asymptotic density, answering Erdős and Prachar [S3:38–45].

## section skeleton

Single main file [S2:28–35] with five section inputs [S2:37–41]
(introduction, counting, weights, cancellation, moments), one
`.bib` file [S6].

**Sections** [S2:37–41]: Introduction (01-introduction.tex) with the
main theorem (line 22) and the prime-ratio corollary (line 38);
counting (02-counting.tex); weights (04-weights.tex); cancellation
(05-cancellation.tex); moments (03-moments.tex). Note the input order
interleaves the numbering.

## Coverage

T2: one manuscript, one comparator challenge, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes density|uniform`, `resolves_named 0`. The family ships
a seven-file LaTeX manuscript (main file plus five sections plus
`references.bib` [S6]) and a compiled `main.pdf` [S7] at the directory
top level. The catalog entry [S8:128] names the single PDF. No
`verification/` bundle, no reasoning trace.

The comparator stub [S5:36–41] states both the large-gap density and
the prime-ratio density as one combined target, ending in `sorry`:

```lean
theorem large_gaps_and_ratio_density :
    (∀ C : ℝ, 0 < C →
      ∃ c : ℝ, 0 < c ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N →
        c * (N : ℝ) ≤ ((LargePrimeGaps.largeGapIndices C N).card : ℝ)) ∧
    0 < lowerAsymptoticDensity ratioIncreaseIndices := by
  sorry
```
[S5:36–41]

The scope note [S4:9] confirms which half the formalization reaches:
"The formalized supplement proves that the indices $`n`$ for which $`p_n/n<p_{n+1}/(n+1)`$ have positive lower asymptotic density, where $`p_n`$ is the $`n`$th prime. Thus the normalized prime sequence has a positive-density set of increases. This is the prime-ratio corollary associated with the paper's theorem on a positive lower density of large prime gaps. [S4:9]" Note the ledger reads `paps_form 0` (no `main_results` entry),
so the scope note describes an intended target, not a landed
formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 026 at line 650) |
| S2 | [`preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/main.tex`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/main.tex) | 44 | Main file: abstract, section inputs |
| S3 | [`preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/sections/01-introduction.tex`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/sections/01-introduction.tex) | 137 | Main theorem (density of large gaps) + prime-ratio corollary |
| S4 | [`lean/docs/026.md`](../../../lean/docs/026.md) | 15 | Scope note |
| S5 | [`lean/ComparatorChallenges/PrimeGaps.lean`](../../../lean/ComparatorChallenges/PrimeGaps.lean) | 47 | Challenge stub (large gaps + ratio density, sorry) |
| S6 | [`preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/references.bib`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/references.bib) | 215 | Bibliography |
| S7 | [`preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf) | 12043 | Compiled manuscript |
| S8 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 026 at line 128) |

## Bibliography

- Bazzanella, Danilo, Languasco, Alessandro, Zaccagnini, Alessandro, Prime numbers in logarithmic intervals (2010)
- Bombieri, Enrico, Friedlander, John B., Iwaniec, Henryk, Primes in arithmetic progressions to large moduli (1986)
- Bombieri, Enrico, On the large sieve (1965)
- Erdős, Paul, Prachar, Karl, Sätze und Probleme über $`p_k/k`$ (1962)
- Erdős, Paul, On the difference of consecutive primes (1935)
- Ford, Kevin, Green, Ben, Konyagin, Sergei, Tao, Terence, Large gaps between consecutive prime numbers (2016)
- Ford, Kevin, Green, Ben, Konyagin, Sergei, Maynard, James, Tao, Terence, Long gaps between primes (2018)
- Gallagher, Patrick X., On the distribution of primes in short intervals (1976)
- Goldston, Daniel A., Yıldırım, Cem Y., Small Gaps Between Primes I (2005)
- Goldston, D. A., Yıldırım, C. Y., Higher correlations of divisor sums related to primes I: Triple correlations (2003)
- Granville, Andrew, Koukoulopoulos, Dimitris, Maynard, James, Sieve weights and their smoothings (2021)
- Jha, Abhishek, The Poisson Tail Conjecture for primes in short intervals (2026)
- Maynard, James, Small gaps between primes (2015)
- Maynard, James, Large gaps between primes (2016)
- Rankin, R. A., The difference between consecutive prime numbers (1938)
- Tao, Terence, Answer to: Positive proportion of logarithmic gaps between consecutive primes (2019)
- Vinogradov, A. I., The density hypothesis for Dirichlet $`L`$-series (1965)
- Westzynthius, E., Über die Verteilung der Zahlen, die zu den $`n`$ ersten Primzahlen teilerfremd sind (1931)
