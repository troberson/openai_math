# Name: friedgut

6 families · subject name · 2 carried by a title or a declaration · 5 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 41 capitalized occurrences, 15 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 2 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | The Unique Games Conjecture and optimal approximation thresholds | — | — | yes | — | yes | yes |
| [106](../theoretical-computer-science/106-hardness-of-coloring-three-colorable-graphs.md) | Hardness of coloring three-colorable graphs | — | — | — | — | — | yes |
| [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | Talagrand's conjectures and graph decompositions at expectation thresholds | — | — | — | — | yes | — |
| [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | The Friedgut--Kalai graph and hypergraph threshold conjectures | yes | — | yes | — | yes | — |
| [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | Random-SAT thresholds, sharp variance and computability | — | — | — | — | yes | yes |
| [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | A hyperbolic group with no geometric CAT(0) action | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026`](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [article.pdf](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf) |
| [`A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026`](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [paper.pdf](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) |
| [`A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026`](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/) | [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | prose | [paper.pdf](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) |
| [`A-uniform-influence-bound-for-hypergraph-properties-October-5-2026`](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [hypergraph-influences.pdf](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) |
| [`Computing-the-Random-3-SAT-Threshold-September-27-2026`](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [article.pdf](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf) |
| [`Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026`](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/) | [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | prose | [paper.pdf](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf) |
| [`Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026`](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [linear-variance-of-the-random-3-sat-hitting-time.pdf](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/linear-variance-of-the-random-3-sat-hitting-time.pdf) |
| [`Talagrands-discrete-convexity-conjecture-September-23-2026`](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/) | [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | prose | [paper.pdf](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf) |
| [`The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026`](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/) | [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | prose | [paper.pdf](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | Friedgut--Kalai sharp-threshold conjecture |
| [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | Friedgut's junta theorem |

## Spelling variants

Every form below normalizes to the key `friedgut`: accents folded, dash variants unified, possessives stripped, case lowered. `Friedgut` · `Friedgut's`

