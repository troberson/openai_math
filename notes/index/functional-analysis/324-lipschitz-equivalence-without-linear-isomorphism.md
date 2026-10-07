# 324 — Lipschitz equivalence without linear isomorphism

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/324.md`](../../../lean/docs/324.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 2 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/) | [paper.pdf](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf) | [build/](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/) | [README.md](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/README.md) | yes | [main.tex](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/main.tex) | — |
| [`Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/) | [paper.pdf](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf) | [build/](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/) | [README.md](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [C0Absorption](../../../lean/ComparatorChallenges/C0Absorption.json) | `OAI.C0Absorption.main_result` | [Main.lean](../../../lean/OAI/Analysis/C0Absorption/Main.lean) | [`OAI/Analysis/C0Absorption`](../../../lean/OAI/Analysis/C0Absorption/) |
| [LipschitzEquivalence](../../../lean/ComparatorChallenges/LipschitzEquivalence.json) | `OAI.LipschitzCounterexample.main` | [Main.lean](../../../lean/OAI/Analysis/LipschitzEquivalence/Main.lean) | [`OAI/Analysis/LipschitzEquivalence`](../../../lean/OAI/Analysis/LipschitzEquivalence/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `C0Absorption` | [.json](../../../lean/ComparatorChallenges/C0Absorption.json) | [.lean](../../../lean/ComparatorChallenges/C0Absorption.lean) | 1 | 0 | no | yes |
| `LipschitzEquivalence` | [.json](../../../lean/ComparatorChallenges/LipschitzEquivalence.json) | [.lean](../../../lean/ComparatorChallenges/LipschitzEquivalence.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic, resolving the separable Lipschitz-isomorphism problem negatively. Thus even the complete metric structure up to bi-Lipschitz equivalence does not determine a separable Banach space's linear isomorphism class.

