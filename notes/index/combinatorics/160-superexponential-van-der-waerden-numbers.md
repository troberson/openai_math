# 160 — Superexponential van der Waerden numbers

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/160.md`](../../../lean/docs/160.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | resolution, uniform |
| Topics | [logic](../topics/logic.md) · [graph-coloring](../topics/graph-coloring.md) · [additive-combinatorics](../topics/additive-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026`](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/) | [paper.pdf](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) | [build/](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/build/) | [README.md](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [QuantitativeVanDerWaerden](../../../lean/ComparatorChallenges/QuantitativeVanDerWaerden.json) | `OAI.QuantitativeVanDerWaerden.uniform_lower_bound` | [Main.lean](../../../lean/OAI/Combinatorics/ProgressionColoring/Main.lean) | [`OAI/Combinatorics/ProgressionColoring`](../../../lean/OAI/Combinatorics/ProgressionColoring/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `QuantitativeVanDerWaerden` | [.json](../../../lean/ComparatorChallenges/QuantitativeVanDerWaerden.json) | [.lean](../../../lean/ComparatorChallenges/QuantitativeVanDerWaerden.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves Erd\H{o}s's superexponential-growth question for van der Waerden numbers. If $W_r(k)$ is the least interval length forcing a monochromatic $k$-term progression in every $r$-coloring, then $W_r(k)>k^{ck\lfloor\log_2 r\rfloor}$ for an absolute $c>0$, all $r\ge2$ and sufficiently large $k$, uniformly in $r$. In particular, $W_r(k)^{1/k}\to\infty$ for each fixed $r$.

