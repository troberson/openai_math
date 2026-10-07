# 114 — Approximate counting of common integer polymatroid bases

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/114.md`](../../../lean/docs/114.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | — |
| Topics | [sampling-and-counting](../topics/sampling-and-counting.md) · [matroids](../topics/matroids.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/) | [polymatroid-fpras.pdf](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) | [build/](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/) | [README.md](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/README.md) | no | [main.tex](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/build/main.tex) | — |
| [`Approximate-counting-of-common-bases-of-two-matroids-September-23-2026`](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/) | [main.pdf](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf) | [build/](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/) | [README.md](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CommonBasesFPRAS](../../../lean/ComparatorChallenges/CommonBasesFPRAS.json) | `OAI.common_bases_fpras` | [CommonBases.lean](../../../lean/OAI/Combinatorics/MatroidCounting/CommonBases.lean) | [`OAI/Combinatorics/MatroidCounting`](../../../lean/OAI/Combinatorics/MatroidCounting/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CommonBasesFPRAS` | [.json](../../../lean/ComparatorChallenges/CommonBasesFPRAS.json) | [.lean](../../../lean/ComparatorChallenges/CommonBasesFPRAS.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a fully polynomial randomized approximation scheme for counting common integer bases of two integral polymatroids of equal total rank, supplied by exact rank-value oracles. Capacities are binary-encoded, each integer vector counts once, and oracle calls and bit operations outside the oracles are polynomial on every execution. For matroids presented by independence oracles, the results also cover common independent sets of prescribed, unrestricted, or maximum cardinality, even when the ranks differ.

