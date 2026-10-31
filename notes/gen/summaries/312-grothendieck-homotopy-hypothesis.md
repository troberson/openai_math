[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 312](../index/topology/312-grothendieck-homotopy-hypothesis.md)

# 312 — The Grothendieck homotopy hypothesis

[Index page](../index/topology/312-grothendieck-homotopy-hypothesis.md)

## Original CONTENTS.md summary

[S1:7685] (family entry):

> **312. The Grothendieck homotopy hypothesis.** Proves the Grothendieck homotopy hypothesis for ∞-groupoids associated with every Grothendieck coherator in the Ara–Henry convention: these algebraic objects recover the homotopy theory of spaces. ([Lean](../../../lean/docs/312.md))

[S2:720] carries the `\resultentry` with the single manuscript [S3:3, S3:5]. The abstract:

> We prove the Grothendieck homotopy hypothesis for every Grothendieck
coherator in the Ara–Henry convention: its weak globular infinity-groupoids
recover the homotopy theory of spaces.
We also resolve Henry's pushout conjecture, showing that elementary expansions
preserve components and all homotopy groups of cellular infinity-groupoids. [S3:8–14]

## Undergraduate summary

The **Grothendieck homotopy hypothesis** asks a deceptively simple question:
can you capture everything about the shape of a space using purely
**algebraic** bookkeeping? Just as the fundamental group captures
1-dimensional "loop" information, an **infinity-groupoid** (or
$`\infty`$-groupoid) is supposed to capture all higher-dimensional
homotopical data — not just loops, but also the "loops of loops," the
"loops of loops of loops," and so on.

The conjecture says these algebraic objects should be **sufficient**: if
you build the right $`\infty`$-groupoid from a space, you should be able to
recover its full homotopy type from the algebraic data alone.

This paper proves the hypothesis for a specific family of algebraic
structures called **Grothendieck coherators** (in the Ara–Henry
convention). The key technical ingredient is the **elementary expansion
theorem**: a precise statement about what happens when you attach a
higher-dimensional "disk" to an algebraic model along its boundary. The
theorem says this operation is a **weak equivalence** — it doesn't change
the algebraic "shape" of the model, just as attaching a disk to a topological
space doesn't change its homotopy type in a meaningful way.

## Graduate summary

**The elementary-expansion weak equivalence (formalized)** [S4:9, S2:720].
For every Grothendieck coherator $`C`$ in the Ara–Henry convention and every
boundary-cellular model $`X`$ of $`C`$, attaching an $`(n+1)`$-disk along its
source $`n`$-face induces a weak equivalence. Formally, given a pushout square
where $`X`$ is a cellular model, $`a: \text{disk}(C, n) \to X`$ is the
attachment of an $`n`$-disk, and $`i: X \to Y`$ is the inclusion after
attaching the $`(n+1)`$-disk, the map $`i`$ is a weak equivalence in the
$`\infty`$-groupoid model.

**Henry's pushout conjecture** [S3:12–14, S2:720].
The paper also resolves Henry's pushout conjecture: elementary expansions
preserve the connected components and all homotopy groups $`\pi_k`$ for
$`k \geq 0`$ of cellular $`\infty`$-groupoids. This is the algebraic content
that the elementary expansion is a "shape-preserving" operation in the
strongest sense.

**The scope boundary.** The scope note [S4:9] formalizes only the
elementary-expansion weak equivalence theorem. The later semi-model
structure and the full comparison with classical homotopy theory of spaces
are **not included** in the formalization [S4:11].

## History of the conjecture

The Grothendieck homotopy hypothesis is one of the foundational
conjectures of higher category theory, proposed informally by
Grothendieck in the 1960s and made precise in various forms by
Simpson, Ara, Henry, and others. It sits at the intersection of
category theory, algebraic topology, and homotopical algebra: the
question is whether the algebraic abstraction is faithful, i.e., whether
no homotopical information is lost in passing from spaces to
$`\infty`$-groupoids.

The Ara–Henry convention is one of several competing algebraic
formalizations of $`\infty`$-groupoids. The "coherator" is the
higher-categorical structure that encodes the coherent relations
between the higher cells. A "boundary-cellular model" is a model
built from a presentation by boundary generators — the algebraic
analogue of a CW-complex built from attaching maps.

**Prior (my training data, not this repo).** The Grothendieck
homotopy hypothesis is a long-standing open problem in higher category
theory, with partial results for specific models of $`\infty`$-groupoids.
A proof via elementary expansions for the Ara–Henry coherators, together
with the resolution of Henry's pushout conjecture, is the novel
contribution claimed here; I cannot verify the coherence-theoretic
arguments independently from training alone.

## Consequences

- **The Grothendieck homotopy hypothesis holds for Ara–Henry
  coherators** [S3:8–11, S2:720]: the weak globular
  $`\infty`$-groupoids associated with every Grothendieck coherator in
  the Ara–Henry convention recover the homotopy theory of spaces.
- **Elementary expansions are weak equivalences** [S4:9, S2:720]:
  attaching an $`(n+1)`$-disk along its source $`n`$-face to a
  boundary-cellular model induces a weak equivalence — the key
  technical lemma underlying the full theorem.
- **Henry's pushout conjecture is resolved** [S3:12–14, S2:720]:
  elementary expansions preserve all homotopy groups of cellular
  $`\infty`$-groupoids, confirming that the algebraic operation is
  homotopically faithful in the strongest sense.
- **The formalization reaches the elementary-expansion theorem only**
  [S4:11]: the semi-model structure and the full comparison with the
  classical homotopy theory of spaces are outside the formalized
  scope.

## Section skeleton

One manuscript [S3:8–14]. Root `build/paper.tex` (22 lines), sections
under `build/sections/`: `00-introduction`, `01-preliminaries`,
`02-cutoffs-trees`, `03-partial-cylinders`, `04-consequences`. No
verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note [S4],
one comparator stub [S5], one `main_results` entry, and a proved OAI tree.
The T3 shape is "scope note, comparator stub, `main_results` entry, and
proved OAI tree all present."

The scope note [S4:9] formalizes the elementary-expansion weak
equivalence: attaching an $`(n+1)`$-disk along its source $`n`$-face to a
boundary-cellular model of a Grothendieck coherator in the Ara–Henry
convention induces a weak equivalence. The scope note [S4:11] excludes
the later semi-model structure and the full comparison with the
homotopy theory of spaces.

The single comparator stub carries 1 `sorry`:
`GrothendieckElementaryExpansion.lean` (476 lines) with
`theorem elementary_expansion` at [S5:465] and the `sorry` at [S5:472].

The proved OAI declaration is `OAI.Grothendieck.elementary_expansion`
at `lean/OAI/CategoryTheory/Globular/ElementaryExpansion.lean` [S6:34].
The OAI tree under `lean/OAI/CategoryTheory/Globular/` comprises 58 `.lean`
files with 0 `sorry` occurrences — the elementary-expansion theorem is
proved in the OAI library. The reading is of source text only.

**Tree measurement (source-level).**

The `main_results` entry OAI.Grothendieck.elementary_expansion resolves to `OAI/CategoryTheory/Globular/ElementaryExpansion.lean` (66 lines); the top-level theorem is `theorem exactBoundaryTest_at_of_low_square.{v} {X Y R S`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 58 files, 380 theorems, 379 defs.

The preprint states 19 theorem environments; the tree carries 20× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=312` [S7] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=479`, `verification=0`, `trace=`. The T3
shape is "scope note, comparator stub, `main_results` entry, and proved
OAI tree." The single comparator stub carries 1 `sorry`; the proved
OAI tree carries 0. The shape flags are `shapes=` (empty),
`resolves_named=0`, `counterex_broad=0`, `covmd=0` — a resolution
family (the Grothendieck homotopy hypothesis) with no coverage document
in the manuscript directory.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7685] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 312 at [S2:720] |
| S3 | [`preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/paper.tex`](../../../preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/paper.tex) | 22 | manuscript; title [S3:3], date [S3:5], abstract [S3:8–14] |
| S4 | [`lean/docs/312.md`](../../../lean/docs/312.md) | 17 | scope note — Scope at [S4:9], exclusion at [S4:11], comparator link `GrothendieckElementaryExpansion.lean` |
| S5 | [`lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean`](../../../lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean) | 476 | comparator stub — 476 lines, 1 `sorry` |
| S6 | [`lean/OAI/CategoryTheory/Globular/ElementaryExpansion.lean`](../../../lean/OAI/CategoryTheory/Globular/ElementaryExpansion.lean) | 66 | proved OAI declaration `OAI.Grothendieck.elementary_expansion` [S6:34] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=312`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
