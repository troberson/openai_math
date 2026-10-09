# 301 — Classification by trace cones after Razak--Jacelon stabilization

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/301.md`](../../../lean/docs/301.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | resolution, uniform |
| Topics | [operator-algebras](../topics/operator-algebras.md) · [functional-analysis](../topics/functional-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026`](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/) | [The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf) | [build/](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/build/) | [README.md](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TraceIdealTransportSupport](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.json) | `OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_finIdeal` | [IdealTransport.lean](../../../lean/OAI/Analysis/TraceCone/IdealTransport.lean) | [`OAI/Analysis/TraceCone`](../../../lean/OAI/Analysis/TraceCone/) |
| [TraceIdealTransportSupport](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.json) | `OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_zeroIdeal` | [IdealTransport.lean](../../../lean/OAI/Analysis/TraceCone/IdealTransport.lean) | [`OAI/Analysis/TraceCone`](../../../lean/OAI/Analysis/TraceCone/) |
| [TraceIdealTransportSupport](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.json) | `OAI.TraceConeClassification.closed_ideal_weight_exists` | [FiniteIdeal.lean](../../../lean/OAI/Analysis/TraceCone/FiniteIdeal.lean) | [`OAI/Analysis/TraceCone`](../../../lean/OAI/Analysis/TraceCone/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TraceIdealTransportSupport` | [.json](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.json) | [.lean](../../../lean/ComparatorChallenges/TraceIdealTransportSupport.lean) | 17 | 0 | yes | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Classifies separable nuclear complex $C^*$-algebras after tensoring with the Razak--Jacelon algebra and the compact operators, using their full topological cones of extended lower-semicontinuous tracial weights. This answers Robert’s trace-cone question, including algebras with arbitrary ideal structure and both finite and infinite subquotients.

