# Name: salamon

4 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 20 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [062](../algebraic-and-complex-geometry/062-lebrun-salamon-conjecture-and-projective-contact-classification.md) | The LeBrun--Salamon conjecture and projective contact classification | yes | yes | — | — | yes | — |
| [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | Conformal universality for weakly interacting and disordered Ising models | — | — | — | — | yes | yes |
| [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | Donaldson's hypersymplectic deformation conjecture | — | — | — | — | — | yes |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Counterexamples to strong forms of Arnold's fixed-point conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026`](../../../preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [paper.pdf](../../../preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf) |
| [`Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/) | [062](../algebraic-and-complex-geometry/062-lebrun-salamon-conjecture-and-projective-contact-classification.md) | prose + title | [paper.pdf](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/paper.pdf) |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [paper.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [hamiltonian-fixed-points-below-stable-morse-number.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Salamon`. The normalized key is `salamon`.

