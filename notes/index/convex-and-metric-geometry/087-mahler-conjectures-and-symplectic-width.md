# 087 — The Mahler conjectures and symplectic width

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 3 (2 formalized at source level) |
| Scope note | [`lean/docs/087.md`](../../../lean/docs/087.md) |
| Comparator configs | 4 (3 with a `main_results` declaration) |
| Reasoning trace | [symmetric-and-general-mahler-conjectures](../../../reasoning_traces/symmetric-and-general-mahler-conjectures.pdf) |
| Verification bundles | 1 |
| Cited by / cites | 3 in · 4 out |
| Claim shapes | resolution, bound, classification |
| Topics | [metric-geometry](../topics/metric-geometry.md) · [complex-geometry](../topics/complex-geometry.md) · [convex-geometry](../topics/convex-geometry.md) · [symplectic-geometry](../topics/symplectic-geometry.md) · [potential-theory](../topics/potential-theory.md) |
| Companion families | — |
| Summary page | [087-the-mahler-conjectures-and-symplectic-width.md](../../../notes/summaries/convex-and-metric-geometry/087-the-mahler-conjectures-and-symplectic-width.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026`](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/) | [paper.pdf](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf) | [build/](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/build/) | [README.md](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/README.md) | yes | [main.tex](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/build/main.tex) | — |
| [`The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026`](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/) | [paper.pdf](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf) | [build/](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/build/) | [README.md](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/README.md) | no | [main.tex](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/build/main.tex) | [verification/](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/verification/) |
| [`The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026`](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) | [paper.pdf](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) | [build/](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/build/) | [README.md](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/README.md) | yes | [main.tex](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MahlerConjecture](../../../lean/ComparatorChallenges/MahlerConjecture.json) | `OAI.SymmetricMahler.symmetric_mahler` | [MainTheorem.lean](../../../lean/OAI/Analysis/Mahler/MainTheorem.lean) | [`OAI/Analysis/Mahler`](../../../lean/OAI/Analysis/Mahler/) |
| [SymmetricMahlerEquality](../../../lean/ComparatorChallenges/SymmetricMahlerEquality.json) | `OAI.SymmetricMahler.symmetric_mahler_equality` | [Classification.lean](../../../lean/OAI/Analysis/Mahler/Classification.lean) | [`OAI/Analysis/Mahler`](../../../lean/OAI/Analysis/Mahler/) |
| [SymmetricPolar](../../../lean/ComparatorChallenges/SymmetricPolar.json) | `OAI.SymmetricPolar.symmetric_polar_main` | [Main.lean](../../../lean/OAI/Geometry/PolarProducts/Main.lean) | [`OAI/Geometry/PolarProducts`](../../../lean/OAI/Geometry/PolarProducts/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GeneralMahler` | [.json](../../../lean/ComparatorChallenges/GeneralMahler.json) | [.lean](../../../lean/ComparatorChallenges/GeneralMahler.lean) | 1 | 0 | no | no |
| `MahlerConjecture` | [.json](../../../lean/ComparatorChallenges/MahlerConjecture.json) | [.lean](../../../lean/ComparatorChallenges/MahlerConjecture.lean) | 1 | 0 | no | yes |
| `SymmetricMahlerEquality` | [.json](../../../lean/ComparatorChallenges/SymmetricMahlerEquality.json) | [.lean](../../../lean/ComparatorChallenges/SymmetricMahlerEquality.lean) | 1 | 0 | no | yes |
| `SymmetricPolar` | [.json](../../../lean/ComparatorChallenges/SymmetricPolar.json) | [.lean](../../../lean/ComparatorChallenges/SymmetricPolar.lean) | 1 | 0 | no | yes |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026` | [verification/](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Resolves the symmetric and nonsymmetric geometric Mahler conjectures in every dimension, with Hanner polytopes and simplices as the respective volume-product minimizers and all equality cases classified. The corresponding sharp functional Mahler inequalities also hold. For $n\ge2$, every symmetric polar product $K\times K^\circ$ in dimension $2n$ has Gromov width $4$.

