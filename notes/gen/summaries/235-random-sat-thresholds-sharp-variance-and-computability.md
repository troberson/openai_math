[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 235](../index/probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md)

# 235 — Random-SAT thresholds, sharp variance and computability

[Index page](../index/probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md)

## Original CONTENTS.md summary

[S1:5664] (family entry):

> **235. Limiting random SAT thresholds, sharp variance and computability.** For random $`k`$-SAT with independent uniformly signed proper clauses sampled with replacement, proves finite positive limiting thresholds and hitting-time variance $`\Theta_k(n)`$ for every fixed $`k\ge3`$, and computability of the 3-SAT threshold. We credit Gaia Carenini with priority for resolving the threshold-existence conjecture in her concurrent ECCC TR26-229, made public October 5, 2026; this family supplies another proof and the sharper variance and computability results. ([Lean](../../../lean/docs/235.md))

[S2:555] carries the `\resultentry`, so the release blurb and the overview agree.
The four manuscripts:

**Fixed-clause-size threshold** [S3:3, S3:5]:

> For every fixed integer $`k\ge3`$, random $`k`$-SAT with independent
uniformly signed clauses on distinct variables, sampled with replacement,
has a finite positive limiting satisfiability threshold.
We credit Gaia Carenini with priority for
resolving the satisfiability conjecture. This paper gives an alternative
proof, using concentration of a capped last satisfiable index and a
comparison between different system sizes. [S3:9–17]

**3-SAT linear variance** [S4:31, S4:33]:

> For random 3-SAT on $`n`$ Boolean variables, with independent uniformly
signed clauses on three distinct variables sampled with replacement,
we prove that the first unsatisfiable prefix has variance $`\Theta(n)`$.
The upper bound removes the logarithmic loss in the earlier variance estimate;
the matching lower bound follows from Wilson's transition-width theorem. [S4:38–44]

**k-SAT variance** [S5:3, S5:5]:

> Let $`H_n`$ be the index of the first unsatisfiable prefix in random $`k`$-SAT
on $`n`$ variables, with independent uniformly signed clauses using $`k`$
distinct variables and sampled with replacement. For every fixed $`k\ge4`$,
we prove $`\mathrm{Var}(H_n)=\Theta_k(n)`$. For $`k=3`$, the variance is bounded below
by a positive multiple of $`n`$ and above by a constant multiple of $`n\log n`$;
the companion paper on random 3-SAT sharpens this to $`\Theta(n)`$.
The same upper bounds proved here hold after clipping at any fixed positive
multiple of $`n`$. [S5:8–17]

**3-SAT threshold computability** [S6:40, S6:42]:

> The limiting satisfiability threshold of uniform random 3-SAT is a
computable real. We credit Gaia Carenini 
with priority for resolving the satisfiability conjecture, which
establishes the threshold's existence. We prove that one finite
deterministic machine can approximate it to any prescribed accuracy. A deletion estimate gives
explicit lower certificates, while a finite hierarchical approximation
of the soft pressure gives upper certificates at every larger rational
density. A fair search through these certificates halts without
requiring a computable rate of finite-size convergence. [S6:45–55]

## Undergraduate summary

**Random SAT** asks: given many logical constraints (clauses) on
randomly chosen variables, is there an assignment that satisfies
them all? As the number of clauses grows relative to the number
of variables, the problem transitions from "always satisfiable"
to "always unsatisfiable." The **threshold** is the critical
ratio. This family proves the threshold exists for every fixed
clause size $`k\ge3`$, nails down the **variance** of the
hitting time (the number of clauses at which satisfiability
first fails), and shows the 3-SAT threshold is
**computable** — a deterministic machine can approximate
it to any desired precision [S3:9–17, S4:38–44,
S5:8–17, S6:45–55, S2:555].

## Graduate summary

**Fixed-clause-size threshold**
[S3:9–17, S2:555]. For every fixed integer
$`k\ge3`$, random $`k`$-SAT with independent uniformly
signed proper clauses sampled with replacement has a
finite positive satisfiability threshold $`\alpha_k`$:
the satisfiability probability tends to one for every
$`c<\alpha_k`$ and to zero for every $`c>\alpha_k`$
as the number of variables grows. The statement makes
no assertion at the threshold itself.

**3-SAT linear variance** [S4:38–44,
S2:555]. For the random 3-SAT hitting time $`H_n`$
(the first unsatisfiable prefix length), the variance
is $`\Theta(n)`$: a positive linear lower bound and
an $`O(n\log n)`$ upper bound. The same upper bounds
hold after clipping at any fixed positive multiple
of $`n`$.

**k-SAT variance** [S5:8–17, S2:555]. For
every fixed $`k\ge4`$, $`\mathrm{Var}(H_n)=\Theta_k(n)`$.
The positive linear lower bounds hold for sufficiently
high clipping levels.

**3-SAT threshold computability**
[S6:45–55, S2:555]. The limiting threshold
$`\alpha`$ for uniform random 3-SAT is a computable
positive real. One deterministic machine produces a
rational $`q_r`$ for every precision $`r`$ with
$`|q_r-\alpha|\le2^{-r}`$. No computable rate of
finite-size convergence is assumed.

## History of the conjecture

The **satisfiability threshold conjecture** for random
$`k`$-SAT has been open since the 1990s. The
**threshold existence** result [S3:9–17]
resolves it positively for every fixed $`k\ge3`$,
with priority to the concurrent Carenini [ECCC
TR26-229]. The **variance** results
[S4:38–44, S5:8–17]
go beyond existence to characterise the hitting
time's spread: linear for $`k\ge4`$, and a sharp
$`O(n\log n)`$ upper bound for $`k=3`$. The
**computability** result [S6:45–55]
shows the 3-SAT threshold is not just a real
number but a computable one, with an explicit
algorithm.

**Prior (my training data, not this repo).** The
random $`k`$-SAT problem, the threshold conjecture, and
the general framework are well-known. The threshold
existence for every $`k\ge3`$, the sharp variance
characterisation, and the computability result are
the novel contributions. I cannot confirm these
independently from training alone.

## Consequences

- **The threshold for every $`k\ge3`$**
  [S3:9–17]: a finite positive
  satisfiability threshold exists for random
  $`k`$-SAT with every fixed clause size.
- **The sharp variance**
  [S4:38–44, S5:8–17]: the hitting
  time variance is $`\Theta_k(n)`$ for $`k\ge4`$
  and has a positive linear lower bound and
  $`O(n\log n)`$ upper bound for $`k=3`$.
- **The computability**
  [S6:45–55]: the 3-SAT threshold is a
  computable positive real, with an explicit
  approximation algorithm.

## Section skeleton

Four manuscripts: [S3:9–17] (title [S3:3], date [S3:5])
— `paper.tex` under `build/source/`;
[S4:38–44] (title [S4:31], date [S4:33]) —
`main.tex` under `build/source/`;
[S5:8–17] (title [S5:3], date [S5:5]) —
`paper.tex` under `build/source/` with `sections/`;
[S6:45–55] (title [S6:40], date [S6:42]) —
`paper.tex` under `build/` with `sections/`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T2 with one
scope note [S7] and four comparator stubs [S8] [S9]
[S10] [S11], but **no** `main_results` entry and
**no** OAI tree. The scope note [S7:11–17]
states four targets: the threshold $`\alpha_k`$ for
every $`k\ge3`$; the variance $`\Theta_k(n)`$ for
$`k\ge4`$ and the $`k=3`$ linear/$`O(n\log n)`$ bounds;
the sharpness of the survival-lifetime and
clause-replacement estimates; and the computability
of the 3-SAT threshold.

The four comparator stubs carry the targets, each
with one `sorry`: [S8] (FixedClauseThreshold.lean),
[S9] (SATSharpness.lean), [S10] (SATVariance.lean),
[S11] (SATComputability.lean). No proved copy exists
under `lean/OAI/`. The gap is the formalization
itself: the release set the targets and created
challenge stubs, but did not produce a
`main_results` entry or an OAI proof. The reading
is of source text only — no `lake` or `lean`
run elaborates the proof.

## Coverage

The ledger row `fam=235` [S12] records the tier and
the counts: `tier=T2`, `paps=4`, `paps_form=0`,
`chal=4`, `mainres=0`, `scope_note=1`,
`verification=0`, `trace=`. The T2 shape: scope note
and comparator stubs exist, no formalization. The
single scope note covers all four manuscripts and
all four targets, but none is registered in
`main_results`. There is no verification bundle and
no reasoning trace. The shape flags are
`resolution|bound|uniform`, and `resolves_named=1`
— the blurb names the threshold-existence
conjecture with "resolving".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5664] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 235 at [S2:555] |
| S3 | [`preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/build/source/paper.tex`](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/build/source/paper.tex) | 28 | manuscript 1 of 4 (fixed-clause-size threshold); title [S3:3], date [S3:5], abstract [S3:9–17] |
| S4 | [`preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/build/source/main.tex`](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/build/source/main.tex) | 713 | manuscript 2 of 4 (3-SAT linear variance); title [S4:31], date [S4:33], abstract [S4:38–44] |
| S5 | [`preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/build/source/paper.tex`](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/build/source/paper.tex) | 31 | manuscript 3 of 4 (k-SAT variance); title [S5:3], date [S5:5], abstract [S5:8–17] |
| S6 | [`preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/build/paper.tex`](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/build/paper.tex) | 69 | manuscript 4 of 4 (3-SAT threshold computability); title [S6:40], date [S6:42], abstract [S6:45–55] |
| S7 | [`lean/docs/235.md`](../../../lean/docs/235.md) | 26 | scope note — the formalization's Scope at [S7:11–17] and its four comparator links at [S7:23–26] |
| S8 | [`lean/ComparatorChallenges/FixedClauseThreshold.lean`](../../../lean/ComparatorChallenges/FixedClauseThreshold.lean) | 56 | comparator stub — the threshold target with its `sorry` |
| S9 | [`lean/ComparatorChallenges/SATSharpness.lean`](../../../lean/ComparatorChallenges/SATSharpness.lean) | 78 | comparator stub — the sharpness target with its `sorry` |
| S10 | [`lean/ComparatorChallenges/SATVariance.lean`](../../../lean/ComparatorChallenges/SATVariance.lean) | 70 | comparator stub — the variance target with its `sorry` |
| S11 | [`lean/ComparatorChallenges/SATComputability.lean`](../../../lean/ComparatorChallenges/SATComputability.lean) | 50 | comparator stub — the computability target with its `sorry` |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=235`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
