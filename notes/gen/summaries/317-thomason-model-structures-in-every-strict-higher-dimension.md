[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 317](../index/topology/317-thomason-model-structures-in-every-strict-higher-dimension.md)

# 317 — Thomason model structures in every strict higher dimension

[Index page](../index/topology/317-thomason-model-structures-in-every-strict-higher-dimension.md)

## Original CONTENTS.md summary

[S1:7765] (family entry):

> **317. Thomason model structures in all strict higher dimensions.** Resolves the Ara–Maltsiniotis conjecture: for every <i>n</i> ≥ 1 and <i>n</i> = <i>ω</i>, small strict globular <i>n</i>-categories admit proper combinatorial Thomason model structures Quillen equivalent to simplicial sets. Thus strict higher categories model the homotopy theory of spaces in every stated dimension. ([Lean](../../../lean/docs/317.md))

[S2:730] carries the `\resultentry` with the single manuscript [S3:70, S3:72]. The abstract:

> We prove the higher-dimensional Thomason model-structure conjecture of
Ara and Maltsiniotis. For every $`1\le n\le\infty`$, the category of small
strict globular $`n`$-categories admits a proper combinatorial model structure
that is Quillen equivalent to simplicial sets. Its weak equivalences and
fibrations are detected by the twice-extended Street nerve $`\mathrm{Ex}^2N_n`$, and
the Quillen equivalence is given by $`c_n\mathrm{Sd}^2\dashv\mathrm{Ex}^2N_n`$. Thus strict
higher categories model the homotopy theory of spaces in every positive
finite dimension and in dimension $`\omega`$. [S3:75–84]

## Undergraduate summary

A **model structure** is a way of deciding, inside a category, which maps
should behave like "weak equivalences," "fibrations," and "cofibrations" —
the three ingredients that let you do homotopy theory in that category.
Classically, homotopy theory lives on **spaces and simplicial sets**. A
**Thomason model structure** is the result of putting such a structure on a
different category — here, the category of **strict globular $`n`$-categories**
— so that it ends up **Quillen equivalent** to simplicial sets. "Quillen
equivalent" means the two categories carry exactly the same homotopy
information, just packaged differently.

The **Ara–Maltsiniotis conjecture** predicted that this is possible in
**every** strict higher dimension. The paper proves it: for every $`n \ge 1`$
and for $`n = \omega`$ (the "infinite" dimension where all the higher cells
are present), the category of small strict globular $`n`$-categories carries a
**proper combinatorial** model structure that is Quillen equivalent to
simplicial sets. The weak equivalences are read off by the **Street nerve**,
the functor that converts an $`n`$-category back into a simplicial set.

## Graduate summary

**The higher-dimensional Thomason model-structure theorem (formalized)**
[S4:9, S2:730].
For every positive finite $`n`$ and for $`n = \omega`$, the category of small
strict globular $`n`$-categories admits a proper combinatorial model structure
that is Quillen equivalent to simplicial sets. The Quillen equivalence is
given by the adjunction
$`c_n \mathrm{Sd}^2 \dashv \mathrm{Ex}^2 N_n`$,
where $`c_n \mathrm{Sd}^2`$ is the twice-subdivided categorification and
$`\mathrm{Ex}^2 N_n`$ is the twice-extended Street nerve.

**Weak equivalences detected by the Street nerve** [S4:11, S2:730].
In every stated dimension, the weak equivalences of the Thomason model
structure are precisely those maps $`f`$ for which $`N_n f`$ is a weak
equivalence of simplicial sets (after the twice-extended Street-nerve
normalization). This is the "nerve detection" clause: the model structure is
not just equivalent to simplicial sets, it is calibrated by the nerve
functor.

**The scope boundary.** The scope note [S4:9–11] covers the positive finite
dimensions and the dimension $`\omega`$ for small strict globular
$`n`$-categories. The constructions model the homotopy theory of spaces
throughout that stated range [S4:11].

## History of the conjecture

The Thomason model structure is a cornerstone result: Thomason (1980)
first showed that the category of small categories (the case $`n=1`$)
carries a cofibrantly generated model structure Quillen equivalent to
simplicial sets, via the nerve functor. The **Ara–Maltsiniotis
conjecture** generalized this to the strict higher-categorical setting:
that strict globular $`n`$-categories, for every $`n`$ (including the
limiting $`\omega`$-case), should admit analogous model structures.

The proof route here is combinatorial: the weak equivalences and
fibrations are detected by the twice-extended Street nerve, and the
Quillen equivalence comes from the twice-subdivided categorification.
The "proper combinatorial" qualifier is load-bearing — it rules out
pathological model structures and ensures the category behaves well
enough for the usual homotopical machinery.

**Prior (my training data, not this repo).** Thomason's $`n=1`$ model
structure and the Street nerve on globular $`n`$-categories are classical.
The extension to every positive finite dimension and to the dimension
$`\omega`$, with the proper combinatorial quality and the
$`c_n \mathrm{Sd}^2 \dashv \mathrm{Ex}^2 N_n`$ Quillen equivalence, is the
novel contribution claimed here; I cannot verify the
higher-categorical model-category arguments independently from training
alone.

## Consequences

- **The Ara–Maltsiniotis conjecture is resolved** [S3:75–77, S2:730]:
  for every $`n \ge 1`$ and $`n=\omega`$, small strict globular
  $`n`$-categories admit a proper combinatorial Thomason model structure
  Quillen equivalent to simplicial sets.
- **A uniform Quillen equivalence across all dimensions** [S3:78–81,
  S4:9]: the adjunction $`c_n \mathrm{Sd}^2 \dashv \mathrm{Ex}^2 N_n`$
  gives the equivalence in every stated dimension, with the same
  twice-subdivided / twice-extended normalization.
- **Weak equivalences are nerwise** [S4:11, S2:730]: the weak
  equivalences of the model structure are identified by the Street
  nerve in all stated dimensions.
- **Strict higher categories model spaces** [S3:82–84, S4:11]: the
  constructions recover the homotopy theory of spaces throughout the
  stated range, so strict globular $`n`$-categories (including
  $`\omega`$-categories) are homotopically faithful to simplicial sets.

## Section skeleton

One manuscript [S3:75–84]. Root `build/paper.tex` (98 lines; an
epstopdf guard precedes the `\documentclass` at [S3:2]), sections under
`build/sections/`: `01-introduction`, `02-foundations`,
`03-relative-prisms`, `04-labelled-pieces`, `05-couniversality`,
`06-subdivided-attachments`, `07-model-structure`, and the appendix
files `09-presentability`, `08-method-context`. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note [S4]
and one comparator stub [S5]. There is **no** `main_results` entry, and
no proved OAI tree. The T2 shape is "scope note and comparator stubs
exist, but no `main_results` entry and no proved OAI tree."

The scope note [S4:9] selects the higher-dimensional Thomason
model-structure theorem for small strict globular $`n`$-categories in every
positive finite dimension and in dimension $`\omega`$, Quillen equivalent to
simplicial sets through the twice-subdivided categorification and
twice-extended Street nerve adjunction. The scope note [S4:11] adds that
the selected statements identify weak equivalences by the Street nerve in
all these dimensions.

The single comparator stub carries 2 `sorry` occurrences:
`ThomasonModelStructures.lean` (2473 lines) with
`theorem Thomason.main` at [S5:2460] (the `sorry` at [S5:2461]) and
`theorem Thomason.nerveDetection_allDimensions` at [S5:2463] (the
`sorry` at [S5:2468]). No proved copy exists under `lean/OAI/`. The
reading is of source text only.

## Coverage

The ledger row `fam=317` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=568`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub exist, with no `main_results`
entry." The single comparator stub carries 2 `sorry`. The shape flags
are `shapes=resolution|uniform`, `resolves_named=1`, `counterex_broad=0`,
`covmd=0` — a resolution/uniform family recording the
Ara–Maltsiniotis resolution, with no coverage document in the manuscript
directory.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7765] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 317 at [S2:730] |
| S3 | [`preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/build/paper.tex`](../../../preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/build/paper.tex) | 98 | manuscript; title [S3:70], date [S3:72], abstract [S3:75–84] |
| S4 | [`lean/docs/317.md`](../../../lean/docs/317.md) | 17 | scope note — Scope at [S4:9–11] and the comparator link `ThomasonModelStructures.lean` |
| S5 | [`lean/ComparatorChallenges/ThomasonModelStructures.lean`](../../../lean/ComparatorChallenges/ThomasonModelStructures.lean) | 2473 | comparator stub — 2473 lines, 2 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=317`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
