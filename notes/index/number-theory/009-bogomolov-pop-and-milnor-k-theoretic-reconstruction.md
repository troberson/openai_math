# 009 — Bogomolov--Pop and Milnor $K$-theoretic reconstruction

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/009.md`](../../../lean/docs/009.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | classification |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026`](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/) | [paper.pdf](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf) | [build/](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/) | [README.md](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/README.md) | no | [main.tex](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/main.tex) | — |
| [`Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026`](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/) | [mod-ell-bogomolov-pop.pdf](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf) | [build/](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/) | [README.md](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/README.md) | no | [main.tex](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/main.tex) | — |
| [`The-Bogomolov-Pop-reconstruction-theorem-September-23-2026`](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/) | [paper.pdf](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf) | [build/](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/) | [README.md](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/README.md) | no | [paper.tex](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BogomolovPopInjectivity` | [.json](../../../lean/ComparatorChallenges/BogomolovPopInjectivity.json) | [.lean](../../../lean/ComparatorChallenges/BogomolovPopInjectivity.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Reconstructs function fields of transcendence degree at least two over algebraically closed constants from $K^{\mathrm M}_1/\ell$, $K^{\mathrm M}_2/\ell$, and their product. These data recover the perfect closure and constants when $\ell$ differs from the characteristic, and the original field and its named base in equal characteristic. Also proves Bogomolov--Pop reconstruction from abelian-by-central pro-$\ell$ Galois data away from the characteristic.

