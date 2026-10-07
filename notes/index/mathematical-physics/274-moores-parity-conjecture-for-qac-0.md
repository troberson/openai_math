# 274 — Moore's parity conjecture for $\mathrm{QAC}^0$

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/274.md`](../../../lean/docs/274.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026`](../../../preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/) | [paper.pdf](../../../preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/paper.pdf) | [build/](../../../preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/build/) | [README.md](../../../preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/build/main.tex) | — |
| [`Regular-trajectories-pruning-and-quantum-parity-September-24-2026`](../../../preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/) | [paper.pdf](../../../preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/paper.pdf) | [build/](../../../preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/build/) | [README.md](../../../preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [QACParity](../../../lean/ComparatorChallenges/QACParity.json) | `OAI.QAC.parity_lower_bound` | [Parity.lean](../../../lean/OAI/InformationTheory/QuantumCircuit/Parity.lean) | [`OAI/InformationTheory/QuantumCircuit`](../../../lean/OAI/InformationTheory/QuantumCircuit/) |
| [RegularParity](../../../lean/ComparatorChallenges/RegularParity.json) | `OAI.QAC.parity_lower_bound_polynomial_size` | [Main.lean](../../../lean/OAI/InformationTheory/QuantumCircuit/Main.lean) | [`OAI/InformationTheory/QuantumCircuit`](../../../lean/OAI/InformationTheory/QuantumCircuit/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `QACParity` | [.json](../../../lean/ComparatorChallenges/QACParity.json) | [.lean](../../../lean/ComparatorChallenges/QACParity.lean) | 1 | 0 | no | yes |
| `RegularParity` | [.json](../../../lean/ComparatorChallenges/RegularParity.json) | [.lean](../../../lean/ComparatorChallenges/RegularParity.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves Moore's parity conjecture in the measured-output model: constant-depth quantum circuits with arbitrary one-qubit gates, unbounded-arity Toffoli gates and polynomially many total qubits cannot compute parity with any fixed positive worst-case advantage. Ancillas start in zero, one output qubit is measured, and all other registers may be discarded. Xu--Li's reductions give the same bounded-error obstruction for strict majority.

