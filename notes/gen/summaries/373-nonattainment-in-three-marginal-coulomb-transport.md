[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 373](../index/partial-differential-equations/373-nonattainment-in-three-marginal-coulomb-transport.md)

# 373 — Nonattainment in three-marginal Coulomb transport

[Index page](../index/partial-differential-equations/373-nonattainment-in-three-marginal-coulomb-transport.md)

## Original CONTENTS.md summary

[S1:9002] (family entry):

> **373. Nonattainment of the three-marginal Coulomb Monge problem.** An optimal three-particle Coulomb configuration need not be a deterministic function of the first particle, even for smooth identical spatial densities. The Monge and Kantorovich infima agree, but the Monge infimum is not attained. The same phenomenon occurs for every inverse-power Riesz exponent in each dimension at least two, with a suitable density in each case. ([Lean](lean/docs/373.md))

[S2:850] carries the `\resultentry` with a single manuscript [S3].
The scope note states the formalized result:

> The Monge ansatz asks whether an optimal multi-marginal transport plan can be induced by maps from one marginal. For the three-marginal Coulomb cost in $`\mathbb R^3`$, the formalization constructs a smooth compactly supported probability density, with smooth compactly supported square root, for which no pair of measure-preserving Borel maps attains the Kantorovich minimum. [S4:9]

## Undergraduate summary

This is a result about **optimal transport** — the mathematics of
moving one distribution of mass into another as cheaply as possible.
The classical **Monge** version asks: is there a single map that sends
each point of the first distribution to a point of the second,
minimizing the total transport cost? The more flexible **Kantorovich**
version allows "splitting": a point can send part of its mass to
several destinations.

The **Monge ansatz** is the assumption that the cheaper, map-based
Monge answer is always available. This result shows the ansatz
**fails** in a multi-particle Coulomb setting: you have three
particles interacting through the Coulomb force, and the optimal way
to arrange them **cannot** be described as a deterministic function of
the first particle's position [S3:40–50, S4:9].

The striking part: the cheapest cost you can achieve with a map (the
Monge infimum) **equals** the cheapest cost with flexible splitting
(the Kantorovich infimum). So maps are *as good as possible* in the
limit — but no single map actually reaches that limit. The infimum is
approached by a sequence of maps, yet never attained by any one of
them [S3:40–50, S4:9].

## Graduate summary

**Main theorem (Monge nonattainment with equal infima)**
[S3:40–50, S1:9002, S4:9].
There is a smooth compactly supported probability density $`\`\rho``$
on $`\`\mathbb R^3`$`, with smooth compactly supported square root,
such that for the three-marginal Coulomb cost the Kantorovich
minimum is achieved by a three-coupling, but **no** pair of
measure-preserving Borel maps attains it: the Monge infimum is not
attained [S3:40–50, S4:9].

**Equality of the infima** [S3:40–50, S4:11].
The Monge and Kantorovich infima are equal: sequences of
measure-preserving maps with finite cost approach the Kantorovich
minimum [S4:11]. The phenomenon is that the value is the same in both
formulations, yet the map form has no minimizer.

**The stated exclusion** [S4:11].
This is the three-dimensional Coulomb result; "the paper's
inverse-power extensions in every dimension are **outside** this
statement." The Riesz-exponent generalization (every
inverse-power cost in every dimension at least two) is not the
formalized statement [S4:11].

**The formalization is T2, not T3** [S4, S5, S6].
The scope note [S4:9] and one comparator stub [S5] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S6]. The comparator stub `CoulombCounterexample.lean` (102 lines)
carries the three-particle/Coulomb-cost/monge-Kantorovich machinery
(`coulombCost`, `mongeValue`, `kantorovichValue`,
`HasCoulombCounterexample`) and states
`theorem coulomb_counterexample_and_equal_infima` [S5:94] with the
`sorry` at [S5:96] (1 in this stub). The T2 shape is "scope note plus
comparator stub, no `main_results` entry, no OAI tree."

## History of the conjecture

The **Monge problem** (Monge 1781) asks for an optimal transport map
between two probability measures. **Kantorovich** (1942) relaxed the
problem to allow couplings (general joint distributions), showing the
relaxed problem always has a solution. The question of when the
Monge and Kantorovich values coincide — and when a Monge *map*
attains the minimum — is a central one in optimal transport. For
two-marginal, convex-cost transport in one dimension, monotone maps
give the answer; in higher dimensions with non-convex costs, the
picture is subtler.

The **multi-marginal** setting (three or more marginals) is much less
understood than the two-marginal case. The classical results on
Monge nonattainment in multi-marginal transport are sparse, and the
**Coulomb** cost (the physically natural pairwise inverse-distance
interaction for charged particles) is a particularly important case.
Prior work by **Carrasco, McCann, and Shiffman** (2003) and
**Villani** (2008) laid the groundwork for multi-marginal and
Coulomb transport, and the **Kannan–Klartag** and related programs
explored nonconvex multi-marginal problems.

The **novel contribution** is the **sharp three-marginal Coulomb
nonattainment counterexample** [S3:40–50, S4:9]: a smooth
compactly supported density for which the Monge infimum is not
attained, together with the **equality of the Monge and Kantorovich
infima** [S4:11], and the extension to every inverse-power Riesz
exponent in every dimension at least two (the latter being outside
the formalized statement) [S4:11]. The proof uses a splitting
construction [S3:53], a locality argument [S3:54], a
**finite-arithmetic certificate** [S3:55] that certifies the key
inequalities, and a passage from the local counterexample to the
global infimum-equality statement [S3:56–57].

**Prior (my training data, not this repo).** As of my training
cutoff, multi-marginal optimal transport was a rapidly developing
area, and the existence of a sharp Coulomb-cost nonattainment
counterexample — showing that the Monge ansatz fails even for smooth
identical densities, while the infima remain equal — was at the
frontier of the multi-marginal transport program. I cannot verify the
transport estimates and the finite-arithmetic certificate
independently from training alone.

## Consequences

- **Monge nonattainment for the three-marginal Coulomb cost**
  [S3:40–50, S1:9002, S4:9]: a smooth compactly supported
  probability density in $`\`\mathbb R^3`$` for which no pair of
  measure-preserving Borel maps attains the Kantorovich minimum.
- **The Monge and Kantorovich infima agree** [S3:40–50, S4:11]:
  although no map attains the minimum, sequences of maps approach it,
  so the two infima are equal.
- **Smooth identical densities suffice** [S1:9002, S3:40–50]: the
  counterexample uses a smooth density (with smooth square root), not
  a pathological one.
- **The inverse-power Riesz extensions are outside the
  formalization** [S4:11]: the every-dimension, every-inverse-power
  generalization is stated in the manuscript but not part of the
  formalized statement.
- **The result is T2, a challenge not a proof** [S5, S6]: the
  comparator stub carries `theorem
  coulomb_counterexample_and_equal_infima` with a `sorry`
  [S5:96] and there is no `main_results` entry or OAI tree.

## Section skeleton

One manuscript, `build/paper.tex` root (62 lines). The root declares
the theorem environments and macros inline [S3:2–30], the title at
[S3:34], the date at [S3:37], the abstract at [S3:40–50], and 7
`input` files [S3:52–58]: `introduction`, `splitting`, `local`,
`certificate`, `proof`, `infima`, `riesz`, plus a BibTeX
`references`. **No verification bundles** in the ledger
(`verification=0`), though the `certificate` section [S3:55]
carries the manuscript's finite-arithmetic certificate.

## Coverage

The ledger row `fam=373` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=619`, `verification=0`, `trace=0`,
`companions=`. The T2 shape is "scope note plus comparator stub,
no `main_results` entry, no OAI tree." The single comparator stub
carries 1 `sorry` [S5:96]. The shape flags are
`shapes=density|uniform`, `resolves_named=0`, `counterex_broad=0`,
`covmd=0` — a **density**-type result (a smooth compactly supported
density counterexample) with a **uniform** character (uniform over
the inverse-power generalization). No named conjecture in the title,
no counterexample ledger tag (the counterexample is the manuscript's
construction, not the `counterex_broad` shape). The ledger's
`verification=0`: the family ships no finite-arithmetic certificate
bundle, even though the manuscript's `certificate` section [S3:55]
carries an in-text certificate. Note `paps_form=0`: the manuscript
does not appear in `formalization.yaml`'s `sources:` list, and there
is no `main_results` entry — the T2 formalization is the scope
note's description and the comparator's challenge only, with no
proved Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:9002] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 373 at [S2:850] |
| S3 | [`preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/build/paper.tex`](../../../preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/build/paper.tex) | 62 | the `\documentclass` root — 62 lines, title [S3:34], date [S3:37], abstract [S3:40–50], 7 `input` files [S3:52–58] |
| S4 | [`lean/docs/373.md`](../../../lean/docs/373.md) | 17 | scope note — names the single manuscript [S4:5]; Scope at [S4:9–11], comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/CoulombCounterexample.lean`](../../../lean/ComparatorChallenges/CoulombCounterexample.lean) | 102 | comparator stub — 102 lines, `def HasFullCoulombConclusion` [S5:88], `theorem coulomb_counterexample_and_equal_infima` [S5:94], `sorry` [S5:96] |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=373`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
