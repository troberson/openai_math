# 359 — Negative K\"ahler curvature without bounded holomorphic coordinates

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/359.md`](../../../lean/docs/359.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | bound, partial |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026`](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/) | [paper.pdf](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf) | [build/](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/) | [README.md](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/README.md) | yes | [main.tex](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/main.tex) | — |
| [`One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026`](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/) | [paper.pdf](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf) | [build/](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/build/) | [README.md](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/README.md) | no | [main.tex](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PinchedKahler](../../../lean/ComparatorChallenges/PinchedKahler.json) | `OAI.PinchedHartogs.main_theorem` | [Main.lean](../../../lean/OAI/Geometry/Kahler/Main.lean) | [`OAI/Geometry/Kahler`](../../../lean/OAI/Geometry/Kahler/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PinchedKahler` | [.json](../../../lean/ComparatorChallenges/PinchedKahler.json) | [.lean](../../../lean/ComparatorChallenges/PinchedKahler.lean) | 3 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a contractible domain in $\mathbb C^3$ with a complete negatively pinched K\"ahler metric but no bounded holomorphic coordinates, disproving bounded-domain uniformization in this setting. A higher-dimensional example has sectional curvature at most $-1$ and only constant bounded holomorphic functions; its curvature is not bounded below.

