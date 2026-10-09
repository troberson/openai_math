# Name: baum

6 families · subject name · 1 carried by a title or a declaration · 4 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 33 capitalized occurrences, 27 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | — | — | — | — | — | yes |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | The rational Hodge conjecture for CM abelian varieties | — | — | — | — | yes | — |
| [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | Log abundance and effective Iitaka fibrations | — | — | — | — | yes | — |
| [041](../algebraic-and-complex-geometry/041-hyperk-ahler-syz-and-projective-space-bases.md) | Hyperk\"ahler SYZ and projective-space bases | — | — | — | — | — | yes |
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Counterexamples to Baum--Connes and Kadison--Kaplansky | yes | yes | — | — | yes | yes |
| [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | Failure of rational injectivity for maximal coarse assembly | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose + title | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf) |
| [`A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) |
| [`A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/) | [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf) |
| [`An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026`](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose + title | [paper.pdf](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/paper.pdf) |
| [`Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026`](../../../preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/) | [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | prose | [paper.pdf](../../../preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf) |
| [`Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026`](../../../preprints/Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026/) | [034](../algebraic-and-complex-geometry/034-log-abundance-and-effective-iitaka-fibrations.md) | prose | [uniform-log-iitaka.pdf](../../../preprints/Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026/uniform-log-iitaka.pdf) |
| [`Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026`](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | prose | [paper.pdf](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf) |
| [`Weil-classes-and-Hodge-classes-on-abelian-powers-September-30-2026`](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-September-30-2026/) | — | prose | — |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Baum`. The normalized key is `baum`.

