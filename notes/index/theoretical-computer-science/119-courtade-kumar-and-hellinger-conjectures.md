# 119 — The Courtade--Kumar and Hellinger conjectures

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/119.md`](../../../lean/docs/119.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026`](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/) | [main.pdf](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf) | [build/](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/build/) | [README.md](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/README.md) | no | [main.tex](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/build/main.tex) | [verification/](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/verification/) |
| [`Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026`](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/) | [main.pdf](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf) | [build/](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/) | [README.md](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CourtadeKumar](../../../lean/ComparatorChallenges/CourtadeKumar.json) | `OAI.LeanBlast.CourtadeKumar.courtadeKumarAndAttainment` | [Main.lean](../../../lean/OAI/InformationTheory/BooleanNoise/Main.lean) | [`OAI/InformationTheory/BooleanNoise`](../../../lean/OAI/InformationTheory/BooleanNoise/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CourtadeKumar` | [.json](../../../lean/ComparatorChallenges/CourtadeKumar.json) | [.lean](../../../lean/ComparatorChallenges/CourtadeKumar.lean) | 1 | 0 | no | yes |
| `SoftChannel204` | [.json](../../../lean/ComparatorChallenges/SoftChannel204.json) | [.lean](../../../lean/ComparatorChallenges/SoftChannel204.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026` | [verification/](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves the Courtade--Kumar conjecture: among Boolean functions of independent uniform bits, a single coordinate retains the most mutual information after independent bit-flip noise. A stronger theorem treats randomized binary summaries at fixed initial information. The Hellinger conjecture is also proved for every Boolean output bias and noise correlation.

