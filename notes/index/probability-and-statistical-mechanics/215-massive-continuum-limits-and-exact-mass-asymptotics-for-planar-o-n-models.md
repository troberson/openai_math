# 215 — Massive continuum limits and exact mass asymptotics for planar $O(n)$ models

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 5 (1 formalized at source level) |
| Scope note | [`lean/docs/215.md`](../../../lean/docs/215.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 6 in · 6 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026`](../../../preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/) | [o3-particle-pole.pdf](../../../preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/o3-particle-pole.pdf) | [build/](../../../preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/build/) | [README.md](../../../preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/README.md) | no | [main.tex](../../../preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/build/main.tex) | — |
| [`Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026`](../../../preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/) | [exact-mass-o4.pdf](../../../preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/exact-mass-o4.pdf) | [build/](../../../preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/build/) | [README.md](../../../preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/README.md) | no | [main.tex](../../../preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/build/main.tex) | — |
| [`Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026`](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/) | [paper.pdf](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf) | [build/](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/build/) | [README.md](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/build/main.tex) | — |
| [`Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026`](../../../preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/) | [paper.pdf](../../../preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf) | [build/](../../../preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/build/) | [README.md](../../../preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/README.md) | no | [main.tex](../../../preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/build/main.tex) | — |
| [`The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026`](../../../preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/) | [massive-continuum-o3.pdf](../../../preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/massive-continuum-o3.pdf) | [build/](../../../preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/build/) | [README.md](../../../preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/README.md) | no | [main.tex](../../../preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ClassicalON](../../../lean/ComparatorChallenges/ClassicalON.json) | `OAI.ClassicalON.main` | [Main.lean](../../../lean/OAI/Probability/ClassicalON/Main.lean) | [`OAI/Probability/ClassicalON`](../../../lean/OAI/Probability/ClassicalON/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ClassicalON` | [.json](../../../lean/ComparatorChallenges/ClassicalON.json) | [.lean](../../../lean/ComparatorChallenges/ClassicalON.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs the canonical continuum limit of the two-dimensional nearest-neighbor $O(3)$ model: a non-Gaussian local relativistic theory with a unique vacuum and a positive mass gap. For the square-lattice $O(4)$ model, determines the exact leading asymptotic of the full transfer gap, $m_{\mathrm{lat}}(\beta)\sim32e^{\pi/4-1/2}\sqrt\beta\,e^{-\pi\beta}$. The family also proves exponential spin-correlation decay for two-dimensional nearest-neighbor $O(n)$ models with $n\ge3$ at every positive temperature.

