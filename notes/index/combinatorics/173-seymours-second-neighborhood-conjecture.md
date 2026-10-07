# 173 — Seymour's second-neighborhood conjecture

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/173.md`](../../../lean/docs/173.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [graph-theory](../topics/graph-theory.md) · [probabilistic-combinatorics](../topics/probabilistic-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026`](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SeymourSecondNeighborhood](../../../lean/ComparatorChallenges/SeymourSecondNeighborhood.json) | `OAI.SeymourSecondNeighborhood.exists_goodVertex` | [Main.lean](../../../lean/OAI/Combinatorics/SecondNeighborhood/Main.lean) | [`OAI/Combinatorics/SecondNeighborhood`](../../../lean/OAI/Combinatorics/SecondNeighborhood/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SeymourSecondNeighborhood` | [.json](../../../lean/ComparatorChallenges/SeymourSecondNeighborhood.json) | [.lean](../../../lean/ComparatorChallenges/SeymourSecondNeighborhood.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Seymour's second-neighborhood conjecture: every nonempty finite oriented graph has a vertex with at least as many vertices at directed distance exactly two as at directed distance one. Oriented graphs may be arbitrary apart from the exclusion of loops and oppositely directed edge pairs.

