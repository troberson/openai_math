# 326 — The cotype--cotype conjecture under the approximation property

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/326.md`](../../../lean/docs/326.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, classification |
| Topics | [functional-analysis](../topics/functional-analysis.md) · [banach-spaces](../topics/banach-spaces.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026`](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/) | [paper.pdf](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/paper.pdf) | [build/](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/build/) | [README.md](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Cotype](../../../lean/ComparatorChallenges/Cotype.json) | `OAI.Cotype.mainTarget_proved` | [Main.lean](../../../lean/OAI/Analysis/Cotype/Main.lean) | [`OAI/Analysis/Cotype`](../../../lean/OAI/Analysis/Cotype/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Cotype` | [.json](../../../lean/ComparatorChallenges/Cotype.json) | [.lean](../../../lean/ComparatorChallenges/Cotype.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the cotype--cotype conjecture for real Banach spaces with the approximation property. Such a nonzero space is $K$-convex if and only if both it and its dual have finite Rademacher cotype, with possibly different exponents. Equivalently, these cotype assumptions force nontrivial Rademacher type.

