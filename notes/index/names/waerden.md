# Name: waerden

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 13 capitalized occurrences, 9 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [159](../combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemer-bounds.md) | Erd\H{o}s's reciprocal-sum conjecture and quasipolynomial Szemer\'edi bounds | — | — | — | — | yes | — |
| [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | Superexponential van der Waerden numbers | yes | yes | — | yes | yes | — |
| [164](../combinatorics/164-hindmans-finite-sums-and-products-conjecture.md) | Hindman's finite sums and products conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026`](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/) | [164](../combinatorics/164-hindmans-finite-sums-and-products-conjecture.md) | prose | [paper.pdf](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf) |
| [`Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026`](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/) | [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | prose + title | [paper.pdf](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) |
| [`Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/) | [159](../combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemer-bounds.md) | prose | [paper.pdf](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [QuantitativeVanDerWaerden](../../../lean/ComparatorChallenges/QuantitativeVanDerWaerden.json) | `OAI.QuantitativeVanDerWaerden.uniform_lower_bound` | [Main.lean](../../../lean/OAI/Combinatorics/ProgressionColoring/Main.lean) | [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `waerden`: accents folded, dash variants unified, possessives stripped, case lowered. `Waerden` · `Waerden's`

