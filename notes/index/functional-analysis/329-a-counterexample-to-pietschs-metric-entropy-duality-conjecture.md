# 329 — A counterexample to Pietsch's metric-entropy duality conjecture

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/329.md`](../../../lean/docs/329.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026`](../../../preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/) | [main.pdf](../../../preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf) | [build/](../../../preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/build/) | [README.md](../../../preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MetricEntropyDuality](../../../lean/ComparatorChallenges/MetricEntropyDuality.json) | `OAI.MetricEntropyDuality.exists_entropy_duality_counterexample_with_covers` | [Main.lean](../../../lean/OAI/Analysis/MetricEntropy/Main.lean) | [`OAI/Analysis/MetricEntropy`](../../../lean/OAI/Analysis/MetricEntropy/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MetricEntropyDuality` | [.json](../../../lean/ComparatorChallenges/MetricEntropyDuality.json) | [.lean](../../../lean/ComparatorChallenges/MetricEntropyDuality.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves Pietsch's dimension-free duality conjecture for metric entropy. Origin-symmetric convex bodies violate every proposed choice of universal constants in the conjectured comparison between covering numbers and those of the polar bodies, even when the covering body is a cube.

