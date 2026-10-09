# Name: lawson

8 families · subject name · 1 carried by a title or a declaration · 5 by prose · 7 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 18 capitalized occurrences, 15 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 7 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [041](../algebraic-and-complex-geometry/041-hyperk-ahler-syz-and-projective-space-bases.md) | Hyperk\"ahler SYZ and projective-space bases | — | — | — | — | — | yes |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | The Mahler conjectures and symplectic width | — | — | — | — | — | yes |
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Spacetime Penrose inequalities and rigidity | — | — | — | — | — | yes |
| [335](../differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md) | Gromov's integral scalar-curvature inequality | — | — | yes | — | yes | yes |
| [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | Spectral scalar curvature and codimension-two width | — | — | — | — | yes | yes |
| [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | Donaldson's hypersymplectic deformation conjecture | — | — | — | — | yes | yes |
| [342](../differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md) | Donaldson's tamed-to-compatible conjecture | — | — | — | — | yes | yes |
| [361](../differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md) | Counterexamples to Yau's harmonic dimension bound | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026`](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/) | [361](../differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/paper.pdf) |
| [`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/) | [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | prose | [paper.pdf](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/paper.pdf) |
| [`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/) | — | prose | — |
| [`Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026`](../../../preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose | [paper.pdf](../../../preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/paper.pdf) |
| [`Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026`](../../../preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/) | [335](../differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md) | prose | [paper.pdf](../../../preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/paper.pdf) |
| [`Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026`](../../../preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose | [spectral-urysohn-three-manifolds.pdf](../../../preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/spectral-urysohn-three-manifolds.pdf) |
| [`Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026`](../../../preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose | [main.pdf](../../../preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf) |
| [`Taming-implies-compatibility-on-four-manifolds-October-6-2026`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/) | [342](../differential-geometry/342-donaldsons-tamed-to-compatible-conjecture.md) | prose | [paper.pdf](../../../preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf) |
| [`Taming-implies-compatibility-on-four-manifolds-September-23-2026`](../../../preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026/) | — | prose | — |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [335](../differential-geometry/335-gromovs-integral-scalar-curvature-inequality.md) | The Gromov--Lawson aspherical conjecture |

## Spelling variants

One surface form in prose: `Lawson`. The normalized key is `lawson`.

