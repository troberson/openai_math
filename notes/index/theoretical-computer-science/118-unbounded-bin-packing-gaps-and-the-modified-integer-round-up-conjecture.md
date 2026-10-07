# 118 — Unbounded bin-packing gaps and the modified integer round-up conjecture

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/118.md`](../../../lean/docs/118.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, counterexample, partial |
| Topics | [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) · [discrete-geometry](../topics/discrete-geometry.md) · [combinatorial-optimization](../topics/combinatorial-optimization.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026`](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/) | [Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf) | [build/](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/) | [README.md](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BinPackingGap](../../../lean/ComparatorChallenges/BinPackingGap.json) | `OAI.BinPackingGap.main_results` | [Main.lean](../../../lean/OAI/Computability/BinPacking/Main.lean) | [`OAI/Computability/BinPacking`](../../../lean/OAI/Computability/BinPacking/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BinPackingGap` | [.json](../../../lean/ComparatorChallenges/BinPackingGap.json) | [.lean](../../../lean/ComparatorChallenges/BinPackingGap.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves the modified integer round-up conjecture of Scheithauer and Terno: the integral bin-packing optimum can exceed its configuration linear-programming value by an arbitrarily large additive constant. Approximating the optimum within any fixed additive constant is also NP-hard, even when every item exceeds $1/6$ and each bin holds at most five items.

