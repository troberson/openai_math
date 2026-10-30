[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 234](../index/probability-and-statistical-mechanics/234-all-temperature-pressure-for-orthogonally-invariant-ising-spin-glasses.md)

# 234 — All-temperature pressure for orthogonally invariant Ising spin glasses

[Index page](../index/probability-and-statistical-mechanics/234-all-temperature-pressure-for-orthogonally-invariant-ising-spin-glasses.md)

## Original CONTENTS.md summary

[S1:5648] (family entry):

> **234. All-temperature pressure and spectral overlaps for invariant Ising spin glasses.** Determines the limiting free-energy pressure of Haar-orthogonally invariant Ising spin glasses with a bounded limiting spectral measure and no asymptotic outliers, at every fixed positive temperature, in expectation and almost surely. It gives deterministic-field pressure limits under first-moment transport convergence, a zero-temperature ground-state energy, all-temperature spectral-overlap bounds, and an upper bound on the zero- and positive-temperature limiting magnetizations. ([Lean](../../../lean/docs/234.md))

[S2:553] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**Invariant Ising spin glass pressure** [S3:51, S3:53]:

> We determine the limiting pressure of an Ising spin glass with Haar
orthogonal eigenvectors, a compact limiting spectral law, and no
asymptotic outliers, at every fixed temperature. The pressure converges
in expectation and almost surely to a variational formula. We also give
the limiting pressure with deterministic external fields whose empirical
laws converge in first-moment transport distance, and derive a formula
for the zero-field ground-state energy by taking temperature to zero. [S3:64–72]

## Undergraduate summary

A **spin glass** is a disordered magnetic system where the
interactions between spins can be positive or negative, leading
to a complex energy landscape with many local minima. The
**pressure** (or **free energy** per spin) is the fundamental
quantity that determines the system's phase behavior at a given
temperature. For **Haar-orthogonally invariant** spin glasses
— those where the interaction matrix's eigenvectors are
randomly rotated by a Haar-uniform orthogonal matrix —
this result pins down the pressure at **every** temperature,
not just above a critical point, showing it converges to a
clean **variational formula** depending only on the limiting
spectral measure [S3:64–70, S2:553].

## Graduate summary

**All-temperature pressure for invariant Ising spin glasses**
[S3:64–70, S2:553]. For an Ising spin glass with
Haar-orthogonal eigenvectors, a compact limiting spectral
law, and no asymptotic outliers, the limiting pressure at
every fixed positive temperature converges in expectation
and almost surely to a variational formula. The
deterministic-field pressure limits are given under
first-moment transport convergence of the empirical
field laws. The zero-temperature ground-state energy is
derived by taking temperature to zero. All-temperature
spectral-overlap bounds and an upper bound on the
limiting magnetization are also established.

## History of the conjecture

The **pressure of random spin glasses** is a central
object in statistical physics. For the
**Sherrington–Kirkpatrick** (SK) model, the
pressure at low temperature was determined by Parisi's
formula. The **Haar-orthogonally invariant** class
generalizes the SK model by allowing an arbitrary
limiting spectral distribution, not just the Gaussian
semicircle. Previous results covered only specific
temperature ranges or specific spectral laws. The
all-temperature result [S3:64–70] removes
both restrictions, giving the variational formula at
every positive temperature for every bounded compact
spectral law without asymptotic outliers.

**Prior (my training data, not this repo).** The SK model,
Parisi's formula, and the spin-glass pressure framework
are standard. The all-temperature extension to Haar-
orthogonal invariant spin glasses with arbitrary spectral
laws is the novel contribution. I cannot confirm this
independently from training alone.

## Consequences

- **The all-temperature variational formula**
  [S3:64–70]: the limiting pressure at every
  positive temperature equals the variational formula
  depending only on the limiting spectral measure.
- **The deterministic-field extension**
  [S3:67–68]: pressure limits under first-moment
  transport convergence of the empirical field laws.
- **The zero-temperature ground-state energy**
  [S3:68–69]: the ground-state energy is obtained
  by taking the temperature to zero.
- **The magnetization upper bound**
  [S3:69–70]: an upper bound on the zero- and
  positive-temperature limiting magnetizations.

## Section skeleton

One manuscript: [S3:64–72] (title [S3:51], date [S3:53])
— `invariant-sk.tex` under `build/` with section
files `10-arrays.tex` through `70-magnetic.tex`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T2 with one
scope note [S4] and one comparator stub [S5], but
**no** `main_results` entry and **no** OAI tree. The
scope note [S4:9–13] states three targets: the
pressure converges in expectation to the variational
formula depending only on the limiting spectral law;
the spectral-overlap bound holds for every fixed
positive temperature; and the magnetization upper
bound holds at the limiting state.

The one comparator stub [S5] (InvariantIsing.lean)
carries the pressure, overlap, and magnetization
targets and ends in eleven `sorry`. No proved copy
exists under `lean/OAI/`. The gap is the formalization
itself: the release set the targets and created a
challenge stub, but did not produce a `main_results`
entry or an OAI proof. The reading is of source text
only — no `lake` or `lean` run elaborates the
proof.

## Coverage

The ledger row `fam=234` [S6] records the tier and the
counts: `tier=T2`, `paps=1`, `paps_form=0`, `chal=1`,
`mainres=0`, `scope_note=1`, `verification=0`, `trace=`.
The T2 shape: scope note and comparator stub exist,
no formalization. The single manuscript carries the
full result — pressure, spectral overlaps, and
magnetization bounds. The deterministic-field and
zero-temperature results are outside the scope note's
three targets. There is no verification bundle and no
reasoning trace. The shape flags are `bound`, and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5648] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 234 at [S2:553] |
| S3 | [`preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex`](../../../preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex) | 349 | manuscript 1 of 1; title [S3:51], date [S3:53], abstract [S3:64–70] |
| S4 | [`lean/docs/234.md`](../../../lean/docs/234.md) | 17 | scope note — the formalization's Scope at [S4:9–13] and its one comparator link at [S4:16] |
| S5 | [`lean/ComparatorChallenges/InvariantIsing.lean`](../../../lean/ComparatorChallenges/InvariantIsing.lean) | 495 | comparator stub — the pressure/overlap/magnetization targets with eleven `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=234`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
