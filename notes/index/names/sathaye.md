# Name: sathaye

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 9 capitalized occurrences, 4 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [049](../algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md) | A stable-coordinate counterexample in four variables | — | — | — | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026`](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/) | [049](../algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md) | prose | [stable-coordinate-four-variables.pdf](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf) |
| [`An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026`](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/) | [049](../algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md) | prose | [paper.pdf](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [AbhyankarSathaye](../../../lean/ComparatorChallenges/AbhyankarSathaye.json) | `OAI.AbhyankarSathaye.exists_noncoordinate_polynomial` | [Counterexample.lean](../../../lean/OAI/AlgebraicGeometry/AbhyankarSathaye/Counterexample.lean) | [049](../algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md) |
| [CommutingDerivations](../../../lean/ComparatorChallenges/CommutingDerivations.json) | `OAI.AbhyankarSathaye.CommutingDerivations.commuting_derivations_with_ordinary_extras` | [OrdinaryExtraMain.lean](../../../lean/OAI/AlgebraicGeometry/CommutingDerivations/OrdinaryExtraMain.lean) | [049](../algebraic-and-complex-geometry/049-a-stable-coordinate-counterexample-in-four-variables.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Sathaye`. The normalized key is `sathaye`.

