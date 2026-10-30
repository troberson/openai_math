[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 229](../index/probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md)

# 229 — Sharp three- and four-state reconstruction thresholds

[Index page](../index/probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md)

## Original CONTENTS.md summary

[S1:5523] (family entry):

> **229. Exact three- and four-state reconstruction thresholds and four-state tree capacity.** Proves the exact reconstruction threshold $`d\lambda^2>1`$, with nonreconstruction at equality, for three-state symmetric and four-state ferromagnetic broadcasting on regular trees ($`d\ge2`$) and observed Poisson trees (mean $`d>1`$ and $`d>0`$, respectively), with Poisson advantage averaged without conditioning on survival. The three-state theorem allows both signs of $`\lambda`$ and gives the exact weak-recovery threshold for the symmetric three-community stochastic block model. ([Lean](../../../lean/docs/229.md))

[S2:543] carries the `\resultentry`, so the release blurb and the overview agree.
The three manuscripts:

**Four-state Potts threshold** [S3:37, S3:40]:

> We establish the exact Kesten–Stigum reconstruction threshold for the
ferromagnetic four-state Potts broadcast model on every regular $`d`$-ary
tree with $`d\ge2`$ and every Poisson Galton–Watson tree of mean $`d>0`$.
Reconstruction occurs exactly when $`d\lambda^2>1`$; we prove
nonreconstruction at and below the threshold, including equality.
In the Poisson model the whole tree is observed and the reconstruction
advantage is averaged without conditioning on survival. The proof uses
reproducible exact-arithmetic verification of polynomial inequalities. [S3:43–52]

**Four-state capacity criterion** [S4:27, S4:29]:

> For the ferromagnetic four-state broadcast model with $`0<\lambda<1`$,
we prove that reconstruction on a bounded-degree deterministic rooted
tree occurs exactly when its $`L^3`$ capacity with edge resistances
$`\lambda^{-2|e|}`$ is positive. This gives an exact criterion without
regularity or growth-rate assumptions on the tree, including at the
exponential critical boundary. [S4:34–41]

**Three-state symmetric threshold** [S5:3, S5:5]:

> We determine the exact reconstruction threshold for the symmetric
three-state broadcast process on every regular $`b`$-ary tree, $`b\ge2`$,
and every observed Poisson Galton–Watson tree of mean $`d>1`$.
Reconstruction occurs exactly when $`d\lambda^2>1`$, with $`d=b`$ in the
regular model; there is non-reconstruction at equality for either sign
of the channel parameter. The Poisson advantage is averaged over trees
and spins without conditioning on survival. This resolves the all-degree
three-state regular-tree prediction.
Combining the Poisson theorem with known tree-to-graph and algorithmic
results gives the exact weak-recovery threshold for the symmetric
three-community sparse stochastic block model with independent uniform
labels, fixed within- and between-community rates $`a,b>0`$, and mean
degree $`(a+2b)/3>1`$: recovery is possible exactly when
$`(a-b)^2>3(a+2b)`$. Above this threshold it is achievable in
$`O(n\log n)`$ time; at or below it, weak recovery is
information-theoretically impossible. [S5:8–25]

## Undergraduate summary

**Reconstruction on a tree** asks: if a signal is broadcast from the
root of a tree, noisily transmitted down each edge, and you can
observe all the leaves, can you recover the root value? The
**Kesten–Stigum threshold** is the critical noise level: above
it (the supercritical regime), the root can be reconstructed; below
it, no information survives. The condition is written in terms of
$`d`$ (the average number of children) and $`\lambda`$ (a channel
signal-to-noise parameter): reconstruction happens exactly when
$`d\lambda^2>1`$. This family pins this threshold for the
three-state and four-state spin models, including the exact
weak-recovery boundary for a three-community
community-detection problem [S3:44–51, S5:9–24, S2:543].

## Graduate summary

**Three-state symmetric threshold**
[S5:9–24, S2:543]. For the symmetric three-state
broadcast process on every regular $`b`$-ary tree ($`b\ge2`$)
and every observed Poisson Galton–Watson tree of mean
$`d>1`$, reconstruction occurs exactly when $`d\lambda^2>1`$,
with non-reconstruction at equality for **either sign** of
$`\lambda`$. The Poisson advantage is averaged over trees and
spins without conditioning on survival. Combining with
tree-to-graph and algorithmic results gives the exact
weak-recovery threshold for the symmetric three-community
sparse stochastic block model: recovery is possible exactly
when $`(a-b)^2>3(a+2b)`$, achievable in $`O(n\log n)`$
above it and information-theoretically impossible at or
below it.

**Four-state ferromagnetic Potts threshold**
[S3:44–51, S2:543]. The exact Kesten–Stigum
threshold for the ferromagnetic four-state Potts broadcast
model on every regular $`d`$-ary tree ($`d\ge2`$) and every
Poisson Galton–Watson tree of mean $`d>0`$:
reconstruction exactly when $`d\lambda^2>1`$, with
nonreconstruction at and below the threshold, including
equality. The whole tree is observed and the advantage
is averaged without conditioning on survival.

**Four-state capacity criterion** [S4:35–40,
S2:543]. For the ferromagnetic four-state broadcast model
with $`0<\lambda<1`$, reconstruction on a bounded-degree
deterministic rooted tree occurs exactly when its $`L^3`$
capacity with edge resistances $`\lambda^{-2|e|}`$ is
positive — an exact criterion with no regularity or
growth-rate assumptions, including at the exponential
critical boundary.

## History of the conjecture

The **Kesten–Stigum theorem** (1966) established the
reconstruction threshold $`d\lambda^2>1`$ for the
**binary** (two-state) broadcast channel. Extending it to
the **$`q`$-state** case for $`q\ge3`$ was a long-standing
open problem: the multi-state nonreconstruction side
requires controlling correlations between multiple
spin states, which the binary proof does not handle. This
family resolves the three-state
[S5:9–24] and four-state
[S3:44–51] thresholds, including the
equality (critical) case. The **stochastic block model**
connection [S5:9–24] translates the tree
threshold into the exact weak-recovery boundary for a
named community-detection problem. The
**capacity criterion** [S4:35–40] provides a
complementary deterministic-tree characterization via
electrical $`L^3`$ capacity.

**Prior (my training data, not this repo).** The
Kesten–Stigum theorem for the binary channel, the
general $`q`$-state open problem, and the
tree-to-graph translation for community detection are
standard. The exact three- and four-state thresholds
with the equality case, and the stochastic block model
consequence, are the novel contributions. I cannot
confirm these independently from training alone.

## Consequences

- **The exact three- and four-state thresholds**
  [S3:44–51, S5:9–24]: reconstruction
  exactly when $`d\lambda^2>1`$, with nonreconstruction
  at equality, for regular trees and observed Poisson
  trees.
- **The three-community stochastic block model**
  [S5:9–24]: the exact weak-recovery threshold
  $`(a-b)^2>3(a+2b)`$, with an $`O(n\log n)`$ algorithm
  above it and impossibility at/below.
- **The four-state capacity criterion**
  [S4:35–40]: a deterministic-tree
  reconstruction characterization via positive
  $`L^3`$ capacity, with no growth assumptions.

## Section skeleton

Three manuscripts: [S3:43–52] (title [S3:37], date [S3:40])
— `main.tex` under `build/` with
`references.tex`; [S4:34–41] (title [S4:27], date [S4:29])
— `main.tex` under `build/`; [S5:8–25] (title [S5:3],
date [S5:5]) — `main.tex` under `build/` with
`preamble.tex`. Two verification bundles ship: the
three-state bundle [S9] (`README.md`, `reproduce.py`,
`pair.py`, `grid.cpp`, `interval.cpp`) and the
four-state bundle [S10] (`checks/`, `review/`).

## Comparison with the formalized statement

The release formalises this family at tier T2 with one
scope note [S6] and two comparator stubs [S7] [S8],
but **no** `main_results` entry and **no** OAI tree.
The scope note [S6:9] states the target: the
**supercritical direction** of reconstruction for the
symmetric three-state channel
($`-1/2\le\lambda\le1`$) — reconstruction
when $`b\lambda^2>1`$ on a regular $`b`$-ary tree and
when $`d\lambda^2>1`$ on an observed Poisson tree of
mean $`d`$, with the root-estimation advantage
converging to a positive limit. [S6:11] records the
exclusion: "the selected statements cover
reconstruction above the Kesten–Stigum
threshold. Non-reconstruction at or below the
threshold and the stochastic-block-model
consequences in the paper are outside
them."

The two comparator stubs carry the targets, each with
two `sorry`: [S7] (supercritical regular/Poisson
reconstruction) and [S8] (above-threshold three-state
tree clauses). No proved copy exists under
`lean/OAI/`. The gap is the formalization itself: the
release set the supercritical target, wrote a scope
note, and created two challenge stubs with `sorry`,
but did not produce a `main_results` entry or an OAI
proof. The two verification bundles [S9] [S10] are
finite-arithmetic certificates, not theorem checks.
The reading is of source text only — no `lake`
or `lean` run elaborates the proof.

## Coverage

The ledger row `fam=229` [S11] records the tier and
the counts: `tier=T2`, `paps=3`, `paps_form=0`,
`chal=2`, `mainres=0`, `scope_note=1`,
`verification=2`, `trace=`. The T2 shape is "scope
note and comparator stubs exist, no
formalization": the release formalizes only the
supercritical three-state direction, and even that has
no `main_results` registration. The
nonreconstruction / equality side, the
stochastic-block-model consequence, and all four-state
theorems are outside the formalization. Two
verification bundles carry the finite-arithmetic
certificates. There is no reasoning trace. The shape
flags are empty, and `resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5523] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 229 at [S2:543] |
| S3 | [`preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/build/main.tex`](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/build/main.tex) | 62 | manuscript 1 of 3 (four-state Potts threshold); title [S3:37], date [S3:40], abstract [S3:44–51] |
| S4 | [`preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/build/main.tex`](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/build/main.tex) | 758 | manuscript 2 of 3 (four-state capacity criterion); title [S4:27], date [S4:29], abstract [S4:35–40] |
| S5 | [`preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/build/main.tex`](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/build/main.tex) | 43 | manuscript 3 of 3 (three-state symmetric threshold); title [S5:3], date [S5:5], abstract [S5:9–24] |
| S6 | [`lean/docs/229.md`](../../../lean/docs/229.md) | 18 | scope note — the formalization's Scope at [S6:9–11] and its two comparator links at [S6:17–18] |
| S7 | [`lean/ComparatorChallenges/ThreeStateSupercritical.lean`](../../../lean/ComparatorChallenges/ThreeStateSupercritical.lean) | 108 | comparator stub — the supercritical regular/Poisson reconstruction target with two `sorry` |
| S8 | [`lean/ComparatorChallenges/ThreeStateTreeClauses.lean`](../../../lean/ComparatorChallenges/ThreeStateTreeClauses.lean) | 104 | comparator stub — the above-threshold three-state tree clauses with two `sorry` |
| S9 | [`preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/verification/README.md`](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/verification/README.md) | 32 | the family 229 three-state verification bundle entry point — `README.md` alongside `reproduce.py` |
| S10 | [`preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/verification/checks/verify.py`](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/verification/checks/verify.py) | 127 | the family 229 four-state verification bundle entry point — `checks/verify.py` alongside `review/` |
| S11 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=229`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
