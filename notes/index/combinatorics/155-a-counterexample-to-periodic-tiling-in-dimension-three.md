# 155 — A counterexample to periodic tiling in dimension three

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/155.md`](../../../lean/docs/155.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026`](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/) | [paper.pdf](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf) | [build/](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/) | [README.md](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PeriodicTilingThree](../../../lean/ComparatorChallenges/PeriodicTilingThree.json) | `OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality` | [Counterexample.lean](../../../lean/OAI/Geometry/PeriodicTiling/Counterexample.lean) | [`OAI/Geometry/PeriodicTiling`](../../../lean/OAI/Geometry/PeriodicTiling/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PeriodicTilingThree` | [.json](../../../lean/ComparatorChallenges/PeriodicTilingThree.json) | [.lean](../../../lean/ComparatorChallenges/PeriodicTilingThree.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a finite translational tile in $\mathbb Z^3$ that tiles space but admits no fully periodic tiling, disproving the periodic tiling conjecture in the smallest possible lattice dimension. Its unit-cube thickening gives the same counterexample in $\mathbb R^3$, even with arbitrary real translation vectors.

