# Name: arthur

8 families · subject name · 1 carried by a title or a declaration · 5 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 77 capitalized occurrences, 53 of them mid-sentence, 12 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | — | — | yes | yes |
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | — | — | — | — | — | yes |
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | yes | yes | yes | — | yes | yes |
| [030](../number-theory/030-modularity-over-imaginary-quadratic-fields.md) | Modularity over imaginary quadratic fields | — | — | — | — | — | yes |
| [125](../theoretical-computer-science/125-approximation-threshold-for-metric-k-median.md) | The approximation threshold for metric $k$-median | — | — | — | — | — | yes |
| [262](../mathematical-physics/262-sharp-one-dimensional-lieb-thirring-inequalities.md) | Sharp one-dimensional Lieb--Thirring inequalities | — | — | — | — | yes | — |
| [294](../operator-algebras/294-a-counterexample-to-kaplanskys-quasitrace-conjecture.md) | A counterexample to Kaplansky's quasitrace conjecture | — | — | — | — | yes | — |
| [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | Counterexamples to disk embedding and Wall's manifold conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-PD4-group-without-an-aspherical-manifold-model-September-24-2026`](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/) | [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | prose | [paper.pdf](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/paper.pdf) |
| [`A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/) | [294](../operator-algebras/294-a-counterexample-to-kaplanskys-quasitrace-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf) |
| [`Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026`](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/) | [262](../mathematical-physics/262-sharp-one-dimensional-lieb-thirring-inequalities.md) | prose | [sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf) |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | — | prose | — |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf) |
| [`Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026`](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose + title | [manuscript.pdf](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf) |
| [`Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose + title | [paper.pdf](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) |
| [`Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose + title | [paper.pdf](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf) |
| [`Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026`](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/) | [262](../mathematical-physics/262-sharp-one-dimensional-lieb-thirring-inequalities.md) | prose | [sharp-matrix-lieb-thirring.pdf](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf) |
| [`Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [ramified-ramanujan.pdf](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) |
| [`The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026`](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [paper.pdf](../../../preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [main.pdf](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/) | — | prose | — |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Finite-level Ramanujan--Arthur decomposition
  \cite[Theorem~1.1 |
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Global Arthur enhancement |

## Spelling variants

Every form below normalizes to the key `arthur`: accents folded, dash variants unified, possessives stripped, case lowered. `Arthur` · `Arthur's`

