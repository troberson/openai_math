# 222 — Perceptron free energies and microscopic jamming

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T2 |
| Manuscripts | 4 (0 formalized at source level) |
| Scope note | [`lean/docs/222.md`](../../../lean/docs/222.md) |
| Comparator configs | 3 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, density |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026`](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/) | [Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026.pdf](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026.pdf) | [build/](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/build/) | [README.md](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/README.md) | no | [main.tex](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/build/main.tex) | — |
| [`The-free-energy-of-the-Ising-random-perceptron-September-24-2026`](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/) | [The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf) | [build/](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/build/) | [README.md](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/README.md) | no | [main.tex](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/build/main.tex) | — |
| [`The-free-energy-of-the-spherical-random-perceptron-September-24-2026`](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/) | [The-free-energy-of-the-spherical-random-perceptron-September-24-2026.pdf](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/The-free-energy-of-the-spherical-random-perceptron-September-24-2026.pdf) | [build/](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/build/) | [README.md](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/README.md) | no | [paper.tex](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/build/paper.tex) | — |
| [`The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026`](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/) | [The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026.pdf](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026.pdf) | [build/](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/build/) | [README.md](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/README.md) | no | [paper.tex](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 3 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `IsingFiniteness` | [.json](../../../lean/ComparatorChallenges/IsingFiniteness.json) | [.lean](../../../lean/ComparatorChallenges/IsingFiniteness.lean) | 1 | 0 | no | no |
| `PerceptronFreeEnergy` | [.json](../../../lean/ComparatorChallenges/PerceptronFreeEnergy.json) | [.lean](../../../lean/ComparatorChallenges/PerceptronFreeEnergy.lean) | 1 | 0 | no | no |
| `SphericalField` | [.json](../../../lean/ComparatorChallenges/SphericalField.json) | [.lean](../../../lean/ComparatorChallenges/SphericalField.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines finite-temperature variational free energies for Gaussian Ising perceptrons with bounded Borel log-potentials and Gaussian spherical perceptrons with bounded continuous potentials, at every positive pattern density. A spherical extension treats bi-orthogonally invariant disorder with compact limiting singular-value distributions and no outliers. At margin $-1$, the quadratic-penalty spherical model has a sharp feasibility threshold and limiting gap and force laws, with system size, zero temperature, and critical density taken in that order.

