# Name: einsiedler

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 19 capitalized occurrences, 10 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | Torus-packet equidistribution in prime, quartic, and sextic degrees | — | — | yes | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026`](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [paper.pdf](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf) |
| [`Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026`](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [quartic-torus-packets.pdf](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf) |
| [`Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026`](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [primitive-sextic-torus-packets.pdf](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | Einsiedler--Katok--Lindenstrauss |

## Spelling variants

One surface form in prose: `Einsiedler`. The normalized key is `einsiedler`.

