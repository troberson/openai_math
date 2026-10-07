# Name: hubbard

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 23 capitalized occurrences, 18 of them mid-sentence, 9 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | The three-quarter diameter exponent for honeycomb walks | — | — | — | — | yes | — |
| [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | QMA-hardness of continuum Coulomb energy | — | — | yes | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026`](../../../preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/) | [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | prose | [Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf](../../../preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf) |
| [`Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026`](../../../preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/) | [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | prose | [main.pdf](../../../preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/main.pdf) |
| [`QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026`](../../../preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/) | [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | prose | [QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026.pdf](../../../preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | Hubbard reduction with rational hoppings |
| [275](../mathematical-physics/275-qma-hardness-of-continuum-coulomb-energy.md) | Simulation of the Hubbard spectral minimum |

## Spelling variants

One surface form in prose: `Hubbard`. The normalized key is `hubbard`.

