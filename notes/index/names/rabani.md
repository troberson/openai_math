# Name: rabani

6 families · subject name · 1 carried by a title or a declaration · 4 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 25 capitalized occurrences, 18 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs | — | — | — | — | yes | yes |
| [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | The sharp distortion of edit distance into $\ell_1$ | — | — | yes | — | yes | — |
| [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | The Unique Games Conjecture and optimal approximation thresholds | — | — | — | — | yes | yes |
| [110](../theoretical-computer-science/110-optimal-order-randomized-k-server-on-arbitrary-metrics.md) | Optimal-order randomized $k$-server on arbitrary metrics | — | — | — | — | — | yes |
| [117](../theoretical-computer-science/117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) | Uniform sparsest cut: hardness and semidefinite gaps | — | — | — | — | — | yes |
| [121](../theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md) | Almost-linear expected-time approximation of edit distance | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/) | [121](../theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md) | prose | [paper.pdf](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf) |
| [`Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026`](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/) | [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | prose | [paper.pdf](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf) |
| [`Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026`](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/) | [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | prose | [paper.pdf](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf) |
| [`L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/) | [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | prose | [paper.pdf](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) |
| [`Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/) | [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | prose | [paper.pdf](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf) |
| [`The-Unique-Games-Theorem-September-23-2026`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/) | [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | prose | [paper.pdf](../../../preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) |
| [`Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026`](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/) | [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | prose | [paper.pdf](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | Ostrovsky--Rabani, normalized form |

## Spelling variants

One surface form in prose: `Rabani`. The normalized key is `rabani`.

