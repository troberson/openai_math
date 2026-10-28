[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 104](../index/theoretical-computer-science/104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md)

# 104 — Quasipolynomial algorithms for mean-payoff, stochastic and parity games

[Index page](../index/theoretical-computer-science/104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md)

## Original CONTENTS.md summary

[S1:2579] (family entry):

> **104. Quasipolynomial algorithms for mean-payoff, stochastic and parity games.** Gives deterministic algorithms using $`2^{O((\log(L+2))^2)}`$ bit operations, for complete binary input length $L$, for ordinary mean-payoff games and two separate extensions. They compute exact values and optimal positional strategies in ordinary games, the nonnegative expectation-of-liminf value set in turn-based stochastic games, and the winning set for nonnegative liminf mean payoff conjoined with parity. Signed rewards, rational chance probabilities, and parity priorities are unrestricted and binary-encoded. (Lean)

The four manuscripts under that family:

[S1:2586] (turn-based stochastic):

> Turn-Based Stochastic Mean-Payoff Games in Deterministic Quasipolynomial Time

[S1:2595] (mean-payoff parity):

> Mean-payoff parity games in quasipolynomial time

[S1:2604] (deterministic):

> Deterministic quasipolynomial-time mean-payoff games

[S1:2613] (randomized):

> Randomized quasipolynomial-time mean-payoff games

[S2:286] carries the `\resultentry`, so the release blurb and the overview agree to
the word on the $2^{O((\log(L+2))^2)}$ bound.

## Undergraduate summary

A **mean-payoff game** is a two-player game on a finite directed graph. Each
vertex belongs to Max or Min, who picks the next edge, and each edge carries an
integer weight. A play is an infinite walk, and its payoff is the long-run
average weight — the liminf of the running average [S4:24–26]. The decision
question is *who can enforce a nonnegative average*: a start is in the zero-
threshold winning set $U$ if Max has a strategy such that every play it forces
has nonnegative liminf average.

What this family delivers is a **quasipolynomial** bound on the length of the
binary input, not on the size of the weights. That distinction is the whole
point: an algorithm polynomial in the *values* of the weights can be exponential
in the *input length*, because a $b$-digit weight has value up to $2^b$. The
bound is $2^{O((\log(L+2))^2)}$ bit operations for complete binary input length
$L$ — the exponent is a square of a logarithm, slower than any polynomial but
faster than $2^{L^{\epsilon}}$ for fixed $\epsilon>0$.

The family is four results on one theme. The deterministic game computes the
whole winning set, and a reduction recovers the exact rational value at every
vertex and optimal positional strategies [S4:34–50]. The randomized variant
computes the same set with probability at least $7/8$ on every random tape, and
a polynomial-time check certifies the answer so repetition turns it into an
always-correct expected-quasipolynomial algorithm [S6:36–53]. Two extensions
carry the bound: the **turn-based stochastic** game, where some vertices are
chosen by chance and the target is the expectation of the liminf average
[S10:49–59], and the **mean-payoff parity** game, where Max must also satisfy a
parity condition on the priorities visited infinitely often [S8:33–42].

## Graduate summary

**Deterministic** ([S4:34–50], `thm:main`). For a finite directed graph with
arbitrary signed binary edge weights, a uniform deterministic algorithm returns
exactly the zero-threshold winning set $U$ in at most
$2^{C(\log_2(L+2))^2}$ bit operations, including preprocessing, exact
arithmetic, recursion, and output [S4:35]. A reduction (`sec:full-solution`)
recovers the exact rational value at every vertex and globally optimal
positional strategies for both players within the same bound; `sec:energy-credits`
decides one-resource energy games and computes minimum winning credits, and
`sec:tropical` applies the classical reductions to tropical feasibility and
fixed-corank tropical rank.

**Randomized** ([S6:36–53]). A uniform randomized algorithm returns the same set
$U$ correctly with probability at least $7/8$; on every random tape its total
cost is at most $2^{C(\log_2(L+2))^2}$ bit operations [S6:37]. The certificate
is a polynomial-time check that validates the winning regions and positional
strategies or reports failure, so independent repetition gives an always-correct
algorithm with the same expected bound. The $7/8$ certificate line [S6:64] states
that a polynomial-time check certifies the winning regions and positional
strategies, and never accepts an incorrect output.

**Turn-based stochastic** ([S10:49–59]). Here the vertex set is partitioned into
Max, Min, and chance vertices, and the objective is the expectation of the
pathwise liminf mean payoff; the algorithm outputs exactly the nonnegative-value
set $U$ (including value zero) in the same quasipolynomial bound, using exact
rational arithmetic [S10:51].

**Mean-payoff parity** ([S8:33–42]). Max must force the conjunction that the
minimum priority visited infinitely often is even *and* the liminf average reward
is nonnegative [S8:20–26]. The reduction reuses the deterministic mean-payoff
theorem as a black box and runs $2^{O((\log(n+2))^2)}$ mean-payoff queries, each
on an arena of encoding length polynomial in $L$ [S8:34].

## History of the conjecture

The deterministic introduction [S4:35] situates the result against the standard
line. **Ehrenfeucht and Mycielski** proved the existence of positional optimal
strategies for mean-payoff games [S4:76]; positional determinacy places the
threshold problem in $\mathrm{NP}\cap\mathrm{coNP}$. **Zwick and Paterson**
developed the pseudopolynomial algorithms and the hardness reductions
[S4:78]. The companion randomized manuscript is the second half of the same
family [S4:132].

The parity manuscript builds directly on the deterministic result: its
algorithmic input is the deterministic theorem and its positional-strategy
corollary, and the novel content is the reduction from the parity-conjunction
objective to ordinary mean payoff, following the reduced-precision approach to
parity games [S8:50–53].

**Prior (my training data, not this repo).** Quasipolynomial algorithms for
parity games opened the door (Jurdziński) and the analogous mean-payoff result
was a long-standing open direction; the binary-weight (quasipolynomial in input
length, not weight magnitude) formulation is the strong form. I cannot confirm
these results independently; the release ships them as proofs, and the Lean
formalization reaches only a finite Truffet counterexample and the randomized
winning-set statement (see the comparison below).

## Consequences

- **The deterministic winning set, value, and strategies.** The whole
  zero-threshold winning set $U$, the exact rational value at every vertex, and
  globally optimal positional strategies for both players, in
  $2^{O((\log(L+2))^2)}$ bit operations [S4:34–50].
- **The randomized winning set with a certificate.** The same set with
  probability at least $7/8$ on every random tape, plus a polynomial-time check
  that makes repetition always correct [S6:36–53].
- **The stochastic extension.** The nonnegative expectation-of-liminf value set
  for turn-based stochastic games [S10:49–59].
- **The parity-conjunction extension.** The winning region for nonnegative
  liminf mean payoff conjoined with parity, reducing to ordinary mean payoff
  [S8:33–42].
- **Energy and tropical corollaries.** One-resource energy games with minimum
  winning credits [S4:55], and the tropical-feasibility / fixed-corank rank
  applications.

## Section skeleton

The four manuscripts are self-contained. The deterministic root [S3] includes
nine sections in the order [S3:20–28]: `01-introduction`, `02-boxes`,
`03-translations`, `04-algorithm`, `05-correctness`, `06-complexity`,
`07-values-and-strategies`, `08-energy-credits`, `09-tropical`. The randomized
root [S5:12] includes its sections in the order [S5:22–32]: `01-introduction`,
`02-boxes`, `03-budgets`, `04-algorithm`, `05-orientation`, `06-solving`,
`07-complexity`, then `08-conclusion` after a page break and `09-comparison` in
the appendix. The parity root [S7] includes five sections [S7:16–20]:
`01-introduction`, `02-arenas`, `03-strategies`, `04-algorithm`,
`05-complexity`. The stochastic root [S9] includes four sections
[S9:59–62]: `introduction`, `discount`, `labeling`, `application`.

The four shipped PDFs [S11] [S12] [S13] [S14] are the manuscripts in the form
the release distributes; the LaTeX under each `build/` tree is the working
source the page cites.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S15] and two
comparator stubs [S16:118] [S17:113]. Reading the scope note [S15] is the load-bearing
step: the formalization's two targets are *narrower* than the four manuscript
theorems.

The first target is a **finite counterexample to a proposed optimization step**.
The scope note states that the formalization "checks that a specified two-step
execution of Truffet's elimination procedure terminates with a feasible but
nonoptimal output. It is a finite counterexample to that proposed optimization
step." The stub [S16:118] carries exactly that: the selected statement
"$```lean
theorem finite_execution_not_optimal :
```
[S16:118]$" proves a two-step execution (`ForcedSingletonStep initial middle` then
`ForcedSingletonStep middle final`) reaches a feasible, stopped state whose
output cost is not minimal, and it ends in a `sorry`.

The second target is the **randomized winning-set algorithm**. The scope note
states that it "gives one randomized algorithm for the complete zero-threshold
winning set of every finite mean-payoff game with signed binary weights",
succeeding with probability at least $7/8$ in quasipolynomial bit time on every
random tape, allowing self-loops, parallel edges, and history-dependent
strategies. The stub [S17:113] carries the selected statement `"```lean
noncomputable def MainClaim : Prop := by
```
[S17:113]"`, which
exists a machine and a constant $C$ with an $O((\log(\text{input length}))^2)$
runtime and a $7/8$ correctness mass, and its `theorem randomized_quasipolynomial_mean_payoff`
ends in a `sorry`.

What is **not** formalized: the deterministic theorem [S4:34–50], the value and
positional-strategy reductions, the stochastic theorem [S10:49–59], and the
parity-conjunction theorem [S8:33–42] have no `main_results` entry in
`lean/formalization.yaml` for this family; the two declared entries are the
Truffet counterexample and the randomized statement only. A comparator stub is
a target the release set itself, not a proof — both end in `sorry`.

## Coverage

The ledger row `fam=104` [S18] records the tier and the counts: `tier=T3`,
`paps=4`, `paps_form=1`, `chal=2`, `mainres=1`, `scope_note=1`,
`verification=0`, `trace=`. The `paps_form=1` against `paps=4` is the coverage
signature of this family: one of the four manuscripts is named as a formalization
source, but the two `main_results` entries over that single config reach only the
Truffet counterexample and the randomized winning-set statement, not the other
three manuscript theorems. There is no verification bundle and no reasoning
trace. The shipped PDFs [S11] [S12] [S13] [S14] are the release-level evidence
for the four theorems; the Lean layer [S15] [S16:118] [S17:113] records the two
formalized targets.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2579] and the four manuscript entries [S1:2586], [S1:2595], [S1:2604], [S1:2613]. The release's inline code spans stay as backticked markdown, and the release's italic L is rendered as $L$ |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 104 at [S2:286] |
| S3 | [`preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex`](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex) | 31 | root (`\documentclass`); abstract [S3:8–15]; the nine-section include order [S3:20–28] |
| S4 | [`preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/sections/01-introduction.tex`](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/sections/01-introduction.tex) | 251 | the deterministic main theorem [S4:34–50]; the mean-payoff definition [S4:24–26] |
| S5 | [`preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex`](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex) | 35 | root (`\documentclass`); abstract [S5:8–17]; the section include order [S5:22–32] |
| S6 | [`preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/sections/01-introduction.tex`](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/sections/01-introduction.tex) | 261 | the randomized main theorem [S6:36–53]; the $7/8$ certificate line [S6:64] |
| S7 | [`preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/main.tex`](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/main.tex) | 23 | root (`\documentclass`); abstract [S7:8–15]; the five-section include order [S7:16–20] |
| S8 | [`preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/sections/01-introduction.tex) | 88 | the parity conjunction objective [S8:20–26]; the parity main theorem [S8:33–42] |
| S9 | [`preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/build/main.tex`](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/build/main.tex) | 69 | root (`\documentclass`); abstract [S9:50–58]; the four-section include order [S9:59–62] |
| S10 | [`preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/build/sections/introduction.tex`](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/build/sections/introduction.tex) | 197 | the stochastic main theorem [S10:49–59]; the value set $U$ [S10:51] |
| S11 | [`preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf`](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) | 14377 | the deterministic manuscript as shipped |
| S12 | [`preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf`](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) | 16269 | the randomized manuscript as shipped |
| S13 | [`preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf`](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf) | 12081 | the parity manuscript as shipped |
| S14 | [`preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf`](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf) | 12856 | the stochastic manuscript as shipped |
| S15 | [`lean/docs/104.md`](../../../lean/docs/104.md) | 19 | scope note — the formalization's Scope (the Truffet counterexample and the randomized winning-set algorithm) and its two comparator links |
| S16 | [`lean/ComparatorChallenges/TruffetCounterexample.lean`](../../../lean/ComparatorChallenges/TruffetCounterexample.lean) | 134 | the comparator stub — the two-step Truffet execution with its `sorry` |
| S17 | [`lean/ComparatorChallenges/RandomizedMeanPayoff.lean`](../../../lean/ComparatorChallenges/RandomizedMeanPayoff.lean) | 126 | the comparator stub — the randomized quasipolynomial claim with its `sorry` |
| S18 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=104`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
