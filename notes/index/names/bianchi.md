# Name: bianchi

8 families · subject name · 1 carried by a title or a declaration · 8 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 65 capitalized occurrences, 48 of them mid-sentence, 9 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 8 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [030](../number-theory/030-modularity-over-imaginary-quadratic-fields.md) | Modularity over imaginary quadratic fields | — | — | — | — | yes | yes |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces | — | — | — | — | yes | — |
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Spacetime Penrose inequalities and rigidity | — | — | — | — | yes | — |
| [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | Strong cosmic censorship near two-ended Kerr data | — | — | — | — | yes | — |
| [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | Counterexamples to disk embedding and Wall's manifold conjecture | — | — | — | — | yes | — |
| [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | A four-dimensional counterexample to Borel rigidity | — | — | — | — | yes | — |
| [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | Nonnegatively curved Einstein four-manifolds and a topological gap | — | — | yes | — | yes | — |
| [351](../differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md) | Scalar curvature detects four-dimensional Ricci-flow singularities | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026`](../../../preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/paper.pdf) |
| [`A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026`](../../../preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/) | [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | prose | [paper.pdf](../../../preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf) |
| [`A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026`](../../../preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/paper.pdf) |
| [`A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026`](../../../preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/) | [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | prose | [paper.pdf](../../../preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf) |
| [`Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026`](../../../preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | prose | [paper.pdf](../../../preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/paper.pdf) |
| [`An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026`](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/) | [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | prose | [einstein-gap.pdf](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf) |
| [`Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/) | [351](../differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md) | prose | [paper.pdf](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf) |
| [`Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026`](../../../preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf) |
| [`Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026`](../../../preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/paper.pdf) |
| [`Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026`](../../../preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/paper.pdf) |
| [`Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/) | [030](../number-theory/030-modularity-over-imaginary-quadratic-fields.md) | prose | [paper.pdf](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf) |
| [`Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/) | [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | prose | [paper.pdf](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf) |
| [`Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/) | [351](../differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md) | prose | [paper.pdf](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf) |
| [`Positively-curved-Einstein-four-manifolds-September-23-2026`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/) | [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | prose | [paper.pdf](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf) |
| [`Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026`](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/) | [264](../mathematical-physics/264-strong-cosmic-censorship-near-two-ended-kerr-data.md) | prose | [paper.pdf](../../../preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/paper.pdf) |
| [`The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026`](../../../preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/paper.pdf) |
| [`The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026`](../../../preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/paper.pdf) |
| [`Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/) | [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | prose | [einstein-boundary.pdf](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | Parametrization of the Bianchi gradient space |
| [348](../differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) | Parametrization of the Bianchi gradient space |

## Spelling variants

Every form below normalizes to the key `bianchi`: accents folded, dash variants unified, possessives stripped, case lowered. `Bianchi` · `Bianchi's`

