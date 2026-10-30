[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 220](../index/probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md)

# 220 — Directional zero–one laws and ballisticity in random environments

[Index page](../index/probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md)

## Original CONTENTS.md summary

[S1:5195] (family entry):

> **220. Directional zero–one laws beyond iid environments and iid ballisticity.** On $`\mathbb Z^d`$, $`d\ge3`$, directional escape has probability zero or one for iid strictly elliptic nearest-neighbor environments, and for stationary ergodic finite-range-dependent environments under uniform ellipticity. In iid uniformly elliptic environments with $`d\ge2`$, almost-sure directional transience implies a deterministic limiting velocity with positive projection in that direction, resolving the ballisticity conjecture.

[S2:525] carries the `\resultentry`, so the release blurb and the overview agree. The family ships three manuscripts:

**Strict-ellipticity zero–one law** [S3:30, S3:32]:

> We prove the directional zero–one conjecture for nearest-neighbor random
walks in independent and identically distributed strictly elliptic environments
on $`\mathbb Z^d`$, $`d\ge3`$: the probability of escape in each fixed nonzero real
direction is zero or one. Only strict positivity of the transition probabilities
is required; no uniform lower bound or moment assumption is imposed. [S3:35–41]

**Transience implies ballisticity** [S4:22, S4:24]:

> We prove that almost-sure transience in a fixed direction implies a
deterministic limiting velocity with positive projection in that direction for
nearest-neighbor random walks in independent and identically distributed
uniformly elliptic environments on $`\mathbb Z^d`$, $`d\ge2`$. This resolves
the ballisticity conjecture positively. [S4:27–33]

**Finite-range-dependent zero–one law** [S5:31, S5:33]:

> We prove a directional zero–one law for uniformly elliptic nearest-neighbor
random walks in stationary, ergodic, finite-range-dependent environments on
$`\mathbb Z^d`$, $`d\ge3`$. For every fixed nonzero real direction, the probability
of escape in that direction, averaged over the environment, is either zero
or one. Finite-range dependence is imposed on the full transition rows:
collections of rows at distance greater than a fixed range are independent,
including collections indexed by infinite deterministic sets. [S5:36–44]

## Undergraduate summary

A **random walk in a random environment** is a path on the integer lattice
$`\mathbb Z^d`$ where at each step the walk chooses a direction with
probabilities that depend on a fixed random "landscape" (the environment)
[S3:35–41]. The **directional zero–one law** asks: for a fixed
direction, is the probability that the walk escapes to infinity in that
direction either zero or one (never in between)? The answer is **yes** for
iid strictly elliptic environments in dimension $`d\ge3`$ [S3:35–41],
and also for stationary ergodic environments with finite-range dependence
under uniform ellipticity [S5:36–44].

The **ballisticity conjecture** asks: if the walk is transient (keeps
moving) in some direction, does it travel at a constant speed in that
direction (a deterministic limiting velocity)? The answer is **yes** for
iid uniformly elliptic environments in dimension $`d\ge2`$
[S4:27–33].

## Graduate summary

**Strict-ellipticity zero–one law**
[S3:35–41, S2:525]. For nearest-neighbor random walks in
independent and identically distributed strictly elliptic environments
on $`\mathbb Z^d`$, $`d\ge3`$, the probability of escape in each fixed
nonzero real direction is zero or one. Only strict positivity of the
transition probabilities is required; no uniform lower bound or moment
assumption is imposed. The probability is the annealed law from the
origin.

**Transience implies ballisticity**
[S4:27–33, S2:525]. For nearest-neighbor random walks in
independent and identically distributed uniformly elliptic environments
on $`\mathbb Z^d`$, $`d\ge2`$, almost-sure transience in a fixed direction
implies convergence of $`X_n/n`$ to a deterministic velocity with
positive projection in that direction. This resolves the ballisticity
conjecture positively.

**Finite-range-dependent zero–one law**
[S5:36–44, S2:525]. For uniformly elliptic nearest-neighbor random
walks in stationary, ergodic, finite-range-dependent environments on
$`\mathbb Z^d`$, $`d\ge3`$, the annealed probability of escape in each
fixed nonzero real direction is zero or one. Finite-range dependence is
imposed on the full transition rows: collections of rows at distance
greater than a fixed range are independent, including collections
indexed by infinite deterministic sets.

## History of the conjecture

**The directional zero–one conjecture** for random walks in random
environments asks whether the escape probability in a fixed direction is
a tail event with probability zero or one. For iid uniformly elliptic
environments in $`d\ge3`$, this follows from the Hewitt–Savage
zero–one law and the ergodicity of the environment; the extension
to **strictly elliptic** (non-uniform) environments [S3:35–41]
removes the uniform lower-bound hypothesis. The **finite-range-dependent**
extension [S5:36–44] moves beyond iid to a broader class of
stationary ergodic environments.

**The ballisticity conjecture** asks whether directional transience
implies the existence of a limiting velocity. The result
[S4:27–33] resolves it positively for iid uniformly elliptic
environments in $`d\ge2`$, and the scope note [S6:10–21] records
that for $`d\ge3`$ positive probability of transience in any nonzero
direction already suffices, with the limiting velocity unique and the
unit directions with positive transience probability forming exactly
the open hemisphere with positive inner product with that velocity.

**Prior (my training data, not this repo).** The Hewitt–Savage
zero–one law, the quenched/annealed distinction, and the general
framework of random walks in random environments are standard. The
strict-ellipticity extension, the finite-range-dependent extension,
and the $`d\ge2`$ ballisticity resolution are the novel contributions.
I cannot confirm these results independently from training alone.

## Consequences

- **The strict-ellipticity zero–one law**
  [S3:35–41]: escape probability is zero or one for every fixed
  nonzero direction in iid strictly elliptic environments, $`d\ge3`$
  — no uniform ellipticity required.
- **The finite-range-dependent extension**
  [S5:36–44]: the same zero–one law holds for stationary
  ergodic finite-range-dependent environments under uniform ellipticity.
- **The ballisticity resolution**
  [S4:27–33]: directional transience implies a deterministic
  limiting velocity in iid uniformly elliptic environments, $`d\ge2`$.
- **The velocity-hemisphere structure**
  [S6:10–21]: for $`d\ge3`$, the transience directions form
  exactly the open hemisphere facing the limiting velocity.

## Section skeleton

Three manuscripts: [S3:35–41] (title [S3:30], date [S3:32]) —
`main.tex` under `build/`; [S4:27–33] (title [S4:22], date [S4:24])
— `main.tex` under `build/`; [S5:36–44] (title [S5:31],
date [S5:33]) — `main.tex` under `build/manuscript/`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note
[S6], three comparator stubs [S7] [S8] [S9], and one
`main_results` entry [S11]. The scope note [S6:10–21]
states three targets: the strict-ellipticity zero–one law,
the transience-implies-ballisticity claim, and the
positive-probability transience / velocity-hemisphere statement.

The `main_results` entry [S11:1195–1197] names
`OAI.DirectionalTransience.directional_transience_implies_ballisticity`
in `lean/OAI/Probability/Ballisticity/Main.lean`. In the source,
the theorem is stated and closed: "theorem
directional_transience_implies_ballisticity : MainStatement :=
by" [S10:25–27] calls
`directional_transience_implies_ballisticity_unit`. `grep` finds
**zero** `sorry` in the whole
`lean/OAI/Probability/Ballisticity/` tree.

The three comparator stubs carry the targets the release set
itself. `DirectionalWalk.lean` [S7] states
`directional_zero_one` [S7:85–88] and ends in `sorry`.
`DirectionalBallisticity.lean` [S8] states
`directional_transience_implies_ballisticity` [S8:95–96]
and ends in `sorry`. `VelocityHemisphere.lean` [S9]
carries the positive-probability transience and velocity-hemisphere
statement [S9:86–98] and ends in `sorry`. Only the
ballisticity claim has a proved copy under `lean/OAI/`; the
other two targets are stubs without a corresponding
`main_results` entry. A comparator stub is a target the
release set itself; the proved version, where it exists,
lives under `lean/OAI/`. The reading is of source text
only — no `lake` or `lean` run elaborates the proof.

## Coverage

The ledger row `fam=220` [S12] records the tier and the
counts: `tier=T3`, `paps=3`, `paps_form=1`, `chal=3`,
`mainres=1`, `scope_note=1`, `verification=0`, `trace=`.
The `paps_form=1` against `paps=3` is the coverage
signature: one of the three manuscripts is named as a
formalization source, and the single `main_results`
entry over that config reaches only the ballisticity
claim — the strict-ellipticity zero–one law
and the finite-range-dependent extension have no
formalization. The three comparator stubs name all
three targets, but only one has a proved copy. There is
no verification bundle and no reasoning trace. The shape
flags are `resolution|uniform`, and `resolves_named=1`
— the blurb names the ballisticity conjecture
with a resolve verb.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5195] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's \resultentry list — 220 at [S2:525] |
| S3 | [`preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/main.tex`](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/main.tex) | 54 | manuscript 1 of 3 (strict-ellipticity zero–one law); title [S3:30], date [S3:32], abstract [S3:35–41] |
| S4 | [`preprints/Directional-transience-implies-ballisticity-September-23-2026/build/main.tex`](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/build/main.tex) | 45 | manuscript 2 of 3 (transience implies ballisticity); title [S4:22], date [S4:24], abstract [S4:27–33] |
| S5 | [`preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/manuscript/main.tex`](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/manuscript/main.tex) | 197 | manuscript 3 of 3 (finite-range-dependent zero–one law); title [S5:31], date [S5:33], abstract [S5:36–44] |
| S6 | [`lean/docs/220.md`](../../../lean/docs/220.md) | 22 | scope note — the formalization's Scope at [S6:10–14] and its three comparator links at [S6:16–22] |
| S7 | [`lean/ComparatorChallenges/DirectionalWalk.lean`](../../../lean/ComparatorChallenges/DirectionalWalk.lean) | 92 | comparator stub — `directional_zero_one` at [S7:85–88] with its `sorry` |
| S8 | [`lean/ComparatorChallenges/DirectionalBallisticity.lean`](../../../lean/ComparatorChallenges/DirectionalBallisticity.lean) | 100 | comparator stub — `directional_transience_implies_ballisticity` at [S8:95–96] with its `sorry` |
| S9 | [`lean/ComparatorChallenges/VelocityHemisphere.lean`](../../../lean/ComparatorChallenges/VelocityHemisphere.lean) | 102 | comparator stub — the positive-probability transience and velocity-hemisphere statement at [S9:86–98] with its `sorry` |
| S10 | [`lean/OAI/Probability/Ballisticity/Main.lean`](../../../lean/OAI/Probability/Ballisticity/Main.lean) | 33 | the formalized file — `directional_transience_implies_ballisticity` proved at [S10:25–27] |
| S11 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming the declaration, at [S11:1195–1197] |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=220`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
