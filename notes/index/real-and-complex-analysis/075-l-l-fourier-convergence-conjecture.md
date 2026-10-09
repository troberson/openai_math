# 075 — The $L\log L$ Fourier-convergence conjecture

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/075.md`](../../../lean/docs/075.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, partial |
| Topics | [harmonic-analysis](../topics/harmonic-analysis.md) · [measure-theory](../topics/measure-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026`](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/) | [paper.pdf](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf) | [build/](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/) | [README.md](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [FourierLLogL](../../../lean/ComparatorChallenges/FourierLLogL.json) | `OAI.FourierLLogL.paperMain` | [PaperMain.lean](../../../lean/OAI/Analysis/FourierLLogL/PaperMain.lean) | [`OAI/Analysis/FourierLLogL`](../../../lean/OAI/Analysis/FourierLLogL/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FourierLLogL` | [.json](../../../lean/ComparatorChallenges/FourierLLogL.json) | [.lean](../../../lean/ComparatorChallenges/FourierLLogL.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that the ordinary symmetric Fourier partial sums of every complex-valued function in $L\log L(\mathbb T)$ converge almost everywhere along the full sequence. This resolves the classical sufficiency conjecture at the $L\log L$ scale.

