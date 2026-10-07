# 266 — Exactly three mutually unbiased bases in dimension six

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/266.md`](../../../lean/docs/266.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026`](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/) | [Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf) | [build/](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/build/) | [README.md](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/README.md) | no | [paper.tex](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/build/paper.tex) | [verification/](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/verification/) |
| [`The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026`](../../../preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/) | [The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf](../../../preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf) | [build/](../../../preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/build/) | [README.md](../../../preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/README.md) | no | [paper.tex](../../../preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HadamardCubeFiber` | [.json](../../../lean/ComparatorChallenges/HadamardCubeFiber.json) | [.lean](../../../lean/ComparatorChallenges/HadamardCubeFiber.lean) | 1 | 0 | no | no |
| `MUBSix` | [.json](../../../lean/ComparatorChallenges/MUBSix.json) | [.lean](../../../lean/ComparatorChallenges/MUBSix.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026` | [verification/](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves $N(6)=3$, resolving Zauner\textquotesingle s dimension-six mutually unbiased bases conjecture: three such bases exist in $\mathbb C^6$, but four cannot. The exclusion is a complete certified computation under the stated binary64 arithmetic and compiler conditions. An independent companion proves the Matolcsi--Ruzsa--Weiner Fourier-vanishing conjecture for order-six complex Hadamard matrices outside Tao\textquotesingle s cubic equivalence class.

