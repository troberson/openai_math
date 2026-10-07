# Name: hansen

5 families · subject name · 1 carried by a title or a declaration · 3 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 12 capitalized occurrences, 7 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | — | — | yes | yes |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | The Mahler conjectures and symplectic width | — | — | yes | — | yes | yes |
| [104](../theoretical-computer-science/104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md) | Quasipolynomial algorithms for mean-payoff, stochastic and parity games | — | — | — | — | — | yes |
| [272](../mathematical-physics/272-entanglement-without-secret-key-and-the-ppt-square-conjecture.md) | Entanglement without secret key and the PPT-square conjecture | — | — | — | — | yes | — |
| [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | Chromatic splitting: counterexamples and filtrations | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026`](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [constructible-tame-hecke-eigensheaves-positive-characteristic.pdf](../../../preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf) |
| [`Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026`](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/) | [272](../mathematical-physics/272-entanglement-without-secret-key-and-the-ppt-square-conjecture.md) | prose | [paper.pdf](../../../preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf) |
| [`Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026`](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [tame-hecke-frobenius.pdf](../../../preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf) |
| [`Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026`](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf](../../../preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf) |
| [`The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026`](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose | [paper.pdf](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | Hansen--Lima |

## Spelling variants

One surface form in prose: `Hansen`. The normalized key is `hansen`.

