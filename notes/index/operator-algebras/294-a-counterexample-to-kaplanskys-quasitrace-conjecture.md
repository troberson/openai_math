# 294 — A counterexample to Kaplansky's quasitrace conjecture

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/294.md`](../../../lean/docs/294.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [KaplanskyQuasitrace](../../../lean/ComparatorChallenges/KaplanskyQuasitrace.json) | `OAI.Kaplansky.kaplansky_quasitrace_counterexample` | [Main.lean](../../../lean/OAI/Analysis/Kaplansky/Main.lean) | [`OAI/Analysis/Kaplansky`](../../../lean/OAI/Analysis/Kaplansky/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `KaplanskyQuasitrace` | [.json](../../../lean/ComparatorChallenges/KaplanskyQuasitrace.json) | [.lean](../../../lean/ComparatorChallenges/KaplanskyQuasitrace.lean) | 1 | 0 | no | yes |
| `KaplanskyStableFiniteness` | [.json](../../../lean/ComparatorChallenges/KaplanskyStableFiniteness.json) | [.lean](../../../lean/ComparatorChallenges/KaplanskyStableFiniteness.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves Kaplansky's quasitrace conjecture by constructing a separable unital complex $C^*$-algebra admitting normalized $2$-quasitraces, all of which are nonadditive. As a consequence, two unital simple stably finite $C^*$-algebras can have a properly infinite minimal tensor product, with one factor $C_r^*(\mathbb F_2)$.

