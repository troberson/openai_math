# Name: falconer

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 16 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [073](../real-and-complex-analysis/073-falconer-distance-conjecture.md) | The Falconer distance conjecture | yes | yes | — | yes | yes | yes |
| [084](../real-and-complex-analysis/084-geometric-case-of-the-erdos-similarity-conjecture.md) | The geometric case of the Erd\H{o}s similarity conjecture | — | — | — | — | yes | yes |
| [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | The Euclidean plane cannot be colored with five colors | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`The-Euclidean-plane-is-not-five-colorable-September-23-2026`](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/) | [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | prose | [paper.pdf](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) |
| [`The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/) | [073](../real-and-complex-analysis/073-falconer-distance-conjecture.md) | prose + title | [paper.pdf](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf) |
| [`The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026`](../../../preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/) | [084](../real-and-complex-analysis/084-geometric-case-of-the-erdos-similarity-conjecture.md) | prose | [paper.pdf](../../../preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf) |
| [`The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026`](../../../preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/) | [084](../real-and-complex-analysis/084-geometric-case-of-the-erdos-similarity-conjecture.md) | prose | [geometric-erdos-similarity.pdf](../../../preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [PlanarFalconer](../../../lean/ComparatorChallenges/PlanarFalconer.json) | `OAI.PlanarFalconer.mainTarget_proved` | [Main.lean](../../../lean/OAI/MeasureTheory/Falconer/Main.lean) | [073](../real-and-complex-analysis/073-falconer-distance-conjecture.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `falconer`: accents folded, dash variants unified, possessives stripped, case lowered. `Falconer` · `Falconer's`

