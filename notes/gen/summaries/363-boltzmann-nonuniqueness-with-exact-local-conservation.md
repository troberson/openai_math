[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 363](../index/partial-differential-equations/363-boltzmann-nonuniqueness-with-exact-local-conservation.md)

# 363 — Boltzmann nonuniqueness with exact local conservation

[Index page](../index/partial-differential-equations/363-boltzmann-nonuniqueness-with-exact-local-conservation.md)

## Original CONTENTS.md summary

[S1:8797] (family entry):

> **363. Nonuniqueness with local conservation for the hard-sphere Boltzmann equation.** Constructs two distinct global entropy solutions of the three-dimensional periodic hard-sphere Boltzmann equation from the same nonnegative initial density, with bounded velocity support and finite mass, energy and absolute entropy. Both are strongly continuous in <i>L</i><sup>1</sup> and satisfy exact local conservation of mass, momentum and kinetic energy. ([Lean](lean/docs/363.md))

[S2:828] carries the `\resultentry` with two manuscripts —
manuscript 1 [S3] (the local-conservation headline) and manuscript 2
[S4] (the periodic result). The scope note names **only** manuscript 2
[S5:5] and states the formalized result 

> The formalization proves nonuniqueness for the periodic hard-sphere Boltzmann equation by constructing two distinct global renormalized solutions on $`\mathbb T^3\times\mathbb R^3`$ with the same nonnegative initial density. The data have bounded velocity support and finite mass, energy, and absolute entropy. Both solutions conserve local mass and total momentum and satisfy the global energy and entropy-dissipation inequalities. [S5:9]

## Undergraduate summary

The **Boltzmann equation** describes how a gas of many particles
evolves: it tracks the density of particles at each position and
velocity, and how collisions change that density. A central question
in the theory is **uniqueness** — given an initial state, is there
only *one* way the gas can evolve?

This result says **no** in a strong form. It starts with an
initial density for a three-dimensional periodic gas of **hard
spheres** (particles that collide elastically when they touch) and
constructs **two different** long-time solutions from *exactly the
same* starting data — both well-behaved (finite mass, energy, and
"disorder"), both physically reasonable (they conserve mass,
momentum, and energy locally). So the equation genuinely does not
pick out a unique future from a given past.

The release formalizes the earlier version of this result (the
"periodic" one), which establishes the two-solution construction with
certain conservation laws. The headline manuscript [S3] is a later
refinement strengthening the conservation laws to *exact* local
conservation of mass, momentum, and kinetic energy — that refinement
is **not** the formalized statement.

## Graduate summary

**Formalized theorem (manuscript 2, the periodic result)**
[S4:8–17, S5:9].
There exist two distinct global **renormalized** solutions
$`f_0, f_1`$ of the three-dimensional periodic hard-sphere Boltzmann
equation on $`\mathbb T^3 \times \mathbb R^3`$ with the same
nonnegative initial density $`f_{\rm in}`$, the data having bounded
velocity support and finite mass, energy, and absolute entropy. Both
solutions conserve local mass and total momentum and satisfy the
global energy and entropy-dissipation inequalities; on a common
initial interval they are strongly continuous in $`L^1`$ with
integrable collision gains and losses [S5:9–11].

**Headline theorem (manuscript 1, the local-conservation
refinement)** [S3:9–18, S1:8797].
Two distinct global **entropy** solutions of the three-dimensional
periodic hard-sphere Boltzmann equation from the same nonnegative
initial density, with bounded velocity support and finite mass,
energy, and absolute entropy, strongly continuous in $`L^1`$ and
satisfying **exact local conservation of mass, momentum, and kinetic
energy** [S3:9–18].

**The formalization is T2, not T3** [S5, S6, S7].
The scope note [S5:9] and one comparator stub [S6] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S7]. The comparator stub `BoltzmannNonuniqueness.lean` (215 lines)
states `theorem nonuniqueness` [S6:204] with the `sorry` at [S6:209]
(1 in this stub), and the statement is left as a challenge, not
promoted to a proved declaration. The T2 shape is "scope note plus
comparator stub, no `main_results` entry, no OAI tree."

## History of the conjecture

The **hard-sphere Boltzmann equation** is the classical kinetic
model for a gas of rigid elastic collisions. Since DiPerna and
Lions's existence theory (1989), a major open problem has been
**uniqueness of renormalized solutions** — do weak (renormalized)
solutions determined by the same initial data agree for all time?
The **Dunlop–Machihara** and **Dunlop–Pareschi** programs and the
classical **Dunlop** nonuniqueness attempts probed this for
various collision kernels.

The **novel contribution** is a **genuine nonuniqueness
construction** [S3, S4]: two distinct global solutions from the
same initial data, both satisfying the physically natural
conservation laws. Manuscript 2 [S4] establishes the construction
with the renormalized-solution conservation structure (local mass,
total momentum, energy and entropy-dissipation inequalities)
[S5:9]. Manuscript 1 [S3] refines the conservation laws to **exact
local** conservation of mass, momentum, and kinetic energy — the
stronger statement the catalog headline describes [S1:8797]. The
gap between the two is precisely what the scope note excludes:
"later local-conservation refinements are outside it" [S5:11].

**Prior (my training data, not this repo).** As of my training
cutoff, uniqueness of renormalized/entropy solutions of the
three-dimensional hard-sphere Boltzmann equation was an open
problem, and a published two-solution nonuniqueness construction
with exact local conservation was not, to my knowledge, established.
The construction of two distinct global solutions from identical
data is the claimed novelty. I cannot verify the kinetic-theoretic
construction independently from training alone.

## Consequences

- **Nonuniqueness of global solutions to the 3D periodic
  hard-sphere Boltzmann equation** [S4:8–17, S5:9]: two distinct
  global solutions arise from the same nonnegative initial density.
- **The formalized conservation structure is the renormalized one**
  [S5:9]: the two solutions conserve local mass and total momentum
  and satisfy the global energy and entropy-dissipation
  inequalities, with $`L^1`$ strong continuity on a common initial
  interval.
- **The headline's exact local conservation is the unproved
  refinement** [S3:9–18, S5:11]: exact local conservation of mass,
  momentum, and kinetic energy is the manuscript-1 statement,
  which the scope note places "outside" the formalization.
- **The result is T2, a challenge not a proof** [S6, S7]: the
  comparator stub carries the `theorem nonuniqueness` with a
  `sorry` [S6:209] and there is no `main_results` entry or OAI
  tree, so the formalized statement stands only as a target.

## Section skeleton

Two manuscript roots. Manuscript 1 [S3] (local-conservation
headline, `build/main.tex`, 34 lines): a `preamble` [S3:2] and 12
`input` files [S3:20–31]: `01-introduction` … `12-separation`.
Manuscript 2 [S4] (periodic result, `build/paper.tex`, 33 lines): a
`preamble` [S4:2] and 10 `input` files [S4:20–29]:
`01-introduction` … `10-separation`. **No verification bundles.**

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note
[S5:9] and one comparator stub [S6]. The T2 shape is "scope note plus
comparator stub, **no** `main_results` entry, **no** proved OAI
tree," so the formalized statement is the comparator's challenge,
not a proved declaration.

The formalization is **asymmetric with the headline**: the scope
note names only manuscript 2 [S5:5] (the periodic result) and states
it as the formalized object [S5:9], while placing manuscript 1's
exact local-conservation refinements "outside it" [S5:11]. The
comparator stub `BoltzmannNonuniqueness.lean` (215 lines) carries the
density/predicate machinery (`FiniteEntropyDatum` [S6:70],
`BoundedVelocitySupport` [S6:73]) and states
`theorem nonuniqueness` [S6:204] with the `sorry` at [S6:209] (1 in
this stub). Unlike a T3 family, there is no `main_results` entry
resolving a declaration to an OAI file, and no proved tree to read —
the statement is a target the release set for itself.

## Coverage

The ledger row `fam=363` [S7] records the tier and the counts:
`tier=T2`, `paps=2`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=654`, `verification=0`, `trace=`. The
T2 shape is "scope note plus comparator stub, no `main_results`
entry, no OAI tree." The single comparator stub carries 1 `sorry`
[S6:209]. The shape flags are `shapes=bound|density`, `resolves_named=0`,
`counterex_broad=0`, `covmd=0` — a kinetic **bound**/existence result
carrying a **density**-type construction (two solution densities from
one datum), no named conjecture in the title, no
counterexample. Note `paps_form=0`: **neither** manuscript appears in
`formalization.yaml`'s `sources:` list, and there is no `main_results`
entry — the T2 formalization is the scope note's description and the
comparator's challenge only, with no proved Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8797] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 363 at [S2:828] |
| S3 | [`preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/build/main.tex`](../../../preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/build/main.tex) | 34 | the `\documentclass` root (manuscript 1, the local-conservation headline, NOT the formalized one) — 34 lines, title [S3:3–4], date [S3:6], abstract [S3:9–18], 12 `input` files [S3:20–31] |
| S4 | [`preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/build/paper.tex`](../../../preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/build/paper.tex) | 33 | the `\documentclass` root (manuscript 2, the periodic result, the formalized one) — 33 lines, title [S4:3], date [S4:5], abstract [S4:8–17], 10 `input` files [S4:20–29] |
| S5 | [`lean/docs/363.md`](../../../lean/docs/363.md) | 17 | scope note — names only manuscript 2; Scope at [S5:9–11], comparator link at [S5:17] |
| S6 | [`lean/ComparatorChallenges/BoltzmannNonuniqueness.lean`](../../../lean/ComparatorChallenges/BoltzmannNonuniqueness.lean) | 215 | comparator stub — 215 lines, `theorem nonuniqueness` [S6:204], `sorry` [S6:209] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=363`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
