[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 295](../index/operator-algebras/295-kadison-ringrose-cohomology-conjecture.md)

# 295 — The Kadison–Ringrose cohomology conjecture

[Index page](../index/operator-algebras/295-kadison-ringrose-cohomology-conjecture.md)

## Original CONTENTS.md summary

[S1:7359] (family entry):

> **295. The Kadison–Ringrose cohomology conjecture.** Proves that every bounded Hochschild cocycle of degree at least two on a complex von Neumann algebra, with coefficients in the algebra itself, has a bounded primitive. Equivalently, all higher bounded Hochschild cohomology groups vanish, resolving the Kadison–Ringrose conjecture. ([Lean](../../../lean/docs/295.md))

[S2:684] carries the `\resultentry` with the single manuscript [S3:40, S3:42]. The abstract 

> We prove that every bounded Hochschild cocycle of degree at least two
on a complex von Neumann algebra, with values in the algebra itself,
has a bounded primitive. Together with the established degree-one
inner-derivation theorem, this resolves the Kadison–Ringrose cohomology
conjecture positively. [S3:45–51]

## Undergraduate summary

**Hochschild cohomology** measures how far an algebra's multiplication
deviates from being "too rigid". A **cocycle** of degree $`n`$ is a multilinear
map that nearly commutes with the algebra's associator; a cocycle that is
the **differential** of a cochain one degree lower is called a **coboundary**,
and only the cocycles that are not coboundaries survive in cohomology.

The **bounded** version keeps only cocycles and primitives that are
bounded as operators, which is the setting relevant to von Neumann algebras
(weakly closed operator algebras on Hilbert space).

The **Kadison–Ringrose cohomology conjecture** asked whether the higher
bounded Hochschild cohomology groups of a von Neumann algebra vanish —
that is, whether every bounded cocycle of degree at least two admits a
bounded primitive. The answer is **yes** [S3:45–51].

Together with the degree-one statement — that every bounded derivation on
a von Neumann algebra is inner — this resolves the Kadison–Ringrose
conjecture in full. The proof imposes no separability or type restriction
[S4:9]: it holds for every complex von Neumann algebra, with coefficients
in the algebra itself.

## Graduate summary

**Main theorem** [S3:45–51, S2:684].
Let $`\\mathcal{M}`$ be a complex von Neumann algebra. For every degree
$`n \\ge 2`$, the bounded Hochschild cohomology group
$`H^n_{\\mathrm{b}}(\\mathcal{M}, \\mathcal{M})`$ vanishes: every bounded
multilinear $`n`$-cocycle
$`\\varphi : \\mathcal{M}^n \\to \\mathcal{M}`$ is the Hochschild
differential of a bounded $`(n-1)`$-cochain. Equivalently, every such
cocycle has a bounded primitive. No separability or type restriction is
imposed [S4:9].

**The degree-one half.** The established inner-derivation theorem
[S3:48–49] says that every bounded derivation
$`\\delta : \\mathcal{M} \\to \\mathcal{M}`$ is inner: there is
$`x \\in \\mathcal{M}`$ with
$`\\delta(a) = xa - ax`$ for all $`a`$. Together the two halves give the full
Kadison–Ringrose resolution [S3:45–51].

**Scope note.** The formalization selects the degree-at-least-two
vanishing statement only; the degree-one inner-derivation theorem is
explicitly outside the selected statement [S4:9].

## History of the conjecture

The Kadison–Ringrose conjecture is a long-standing problem in the
cohomology of von Neumann algebras, named after Richard Kadison and
Joel Ringrose. It asks whether the higher bounded Hochschild cohomology
groups of a (complex) von Neumann algebra with coefficients in itself
vanish. The degree-one case — bounded derivations are inner — is the
classical Sakai–Singer-type inner-derivation theorem for von Neumann
algebras, and the higher-degree vanishing was the open half.

The proof in this paper [S3:45–51] uses a three-step argument visible in
the section skeleton: a walk estimate, a Liouville-type rigidity step,
and a final cohomological conclusion. The formalization [S4:9] records
the higher-degree vanishing as its selected statement, with the
degree-one half cited as established context.

**Prior (my training data, not this repo).** Kadison's and Ringrose's
cohomology problem for von Neumann algebras is a classical open problem
in operator algebras, sitting next to the inner-derivation theorem and
to the bounded cohomology of $`C^*`$-algebras. The full positive resolution
for the higher bounded groups on arbitrary complex von Neumann algebras
is the novel contribution claimed here; I cannot verify the
Liouville/rigidity arguments independently from training alone.

## Consequences

- **The Kadison–Ringrose cohomology conjecture is resolved positively**
  [S3:45–51, S2:684]: the higher bounded Hochschild cohomology groups of
  every complex von Neumann algebra with coefficients in itself vanish.
  This is the named resolution the ledger's `resolves_named` flag records.
- **Bounded primitives exist in every degree at least two** [S3:45–51,
  S4:9]: every bounded multilinear cocycle of degree $`n \\ge 2`$ is the
  Hochschild differential of a bounded $`(n-1)`$-cochain.
- **No separability or type restriction** [S4:9]: the vanishing holds for
  every complex von Neumann algebra — type I, II, III, nonseparable
  included — with coefficients in the algebra itself.
- **The bounded cohomology of a von Neumann algebra is concentrated in
  degree one** [S3:45–51, S4:9]: the only survivor of the bounded
  Hochschild complex, once the inner-derivation theorem is included, is
  the degree-one group of inner derivations.

## Section skeleton

One manuscript [S3:45–51]. Root `build/paper.tex` (61 lines), abstract in the
root [S3:45–51]. Sections under `build/sections/`: `01-introduction`,
`02-walk`, `03-liouville`, `04-rigidity`, `05-cohomology`, plus a
`references` file. No verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note [S4:9]
and one comparator stub [S5]. There is **no** `main_results` entry, and
no proved OAI tree. The T2 shape is "scope note and comparator stubs
exist, but no `main_results` entry and no proved OAI tree."

The scope note [S4:9] selects the degree-at-least-two vanishing
statement: every bounded multilinear $`n`$-cocycle on a complex von
Neumann algebra, $`n \\ge 2`$, is the Hochschild differential of a bounded
$`(n-1)`$-cochain. The degree-one inner-derivation theorem is explicitly
outside the selected statement [S4:9].

The single comparator stub carries 1 `sorry`: `KadisonRingrose.lean`
(43 lines) with `theorem main_result` at [S5:30] and the `sorry` at
[S5:36]. The statement the release set for the comparator is the
cohomological vanishing itself; no proved copy exists under
`lean/OAI/`. The reading is of source text only.

## Coverage

The ledger row `fam=295` [S6] records the tier and the counts:
`tier=T2`, `paps=1`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=416`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub exist, with no `main_results`
entry." The single comparator stub carries 1 `sorry`. The shape flags
are `shapes=resolution|bound`, `resolves_named=1` — this is a
resolution family resolving the Kadison–Ringrose cohomology conjecture.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7359] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 295 at [S2:684] |
| S3 | [`preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/build/paper.tex`](../../../preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/build/paper.tex) | 61 | manuscript (root); title [S3:40], date [S3:42], abstract [S3:45–51] |
| S4 | [`lean/docs/295.md`](../../../lean/docs/295.md) | 15 | scope note — Scope at [S4:9] and the comparator link `KadisonRingrose.lean` |
| S5 | [`lean/ComparatorChallenges/KadisonRingrose.lean`](../../../lean/ComparatorChallenges/KadisonRingrose.lean) | 43 | comparator stub — 43 lines, 1 `sorry` |
| S6 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=295`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
