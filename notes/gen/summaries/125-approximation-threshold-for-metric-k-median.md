[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 125](../index/theoretical-computer-science/125-approximation-threshold-for-metric-k-median.md)

# 125 — The approximation threshold for metric $k$-median

[Index page](../index/theoretical-computer-science/125-approximation-threshold-for-metric-k-median.md)

## Original CONTENTS.md summary

[S1:3038] (family entry):

> **125. The metric k-median approximation threshold and recovery.** Gives a deterministic polynomial-time $`(1+2/e+\varepsilon)`$-approximation for finite rational metric k-median with specified candidate facilities, for every fixed ε > 0. Assuming $`P\ne NP`$, the optimal infimum approximation factor is $`1+2/e`$. (Lean)

[S2:327] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**$`k`$-median** is a classic clustering problem. You have a set of clients
and a set of facility locations in a metric space. You must open at most
$`k`$ facilities and assign each client to its nearest open facility. The
goal is to minimize the total assignment cost.

The question is: **how good can an approximation algorithm be?** The
answer, for metric $`k`$-median with candidate facilities, is
**$`1+2/e \approx 1.736`$** — and this family proves it.

The second manuscript gives a deterministic polynomial-time algorithm that
achieves any factor above $`1+2/e`$ [S7:25–35]. The first manuscript provides
a randomized sub-two approximation $`(2-\sigma)`$ that feeds into the
derandomization [S4:142–155]. Together they establish that $`1+2/e`$ is the
**optimal** threshold: no polynomial-time algorithm can do better,
assuming $`P \ne NP`$ [S7:56–59].

This is a "meeting in the middle" result: the upper bound (algorithm) and
lower bound (hardness) meet at the same constant, closing a problem that
had lingered between factor 2.613 (best known approximation) and the
factor-3 barrier.

## Graduate summary

**Main theorem (deterministic approximation)** ([S7:25–35], `thm:main`).
"For every fixed $`\varepsilon>0`$, there is a deterministic algorithm which,
given a finite rational metric $`k`$-median instance with $`1\le k\le |F|`$,
returns $`S\subseteq F`$, $`|S|\le k`$, such that
$`\sum_{j\in J}d(j,S)\le(1+2/e+\varepsilon)\mathrm{OPT}_k`$. Its running time is
polynomial in the binary encoding length of the instance. The polynomial
may depend on $`\varepsilon`$" [S7:25–35].

**Hardness corollary** ([S7:56–59], `cor:threshold`). "If $`P\ne NP`$, the
infimum of deterministic polynomial-time approximation factors for metric
$`k`$-median with specified candidate facilities is $`1+2/e`$" [S7:56–59].
The gap reduction is from **Max-$`k`$-Coverage**: covered clients have
distance one, uncovered have distance at least three, and the connection
cost is exactly $`3m-2c`$ when the chosen sets cover $`c`$ elements
[S7:37–52].

**Refined recovery** ([S4:47–75], `ref:recovery`). "Let $`D`$ and $`F`$ be
disjoint indexed sets in a metric whose distances between distinct indices
are positive integers bounded by a fixed polynomial in
$`N=|D|+|F|`$. [...] Given $`S`$, $`\mu`$, $`L_0`$, and a failure parameter
$`\zeta\in(0,1)`$, a randomized algorithm returns
$`\widehat S\subseteq F`$ with $`|\widehat S|\le h`$ always and
$`\mathrm{cost}(\widehat S)\le(1+2/e+\varepsilon)P`$ with probability
at least $`1-\zeta`$" [S4:47–75]. The running time is single-exponential
in the allowed number of bad centers $`m\le L_0\log N`$
[S4:77–82].

**Global application** ([S4:142–155], `main:theorem`). "There is an
absolute constant $`\sigma>0`$ with the following property. For every fixed
$`a>0`$, a randomized polynomial-time algorithm for metric $`k`$-median always
returns a set $`S\subseteq F`$ with $`|S|\le k`$ and satisfies
$`\Pr\{\mathrm{cost}(S)\le(2-\sigma)\mathrm{opt}_k\}\ge
1-(|D|+|F|+2)^{-a}`$. The same algorithm can be chosen to satisfy
$`\mathbb E\mathrm{cost}(S)\le(2-\sigma)\mathrm{opt}_k`$"
[S4:142–155].

## History of the conjecture

Metric $`k`$-median approximations developed through LP rounding
(**Charikar, Guha, Tardos, Shmoys**), primal-dual and Lagrangian methods
(**Jain, Vazirani**), dual-fitting (**Jain et al.**), and bounded-swap
local search (**Arya et al.**) [S7:68–78].

**Li and Svensson** made constant-additive pseudo-approximations a route
past the factor-three barrier: a constant number of extra facilities can
be removed at an arbitrarily small additional approximation loss.
Subsequent bi-point rounding, including the corrected $`2.675+\varepsilon`$
guarantee of **Byrka et al.**, refined this approach. **Gowda et al.**
obtained $`2.613`$. **Cohen-Addad et al.** reached $`2+\varepsilon`$, first
announced in 2025. **Byrka et al.** subsequently developed a graph-based
iterative rounding framework that also gives $`2+\varepsilon`$ [S7:80–93].
The theorem here reaches every fixed factor above the $`1+2/e`$ hardness
boundary, which is strictly below all prior upper bounds
[S7:92–93].

**Prior (my training data, not this repo).** The best-known approximation
factors for metric $`k`$-median in 2025 were in the $`2+\varepsilon`$ range.
A deterministic algorithm achieving $`1+2/e+\varepsilon`$ together with a
matching $`P\ne NP`$ hardness is a major advance, essentially closing the
approximation threshold question for the candidate-facility model. I cannot
confirm the specific prior results independently; the release ships the
two manuscripts as proofs.

## Consequences

- **The approximation threshold is $`1+2/e`$.** For metric $`k`$-median with
  specified candidate facilities, the infimum of deterministic
  polynomial-time approximation factors is exactly $`1+2/e`$ under
  $`P\ne NP`$ [S7:56–59].
- **A deterministic algorithm achieves any factor above the threshold.**
  For every fixed $`\varepsilon>0`$, a polynomial-time algorithm achieves
  $`(1+2/e+\varepsilon)`$ [S7:25–35].
- **A randomized sub-two approximation feeds the derandomization.** The
  $`(2-\sigma)`$ global application on arbitrary finite rational metrics
  provides the input to the directed comparison inequality and potential
  framework [S4:142–155].
- **The gap reduction is from Max-$`k`$-Coverage.** The hardness is via a
  metric completion where covered clients have distance one and uncovered
  have distance three, yielding the exact $`3m-2c`$ cost structure
  [S7:37–52].
- **The result is for the candidate-facility model.** The lower bound
  does not apply to the unrestricted model where $`F=J`$ is the full point
  set [S7:63–64].

## Section skeleton

MS1 [S3] is a 39-line root: `\documentclass`, `\input{preamble}`, title
block, abstract [S3:9–20], `\tableofcontents`, `\clearpage`, then ten
section files [S3:24–33] and a `plain` bibliography. The sections, in
order and line count: `introduction` (276), `preliminaries` (128),
`local` (410), `sampling` (674), `completion` (579), `refinement` (406),
`imports` (633), `strictness` (249), `surplus` (231), `assembly` (206) —
3,792 section lines. The shipped PDF [S5] is the manuscript in the form
the release distributes.

MS2 [S6] is a 109-line root: a 60-line preamble with glyph mappings and
package declarations, title block, abstract [S6:91–95], seven section
files [S6:98–105], `\appendix` with a certificates section [S6:107], and
a `plainnat` bibliography [S6:108–109]. The sections, in order and line
count: `introduction` (196), `preliminaries` (104), `preparation` (526),
`inequality` (365), `rounding` (871), `derandomization` (585),
`certificates` (631) — 3,278 section lines. The shipped PDF [S8] is the
manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S9:10–16] and
**four** comparator stubs, with **one** `main_results` declaration.
This is the most complete formalization in the TCS queue so far.

The scope note [S9:10–16] describes three layers of formalized content:
[S9:10] the exact-budget recovery algorithm on polynomially bounded
integral metrics; [S9:12] the linked final approximation result on
arbitrary finite rational metrics; and [S9:14–16] the deterministic
$`(1+2/e+\varepsilon)`$-approximation and the $`P\ne NP`$ threshold.

The scope note links **four** comparator configs [S9:22–25]:

- `KMedianRecovery.lean` [S10] (107 lines) — `global_application`
  [S10:102–103], `sorry` at [S10:103]. This is the **only** comparator
  with a `main_results` entry: declaration
  `OAI.MetricKMedianRecovery.global_application` in
  `OAI/Combinatorics/KMedianRecovery/Main.lean`.
- `KMedianRefinedRecovery.lean` [S11] (167 lines) —
  `refined_recovery` [S11:153–163], `sorry` at [S11:163]. No
  `main_results` entry.
- `KMedianThreshold.lean` [S12] (107 lines) — `threshold`
  [S12:102–104], `sorry` at [S12:104]. No `main_results` entry.
- `MetricKMedian.lean` [S13] (68 lines) — `main_finite_work`
  [S13:59–62], `sorry` at [S13:62]. No `main_results` entry.

The one proved declaration (`global_application`) covers the randomized
$`(2-\sigma)`$ sub-two approximation on polynomially bounded integral
metrics. The three remaining comparators — the refined recovery, the
$`P\ne NP`$ threshold, and the deterministic approximation at the threshold —
have no proved declaration under `lean/OAI/`, so the formalization
incompletes at the challenge stubs for those three results.

The reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the stubs' statements and their
`sorry` exist in the source, and that one declaration's file exists, not
that anything is proved.

## Coverage

The ledger row `fam=125` [S14] records: `tier=T3`, `paps=2`,
`paps_form=1`, `chal=4`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **partially complete**: one of the
four comparator configs (`KMedianRecovery.lean`) carries a
`main_results` entry with declaration
`OAI.MetricKMedianRecovery.global_application`, so that one result is
formalized at the declaration level; the other three comparators
(`KMedianRefinedRecovery`, `KMedianThreshold`, `MetricKMedian`) have no
`main_results` entries. MS2 (the deterministic threshold) is the
formalized manuscript (`paps_form=1`). The shape flags are
`uniform|conditional`; `resolves_named=1` — the result establishes the
named $`1+2/e`$ threshold; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3038], manuscript link [S1:3038] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 125 at [S2:327] |
| S3 | [`preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/paper.tex`](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/paper.tex) | 39 | document root; abstract [S3:9–20]; ten `\input` directives [S3:24–33]; 39 lines |
| S4 | [`preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/sections/introduction.tex`](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/sections/introduction.tex) | 276 | `ref:recovery` [S4:47–75]; `main:theorem` [S4:142–155]; 276 lines |
| S5 | [`preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf`](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf) | 14138 | the manuscript as shipped |
| S6 | [`preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/main.tex`](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/main.tex) | 109 | document root; abstract [S6:91–95]; seven `\input` directives [S6:98–108]; 109 lines |
| S7 | [`preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/sections/introduction.tex) | 196 | `thm:main` [S7:25–35]; `cor:threshold` [S7:56–59]; 196 lines |
| S8 | [`preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf`](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf) | 15977 | the manuscript as shipped |
| S9 | [`lean/docs/125.md`](../../../lean/docs/125.md) | 25 | scope note — Scope at [S9:10–16], comparator links at [S9:22–25] |
| S10 | [`lean/ComparatorChallenges/KMedianRecovery.lean`](../../../lean/ComparatorChallenges/KMedianRecovery.lean) | 107 | comparator — `global_application` [S10:102–103]; 107 lines |
| S11 | [`lean/ComparatorChallenges/KMedianRefinedRecovery.lean`](../../../lean/ComparatorChallenges/KMedianRefinedRecovery.lean) | 167 | comparator — `refined_recovery` [S11:153–163]; 167 lines |
| S12 | [`lean/ComparatorChallenges/KMedianThreshold.lean`](../../../lean/ComparatorChallenges/KMedianThreshold.lean) | 107 | comparator — `threshold` [S12:102–104]; 107 lines |
| S13 | [`lean/ComparatorChallenges/MetricKMedian.lean`](../../../lean/ComparatorChallenges/MetricKMedian.lean) | 68 | comparator — `main_finite_work` [S13:59–62]; 68 lines |
| S14 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=125`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
