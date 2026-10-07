# Name: servedio

7 families · subject name · 1 carried by a title or a declaration · 6 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 32 capitalized occurrences, 20 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 6 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | Superpolynomial lower bounds and quasipolynomial reconstruction from deletion traces | — | — | — | — | yes | yes |
| [127](../theoretical-computer-science/127-asymptotic-gotsman-linial-conjecture.md) | The asymptotic Gotsman--Linial conjecture | — | — | — | — | yes | — |
| [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | Subset Sum in $O(2^{0.49n})$ time | — | — | — | — | yes | yes |
| [192](../combinatorics/192-a-counterexample-to-the-gopalan-servedio-conjecture.md) | A counterexample to the Gopalan--Servedio conjecture | yes | — | — | — | yes | — |
| [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | No infinite critical clusters on quasi-transitive graphs | — | — | — | — | — | yes |
| [214](../probability-and-statistical-mechanics/214-benjamini-schramm-nonuniqueness-conjecture.md) | The Benjamini--Schramm nonuniqueness conjecture | — | — | — | — | yes | — |
| [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | Conformal universality for weakly interacting and disordered Ising models | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026`](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/) | [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | prose | [paper.pdf](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf) |
| [`A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026`](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/) | [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | prose | [paper.pdf](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf) |
| [`Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026`](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/) | [127](../theoretical-computer-science/127-asymptotic-gotsman-linial-conjecture.md) | prose | [main.pdf](../../../preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) |
| [`Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026`](../../../preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [critical-relative-second-moment-weak-random-bond-ising.pdf](../../../preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/critical-relative-second-moment-weak-random-bond-ising.pdf) |
| [`Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026`](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/) | [214](../probability-and-statistical-mechanics/214-benjamini-schramm-nonuniqueness-conjecture.md) | prose | [paper.pdf](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) |
| [`Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026`](../../../preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [quenched-sle3-weak-random-bond-ising.pdf](../../../preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/quenched-sle3-weak-random-bond-ising.pdf) |
| [`Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026`](../../../preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [general-weak-random-bond-ising.pdf](../../../preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/general-weak-random-bond-ising.pdf) |
| [`Subset-Sum-in-Time-2-power-0-49n-October-4-2026`](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/) | [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | prose | [subset-sum.pdf](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf) |
| [`Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026`](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/) | [192](../combinatorics/192-a-counterexample-to-the-gopalan-servedio-conjecture.md) | prose | [Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf) |
| [`Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026`](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/) | [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | prose | [uniform-trace-reconstruction.pdf](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf) |
| [`quantitative-lower-bounds-for-trace-reconstruction-September-24-2026`](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/) | [122](../theoretical-computer-science/122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) | prose | [paper.pdf](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Servedio`. The normalized key is `servedio`.

