# 281 — QAOA optimality for the SK model

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/281.md`](../../../lean/docs/281.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [graph-theory](../topics/graph-theory.md) · [complexity-theory](../topics/complexity-theory.md) · [disordered-systems](../topics/disordered-systems.md) · [condensed-matter](../topics/condensed-matter.md) · [probability](../topics/probability.md) · [quantum-computing](../topics/quantum-computing.md) · [random-graphs](../topics/random-graphs.md) · [spin-glasses](../topics/spin-glasses.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026`](../../../preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/) | [main.pdf](../../../preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf) | [build/](../../../preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/) | [README.md](../../../preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/README.md) | no | [main.tex](../../../preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/main.tex) | — |
| [`QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026`](../../../preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/) | [QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf](../../../preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf) | [build/](../../../preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/) | [README.md](../../../preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/README.md) | no | [main.tex](../../../preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SKFullSupport` | [.json](../../../lean/ComparatorChallenges/SKFullSupport.json) | [.lean](../../../lean/ComparatorChallenges/SKFullSupport.lean) | 1 | 0 | no | no |
| `SKValue` | [.json](../../../lean/ComparatorChallenges/SKValue.json) | [.lean](../../../lean/ComparatorChallenges/SKValue.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that QAOA approaches the ground-state energy of the Gaussian zero-field Sherrington--Kirkpatrick model when system size tends to infinity before circuit depth. For every accuracy, finite depth and deterministic angles independent of size and disorder achieve the required limiting expected energy per spin. This also yields leading-order optimal expected MaxCut values on large-degree random regular graphs, with size tending to infinity before degree.

