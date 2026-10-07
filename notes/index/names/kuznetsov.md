# Name: kuznetsov

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 12 capitalized occurrences, 6 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [054](../algebraic-and-complex-geometry/054-counterexamples-to-kuznetsovs-rationality-conjecture.md) | Counterexamples to Kuznetsov's rationality conjecture | yes | — | — | — | yes | yes |
| [130](../theoretical-computer-science/130-fourier-transforms-below-n-n.md) | Fourier transforms below $n\log n$ | — | — | — | — | yes | yes |
| [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | The Boone--Higman conjecture and higher finiteness | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) |
| [`Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026`](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/) | [130](../theoretical-computer-science/130-fourier-transforms-below-n-n.md) | prose | [main.pdf](../../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf) |
| [`Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026`](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/) | [054](../algebraic-and-complex-geometry/054-counterexamples-to-kuznetsovs-rationality-conjecture.md) | prose | [Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026.pdf](../../../preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `kuznetsov`: accents folded, dash variants unified, possessives stripped, case lowered. `Kuznetsov` · `Kuznetsov's`

