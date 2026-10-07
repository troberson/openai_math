# 162 — Counterexamples to Ryser's covering and Gy\'arf\'as's tree-cover conjectures

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/162.md`](../../../lean/docs/162.md) |
| Comparator configs | 3 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | counterexample, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026`](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/build/paper.tex) | — |
| [`Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026`](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/) | [paper.pdf](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf) | [build/](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/build/) | [README.md](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/README.md) | no | [paper.tex](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [RyserCovering](../../../lean/ComparatorChallenges/RyserCovering.json) | `OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank` | [Main.lean](../../../lean/OAI/Combinatorics/Ryser/Construction/Main.lean) | [`OAI/Combinatorics/Ryser/Construction`](../../../lean/OAI/Combinatorics/Ryser/Construction/) |
| [RyserOddExtensions](../../../lean/ComparatorChallenges/RyserOddExtensions.json) | `OAI.RyserOdd.eventualOddFailures_and_infinite` | [OddExtensions.lean](../../../lean/OAI/Combinatorics/Ryser/OddExtensions.lean) | [`OAI/Combinatorics/Ryser`](../../../lean/OAI/Combinatorics/Ryser/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BalancedRyser` | [.json](../../../lean/ComparatorChallenges/BalancedRyser.json) | [.lean](../../../lean/ComparatorChallenges/BalancedRyser.lean) | 1 | 0 | no | no |
| `RyserCovering` | [.json](../../../lean/ComparatorChallenges/RyserCovering.json) | [.lean](../../../lean/ComparatorChallenges/RyserCovering.lean) | 1 | 0 | no | yes |
| `RyserOddExtensions` | [.json](../../../lean/ComparatorChallenges/RyserOddExtensions.json) | [.lean](../../../lean/ComparatorChallenges/RyserOddExtensions.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves Ryser's covering conjecture by constructing intersecting $(q+1)$-partite, $(q+1)$-uniform hypergraphs with covering number $q+1$, rather than the predicted bound $q$, for every sufficiently large prime $q$. A separate construction over extension fields also disproves Gy\'arf\'as's monochromatic tree-cover conjecture.

