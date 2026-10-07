# Name: leng

4 families · subject name · 1 carried by a title or a declaration · 4 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 19 capitalized occurrences, 9 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [086](../real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md) | An $L^3$ bound for the trilinear Hilbert transform | — | — | yes | — | yes | yes |
| [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | Pointwise multiple ergodic averages for mixing transformations | — | — | — | — | yes | yes |
| [159](../combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemer-bounds.md) | Erd\H{o}s's reciprocal-sum conjecture and quasipolynomial Szemer\'edi bounds | — | — | — | — | yes | — |
| [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | Superexponential van der Waerden numbers | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026`](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/) | [086](../real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md) | prose | [paper.pdf](../../../preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/paper.pdf) |
| [`Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026`](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/) | [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | prose | [paper.pdf](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) |
| [`Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/) | [159](../combinatorics/159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemer-bounds.md) | prose | [paper.pdf](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) |
| [`Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026`](../../../preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/) | [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | prose | [triple-ergodic-distinct-slopes.pdf](../../../preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/triple-ergodic-distinct-slopes.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [086](../real-and-complex-analysis/086-an-l-3-bound-for-the-trilinear-hilbert-transform.md) | Leng--Sah--Sawhney |

## Spelling variants

Every form below normalizes to the key `leng`: accents folded, dash variants unified, possessives stripped, case lowered. `Leng` · `Leng's`

