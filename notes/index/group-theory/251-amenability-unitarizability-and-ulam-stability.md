# 251 — Amenability, unitarizability, and Ulam stability

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/251.md`](../../../lean/docs/251.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 1 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [group-theory](../topics/group-theory.md) · [functional-analysis](../topics/functional-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026`](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/) | [strong-ulam-stability.pdf](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf) | [build/](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/build/) | [README.md](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/README.md) | no | [strong-ulam-stability.tex](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/build/strong-ulam-stability.tex) | — |
| [`Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026`](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/) | [paper.pdf](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf) | [build/](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/) | [README.md](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [DixmierAllDiscrete](../../../lean/ComparatorChallenges/DixmierAllDiscrete.json) | `OAI.Dixmier.current_main_theorem` | [AllDiscrete.lean](../../../lean/OAI/Analysis/Unitarizability/AllDiscrete.lean) | [`OAI/Analysis/Unitarizability`](../../../lean/OAI/Analysis/Unitarizability/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Dixmier` | [.json](../../../lean/ComparatorChallenges/Dixmier.json) | [.lean](../../../lean/ComparatorChallenges/Dixmier.lean) | 1 | 0 | no | no |
| `DixmierAllDiscrete` | [.json](../../../lean/ComparatorChallenges/DixmierAllDiscrete.json) | [.lean](../../../lean/ComparatorChallenges/DixmierAllDiscrete.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves Dixmier's problem for all discrete groups: amenability is equivalent to every uniformly bounded Hilbert-space representation being similar to a unitary representation. For countable discrete groups, amenability is also equivalent to strong Ulam stability: sufficiently accurate unitary approximate representations are uniformly close in operator norm to genuine representations on the same, possibly infinite-dimensional, Hilbert space.

