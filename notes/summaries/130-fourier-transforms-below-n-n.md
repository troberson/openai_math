[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 130](../index/theoretical-computer-science/130-fourier-transforms-below-n-n.md)

# 130 — Fourier transforms below $n\log n$

[Index page](../index/theoretical-computer-science/130-fourier-transforms-below-n-n.md)

## Original CONTENTS.md summary

[S1:3127] (family entry):

> **130. Exact Fourier transforms below $`n\log n`$.** Gives a deterministic length-n discrete Fourier transform algorithm using $`O(n(\log n)^{1-\delta})`$ operations for every n, with explicit $`\delta=10^{-13}`$. The model uses exact complex arithmetic, unrestricted coefficients and a supplied root of unity, and counts scalar preparation and logarithmic-word indexing. ([Lean](lean/docs/130.md))

[S2:337] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

The **discrete Fourier transform** (DFT) of a vector of $n$ complex
numbers produces a new vector capturing the frequencies in the original.
The classic **Fast Fourier Transform** (FFT) computes it in
$O(n\log n)$ operations, down from the naive $O(n^2)$.

This family asks: can we do **better than $O(n\log n)$** while computing
the DFT *exactly* (no rounding)? The answer, in a precise model, is yes —
in a limited sense.

MS1 [S4:85–91] gives a single deterministic algorithm that computes the
exact DFT at every length $n$ in
$O(n(\log n)^{1-10^{-13}})$ operations [S4:93–99] — a power saving of
$\delta=10^{-13}$ over the $O(n\log n)$ barrier. MS2 [S8:46–54] proves the
subsequential form: along some unbounded sequence of lengths, the exact
circuit cost is $o(n\log n)$.

The catch is the **model**: exact complex arithmetic, unrestricted
coefficients, a supplied root of unity, and logarithmic-word indexing
[S6:10]. The result is an asymptotic existence statement — the constants
are enormous — not a practical speedup over the FFT.

## Graduate summary

**MS1 main theorem** ([S4:85–91], `thm:main`). "There is a single
deterministic algorithm which, for every positive integer $n$ and every
$x\in\mathbb C^n$, computes $F_nx$ exactly. In the model above, including scalar
preparation, schedule construction, and index work, its running time is
$O(n(\log n)^\theta(\log\log n)^{4-\theta})$ as $n\to\infty$" [S4:85–91].
The corollary specializes to
$O(n(\log n)^{1-10^{-13}})=o(n\log n)$ [S4:93–99]. The model uses exact
complex arithmetic, unrestricted coefficients, and a supplied root of
unity; scalar preparation and indexing work are included [S4:101].

**MS2 main theorem** ([S8:46–54], `thm:main`). "In this model,
$\liminf_{n\to\infty}\frac{L(n)}{n\log_2 n}=0$. Equivalently, for every
$c>0$ and every integer $N_0\ge2$, there is an integer $n\ge N_0$ and an
exact circuit for $F_n$ with fewer than $c n\log_2 n$ gates" [S8:46–54].
This refutes the assertion that $L(n)\ge c n\log_2 n$ for some fixed
$c>0$ and all sufficiently large $n$ [S8:58–59].

**The two results are related but distinct.** MS1 is *uniform* — one
algorithm for every length — with an explicit (tiny) power saving. MS2 is
*subsequential* — along an unbounded sequence of lengths — with an
arbitrarily small normalized cost [S6:10,12].

## History of the conjecture

The $\Omega(n\log n)$ lower-bound question for the Fourier transform is
discussed in the work of **Ailon** and of **Alman and Rao**
[S8:56–57]. The prior best exact-arithmetic bounds met the
$O(n\log n)$ barrier; the question was whether an exact algorithm could
behave asymptotically better.

MS2's proof refutes the lower-bound assertion by constructing, via tensor
methods, circuits of sub-$n\log n$ cost on an unbounded sequence of
lengths [S8:46–60]. MS1's proof supplies the uniform algorithm with an
explicit, if tiny, power saving [S4:85–101].

**Prior (my training data, not this repo).** The $O(n\log n)$ barrier for
the DFT was long believed to be fundamental in exact-arithmetic models.
Sub-$n\log n$ upper bounds in the *real-arithmetic* / bounded-coefficient
setting were known (the Schönhage-style results), but the extension to
the exact-complex-unrestricted-coefficient model with the power saving
made explicit is the contribution here. I cannot confirm the specific
prior results independently; the release ships the two manuscripts as
proofs.

## Consequences

- **The exact DFT is computable in sub-$n\log n$ time (subsequentially).**
  There is an unbounded sequence of lengths $n$ for which the exact DFT
  circuit cost is $o(n\log n)$ [S8:46–54].
- **A uniform algorithm with an explicit power saving exists.** A single
  deterministic algorithm computes the exact DFT at every length $n$ in
  $O(n(\log n)^{1-10^{-13}})$ operations [S4:85–99].
- **The model is exact and unrestricted.** Exact complex arithmetic,
  unrestricted coefficients, a supplied root of unity, logarithmic-word
  indexing; scalar preparation and indexing work are counted [S6:10].
- **Convolution is covered too.** The uniform formalization also gives a
  bilinear program for the full length-$n$ convolution at the same
  asymptotic bound [S6:12].
- **No practical crossover.** The constants are enormous; the results are
  asymptotic existence and explicitness, not a floating-point speedup or
  a bit-complexity claim [S4:101].

## Section skeleton

MS1 [S3] is a 57-line root: a 40-line preamble with package declarations,
title block, abstract [S3:41–43], five section files [S3:44–48], a
synthesis appendix [S3:49–50], and a `plain` bibliography [S3:52–56]. The
sections, in order and line count: `introduction` (160), `network` (575),
`local` (444), `synchronization` (85), `all-lengths` (203), and the
appendix `synthesis` (420) — 1,887 section lines. The shipped PDF [S5] is
the manuscript in the form the release distributes.

MS2 [S7] is a 71-line root: package declarations and title block,
abstract [S7:51–59], eight section files [S7:61–68], and a bibliography.
The sections, in order and line count: `01-introduction` (263),
`02-generation` (306), `03-fourier-transfer` (443),
`04-packing-prices` (581), `05-corners` (487), `06-feedback` (494),
`07-pivots` (431), `08-reflection` (551) — 3,156 section lines. The
shipped PDF [S9] is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S6],
**two** comparator stubs, and **two** `main_results` configs — the
formalization is **complete at the declaration level**.

The scope note [S6] describes two layers of formalized content:
[S6:10] the subsequential result — for every $c>0$ and cutoff $N_0\ge2$,
some $n\ge N_0$ has a circuit computing the unnormalized DFT with fewer
than $cn\log_2 n$ gates, with addition, subtraction, and scalar
multiplication each costing one gate; and [S6:12] the uniform
formalization — fixed deterministic programs for every positive length $n$
computing the canonical DFT and the full convolution exactly, at
$O(n(\log n)^{1-10^{-13}})=o(n\log n)$ work.

The scope note links **two** comparator configs [S6:18–19]:

- `ExactFourier.lean` [S10] (62 lines) — `MainStatement` [S10:52–55]
  encodes the subsequential claim: for every $c>0$ and $N_0\ge2$, some
  $n\ge N_0$ has a circuit computing the Fourier matrix with size
  $< c n\log_2 n$; `main_theorem` [S10:57–58], `sorry` at [S10:58].
  Declaration `OAI.ExactFourier.main_theorem`.
- `UniformFourier.lean` [S11:326–331] (336 lines) —
  `transform_main : DFTGoal` [S11:326–327] (one fixed program computes
  every positive-length canonical DFT, including preparation, with a
  sub-$n\log n$ time bound) and `convolution_main : ConvGoal`
  [S11:330–331] (one fixed bilinear program computes the convolution at
  the same bound); `sorry` at [S11:327] and [S11:331]. Declarations
  `OAI.PowerSaving.transform_main` and `OAI.PowerSaving.convolution_main`.

Both comparators carry `sorry`, but both configs have `main_results`
entries (the `UniformFourier` config carries two declarations), so the
challenges are registered as targets the release set itself with named
entry points. The reading is of source text only — no `lake` or `lean`
run elaborates the library, so the claim here is that the statements and
their `sorry` exist in the source, not that the declarations are proved.

## Coverage

The ledger row `fam=130` [S12] records: `tier=T3`, `paps=2`,
`paps_form=2`, `chal=2`, `mainres=2`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration level**
for both comparator configs (three declarations over the two configs).
Both manuscripts are formalized (`paps_form=2`). The shape flags are
`uniform`; `resolves_named=0` — the result is a superlinear saving, not a
resolution of a named conjecture; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3127], manuscript link [S1:3127] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 130 at [S2:337] |
| S3 | [`preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/main.tex`](../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/main.tex) | 57 | MS1 document root; abstract [S3:41–43]; five section `\input` directives plus a synthesis appendix [S3:44–50]; 57 lines |
| S4 | [`preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/sections/introduction.tex`](../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/sections/introduction.tex) | 160 | MS1 `thm:main` [S4:85–91], `cor:decimal` [S4:93–99]; 160 lines |
| S5 | [`preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf`](../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf) | 12925 | MS1 as shipped |
| S6 | [`lean/docs/130.md`](../../lean/docs/130.md) | 19 | scope note — Scope at [S6:10] (subsequential) and [S6:12] (uniform), comparator links at [S6:18–19] |
| S7 | [`preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/main.tex`](../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/main.tex) | 71 | MS2 document root; abstract [S7:51–59]; eight section `\input` directives [S7:61–68]; 71 lines |
| S8 | [`preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/sections/01-introduction.tex`](../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/sections/01-introduction.tex) | 263 | MS2 `thm:main` [S8:46–54]; 263 lines |
| S9 | [`preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf`](../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf) | 17794 | MS2 as shipped |
| S10 | [`lean/ComparatorChallenges/ExactFourier.lean`](../../lean/ComparatorChallenges/ExactFourier.lean) | 62 | comparator — `MainStatement` [S10:52–55], `main_theorem` [S10:57–58], `sorry` at [S10:58]; 62 lines |
| S11 | [`lean/ComparatorChallenges/UniformFourier.lean`](../../lean/ComparatorChallenges/UniformFourier.lean) | 336 | comparator — `transform_main` [S11:326–327], `convolution_main` [S11:330–331], `sorry` at [S11:327] and [S11:331]; 336 lines |
| S12 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=130`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
