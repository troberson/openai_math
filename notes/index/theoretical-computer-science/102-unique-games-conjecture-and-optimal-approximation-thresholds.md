# 102 — The Unique Games Conjecture and optimal approximation thresholds

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 5 (3 formalized at source level) |
| Scope note | [`lean/docs/102.md`](../../../lean/docs/102.md) |
| Comparator configs | 5 (3 with a `main_results` declaration) |
| Reasoning trace | [basic-semidefinite-threshold-np-hardness](../../../reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 3 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | [102-unique-games-conjecture-and-optimal-approximation-thresholds.md](../../../notes/summaries/theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026`](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/) | [paper.pdf](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/build/) | [README.md](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/build/main.tex) | — |
| [`Constant-factor-hardness-of-Min-UnCut-September-23-2026`](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/) | [paper.pdf](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf) | [build/](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/build/) | [README.md](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/README.md) | no | [main.tex](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/build/main.tex) | — |
| [`Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026`](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/) | [paper.pdf](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf) | [build/](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/build/) | [README.md](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/README.md) | no | [main.tex](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/build/main.tex) | — |
| [`The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026`](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/) | [paper.pdf](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf) | [build/](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/) | [README.md](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/main.tex) | — |
| [`The-Unique-Games-Theorem-September-23-2026`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/) | [paper.pdf](../../../preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) | [build/](../../../preprints/The-Unique-Games-Theorem-September-23-2026/build/) | [README.md](../../../preprints/The-Unique-Games-Theorem-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-Unique-Games-Theorem-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [OptimalMaxCut](../../../lean/ComparatorChallenges/OptimalMaxCut.json) | `OAI.OptimalMaxCut.main` | [Main.lean](../../../lean/OAI/Computability/MaxCut/Main.lean) | [`OAI/Computability/MaxCut`](../../../lean/OAI/Computability/MaxCut/) |
| [UniqueGamesTheorem](../../../lean/ComparatorChallenges/UniqueGamesTheorem.json) | `OAI.UniqueGamesTheorem.theorem11` | [Theorem.lean](../../../lean/OAI/Computability/UniqueGames/Theorem.lean) | [`OAI/Computability/UniqueGames`](../../../lean/OAI/Computability/UniqueGames/) |
| [VertexCover](../../../lean/ComparatorChallenges/VertexCover.json) | `OAI.VertexCover.every_fixed_factor_below_two` | [Main.lean](../../../lean/OAI/Computability/VertexCover/Main.lean) | [`OAI/Computability/VertexCover`](../../../lean/OAI/Computability/VertexCover/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DirectedFeedback` | [.json](../../../lean/ComparatorChallenges/DirectedFeedback.json) | [.lean](../../../lean/ComparatorChallenges/DirectedFeedback.lean) | 1 | 0 | no | no |
| `MinUncut` | [.json](../../../lean/ComparatorChallenges/MinUncut.json) | [.lean](../../../lean/ComparatorChallenges/MinUncut.lean) | 1 | 0 | no | no |
| `OptimalMaxCut` | [.json](../../../lean/ComparatorChallenges/OptimalMaxCut.json) | [.lean](../../../lean/ComparatorChallenges/OptimalMaxCut.lean) | 1 | 0 | no | yes |
| `UniqueGamesTheorem` | [.json](../../../lean/ComparatorChallenges/UniqueGamesTheorem.json) | [.lean](../../../lean/ComparatorChallenges/UniqueGamesTheorem.lean) | 1 | 0 | no | yes |
| `VertexCover` | [.json](../../../lean/ComparatorChallenges/VertexCover.json) | [.lean](../../../lean/ComparatorChallenges/VertexCover.lean) | 2 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Khot's Unique Games Conjecture. Independent direct reductions also establish NP-hardness, on unweighted graphs, of approximation beyond the Goemans--Williamson ratio for Max-Cut, below factor two for Vertex Cover, and within any fixed constant factor for Min-UnCut and directed feedback vertex set. These direct proofs use established PCP and Label Cover hardness results.

