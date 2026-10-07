# Name: brenier

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 11 capitalized occurrences, 10 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [101](../convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md) | The sharp simplex conjecture for isotropic constants | — | — | — | — | yes | yes |
| [374](../partial-differential-equations/374-sharp-one-third-stability-of-optimal-transport-maps.md) | Sharp one-third stability of optimal transport maps | — | yes | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/) | [101](../convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md) | prose | [isotropic-simplex.pdf](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf) |
| [`Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026`](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/) | [374](../partial-differential-equations/374-sharp-one-third-stability-of-optimal-transport-maps.md) | prose + title | [article.pdf](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `brenier`: accents folded, dash variants unified, possessives stripped, case lowered. `Brenier` · `Brenier's`

