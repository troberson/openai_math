# 112 — Beyond the square-root exponent for depth-three circuits

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/112.md`](../../../lean/docs/112.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/) | [main.pdf](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf) | [build/](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/) | [README.md](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [DepthThree](../../../lean/ComparatorChallenges/DepthThree.json) | `OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound` | [Main.lean](../../../lean/OAI/Computability/DepthThree/Main.lean) | [`OAI/Computability/DepthThree`](../../../lean/OAI/Computability/DepthThree/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DepthThree` | [.json](../../../lean/ComparatorChallenges/DepthThree.json) | [.lean](../../../lean/ComparatorChallenges/DepthThree.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a single language in deterministic polynomial time whose $n$-bit membership function requires $2^{\omega(\sqrt n)}$ total gates in unbounded-fan-in OR--AND--OR circuits, at every sufficiently large input length. This crosses the square-root-exponent threshold for explicit depth-three Boolean circuit lower bounds.

