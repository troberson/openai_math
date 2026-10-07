# 220 — Directional zero--one laws and ballisticity in random environments

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/220.md`](../../../lean/docs/220.md) |
| Comparator configs | 3 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026`](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/) | [directional-zero-one-finite-range.pdf](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf) | [build/](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/) | [README.md](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/build/manuscript/main.tex) | — |
| [`A-directional-zero-one-law-under-strict-ellipticity-September-23-2026`](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/) | [paper.pdf](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf) | [build/](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/) | [README.md](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/main.tex) | — |
| [`Directional-transience-implies-ballisticity-September-23-2026`](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/) | [paper.pdf](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf) | [build/](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/build/) | [README.md](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [DirectionalBallisticity](../../../lean/ComparatorChallenges/DirectionalBallisticity.json) | `OAI.DirectionalTransience.directional_transience_implies_ballisticity` | [Main.lean](../../../lean/OAI/Probability/Ballisticity/Main.lean) | [`OAI/Probability/Ballisticity`](../../../lean/OAI/Probability/Ballisticity/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DirectionalBallisticity` | [.json](../../../lean/ComparatorChallenges/DirectionalBallisticity.json) | [.lean](../../../lean/ComparatorChallenges/DirectionalBallisticity.lean) | 1 | 0 | no | yes |
| `DirectionalWalk` | [.json](../../../lean/ComparatorChallenges/DirectionalWalk.json) | [.lean](../../../lean/ComparatorChallenges/DirectionalWalk.lean) | 1 | 0 | no | no |
| `VelocityHemisphere` | [.json](../../../lean/ComparatorChallenges/VelocityHemisphere.json) | [.lean](../../../lean/ComparatorChallenges/VelocityHemisphere.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

On $\mathbb Z^d$, $d\ge3$, directional escape has probability zero or one for iid strictly elliptic nearest-neighbor environments, and for stationary ergodic finite-range-dependent environments under uniform ellipticity. In iid uniformly elliptic environments with $d\ge2$, almost-sure directional transience implies a deterministic limiting velocity with positive projection in that direction, resolving the ballisticity conjecture.

