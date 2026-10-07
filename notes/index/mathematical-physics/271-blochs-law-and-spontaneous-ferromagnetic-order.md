# 271 — Bloch's law and spontaneous ferromagnetic order

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T2 |
| Manuscripts | 4 (0 formalized at source level) |
| Scope note | [`lean/docs/271.md`](../../../lean/docs/271.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | [spontaneous-magnetization-quantum-heisenberg-ferromagnet](../../../reasoning_traces/spontaneous-magnetization-quantum-heisenberg-ferromagnet.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | [271-blochs-law-and-spontaneous-ferromagnetic-order.md](../../../notes/summaries/mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/) | [bloch-law-heisenberg.pdf](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf) | [build/](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/) | [README.md](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/README.md) | no | [main.tex](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/build/main.tex) | — |
| [`Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026`](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/) | [paper.pdf](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf) | [build/](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/) | [README.md](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/README.md) | no | [main.tex](../../../preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/build/source/main.tex) | — |
| [`The-first-lattice-correction-to-Blochs-law-October-5-2026`](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/) | [first-lattice-correction-bloch-law.pdf](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf) | [build/](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/) | [README.md](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/README.md) | no | [main.tex](../../../preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/build/main.tex) | — |
| [`The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/) | [spherical-magnetization.pdf](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) | [build/](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/) | [README.md](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/README.md) | no | [main.tex](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Heisenberg` | [.json](../../../lean/ComparatorChallenges/Heisenberg.json) | [.lean](../../../lean/ComparatorChallenges/Heisenberg.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Bloch's $T^{3/2}$ law with its exact coefficient for three-dimensional quantum Heisenberg ferromagnets at every positive quantum spin, allowing nonnegative symmetric finite-range couplings whose support generates $\mathbb Z^3$. The thermodynamic limit precedes the zero-field derivative and low-temperature limit. The family also proves spontaneous magnetization for nearest-neighbor models in every dimension $d\ge3$ and determines the first lattice correction for three-dimensional nearest-neighbor couplings.

