# Name: trotter

5 families · subject name · 1 carried by a title or a declaration · 4 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 10 capitalized occurrences, 7 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [106](../theoretical-computer-science/106-hardness-of-coloring-three-colorable-graphs.md) | Hardness of coloring three-colorable graphs | — | — | — | — | — | yes |
| [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | The higher-dimensional Erd\H{o}s distinct-distances conjecture | — | — | yes | — | yes | yes |
| [167](../combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) | Pinned distances and a power saving for planar unit distances | — | — | — | — | yes | yes |
| [171](../combinatorics/171-hypercube-ramsey-conjecture.md) | The hypercube Ramsey conjecture | — | — | — | — | yes | — |
| [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | Bloch's law and spontaneous ferromagnetic order | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-power-saving-for-planar-unit-distances-September-23-2026`](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/) | [167](../combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) | prose | [paper.pdf](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) |
| [`The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/) | [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | prose | [paper.pdf](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) |
| [`The-hypercube-Ramsey-number-has-linear-order-September-23-2026`](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/) | [171](../combinatorics/171-hypercube-ramsey-conjecture.md) | prose | [paper.pdf](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf) |
| [`The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/) | [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | prose | [spherical-magnetization.pdf](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | Szemeredi--Trotter |

## Spelling variants

One surface form in prose: `Trotter`. The normalized key is `trotter`.

