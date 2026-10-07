# Name: branden

6 families · subject name · 1 carried by a title or a declaration · 6 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 22 capitalized occurrences, 13 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 6 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [095](../convex-and-metric-geometry/095-hyperbolicity-cones-without-semidefinite-lifts.md) | Hyperbolicity cones without semidefinite lifts | — | — | — | — | yes | yes |
| [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | Approximate counting of common integer polymatroid bases | — | — | yes | — | yes | yes |
| [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | Sampling and counting contingency tables with arbitrary margins | — | — | — | — | yes | yes |
| [231](../probability-and-statistical-mechanics/231-free-uniform-spanning-forest-is-a-factor-of-iid.md) | The free uniform spanning forest is a factor of IID | — | — | — | — | yes | yes |
| [238](../probability-and-statistical-mechanics/238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md) | Optimal logarithmic mixing of the Thorp shuffle | — | — | — | — | yes | — |
| [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | Bloch's law and spontaneous ferromagnetic order | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026`](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/) | [095](../convex-and-metric-geometry/095-hyperbolicity-cones-without-semidefinite-lifts.md) | prose | [nonspectrahedral-hyperbolicity-cone.pdf](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf) |
| [`An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026`](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/) | [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | prose | [main.pdf](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf) |
| [`An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/) | [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | prose | [polymatroid-fpras.pdf](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) |
| [`Approximate-counting-of-common-bases-of-two-matroids-September-23-2026`](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/) | [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | prose | [main.pdf](../../../preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf) |
| [`Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026`](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/) | [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | prose | [bloch-law-heisenberg.pdf](../../../preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf) |
| [`Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026`](../../../preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/) | [238](../probability-and-statistical-mechanics/238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md) | prose | [paper.pdf](../../../preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/paper.pdf) |
| [`Conditional-permutations-in-a-revealed-switching-environment-September-26-2026`](../../../preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/) | [238](../probability-and-statistical-mechanics/238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md) | prose | [paper.pdf](../../../preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/paper.pdf) |
| [`Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026`](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/) | [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | prose | [main.pdf](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf) |
| [`Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026`](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/) | [095](../convex-and-metric-geometry/095-hyperbolicity-cones-without-semidefinite-lifts.md) | prose | [nonliftable-hyperbolicity.pdf](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf) |
| [`The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026`](../../../preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/) | [231](../probability-and-statistical-mechanics/231-free-uniform-spanning-forest-is-a-factor-of-iid.md) | prose | [The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf](../../../preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf) |
| [`The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/) | [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | prose | [spherical-magnetization.pdf](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | Branden--Huh |

## Spelling variants

One surface form in prose: `Branden`. The normalized key is `branden`.

