[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 127](../index/theoretical-computer-science/127-asymptotic-gotsman-linial-conjecture.md)

# 127 — The asymptotic Gotsman–Linial conjecture

[Index page](../index/theoretical-computer-science/127-asymptotic-gotsman-linial-conjecture.md)

## Original CONTENTS.md summary

[S1:3070] (family entry):

> **127. Average sensitivity of polynomial threshold functions.** Proves that a degree-at-most-d polynomial threshold function on the uniform n-dimensional Boolean cube has average sensitivity at most $`8d\sqrt n`$, uniformly for $`1\le d\le n`$. Average sensitivity counts expected output changes under single-bit flips. This establishes the asymptotic Gotsman–Linial conjecture, allowing polynomial zeros with $`\mathop{\mathrm{sign}}\nolimits (0)=1`$. ([Lean](../../../lean/docs/127.md))

[S2:331] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Average sensitivity** measures how "unstable" a Boolean function is. For
a function $f$ on an $n$-bit input, count how often flipping a single
random bit changes the output, then average over all bits. This is the
**average sensitivity** (or **total influence**) $I(f)$.

A **polynomial threshold function** (PTF) is the sign of a polynomial. For
example, "do the majority of the bits equal 1?" is the sign of
$x_1+\cdots+x_n$.

**Gotsman and Linial** conjectured that degree-$d$ PTFs have average
sensitivity at most on the order of $d\sqrt n$. This family proves an
explicit version: **$I(f) \le 8d\sqrt n$** [S4:20–28], for every
degree-at-most-$d$ real multilinear polynomial, on the uniform $n$-dimensional
Boolean cube. The constant 8 is absolute — it does not depend on $d$ or
$n$, so the degree may grow with the dimension.

This establishes the **asymptotic** form of the conjecture. The *exact*
extremal version (which function maximizes influence) is a separate,
harder question — and it is false, as **Chapman** showed
[S4:34–42].

## Graduate summary

**Main theorem** ([S4:20–28], `thm:main`). "Let $n\ge1$ and
$1\le d\le n$ be integers. Let $p$ be a real multilinear polynomial of
degree at most $d$, and define $f:\{-1,1\}^n\to\{-1,1\}$ by
$f(x)=\mathrm{sgn}(p(x))$, with $\mathrm{sgn}(0)=1$. Then, for average sensitivity under
the uniform law, $I(f)\le 8d\sqrt n$" [S4:20–28]. The convention
$\mathrm{sgn}(0)=1$ is load-bearing: it lets the polynomial vanish on the cube
without a regularity condition [S4:30–32].

**Asymptotic vs. exact.** "Gotsman and Linial proposed an exact extremal
bound for average sensitivity. Their candidate is symmetric: it is the
sign of a degree-$d$ polynomial in $x_1+\cdots+x_n$ whose roots lie between
the central levels of the cube. The proposal asserts that this function
maximizes influence among all degree-$d$ polynomial threshold functions in
$n$ variables. Chapman constructed counterexamples to this exact assertion
and explicitly distinguished it from the asymptotic bound
$I(f)=O(d\sqrt n)$" [S4:34–42]. The theorem here establishes the
asymptotic bound with an absolute constant "and makes no assertion about
exact maximizers" [S4:48–49].

**Sharpness.** The symmetric examples show the order $d\sqrt n$ is sharp
for $1\le d\le\sqrt n$: a sign function whose roots sit between the central
Hamming levels has influence $\asymp d\sqrt n$ [S4:53–78].

## History of the conjecture

**Gotsman and Linial** proposed the exact extremal bound in 1994.
**Chapman** constructed counterexamples to the exact assertion and
distinguished it from the asymptotic bound [S4:34–42]. **Kim, Maldonado,
and Wellens** independently constructed quadratic counterexamples for odd
$n\ge5$ and proved influence bounds for quadratic polynomials with
restricted support graphs [S4:44–47].

The early general bounds established sublinear influence for every fixed
degree. For $n>1$, **Harsha, Klivans, and Meka** proved
$I(f)\le 2^{O(d)}n^{1-1/(4d+6)}$, while the independent work of
**Diakonikolas, Raghavendra, Servedio, and Tan** gave
$I(f)\le 2^{O(d)}(\log n)n^{1-1/(4d+2)}$. Their proofs use regularity and
invariance arguments to compare sufficiently regular Boolean polynomials
with Gaussian ones [S4:81–90]. The theorem here gives the matching
$\tilde O(d\sqrt n)$ scale with a clean absolute constant.

**Prior (my training data, not this repo).** The Gotsman–Linial conjecture
was a central open problem in analysis of Boolean functions. The exact
extremal version was known to be false (Chapman's counterexamples), leaving
the asymptotic $O(d\sqrt n)$ bound as the target; an explicit constant
(8) with no regularity condition on the polynomial is a clean resolution of
the asymptotic form. I cannot confirm the specific prior results
independently; the release ships the manuscript as proof.

## Consequences

- **The asymptotic Gotsman–Linial bound is proved.** For every
  degree-at-most-$d$ real multilinear polynomial $p$ on the uniform
  $n$-cube, the average sensitivity of $\mathrm{sgn}\circ p$ (with
  $\mathrm{sgn}(0)=1$) is at most $8d\sqrt n$ [S4:20–28].
- **The constant is absolute and the degree may grow.** The 8 is
  independent of both $d$ and $n$, and the polynomial may vanish on the
  cube with no regularity condition [S4:30–32].
- **The exact extremal version is out of scope.** The theorem is the
  asymptotic bound, not the (false) exact maximizer claim; Chapman's
  counterexamples apply to the latter [S4:34–42].
- **The $d\sqrt n$ scale is sharp** for $1\le d\le\sqrt n$ via the
  symmetric central-level sign functions [S4:53–78].

## Section skeleton

The manuscript [S3] is a 76-line root: a 30-line preamble with glyph
mappings, title block, abstract [S3:62–66], six section files
[S3:69–74], and a `references` import [S3:75]. The sections, in order and
line count: `01-introduction` (172), `02-coupling` (62),
`03-weighted-grading` (103), `04-edge-recovery` (118),
`05-parity-coupling` (103), `06-consequences` (183) — 741 section lines.
The proof proceeds by a coupling argument, a weighted grading of the
function, an edge-recovery step, and a parity coupling, with the
consequences assembled at the end. The shipped PDF [S5] is the manuscript
in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S6:9],
one comparator stub [S7:43–47], and **one** `main_results` declaration — the
formalization is **complete at the declaration level**, in contrast to the
T2 structural-absence cases.

The scope note [S6:9] states precisely what is formalized and what is not:
"The formalized result proves the average-sensitivity bound $8d\sqrt n$
for every Boolean threshold function defined by a real multilinear
polynomial of degree at most $d$ on the $n$-dimensional cube. The sign
convention assigns value $1$ at zero. This establishes the stated
asymptotic bound, rather than the separate conjecture identifying exact
extremizers" [S6:9].

The scope note links a single comparator config [`GotsmanLinial.lean`]
[S6:15]. That config is the **only** one of the family's comparators with a
`main_results` entry: declaration
`OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement` in
`OAI/Combinatorics/GotsmanLinial/Main.lean`.

The `GotsmanLinial.lean` comparator stub [S7:43–47] (54 lines) defines the full
apparatus: `cubeCoord`, `flip`, `thresholdSign`, `sensitiveVertices`,
`averageSensitivity`, `IsMultilinear`, `polynomialValue`,
`polynomialThreshold`, and the statement

- `GotsmanLinialStatement` [S7:43–47] — for every $1\le d\le n$ and every
  multilinear $p$ of degree $\le d$,
  `averageSensitivity (polynomialThreshold p) ≤ 8 * d * sqrt n`;
  `gotsmanLinialStatement` [S7:49–50], `sorry` at [S7:50].

The comparator still carries a `sorry`, but unlike the T2 cases the
declaration `OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement` exists in
the library's `main_results` list, so the challenge is registered as a
target the release set itself with a named entry point. The reading is of
source text only — no `lake` or `lean` run elaborates the library, so the
claim here is that the statement and its `sorry` exist in the source, not
that the declaration is proved.

## Coverage

The ledger row `fam=127` [S8] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration level**:
the `GotsmanLinial.lean` comparator config carries a `main_results` entry
with declaration `OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement`. The
manuscript is formalized (`paps_form=1`). The shape flags are
`partial|uniform`; `resolves_named=0` — the result is the asymptotic bound,
not a resolution of the exact extremizer conjecture (which is false);
`counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3070], manuscript link [S1:3070] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 127 at [S2:331] |
| S3 | [`preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/main.tex`](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/main.tex) | 76 | document root; abstract [S3:62–66]; six section `\input` directives [S3:69–74]; 76 lines |
| S4 | [`preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/sections/01-introduction.tex`](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/sections/01-introduction.tex) | 172 | `thm:main` [S4:20–28]; 172 lines |
| S5 | [`preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf`](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) | 9822 | the manuscript as shipped |
| S6 | [`lean/docs/127.md`](../../../lean/docs/127.md) | 15 | scope note — Scope at [S6:9], comparator link at [S6:15] |
| S7 | [`lean/ComparatorChallenges/GotsmanLinial.lean`](../../../lean/ComparatorChallenges/GotsmanLinial.lean) | 54 | comparator — `GotsmanLinialStatement` [S7:43–47], `gotsmanLinialStatement` [S7:49–50]; 54 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=127`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
