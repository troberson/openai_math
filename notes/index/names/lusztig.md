# Name: lusztig

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 68 capitalized occurrences, 62 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [001](../number-theory/001-milnes-rationality-conjecture.md) | Milne's rationality conjecture | — | — | — | — | yes | — |
| [069](../algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md) | Quantum geometric Langlands at irrational level | — | — | — | — | yes | — |
| [168](../combinatorics/168-combinatorial-invariance-of-kazhdan-lusztig-polynomials.md) | Combinatorial invariance of Kazhdan--Lusztig polynomials | yes | yes | yes | — | yes | — |
| [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | Donovan's conjecture over fields and discrete valuation rings | — | — | — | — | yes | — |
| [204](../algebra/204-tensor-saturation-for-even-spin-groups.md) | Tensor saturation for even spin groups | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026`](../../../preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/) | [168](../combinatorics/168-combinatorial-invariance-of-kazhdan-lusztig-polynomials.md) | prose + title | [paper.pdf](../../../preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf) |
| [`Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026`](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/) | [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | prose | [main.pdf](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf) |
| [`Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026`](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/) | [069](../algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md) | prose | [quantum-langlands.pdf](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf) |
| [`Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/) | [001](../number-theory/001-milnes-rationality-conjecture.md) | prose | [paper.pdf](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf) |
| [`Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/) | — | prose | — |
| [`Tensor-Saturation-for-Even-Spin-Groups-September-24-2026`](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/) | [204](../algebra/204-tensor-saturation-for-even-spin-groups.md) | prose | [Tensor-Saturation-for-Even-Spin-Groups-September-24-2026.pdf](../../../preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [168](../combinatorics/168-combinatorial-invariance-of-kazhdan-lusztig-polynomials.md) | Dihedral Kazhdan--Lusztig polynomials |

## Spelling variants

Every form below normalizes to the key `lusztig`: accents folded, dash variants unified, possessives stripped, case lowered. `Lusztig` · `Lusztig's`

