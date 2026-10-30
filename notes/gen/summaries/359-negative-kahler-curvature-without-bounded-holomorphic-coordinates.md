[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 359](../index/differential-geometry/359-negative-kahler-curvature-without-bounded-holomorphic-coordinates.md)

# 359 — Negative Kähler curvature without bounded holomorphic coordinates

[Index page](../index/differential-geometry/359-negative-kahler-curvature-without-bounded-holomorphic-coordinates.md)

## Original CONTENTS.md summary

[S1:8706] (family entry):

> **359. Negative Kähler curvature without bounded holomorphic coordinates.** Constructs a contractible domain in ℂ<sup>3</sup> with a complete negatively pinched Kähler metric but no bounded holomorphic coordinates, disproving bounded-domain uniformization in this setting. A higher-dimensional example has sectional curvature at most −1 and only constant bounded holomorphic functions; its curvature is not bounded below. ([Lean](lean/docs/359.md))

[S2:818] carries the `\resultentry` with two manuscripts —
manuscript 1 [S3] (the negatively pinched threefold, the formalized
construction) and manuscript 2 [S4] (the one-sided companion). The
scope note names **only** manuscript 1 [S5:5] and states the formalized
result 

> The formalized result constructs a nonempty contractible complex threefold with a complete Kähler metric whose real sectional curvatures lie between two fixed negative constants. Nevertheless, it has no system of bounded holomorphic coordinates and is not biholomorphic to a bounded domain. The metric is obtained from an explicitly controlled potential. This is the negatively pinched construction; the different companion with only one-sided curvature control is separate. [S5:9]

## Undergraduate summary

A **Kähler** space is a special kind of complex space — one that,
roughly, behaves a lot like a smooth manifold with a rich
complex-geometric structure baked in. For such spaces, two questions
long had in the literature:

1. *Can a negatively curved Kähler space still look like a piece of
   $`\mathbb C^n`$?* This is the "uniformization" question.
2. *How "large" is the space in a function-theoretic sense?* In
   particular, are there any nonconstant **bounded holomorphic
   functions** on it — functions that take values in the complex
   numbers, are holomorphic (satisfy the Cauchy–Riemann equations),
   and are bounded in magnitude?

These two questions are related in the classical setting (the
Bieberbach-type results and the classical Liouville theorem). The
result here says **no** on both, in a stronger form:

- Manuscript 1 constructs a contractible three-dimensional complex
  space (a **threefold**) with a complete Kähler metric whose
  curvature sits between two fixed negative numbers — a very
  "strongly negatively curved" space — that nevertheless has no
  bounded holomorphic coordinates at all, and so is not biholomorphic
  to any bounded domain in $`\mathbb C^3`$.
- Manuscript 2 generalizes the theme to a higher dimension: a space
  with sectional curvature at most $`-1`$ (one-sided, not pinched) on
  which *every* bounded holomorphic function is constant.

The release formalizes manuscript 1 — the pinched threefold — and
leaves manuscript 2 as the unformalized "separate" companion [S5:9].

## Graduate summary

**Main theorem (manuscript 1, the formalized construction)**
[S3:41–47, S5:9].
There exists a nonempty contractible complex threefold $`X`$ with a
complete Kähler metric $`\omega`$ whose real sectional curvatures lie
between two fixed negative constants $`-C`$ and $`-c`$
($`0 < c < C`$). The space $`X`$ admits no system of bounded
holomorphic coordinates — equivalently, no bounded holomorphic map
$`X \to \mathbb C^3`$ with nowhere-vanishing Jacobian — and is
therefore not biholomorphic to a bounded domain in
$`\mathbb C^3`$ [S3:41–47].

**Companion theorem (manuscript 2, unformalized)**
[S4:35–41].
In some sufficiently large fixed finite complex dimension $`m`$,
there exists a domain $`Y \subseteq \mathbb C^m`$ diffeomorphic to
$`\mathbb R^{2m}`$ admitting a complete Kähler metric with real
sectional curvature at most $`-1`$ (unbounded below) on which every
bounded holomorphic function is constant [S4:35–41].

**What the formalization states** [S5:9, S7].
The scope note [S5:9] selects manuscript 1's pinched construction,
*not* the one-sided companion. The comparator stub
`PinchedKahler.lean` (159 lines) carries three declarations:
`theorem main_theorem : MainTheorem` [S7:146],
`theorem controlled_potential : ControlledPotential` [S7:149], and
`theorem metric_transfer : MetricTransfer` [S7:152], each with a
`sorry`. Only `main_theorem` appears in the `main_results` entry
[S6:1511–1513], which resolves the declaration
`OAI.PinchedHartogs.main_theorem` to
`lean/OAI/Geometry/Kahler/Main.lean` [S8] (44 lines), entry of a
119-file OAI tree carrying 0 `sorry`.

## History of the conjecture

The **Kähler uniformization** question asks which Kähler manifolds
of negative curvature are biholomorphic to bounded domains in
$`\mathbb C^n`$ — the classical answer for the complex ball
(pseudoconvex domains with negative curvature) is yes, by the
Levi problem and the classical pseudoconvexity theory. The **negative
answer** here [S3:41–47] constructs a counterexample in dimension
three: a complete negatively pinched Kähler threefold with no
bounded holomorphic coordinates at all, hence not biholomorphic to a
bounded domain. This is a **Hartogs-type** counterexample in the
negative-curvature setting.

The **holomorphic Liouville property** — that all bounded
holomorphic functions on a space are constant — is a strong
function-theoretic rigidity. Manuscript 2 [S4:35–41] shows it can
coexist with one-sided negative sectional curvature in a higher
dimension, giving a negative answer to the one-sided
bounded-holomorphic-function question. The two manuscripts form a
complementary pair: manuscript 1 has **pinched** (two-sided)
curvature with a coordinate-free failure; manuscript 2 has
**one-sided** curvature with a function-theoretic failure.

**Prior (my training data, not this repo).** As of my training
cutoff, the existence of a complete negatively pinched Kähler
threefold that is not biholomorphic to a bounded domain was not
established in the literature as I recall it. The construction
relies on a carefully controlled Kähler potential that produces the
pinching while killing bounded holomorphic coordinates — a genuine
new construction in the negative-curvature Hartogs theory. I cannot
verify the complex-geometric construction independently from training
alone.

## Consequences

- **The negatively pinched Kähler uniformization question fails in
  complex dimension three** [S3:41–47, S5:9]: there exists a
  complete negatively pinched Kähler threefold with no bounded
  holomorphic coordinates, not biholomorphic to a bounded domain.
- **The construction has a controlled curvature** [S3:41–47, S5:9]:
  the real sectional curvatures of the constructed metric lie between
  two fixed negative constants, the negative pinching is two-sided.
- **The one-sided companion is a separate, unformalized result**
  [S4:35–41, S5:9]: the higher-dimensional example has sectional
  curvature at most $`-1`$ (unbounded below) and only constant bounded
  holomorphic functions.
- **Function-theoretic rigidity accompanies negative curvature beyond
  the classical setting** [S4:35–41]: the holomorphic Liouville
  property (only constant bounded holomorphic functions) holds on a
  complete one-sided negatively curved Kähler domain.

## Section skeleton

Two manuscripts, both with `build/main.tex` roots.
Manuscript 1 [S3] (pinched construction, 64 lines): 10 `input` files
[S3:52–61]: `01-introduction`, `02-reduction`, `03-peaks`,
`04-densities-construction`, `04-densities-estimates`,
`05-logarithmic-tests`, `06-base-potential`, `07-hartogs-metric`,
`08-curvature`, `09-pinching`, plus a BibTeX `references.bib`.
Manuscript 2 [S4] (one-sided companion, 59 lines): 8 `input` files
[S4:49–56]: `01-introduction`, `02-tube`, `03-analytic`,
`04-fiber`, `05-quiet`, `06-radial`, `07-centers`, `08-assembly`,
plus a BibTeX `refs.bib`. **No verification bundles.**

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S5:9], one comparator stub [S7], **one** `main_results` entry
[S6:1511–1513], and one proved OAI tree [S8]. The T3 shape is "scope
note, comparator stub, `main_results` entry, and proved OAI tree (0
`sorry`)."

The formalization is **asymmetric with the family**: the scope note
names only manuscript 1 [S5:5] (the pinched threefold), and states
that manuscript 2 "is separate" [S5:9]. The comparator stub
`PinchedKahler.lean` (159 lines) carries three declarations —
`main_theorem` [S7:146], `controlled_potential` [S7:149], and
`metric_transfer` [S7:152], each with a `sorry` — but only
`main_theorem` appears in `main_results` [S6:1511–1513], which
resolves `OAI.PinchedHartogs.main_theorem` to
`lean/OAI/Geometry/Kahler/Main.lean` [S8] (44 lines), entry of a
119-file OAI tree carrying 0 `sorry`. The controlled-potential and
metric-transfer lemmas are formalized in the OAI tree (0 `sorry`)
but are not the `main_results` declaration; the formalized statement
is the pinched-construction `main_theorem` [S5:9]. The reading is of
source text only.

## Coverage

The ledger row `fam=359` [S9] records the tier and the counts:
`tier=T3`, `paps=2`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=474`, `verification=0`, `trace=`. The T3
shape is "scope note, comparator stub, `main_results` entry, and
proved OAI tree (0 `sorry`)." The single comparator stub carries 3
`sorry` (one per declaration). The shape flags are
`shapes=bound|partial`, `resolves_named=0`, `counterex_broad=1`,
`covmd=0` — a **bound**/curvature result with a **partial**-answer
(negative answer to the uniformization question), with a
counterexample-shaped construction (the pinched threefold is a
counterexample to the bounded-domain uniformization conjecture) in
the title. Note `paps_form=1`: only manuscript 1 (the pinched
construction) appears in `formalization.yaml`'s `sources:` list;
manuscript 2 (the one-sided companion) does not — the scope note
[S5:9] names only manuscript 1 and states that manuscript 2 "is
separate."

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8706] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 359 at [S2:818] |
| S3 | [`preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/main.tex`](../../../preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/main.tex) | 64 | the `\documentclass` root (manuscript 1, the pinched construction) — 64 lines, title [S3:36], date [S3:38], abstract [S3:41–47], 10 `input` files [S3:52–61] |
| S4 | [`preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/build/main.tex`](../../../preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/build/main.tex) | 59 | the `\documentclass` root (manuscript 2, the one-sided companion) — 59 lines, title [S4:30], date [S4:32], abstract [S4:35–41], 8 `input` files [S4:49–56] |
| S5 | [`lean/docs/359.md`](../../../lean/docs/359.md) | 15 | scope note — names only manuscript 1; Scope at [S5:9], comparator link at [S5:15] |
| S6 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry — [S6:1511–1513] |
| S7 | [`lean/ComparatorChallenges/PinchedKahler.lean`](../../../lean/ComparatorChallenges/PinchedKahler.lean) | 159 | comparator stub — 159 lines, `theorem main_theorem` [S7:146], `theorem controlled_potential` [S7:149], `theorem metric_transfer` [S7:152], 3 `sorry` |
| S8 | [`lean/OAI/Geometry/Kahler/Main.lean`](../../../lean/OAI/Geometry/Kahler/Main.lean) | 44 | proved OAI declaration — 44 lines, 0 `sorry`; 119 files under the tree |
| S9 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=359`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
