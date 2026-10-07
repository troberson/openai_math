# Name: alperin

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 25 capitalized occurrences, 18 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [202](../algebra/202-blockwise-alperin-weight-conjecture.md) | The blockwise Alperin weight conjecture | yes | yes | yes | — | yes | yes |
| [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | Donovan's conjecture over fields and discrete valuation rings | — | — | — | — | yes | yes |
| [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | A four-dimensional counterexample to Borel rigidity | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026`](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/) | [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | prose | [main.pdf](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf) |
| [`Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026`](../../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/) | [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | prose | [main.pdf](../../../preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/main.pdf) |
| [`Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/) | [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | prose | [paper.pdf](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf) |
| [`The-Blockwise-Alperin-Weight-Conjecture-September-23-2026`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/) | [202](../algebra/202-blockwise-alperin-weight-conjecture.md) | prose + title | [paper.pdf](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [202](../algebra/202-blockwise-alperin-weight-conjecture.md) | Functorial Alperin weight identity |

## Spelling variants

Every form below normalizes to the key `alperin`: accents folded, dash variants unified, possessives stripped, case lowered. `Alperin` · `Alperin's`

