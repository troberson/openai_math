# Name: hadwiger

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 37 capitalized occurrences, 29 of them mid-sentence, 3 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | yes | yes | — | yes | yes | yes |
| [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | The Euclidean plane cannot be colored with five colors | — | — | — | — | yes | yes |
| [354](../differential-geometry/354-isoperimetric-regions-in-the-cubic-three-torus.md) | Isoperimetric regions in the cubic three-torus | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) |
| [`A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf) |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose + title | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) |
| [`The-Euclidean-plane-is-not-five-colorable-September-23-2026`](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/) | [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | prose | [paper.pdf](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) |
| [`The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026`](../../../preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/) | [354](../differential-geometry/354-isoperimetric-regions-in-the-cubic-three-torus.md) | prose | [article.pdf](../../../preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [HadwigerCounterexample](../../../lean/ComparatorChallenges/HadwigerCounterexample.json) | `OAI.HadwigerCounterexample.not_hadwiger_conjecture` | [Main.lean](../../../lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `hadwiger`: accents folded, dash variants unified, possessives stripped, case lowered. `Hadwiger` · `Hadwiger's`

