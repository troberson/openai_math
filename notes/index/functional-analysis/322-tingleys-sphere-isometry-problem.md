# 322 — Tingley's sphere-isometry problem

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/322.md`](../../../lean/docs/322.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | resolution |
| Topics | [functional-analysis](../topics/functional-analysis.md) · [banach-spaces](../topics/banach-spaces.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-positive-solution-to-Tingleys-problem-September-23-2026`](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/) | [paper.pdf](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf) | [build/](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/) | [README.md](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TingleySphereIsometry](../../../lean/ComparatorChallenges/TingleySphereIsometry.json) | `OAI.Tingley.tingley_sphere_isometry_full` | [Extension.lean](../../../lean/OAI/Analysis/SphereIsometry/Extension.lean) | [`OAI/Analysis/SphereIsometry`](../../../lean/OAI/Analysis/SphereIsometry/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TingleySphereIsometry` | [.json](../../../lean/ComparatorChallenges/TingleySphereIsometry.json) | [.lean](../../../lean/ComparatorChallenges/TingleySphereIsometry.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves Tingley's problem: every surjective isometry between the unit spheres of nonzero real Banach spaces extends uniquely to a surjective real-linear isometry of the whole spaces. No dimension restriction is imposed, so the metric geometry of the unit sphere determines the Banach space up to linear isometry.

