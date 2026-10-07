# 137 — One-tape time simulation in two-fifths-power space

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T0 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | — |
| Comparator configs | 0 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, partial |
| Topics | [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/) | [article.pdf](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf) | [build/](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/) | [README.md](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/README.md) | no | [main.tex](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family, and no scope note links a comparator config.

## Comparator configs

No scope note links a comparator config for this family.

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines the halting and finite-control outcome of a fixed deterministic one-writable-tape machine up to time $T$ using $O(T^{2/5}\log^C(T+2))$ space, improving the square-root exponent. Heads move at most one cell per step; finitely many read-only input heads are allowed. Initial contents are independent of $T$, and contents and input symbols have polylogarithmic-space access. Simulation time is unrestricted.

