[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 162](../index/combinatorics/162-counterexamples-to-rysers-covering-and-gyarfass-tree-cover-conjectures.md)

# 162 — Counterexamples to Ryser's covering and Gyárfás's tree-cover conjectures

[Index page](../index/combinatorics/162-counterexamples-to-rysers-covering-and-gyarfass-tree-cover-conjectures.md)

## Original CONTENTS.md summary

The release's blurb [S1:3845] and the catalog abstract [S2:407] state
the family's claim. It **disproves Ryser's covering conjecture** by
constructing intersecting $`(q+1)`$-partite, $`(q+1)`$-uniform
hypergraphs with covering number $`q+1`$ — not the predicted
bound $`q`$ — for every sufficiently large prime $`q`$. A separate
construction over extension fields also **disproves
Gyárfás's monochromatic tree-cover conjecture**. Two
manuscripts carry the family. The first, *Balanced counterexamples
to Ryser's conjecture at prime orders* [S3:35, S3:37], abstract


> For every sufficiently large prime $`q`$, we construct a finite intersecting
$`(q+1)`$-partite $`(q+1)`$-uniform hypergraph with covering number $`q+1`$
and exactly $`q+1`$ nonisolated vertices in each part. This disproves
Ryser's covering conjecture, even for intersecting hypergraphs with
equally sized parts. [S3:41–45]

The second, *A counterexample to Ryser's covering conjecture*
[S4:40, S4:42], abstract [S4:47–51]:

For every sufficiently large prime $`s\equiv2\pmod{3}`$ and every
sufficiently large odd integer $`n`$, with the threshold depending on
$`s`$, we construct an intersecting $`(s^n+1)`$-partite $`(s^n+1)`$-uniform
hypergraph with covering number $`s^n+1`$. This disproves Ryser's
covering conjecture in its intersecting case [S4:47–51].

## Undergraduate summary

A **hypergraph** is like a graph, but an "edge" may join any number
of vertices, not just two. An $`r`$-partite hypergraph splits its
vertices into $`r`$ labeled groups, with every edge touching each
group exactly once; $`r`$-uniform means every edge has exactly
$`r`$ vertices. A **vertex cover** is a set of vertices that meets
every edge, and the **covering number** $`\tau`$ is the size of the
smallest such set. The **matching number** $`\nu`$ is the size of the
largest set of pairwise edge-disjoint edges. Ryser's covering
conjecture says $`\tau\le(r-1)\nu`$ for an $`r`$-partite
hypergraph. When the hypergraph is *intersecting* (any two edges
share a vertex), $`\nu=1`$, so the bound collapses to
$`\tau\le r-1`$: a cover of size $`r-1`$ should always exist. This
family breaks that: for every large prime $`q`$ it builds an
intersecting $`(q+1)`$-partite hypergraph whose **smallest** cover has
size $`q+1`$, not $`q`$, with every part the same size
[S3:41–45, S5:10].

## Graduate summary

**The balanced counterexample** [S3:41–45, S5:10]. For every
sufficiently large prime $`q`$ there is a finite intersecting
$`(q+1)`$-partite, $`(q+1)`$-uniform hypergraph with covering number
$`q+1`$ and **exactly $`q+1`$ nonisolated vertices in each part**
— the parts are perfectly balanced, and the covering number is
$`r`$ rather than $`r-1`$. The prime threshold is existential
[S3:41–45, S5:10].

**The general rank form** [S4:47–51, S5:12]. The ranks occur
as $`r=p^n+1`$: one fixed prime $`p\equiv2\pmod3`$ works for all
sufficiently large prime degrees $`n`$, and a second construction
covers every sufficiently large such prime $`p`$ and every
sufficiently large odd $`n`$ (degree threshold depending on $`p`$).
Infinitely many ranks occur, and each gives a finite intersecting
$`r`$-partite $`r`$-uniform hypergraph with $`\nu=1`$ and
$`\tau=r`$, contradicting $`\tau\le(r-1)\nu`$
[S4:47–51, S5:12].

**The Gyárfás tree-cover consequence.** A separate
construction over extension fields also disproves
Gyárfás's monochromatic tree-cover conjecture
[S1:3845, S2:407].

**The scope of the formalization.** The two **registered**
declarations are the general $`r=p^n+1`$ rank form (the scope note's
second paragraph). The **balanced** equal-part-size form (the scope
note's first paragraph and the blurb's headline) is carried by the
`BalancedRyser` comparator, which has **no** `main_results` entry,
and the Gyárfás tree-cover consequence has **no
comparator at all** [S5:10, S5:12, S5:16–20].

## History of the conjecture

Ryser's covering conjecture (1960s) is a central problem in
extremal hypergraph theory, connecting the covering and matching
numbers of multipartite hypergraphs; the bound
$`\tau\le(r-1)\nu`$ is known for several special families, and the
intersecting case $`\tau\le r-1`$ was a key open question.
Gyárfás's monochromatic tree-cover conjecture is a
related extremal question about covering colored structures by
monochromatic trees. Both stood as expected-true for all
$`r`$; this family disproves both with **algebraic** constructions
rooted in finite fields and their extensions
[S3:41–45, S4:47–51, S5:10, S5:12].

**Prior (my training data, not this repo).** I know Ryser's
covering conjecture, the $`\tau\le(r-1)\nu`$ bound, and that the
intersecting case was a long-standing open problem. Concrete
counterexamples — at **every** sufficiently large prime order,
balanced across parts, with the rank form $`r=p^n+1`$ giving
infinitely many ranks, plus a tree-cover disproof over extension
fields — go beyond the specific constructions I recall; I
cannot independently verify the finite-field gadget / small-proper-
subfield argument in [S3, S4] from training alone.

## Consequences

**Ryser's covering conjecture is false, in the intersecting case.**
For every sufficiently large prime $`q`$ there is an intersecting
$`(q+1)`$-partite hypergraph with covering number $`q+1>q=(r-1)`$
[S3:41–45, S5:10].

**It fails even with equal part sizes.** The counterexample can be
taken with exactly $`q+1`$ nonisolated vertices in each part
[S3:41–45, S5:10].

**Infinitely many ranks.** Counterexamples occur at every rank
$`r=p^n+1`$ in the two registered families, so the failure is not an
isolated rank [S4:47–51, S5:12].

**Gyárfás's tree-cover conjecture is also false.** A
separate extension-field construction disproves it
[S1:3845, S2:407].

## Section skeleton

Two manuscripts. Manuscript 1 [S3:41–45] (title [S3:35], date [S3:37])
— `paper.tex` (354 lines) under `build/`, inputs the sections
`elementary`, `local`, `construction`, `candidates`, `selection`,
`deletion`, plus a figure macro and a `references` bibliography.
Manuscript 2 [S4] (title [S4:40], date [S4:42]) — `paper.tex`
(301 lines) under `build/`, inputs the sections `incidence`,
`construction`, `selection`, `linecover`, plus a figure macro and a
`references` bibliography. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S5:10, S5:12]. The first paragraph formalizes the
balanced claim: an intersecting $`(q+1)`$-partite, $`(q+1)`$-uniform
hypergraph with covering number $`q+1`$ and equal part sizes, for
every sufficiently large prime $`q`$ (the prime threshold
existential) [S5:10]. The second paragraph formalizes the general
rank form: finite intersecting $`r`$-partite $`r`$-uniform hypergraphs
with $`\nu=1`$ and $`\tau=r`$ at ranks $`r=p^n+1`$ — one fixed
prime $`p\equiv2\pmod3`$ for all large prime degrees $`n`$, and every
large such prime $`p`$ for every large odd $`n`$, infinitely many
ranks [S5:12]. The scope note names three comparators
[S5:16–20]: `BalancedRyser.lean`, `RyserCovering.lean`, and
`RyserOddExtensions.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 2` and `paps_form 1`. `formalization.yaml`
registers **two** `main_results` entries, both in the general rank
form and both manuscripts being in its `sources:` listing:
`OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank`
at `OAI/Combinatorics/Ryser/Construction/Main.lean`, and
`OAI.RyserOdd.eventualOddFailures_and_infinite` at
`OAI/Combinatorics/Ryser/OddExtensions.lean`. The two declarations
live in **two namespaces** (`OAI.RyserCoveringCounterexample` and
`OAI.RyserOdd`). The `BalancedRyser.lean` comparator (the balanced
head-line form) is a scope-note link but carries no `main_results`
entry, and the Gyárfás tree-cover consequence is not
named by any comparator
[S5:10, S5:12, S5:16–20].

**What the proofs do.** The registered
`exists_prime_eventually_counterexampleRank` states
$`\exists p,\ p.\mathrm{Prime}\wedge5<p\wedge p
\equiv2\ (3),\ \exists N\,\forall n\ge N\,(n.\mathrm{Prime}
\wedge2<n)\Rightarrow\mathrm{CounterexampleRank}(p^n+1)`$, and the
OAI tree proves it with a genuine Lean proof: it extracts a prime
good-gadget, builds a uniform ambient pool over the extension field
$`\mathbb F_{p^n}`$, verifies the small-proper-subfield condition, and
closes from the good-pool counterexample-rank lemma
[S9:14–17, S9:45]:

```lean
theorem exists_prime_eventually_counterexampleRank :
    ∃ p : ℕ, p.Prime ∧ 5 < p ∧ p % 3 = 2 ∧
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Prime → 2 < n →
        CounterexampleRank (p ^ n + 1) := by
```
[S9:14–17]

The proof is not a `sorry`: it discharges the goal with
`simpa only [extensionField_card p n hn.ne_zero] using hr`
[S9:45]. The second registered declaration
`eventualOddFailures_and_infinite` states the eventual odd-degree
failure together with the infinitude of the failing ranks, and the
OAI tree proves it by assembling the eventual-explicit-failures
witness with the infinite-ranks set, closing via
`infiniteRanks.mono` and
`explicitFailureAt_of_counterexampleRank`
[S10:132–140].

**What the OAI tree does carry.** The
`OAI/Combinatorics/Ryser` package (221 files over 27,012 lines,
zero `sorry`) carries the supporting definitions (`Hypergraph`,
`RPartiteUniform`, `Intersecting`, `coverNumber`, `matchingNumber`,
`CounterexampleRank`, the `Incidence` small-proper-subfield
machinery, the `ExtensionField` construction,
`counterexampleRank_of_goodAmbientPool`) that both registered
theorems assemble [S9:45, S10:132–140].

**The comparator stubs.** The registered `RyserCovering.lean`
comparator restates
`exists_prime_eventually_counterexampleRank` with a bare `sorry`
body 

```lean
theorem exists_prime_eventually_counterexampleRank :
    ∃ p : ℕ, p.Prime ∧ 5 < p ∧ p % 3 = 2 ∧
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Prime → 2 < n →
        CounterexampleRank (p ^ n + 1) := by
  sorry
```
[S6:49–53]

The registered `RyserOddExtensions.lean` comparator restates
`eventualOddFailures_and_infinite` with a bare `sorry`
[S7:61–68], and the unregistered `BalancedRyser.lean`
comparator restates the balanced `main_result`
— $`\exists q_0\,\forall q\ge q_0\,(q.\mathrm{Prime}
\Rightarrow\mathrm{BalancedCounterexample}\ q)`$ — with a
bare `sorry` [S8:39–40]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; the
comparators' `sorry` bodies are the targets the release set itself,
and the proved versions in the OAI tree are the registered results.

**Tree measurement (source-level).**

The family registers 2 `main_results` declarations (`OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank`; `OAI.RyserOdd.eventualOddFailures_and_infinite`); the primary file `OAI/Combinatorics/Ryser/Construction/Main.lean` carries 57 lines with top-level theorem `theorem exists_prime_eventually_counterexampleRank`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 62 files, 370 theorems, 117 defs.

The preprint states 35 theorem environments; the tree carries 11× as many (source-level count, not a proof-quality ratio).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 162 at [S1:3845] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{162} at [S2:407] |
| S3 | [`preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/build/paper.tex`](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/build/paper.tex) | 354 | manuscript 1 (balanced): title [S3:35], date [S3:37], abstract [S3:41–45] |
| S4 | [`preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/build/paper.tex`](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/build/paper.tex) | 301 | manuscript 2 (original): title [S4:40], date [S4:42], abstract [S4:47–51] |
| S5 | [`lean/docs/162.md`](../../../lean/docs/162.md) | 20 | the formalization scope note: the balanced scope paragraph [S5:10], the rank-form paragraph [S5:12], and the comparator table [S5:16–20] |
| S6 | [`lean/ComparatorChallenges/RyserCovering.lean`](../../../lean/ComparatorChallenges/RyserCovering.lean) | 59 | registered comparator (fixed prime): the `exists_prime_eventually_counterexampleRank` theorem [S6:49–52] and the `sorry` [S6:53] |
| S7 | [`lean/ComparatorChallenges/RyserOddExtensions.lean`](../../../lean/ComparatorChallenges/RyserOddExtensions.lean) | 74 | registered comparator (odd extensions): the `eventualOddFailures_and_infinite` theorem [S7:61–68] and the `sorry` [S7:68] |
| S8 | [`lean/ComparatorChallenges/BalancedRyser.lean`](../../../lean/ComparatorChallenges/BalancedRyser.lean) | 44 | unregistered comparator (balanced): the `main_result` theorem [S8:39] and the `sorry` [S8:40] |
| S9 | [`lean/OAI/Combinatorics/Ryser/Construction/Main.lean`](../../../lean/OAI/Combinatorics/Ryser/Construction/Main.lean) | 57 | the registered declaration in the OAI tree: the real proof of `exists_prime_eventually_counterexampleRank`, the statement [S9:14–17] and the closing tactic [S9:45] |
| S10 | [`lean/OAI/Combinatorics/Ryser/OddExtensions.lean`](../../../lean/OAI/Combinatorics/Ryser/OddExtensions.lean) | 153 | the registered declaration in the OAI tree: the real proof of `eventualOddFailures_and_infinite` [S10:132–140] |
