# Name: ulam

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 29 capitalized occurrences, 27 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [144](../dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md) | Banach's simple Lebesgue-spectrum problem | — | — | — | — | yes | yes |
| [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | The higher-dimensional Erd\H{o}s distinct-distances conjecture | — | — | — | — | yes | — |
| [251](../group-theory/251-amenability-unitarizability-and-ulam-stability.md) | Amenability, unitarizability, and Ulam stability | yes | yes | — | — | yes | — |
| [289](../operator-algebras/289-strong-kadison-kastler-conjecture.md) | The strong Kadison--Kastler conjecture | — | — | — | — | yes | — |
| [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | Tingley's sphere-isometry problem | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-positive-solution-to-Tingleys-problem-September-23-2026`](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/) | [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | prose | [paper.pdf](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf) |
| [`A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026`](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/) | [144](../dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md) | prose | [paper.pdf](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf) |
| [`Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026`](../../../preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/) | [289](../operator-algebras/289-strong-kadison-kastler-conjecture.md) | prose | [paper.pdf](../../../preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/paper.pdf) |
| [`Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026`](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/) | [251](../group-theory/251-amenability-unitarizability-and-ulam-stability.md) | prose + title | [strong-ulam-stability.pdf](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf) |
| [`The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/) | [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | prose | [paper.pdf](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Ulam`. The normalized key is `ulam`.

