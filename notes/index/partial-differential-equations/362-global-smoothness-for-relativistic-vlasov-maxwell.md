# 362 — Global smoothness for relativistic Vlasov--Maxwell

|  |  |
|---|---|
| Discipline | [Partial differential equations](../disciplines/partial-differential-equations.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/362.md`](../../../lean/docs/362.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | [relativistic-vlasov-maxwell](../../../reasoning_traces/relativistic-vlasov-maxwell.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, density, uniform |
| Topics | [partial-differential-equations](../topics/partial-differential-equations.md) · [kinetic-theory](../topics/kinetic-theory.md) |
| Companion families | — |
| Summary page | [362-global-smoothness-for-relativistic-vlasov-maxwell.md](../../../notes/summaries/partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/) | [paper.pdf](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf) | [build/](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/) | [README.md](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [VlasovMaxwell](../../../lean/ComparatorChallenges/VlasovMaxwell.json) | `OAI.RVM.global_classical_solution` | [Main.lean](../../../lean/OAI/Analysis/VlasovMaxwell/Main.lean) | [`OAI/Analysis/VlasovMaxwell`](../../../lean/OAI/Analysis/VlasovMaxwell/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `VlasovMaxwell` | [.json](../../../lean/ComparatorChallenges/VlasovMaxwell.json) | [.lean](../../../lean/ComparatorChallenges/VlasovMaxwell.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves large-data global existence and uniqueness for the three-dimensional, one-species relativistic Vlasov--Maxwell system. Smooth admissible initial data may be arbitrary provided the particle density is compactly supported and the electromagnetic fields have finite energy and bounded derivatives of every order; the solution remains smooth on every finite time interval.

