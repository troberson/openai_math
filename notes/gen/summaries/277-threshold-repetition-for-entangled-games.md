[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 277](../index/mathematical-physics/277-threshold-repetition-for-entangled-games.md)

# 277 — Threshold repetition for entangled games

[Index page](../index/mathematical-physics/277-threshold-repetition-for-entangled-games.md)

## Original CONTENTS.md summary

[S1:6972] (family entry):

> **277. Threshold repetition for entangled games.** Proves exponential threshold repetition for every finite two-player one-round game: if its entangled value is $`v<1`$, the probability of winning at least a fraction $`v+\delta`$ of $`k`$ independent repetitions decays exponentially in $`k`$, for $`0<\delta<1-v`$. Arbitrary joint finite-dimensional entangled strategies and correlated question distributions are allowed. ([Lean](../../../lean/docs/277.md))

[S2:645] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript:

**Threshold parallel repetition for finite-dimensional entangled games** [S3:25, S3:27]:

> For every finite two-player game with entangled value $`v<1`$, we prove
exponential decay for the probability of winning at least a $`v+\delta`$
fraction of $`k`$ independent repetitions, uniformly over all
finite-dimensional joint strategies. The result allows arbitrary correlated
question distributions and holds for every $`0<\delta<1-v`$ and $`k\ge1`$.
Its universal rate is proportional to
$`\delta^5/(1+\log(|\mathcal A||\mathcal B|))`$, where
$`\mathcal A,\mathcal B`$ are the answer alphabets. For each fixed question
distribution, we also obtain an explicit cubic rate in $`\delta`$. [S3:30–40]

## Undergraduate summary

An **entangled game** is a two-player game where the players can share
a quantum entangled state before receiving their questions, letting
them coordinate answers in ways that classical shared randomness
cannot. The **entangled value** is the best winning probability any
entangled strategy achieves. **Parallel repetition** asks: if you play
the game $`k`$ times independently, how fast does the probability of
winning *more than* a fraction $`v+\delta`$ of the rounds (when the
single-shot value is only $`v`$) decay? These results prove it decays
**exponentially** in $`k`$ — for every finite two-player game with
any correlated question distribution and any finite-dimensional
entangled strategy [S3:31–39]. This matters because it means
parallel repetition reliably amplifies the gap between a game's value
and any higher threshold, uniformly across all strategies.

## Graduate summary

**Exponential threshold parallel repetition**
[S3:31–39, S2:645, S4:9].
For every finite two-player one-round game with answer sets
$`A, B`$
and finite-dimensional entangled value
$`v < 1`$,
for
every
$`0 < \delta < 1 - v`$
and
every
$`k
\ge 1`$,
the probability that a joint finite-dimensional entangled strategy wins
at least the fraction
$`v + \delta`$
of $`k`$ independent repetitions is at most
$`\exp(-\kappa \delta^{13} k / (1 + \log(|A||B|)))`$
for
one
universal
$`\kappa > 0`$
[S4:9]. The bound applies uniformly to every joint finite-dimensional
strategy and to their supremum, without assuming attainment, and allows
arbitrary correlated question distributions [S4:9]. The manuscript also
proves a separate distribution-dependent cubic rate in $`\delta`$ for each
fixed question distribution [S3:37–39], which is **outside** the
formalized scope [S4:9].

## History of the conjecture

**Parallel repetition** for classical games follows from the Hägström
reduction (1992) and the constant factor of Ralph and Rudolph (2010).
The **quantum** and **entangled** settings resisted these arguments: the
players' shared quantum state correlates all $`k`$ rounds, so the
classical independence argument fails. The best prior results gave sub-
exponential rates or required restricted strategy classes. The
manuscript [S3:31–39] closes the gap: a universal exponential threshold
bound for every finite-dimensional entangled strategy, uniform in the
question distribution, with rate $`\delta^{13}`$ up to a logarithmic
factor in the answer-set sizes. A companion cubic rate for fixed
distributions improves the $`\delta`$ dependence at the cost of
distribution dependence.

**Prior (my training data, not this repo).** Entangled games, the
Tsirelson bound, and classical parallel repetition are standard in
quantum information and communication complexity. The universal
exponential threshold bound for arbitrary finite-dimensional entangled
strategies with correlated questions, at rate
$`\delta^{13}/(1+\log|A||B|)`$, and the companion cubic fixed-distribution
rate are the novel contributions. I cannot confirm these independently
from training alone.

## Consequences

- **The
universal exponential threshold bound**
  [S3:31–39, S2:645]:
for every finite two-player game with entangled value $`v<1`$, the
probability of winning at least a $`v+\delta`$ fraction of $`k`$ repetitions
decays exponentially in $`k`$, uniformly over all finite-dimensional
entangled strategies and correlated question distributions.
- **The
distribution-dependent cubic rate** [S3:37–39]: for each fixed question
distribution, an explicit cubic rate in $`\delta`$ (outside the formalized
scope).

## Section skeleton

One manuscript. [S3:30–40] (title [S3:25], date [S3:27]) — `main.tex` under
`build/`, with sections under `build/sections/`. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S4],
one comparator stub [S5], and one `main_results` entry [S7]. The scope
note links the single manuscript [S4:5] and records the formalized scope
[S4:9]: the exponential threshold parallel repetition bound for every
finite two-player game with arbitrary correlated questions, rate
$`\delta^{13}/(1+\log(|A||B|))`$, uniform over every joint finite-
dimensional strategy and to their supremum without assuming attainment.
The scope note is explicit that the **separate distribution-dependent
cubic bound is outside this scope** [S4:9] — the manuscript's second
rate [S3:37–39] is not formalized.

The `main_results` entry [S7:1223–1225] names
`OAI.ThresholdParallelRepetition.threshold_parallel_repetition` in
`lean/OAI/Probability/EntangledGames/Main.lean` (where the theorem
`threshold_parallel_repetition` is stated and closed at [S6:9]). `grep`
finds **zero** `sorry` in the whole
`lean/OAI/Probability/EntangledGames/` tree (30 `.lean` files).

The one comparator stub [S5] carries
`theorem threshold_parallel_repetition`
at [S5:64] with its `sorry` at [S5:74]. It is a `main_results`
registration. A comparator stub is a target the release set itself; the
proved version lives under `lean/OAI/`. The reading is of source text
only — no `lake` or `lean` run elaborates the proof.

## Coverage

The ledger row `fam=277` [S8] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `verification=0`, `trace=`. The `paps_form=1` against
`paps=1` is the coverage signature: the scope note links the manuscript
[S4:5], and the `main_results` entry [S7] reaches the proved theorem
[S6] in the zero-`sorry` OAI tree. The one caveat is scope-level: the
distribution-dependent cubic bound [S3:37–39] is outside the formalized
scope [S4:9]. The comparator stub [S5] carries one `sorry`. There is no
verification bundle and no reasoning trace. The shape flag is `uniform`,
and `resolves_named=1` — the blurb states a threshold repetition result
for every finite two-player game in a named-conjecture form.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6972] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 277 at [S2:645] |
| S3 | [`preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/build/main.tex`](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/build/main.tex) | 52 | manuscript (single); title [S3:25], date [S3:27], abstract [S3:31–39] |
| S4 | [`lean/docs/277.md`](../../../lean/docs/277.md) | 15 | scope note — links the manuscript [S4:5], the formalized threshold bound at [S4:9] (excluding the distribution-dependent cubic bound), and its comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/EntangledGames.lean`](../../../lean/ComparatorChallenges/EntangledGames.lean) | 80 | comparator stub — `theorem threshold_parallel_repetition` at [S5:64] with its `sorry` at [S5:74] (registered) |
| S6 | [`lean/OAI/Probability/EntangledGames/Main.lean`](../../../lean/OAI/Probability/EntangledGames/Main.lean) | 46 | the formalized file — `theorem threshold_parallel_repetition` at [S6:9] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry — `OAI.ThresholdParallelRepetition.threshold_parallel_repetition` at [S7:1223–1225] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=277`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
