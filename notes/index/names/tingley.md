# Name: tingley

3 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 15 capitalized occurrences, 9 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [044](../algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md) | The equivariant cohomological Hikita conjecture for quivers | — | — | — | — | yes | yes |
| [254](../group-theory/254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md) | Classifying spaces and geometric obstructions for Artin groups | — | — | — | — | — | yes |
| [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | Tingley's sphere-isometry problem | yes | — | — | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-positive-solution-to-Tingleys-problem-September-23-2026`](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/) | [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | prose | [paper.pdf](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf) |
| [`The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/) | [044](../algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md) | prose | [main.pdf](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [TingleySphereIsometry](../../../lean/ComparatorChallenges/TingleySphereIsometry.json) | `OAI.Tingley.tingley_sphere_isometry_full` | [Extension.lean](../../../lean/OAI/Analysis/SphereIsometry/Extension.lean) | [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `tingley`: accents folded, dash variants unified, possessives stripped, case lowered. `Tingley's` · `Tingley`

