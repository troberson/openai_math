# 197 — Nonsofic groups and group-ring counterexamples

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 4 (3 formalized at source level) |
| Scope note | [`lean/docs/197.md`](../../../lean/docs/197.md) |
| Comparator configs | 4 (3 with a `main_results` declaration) |
| Reasoning trace | [kaplansky-direct-finiteness-characteristic-two](../../../reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 6 out |
| Claim shapes | counterexample |
| Companion families | — |
| Summary page | [197-nonsofic-groups-and-group-ring-counterexamples.md](../../../notes/summaries/algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026`](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/) | [paper.pdf](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/) | [README.md](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/paper.tex) | — |
| [`A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026`](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/) | [paper.pdf](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf) | [build/](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/build/) | [README.md](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/README.md) | yes | [paper.tex](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/build/paper.tex) | — |
| [`A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026`](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/build/main.tex) | — |
| [`A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026`](../../../preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/) | [direct-finiteness.pdf](../../../preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/direct-finiteness.pdf) | [build/](../../../preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/build/) | [README.md](../../../preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/README.md) | no | [paper.tex](../../../preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GroupRingDeterminant](../../../lean/ComparatorChallenges/GroupRingDeterminant.json) | `OAI.GroupRingDeterminant.main` | [Main.lean](../../../lean/OAI/Analysis/GroupDeterminants/Main.lean) | [`OAI/Analysis/GroupDeterminants`](../../../lean/OAI/Analysis/GroupDeterminants/) |
| [KaplanskyFinitelyPresented](../../../lean/ComparatorChallenges/KaplanskyFinitelyPresented.json) | `OAI.KaplanskyCounterexample.finitelyPresented_counterexample` | [FinitelyPresented.lean](../../../lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean) | [`OAI/RingTheory/DirectFiniteness`](../../../lean/OAI/RingTheory/DirectFiniteness/) |
| [OddKaplansky](../../../lean/ComparatorChallenges/OddKaplansky.json) | `OAI.OddKaplansky.main_theorem` | [Main.lean](../../../lean/OAI/Algebra/OddKaplansky/Main.lean) | [`OAI/Algebra/OddKaplansky`](../../../lean/OAI/Algebra/OddKaplansky/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GroupRingDeterminant` | [.json](../../../lean/ComparatorChallenges/GroupRingDeterminant.json) | [.lean](../../../lean/ComparatorChallenges/GroupRingDeterminant.lean) | 1 | 0 | no | yes |
| `KaplanskyDirectFiniteness` | [.json](../../../lean/ComparatorChallenges/KaplanskyDirectFiniteness.json) | [.lean](../../../lean/ComparatorChallenges/KaplanskyDirectFiniteness.lean) | 1 | 0 | no | no |
| `KaplanskyFinitelyPresented` | [.json](../../../lean/ComparatorChallenges/KaplanskyFinitelyPresented.json) | [.lean](../../../lean/ComparatorChallenges/KaplanskyFinitelyPresented.lean) | 1 | 0 | no | yes |
| `OddKaplansky` | [.json](../../../lean/ComparatorChallenges/OddKaplansky.json) | [.lean](../../../lean/ComparatorChallenges/OddKaplansky.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a finitely presented torsion-free nonsofic group whose group algebra over $\mathbb F_2$ is not directly finite, disproving Kaplansky's conjecture even without torsion. Companion examples give injective nonsurjective cellular automata on all configurations, refuting Gottschalk's surjunctivity conjecture. Another counterexample is an integral group-ring matrix, invertible over the rational group ring, with Fuglede--Kadison determinant strictly between zero and one, disproving the unrestricted Determinant Conjecture.

