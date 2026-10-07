# 097 — The Euclidean Steinitz--Bergstr\"om conjecture

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/097.md`](../../../lean/docs/097.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, partial |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026`](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/) | [The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf) | [build/](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/) | [README.md](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SteinitzBergstrom](../../../lean/ComparatorChallenges/SteinitzBergstrom.json) | `OAI.EuclideanSteinitzBergstrom.main` | [Main.lean](../../../lean/OAI/Analysis/Steinitz/Main.lean) | [`OAI/Analysis/Steinitz`](../../../lean/OAI/Analysis/Steinitz/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SteinitzBergstrom` | [.json](../../../lean/ComparatorChallenges/SteinitzBergstrom.json) | [.lean](../../../lean/ComparatorChallenges/SteinitzBergstrom.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that any finite sequence in the Euclidean unit ball of $\mathbb R^d$ admits signs keeping every partial sum within $C\sqrt d$, independently of length. Consequently every zero-sum family can be reordered with the same bound on unsigned partial sums. A matching lower bound gives the optimal order $S_2(d)=\Theta(\sqrt d)$.

