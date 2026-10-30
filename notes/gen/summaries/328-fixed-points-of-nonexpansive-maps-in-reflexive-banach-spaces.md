[Notes](../../README.md) / [Summaries](README.md) / [Functional analysis](../index/disciplines/functional-analysis.md) / [Family 328](../index/functional-analysis/328-fixed-points-of-nonexpansive-maps-in-reflexive-banach-spaces.md)

# 328 — Fixed points of nonexpansive maps in reflexive Banach spaces

[Index page](../index/functional-analysis/328-fixed-points-of-nonexpansive-maps-in-reflexive-banach-spaces.md)

## Original CONTENTS.md summary

[S1:7995] (family entry):

> **328. Nonexpansive fixed points in reflexive Banach spaces.** Resolves Kirk's reflexive-space fixed-point problem: every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. The result uses the original norm, without assuming uniform convexity. ([Lean](../../../lean/docs/328.md))

[S2:754] carries the `\resultentry` with the single manuscript [S3:3, S3:5]. The abstract:

> Every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. This resolves the reflexive-space fixed point problem for the given norm. [S3:8–11]

## Undergraduate summary

A **nonexpansive map** is a function that never increases distances: if you
measure the distance between any two points, the images under the map are at
most that far apart. A **fixed point** is a point that the map sends to
itself.

The question here is: if your map acts on a nice-looking chunk of a
"reflexive" Banach space (roughly, a space where the geometry is
"complete enough" that bounded convex sets behave well), does the map
have to have a fixed point? The answer is **yes**, and remarkably, no
extra roundness assumption (uniform convexity) is needed. This resolves
a long-standing open problem in fixed-point theory known as **Kirk's
problem**.

In plain terms: if you have a distance-non-increasing function on a
bounded, closed, convex set in a "well-behaved" infinite-dimensional
space, there is always a point that stays put.

## Graduate summary

**Main theorem (formalized)** [S3:8–11, S2:754, S4:9].
Every nonexpansive self-map $`F : C \to C`$ of a nonempty closed bounded
convex subset $`C`$ of a real reflexive Banach space $`X`$ has a fixed
point: there exists $`a \in C`$ with $`F(a) = a`$. Nonexpansiveness is
stated in the original norm:
$``\lVert F(a) - F(b) \rVert \leq \lVert a - b \rVert`$` for all $`a, b \in C`$.
Zero and nonseparable spaces are included; no uniform convexity, normal
structure, or weak-continuity assumption is required.

**The formalized statement** [S4:9, S5].
The comparator stub states the theorem as
`theorem exists_fixedPoint_of_canonicallyReflexive` with hypothesis
`CanonicallyReflexive X` (surjectivity of the canonical map into the
continuous bidual — the formal definition of reflexivity), the set
hypotheses (nonempty, closed, bounded, convex), and the nonexpansiveness
condition in the original norm. The conclusion is existence of a fixed
point.

**What "reflexivity" buys** [S4:9].
Reflexivity is the property that the canonical embedding of a Banach
space into its bidual is surjective. This is the weakest geometric
hypothesis under which the fixed-point conclusion holds; the result
shows no stronger condition (uniform convexity, weak compactness of the
unit ball in a separate sense, normal structure) is needed beyond
reflexivity itself.

## History of the conjecture

**Kirk's reflexive-space fixed-point problem** (W. A. Kirk, 1965) asked
whether every nonexpansive self-map of a nonempty closed bounded convex
subset of a reflexive Banach space has a fixed point. The problem was
solved in the affirmative for **uniformly convex** spaces (Kirk 1965,
Goebel–Kirk) and for spaces with **normal structure** (Browder 1965),
but the general reflexive case remained open for decades.

Known positive results before this work: uniformly convex Banach spaces
(Kirk), Hilbert spaces (a special case), and L-ur-al spaces. The
difficult case was reflexive spaces without uniform convexity, where
the classical geometric arguments (barycentric functions on the
hyperplanes, normal structure) do not apply directly.

The present result closes the gap: reflexivity alone suffices. The
proof does not use uniform convexity, normal structure, or
weak-continuity — it works in the original norm for arbitrary real
reflexive Banach spaces, including nonseparable ones.

**Prior (my training data, not this repo).** Kirk's problem and the
uniform-convexity / normal-structure positive results are classical.
The resolution of the general reflexive case, with the stated norm and
the inclusion of zero and nonseparable spaces, is the novel
contribution claimed here; I cannot verify the fixed-point argument
independently from training alone.

## Consequences

- **Kirk's reflexive-space problem is resolved** [S3:8–11, S2:754,
  S4:9]: every nonexpansive self-map of a nonempty closed bounded
  convex subset of a real reflexive Banach space has a fixed point, in
  the original norm, with no uniform convexity assumption.
- **No uniform convexity needed** [S4:9]: the result holds for all
  reflexive Banach spaces, not just the uniformly convex subclass.
- **Zero and nonseparable spaces included** [S4:9]: the theorem does
  not exclude the trivial space nor require separability.
- **The bound is in the original norm** [S4:9, S5:21–29]:
  nonexpansiveness is the standard Lipschitz-1 condition in the given
  norm, not a weaker weak-topology condition.

## Section skeleton

One manuscript [S3:8–11]. Root `build/paper.tex` (20 lines;
`\documentclass` at [S3:1], `\input{preamble}` at [S3:2], title at
[S3:3], date at [S3:5]). Five `input` section files under `sections/`:
`00-introduction`, `01-preliminaries`, `02-anchor`, `03-tree`,
`04-switching`, plus an appendix `05-foundations`. A `references.bib`
bibliography. **No verification bundle.**

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S4:9], one comparator stub [S5], one `main_results` entry, and a
proved OAI tree. The T3 shape is "scope note, comparator stub,
`main_results` entry, and proved OAI tree all present."

The scope note [S4:9] selects the fixed-point theorem: every
nonexpansive self-map of a nonempty closed bounded convex subset of a
real reflexive Banach space has a fixed point in the original norm.
Zero and nonseparable spaces are included, with no uniform convexity,
normal structure, or weak-continuity assumption.

The single comparator stub carries 1 `sorry`:
`ReflexiveFixedPoints.lean` (35 lines) with
`theorem exists_fixedPoint_of_canonicallyReflexive` at [S5:21] and
the `sorry` at [S5:29]. The stub defines `CanonicallyReflexive`
(surjectivity of the canonical bidual inclusion) and states the
theorem with the set hypotheses (nonempty, closed, bounded, convex)
and the nonexpansiveness condition.

The proved OAI declaration is
`OAI.ReflexiveFixedPoints.exists_fixedPoint_of_canonicallyReflexive`
at `lean/OAI/Analysis/Nonexpansive/Main.lean` [S6:40]. The OAI tree
under `lean/OAI/Analysis/Nonexpansive/` comprises 86 `.lean` files
with 0 `sorry` occurrences — the fixed-point theorem is proved in the
OAI library. The reading is of source text only.

## Coverage

The ledger row `fam=328` [S7] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=418`, `verification=0`, `trace=`. The T3
shape is "scope note, comparator stub, `main_results` entry, and proved
OAI tree." The single comparator stub carries 1 `sorry`; the proved
OAI tree carries 0. The shape flags are
`shapes=resolution|bound|uniform`, `resolves_named=1`,
`counterex_broad=0`, `covmd=0` — a resolution family recording the
Kirk fixed-point resolution with a uniform (norm-based) bound, with no
coverage document in the manuscript directory.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7995] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 328 at [S2:754] |
| S3 | [`preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/build/paper.tex`](../../../preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/build/paper.tex) | 20 | manuscript; title [S3:3], date [S3:5], abstract [S3:8–11] |
| S4 | [`lean/docs/328.md`](../../../lean/docs/328.md) | 15 | scope note — Scope at [S4:9] and the comparator link `ReflexiveFixedPoints.lean` |
| S5 | [`lean/ComparatorChallenges/ReflexiveFixedPoints.lean`](../../../lean/ComparatorChallenges/ReflexiveFixedPoints.lean) | 35 | comparator stub — 35 lines, 1 `sorry` |
| S6 | [`lean/OAI/Analysis/Nonexpansive/Main.lean`](../../../lean/OAI/Analysis/Nonexpansive/Main.lean) | 77 | proved OAI declaration `OAI.ReflexiveFixedPoints.exists_fixedPoint_of_canonicallyReflexive` [S6:40] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=328`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
