# 328 — Fixed points of nonexpansive maps in reflexive Banach spaces

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/328.md`](../../../lean/docs/328.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026`](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/) | [paper.pdf](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/paper.pdf) | [build/](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/build/) | [README.md](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ReflexiveFixedPoints](../../../lean/ComparatorChallenges/ReflexiveFixedPoints.json) | `OAI.ReflexiveFixedPoints.exists_fixedPoint_of_canonicallyReflexive` | [Main.lean](../../../lean/OAI/Analysis/Nonexpansive/Main.lean) | [`OAI/Analysis/Nonexpansive`](../../../lean/OAI/Analysis/Nonexpansive/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ReflexiveFixedPoints` | [.json](../../../lean/ComparatorChallenges/ReflexiveFixedPoints.json) | [.lean](../../../lean/ComparatorChallenges/ReflexiveFixedPoints.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves Kirk's reflexive-space fixed-point problem: every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. The result uses the original norm, without assuming uniform convexity.

