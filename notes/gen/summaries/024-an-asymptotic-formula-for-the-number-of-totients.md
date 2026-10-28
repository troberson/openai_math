[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 024](../index/number-theory/024-an-asymptotic-formula-for-the-number-of-totients.md)

# 024 — An asymptotic formula for the number of totients

[Index page](../index/number-theory/024-an-asymptotic-formula-for-the-number-of-totients.md)

## Original CONTENTS.md summary

The release blurb 

> **024. An asymptotic formula for the number of totients.** Gives an asymptotic equivalent for the number $`V(x)`$ of distinct totient values up to x, with a positive bounded phase-dependent factor determined by convergent arithmetic approximations. In particular, $`V(cx)/V(x)\to c`$ for every fixed c > 0, answering Erdős and Hall’s scaling question. [S1:618]

The manuscript abstract 

> Let $V(x)$ count the distinct values of Euler's totient function up to $x$. We give an explicit asymptotic equivalent for $V(x)$. Its coefficient is a uniform limit of functions defined from finite arithmetic data. We also prove that $V(cx)/V(x)\to c$ as $x\to\infty$ for every fixed $c>0$, answering a question of Erdős and Hall. [S2:32–34]

## Undergraduate summary

Euler's totient function $\varphi(n)$ counts the integers up to $n$
that are coprime to $n$. A "totient value" is any number in the image
of $\varphi$ — every $v$ such that $\varphi(n) = v$ for some $n$. Let
$V(x)$ count the distinct totient values at most $x$.

The question here is how $V(x)$ grows. Because most integers have many
representations as a totient value, $V(x)$ grows slower than $x$ — the
paper shows it is of order $x / \log x$ times a positive, bounded,
phase-dependent factor. A clean consequence answers a scaling
question of Erdős and Hall: for any fixed $c > 0$, the ratio
$V(cx) / V(x) \to c$ as $x \to \infty$, so $V$ is "regularly varying"
with index 1 (up to the bounded oscillating factor).

The main statement 

> **theorem**
For sufficiently large positive integers $H$, there are nonnegative
functions $A_H(1;\cdot):[0,1)\to\mathbb R$, given by the finite
arithmetic formula below,
which converge uniformly as $H\to\infty$ to a function $A(1;\cdot)$
satisfying
$$0<\inf_{0\le s<1}A(1;s)
   \le\sup_{0\le s<1}A(1;s)<\infty.$$
With the parameters – ,
$$V(x)\sim\frac{x}{\log x}\,G_m A(1;\theta).$$
Moreover, for every fixed real $c>0$,
$$\frac{V(cx)}{V(x)}\longrightarrow c.$$ [S3:45–63]

## Graduate summary

The theorem is an explicit asymptotic equivalent for the counting
function of totient values, with a bounded oscillating coefficient.

**Main theorem.** 

> **theorem**
For sufficiently large positive integers $H$, there are nonnegative
functions $A_H(1;\cdot):[0,1)\to\mathbb R$, given by the finite
arithmetic formula below,
which converge uniformly as $H\to\infty$ to a function $A(1;\cdot)$
satisfying
$$0<\inf_{0\le s<1}A(1;s)
   \le\sup_{0\le s<1}A(1;s)<\infty.$$
With the parameters – ,
$$V(x)\sim\frac{x}{\log x}\,G_m A(1;\theta).$$
Moreover, for every fixed real $c>0$,
$$\frac{V(cx)}{V(x)}\longrightarrow c.$$ [S3:45–63]

For large $H$ there are nonnegative functions $A_H(1;\cdot)$ of the
phase variable $s \in [0,1)$, defined by a finite arithmetic formula,
which converge uniformly to a limit $A(1;\cdot)$ that is bounded away
from 0 and above on $[0,1)$. With the renewal parameters,
$V(x) \sim (x / \log x) \cdot G_m \cdot A(1;\theta)$, and in particular
$V(cx)/V(x) \to c$ for every fixed real $c > 0$. The content is the
uniform limit of the finite approximants and the positivity: the
coefficient is not zero and not infinite, so the asymptotic is a
genuine equivalent, not just an order bound.

**Companion counts.** The scope note [S4:11] records a second
statement: the asymptotics for totients $v \le x$ whose least preimage
$\ell(v) = \min\{n \ge 1 : \varphi(n) = v\}$ lies in
$[kx, (k+1)x]$. The companion theorem [S3:176–192] gives a positive
coefficient under the stated existence condition, and the exact-zero
case (when no totient $d$ satisfies $kd < \ell(d)$) makes the count
and coefficient identically zero. The cases $k = 1, 2$ have positive
coefficients.

## history of the conjecture

Prior (my training data, not this repo): the distribution of totient
values goes back to Erdős (1935), who established the order
$V(x) \asymp x / \log x \cdot \exp(C \log_2 x / \log_3 x)$ type
estimates. The precise asymptotic equivalent with a bounded
phase-dependent factor is the content here: earlier work gave the
right order but left a slowly varying oscillation. Erdős and Hall
asked, among other things, whether $V$ is regularly varying — i.e.
whether $V(cx)/V(x) \to c$ — and this paper answers that affirmatively
by pinning the coefficient to a positive bounded function of the
phase. The companion count (least preimage in a specified multiple
band) extends the analysis from the total count to a finer
resolution.

## Consequences

**An explicit asymptotic equivalent for the number of totients.**
$V(x) \sim (x/\log x) \cdot G_m \cdot A(1;\theta)$ with
$A(1;\cdot)$ a positive bounded function of the phase, the limit of
uniformly convergent finite arithmetic approximants [S3:45–63].

**The Erdős–Hall regular-variation answer.** $V(cx)/V(x) \to c$ for
every fixed $c > 0$: the counting function is regularly varying with
the bounded oscillating factor [S2:32–34].

**The companion least-preimage counts.** The count of totients
$v \le x$ with $kx \le \ell(v) \le (k+1)x$ has a positive coefficient
for $k = 1, 2$, and is identically zero in the exact no-seed case
[S4:11].

## section skeleton

Single main file [S2:32–34] with seven flat `\input` sections
[S2:41–47], one `.bib` file [S7]. The source tree is nested under
`build/source/`, and the compiled manuscript is at the directory top
level (not under `build/`).

**Sections** [S2:41–47]: Introduction (introduction.tex); Statements
(statements.tex) with the main theorem (line 45) and the companion
theorem (line 176); Extraction (extraction.tex); Layers (layers.tex);
Collisions (collisions.tex); Limits (limits.tex) with the fixed-scaling
corollary (line 103); Companion (companion.tex).

## Coverage

T2: one manuscript, two comparator challenges, zero `main_results`
entries, one scope note. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 2`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes bound|uniform`, `resolves_named 1`. The family ships a
ten-file LaTeX manuscript under `build/source/` (main file plus seven
sections plus `references.bib` [S7]) and a compiled PDF [S8] at the
directory top level. The catalog entry [S9:124] names the single PDF.
No `verification/` bundle, no reasoning trace.

The comparator stubs state the two linked targets.
`TotientAsymptotic.lean` [S5:118–126] is the main asymptotic formula
and the regular-variation statement:

```lean
theorem totient_asymptotic_formula
    :
    TendstoUniformlyOn (fun H => AH H (fun _ => 1)) (A (fun _ => 1))
      atTop (Set.Ico (0 : ℝ) 1) ∧
    (∃ cMinus cPlus : ℝ, 0 < cMinus ∧ ∀ s ∈ Set.Ico (0 : ℝ) 1,
      cMinus ≤ A (fun _ => 1) s ∧ A (fun _ => 1) s ≤ cPlus) ∧
    Tendsto (fun x => V x/mainTerm x) atTop (nhds 1) ∧
    ∀ c : ℝ, 0 < c → Tendsto (fun x => V (c*x)/V x) atTop (nhds c) := by
  sorry
```
[S5:118–126]

`TotientCompanionZero.lean` [S6:95–99] is the companion's exact-zero
case:

```lean
theorem companion_zero_case (k : ℕ) (_hk : 0 < k)
    (hno : ¬ ∃ d : ℕ, IsTotient d ∧ k*d < ell d) :
    (∀ x : ℝ, 0 < x → N k x = 0) ∧
    (∀ s ∈ Set.Ico (0 : ℝ) 1, A (fk k) s = 0) := by
  sorry
```
[S6:95–99]

Both end in `sorry`. The scope note [S4:9] confirms the
formalization's reach: "Let $V(x)$ count the distinct values of Euler's totient function up to $x$. The formalization constructs the paper's explicit positive main term from finite arithmetic approximants and proves that their ratio tends to one. In particular, $V(cx)/V(x)\to c$ for every fixed $c>0$, answering the Erdős–Hall regular-variation question. [S4:9]" Note the ledger reads `paps_form 0`
(no `main_results` entry), so the scope note describes an intended
target, not a landed formalization.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 024 at line 618) |
| S2 | [`preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/main.tex`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/main.tex) | 51 | Main file: abstract, section inputs |
| S3 | [`preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/statements.tex`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/statements.tex) | 210 | Main theorem (totient-count asymptotic) and companion |
| S4 | [`lean/docs/024.md`](../../../lean/docs/024.md) | 18 | Scope note |
| S5 | [`lean/ComparatorChallenges/TotientAsymptotic.lean`](../../../lean/ComparatorChallenges/TotientAsymptotic.lean) | 155 | Challenge stub (asymptotic formula + regular variation, sorry) |
| S6 | [`lean/ComparatorChallenges/TotientCompanionZero.lean`](../../../lean/ComparatorChallenges/TotientCompanionZero.lean) | 104 | Challenge stub (companion zero case, sorry) |
| S7 | [`preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/references.bib`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/references.bib) | 161 | Bibliography |
| S8 | [`preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf) | 15747 | Compiled manuscript |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 024 at line 124) |

## Bibliography

- Erdős, Paul, Some unconventional problems in number theory (1979)
- Erdős, Paul, Some of my favourite problems in number theory, combinatorics, and geometry (1995)
- Ford, Kevin, The distribution of totients (1998)
- Ford, Kevin, Sieve methods lecture notes (2023)
- Ford, Kevin, Lau, Kee-Wai, Asymptotics of a recurrent sequence: 10682 (2000)
- Maier, Helmut, Pomerance, Carl, On the number of distinct values of Euler's $\varphi$-function (1988)
- OpenAI, Weighted dilation graphs, smooth shifted primes and totient fibers (2026)
- Pillai, S. S., On some functions connected with $\phi(n)$ (1929)
- Pollack, Paul, Pomerance, Carl, Trevi{\ n}o, Enrique, Sets of monotonicity for Euler's totient function (2013)
- Pomerance, Carl, On the distribution of the values of Euler's function (1986)
- Erdős, Paul, On the normal number of prime factors of $p-1$ and some related problems concerning Euler's $\phi$-function (1935)
- Erdős, Paul, Some remarks on Euler's $\phi$ function (1958)
- Erdős, Paul, Some remarks on Euler's $\phi$ function and some related problems (1945)
- Erdős, Paul, Hall, R. R., Distinct values of Euler's $\phi$-function (1976)
