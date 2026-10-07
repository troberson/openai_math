# 272 — Entanglement without secret key and the PPT-square conjecture

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/272.md`](../../../lean/docs/272.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026`](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/) | [paper.pdf](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf) | [build/](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/build/) | [README.md](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/README.md) | no | [main.tex](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/build/source/main.tex) | [verification/](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/verification/) |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DimensionTenChannel` | [.json](../../../lean/ComparatorChallenges/DimensionTenChannel.json) | [.lean](../../../lean/ComparatorChallenges/DimensionTenChannel.lean) | 1 | 0 | no | no |
| `DimensionTenPair` | [.json](../../../lean/ComparatorChallenges/DimensionTenPair.json) | [.lean](../../../lean/ComparatorChallenges/DimensionTenPair.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026` | [verification/](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Constructs an entangled state on $\mathbb C^{10}\otimes\mathbb C^{10}$ with zero distillable secret key for the specified local-instrument protocols that complete almost surely. These allow joint local processing and authenticated two-way public communication, with no other shared private resource and an eavesdropper holding the input purification and public record. A trace-preserving PPT channel on $M_{21}(\mathbb C)$ whose square is not entanglement breaking disproves Christandl\textquotesingle s PPT-square conjecture.

