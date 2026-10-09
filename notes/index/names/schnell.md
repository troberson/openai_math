# Name: schnell

5 families · subject name · 1 carried by a title or a declaration · 3 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 54 capitalized occurrences, 30 of them mid-sentence, 12 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink in abelian varieties and the Siegel threefold | — | — | — | — | yes | — |
| [033](../algebraic-and-complex-geometry/033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) | Campana's orbifold Iitaka conjecture and logarithmic subadditivity | — | — | — | — | yes | yes |
| [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | Log abundance and effective Iitaka fibrations | — | yes | yes | — | yes | yes |
| [036](../algebraic-and-complex-geometry/036-numerical-semiampleness-and-generalized-minimal-models.md) | Numerical semiampleness and generalized minimal models | — | — | — | — | — | yes |
| [068](../algebraic-and-complex-geometry/068-anticanonical-nonvanishing-under-smooth-semipositivity.md) | Anticanonical nonvanishing under smooth semipositivity | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026`](../../../preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [paper.pdf](../../../preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/paper.pdf) |
| [`Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026`](../../../preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [paper.pdf](../../../preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/paper.pdf) |
| [`Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-4-2026`](../../../preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-4-2026/) | — | prose | — |
| [`Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026`](../../../preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [main.pdf](../../../preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026/main.pdf) |
| [`Log-abundance-in-characteristic-zero-September-24-2026`](../../../preprints/Log-abundance-in-characteristic-zero-September-24-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [paper.pdf](../../../preprints/Log-abundance-in-characteristic-zero-September-24-2026/paper.pdf) |
| [`Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026`](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/) | [033](../algebraic-and-complex-geometry/033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) | prose | [paper.pdf](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf) |
| [`Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026`](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/) | [033](../algebraic-and-complex-geometry/033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) | prose | [paper.pdf](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf) |
| [`Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026`](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/) | [033](../algebraic-and-complex-geometry/033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) | prose | [paper.pdf](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf) |
| [`Schnell-fiber-spaces-and-good-canonical-models-September-24-2026`](../../../preprints/Schnell-fiber-spaces-and-good-canonical-models-September-24-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose + title | [paper.pdf](../../../preprints/Schnell-fiber-spaces-and-good-canonical-models-September-24-2026/paper.pdf) |
| [`The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose | [paper.pdf](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) |
| [`The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026`](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/) | [033](../algebraic-and-complex-geometry/033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) | prose | [paper.pdf](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | Schnell's zero-Kodaira fiber-space conclusion |
| [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | Schnell's general fiber-space conclusion |

## Spelling variants

Every form below normalizes to the key `schnell`: accents folded, dash variants unified, possessives stripped, case lowered. `Schnell` · `Schnell's`

