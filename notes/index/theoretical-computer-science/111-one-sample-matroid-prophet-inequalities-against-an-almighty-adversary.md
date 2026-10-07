# 111 — One-sample matroid prophet inequalities against an almighty adversary

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/111.md`](../../../lean/docs/111.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [combinatorial-optimization](../topics/combinatorial-optimization.md) · [matroids](../topics/matroids.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026`](../../../preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/) | [final.pdf](../../../preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf) | [build/](../../../preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/) | [README.md](../../../preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/README.md) | no | [main.tex](../../../preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MatroidProphet` | [.json](../../../lean/ComparatorChallenges/MatroidProphet.json) | [.lean](../../../lean/ComparatorChallenges/MatroidProphet.lean) | 1 | 0 | no | no |
| `MatroidSecretary` | [.json](../../../lean/ComparatorChallenges/MatroidSecretary.json) | [.lean](../../../lean/ComparatorChallenges/MatroidSecretary.lean) | 3 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every finite matroid known in advance, gives a distribution-independent online rule using one independent sample per element and earning a universal constant fraction of the expected offline optimum. Values are independent and nonnegative, with finite expected optimum. The guarantee holds even when the arrival-order adversary sees all samples, values, and the rule's entire random seed; no polynomial-time implementation is asserted.

