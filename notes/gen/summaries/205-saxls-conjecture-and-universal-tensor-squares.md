[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 205](../index/algebra/205-saxls-conjecture-and-universal-tensor-squares.md)

# 205 — Saxl's conjecture and universal tensor squares

[Index page](../index/algebra/205-saxls-conjecture-and-universal-tensor-squares.md)

## Original CONTENTS.md summary

The release's blurb [S1:4682] and the catalog abstract [S2:493]
state the family's claim: Saxl's conjecture proved —
the tensor square of every staircase representation
contains every irreducible complex representation of the
corresponding symmetric group. More generally, every
$S_n$ with $n \notin \{2,4,9\}$ has an irreducible
representation whose tensor square contains all
irreducibles. The family ships two manuscripts [S1:4682]:

- *Universal Tensor Squares for Symmetric
  Groups* [S3:51, S3:53]
- *A Cyclic Polytabloid Proof of Saxl's
  Conjecture* [S4:50, S4:52]

The universal tensor squares abstract 

> For every positive integer $n$ other than $2$, $4$, and $9$, we prove that
some irreducible complex representation of $S_n$ has a tensor square [S3:56–58]

The cyclic polytabloid proof abstract 

> For every staircase partition, we prove that the tensor square of the
corresponding irreducible complex representation of the symmetric group [S4:55–57]

## Undergraduate summary

A **symmetric group** $S_n$ (permutations of $n$ objects)
has a "building block" structure for its
representations — ways the group acts on a vector
space. The irreducible representations are classified
by **partitions** (ways to write $n$ as a sum of
non-increasing positive integers). The **tensor
square** of a representation $V$ is $V \otimes V$
— "multiplying" the representation by itself. A
representation is **universal** (in this context) if its
tensor square contains every irreducible representation
as a subrepresentation. **Saxl's conjecture** says: the
**staircase** partitions (those shaped like
$(m, m-1, \ldots, 1)$) give universal tensor squares.
This manuscript pair says **yes** — for every
staircase, the tensor square of the representation
contains all irreducibles. More generally, for
$n \notin \{2, 4, 9\}$, some irreducible
representation has this property [S3:56–58,
S4:55–57, S2:493].

## Graduate summary

**The universal tensor square theorem**
[S3:56–58, S2:493]. For every positive integer $n$
with $n \notin \{2,4,9\}$, there exists an
irreducible complex representation $V$ of $S_n$ such
that for every irreducible complex representation
$W$ of $S_n$, $\mathrm{Hom}_{S_n}(W, V
\otimes V) \neq 0$. Equivalently, all corresponding
Kronecker coefficients $g(\lambda, \lambda,
\mu) > 0$.

**The Saxl conjecture (staircase form)** [S4:55–57,
S2:493]. For every $m \geq 1$, let
$\rho_m = (m, m-1, \ldots, 1)$ be the staircase
partition of $m(m+1)/2$. Then
$g(\rho_m, \rho_m, \mu) > 0$ for every partition
$\mu$ of $m(m+1)/2$.

**The scope of the formalization.** The scope note
covers both results [S5:10, S5:12]. The universal
form: for every $n \notin \{2,4,9\}$, the
formalization constructs an irreducible whose tensor
square contains every irreducible, and supplies
injective intertwining maps [S5:10]. The
staircase form: for every $m \geq 1$,
$g(\rho_m, \rho_m, \mu) > 0$ [S5:12]. The
stronger claim that every constituent appears in the
orbit span of one prescribed tensor is not included
[S5:14]. The scope note names two comparators
[S5:20–21]: `Saxl.lean` and
`UniversalTensorSquares.lean`.

## History of the conjecture

**Saxl's conjecture** (1972) predicts that the tensor
square of the staircase Specht module contains every
irreducible representation of the corresponding
symmetric group. It is a special case of the **tensor
square conjecture** for symmetric groups, which asks
for which $n$ there exists an irreducible
representation whose tensor square is "universal"
(contains every irreducible as a constituent). The
exceptions $n \in \{2, 4, 9\}$ are the only degrees
where no such representation exists. Known partial
results: the staircase case was verified computationally
for small $m$, and the universal case was proved for
$S_3$, $S_5$, $S_6$, $S_7$, $S_8$ by direct computation.
The two manuscripts attack the conjecture from
complementary directions: the first classifies
candidate partitions by **band structure** and
**capacity**, proving the universal form via a
geometric-combinatorial argument with a
**finite-verification** appendix; the second proves
the staircase form via **cyclic polytabloid**
construction and **path-band** analysis
[S3:56–58, S4:55–57, S2:493].

**Prior (my training data, not this repo).** I know
Saxl's conjecture as a named open problem in symmetric
group representation theory, the staircase partition
as the conjectured universal tensor square, and the
exception set $\{2,4,9\}$. The **full proof** —
the universal form via band structure and capacity, and
the staircase form via cyclic polytabloids — is a
result I cannot independently verify from training
alone.

## Consequences

**Saxl's conjecture is proved.** The tensor square of
every staircase Specht module contains every
irreducible representation [S4:55–57, S2:493].

**The universal tensor square conjecture is proved.**
Every $S_n$ with $n \notin \{2,4,9\}$ has an
irreducible representation whose tensor square contains
all irreducibles [S3:56–58, S2:493].

**The exceptions are characterized.** $n \in
\{2,4,9\}$ are the only degrees where no universal
tensor square exists [S3:56–58].

## Section skeleton

Two manuscripts: [S3:56–58] (title [S3:51], date [S3:53])
— `main.tex` under `build/` with eight sections
under `build/sections/` (`introduction`, `preliminaries`,
`candidate`, `band`, `balance`, `capacity`, `finite`,
`completion`) and a `references.tex`, plus a
`verification/` bundle with `code/` (capacity_checks.py,
capacity_independent.py, smallcode_submitted.cpp,
smallcode_dump.cpp, smallcode_verify.py,
test_smallcode_verify.py) and `computation/`
(README.md, RESULTS.json, and four log files); [S4:55–57]
(title [S4:50], date [S4:52]) — `paper.tex` under
`build/` with six sections under `build/sections/`
(`introduction`, `specht-tools`, `dominance`,
`band-quotient`, `path-band`, `completion`) and a
`references.tex`.

## Comparison with the formalized statement

**Scope note** [S5:10, S5:12]. The scope note covers
both results. The universal form: for every $n
\notin \{2,4,9\}$, the formalization constructs an
irreducible complex representation of $S_n$ whose
tensor square contains every irreducible, and supplies
injective intertwining maps [S5:10]. The
staircase form: for every $m \geq 1$,
$g(\rho_m, \rho_m, \mu) > 0$ [S5:12]. The
stronger claim about orbit span of one prescribed
tensor is not included [S5:14]. The scope note names
two comparators [S5:20–21]: `Saxl.lean` and
`UniversalTensorSquares.lean`.

**The registration.** The family is at tier T3: the
ledger row records `mainres 1` and `paps_form 1`.
`formalization.yaml` registers one `main_results`
entry: `OAI.Saxl.saxl_conjecture` at
`OAI/RepresentationTheory/Saxl/Main.lean`. The one
registered manuscript (M2, the cyclic polytabloid
proof) is in the `sources:` listing. The other
manuscript (M1, universal tensor squares) is **not**
in the yaml `sources:` listing.

**The Saxl comparator stub.** The `Saxl.lean`
comparator defines the `staircase` partition
[S6:97–104], the `SaxlConjecture` proposition
[S6:107–110], and states
`theorem saxl_conjecture : SaxlConjecture` with a bare
`sorry` body 

```lean
theorem saxl_conjecture : SaxlConjecture := by
  sorry
```
[S6:112–113]

**What the OAI tree carries.** One OAI package carries
a real non-`sorry` proof:

- `OAI/RepresentationTheory/Saxl` (**38 files over
  7,558 lines, zero `sorry`**): the
  `saxl_conjecture` proof [S7:88] discharges by
 `saxl_of_cyclic_support cyclic_saxl_conjecture`:

```lean
theorem saxl_conjecture : SaxlConjecture := saxl_of_cyclic_support cyclic_saxl_conjecture
```
[S7:88]

**The UniversalTensorSquares comparator stub.** The
`UniversalTensorSquares.lean` comparator states
`theorem universal_tensor_square` with a bare `sorry`
body [S8:91, S8:104]. No OAI tree entry is registered
for this comparator: the universal tensor square
result is not in `main_results`.

**The verification bundle.** M1 ships a
`verification/` bundle with two components:
`code/` (capacity_checks.py, capacity_independent.py,
smallcode_submitted.cpp, smallcode_dump.cpp,
smallcode_verify.py, test_smallcode_verify.py) and
`computation/` (README.md, RESULTS.json, and four log
files: capacity-exceptional.log,
capacity-independent.log, capacity-intermediate.log,
character-61-degrees.log, character-independent-1-12.log).
A `verification/computation/README.md` names the run
command.

The release records `scope: "Partial progress."` and
`review: status: unchecked`. The Saxl `sorry` stub is
answered by a real proof in the OAI tree. The
UniversalTensorSquares `sorry` stub has no OAI tree
answer.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 205 at [S1:4682] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{205} at [S2:493] |
| S3 | [`preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/build/main.tex`](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/build/main.tex) | 108 | manuscript 1 of 2 (universal tensor squares); title [S3:51], date [S3:53], abstract [S3:56–58] |
| S4 | [`preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/build/paper.tex`](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/build/paper.tex) | 68 | manuscript 2 of 2 (cyclic polytabloid proof of Saxl); title [S4:50], date [S4:52], abstract [S4:55–57] |
| S5 | [`lean/docs/205.md`](../../../lean/docs/205.md) | 21 | the formalization scope note: the universal scope [S5:10], the Saxl scope [S5:12], the exclusion [S5:14], and the comparator table [S5:20–21] |
| S6 | [`lean/ComparatorChallenges/Saxl.lean`](../../../lean/ComparatorChallenges/Saxl.lean) | 119 | the Saxl comparator: the `SaxlConjecture` definition [S6:107–110], the `theorem saxl_conjecture` [S6:112] and the `sorry` [S6:113] |
| S7 | [`lean/OAI/RepresentationTheory/Saxl/Main.lean`](../../../lean/OAI/RepresentationTheory/Saxl/Main.lean) | 128 | the registered declaration in the OAI tree (38 files, 7558 lines, 0 sorry): the real `saxl_conjecture` proof [S7:88] via `saxl_of_cyclic_support` |
| S8 | [`lean/ComparatorChallenges/UniversalTensorSquares.lean`](../../../lean/ComparatorChallenges/UniversalTensorSquares.lean) | 110 | the universal tensor square comparator: the `theorem universal_tensor_square` [S8:91] and the `sorry` [S8:104] |
