[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 297](../index/operator-algebras/297-a-zfc-counterexample-to-naimarks-problem.md)

# 297 — A ZFC counterexample to Naimark's problem

[Index page](../index/operator-algebras/297-a-zfc-counterexample-to-naimarks-problem.md)

## Original CONTENTS.md summary

[S1:7391] (family entry):

> **297. A ZFC counterexample to Naimark's problem.** Gives an alternative to Tanaka's ZFC construction of a unital infinite-dimensional simple complex *C*∗-algebra with a faithful tracial state and exactly one nonzero irreducible representation up to unitary equivalence. Thus the unrestricted compact-operator characterization fails without additional set-theoretic assumptions; the counterexample is nonseparable. ([Lean](../../../lean/docs/297.md))

[S2:688] carries the `\resultentry` with the single manuscript [S3:26, S3:28]. The abstract 

> We construct in ZFC a unital infinite-dimensional simple complex
$`C^*`$-algebra with a faithful tracial state whose nonzero irreducible
representations are all unitarily equivalent. This gives a negative answer
to Naimark's problem without additional set-theoretic assumptions. [S3:31–36]

## Undergraduate summary

**Naimark's problem** asks a precise question about $`C^*`$-algebras: if all
the nonzero irreducible representations of a $`C^*`$-algebra are
unitarily equivalent to one another, must the algebra be the **compact
operators** on a Hilbert space? The intuition is that "only one
irreducible representation up to equivalence" should single out the
compact algebra.

The answer is **no**, and this paper [S3:31–36] gives the counterexample
in **ZFC** — ordinary set theory, with no extra axioms like the
Continuum Hypothesis. The construction is a unital, infinite-dimensional,
**simple** (no nontrivial ideals) $`C^*`$-algebra that carries a faithful
tracial state and whose nonzero irreducible representations are all
unitarily equivalent — yet it is not the compact operators on any Hilbert
space. The counterexample is **nonseparable** [S1:7391].

## Graduate summary

**Main theorem** [S3:31–36, S2:688].
There exists a unital, infinite-dimensional, simple complex $`C^*`$-algebra
$`A`$ with a faithful tracial state $`\tau`$ such that every nonzero
irreducible representation of $`A`$ is unitarily equivalent to every other.
In particular $`A \not\cong \mathcal{K}(H)`$ for any Hilbert space $`H`$. The
construction is in ZFC; no additional set-theoretic hypothesis is used
[S4:9].

**Why this refutes Naimark.** Naimark's problem predicts that the
unitary-equivalence uniqueness of the nonzero irreducibles forces
$`A \cong \mathcal{K}(H)`$. The constructed $`A`$ satisfies the premise
(all nonzero irreducibles unitarily equivalent) and falsifies the
conclusion (not isomorphic to the compacts) [S4:9]. The faithful tracial
state and simplicity are part of the counterexample's strength: the
algebra is not merely non-compact, it is a simple tracial algebra.

**The ZFC point.** Earlier counterexamples to related characterizations
required additional set-theoretic assumptions. The release's framing
[S2:688] positions this as an alternative to a prior ZFC construction,
giving the counterexample in the base theory [S4:9].

## History of the conjecture

Naimark's problem is a classical question in the representation theory of
$`C^*`$-algebras, named after Marc Naimark. It asks whether a
$`C^*`$-algebra determined up to representation by a single irreducible
class must be the compact operators. The problem sits at the intersection
of the structure theory of simple $`C^*`$-algebras and the role of set
theory in their classification.

The construction of the counterexample uses a direct-limit /
HNN-extension type argument visible in the section skeleton
(`construction`, `hnn`, `iteration`, `states`). The faithful tracial
state is produced alongside the algebra; the simplicity and the
irreducible-representation uniqueness follow from the
construction [S4:9].

**Prior (my training data, not this repo).** Naimark's problem is a
long-standing open problem in $`C^*`$-algebra theory. Simple
infinite-dimensional $`C^*`$-algebras with a faithful trace (often called
"stably finite simple" algebras) are well studied; a counterexample in
ZFC to the compact-operator characterization is the novel contribution
claimed here. I cannot verify the direct-limit / HNN constructions
independently from training alone.

## Consequences

- **Naimark's problem is answered negatively in ZFC** [S3:31–36, S2:688]:
  a unital infinite-dimensional simple $`C^*`$-algebra with a faithful
  tracial state can have all nonzero irreducible representations
  unitarily equivalent without being the compact operators. This is the
  named counterexample the ledger's `resolves_named` and
  `counterex_broad` flags record.
- **The unrestricted compact-operator characterization fails** [S4:9]:
  the premise of Naimark's problem (unique irreducible class) does not
  force the compact-operator conclusion without additional
  set-theoretic assumptions.
- **A nonseparable counterexample** [S1:7391]: the constructed algebra
  is nonseparable, marking the boundary of the separable structure
  theory.

## Section skeleton

One manuscript [S3:31–36]. Root `build/main.tex` (49 lines), abstract in the
root [S3:31–36]. Sections under `build/sections/`: `introduction`,
`construction`, `hnn`, `iteration`, `states`, `bridge`, plus a
`references.bib`. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note [S4:9]
and one comparator stub [S5]. There is **no** `main_results` entry, and
no proved OAI tree. The T2 shape is "scope note and comparator stubs
exist, but no `main_results` entry and no proved OAI tree."

The scope note [S4:9] selects the ZFC counterexample: a unital
infinite-dimensional simple complex $`C^*`$-algebra with a faithful tracial
state whose nonzero irreducible representations are all unitarily
equivalent, and which is not isomorphic to the compact operators on any
Hilbert space, with no additional set-theoretic assumption used [S4:9].

The single comparator stub carries 1 `sorry`: `Naimark.lean` (57 lines)
with `theorem main` at [S5:44] and the `sorry` at [S5:51]. The statement
the release set for the comparator is the Naimark counterexample itself;
no proved copy exists under `lean/OAI/`. The reading is of source text
only.

## Coverage

The ledger row `fam=297` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=474`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub exist, with no `main_results`
entry." The single comparator stub carries 1 `sorry`. The shape flags are
`shapes=counterexample|classification`, `counterex_broad=1`,
`resolves_named=1` — this is a counterexample family resolving
Naimark's problem.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7391] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 297 at [S2:688] |
| S3 | [`preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/build/main.tex`](../../../preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/build/main.tex) | 49 | manuscript (root); title [S3:26], date [S3:28], abstract [S3:31–36] |
| S4 | [`lean/docs/297.md`](../../../lean/docs/297.md) | 15 | scope note — Scope at [S4:9] and the comparator link `Naimark.lean` |
| S5 | [`lean/ComparatorChallenges/Naimark.lean`](../../../lean/ComparatorChallenges/Naimark.lean) | 57 | comparator stub — 57 lines, 1 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=297`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
