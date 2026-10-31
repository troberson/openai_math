[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 367](../index/partial-differential-equations/367-critical-dimension-for-the-one-phase-bernoulli-problem.md)

# 367 — The critical dimension for the one-phase Bernoulli problem

[Index page](../index/partial-differential-equations/367-critical-dimension-for-the-one-phase-bernoulli-problem.md)

## Original CONTENTS.md summary

[S1:8897] (family entry):

> **367. The critical dimension for the one-phase Bernoulli problem.** Establishes seven as the first dimension admitting a nonflat, one-homogeneous global minimizer of the one-phase Bernoulli energy. Consequently, minimizing free boundaries are smooth through dimension six, and their singular sets have dimension at most $`n-7`$ in higher dimensions. ([Lean](../../../lean/docs/367.md))

[S2:836] carries the `\resultentry` with a single manuscript [S3].
The scope note [S4:9] states the formalized result as the
**existence** side only, and places the flatness classification and
regularity consequences "outside" that selected statement [S4:11]:

> The paper identifies seven as the critical dimension for nonflat one-homogeneous global minimizers of the one-phase Bernoulli problem. The linked formalization proves the existence side: in dimension seven there is a nonzero one-homogeneous global minimizer that is not a half-space solution. [S4:9]

## Undergraduate summary

The **one-phase Bernoulli problem** is a model for a fluid-structure
interface: a nonnegative function $`u`$ minimizes an energy that
penalizes both its gradient (elastic energy in the fluid) and the
region where it is positive (surface area of the interface). A
**global minimizer** is a function that wins this competition in every
ball simultaneously.

A key question is: what is the **first dimension** where a
nontrivial shape can appear? The nonzero **flat** minimizers are the
simple half-spaces $`u(x)=(x\cdot e)_+`$ — the interface is a flat
hyperplane. The result here says that in dimensions 1 through 6, every
nonzero one-homogeneous global minimizer is **flat** (the interface
must be planar). Only in dimension 7 does a **genuinely curved**
minimizer exist — a nonflat shape.

Consequently, the **free boundary** (the interface) of a local
minimizer is smooth in dimensions at most 6, and in higher dimensions
its **singular set** (where the boundary fails to be smooth) has
Hausdorff dimension at most $`n-7`$ — a sharp bound achieved by taking
Cartesian products of the dimension-7 construction.

The release formalizes the **existence** half of this result (the
nonflat minimizer in dimension 7), not the flatness-through-six part
[S4:9, S4:11].

## Graduate summary

**Main theorem** [S3:73–80, S1:8897].
Every nonzero one-homogeneous global minimizer of the one-phase
Bernoulli energy in $`\mathbb R^d`$, $`1\le d\le 6`$, is flat. There is
a nonflat one-homogeneous global minimizer in $`\mathbb R^7`$.
Consequently, $`d_*=7`$.

**Consequences (corollary)** [S3:90–99].
The interior free boundary of a nonnegative local minimizer is smooth
outside its singular set. This set is empty when $`n\le 6`$, is locally
finite when $`n=7`$, and satisfies
$`\dim_{\mathrm H}\mathrm{Sing}(u)\le n-7`$ for $`n\ge 7`$. For
every $`n\ge 7`$, a global minimizer attains this dimension bound
[sharpness by Cartesian products of the De Silva–Jerison cone].

**The formalization is T2, not T3** [S4, S5, S7].
The scope note [S4:9] and one comparator stub [S5] are present, but
there is **no** `main_results` entry and **no** proved OAI tree
[S7]. The comparator stub `BernoulliNonflatInSeven.lean` (86 lines)
states `theorem nonflat_in_seven` [S5:78] with the `sorry` at
[S5:80] (1 in this stub), and the statement is left as a challenge,
not promoted to a proved declaration. The T2 shape is "scope note
plus comparator stub, no `main_results` entry, no OAI tree."

**The formalization is asymmetric with the theorem** [S4:11, S5].
The scope note proves the **existence** side only: "in dimension seven
there is a nonzero one-homogeneous global minimizer that is not a
half-space solution" [S4:9]. "The flatness classification in
dimensions at most six and the resulting regularity and singular-set
bounds are **outside** this selected statement" [S4:11]. The
comparator stub states the existence claim:
`theorem nonflat_in_seven : ∃ u : Space 7 → ℝ, GlobalMinimizer u ∧
Nonzero u ∧ OneHomogeneous u ∧ ¬ Flat u` [S5:78–79]. The flatness
half (minimizers in $`d\le 6`$ are flat) is not the formalized
statement.

## History of the conjecture

The **one-phase Bernoulli problem** models a free-boundary variational
problem: minimize $`\int(|\nabla u|^2 + \mathbf 1_{\{u>0\}})`$ over
nonnegative functions. The classical work of **Berger** (1977) and
**Caffarelli–Salsa–Silvestre** (2008) established regularity and
classification results for the free boundary in low dimensions. The
**De Silva–Jerison** (2010) construction of a nonflat one-homogeneous
minimizer in dimension 7 was a landmark, showing that the flatness
classification breaks at dimension 7 — but the sharp dimension
identification $`d_*=7`$ (flatness for *all* $`d\le 6`$ plus existence at
$`d=7`$) is the complete statement.

The **novel contribution** is the **complete two-sided
identification** [S3:73–80]: the flatness classification in all
dimensions at most 6 *and* the existence of a nonflat minimizer in
dimension 7, with the sharp singular-set bound $`n-7`$ as a
consequence [S3:90–99]. The flatness proof reduces a hypothetical
first nonflat minimizer to a smooth spherical component in dimension
6, allowing two suspension tips, then derives tensor identities and
a universal algebraic certificate (verified by finite arithmetic) that
forces a contradiction [S3:53–55]. The singular-set sharpness follows
by Cartesian products of the De Silva–Jerison cone with Euclidean
space [S3:98–99].

**Prior (my training data, not this repo).** As of my training cutoff,
the De Silva–Jerison nonflat minimizer in dimension 7 was known, and
the flatness in dimensions at most 6 for the one-homogeneous class
was an open question. The complete two-sided identification $`d_*=7`$
with the sharp singular-set bound was at the frontier of the
free-boundary regularity theory. I cannot verify the variational
analysis independently from training alone.

## Consequences

- **$`d_*=7`$ is the critical dimension** [S3:73–80, S1:8897]: every
  nonzero one-homogeneous global minimizer in $`\mathbb R^d`$ for
  $`1\le d\le 6`$ is flat, and a nonflat one exists in $`\mathbb R^7`$.
- **Free boundaries are smooth through dimension 6**
  [S3:90–99]: the singular set of a local minimizer is empty when
  $`n\le 6`$.
- **Sharp singular-set bound in higher dimensions** [S3:90–99]:
  for $`n\ge 7`$, the singular set has Hausdorff dimension at most
  $`n-7`$, and this bound is attained.
- **The formalization covers only the existence half**
  [S4:9, S4:11]: the T2 comparator stub states the existence of a
  nonflat minimizer in dimension 7; the flatness classification and
  regularity/singular-set bounds are explicitly outside the
  formalized statement.
- **A finite-arithmetic certificate ships with the manuscript**
  [S6]: the verification bundle (`checks/reproduce.py` and
  `independent-certificate/`) mechanically verifies the algebraic
  certificate the flatness proof relies on.

## Section skeleton

One manuscript, `build/paper.tex` root (136 lines). The root
declares the theorem environments and macros inline, the main
theorem at [S3:73–80], the corollary at [S3:90–99], and 8 `input`
section files [S3:106–130]: `history`, `reductions`, `geometry`,
`certificate`, `flux`, `certificate-proof`, `cutoffs`,
`consequences`, plus an appendix `tables.tex` [S3:133] and a
`references.tex` [S3:135]. The manuscript also ships a
**verification bundle** [S6] with two subdirectories: `checks/`
(`reproduce.py`, `generate_tables.py`, `test_reproduce.py`) and
`independent-certificate/` (`engine.py`, `bounds.py`,
`compare_oracle.py`).

## Coverage

The ledger row `fam=367` [S7] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=437`, `verification=1`, `trace=`,
`companions=`. The T2 shape is "scope note plus comparator stub,
no `main_results` entry, no OAI tree." The single comparator stub
carries 1 `sorry` [S5:80]. The shape flags are
`shapes=bound|partial`, `resolves_named=1`, `counterex_broad=0`,
`covmd=0` — a **bound** (the critical dimension 7) with a
**partial** character (the formalization covers the existence half
only). `resolves_named=1` is the "one-phase Bernoulli problem"
named in the title. The `verification=1` is the finite-arithmetic
certificate bundle [S6] (the algebraic certificate check and the
independent oracle comparison). Note `paps_form=0`: the manuscript
does not appear in `formalization.yaml`'s `sources:` list, and there
is no `main_results` entry — the T2 formalization is the scope
note's description and the comparator's challenge only, with no
proved Lean surface.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8897] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 367 at [S2:836] |
| S3 | [`preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/build/paper.tex`](../../../preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/build/paper.tex) | 136 | the `\documentclass` root — 136 lines, title [S3:37], date [S3:39], abstract [S3:43–51], theorem [S3:73–80], corollary [S3:90–99], 8 `input` section files [S3:106–130], 1 appendix [S3:133], references [S3:135] |
| S4 | [`lean/docs/367.md`](../../../lean/docs/367.md) | 17 | scope note — Scope at [S4:9–11], comparator link at [S4:17] |
| S5 | [`lean/ComparatorChallenges/BernoulliNonflatInSeven.lean`](../../../lean/ComparatorChallenges/BernoulliNonflatInSeven.lean) | 86 | comparator stub — 86 lines, `def Flat` [S5:75], `theorem nonflat_in_seven` [S5:78], `sorry` [S5:80] |
| S6 | [`preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/verification/checks/reproduce.py`](../../../preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/verification/checks/reproduce.py) | 448 | finite-arithmetic certificate — the shipped reproduction script in the verification bundle |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=367`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
