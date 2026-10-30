[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 371](../index/partial-differential-equations/371-stable-blowup-for-a-defocusing-schrodinger-equation.md)

# 371 — Stable blowup for a defocusing Schrödinger equation

[Index page](../index/partial-differential-equations/371-stable-blowup-for-a-defocusing-schrodinger-equation.md)

## Original CONTENTS.md summary

[S1:8970] (family entry):

> **371. Stable blowup for the defocusing Schrödinger equation.** For a sufficiently large odd nonlinearity power, constructs a nonempty open set of initial data in $`H^k(\mathbb T^{12})`$, with <i>k</i> &gt; 8, whose solutions of the scalar defocusing nonlinear Schrödinger equation blow up in finite time. Thus finite-time blowup is stable under Sobolev perturbations in this supercritical regime. ([Lean](lean/docs/371.md))

[S2:845] carries the `\resultentry` with a single manuscript [S3].
The scope note states the formalized result:

> The formalization constructs stable self-similar finite-time blowup for defocusing nonlinear Schrödinger equations on the twelve-dimensional torus. For every prescribed lower bound on the power, it selects an odd power at least that large and a Sobolev index $`k>8`$ for which a nonempty open set of $`H^k`$ initial data has the stated classical blowup behavior. The selected quantifier gives arbitrarily large odd powers, rather than every sufficiently large odd power. [S4:9]

## Undergraduate summary

The **Schrödinger equation** is one of the central equations in
physics — it describes how quantum wave functions evolve over time.
The **defocusing** variant has a sign that tends to spread waves
apart rather than focus them, so in the classical theory solutions
usually exist for all time (they are "globally well-posed").

This result shows that in a **supercritical** regime (where the
nonlinearity is strong enough relative to the dimension), finite-time
**blowup** — where the solution becomes infinite at a finite time —
is not just possible but **stable**: there is a whole *open set* of
initial conditions near a blowup trajectory that also blow up.
"Stable" means that if you perturb the initial data slightly (in the
Sobolev sense, a measure of smoothness), the blowup persists.

The setting is the **twelve-dimensional torus** (a 12-dimensional
box with opposite sides identified), and the nonlinearity power must
be large and odd. The result also shows that **Gaussian random initial
data** of high enough smoothness hit this blowup set with positive
probability, so almost-sure global existence **fails** for the
random problem [S3:34–41, S4:9].

## Graduate summary

**Main theorem (stable self-similar blowup)** [S3:34–41, S1:8970].
For a sufficiently large odd power $`p`$, there is a nonempty open
set $`U \subset H^k(\mathbb T^{12})`$ with $`k > 8`$ such that every
initial datum in $`U`$ produces a classical solution of the scalar
defocusing nonlinear Schrödinger equation that blows up in finite
time via a self-similar profile [S3:34–41].

**Gaussian corollary** [S3:34–41, S1:8970].
Gaussian Fourier initial data with decay exponent
$`\alpha > k+6`$ assign positive probability to the blowup set $`U`$,
and almost-sure global existence fails [S3:34–41].

**The formalization is T2, not T3** [S4, S5, S7].
The scope note [S4:9] and one comparator stub [S5] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S7]. The comparator stub `DefocusingNLS.lean` (305 lines) carries
the Fourier/Sobolev/blowup machinery and states **three** challenge
theorems: `theorem stable_blowup` [S5:269] with `sorry`
[S5:275], `theorem gaussian_blowup` [S5:279] with `sorry`
[S5:291], and `theorem gaussian_not_almost_sure_global` [S5:294]
with `sorry` [S5:299] (3 in this stub). The T2 shape is "scope note
plus comparator stub, no `main_results` entry, no OAI tree."

**The formalization is asymmetric with the manuscript on the
quantifier** [S4:11, S5].
The scope note states the quantifier explicitly: "it **selects** an
odd power at least that large" — an existential statement. The
manuscript's claim is "for a **sufficiently large** odd power" — a
universal statement over a tail of powers. "The selected quantifier
gives arbitrarily large odd powers, **rather than every** sufficiently
large odd power" [S4:11]. The comparator stubs encode the existential
form: `theorem stable_blowup (p₀ : ℕ) : ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ …`
[S5:269–274]. The universal "for all large odd $`p`$" is not the
formalized statement.

## History of the conjecture

The **defocusing nonlinear Schrödinger equation** is
$`i \partial_t u + \Delta u = |u|^{p-1} u`$, where the plus sign
in the nonlinearity makes the equation defocusing (energy-dispersive).
In the **subcritical** regime (low nonlinearity relative to dimension),
solutions are globally well-posed in the energy space. The
**supercritical** regime is where blowup can occur, and the
self-similar blowup constructions of **Merle–Philippe**, **Kenig–Merle**,
and **Krieger–Schlag** (among others) established blowup for critical
and supercritical variants in various settings.

The **novel contribution** is the **stability of blowup in the
supercritical defocusing regime on the torus** [S3:34–41, S4:9]: not
just the existence of a single blowup trajectory, but a **nonempty
open set** of initial data that blow up, together with the **Gaussian
random-data corollary** (positive-probability blowup and failure of
almost-sure global existence). The proof uses a
free-propagation/profile decomposition framework [S3:224–228],
spectral analysis [S3:226], and **exact-arithmetic certificates**
[S6] that verify the finite integer and rational comparisons
underlying the blowup estimates.

**Prior (my training data, not this repo).** As of my training cutoff,
finite-time blowup for the supercritical defocusing NLS was known in
various settings (radial, whole-space, critical), and stability results
were an active direction. The torus setting in twelve dimensions with
the open-set stability and the Gaussian positive-probability
corollary was at the frontier of the dispersive PDE blowup program.
I cannot verify the dispersive estimates independently from training
alone.

## Consequences

- **Stable blowup on the 12-torus** [S3:34–41, S1:8970]: for a
  sufficiently large odd power, a nonempty open set of
  $`H^k(\mathbb T^{12})`$ initial data (with $`k > 8`$) blow up
  in finite time via self-similar profiles.
- **Gaussian positive-probability blowup** [S3:34–41, S1:8970]:
  Gaussian Fourier data with decay exponent $`\alpha > k+6`$ hit
  the blowup set with positive probability.
- **Almost-sure global existence fails** [S3:34–41, S4:9]: for
  the Gaussian random-data problem, global existence does not hold
  with probability one.
- **The formalization is T2, a challenge not a proof**
  [S5, S7]: three comparator stubs carry 3 `sorry` occurrences
  [S5:275, S5:291, S5:299] and there is no `main_results` entry
  or OAI tree.
- **The quantifier is existential, not universal** [S4:11, S5:269]:
  the formalized statement selects an odd power at least `p₀`, not
  every sufficiently large odd power.
- **A finite-arithmetic certificate ships with the manuscript**
  [S6]: the verification bundle rechecks the integer and rational
  comparisons underlying the blowup estimates (428-line exact
  verifier, `RESULTS.json` with `all_finite_arithmetic_checks_pass`).

## Section skeleton

One manuscript, `build/main.tex` root (235 lines). The root
declares the theorem environments and macros inline [S3:1–22],
the title at [S3:27], the date at [S3:29], the abstract at
[S3:34–41], the introduction at [S3:44], and 6 `input` files
[S3:224–231]: `01-free`, `02-profiles`, `03-spectrum`,
`04-linear`, `05-nonlinear`, `06-certificates`, plus a BibTeX
`references`. The manuscript also ships a **verification bundle**
[S6] with the `certificates/` subdirectory containing
`exact_verifier.py` (428 lines), `RESULTS.json`,
`original_exact_certificates.py`, and integrity checksums.

## Coverage

The ledger row `fam=371` [S7] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=685`, `verification=1`, `trace=0`,
`companions=`. The T2 shape is "scope note plus comparator stub,
no `main_results` entry, no OAI tree." The single comparator stub
carries 3 `sorry` [S5:275, S5:291, S5:299]. The shape flags are
`shapes=` (empty — no claim-shape tag), `resolves_named=0`,
`counterex_broad=0`, `covmd=0`. The `verification=1` is the
finite-arithmetic certificate bundle [S6] (the exact-arithmetic
verifier and its shipped `RESULTS.json`). No named conjecture,
no counterexample tag, and no claim-shape tags in the ledger.
Note `paps_form=0`: the manuscript does not appear in
`formalization.yaml`'s `sources:` list, and there is no
`main_results` entry — the T2 formalization is the scope note's
description and the comparator's three challenge statements only,
with no proved Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8970] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 371 at [S2:845] |
| S3 | [`preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/build/main.tex`](../../../preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/build/main.tex) | 235 | the `\documentclass` root — 235 lines, title [S3:27], date [S3:29], abstract [S3:34–41], 6 `input` files [S3:224–231] |
| S4 | [`lean/docs/371.md`](../../../lean/docs/371.md) | 17 | scope note — names the single manuscript [S4:5]; Scope at [S4:9–11], comparator link at [S4:17] |
| S5 | [`lean/ComparatorChallenges/DefocusingNLS.lean`](../../../lean/ComparatorChallenges/DefocusingNLS.lean) | 305 | comparator stub — 305 lines, `def HasFiniteTimeSelfSimilarBlowup` [S5:253], `theorem stable_blowup` [S5:269], `sorry` [S5:275], `theorem gaussian_blowup` [S5:279], `sorry` [S5:291], `theorem gaussian_not_almost_sure_global` [S5:294], `sorry` [S5:299] |
| S6 | [`preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/verification/certificates/exact_verifier.py`](../../../preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/verification/certificates/exact_verifier.py) | 428 | finite-arithmetic certificate — 428 lines, the exact-arithmetic verifier in the verification bundle |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=371`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
