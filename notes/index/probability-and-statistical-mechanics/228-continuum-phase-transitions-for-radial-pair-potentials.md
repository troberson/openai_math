# 228 — Continuum phase transitions for radial pair potentials

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/228.md`](../../../lean/docs/228.md) |
| Comparator configs | 3 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | bound, density |
| Topics | [statistical-mechanics](../topics/statistical-mechanics.md) · [disordered-systems](../topics/disordered-systems.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026`](../../../preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/) | [paper.pdf](../../../preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/paper.pdf) | [build/](../../../preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/build/) | [README.md](../../../preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/build/paper.tex) | — |
| [`A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026`](../../../preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/) | [paper.pdf](../../../preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/paper.pdf) | [build/](../../../preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/build/) | [README.md](../../../preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ContinuumTransition](../../../lean/ComparatorChallenges/ContinuumTransition.json) | `OAI.ContinuumTemperature.main_theorem` | [Main.lean](../../../lean/OAI/Probability/ContinuumTransition/Main.lean) | [`OAI/Probability/ContinuumTransition`](../../../lean/OAI/Probability/ContinuumTransition/) |
| [RadialTransition](../../../lean/ComparatorChallenges/RadialTransition.json) | `OAI.RadialTransition.main` | [Main.lean](../../../lean/OAI/Probability/RadialTransition/Main.lean) | [`OAI/Probability/RadialTransition`](../../../lean/OAI/Probability/RadialTransition/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ContinuumTransition` | [.json](../../../lean/ComparatorChallenges/ContinuumTransition.json) | [.lean](../../../lean/ComparatorChallenges/ContinuumTransition.lean) | 1 | 0 | no | yes |
| `RadialDensityInterval` | [.json](../../../lean/ComparatorChallenges/RadialDensityInterval.json) | [.lean](../../../lean/ComparatorChallenges/RadialDensityInterval.lean) | 1 | 0 | no | no |
| `RadialTransition` | [.json](../../../lean/ComparatorChallenges/RadialTransition.json) | [.lean](../../../lean/ComparatorChallenges/RadialTransition.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs stable distance-dependent pair interactions for three-dimensional classical particles with a first-order phase transition: the canonical free energy has a derivative jump at one inverse temperature throughout an open density interval. One potential has a divergent repulsive core; another is bounded and continuous with an integrable power-law tail, realizing the type of transition sought in Simon's continuum problem.

