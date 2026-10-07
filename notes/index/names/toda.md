# Name: toda

4 families · subject name · 2 carried by a title or a declaration · 4 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 50 capitalized occurrences, 28 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 2 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | — | — | yes | — |
| [055](../algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md) | Toda's Gepner conjecture and large-volume stability | yes | — | — | — | yes | yes |
| [308](../topology/308-smith-toda-complexes-at-every-height-with-varying-primes.md) | Smith--Toda complexes at every height with varying primes | yes | yes | — | — | yes | yes |
| [309](../topology/309-kervaire-invariant-problem-at-the-prime-three.md) | The Kervaire invariant problem at the prime three | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/) | [055](../algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md) | prose | [paper.pdf](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/paper.pdf) |
| [`A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026`](../../../preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/) | [308](../topology/308-smith-toda-complexes-at-every-height-with-varying-primes.md) | prose + title | [paper.pdf](../../../preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/paper.pdf) |
| [`Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026`](../../../preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/) | [308](../topology/308-smith-toda-complexes-at-every-height-with-varying-primes.md) | prose + title | [paper.pdf](../../../preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/paper.pdf) |
| [`Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/) | [055](../algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md) | prose | [paper.pdf](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf) |
| [`Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026`](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [paper.pdf](../../../preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf) |
| [`The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026`](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/) | [309](../topology/309-kervaire-invariant-problem-at-the-prime-three.md) | prose | [paper.pdf](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `toda`: accents folded, dash variants unified, possessives stripped, case lowered. `Toda` · `Toda's`

