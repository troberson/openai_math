# 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 5 (1 formalized at source level) |
| Scope note | [`lean/docs/347.md`](../../../lean/docs/347.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | counterexample, bound |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/) | [paper.pdf](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf) | [build/](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/) | [README.md](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex) | — |
| [`A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/) | [paper.pdf](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf) | [build/](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/) | [README.md](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex) | — |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/) | [paper.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) | [build/](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/) | [README.md](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md) | no | [main.tex](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex) | — |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/) | [hamiltonian-fixed-points-below-stable-morse-number.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) | [build/](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/) | [README.md](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md) | no | [main.tex](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/main.tex) | — |
| [`Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/) | [sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf) | [build/](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/) | [README.md](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md) | no | [main.tex](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ArnoldCounterexample](../../../lean/ComparatorChallenges/ArnoldCounterexample.json) | `OAI.ArnoldCounterexample.main` | [Main.lean](../../../lean/OAI/Geometry/Arnold/Main.lean) | [`OAI/Geometry/Arnold`](../../../lean/OAI/Geometry/Arnold/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ArnoldCounterexample` | [.json](../../../lean/ComparatorChallenges/ArnoldCounterexample.json) | [.lean](../../../lean/ComparatorChallenges/ArnoldCounterexample.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed K\"ahler manifolds of real dimension $22$, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function.

