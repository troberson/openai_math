# 047 — Complex counterexamples to cancellation and affine fibrations

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/047.md`](../../../lean/docs/047.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | resolution, counterexample |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [commutative-algebra](../topics/commutative-algebra.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/) | [paper.pdf](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) | [build/](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/) | [README.md](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md) | yes | [main.tex](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ComplexCancellation](../../../lean/ComparatorChallenges/ComplexCancellation.json) | `OAI.ComplexCancellation.main` | [Main.lean](../../../lean/OAI/Algebra/AffineCancellation/Main.lean) | [`OAI/Algebra/AffineCancellation`](../../../lean/OAI/Algebra/AffineCancellation/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ComplexCancellation` | [.json](../../../lean/ComparatorChallenges/ComplexCancellation.json) | [.lean](../../../lean/ComparatorChallenges/ComplexCancellation.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with $X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over $\mathbb C$ in dimension four. It also disproves the Dolgachev--Weisfeiler affine-fibration conjecture: smooth surjections $X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine three-space but are not Zariski-locally trivial.

