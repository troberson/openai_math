[Notes](../../README.md) / [Summaries](../README.md) / [Number theory](../../index/disciplines/number-theory.md) / [Family 022](../../index/number-theory/022-weak-inhomogeneous-duffin-schaeffer-conjecture.md)

# 022 — The weak inhomogeneous Duffin–Schaeffer conjecture

[Index page](../../index/number-theory/022-weak-inhomogeneous-duffin-schaeffer-conjecture.md)

## Original CONTENTS.md summary

The release's blurb 

> **022. The weak inhomogeneous Duffin–Schaeffer conjecture.** Proves that for every real shift *γ* and finite-valued $\`\psi:\mathbb N\to[0,\infty)`$, divergence of $\`\sum_q\phi(q)\psi(q)/q`$ implies $\`\|qx-\gamma\|\lt \psi(q)`$ for infinitely many *q*, for almost every *x*. Here *ϕ* is Euler's totient and the norm is distance to the nearest integer. Numerators are unrestricted; no monotonicity or Diophantine condition on *γ* is needed. [S1:586]

The catalog abstract says the same thing: "Proves that for every real shift $\gamma$ and finite-valued $\psi:\mathbb N\to[0,\infty)$, divergence of $\sum_q\phi(q)\psi(q)/q$ implies $\|qx-\gamma\|<\psi(q)$ for infinitely many $q$, for almost every $x$. Here $\phi$ is Euler's totient and the norm is distance to the nearest integer. Numerators are unrestricted; no Diophantine condition on $\gamma$ is needed. [S2:120]" The manuscript's own
title is "The Weak Inhomogeneous Duffin–Schaeffer Conjecture [S3:1]" , and its abstract reads: "We prove the weak inhomogeneous Duffin–Schaeffer conjecture. For every fixed $\gamma\in\mathbb R$ and finite-valued $\psi:\mathbb N\to[0,\infty)$, divergence of $\sum_{q\ge1}\phi(q)\psi(q)/q$ implies $\|qx-\gamma\|<\psi(q)$ for infinitely many $q$, for almost every $x$. Here $\phi$ is Euler's totient and $\|\cdot\|$ is distance to the nearest integer. Numerators need not be reduced, and the shift satisfies no Diophantine restriction. [S4:38–45]"

## Undergraduate summary

The setting is Diophantine approximation with a shift. Write $\|t\|$ for
distance to the nearest integer, and let $\phi$ be Euler's totient.
The theorem 

> **Theorem 1.1**
Let $\gamma\in\mathbb R$ be fixed, and let
$\psi:\mathbb N\to[0,\infty)$ be finite-valued. If
$$\label{eq:main-divergence}
  \sum_{q=1}^{\infty}\frac{\phi(q)}q\,\psi(q)=\infty,$$
then, for Lebesgue-almost every $x\in\mathbb R$, the inequality
\[
  \|qx-\gamma\|<\psi(q)
\]
holds for infinitely many positive integers $q$. [S5:9–21]

In words: if the totient-weighted sum $\sum_q \phi(q)\psi(q)/q$ diverges,
then for almost every real $x$ the inequality $\|qx-\gamma\|<\psi(q)$
holds for infinitely many $q$. The shift $\gamma$ is arbitrary — no
Diophantine condition. The integer nearest to $qx-\gamma$ is
unrestricted: no coprimality condition on the numerator [S5:23–27].
"Theorem   resolves the weak inhomogeneous Duffin–Schaeffer
conjecture positively, including every prescribed irrational shift.
The integer nearest to $qx-\gamma$ is unrestricted: no coprimality
condition is imposed on the numerator. The conclusion is a divergence
statement, not a convergence converse or a quantitative asymptotic. [S5:23–27]"

The "weak" in the name refers to the unrestricted numerator. The
stronger formulation requires $(a,q)=1$, and that assertion is false
in general: counterexamples exist for every nonzero rational shift
. "$|qx-a-\gamma|<\psi(q)$ is arbitrary. The stronger formulation
requires $(a,q)=1$; this distinction is already explicit in
Ramírez  . Theorem   addresses the weak
formulation for every prescribed real shift.

The coprime-numerator assertion is false in general: Hauke-Treuer,
Maynard and Pollington \cite[Theorem 1]HMP2026 construct [S5:95–101]"

## Graduate summary

**The proof strategy.** The proof works on arbitrarily late finite
collections of "rows" — periodic arrays of points $(z+\gamma)/q$ with
spatial half-width $\psi(q)/q$. On each collection it constructs a
nonnegative weighted sum of interval indicators, changes weights through
prescribed prime-step updates, and shows the comparison sum is
equidistributed with a uniform second-moment bound. These bounds
contradict the existence of a positive-measure set avoiding all
sufficiently late rows . "Put $r(q)=\psi(q)/q$. A row is the periodic array of points
$(z+\gamma)/q$, $z\in\mathbb Z$, with spatial half-width $r(q)$.
The proof works on arbitrarily late finite collections of rows whose
totient-weighted mass lies in a fixed small interval. On each collection
we construct a nonnegative weighted sum of interval indicators supported
inside the original approximation intervals. The construction changes
weights through prescribed prime-step updates and additional deletions. [S5:167–173]"

**The arithmetic engine.** The second-moment bound faces two
obstructions. First, nearness of two shifted points constrains an integer
combination of their numerators to a short interval; the small-scale
extraction estimates of Section 4 handle this via a sieve, rotation
argument, or rational-approximation alternative [S10] [S11]. Second,
large common primes create correlated alignments across collections; the
centre construction exposes prime factors in an increasing sequence of
scales, and the prime-step pairing rule in Section 6 cancels the most
tightly correlated transfers [S7] [S12]. The remaining correlations are
paid by a squared-mass argument using history-preserving partitions
[S13] [S14].

**The Hausdorff corollary.** The Lebesgue-measure theorem feeds the
mass transference principle of Beresnevich–Velani to give a
Hausdorff-$f$-measure divergence theorem: if
$\sum_q \phi(q)\,f(\psi(q)/q)$ diverges with $f(r)/r$ monotone,
then the limsup set has full $\mathcal H^f$-measure in every bounded
interval . "\section{The Hausdorff-measure consequence}
 

We now apply the proved Lebesgue-measure theorem to the transformed
radii in the mass transference principle.

\beginproof[Proof of Corollary  ]
Put $r_q=\psi(q)/q$. If $r_q\not\to0$, then along an unbounded
sequence of denominators $r_q\ge\delta>0$, so $\psi(q)>1/2$
eventually. Since $\|qx-\gamma\|\le1/2$ for every $x$, in this
case $W_\gamma(\psi)=\mathbb R$. [S15:1–15]"

## History of the conjecture

The monotone theory is classical: Khintchine's theorem gives a
full-measure conclusion for $\|qx\|<\psi(q)$ when $\psi$ is
non-increasing and $\sum_q\psi(q)$ diverges; Szüsz extended it to
each fixed inhomogeneous shift . "The starting point is the monotone theory of metric approximation.
Khintchine's theorem  , in its usual modern form,
gives a full-measure conclusion for $\|qx\|<\psi(q)$ when $\psi$ is
non-increasing and $\sum_q\psi(q)$ diverges. Szüsz extended the
monotone theory to each fixed inhomogeneous shift  ;
see also the precise modern formulation in  .
Removing monotonicity changes the problem because many denominators
can describe strongly overlapping approximation intervals. [S5:60–67]"

Removing monotonicity is the hard step: "many denominators can
describe strongly overlapping approximation intervals" [S5:67].
"can describe strongly overlapping approximation intervals. [S5:67]" Duffin and Schaeffer proposed the weighted sum
$\sum_q\phi(q)\psi(q)/q$ in the homogeneous setting;
Koukoulopoulos and Maynard proved their 1941 conjecture [S5:68–74].
"Duffin and Schaeffer   exhibited this obstruction in the
homogeneous setting and proposed using reduced fractions with the
weighted sum $\sum_q\phi(q)\psi(q)/q$. Koukoulopoulos and
Maynard   proved their conjecture. The weight $\phi(q)/q$
records the proportion of reduced residue classes; it also gives a
meaningful sufficient divergence criterion when all numerators are
allowed. [S5:68–74]"

The fixed-shift weighted question appears under the name "weak
inhomogeneous Duffin–Schaeffer conjecture" in Chow and Technau and
as Conjecture 2 of Beresnevich, Hauke and Velani [S5:89–95].
"The fixed-shift weighted question appears explicitly in
Yu \cite[Question 1.2]Yu2021 and under the name _weak inhomogeneous
Duffin–Schaeffer conjecture_ in Chow and
Technau \cite[Conjecture 1.22]ChowTechnau2024. It is also
Conjecture 2 of Beresnevich, Hauke and Velani  .
The word ``weak'' concerns the conclusion: the integer $a$ in
$|qx-a-\gamma|<\psi(q)$ is arbitrary. [S5:89–95]"

## Consequences

**Hausdorff-measure divergence.** The mass transference principle
gives a full Hausdorff-$f$-measure conclusion for each fixed shift,
with unrestricted numerators and no monotonicity of $\psi$
[S15:1–15]. The proof applies the theorem to the transformed radii
$f(\psi(q)/q)$ and transfers via the closed-ball limsup [S15:1–15].

## Section skeleton

**Main file** [S4:38–45], 11 sections under `build/sections/`:

1. Introduction [S5]
2. Finite blocks and elementary conventions [S6]
3. Centres, density, and prime heights [S7]
4. Masks and initial numerator prescriptions [S8]
5. Projected tables and the second-moment reduction [S9]
6. Arithmetic estimates for close pairs [S10]
7. Direct comparisons at simultaneous births [S11]
8. Alignments in sparse prime steps [S12]
9. Construction of the operational partitions [S13]
10. First joins of previously constructed tables [S14]
11. The Hausdorff-measure consequence [S15:1–15]

Bibliography: `references/main.bib` [S16].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
13 `.tex` files and 1 `.bib` file under `build/`, totalling 6,644 lines of
section `.tex` alone.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 022 at line 586. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 120. |
| S3 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/README.md`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S4 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/main.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/main.tex) | 64 | The main file: the abstract and the section order. |
| S5 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/introduction.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/introduction.tex) | 241 | The theorem, the Hausdorff corollary, the background, the weak/strong distinction, and the proof strategy. |
| S6 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/preliminaries.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/preliminaries.tex) | 306 | Finite blocks, small-width reduction, and elementary tensor and residue estimates. |
| S7 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/centres.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/centres.tex) | 516 | Centres, density, and prime heights: the scale-sequence construction. |
| S8 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/prescriptions.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/prescriptions.tex) | 413 | Masks and initial numerator prescriptions. |
| S9 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/tables.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/tables.tex) | 1066 | Projected tables and the second-moment reduction to three comparison and partition assertions. |
| S10 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/arithmetic.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/arithmetic.tex) | 780 | Arithmetic estimates for close pairs: the sieve, rotation, and small-scale concentration estimates. |
| S11 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/direct.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/direct.tex) | 1169 | Direct comparisons at simultaneous births: both alternatives for the overlap weight. |
| S12 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/sparse.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/sparse.tex) | 513 | Alignments in sparse prime steps: the prime-step update rule. |
| S13 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/partitions.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/partitions.tex) | 749 | Construction of the operational partitions. |
| S14 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/joins.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/joins.tex) | 853 | First joins of previously constructed tables: the covariance transfer and capacity bound. |
| S15 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/consequences.tex`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/sections/consequences.tex) | 38 | The Hausdorff-measure corollary proof via the mass transference principle. |
| S16 | [`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/references/main.bib`](../../../preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/references/main.bib) | 230 | The bibliography. |

## Bibliography

- Beresnevich, Victor, Velani, Sanju, A Mass Transference Principle and the Duffin–Schaeffer conjecture for Hausdorff measures (2006)
- Beresnevich, Victor, Hauke, Manuel, Velani, Sanju, Borel–Cantelli, zero-one laws and inhomogeneous Duffin–Schaeffer (2024)
- Chow, Sam, Technau, Niclas, Littlewood and Duffin–Schaeffer-type problems in Diophantine approximation (2024)
- Chow, Sam, Hauke, Manuel, Pollington, Andrew, Ram{í}rez, Felipe A., General Duffin–Schaeffer-type counterexamples in Diophantine approximation (2025)
- Duffin, R. J., Schaeffer, A. C., Khintchine's problem in metric Diophantine approximation (1941)
- Gou, Haozhe, Extremal Problems for GCDs and LCMs in Higher Dimensions (2026)
- Green, Ben, Walker, Aled, Extremal problems for GCDs (2021)
- Hauke-Treuer, Manuel, Vazquez, Santiago, Walker, Aled, Proving the Duffin–Schaeffer conjecture without GCD graphs (2026)
- Hauke-Treuer, Manuel, Maynard, James, Pollington, Andrew, Counterexamples to the inhomogeneous Duffin–Schaeffer Conjecture (2026)
- He, Yubin, Liao, Lingmin, Counterexamples to the inhomogeneous Duffin–Schaeffer conjecture for a residual set of shifts (2026)
- Khintchine, A., Einige S{ä}tze {ü}ber Kettenbr{ü}che, mit Anwendungen auf die Theorie der Diophantischen Approximationen (1924)
- Koukoulopoulos, Dimitris, Maynard, James, On the Duffin–Schaeffer conjecture (2020)
- Pollington, A. D., Vaughan, R. C., The $k$-dimensional Duffin and Schaeffer conjecture (1990)
- Ram{í}rez, Felipe A., Counterexamples, covering systems, and zero-one laws for inhomogeneous approximation (2017)
- Selberg, Atle, On an elementary method in the theory of primes (1947)
- Sz{ü}sz, P., {Ü}ber die metrische Theorie der diophantischen Approximation (1958)
- Uchiyama, Sabur{\^o}, A note on the sieve method of {A. Selberg} (1962)
- Yu, Han, A Fourier-analytic approach to inhomogeneous Diophantine approximation (2019)
- Yu, Han, On the metric theory of inhomogeneous Diophantine approximation: An {Erdős–Vaaler} type result (2021)
