# 133 — The complexity of Weisfeiler--Leman refinement

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 4 (0 formalized at source level) |
| Scope note | [`lean/docs/133.md`](../../../lean/docs/133.md) |
| Comparator configs | 4 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 3 out |
| Claim shapes | bound |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [paper.pdf](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) | [build/](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/) | [README.md](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/README.md) | no | [main.tex](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex) | — |
| [`The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026`](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/) | [paper.pdf](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf) | [build/](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/) | [README.md](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/README.md) | no | [paper.tex](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/paper.tex) | — |
| [`Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [paper.pdf](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) | [build/](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/) | [README.md](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/README.md) | no | [main.tex](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex) | — |
| [`Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026`](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/) | [paper.pdf](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf) | [build/](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/) | [README.md](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/README.md) | no | [main.tex](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 4 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ParityLifts` | [.json](../../../lean/ComparatorChallenges/ParityLifts.json) | [.lean](../../../lean/ComparatorChallenges/ParityLifts.lean) | 1 | 0 | no | no |
| `VariableWL` | [.json](../../../lean/ComparatorChallenges/VariableWL.json) | [.lean](../../../lean/ComparatorChallenges/VariableWL.lean) | 1 | 0 | no | no |
| `WLIdentification` | [.json](../../../lean/ComparatorChallenges/WLIdentification.json) | [.lean](../../../lean/ComparatorChallenges/WLIdentification.lean) | 1 | 0 | no | no |
| `WeisfeilerLeman` | [.json](../../../lean/ComparatorChallenges/WeisfeilerLeman.json) | [.lean](../../../lean/ComparatorChallenges/WeisfeilerLeman.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves unconditional $n^{\Omega(k)}$ deterministic time lower bounds for joint and separate $k$-dimensional Weisfeiler--Leman equivalence, for sufficiently large fixed $k$ in the specified sequential adjacency-matrix models. With dimension as input, joint equivalence is EXPTIME-complete even on subcubic graphs; deciding whether refinement identifies a graph is also EXPTIME-complete.

