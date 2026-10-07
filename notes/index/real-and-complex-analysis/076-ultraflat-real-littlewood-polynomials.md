# 076 — Ultraflat real Littlewood polynomials

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/076.md`](../../../lean/docs/076.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 4 out |
| Claim shapes | bound, uniform |
| Topics | [algorithms](../topics/algorithms.md) · [harmonic-analysis](../topics/harmonic-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026`](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/) | [paper.pdf](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf) | [build/](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/) | [README.md](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/build/main.tex) | — |
| [`Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026`](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/) | [littlewood-lower-envelope.pdf](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/littlewood-lower-envelope.pdf) | [build/](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/) | [README.md](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/README.md) | no | [main.tex](../../../preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/build/main.tex) | — |
| [`Ultraflat-real-Littlewood-polynomials-October-5-2026`](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/) | [ultraflat-real-littlewood-polynomials.pdf](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/ultraflat-real-littlewood-polynomials.pdf) | [build/](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/) | [README.md](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/README.md) | no | [main.tex](../../../preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [AsymptoticallyMinimalLittlewood](../../../lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.json) | `OAI.AsymptoticallyMinimalLittlewood.main` | [Main.lean](../../../lean/OAI/Analysis/Littlewood/Main.lean) | [`OAI/Analysis/Littlewood`](../../../lean/OAI/Analysis/Littlewood/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `AsymptoticallyMinimalLittlewood` | [.json](../../../lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.json) | [.lean](../../../lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean) | 1 | 0 | no | yes |
| `LittlewoodFiniteFlatness` | [.json](../../../lean/ComparatorChallenges/LittlewoodFiniteFlatness.json) | [.lean](../../../lean/ComparatorChallenges/LittlewoodFiniteFlatness.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs polynomials with $N$ consecutive coefficients in $\{-1,1\}$ whose modulus is $(1+o(1))\sqrt N$ uniformly on the entire unit circle, for every sufficiently large integer length $N$. Thus real Littlewood polynomials are ultraflat, including at the real endpoints. Their binary merit factors tend to infinity, disproving Turyn's bounded-merit-factor conjecture.

