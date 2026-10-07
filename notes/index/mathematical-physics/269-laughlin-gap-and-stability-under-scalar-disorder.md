# 269 — The Laughlin gap and stability under scalar disorder

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/269.md`](../../../lean/docs/269.md) |
| Comparator configs | 4 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 2 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026`](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/) | [A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf) | [build/](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/build/) | [README.md](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/build/main.tex) | [verification/](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/verification/) |
| [`Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026`](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/) | [uniform-stability-spherical-laughlin-gap.pdf](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/uniform-stability-spherical-laughlin-gap.pdf) | [build/](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/) | [README.md](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/README.md) | no | [paper.tex](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/paper.tex) | [verification/](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/verification/) |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Laughlin](../../../lean/ComparatorChallenges/Laughlin.json) | `OAI.Laughlin.mainTarget_proved` | [Main.lean](../../../lean/OAI/Analysis/Laughlin/Main.lean) | [`OAI/Analysis/Laughlin`](../../../lean/OAI/Analysis/Laughlin/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Laughlin` | [.json](../../../lean/ComparatorChallenges/Laughlin.json) | [.lean](../../../lean/ComparatorChallenges/Laughlin.lean) | 1 | 0 | no | yes |
| `LaughlinFock` | [.json](../../../lean/ComparatorChallenges/LaughlinFock.json) | [.lean](../../../lean/ComparatorChallenges/LaughlinFock.lean) | 1 | 0 | no | no |
| `LaughlinGap` | [.json](../../../lean/ComparatorChallenges/LaughlinGap.json) | [.lean](../../../lean/ComparatorChallenges/LaughlinGap.lean) | 1 | 0 | no | no |
| `LaughlinPlanar` | [.json](../../../lean/ComparatorChallenges/LaughlinPlanar.json) | [.lean](../../../lean/ComparatorChallenges/LaughlinPlanar.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026` | [verification/](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/verification/) | no | no |
| `Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026` | [verification/](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves the fermionic Laughlin spectral-gap conjecture for the full $V_1$ interaction at filling $1/3$ on the round sphere. The unique ground state remains uniformly gapped under sufficiently weak bounded real scalar one-body potentials projected to the lowest Landau level. Both the gap and disorder threshold are uniform over all sufficiently large particle numbers and all normalized potential profiles.

