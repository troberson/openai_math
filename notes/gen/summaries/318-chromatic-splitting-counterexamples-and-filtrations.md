[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 318](../index/topology/318-chromatic-splitting-counterexamples-and-filtrations.md)

# 318 — Chromatic splitting: counterexamples and filtrations

[Index page](../index/topology/318-chromatic-splitting-counterexamples-and-filtrations.md)

## Original CONTENTS.md summary

[S1:7781] (family entry):

> **318. Chromatic splitting: filtrations and counterexamples.** Disproves strong chromatic splitting at height three for primes *p* ≥ 5, and weak splitting for the derived *p*-completed sphere at heights *p* (*p* ≥ 5) and $`p+1`$ (*p* ≥ 7). Nevertheless, for *n* ≥ 1 and $`p\gt n+1`$, the overlap $`L_{n-1}L_{K(n)}S_p^\wedge`$ admits a $`2^n`$-stage filtration by the predicted localized-sphere pieces. At height three and prime three, even finite assembly from such pieces fails in the category of $`E(2)`$-local modules over the derived completed sphere.

[S2:732] carries the `\resultentry` with all five manuscripts [S3:3, S4:3, S5:3, S6:47, S7:3]. The five abstracts:

> For every $`n\geq1`$ and prime $`p>n+1`$, we construct a
$`2^n`$-stage ordered filtration of $`L_{n-1}L_{K(n)}S_p^\wedge`$ with the
classical chromatic-splitting cofibers. The map from the first stage to
the target is the canonical localization unit. [S3:8–13]

> For every prime $`p\geq5`$, we construct an explicit eight-stage
filtration of $`L_2L_{K(3)}\mathbb S_p^\wedge`$ by the local-sphere
layers in the height-three chromatic-splitting pattern. The map from
its first stage to the overlap is the canonical unit, and two signed
fracture formulas identify all attachments for the chosen local maps
and compatibility homotopy. A companion canonical-map theorem further
implies that the first height-one attachment is nonzero. [S4:9–17]

> For every prime $`p\ge5`$, the canonical map
$`L_0L_{K(3)}S\to L_0L_{K(2)}L_{K(3)}S`$ for the sphere spectrum $`S`$
is nonzero on $`\pi_{-3}`$. Consequently, the height-three strong chromatic
splitting formula is false in this range, even as an equivalence of
underlying $`E(2)`$-local spectra without specified summand maps. [S5:8–14]

> At the prime three and height three, the chromatic overlap cannot be
constructed from the rational, height-one, and height-two local spheres by
finitely many sums, shifts, cofibers, and retracts in the category of
$`E(2)`$-local modules over the derived 3-complete sphere. This gives a
negative answer to the ordinary finite-assembly question for chromatic
overlaps. [S6:54–61]

> For the derived $`p`$-completion of the sphere, the canonical weak chromatic
splitting map has no homotopy retraction at height $`p`$ for every prime
$`p\geq5`$, and at height $`p+1`$ for every prime $`p\geq7`$.
The classical sphere product $`\beta_1^{(p-1)^2}`$ gives a nonzero
kernel class in both ranges. [S7:9–15]

## Undergraduate summary

The **chromatic splitting conjecture** predicts that the stable homotopy
type of a spectrum can be "split" into a clean sum of pieces, each one
capturing a single layer of **chromatic** (height-sensitive) information.
Think of it as decomposing a color image into separate red, green, and
blue channels and hoping the original can be perfectly rebuilt from the
channels.

This family delivers a **mixed verdict**. On one side are **filtrations**
that work: the overlap between two chromatic localizations admits a
controlled, finite-stage filtration built from the predicted localized
sphere pieces [S3:8–13, S4:9–17]. On the other side are **counterexamples**
that break the conjecture in its strong and weak forms: the strong
splitting formula fails at height three for large primes [S5:8–14],
the weak splitting map has no retraction in certain height ranges
[S7:9–15], and at prime three the overlap cannot even be assembled by
finitely many algebraic operations from the obvious pieces [S6:54–61].
So the pieces are there, and they filter the object — but they do not
always reassemble it the way the conjecture promised.

## Graduate summary

**Filtered splitting at generic primes (Manuscript 1)** [S3:8–13,
S2:732].
For every $`n \ge 1`$ and prime $`p > n+1`$, the overlap
$`L_{n-1}L_{K(n)}S_p^\wedge`$ admits a $`2^n`$-stage ordered filtration whose
successive cofibers are the classical chromatic-splitting pieces, with the
canonical localization unit as the map from the first stage to the target.

**The explicit height-three filtration (Manuscript 2)** [S4:9–17,
S2:732].
For every prime $`p \ge 5`$, an explicit eight-stage filtration of
$`L_2L_{K(3)}\mathbb{S}_p^\wedge`$ by the local-sphere layers is
constructed; two signed fracture formulas identify all attachments, and a
companion canonical-map theorem shows the first height-one attachment is
nonzero.

**The strong-splitting counterexample (Manuscript 3)** [S5:8–14,
S2:732].
For every prime $`p \ge 5`$, the canonical map
$`L_0L_{K(3)}S \to L_0L_{K(2)}L_{K(3)}S`$ is nonzero on
$`\pi_{-3}`$, so the height-three **strong** chromatic splitting formula is
false in this range, even as an equivalence of the underlying
$`E(2)`$-local spectra without specified summand maps.

**The finite-assembly failure (Manuscript 4)** [S6:54–61, S2:732].
At prime three and height three, the chromatic overlap cannot be
constructed from the rational, height-one, and height-two local spheres by
finitely many sums, shifts, cofibers, and retracts in the category of
$`E(2)`$-local modules over the derived 3-complete sphere, answering
negatively the ordinary finite-assembly question.

**The weak-splitting counterexamples (Manuscript 5)** [S7:9–15,
S2:732].
For the derived $`p`$-completion of the sphere, the canonical **weak**
chromatic splitting map has no homotopy retraction at height $`p`$ for
$`p \ge 5`$ and at height $`p+1`$ for $`p \ge 7`$; the classical sphere product
$`\beta_1^{(p-1)^2}`$ supplies a nonzero kernel class in both ranges.

## History of the conjecture

The **chromatic splitting conjecture**, associated with Ravenel and the
broader chromatic program, is the stable-homotopy analogue of splitting an
object into its "prime" chromatic layers. The **strong** form asserts a
canonical direct-sum decomposition of a localization overlap into the
localized sphere pieces; the **weak** form allows this only up to a map
admitting a retraction. Stronger, the **finite-assembly** question asks
whether the overlap can be built from the pieces using finitely many of
the basic stable-homotopy operations (sums, shifts, cofibers, retracts).

The five manuscripts together map out where the conjecture holds and
where it fails: the filtrations (Manuscripts 1–2) give the positive,
structural content; the strong and weak counterexamples (Manuscripts 3
and 5) and the finite-assembly failure (Manuscript 4) delineate the
negative boundary. The choice of heights and primes ($`p \ge 5`$ for the
generic statements, prime three for the assembly failure) is what
separates the two regimes.

**Prior (my training data, not this repo).** The chromatic splitting
conjecture and its strong/weak formulations are well studied, with
partial positive results at low heights and for small primes. The
systematic counterexamples at height three and in the stated
height-$`p`$ / height-$`p+1`$ weak ranges, the explicit eight-stage
height-three filtration, and the finite-assembly failure in
$`E(2)`$-local modules are the novel contributions claimed here; I cannot
verify the chromatic-localization and $`K(n)`$-local computations
independently from training alone.

## Consequences

- **Strong chromatic splitting fails at height three for $`p \ge 5`$**
  [S5:8–14, S2:732]: the canonical overlap map is nonzero on
  $`\pi_{-3}`$, falsifying the strong formula even at the level of
  underlying $`E(2)`$-local spectra. This is the named counterexample the
  ledger's `counterex_broad` flag records.
- **Weak splitting fails in the height-$`p`$ and height-$`p+1`$ ranges**
  [S7:9–15, S2:732]: the weak splitting map has no homotopy retraction
  for the derived $`p`$-completed sphere at height $`p`$ ($`p \ge 5`$) and
  height $`p+1`$ ($`p \ge 7`$), with a nonzero kernel class in each range.
- **A $`2^n`$-stage filtration exists at generic primes** [S3:8–13,
  S2:732]: for $`n \ge 1`$ and $`p > n+1`$, the overlap
  $`L_{n-1}L_{K(n)}S_p^\wedge`$ admits an ordered filtration by the
  predicted localized-sphere pieces.
- **The height-three filtration is explicit and its attachments known**
  [S4:9–17, S2:732]: the eight-stage filtration of
  $`L_2L_{K(3)}\mathbb{S}_p^\wedge`$ has all attachments identified by
  signed fracture formulas, with the first height-one attachment nonzero.
- **Finite assembly fails at prime three and height three** [S6:54–61,
  S2:732]: the overlap cannot be built from the rational, height-one, and
  height-two local spheres by finitely many stable-homotopy operations
  in $`E(2)`$-local modules.

## Section skeleton

Five manuscripts, all roots under `build/`:
- Manuscript 1 [S3:8–13]: `build/paper.tex` (30 lines); sections
  `01-introduction` through `11-spectral`.
- Manuscript 2 [S4:9–17]: `build/paper.tex` (35 lines); sections
  `01-introduction` through `12-attachment`, plus appendix
  `10-rational-boundary`.
- Manuscript 3 [S5:8–14]: `build/main.tex` (33 lines); sections
  `01-introduction` through `10-oriented-projection`.
- Manuscript 4 [S6:54–61]: `build/paper.tex` (83 lines; an inline
  preamble precedes the `\documentclass` at [S6:1], title at [S6:47]);
  sections `01-introduction` through `10-obstruction`.
- Manuscript 5 [S7:9–15]: `build/main.tex` (35 lines); sections
  `01-introduction` through `13-exponent-contradiction`, plus appendix
  `03-ordinary-products`. No verification bundle.

## Comparison with the formalized statement

This family is **not formalized**. It sits at tier **T0** in the ledger
[S8]: no scope note, no comparator stub, no `main_results` entry, no
proved OAI tree. The T0 shape is "no formalization at all in the
release."

The absence is expected for this corner of the catalog: the chromatic
splitting and $`K(n)`$-local families are among the thinnest formalized,
and a five-manuscript counterexample-plus-filtration spread of exactly
this kind is the representative case. The reading of the five
manuscripts above is of source text only.

## Coverage

The ledger row `fam=318` [S8] records the tier and the counts:
`tier=T0`, `paps=5`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `scope_chars=0`, `verification=0`, `trace=`. The T0
shape is "no formalization at all." The shape flags are
`shapes=counterexample`, `resolves_named=0`, `counterex_broad=1`,
`covmd=0` — a counterexample family recording the strong and weak
splitting failures, with no formalization record in the release and no
coverage document in the manuscript directories.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7781] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 318 at [S2:732] |
| S3 | [`preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/build/paper.tex`](../../../preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/build/paper.tex) | 30 | manuscript 1 (filtered splitting); title [S3:3], date [S3:5], abstract [S3:8–13] |
| S4 | [`preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/build/paper.tex`](../../../preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/build/paper.tex) | 35 | manuscript 2 (height-three filtration); title [S4:3], date [S4:5], abstract [S4:9–17] |
| S5 | [`preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/build/main.tex`](../../../preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/build/main.tex) | 33 | manuscript 3 (rational obstruction); title [S5:3], date [S5:5], abstract [S5:8–14] |
| S6 | [`preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/build/paper.tex`](../../../preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/build/paper.tex) | 83 | manuscript 4 (finite-assembly failure); title [S6:47], date [S6:50], abstract [S6:54–61] |
| S7 | [`preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/build/main.tex`](../../../preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/build/main.tex) | 35 | manuscript 5 (weak-splitting counterexamples); title [S7:3], date [S7:5], abstract [S7:9–15] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=318`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
