# 124 — Polynomial-time scheduling on three identical machines

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/124.md`](../../../lean/docs/124.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026`](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/) | [paper.pdf](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) | [build/](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/) | [README.md](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/README.md) | no | [paper.tex](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ThreeMachine` | [.json](../../../lean/ComparatorChallenges/ThreeMachine.json) | [.lean](../../../lean/ComparatorChallenges/ThreeMachine.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the three-processor unit-job scheduling problem of Garey and Johnson: a deterministic polynomial-time algorithm minimizes makespan for nonpreemptive unit-length jobs with arbitrary precedence constraints on three identical parallel machines. For an explicitly given precedence graph, it decides deadline feasibility exactly and constructs a feasible schedule.

