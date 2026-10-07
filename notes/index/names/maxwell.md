# Name: maxwell

5 families · subject name · 2 carried by a title or a declaration · 5 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 105 capitalized occurrences, 75 of them mid-sentence, 11 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

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
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Spacetime Penrose inequalities and rigidity | — | — | — | — | yes | — |
| [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | Strong cosmic censorship near two-ended Kerr data | — | — | — | — | yes | — |
| [266](../mathematical-physics/266-exactly-three-mutually-unbiased-bases-in-dimension-six.md) | Exactly three mutually unbiased bases in dimension six | — | — | — | — | yes | yes |
| [282](../mathematical-physics/282-scale-to-conformal-enhancement-in-four-dimensional-qft.md) | Scale-to-conformal enhancement in four-dimensional QFT | — | — | yes | — | yes | — |
| [362](../partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md) | Global smoothness for relativistic Vlasov--Maxwell | yes | yes | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026`](../../../preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/paper.pdf) |
| [`Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026`](../../../preprints/Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026/paper.pdf) |
| [`Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026`](../../../preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf) |
| [`Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026`](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/) | [266](../mathematical-physics/266-exactly-three-mutually-unbiased-bases-in-dimension-six.md) | prose | [Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf](../../../preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf) |
| [`Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026`](../../../preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/paper.pdf) |
| [`Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026`](../../../preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/paper.pdf) |
| [`Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026`](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/) | [362](../partial-differential-equations/362-global-smoothness-for-relativistic-vlasov-maxwell.md) | prose + title | [paper.pdf](../../../preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf) |
| [`Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026`](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/paper.pdf) |
| [`Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026`](../../../preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/) | [282](../mathematical-physics/282-scale-to-conformal-enhancement-in-four-dimensional-qft.md) | prose | [main.pdf](../../../preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/main.pdf) |
| [`The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026`](../../../preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/paper.pdf) |
| [`The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026`](../../../preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [282](../mathematical-physics/282-scale-to-conformal-enhancement-in-four-dimensional-qft.md) | The exterior Maxwell test |

## Spelling variants

Every form below normalizes to the key `maxwell`: accents folded, dash variants unified, possessives stripped, case lowered. `Maxwell` · `Maxwell's`

