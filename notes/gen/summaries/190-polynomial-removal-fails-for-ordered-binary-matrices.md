[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 190](../index/combinatorics/190-polynomial-removal-fails-for-ordered-binary-matrices.md)

# 190 — Polynomial removal fails for ordered binary matrices

[Index page](../index/combinatorics/190-polynomial-removal-fails-for-ordered-binary-matrices.md)

## Original CONTENTS.md summary

The release's blurb [S1:4384] and the catalog abstract [S2:461]
state the family's claim: a **counterexample** disproving
polynomial removal for ordered binary matrices, built from one
fixed $`66 \times 66`$ zero–one pattern. There are binary
matrices that require many entry changes to become
pattern-free while their ordered-copy density is smaller than
every proposed polynomial bound in that distance. Copies
preserve row and column orders and match both zeros and ones.
The manuscript is *Polynomial removal fails for ordered
binary matrices* [S3:29, S3:31]; its abstract


> We construct a fixed $`66\times66`$ binary matrix for which ordered matrix
removal has no polynomial bound. This disproves the polynomial ordered
binary matrix-removal conjecture. Ordered copies preserve the separate
row and column orders and match both zeros and ones; removal permits
changing entries in either direction. [S3:35–39]

## Undergraduate summary

An **ordered binary matrix** is a grid of zeros and ones
where the rows and columns each have a fixed left-to-right /
top-to-bottom order that a "copy" must respect. To find a
pattern inside a big matrix, you look for a smaller grid of
rows and columns (taken in their **increasing** order) whose
entries match the target exactly, zeros and ones alike. A
**removal bound** asks: if a matrix has very few copies of a
pattern, can you delete a small number of entries to destroy
them all? For **unordered** patterns, a polynomial relationship
between "few copies" and "few deletions" is known. This
constructs a specific $`66 \times 66`$ pattern for which that
relationship **breaks**: you can have a matrix with hardly any
copies of the pattern, yet the number of entries you must flip
to remove them all is **disproportionately large** —
larger than any polynomial in the copy density
[S3:35–39, S2:461].

## Graduate summary

**The main theorem** [S3:35–39, S4:9]. For a fixed
$`66 \times 66`$ binary pattern $`H`$, for every
$`c, C > 0`$ there exists an $`n \times n`$ binary matrix $`A`$
and $`\varepsilon > 0`$ such that $`A`$ is at normalized
Hamming (edit) distance at least $`\varepsilon`$ from being
$`H`$-free, while its count of **induced ordered** copies of
$`H`$ is fewer than
$`c\, \varepsilon^{C}\, n^{132}`$:

```
∀ c C : ℝ, 0 < c → 0 < C →
  ∃ n : ℕ, 1 ≤ n ∧ ∃ ε : ℝ, 0 < ε < 1 ∧
    ∃ A : BinaryMatrix n,
      fixedDistance A ≥ ε ∧
      (copyCount H A : ℝ) < c * ε^C * n^132
```

Row and column indices are independently increasing, every
zero and one entry must match, and removal permits changing
entries in **both** directions [S4:9, S5:63–70]. The
construction supplies an **explicit sequence** of such
matrices, parameterized by a height $`h`$
[S4:9, S6:11–24].

**The scope of the formalization.** The scope note states the
formalized result disproves the polynomial removal bound for
one explicit $`66 \times 66`$ binary pattern, with the
edit-distance and copy-density form above
[S4:9]. The scope note names one comparator [S4:15]:
`MatrixRemoval.lean`.

## History of the conjecture

**Removal lemmas** are a central theme in extremal combinatorics:
the Roth/Removal paradigm says that a set structure with very
few copies of a forbidden configuration can be made
configuration-free by deleting a **small** fraction of
elements — and the dependence of that fraction on the
copy density is the quantitative content. For **graph** and
**unordered matrix** settings, polynomial removal bounds are
known and nearly sharp. The **ordered** setting is harder
because the copy condition is asymmetric (rows and columns
must be increasing), and the counterintuitive behavior is that
the ordered structure can hide a **large removal cost** behind
a vanishing copy density. This manuscript provides the first
counterexample **with a single fixed pattern**: a
$`66 \times 66`$ zero–one matrix $`H`$ for which no
polynomial in the copy density bounds the edit distance
[S3:35–39, S2:461].

**Prior (my training data, not this repo).** I know the
Removal Lemma paradigm, Roth's theorem, and that polynomial
removal bounds hold for graph and unordered-matrix settings,
and that ordered (poset) settings are generally harder.
A **specific $`66 \times 66`$ ordered binary pattern** that
disproves **every** polynomial removal bound, with an explicit
constructive sequence parameterized by a height $`h`$ and a
$`386h+2`$ dimension, is a concrete counterexample I cannot
independently verify from training alone; the
`counterexample_sequence` and
`no_polynomial_removal_bound_of_sequence` machinery in [S6:26–34]
is not something I can recall.

## Consequences

**Polynomial ordered binary matrix removal is disproved.**
A single fixed $`66 \times 66`$ pattern $`H`$ has no polynomial
removal bound: for every $`c, C > 0`$ there is a matrix at
normalized edit distance $`\geq \varepsilon`$ from
$`H`$-free with fewer than
$`c\,\varepsilon^C n^{132}`$ induced ordered copies
[S3:35–39, S4:9, S2:461].

**The counterexample is explicit and constructive.** The
construction gives a sequence of matrices parameterized by a
height $`h`$, with dimension $`n = (386h+2) \cdot 2^h`$
[S6:11–24].

**Removal is two-sided.** The edit distance allows changing
entries in both directions (zeros to ones and ones to zeros)
[S4:9].

## Section skeleton

One manuscript [S3:35–39] (title [S3:29], date [S3:31]) —
`paper.tex` (49 lines) under `build/`, with sections
`01-introduction`, `02-construction`, `03-pinning`,
`03b-count`, `04-distance`, `05-conclusion` under
`build/sections/`, and a `figures/tree-orders.tex`
diagram. The family ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result disproves a
polynomial removal bound for one explicit
$`66 \times 66`$ binary pattern: for every $`c, C > 0`$ there is
an $`n \times n`$ binary matrix at normalized edit distance at
least $`\varepsilon > 0`$ from being pattern-free but with
fewer than $`c\,\varepsilon^{C}\, n^{132}`$ induced ordered
copies. Row and column indices are independently increasing
and every zero and one entry must match. The construction
gives an explicit sequence of such matrices, allowing edits in
both directions [S4:9]. The scope note names one comparator
[S4:15]: `MatrixRemoval.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml`
registers one `main_results` entry — the
`OAI.Problem348.no_polynomial_removal_bound` declaration at
`OAI/Combinatorics/MatrixRemoval/Main.lean` — and the
one manuscript is in its `sources:` listing. The comparator
`MatrixRemoval.lean` is registered
[S4:9, S4:15].

**The comparator stub.** The `MatrixRemoval.lean` comparator
defines `fixedMinEdits` (the minimum Hamming distance to a
pattern-free matrix) and `fixedDistance` (the normalized
version), then restates the target
`theorem no_polynomial_removal_bound` with a bare `sorry` body
[S5:53–71]:

```lean
theorem no_polynomial_removal_bound :
    ∀ c C : ℝ, 0 < c → 0 < C →
  ∃ n : ℕ, 1 ≤ n ∧
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
      ∃ A : BinaryMatrix n,
        fixedDistance A ≥ ε ∧
        (copyCount fixedH A : ℝ) <
          c * Real.rpow ε C * ((n : ℝ) ^ 132) := by
  sorry
```
[S5:63–71]

**What the proof does.** The registered
`no_polynomial_removal_bound` in the OAI tree is a genuine
proof, not a `sorry`: it is a one-line body
`exact no_polynomial_removal_bound_of_sequence
counterexample_sequence` [S6:26–34]. The work is in the
`counterexample_sequence` lemma [S6:11–24], which for
every height $`h \geq 1`$ sets $`d = 386h + 2`$ and
$`n = d \cdot 2^h`$, witnesses the matrix as
`Construction.hostMatrix (OrderedHost.rowIndex h)
(OrderedHost.columnIndex h)`, proves the edit-distance lower
bound by `OrderedHost.hammingDistance_ge`, and the copy-count
upper bound by `OrderedHost.canonical_copyCount_le` via
`SequenceAssembly.counterexample_sequence_of_integer_bounds`.
The `no_polynomial_removal_bound_of_sequence` consequence
lemma then converts the explicit sequence into the
$`\forall\, c\, C`$ polynomial-free form [S6:11–34].

**What the OAI tree does carry.** The
`OAI/Combinatorics/MatrixRemoval` package (**61 files over
7,609 lines, zero `sorry`**) carries the supporting
machinery: the `Construction.hostMatrix` host construction,
the `OrderedHost` row/column index and Hamming-distance and
copy-count lemmas, the `SequenceAssembly` integer-bounds
assembler, and the `Consequence`
`no_polynomial_removal_bound_of_sequence` reduction
[S6:11–34].

The release records `scope: "Partial progress."` and
`review: status: unchecked`; the comparator's `sorry` is the
target the release set, and the proved
`no_polynomial_removal_bound` in the OAI tree is the
registered result.

**Tree measurement (source-level).**

The `main_results` entry OAI.Problem348.no_polynomial_removal_bound resolves to `OAI/Combinatorics/MatrixRemoval/Main.lean` (40 lines); the top-level theorem is `theorem counterexample_sequence`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 61 files, 404 theorems, 128 defs.

The preprint states 9 theorem environments; the tree carries 45× as many (source-level count, not a proof-quality ratio).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 190 at [S1:4384] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{190} at [S2:461] |
| S3 | [`preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/build/paper.tex`](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/build/paper.tex) | 49 | the single manuscript root; title [S3:29], date [S3:31], abstract [S3:35–39] |
| S4 | [`lean/docs/190.md`](../../../lean/docs/190.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15] |
| S5 | [`lean/ComparatorChallenges/MatrixRemoval.lean`](../../../lean/ComparatorChallenges/MatrixRemoval.lean) | 77 | the comparator: the `fixedMinEdits` definition [S5:53–61], the `no_polynomial_removal_bound` theorem [S5:63–70] and the `sorry` [S5:71] |
| S6 | [`lean/OAI/Combinatorics/MatrixRemoval/Main.lean`](../../../lean/OAI/Combinatorics/MatrixRemoval/Main.lean) | 40 | the registered declaration in the OAI tree (61 files, 7609 lines, 0 sorry): the `counterexample_sequence` construction [S6:11–24] and the real `no_polynomial_removal_bound` proof [S6:26–34] via `no_polynomial_removal_bound_of_sequence` |
