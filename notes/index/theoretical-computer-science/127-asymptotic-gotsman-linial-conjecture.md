# 127 — The asymptotic Gotsman--Linial conjecture

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/127.md`](../../../lean/docs/127.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026`](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/) | [main.pdf](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) | [build/](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/) | [README.md](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GotsmanLinial](../../../lean/ComparatorChallenges/GotsmanLinial.json) | `OAI.LeanBlast.GotsmanLinial.gotsmanLinialStatement` | [Main.lean](../../../lean/OAI/Combinatorics/GotsmanLinial/Main.lean) | [`OAI/Combinatorics/GotsmanLinial`](../../../lean/OAI/Combinatorics/GotsmanLinial/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GotsmanLinial` | [.json](../../../lean/ComparatorChallenges/GotsmanLinial.json) | [.lean](../../../lean/ComparatorChallenges/GotsmanLinial.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that a degree-at-most-$d$ polynomial threshold function on the uniform $n$-dimensional Boolean cube has average sensitivity at most $8d\sqrt n$, uniformly for $1\le d\le n$. Average sensitivity counts expected output changes under single-bit flips. This establishes the asymptotic Gotsman--Linial conjecture, allowing polynomial zeros with $\operatorname{sign}(0)=1$.

