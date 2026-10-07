# Name: sitter

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 32 capitalized occurrences, 29 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Spacetime Penrose inequalities and rigidity | — | yes | yes | — | yes | — |
| [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | Strong cosmic censorship near two-ended Kerr data | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026`](../../../preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose + title | [paper.pdf](../../../preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/paper.pdf) |
| [`Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026`](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/paper.pdf) |
| [`Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026`](../../../preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/paper.pdf) |
| [`The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026`](../../../preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/paper.pdf) |
| [`The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026`](../../../preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose + title | [paper.pdf](../../../preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Nonmaximal anti-de Sitter Penrose Inequality |

## Spelling variants

One surface form in prose: `Sitter`. The normalized key is `sitter`.

