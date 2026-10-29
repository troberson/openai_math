[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 237](../index/probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md)

# 237 — The three-quarter diameter exponent for honeycomb walks

[Index page](../index/probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md)

## Original CONTENTS.md summary

[S1:5723] (family entry):

> **237. The three-quarter diameter exponent for honeycomb walks.** Proves the diameter form of Nienhuis's predicted three-quarter exponent: a uniformly chosen $`n`$-step self-avoiding walk on the honeycomb lattice has diameter $`n^{3/4+o(1)}`$. Its local mass and covering numbers have exponent $`4/3`$. These estimates hold at every sufficiently large fixed length, simultaneously across scales, with arbitrarily high polynomial probability. ([Lean](../../../lean/docs/237.md))

[S2:559] carries the `\resultentry`, so the release blurb and the overview agree.
The family ships thirteen manuscripts; the two headline papers:

**Radial transfer and polygon length laws** [S3:40, S3:42]:

> 1

**Critical chords with prescribed endpoints** [S4:22, S4:23]:

> 2

The remaining eleven manuscripts build the radial transfer,
cylinder loop-weight, marked-polygon, disk transfer, polynomial
vacuum, renewal, strip-crossing, and cap-selected-amplitude
components.

## Undergraduate summary

A **self-avoiding walk** (SAW) on the honeycomb lattice is a
path that never visits the same vertex twice. **Nienhuis's
conjecture** (1982) predicts that as the walk gets longer,
its **diameter** (the distance from the farthest point to the
origin) grows like $`n^{3/4}`$, where $`n`$ is the number of
steps. This is slower than linear growth (a straight line)
but faster than square-root growth (a random walk without
the self-avoidance constraint). The result proves the
diameter form of this prediction: a uniformly chosen
$`n`$-step SAW on the honeycomb lattice has diameter
$`n^{3/4+o(1)}`$ [S3:45–47, S4:25–27, S2:559].

## Graduate summary

**Diameter tail exponents**
[S3:45–47, S2:559]. Critical diameter-tail
exponents $`-2`$ for unrooted honeycomb polygons and
$`-2/3`$ for length-weighted polygons, together with a
truncated second-length-moment bound of exponent $`2/3`$.
Consequently, polygons conditioned to have length at
least $`n`$ have diameter $`n^{3/4+o(1)}`$ in probability
under either weight.

**Critical honeycomb chords**
[S4:25–27, S2:559]. For every $`\varepsilon>0`$,
the probability that a chord between two specified
boundary endpoints has length between
$`R^{4/3-\varepsilon}`$ and $`R^{4/3+\varepsilon}`$ tends
to one as $`R\to\infty`$. The $`4/3`$ exponent is the dual
of the $`3/4`$ diameter exponent: diameter $`\sim n^{3/4}`$
means length $`\sim R^{4/3}`$ when $`R`$ is the chord
distance.

## History of the conjecture

**Nienhuis's three-quarter conjecture** (1982) predicted
that the diameter of a uniformly chosen $`n`$-step SAW on
the honeycomb lattice grows like $`n^{3/4}`$. The $`4/3`$
exponent for local mass and covering numbers is the
conjugate statement. The result [S3:45–47] proves
the diameter form via radial transfer estimates and
polygon length laws. The companion [S4:25–27]
establishes the $`4/3`$ exponent for chord lengths with
prescribed boundary endpoints. The eleven supporting
manuscripts build the cylinder loop-weight,
marked-polygon, disk transfer, polynomial vacuum,
renewal, strip-crossing, and cap-selected amplitude
machinery.

**Prior (my training data, not this repo).** Nienhuis's
prediction, the SAW framework, and the relation between
diameter exponent $`\nu`$ and connectivity exponent are
standard. The proof of the diameter form and the $`4/3`$
chord exponent are the novel contributions. I cannot
confirm these independently from training alone.

## Consequences

- **The three-quarter diameter exponent**
  [S3:45–47]: a uniformly chosen $`n`$-step SAW on
  the honeycomb lattice has diameter $`n^{3/4+o(1)}`$.
- **The four-thirds exponent**
  [S4:25–27, S3:45–47]: local mass and
  covering numbers have exponent $`4/3`$; chord length
  between prescribed endpoints is $`R^{4/3+o(1)}`$.
- **Simultaneous scales**
  [S3:45–47]: the estimates hold at every
  sufficiently large fixed length, simultaneously across
  scales, with arbitrarily high polynomial probability.

## Section skeleton

Thirteen manuscripts. [S3] (title [S3:40], date [S3:42])
— `main.tex` under `build/`; [S4] (title [S4:22],
date [S4:23]) — `main.tex` under `build/`. The
remaining eleven cover cylinder loop weights, marked
polygons, disk transfer, polynomial vacuum, renewal,
strip crossing, cap selected amplitudes, mass and
covering exponents, signed cylinder propagation,
logarithmic bridge length windows, and uniform marked
polygon estimates. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one
scope note [S5], four comparator stubs [S6] [S7] [S8]
[S9], and one `main_results` entry [S11]. The scope note
[S5:12–26] states four targets: finiteness of
critical bridge measures and first length moments;
existence of the infinite-length free energy; strip mass
comparable to $`N^{-1/4}`$ and displacement moment
comparable to $`N^{3/4}`$; and the bridge mass estimate
$`B_h = (1+h)^{-1/4+o(1)}`$.

The `main_results` entry [S11:1319–1321] names
`OAI.CriticalHoneycomb.finiteBridgeMassEstimate` in
`lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean`.
In the source, the theorem is stated and closed at
[S10:114]. `grep` finds **zero** `sorry` in the whole
`lean/OAI/Combinatorics/HoneycombChords/` tree.

The four comparator stubs carry the targets, each with
one `sorry`: [S6] (bridge finiteness), [S7] (free
energy), [S8] (strip mass and displacement moment),
[S9] (bridge mass of order $`(1+h)^{-1/4}`$). Only the
bridge mass estimate has a proved copy under
`lean/OAI/`; the other three targets are stubs without
a corresponding `main_results` entry. A comparator stub
is a target the release set itself; the proved version,
where it exists, lives under `lean/OAI/`. The reading is
of source text only — no `lake` or `lean` run
elaborates the proof.

## Coverage

The ledger row `fam=237` [S12] records the tier and the
counts: `tier=T3`, `paps=13`, `paps_form=1`, `chal=4`,
`mainres=1`, `scope_note=1`, `verification=0`, `trace=`.
The `paps_form=1` against `paps=13` is the coverage
signature: one of the thirteen manuscripts is named as
a formalization source (the chords paper), and the
single `main_results` entry over that config reaches
only the bridge mass estimate — the diameter
$`3/4`$ exponent, the free energy, and the strip crossing
results have no formalization. The four comparator
stubs name all four targets, but only one has a proved
copy. There is no verification bundle and no reasoning
trace. The shape flags are `uniform`, and
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5723] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 237 at [S2:559] |
| S3 | [`preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/build/main.tex`](../../../preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/build/main.tex) | 77 | manuscript 1 of 13 (radial transfer and polygon length laws); title [S3:40], date [S3:42], abstract [S3:45–47] |
| S4 | [`preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/build/main.tex`](../../../preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/build/main.tex) | 39 | manuscript 2 of 13 (critical honeycomb chords); title [S4:22], date [S4:23], abstract [S4:25–27] |
| S5 | [`lean/docs/237.md`](../../../lean/docs/237.md) | 35 | scope note — the formalization's Scope at [S5:12–26] and its four comparator links at [S5:30–35] |
| S6 | [`lean/ComparatorChallenges/HoneycombBridgeFiniteness.lean`](../../../lean/ComparatorChallenges/HoneycombBridgeFiniteness.lean) | 65 | comparator stub — the bridge finiteness target with its `sorry` |
| S7 | [`lean/ComparatorChallenges/HoneycombFreeEnergy.lean`](../../../lean/ComparatorChallenges/HoneycombFreeEnergy.lean) | 72 | comparator stub — the free-energy limit target with its `sorry` |
| S8 | [`lean/ComparatorChallenges/CriticalStripMass.lean`](../../../lean/ComparatorChallenges/CriticalStripMass.lean) | 82 | comparator stub — the strip mass and displacement moment target with its `sorry` |
| S9 | [`lean/ComparatorChallenges/HoneycombBridgeMassSupport.lean`](../../../lean/ComparatorChallenges/HoneycombBridgeMassSupport.lean) | 78 | comparator stub — the bridge mass of order $(1+h)^{-1/4}$ target with its `sorry` |
| S10 | [`lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean`](../../../lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean) | 147 | the formalized file — `finiteBridgeMassEstimate` proved at [S10:114] |
| S11 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming the declaration, at [S11:1319–1321] |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=237`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
