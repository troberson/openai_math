# Name: ren

8 families · subject name · 1 carried by a title or a declaration · 8 by prose · 7 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 24 capitalized occurrences, 18 of them mid-sentence, 9 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 8 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 7 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [073](../real-and-complex-analysis/073-falconer-distance-conjecture.md) | The Falconer distance conjecture | — | — | — | — | yes | yes |
| [074](../real-and-complex-analysis/074-kakeya-in-three-and-four-dimensions.md) | Kakeya in three and four dimensions | — | — | — | — | yes | yes |
| [077](../real-and-complex-analysis/077-fourier-restriction-for-positively-curved-surfaces.md) | Fourier restriction for positively curved surfaces | — | — | — | — | yes | yes |
| [078](../real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md) | The three-dimensional Bochner--Riesz conjecture | — | — | yes | — | yes | yes |
| [079](../real-and-complex-analysis/079-sogges-local-smoothing-conjecture-in-dimension-three.md) | Sogge's local smoothing conjecture in dimension three | — | — | — | — | yes | yes |
| [094](../convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md) | Subpolynomial dimension reduction in $L_p$ | — | — | — | — | yes | — |
| [117](../theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) | Uniform sparsest cut: hardness and semidefinite gaps | — | — | — | — | yes | yes |
| [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | The purely cosmetic surgery conjecture for knots in $S^3$ | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026`](../../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/) | [078](../real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md) | prose | [Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf](../../../preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf) |
| [`Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026`](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/) | [079](../real-and-complex-analysis/079-sogges-local-smoothing-conjecture-in-dimension-three.md) | prose | [paper.pdf](../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf) |
| [`Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026`](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/) | [077](../real-and-complex-analysis/077-fourier-restriction-for-positively-curved-surfaces.md) | prose | [Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf](../../../preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf) |
| [`Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026`](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/) | [117](../theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) | prose | [Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf) |
| [`Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/) | [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | prose | [paper.pdf](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/paper.pdf) |
| [`Subpolynomial-dimension-reduction-in-Lp-September-23-2026`](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/) | [094](../convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md) | prose | [paper.pdf](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf) |
| [`The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/) | [073](../real-and-complex-analysis/073-falconer-distance-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf) |
| [`The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026`](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/) | [074](../real-and-complex-analysis/074-kakeya-in-three-and-four-dimensions.md) | prose | [paper.pdf](../../../preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [078](../real-and-complex-analysis/078-three-dimensional-bochner-riesz-conjecture.md) | Ren--Wang, discrete form |

## Spelling variants

Every form below normalizes to the key `ren`: accents folded, dash variants unified, possessives stripped, case lowered. `Ren` · `Ren's`

