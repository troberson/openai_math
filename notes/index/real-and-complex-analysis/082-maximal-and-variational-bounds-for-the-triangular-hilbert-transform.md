# 082 — Maximal and variational bounds for the triangular Hilbert transform

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/082.md`](../../../lean/docs/082.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026`](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/) | [dyadic-triangular-hilbert.pdf](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/dyadic-triangular-hilbert.pdf) | [build/](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/build/) | [README.md](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/README.md) | no | [main.tex](../../../preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/build/main.tex) | — |
| [`Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026`](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/) | [annular-variation.pdf](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/annular-variation.pdf) | [build/](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/) | [README.md](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/README.md) | no | [main.tex](../../../preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/build/main.tex) | — |
| [`The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026`](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/) | [paper.pdf](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf) | [build/](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/) | [README.md](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/README.md) | yes | [preamble.tex](../../../preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/build/preamble.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TriangularHilbert](../../../lean/ComparatorChallenges/TriangularHilbert.json) | `OAI.TriangularHilbert.main_estimate` | [Main.lean](../../../lean/OAI/Analysis/TriangularHilbert/Main.lean) | [`OAI/Analysis/TriangularHilbert`](../../../lean/OAI/Analysis/TriangularHilbert/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TriangularHilbert` | [.json](../../../lean/ComparatorChallenges/TriangularHilbert.json) | [.lean](../../../lean/ComparatorChallenges/TriangularHilbert.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves maximal and annular $r$-variation bounds, for every $r>2$, from complex $L^3(\mathbb R^2)\times L^3(\mathbb R^2)$ to $L^{3/2}(\mathbb R^2)$. The maximal estimate controls both hard truncation endpoints and gives almost-everywhere and norm convergence. Pairing with a third input settles the triangular Hilbert transform estimate at the symmetric $L^3\times L^3\times L^3$ point.

