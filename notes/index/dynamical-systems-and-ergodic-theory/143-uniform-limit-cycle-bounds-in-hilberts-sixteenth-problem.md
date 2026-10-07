# 143 — Uniform limit-cycle bounds in Hilbert's sixteenth problem

|  |  |
|---|---|
| Discipline | [Dynamical systems and ergodic theory](../disciplines/dynamical-systems-and-ergodic-theory.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/143.md`](../../../lean/docs/143.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [dynamical-systems](../topics/dynamical-systems.md) · [hilbert-problems](../topics/hilbert-problems.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`two-limit-cycles-for-quintic-lienard-systems-September-24-2026`](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/) | [two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf) | [build/](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/build/) | [README.md](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/build/paper.tex) | — |
| [`uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026`](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/) | [uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf) | [build/](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/) | [README.md](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/README.md) | no | [main.tex](../../../preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [QuinticLienard](../../../lean/ComparatorChallenges/QuinticLienard.json) | `OAI.QuinticLienard.main` | [Main.lean](../../../lean/OAI/Analysis/LienardCycles/Main.lean) | [`OAI/Analysis/LienardCycles`](../../../lean/OAI/Analysis/LienardCycles/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `QuinticLienard` | [.json](../../../lean/ComparatorChallenges/QuinticLienard.json) | [.lean](../../../lean/ComparatorChallenges/QuinticLienard.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the uniform boundedness assertion in Hilbert's sixteenth problem: the number of isolated periodic orbits of a real planar polynomial vector field is bounded by a finite constant depending only on its degree. For classical quintic Li\'enard systems, the exact maximum is two limit cycles.

