# Name: oka

7 families · subject name · 1 carried by a title or a declaration · 7 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 44 capitalized occurrences, 41 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 7 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | Log abundance and effective Iitaka fibrations | — | — | — | — | yes | — |
| [042](../algebraic-and-complex-geometry/042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md) | Oka classification for K3 surfaces and other compact complex surfaces | yes | yes | yes | — | yes | — |
| [051](../algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md) | Kobayashi's canonical-ampleness conjecture | — | — | — | — | yes | — |
| [057](../algebraic-and-complex-geometry/057-campanas-abelianity-conjecture-and-special-varieties.md) | Campana's abelianity conjecture and special varieties | — | — | — | — | yes | — |
| [058](../algebraic-and-complex-geometry/058-koll-pardon-universal-cover-conjecture.md) | The Koll\'ar--Pardon universal-cover conjecture | — | — | — | — | yes | — |
| [338](../differential-geometry/338-yaus-uniformization-conjecture.md) | Yau's uniformization conjecture | — | — | — | — | yes | — |
| [372](../partial-differential-equations/372-global-uniqueness-in-smooth-isotropic-elasticity.md) | Global uniqueness in smooth isotropic elasticity | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026`](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/) | [051](../algebraic-and-complex-geometry/051-kobayashis-canonical-ampleness-conjecture.md) | prose | [canonical-ampleness.pdf](../../../preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/canonical-ampleness.pdf) |
| [`Every-complex-K3-surface-is-Oka-September-23-2026`](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/) | [042](../algebraic-and-complex-geometry/042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md) | prose + title | [paper.pdf](../../../preprints/Every-complex-K3-surface-is-Oka-September-23-2026/paper.pdf) |
| [`Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026`](../../../preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/) | [372](../partial-differential-equations/372-global-uniqueness-in-smooth-isotropic-elasticity.md) | prose | [article.pdf](../../../preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf) |
| [`Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026`](../../../preprints/Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [paper.pdf](../../../preprints/Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026/paper.pdf) |
| [`Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026`](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/) | [058](../algebraic-and-complex-geometry/058-koll-pardon-universal-cover-conjecture.md) | prose | [paper.pdf](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/paper.pdf) |
| [`The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/) | [057](../algebraic-and-complex-geometry/057-campanas-abelianity-conjecture-and-special-varieties.md) | prose | [paper.pdf](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/paper.pdf) |
| [`Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026`](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/) | [338](../differential-geometry/338-yaus-uniformization-conjecture.md) | prose | [paper.pdf](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [042](../algebraic-and-complex-geometry/042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md) | Oka surfaces in Kodaira dimension zero and class VII |

## Spelling variants

One surface form in prose: `Oka`. The normalized key is `oka`.

