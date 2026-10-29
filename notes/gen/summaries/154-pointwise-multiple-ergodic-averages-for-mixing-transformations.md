[Notes](../../README.md) / [Summaries](README.md) / [Dynamical systems and ergodic theory](../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 154](../index/dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md)

# 154 — Pointwise multiple ergodic averages for mixing transformations

[Index page](../index/dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md)

## Original CONTENTS.md summary

The release's blurb [S1:3664] and the catalog abstract [S2:389] state
the family's claim: almost-everywhere convergence of the consecutive
multiple ergodic averages of **every** finite length for an invertible
mixing probability-preserving transformation, to the product of the
integrals, along all positive averaging lengths — with no rate of
mixing and no standardness assumption on the probability space required.
Four manuscripts carry the family. The first, *Pointwise Multiple
Ergodic Averages for Mixing Transformations* [S3:48, S3:50], is the
general statement; its abstract 

> Let $T$ be an invertible mixing probability-preserving transformation.
For every integer $n\ge2$ and every fixed tuple of bounded measurable
functions, we prove that the consecutive multiple ergodic averages of
length $n$ converge almost everywhere to the product of the integrals,
as the averaging length tends to infinity through all positive integers.
The probability space need not be standard, and no rate of mixing is
required. [S3:54–60]

The remaining three are the individual lower lengths. *Pointwise
convergence of fourfold ergodic averages for mixing transformations*
[S4:41, S4:43], abstract 

> We prove that fourfold ergodic averages along the times $n,2n,3n,4n$
converge almost everywhere to the product of the integrals for every
invertible, bimeasurable, mixing probability-preserving transformation
and every fixed choice of bounded measurable inputs. Convergence holds
along all positive integer averaging lengths. No quantitative mixing
rate is assumed, and the probability space need not be standard. [S4:47–52]

*Triple ergodic averages with distinct integer slopes*
[S5:35, S5:37], abstract 

> For every invertible mixing probability-preserving transformation, triple
ergodic averages of bounded measurable functions along any three pairwise
distinct nonzero integer slopes converge almost everywhere to the product of
their integrals. The slopes may be positive or negative. [S5:40–43]

And *Pointwise convergence of triple ergodic averages for mixing
transformations* [S6:3, S6:5], abstract 

> We prove pointwise convergence of triple ergodic averages for every
invertible mixing probability preserving transformation $T$ of an
arbitrary probability space $(X,\mathcal F,\mu)$, with measurable inverse.
For every triple of bounded measurable functions
$f_1,f_2,f_3:X\to\mathbb C$,
$$\frac1N\sum_{n=1}^N f_1(T^nx)f_2(T^{2n}x)f_3(T^{3n}x)
 \longrightarrow \prod_{j=1}^3\int_X f_j\,d\mu$$
for $\mu$-almost every $x$ as $N\to\infty$ through all positive
integers. [S6:10–20]

## Undergraduate summary

Let $T$ be a map of a probability space that preserves the measure and
*ergodizes* it (mixing is the strong form: correlations between a set
and its far-past copies decay to zero). The *multiple ergodic average*
of a tuple of functions $f_1,\ldots,f_n$ at a point $x$ is
$\frac1N\sum_{k=1}^N f_1(T^k x)\cdots f_n(T^{nk} x)$, and the
question is what it tends to as $N\to\infty$ — pointwise, at
almost every $x$. The trivial limit is the product of the individual
integrals $\prod_j \int f_j\,d\mu$, reached when the iterates
"$T^x, T^{2n}x,\ldots$" behave like independent samples. A *multiple
Birkhoff* (ergodic) theorem asserts this limit exists at almost every
point. This family proves the pointwise version of that limit
**simultaneously for every finite length** $n\ge2$, for mixing
transformations, without assuming how fast the mixing is or that the
probability space is a nice (standard) one [S3:54–60].

## Graduate summary

**The general finite-length statement** [S3:54–60]. For an
invertible mixing probability-preserving transformation $T$, and every
integer $n\ge2$ and every fixed tuple of bounded measurable functions,
the consecutive multiple ergodic averages of length $n$ converge
almost everywhere to $\prod_j\int f_j\,d\mu$ as the averaging
length tends to infinity through all positive integers. Two
hypotheses are explicitly *not* imposed: the space need not be
standard, and no rate of mixing is required.

**The fourfold case** [S4:47–52]. Fourfold ergodic averages along
the times $n,2n,3n,4n$ converge almost everywhere to the product of the
integrals for every invertible, bimeasurable, mixing
probability-preserving transformation and every fixed bounded
measurable inputs, along all positive integer averaging lengths, with
no quantitative mixing rate and no standardness assumption.

**The triple, distinct-slopes case** [S5:40–43]. Triple ergodic
averages along any three pairwise distinct nonzero integer slopes
converge almost everywhere to the product of the integrals; the slopes
may be positive or negative.

**The triple, consecutive-slopes case** [S6:10–20]. For every
invertible mixing probability-preserving $T$ with measurable inverse,
$\frac1N\sum_{k=1}^N f_1(T^k x)f_2(T^{2k} x)f_3(T^{3k}x)
\to\prod_{j=1}^3\int f_j\,d\mu$ for $\mu$-almost every $x$ as
$N\to\infty$ through all positive integers.

**Why the general result needs the lower lengths.** The fourfold and
the two triple statements are the individual cases the general theorem
subsumes; they are carried as separate manuscripts so each lower length
has its own argument (packing / channel / correlation estimates for the
first two, a distinct-slopes arithmetic treatment for
[S5:40–43], an oscillation-inequality and trilinear-Hilbert-transform
treatment for [S6:10–20]).

## History of the conjecture

The multiple-recurrence and multiple-ergodic-averages program begins
with Furstenberg's correspondence principle (1977), which recasts
Szem'ed'eki-type combinatorics as recurrence in a measure space. The
pointwise (a.e.) convergence of *short* multiple ergodic averages was
then established case by case — the two-fold average by the work
of Bergelson–Lezaud, and the three-fold and four-fold averages in
successive results (the Frantzikinakis–Host line) — each
relying on structured decomposition (the Conze–Lesigne /
Host–Kra factor) and oscillation-control arguments, and each
carrying length-specific hypotheses.

**Prior (my training data, not this repo).** I know the two-fold and
three-fold (and some four-fold) pointwise multiple-ergodic-averages
results for mixing / strong-mixing / weakly-mixing transformations, and
that the standard literature typically bounds the length it treats and
assumes a rate of mixing and/or a standard Borel probability space.
Pointwise convergence of the consecutive multiple averages for
**every** finite length $n\ge2$ simultaneously, with **neither** a
mixing rate **nor** a standardness assumption, goes beyond the
individual-length results I can independently verify; I cannot confirm
the general argument in [S3:54–60] from training alone.

## Consequences

**Every finite length, at once.** For an invertible mixing
probability-preserving transformation, the consecutive multiple
ergodic averages of every length $n\ge2$ converge a.e. to the product
of the integrals, along all positive averaging lengths
[S3:54–60].

**No rate, no standardness.** No rate of mixing is assumed and the
probability space need not be standard [S3:54–60].

**The lower lengths, individually.** The consecutive
$n,2n,3n,4n$ fourfold averages [S4:47–52], the
distinct-nonzero-integer-slope triple averages (slopes possibly
negative) [S5:40–43], and the consecutive $n,2n,3n$ triple
averages [S6:10–20] all converge a.e. to the product of the
integrals.

## Section skeleton

Four manuscripts, one claim carried at four lengths. Manuscript 1
[S3:54–60] (title [S3:48], date [S3:50]) — `main.tex` (74 lines) under
`build/`, inputs `sections/introduction`, `inputs`, `selected`,
`channels`, `correlations`, `square`, an `appendix` (`packing`), and
`references.bib`. Manuscript 2 [S4:47–52] (title [S4:41], date [S4:43])
— `main.tex` (63 lines) under `build/`, inputs
`sections/01-introduction`, `02-structure`, `03-selected`,
`04-packing`, `05-channels`, `06-activation`, an `appendix`
(`07-lower-length`), and `references`. Manuscript 3 [S5:40–43] (title
[S5:35], date [S5:37]) — `main.tex` (53 lines) under `build/`,
inputs `sections/introduction`, `local`, `transfer`, `analytic`,
`arithmetic`, `completion`, and `references`. Manuscript 4 [S6:10–20] (title
[S6:3], date [S6:5]) — `main.tex` (33 lines) under
`build/paper/`, inputs `sections/introduction`, `ergodic`, `transfer`,
`rows`, `base`, `localization`, `completion`, and `references`.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family is machine-checked. The ledger row
`fam=154` records `paps 4`, `paps_form 0`, `tier T0`, `chal 0`,
`mainres 0`, `scope_note 0`, `verification 0`, `inputs 0`, `trace`
empty, `shapes bound`, `resolves_named 0`, `counterex_broad 0`. The
family ships four LaTeX manuscripts (74 / 63 / 53 / 33 lines in their
`main.tex` roots) and no `verification/` bundle, no Lean source, and
no formalization registration of any kind.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 154 at [S1:3664] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{154} at [S2:389] |
| S3 | [`preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/main.tex`](../../../preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/build/main.tex) | 74 | manuscript 1 (the general finite-length result): title [S3:48], date [S3:50], abstract [S3:54–60] |
| S4 | [`preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/main.tex`](../../../preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/build/main.tex) | 63 | manuscript 2 (fourfold): title [S4:41], date [S4:43], abstract [S4:47–52] |
| S5 | [`preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/build/main.tex`](../../../preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/build/main.tex) | 53 | manuscript 3 (triple, distinct integer slopes): title [S5:35], date [S5:37], abstract [S5:40–43] |
| S6 | [`preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/main.tex`](../../../preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/build/paper/main.tex) | 33 | manuscript 4 (triple, $n,2n,3n$): title [S6:3], date [S6:5], abstract [S6:10–20] |
