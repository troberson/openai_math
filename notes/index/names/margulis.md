# Name: margulis

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 55 capitalized occurrences, 34 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | The Margulis--Platonov conjecture over global fields | yes | yes | — | — | yes | yes |
| [136](../theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md) | The quasilinear PCP-for-PPAD conjecture | — | — | — | — | yes | yes |
| [178](../combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md) | Deterministic nonbipartite Ramanujan graphs in every fixed degree | — | — | — | — | yes | — |
| [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | The Friedgut--Kalai graph and hypergraph threshold conjectures | — | — | — | — | yes | — |
| [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | Arithmetic rigidity of lattice von Neumann algebras | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026`](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [paper.pdf](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) |
| [`A-uniform-influence-bound-for-hypergraph-properties-October-5-2026`](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [hypergraph-influences.pdf](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) |
| [`Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026`](../../../preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/) | [178](../combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md) | prose | [paper.pdf](../../../preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/paper.pdf) |
| [`The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose + title | [margulis-platonov-global-function-fields.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf) |
| [`The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose + title | [paper.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) |
| [`The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026`](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/) | [136](../theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md) | prose | [paper.pdf](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/paper.pdf) |
| [`The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026`](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/) | [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | prose | [paper.pdf](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `margulis`: accents folded, dash variants unified, possessives stripped, case lowered. `Margulis` · `Margulis's`

