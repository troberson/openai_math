# 342 — Donaldson's tamed-to-compatible conjecture

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/342.md`](../../../lean/docs/342.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | — |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [manifolds](../topics/manifolds.md) · [riemannian-geometry](../topics/riemannian-geometry.md) · [symplectic-geometry](../topics/symplectic-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Taming-implies-compatibility-on-four-manifolds-September-23-2026`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/) | [paper.pdf](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/paper.pdf) | [build/](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/build/) | [README.md](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TamingCompatibility](../../../lean/ComparatorChallenges/TamingCompatibility.json) | `OAI.TamingCompatibility.taming_implies_compatibility` | [Main.lean](../../../lean/OAI/Geometry/TamingCompatibility/Main.lean) | [`OAI/Geometry/TamingCompatibility`](../../../lean/OAI/Geometry/TamingCompatibility/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TamingCompatibility` | [.json](../../../lean/ComparatorChallenges/TamingCompatibility.json) | [.lean](../../../lean/ComparatorChallenges/TamingCompatibility.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Donaldson's tamed-to-compatible conjecture: every smooth almost complex structure on a closed four-manifold that is tamed by a symplectic form admits a compatible symplectic form. The almost complex structure stays fixed; the form's cohomology class may change.

