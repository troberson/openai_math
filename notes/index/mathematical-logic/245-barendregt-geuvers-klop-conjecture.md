# 245 — The $\beta$-Barendregt--Geuvers--Klop conjecture

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/245.md`](../../../lean/docs/245.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Topics | [logic](../topics/logic.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Weak-and-strong-normalization-in-pure-type-systems-September-25-2026`](../../../preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/) | [paper.pdf](../../../preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/paper.pdf) | [build/](../../../preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/build/) | [README.md](../../../preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/README.md) | no | [paper.tex](../../../preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TypeSystemNormalization` | [.json](../../../lean/ComparatorChallenges/TypeSystemNormalization.json) | [.lean](../../../lean/ComparatorChallenges/TypeSystemNormalization.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that weak normalization implies strong normalization for every pure type system: if every legal expression in every valid context has a $\beta$-normal form, every $\beta$-reduction sequence terminates. This resolves the $\beta$-Barendregt--Geuvers--Klop conjecture, including nonfunctional rules and open contexts.

