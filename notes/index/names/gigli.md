# Name: gigli

5 families · subject name · 1 carried by a title or a declaration · 3 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 35 capitalized occurrences, 27 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [041](../algebraic-and-complex-geometry/041-hyperk-ahler-syz-and-projective-space-bases.md) | Hyperk\"ahler SYZ and projective-space bases | — | — | — | — | — | yes |
| [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | A hyperbolic group with no geometric CAT(0) action | — | — | — | — | yes | yes |
| [356](../differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md) | Gigli's characterization of Alexandrov curvature | yes | — | yes | — | yes | yes |
| [357](../differential-geometry/357-bi-lipschitz-coordinates-at-every-regular-rcd-point.md) | Bi-Lipschitz coordinates at every regular RCD point | — | — | — | — | yes | yes |
| [374](../partial-differential-equations/374-sharp-one-third-stability-of-optimal-transport-maps.md) | Sharp one-third stability of optimal transport maps | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026`](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/) | [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | prose | [paper.pdf](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) |
| [`Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026`](../../../preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/) | [357](../differential-geometry/357-bi-lipschitz-coordinates-at-every-regular-rcd-point.md) | prose | [paper.pdf](../../../preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/paper.pdf) |
| [`Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026`](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/) | [356](../differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md) | prose | [main.pdf](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf) |
| [`Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026`](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/) | [356](../differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md) | prose | [weak-hessian-geodesics.pdf](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [356](../differential-geometry/356-giglis-characterization-of-alexandrov-curvature.md) | Gigli's characterization |

## Spelling variants

Every form below normalizes to the key `gigli`: accents folded, dash variants unified, possessives stripped, case lowered. `Gigli` · `Gigli's`

