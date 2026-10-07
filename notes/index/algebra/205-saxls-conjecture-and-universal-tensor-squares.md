# 205 — Saxl's conjecture and universal tensor squares

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/205.md`](../../../lean/docs/205.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026`](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/) | [paper.pdf](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf) | [build/](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/build/) | [README.md](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/build/paper.tex) | — |
| [`Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026`](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/) | [main.pdf](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf) | [build/](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/build/) | [README.md](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/README.md) | no | [main.tex](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/build/main.tex) | [verification/](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/verification/) |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Saxl](../../../lean/ComparatorChallenges/Saxl.json) | `OAI.Saxl.saxl_conjecture` | [Main.lean](../../../lean/OAI/RepresentationTheory/Saxl/Main.lean) | [`OAI/RepresentationTheory/Saxl`](../../../lean/OAI/RepresentationTheory/Saxl/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Saxl` | [.json](../../../lean/ComparatorChallenges/Saxl.json) | [.lean](../../../lean/ComparatorChallenges/Saxl.lean) | 1 | 0 | no | yes |
| `UniversalTensorSquares` | [.json](../../../lean/ComparatorChallenges/UniversalTensorSquares.json) | [.lean](../../../lean/ComparatorChallenges/UniversalTensorSquares.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026` | [verification/](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves Saxl's conjecture: the tensor square of every staircase representation contains every irreducible complex representation of the corresponding symmetric group. More generally, every $S_n$ with $n\notin\{2,4,9\}$ has an irreducible representation whose tensor square contains all irreducibles.

