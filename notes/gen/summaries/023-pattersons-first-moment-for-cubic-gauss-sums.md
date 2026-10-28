[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 023](../index/number-theory/023-pattersons-first-moment-for-cubic-gauss-sums.md)

# 023 — Patterson’s first moment for cubic Gauss sums

[Index page](../index/number-theory/023-pattersons-first-moment-for-cubic-gauss-sums.md)

## Original CONTENTS.md summary

The release blurb 

> **023. Patterson's first moment for cubic Gauss sums.** Proves unconditionally the all-primary-prime form of Patterson's first-moment asymptotic: normalized cubic Gauss sums over primary Eisenstein primes of norm at most X, including both conjugates, have an explicit positive main term of order $`X^{5/6}/\log X`$. Every fixed nonzero prime-angle Fourier mode has smaller order. [S1:602]

The manuscript abstract 

> We prove Patterson's first-moment conjecture for normalized cubic
Gauss sums over all primary Eisenstein primes, unconditionally. The sharp-cutoff main
term is $(6/5)c_*X^{5/6}/\log X$, where
$c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$.
For every fixed nonzero angular Fourier mode of the prime argument,
we also prove cancellation at the first-moment scale. [S2:40–47]

## Undergraduate summary

A "Gauss sum" attached to a prime $\pi$ in the ring of Eisenstein
integers (integers of the form $a + b\sqrt{-3}$) is a finite sum of
cubic roots of unity that encodes how the prime sits in the number
field. Patterson's conjecture predicts what the *average* of these
sums looks like as you sweep over all primes up to a size $X$: the
average should have a main term of order $X^{5/6} / \log X$ with an
explicit positive constant.

This paper proves that prediction unconditionally — no unproved
hypotheses needed. It covers all primary Eisenstein primes (those
congruent to $1 \bmod 3$), including both conjugate directions, and
proves that the leading term is $(6/5) \cdot c_* \cdot X^{5/6} /
\log X$ where $c_* = (2\pi)^{2/3} / (3\Gamma(2/3))$. It also proves
that the "angular" Fourier modes (the parts of the sum that oscillate
with the angle of the prime) are all smaller order for any
nonzero frequency.

The main statement 

> **theorem**
As $X\longrightarrow\infty$,
$$\label{eq:main}
 \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}G(\pi)
 =\frac65c_*\frac{X^{5/6}}{\log X}
   +o\!\left(\frac{X^{5/6}}{\log X}\right).$$
The sum is over all primary primes in $\mathcal O$. [S2:64–72]

## Graduate summary

The theorem is an unconditional first-moment asymptotic for
normalized cubic Gauss sums over primary Eisenstein primes.

**First moment.** 

> **theorem**
As $X\longrightarrow\infty$,
$$\label{eq:main}
 \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}G(\pi)
 =\frac65c_*\frac{X^{5/6}}{\log X}
   +o\!\left(\frac{X^{5/6}}{\log X}\right).$$
The sum is over all primary primes in $\mathcal O$. [S2:64–72]

As $X \to \infty$, the sum of $G(\pi)$ over all primary Eisenstein
primes of norm at most $X$ equals
$\frac{6}{5} c_* X^{5/6} / \log X + o(X^{5/6} / \log X)$, with
$c_* = (2\pi)^{2/3} / (3\Gamma(2/3))$. The sum is unconditional — all
primary primes are included, no GRH-type hypothesis, and both
conjugate directions contribute to the same main term.

**Angular comparison.** For each fixed integer angular Fourier mode
$\ell$, the oscillatory part of the sum is $o(X^{5/6} / \log X)$
[S3:19–35]. In the nonzero-mode case this gives cancellation: the
angular component of the first moment is smaller than the main term
at the first-moment scale.

**Scope note confirmation.** "Patterson's first-moment conjecture concerns the average of normalized cubic Gauss sums over primary Eisenstein primes. The formalization proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. It also proves the corresponding angular comparison for every integer Fourier mode and cancellation of order $o(X^{5/6}/\log X)$ for each fixed nonzero mode. All primary Eisenstein primes are included, without an extra conjectural premise. [S4:9]" All primary Eisenstein
primes are included without an extra conjectural premise, and the
angular comparison covers every integer Fourier mode.

## history of the conjecture

Prior (my training data, not this repo): Patterson (1976) studied the
first moment of cubic Gauss sums and predicted the sharp-cutoff
asymptotic with main term of order $X^{5/6} / \log X$ under a
conditional framework. The unconditional all-primary-prime form is
the content of this paper: it removes the conditional premise and
covers the full prime set without a bias towards one conjugate class.
The angular comparison and cancellation for nonzero modes is a
refinement over the mean: it says the leading term captures the full
first moment, not just the zero-frequency projection. The proof
combines Heath-Brown's cubic large sieve with a level-Voronoi formula
and a Perron-type integral decomposition.

## Consequences

**Unconditional first-moment asymptotic for cubic Gauss sums.** The
sharp-cutoff main term $(6/5)c_* X^{5/6}/\log X$ is proved for all
primary Eisenstein primes, with both conjugates, no conjectural
premise [S2:64–72].

**Angular comparison and cancellation.** Every fixed nonzero angular
Fourier mode is $o(X^{5/6}/\log X)$: the oscillatory part of the
first moment is strictly smaller than the main term [S3:19–35].

## section skeleton

Single main file [S2] with a `figures/` input [S2:225] and six
section inputs [S2:253–260] (background-type1, dual, dispersion,
decomposition, perron, angular), no `.bib` file (inline
`thebibliography`).

**Sections:** Background and the cubic large sieve
(01-background-type1.tex) with Heath-Brown's cubic large sieve
(line 158) and the level-Voronoi formula (line 306); dual (dual.tex);
dispersion (dispersion.tex); decomposition (decomposition.tex);
Perron integral (perron.tex); angular comparison (angular.tex) with
the main angular theorem (line 19).

## Coverage

T2: one manuscript, one comparator challenge, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes partial`. The family ships a seven-file LaTeX
manuscript (main file plus six sections), a compiled `paper.pdf`
[S6], and a `README.md`. No `.bib` file, no `verification/` bundle,
no reasoning trace. The catalog entry [S7:122] names the single PDF.

The comparator stub [S5:84–93] states three targets — the first
moment, the angular comparison, and the angular cancellation — all
ending in `sorry`:

```lean
theorem patterson_firstMoment : FirstMomentStatement := by
  sorry

/-- Model comparison in every fixed integer angular mode. -/
theorem patterson_angularComparison : AngularComparisonStatement := by
  sorry

/-- Cancellation at the first-moment scale for each nonzero angular mode. -/
theorem patterson_angularCancellation : AngularCancellationStatement := by
  sorry
```
[S5:84–93]

The scope note confirms the formalization's reach: "Patterson's first-moment conjecture concerns the average of normalized cubic Gauss sums over primary Eisenstein primes. The formalization proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. It also proves the corresponding angular comparison for every integer Fourier mode and cancellation of order $o(X^{5/6}/\log X)$ for each fixed nonzero mode. All primary Eisenstein primes are included, without an extra conjectural premise. [S4:9]"
Note the ledger reads `paps_form 0` (no `main_results` entry), so
the scope note describes an intended target, not a landed
formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 023 at line 602) |
| S2 | [`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex`](../../../preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex) | 394 | Main file: abstract, main theorem, section inputs |
| S3 | [`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex`](../../../preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex) | 838 | Angular comparison theorem |
| S4 | [`lean/docs/023.md`](../../../lean/docs/023.md) | 15 | Scope note |
| S5 | [`lean/ComparatorChallenges/PattersonFirstMoment.lean`](../../../lean/ComparatorChallenges/PattersonFirstMoment.lean) | 99 | Challenge stub (first moment + angular, sorry) |
| S6 | [`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf`](../../../preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) | 18439 | Compiled manuscript |
| S7 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 023 at line 122) |

## Bibliography

- E. Chen, P. S. Park and A. A. Swaminathan, _Linnik's theorem for Sato–Tate laws on elliptic curves with complex multiplication_, Research in Number Theory **1** (2015), article 28. . Numbered references use arXiv:1506.09170v3, .
- G. Harcos, _The Bombieri–Halász–Montgomery inequality_, undated note, Theorem 1, equation (1). .
- D. R. Heath-Brown, _Kummer's conjecture for cubic Gauss sums_, Israel Journal of Mathematics **120** (2000), 97–124. . Numbered references use the author's manuscript.
- M. N. Huxley, _The large sieve inequality for algebraic number fields_, Mathematika **15** (1968), no. 2, 178–187. .
- H. Iwaniec and E. Kowalski, _Analytic Number Theory_, American Mathematical Society Colloquium Publications, vol. 53, American Mathematical Society, Providence, RI, 2004. .
- E. E. Kummer, _De residuis cubicis disquisitiones nonnullae analyticae_, Journal für die reine und angewandte Mathematik **32** (1846), 341–359. .
- D. R. Heath-Brown and S. J. Patterson, _The distribution of Kummer sums at prime arguments_, Journal für die reine und angewandte Mathematik **310** (1979), 111–130. .
- S. J. Patterson, _A cubic analogue of the theta series_, Journal für die reine und angewandte Mathematik **296** (1977), 125–161. .
- S. J. Patterson, _On the distribution of Kummer sums_, Journal für die reine und angewandte Mathematik **303/304** (1978), 126–143. .
- A. Dunn and M. Radziwiłł, _Bias in cubic Gauss sums: Patterson's conjecture_, Annals of Mathematics **200** (2024), no. 3, 967–1057. . All numbered references to this paper use arXiv:2109.07463v3, May 14, 2024, .
- C. S. Rajan, _Distribution of values of Hecke characters of infinite order_, Acta Arithmetica **85** (1998), no. 3, 279–291. .
- I. Kaneko and J. Thorner, _Highly uniform prime number theorems_, Annales de l'Institut Fourier **75** (2025), no. 5, 1901–1923. .
- H. L. Montgomery and R. C. Vaughan, _Hilbert's inequality_, Journal of the London Mathematical Society (2) **8** (1974), 73–82. .
- D. Wan, _Exponential sums over finite fields_, Journal of Systems Science and Complexity **34** (2021), 1225–1278. .
- M. Watkins, _Computing with Hecke Grössencharacters_, Publications mathématiques de Besançon. Alg\`ebre et théorie des nombres (2011), 119–135. .
- A. Yoshimoto, _On the cubic theta function_, Nagoya Mathematical Journal **105** (1987), 153–167. .
- J. Thorner and A. Zaman, _A unified and improved Chebotarev density theorem_, Algebra & Number Theory **13** (2019), no. 5, 1039–1068. .
- P. Gao and L. Zhao, _The large sieve with power moduli in imaginary quadratic number fields_, International Journal of Number Theory **18** (2022), no. 8, 1713–1733. . The equation (1.2) locator refers to arXiv:2101.00811v2, .
