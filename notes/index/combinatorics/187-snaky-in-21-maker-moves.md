# 187 — Snaky in 21 Maker moves

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/187.md`](../../../lean/docs/187.md) |
| Comparator configs | 3 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution |
| Topics | [combinatorial-games](../topics/combinatorial-games.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Snaky-in-21-Maker-moves-September-25-2026`](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/) | [article.pdf](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/article.pdf) | [build/](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/build/) | [README.md](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/README.md) | no | [paper.tex](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/build/paper.tex) | [verification/](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/verification/) |

## Lean

No `main_results` declaration reaches this family: its scope note links 3 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SnakyCertificate` | [.json](../../../lean/ComparatorChallenges/SnakyCertificate.json) | [.lean](../../../lean/ComparatorChallenges/SnakyCertificate.lean) | 1 | 0 | no | no |
| `SnakyConditional` | [.json](../../../lean/ComparatorChallenges/SnakyConditional.json) | [.lean](../../../lean/ComparatorChallenges/SnakyConditional.lean) | 1 | 0 | no | no |
| `SnakyTwentyOne` | [.json](../../../lean/ComparatorChallenges/SnakyTwentyOne.json) | [.lean](../../../lean/ComparatorChallenges/SnakyTwentyOne.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Snaky-in-21-Maker-moves-September-25-2026` | [verification/](../../../preprints/Snaky-in-21-Maker-moves-September-25-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Settles the Snaky achievement problem: Maker can force the six-cell Snaky shape within 21 of its own moves on the initially empty infinite square board. Maker moves first, each player claims one free cell per turn, and translations, rotations and reflections count as wins.

