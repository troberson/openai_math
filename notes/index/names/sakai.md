# Name: sakai

4 families · subject name · 1 carried by a title or a declaration · 4 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 10 capitalized occurrences, 3 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

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
| [289](../operator-algebras/289-strong-kadison-kastler-conjecture.md) | The strong Kadison--Kastler conjecture | — | — | — | — | yes | yes |
| [295](../operator-algebras/295-kadison-ringrose-cohomology-conjecture.md) | The Kadison--Ringrose cohomology conjecture | — | — | — | — | yes | yes |
| [297](../operator-algebras/297-a-zfc-counterexample-to-naimarks-problem.md) | A ZFC counterexample to Naimark's problem | — | — | yes | — | yes | yes |
| [335](../differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md) | Gromov's integral scalar-curvature inequality | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026`](../../../preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/) | [297](../operator-algebras/297-a-zfc-counterexample-to-naimarks-problem.md) | prose | [naimark-counterexample-zfc.pdf](../../../preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/naimark-counterexample-zfc.pdf) |
| [`An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026`](../../../preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/) | [335](../differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md) | prose | [v126-proof.pdf](../../../preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf) |
| [`Universal-strong-Kadison-Kastler-stability-September-23-2026`](../../../preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/) | [289](../operator-algebras/289-strong-kadison-kastler-conjecture.md) | prose | [paper.pdf](../../../preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf) |
| [`Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026`](../../../preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/) | [295](../operator-algebras/295-kadison-ringrose-cohomology-conjecture.md) | prose | [paper.pdf](../../../preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [297](../operator-algebras/297-a-zfc-counterexample-to-naimarks-problem.md) | Kishimoto--Ozawa--Sakai |

## Spelling variants

Every form below normalizes to the key `sakai`: accents folded, dash variants unified, possessives stripped, case lowered. `Sakai` · `Sakai's`

