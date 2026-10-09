# 137 — One-tape time simulation in two-fifths-power space

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/137.md`](../../../lean/docs/137.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, partial |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/) | [article.pdf](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf) | [build/](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/) | [README.md](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [OneTapeSpace](../../../lean/ComparatorChallenges/OneTapeSpace.json) | `OAI.Fifths.Single.capped` | [Main.lean](../../../lean/OAI/Computability/SpaceSimulation/Main.lean) | [`OAI/Computability/SpaceSimulation`](../../../lean/OAI/Computability/SpaceSimulation/) |
| [OneTapeSpace](../../../lean/ComparatorChallenges/OneTapeSpace.json) | `OAI.Fifths.Single.unknown` | [Main.lean](../../../lean/OAI/Computability/SpaceSimulation/Main.lean) | [`OAI/Computability/SpaceSimulation`](../../../lean/OAI/Computability/SpaceSimulation/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `OneTapeSpace` | [.json](../../../lean/ComparatorChallenges/OneTapeSpace.json) | [.lean](../../../lean/ComparatorChallenges/OneTapeSpace.lean) | 2 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines the halting and finite-control outcome of a fixed deterministic one-writable-tape machine up to time $T$ using $O(T^{2/5}\log^C(T+2))$ space, improving the square-root exponent. Heads move at most one cell per step; finitely many read-only input heads are allowed. Initial contents are independent of $T$, and contents and input symbols have polylogarithmic-space access. Simulation time is unrestricted.

