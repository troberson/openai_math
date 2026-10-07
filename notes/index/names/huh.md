# Name: huh

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 10 capitalized occurrences, 9 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | Approximate counting of common integer polymatroid bases | — | — | yes | — | yes | yes |
| [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | Sampling and counting contingency tables with arbitrary margins | — | — | — | — | yes | yes |
| [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | The Shareshian--Wachs $e$-positivity conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026`](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/) | [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | prose | [main.pdf](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf) |
| [`An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/) | [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | prose | [polymatroid-fpras.pdf](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) |
| [`Approximate-counting-of-common-bases-of-two-matroids-September-23-2026`](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/) | [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | prose | [main.pdf](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf) |
| [`Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026`](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/) | [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | prose | [paper.pdf](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf) |
| [`Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026`](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/) | [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | prose | [main.pdf](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | Branden--Huh |

## Spelling variants

Every form below normalizes to the key `huh`: accents folded, dash variants unified, possessives stripped, case lowered. `Huh` · `Huh's`

