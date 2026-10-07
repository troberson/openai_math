# 213 — No infinite critical clusters on quasi-transitive graphs

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/213.md`](../../../lean/docs/213.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026`](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/) | [paper.pdf](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf) | [build/](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/build/) | [README.md](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md) | yes | [critical-percolation-z3.tex](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/build/critical-percolation-z3.tex) | — |
| [`No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026`](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/) | [paper.pdf](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf) | [build/](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/) | [README.md](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/README.md) | no | [main.tex](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CriticalZ3](../../../lean/ComparatorChallenges/CriticalZ3.json) | `OAI.CriticalZ3.critical_no_infinite` | [Main.lean](../../../lean/OAI/Probability/CriticalZ3/Main.lean) | [`OAI/Probability/CriticalZ3`](../../../lean/OAI/Probability/CriticalZ3/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CriticalPercolation` | [.json](../../../lean/ComparatorChallenges/CriticalPercolation.json) | [.lean](../../../lean/ComparatorChallenges/CriticalPercolation.lean) | 1 | 0 | no | no |
| `CriticalZ3` | [.json](../../../lean/ComparatorChallenges/CriticalZ3.json) | [.lean](../../../lean/ComparatorChallenges/CriticalZ3.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the Benjamini--Schramm criticality conjecture for bond percolation on every infinite connected locally finite quasi-transitive graph with $p_c<1$: at the critical probability, there is almost surely no infinite cluster. The family also establishes this conclusion for both nearest-neighbor bond and site percolation on $\mathbb Z^3$.

