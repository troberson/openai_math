# Name: kleiner

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 23 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [117](../theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) | Uniform sparsest cut: hardness and semidefinite gaps | — | — | — | — | yes | yes |
| [246](../group-theory/246-cannons-conjecture.md) | Cannon's conjecture | — | — | yes | — | yes | — |
| [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | A hyperbolic group with no geometric CAT(0) action | — | — | — | — | yes | yes |
| [337](../differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md) | Cartan--Hadamard isoperimetry and CAT$(0)$ fillings | — | — | — | — | yes | yes |
| [355](../differential-geometry/355-unique-tangent-flows-at-the-first-surface-singularity.md) | Unique tangent flows at the first surface singularity | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026`](../../../preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/) | [246](../group-theory/246-cannons-conjecture.md) | prose | [paper.pdf](../../../preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf) |
| [`A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026`](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/) | [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | prose | [paper.pdf](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) |
| [`Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026`](../../../preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/) | [337](../differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md) | prose | [paper.pdf](../../../preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf) |
| [`Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026`](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/) | [117](../theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) | prose | [Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf) |
| [`Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026`](../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/) | [337](../differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md) | prose | [paper.pdf](../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf) |
| [`Tangent-flow-uniqueness-2026-09-24`](../../../preprints/Tangent-flow-uniqueness-2026-09-24/) | [355](../differential-geometry/355-unique-tangent-flows-at-the-first-surface-singularity.md) | prose | [paper.pdf](../../../preprints/Tangent-flow-uniqueness-2026-09-24/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [246](../group-theory/246-cannons-conjecture.md) | Bonk--Kleiner; Bourdon--Kleiner |
| [246](../group-theory/246-cannons-conjecture.md) | Bonk--Kleiner; Bourdon--Kleiner |

## Spelling variants

Every form below normalizes to the key `kleiner`: accents folded, dash variants unified, possessives stripped, case lowered. `Kleiner` · `Kleiner's`

