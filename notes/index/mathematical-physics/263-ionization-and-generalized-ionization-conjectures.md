# 263 — The ionization and generalized ionization conjectures

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/263.md`](../../../lean/docs/263.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 3 out |
| Claim shapes | bound, partial |
| Topics | [mathematical-physics](../topics/mathematical-physics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026`](../../../preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/) | [paper.pdf](../../../preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf) | [build/](../../../preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/build/) | [README.md](../../../preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/build/paper.tex) | — |
| [`Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026`](../../../preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/) | [paper.pdf](../../../preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/paper.pdf) | [build/](../../../preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/build/) | [README.md](../../../preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/README.md) | no | [paper.tex](../../../preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/build/paper.tex) | — |
| [`Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026`](../../../preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/) | [paper.pdf](../../../preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) | [build/](../../../preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/build/) | [README.md](../../../preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/README.md) | no | [main.tex](../../../preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CoulombIonization](../../../lean/ComparatorChallenges/CoulombIonization.json) | `OAI.CoulombAtom.generalized_ionization` | [Main.lean](../../../lean/OAI/Analysis/CoulombIonization/Main.lean) | [`OAI/Analysis/CoulombIonization`](../../../lean/OAI/Analysis/CoulombIonization/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CoulombIonization` | [.json](../../../lean/ComparatorChallenges/CoulombIonization.json) | [.lean](../../../lean/ComparatorChallenges/CoulombIonization.lean) | 1 | 0 | no | yes |
| `CoulombRadii` | [.json](../../../lean/ComparatorChallenges/CoulombRadii.json) | [.lean](../../../lean/ComparatorChallenges/CoulombRadii.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For the full nonrelativistic Coulomb model with two electron spin states, proves that a molecule with $M$ fixed nuclei of charges at least one and total charge $Z$ strictly binds at most $Z+CM$ electrons. Neutral-atom first ionization energies and radii containing all but an expected half-electron have universal positive upper and lower bounds. The energy cost of removing $m$ electrons has Thomas--Fermi asymptotics as $m\to\infty$ and $Z/m\to\infty$; neutral-atom outer radii have the corresponding iterated-limit asymptotics, taking $Z\to\infty$ first.

