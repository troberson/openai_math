# 312 — The Grothendieck homotopy hypothesis

|  |  |
|---|---|
| Discipline | [Topology](../disciplines/topology.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/312.md`](../../../lean/docs/312.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026`](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/) | [paper.pdf](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf) | [build/](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/) | [README.md](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GrothendieckElementaryExpansion](../../../lean/ComparatorChallenges/GrothendieckElementaryExpansion.json) | `OAI.Grothendieck.elementary_expansion` | [ElementaryExpansion.lean](../../../lean/OAI/CategoryTheory/Globular/ElementaryExpansion.lean) | [`OAI/CategoryTheory/Globular`](../../../lean/OAI/CategoryTheory/Globular/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GrothendieckElementaryExpansion` | [.json](../../../lean/ComparatorChallenges/GrothendieckElementaryExpansion.json) | [.lean](../../../lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the Grothendieck homotopy hypothesis for $\infty$-groupoids associated with every Grothendieck coherator in the Ara--Henry convention: these algebraic objects recover the homotopy theory of spaces.

