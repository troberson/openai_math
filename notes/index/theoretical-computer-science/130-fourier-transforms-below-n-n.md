# 130 — Fourier transforms below $n\log n$

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/130.md`](../../../lean/docs/130.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 3 out |
| Claim shapes | uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026`](../../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/) | [main.pdf](../../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf) | [build/](../../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/) | [README.md](../../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/README.md) | no | [main.tex](../../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/build/main.tex) | — |
| [`Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026`](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/) | [main.pdf](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf) | [build/](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/) | [README.md](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ExactFourier](../../../lean/ComparatorChallenges/ExactFourier.json) | `OAI.ExactFourier.main_theorem` | [Main.lean](../../../lean/OAI/Computability/FourierCircuit/Main.lean) | [`OAI/Computability/FourierCircuit`](../../../lean/OAI/Computability/FourierCircuit/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ExactFourier` | [.json](../../../lean/ComparatorChallenges/ExactFourier.json) | [.lean](../../../lean/ComparatorChallenges/ExactFourier.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a deterministic length-$n$ discrete Fourier transform algorithm using $O(n(\log n)^{1-\delta})$ operations for every $n$, with explicit $\delta=10^{-13}$. The model uses exact complex arithmetic, unrestricted coefficients and a supplied root of unity, and counts scalar preparation and logarithmic-word indexing.

