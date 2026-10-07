# Name: seymour

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 17 capitalized occurrences, 14 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs | — | — | — | — | yes | yes |
| [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | The Unique Games Conjecture and optimal approximation thresholds | — | — | — | — | yes | yes |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | yes | yes |
| [173](../combinatorics/173-seymours-second-neighborhood-conjecture.md) | Seymour's second-neighborhood conjecture | yes | — | — | yes | yes | — |
| [224](../probability-and-statistical-mechanics/224-critical-and-near-critical-universality-for-voronoi-percolation.md) | Critical and near-critical universality for Voronoi percolation | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) |
| [`A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026`](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/) | [173](../combinatorics/173-seymours-second-neighborhood-conjecture.md) | prose | [paper.pdf](../../../preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf) |
| [`Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026`](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/) | [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | prose | [paper.pdf](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf) |
| [`From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026`](../../../preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/) | [224](../probability-and-statistical-mechanics/224-critical-and-near-critical-universality-for-voronoi-percolation.md) | prose | [critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf](../../../preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf) |
| [`L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/) | [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | prose | [paper.pdf](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) |
| [`Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/) | [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | prose | [paper.pdf](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [SeymourSecondNeighborhood](../../../lean/ComparatorChallenges/SeymourSecondNeighborhood.json) | `OAI.SeymourSecondNeighborhood.exists_goodVertex` | [Main.lean](../../../lean/OAI/Combinatorics/SecondNeighborhood/Main.lean) | [173](../combinatorics/173-seymours-second-neighborhood-conjecture.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `seymour`: accents folded, dash variants unified, possessives stripped, case lowered. `Seymour` · `Seymour's`

