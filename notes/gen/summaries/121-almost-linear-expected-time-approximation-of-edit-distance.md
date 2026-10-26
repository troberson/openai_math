[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 121](../index/theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md)

# 121 — Almost-linear expected-time approximation of edit distance

[Index page](../index/theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md)

## Original CONTENTS.md summary

[S1:2963] (family entry):

> **121. Almost-linear approximation of edit distance.** For every fixed rational $`\varepsilon\in(0,1)`$, gives a randomized $`(1+\varepsilon)`$ approximation to unit-cost edit distance in worst-case expected time $`N^{1+o(1)}`$, with success probability at least 2/3. The strings have total length N and polynomially bounded integer symbols. This is an asymptotic guarantee at fixed accuracy. ([Lean](../../../lean/docs/121.md))

[S2:320] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Edit distance** is the minimum number of single-character insertions,
deletions, and substitutions that turn one string into another. It is the
basic similarity measure in string comparison — used for spell-checking,
DNA alignment, and diffing. The classical algorithm is a dynamic
program, the **Wagner–Fischer** recurrence, which fills an $n \times m$
table in $O(nm)$ time.

The open problem for decades was to do it faster. This family gives an
**approximation algorithm**. For any fixed accuracy $\varepsilon \in (0,1)$,
a **uniform randomized** algorithm estimates the edit distance between
two strings of total length $N$ within a factor $1+\varepsilon$ — that is,
it returns a number $\widehat D$ with the true distance between $\widehat D$
and $(1+\varepsilon)\widehat D$ — with probability at least $2/3$, in
worst-case **expected** time $N^{1+o(1)}$ [S4:13–26]. That is essentially
**linear** time.

Three caveats are stated up front, and they matter. First, the guarantee
is **expected** over the algorithm's internal randomness, not on every
execution. Second, it is an **asymptotic** statement at fixed accuracy:
the constants and the input-size threshold may depend on $\varepsilon$, and
no polynomial dependence on $1/\varepsilon$ is claimed. Third, the
algorithm supports polynomially bounded **integer** symbols, not just
fixed-size alphabets, and returns exactly zero on equal strings
deterministically. The output is a distance estimate only — no
edit script is reconstructed.

## Graduate summary

**Main theorem (almost-linear approximation)** ([S4:13–26],
`thm:main`). "There is one uniform randomized algorithm that, given
$x,y$ and a rational $\varepsilon\in(0,1)$, returns a nonnegative integer
$\widehat D$ such that
$\Pr[\mathrm{ED}(x,y)\le \widehat D\le(1+\varepsilon)\mathrm{ED}(x,y)] \ge \frac23$.
For every fixed rational $\varepsilon$, its worst-case expected running
time on strings of total length $N$ is $N^{1+o(1)}$ as $N\to\infty$ on
the logarithmic-word RAM. The expectation is over internal randomness
only, and the bound includes input processing, preprocessing, numerical
work, random sampling and all data-structure operations. Equal strings
return zero deterministically" [S4:13–26]. The program is uniform in the
accuracy input, and the asymptotic assertion is pointwise in each fixed
rational accuracy — the constants and the threshold may depend on
$\varepsilon$ [S4:28–33]. The algorithm uses exact computation below an
accuracy-dependent input-length threshold [S4:35–38].

**Scope (formalization)** ([S5:7–11]). "The formalization gives a
randomized $(1+\varepsilon)$-approximation for unit-cost edit distance
between explicitly stored integer strings, for every fixed rational
$0<\varepsilon<1$. Its estimate is at least the true distance and at most
$(1+\varepsilon)$ times it with probability at least $2/3$; equal strings
return zero on every execution. For total length at most $N$ and integer
symbols bounded by a fixed polynomial in $N$, expected work is at most
$(N+2)^{1+\eta}$ for every fixed $\eta>0$ and all sufficiently large
$N$. Space is polynomially bounded on every execution" [S5:7–11]. The
manuscript's $N^{1+o(1)}$ is here made explicit as
$(N+2)^{1+\eta}$ for every fixed $\eta>0$.

## History of the conjecture

Edit distance originates in the study of errors in transmitted strings,
including **Levenshtein's** binary codes for insertions, deletions, and bit
flips [S4:41–42]. The dynamic program of **Wagner and Fischer** (1974)
computes the minimum cost of insertions, deletions, and substitutions in
quadratic time [S4:43–45].

**Prior (my training data, not this repo).** The edit-distance
approximation literature is large: for constant-alphabet strings,
several $(1+\varepsilon)$-approximation schemes with near-linear worst-
case time exist (e.g. the Abbasi–Tiskin line of work); the long-standing
difficulty is extending near-linear guarantees to arbitrary symbol
alphabets, where the input size is dominated by the symbol values. The
asymptotic $N^{1+o(1)}$ expected-time bound with polynomially bounded
integer symbols is consistent with that frontier. I cannot confirm the
specific prior results independently; the release ships the manuscript as
a proof.

## Consequences

- **Almost-linear edit-distance approximation.** A uniform randomized
  algorithm estimates unit-cost edit distance within a factor
  $1+\varepsilon$ with probability at least $2/3$ in worst-case expected
  time $N^{1+o(1)}$ for every fixed rational $\varepsilon\in(0,1)$
  [S4:13–26].
- **Explicit work bound.** For total length at most $N$ and integer
  symbols bounded by a fixed polynomial in $N$, expected work is at most
  $(N+2)^{1+\eta}$ for every fixed $\eta>0$ and all sufficiently large
  $N$; space is polynomially bounded on every execution [S5:11].
- **Integer alphabets.** The guarantee holds for polynomially bounded
  integer symbols, not only fixed-size alphabets [S4:13–26].
- **Deterministic zero.** Equal strings return exactly zero on every
  execution [S4:13–26].
- **Asymptotic, not near-linear-constant.** The bound is pointwise in the
  fixed accuracy; no polynomial dependence on $1/\varepsilon$ and no
  joint bound as the accuracy varies with $N$ is asserted
  [S4:28–33].

## Section skeleton

The root [S3] is a 31-line file: `\documentclass`, `\input{macros.tex}`
[S3:2], the title block, the abstract [S3:8–16], a table-of-contents
page, then ten section files [S3:19–28] and a bibliography. The sections,
in order and line count: `01-introduction` (203), `02-geometry` (194),
`03-seed` (342), `04-cones` (269), `05-bands` (388), `06-comparison`
(329), `07-regret` (398), `08-accuracy` (184), `09-numerics` (215),
`10-work` (501) — 3,023 section lines. The shipped PDF [S7] is the
manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note [S5:7–11]
and one comparator stub [S6], but **no** `main_results` declaration. This
is a structural absence: the scope note links a comparator config, and
that config has no proved declaration in `lean/OAI/`.

The `EditApproximation.lean` comparator stub [S6] is a 19,169-line file
— by far the largest in this family set — carrying the full physical-
table, band, and workload machinery for the approximation algorithm. Its
single top-level statement,
`theorem almostLinearEditDistanceRawBand` [S6:19146], conjoins the four
guarantees: the $2/3$-probability $(1+\varepsilon)$ bound, the
deterministic-zero case for equal strings, the expected-work bound at most
$(N+2)^{1+\eta}$, and the polynomially bounded space on every outcome.
It closes with `sorry` [S6:19166]. There is no `OAI/**` declaration that
proves it, so the formalization stops at the challenge stub.

The reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the stub's statement and its
`sorry` exist in the source, not that anything is proved.

## Coverage

The ledger row `fam=121` [S8] records: `tier=T2`, `paps=1`,
`paps_form=0`, `chal=1`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the scope note links
the `EditApproximation.lean` comparator config, but that config has no
`main_results` entry and no proved declaration — a T2 structural absence.
The shape flags are `bound|uniform`; `resolves_named=0` — the result is an
asymptotic time bound for an approximation scheme, not a resolution of a
named conjecture; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:2963], manuscript link [S1:2963] |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | the release's `\resultentry` list — 121 at [S2:320] |
| S3 | [`preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/paper.tex`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/paper.tex) | 31 | document root; abstract [S3:8–16]; eleven `\input` directives [S3:2–28]; 31 lines |
| S4 | [`preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/sections/01-introduction.tex) | 203 | `thm:main` [S4:13–26]; context [S4:40–55]; 203 lines |
| S5 | [`lean/docs/121.md`](../../../lean/docs/121.md) | 17 | scope note — Scope at [S5:7], comparator link at [S5:17] |
| S6 | [`lean/ComparatorChallenges/EditApproximation.lean`](../../../lean/ComparatorChallenges/EditApproximation.lean) | 19169 | the comparator — `theorem almostLinearEditDistanceRawBand` [S6:19146], `sorry` at [S6:19166]; 19,169 lines |
| S7 | [`preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf) | 16524 | the manuscript as shipped |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 373 | the ledger row `fam=121`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
