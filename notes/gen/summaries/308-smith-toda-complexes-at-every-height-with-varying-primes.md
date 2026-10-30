[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 308](../index/topology/308-smith-toda-complexes-at-every-height-with-varying-primes.md)

# 308 — Smith–Toda complexes at every height with varying primes

[Index page](../index/topology/308-smith-toda-complexes-at-every-height-with-varying-primes.md)

## Original CONTENTS.md summary

[S1:7612] (family entry):

> **308. Finite Smith–Toda complexes at every height.** For every <i>n</i> ≥ 0, constructs a finite Smith–Toda spectrum at a prime <i>p</i> depending on <i>n</i>, with Brown–Peterson homology $`BP_*/(p,v_1,\ldots,v_n)`$ and the canonical comodule structure. Thus Smith–Toda complexes exist at every height when the prime may vary; an explicit example realizes $`V(4)`$ at <i>p</i> = 1009.

[S2:712] carries the `\resultentry` with both manuscripts [S3:3, S3:5, S4:3, S4:5]. The two abstracts:

> For every nonnegative integer $`n`$, we construct a Smith–Toda complex
$`V(n)`$ at some prime $`p`$ depending on $`n`$. It is a finite $`p`$-local
spectrum whose Brown–Peterson homology is
$`\mathrm{BP}_*/(p,v_1,\ldots,v_n)`$ with its canonical comodule structure and
generator in degree zero. Each listed generator is killed to its first
power. [S3:8–15]

> We construct a Smith–Toda complex $`V(4)`$ at the prime $`1009`$. It is an
ordinary finite $`1009`$-local spectrum whose Brown–Peterson homology is
$`BP_*/(1009,v_1,v_2,v_3,v_4)`$, with its canonical comodule structure and
generator in degree zero. [S4:8–13]

## Undergraduate summary

A **Smith–Toda complex** $`V(n)`$ is a special kind of spectrum — think of a
spectrum as a long, structured list of spaces used to measure
(co)homology. A Smith–Toda complex of **height** $`n`$ is one whose
**Brown–Peterson homology** ($`BP_*`$, an algebra that encodes
complex-orientation data) is exactly $`p, v_1, \ldots, v_n`$-quotiented: the
first $`n+1`$ "periodicity operators" all act trivially, and the next one
does not.

The classical construction works for small heights at a *fixed* prime.
This family answers the open question of what happens at **every** height.
Manuscript 1 [S3:8–15] shows that a finite Smith–Toda complex $`V(n)`$
exists for every $`n \ge 0`$, provided the **prime may depend on** $`n`$ — at
each height there is some prime $`p`$ (growing with $`n`$) where the complex
lives. Manuscript 2 [S4:8–13] gives the explicit concrete example: a
finite $`V(4)`$ at the specific prime $`1009`$.

## Graduate summary

**Varying-prime existence (Manuscript 1)** [S3:8–15, S2:712].
For every nonnegative integer $`n`$ there exists a prime $`p = p(n)`$ and a
finite $`p`$-local spectrum $`V(n)`$ whose Brown–Peterson homology is
$`BP_*/(p, v_1, \ldots, v_n)`$ with its canonical comodule structure and
generator in degree zero. Each $`v_i`$ for $`0 \le i \le n`$ is killed to its
first power. The prime is not fixed: it is allowed to grow with $`n`$, and is
what makes the construction available at arbitrarily high heights.

**The explicit $`V(4)`$ at $`1009`$ (Manuscript 2)** [S4:8–13, S2:712].
There is an ordinary finite $`1009`$-local spectrum $`V(4)`$ whose
Brown–Peterson homology is $`BP_*/(1009, v_1, v_2, v_3, v_4)`$, with its
canonical comodule structure and generator in degree zero. This is a
specific, named instance of the general construction at height $`4`$.

**What the prime-varying hypothesis buys.** The classical
Smith–Toda complexes are known in low heights at a fixed prime, and the
obstruction to carrying them to higher heights at a *single* prime is the
content of the long-standing height problem. Allowing the prime to depend
on $`n`$ is exactly the weakening that makes every height attainable
[S2:712]: the explicit $`V(4)`$ at $`1009`$ is the release's witness that the
scheme reaches the fourth height.

## History of the conjecture

The Smith–Toda complexes $`V(n)`$ were introduced as finite spectra of
increasing chromatic height, central to the chromatic structure of the
stable homotopy category. Their existence at low heights at a fixed
prime is classical; the open question is whether they exist at every
height. The answer here is conditional on the prime: fixing a single
prime is not required, and letting the prime vary with the height
recovers existence in full [S3:8–15, S2:712].

The explicit construction of $`V(4)`$ at the specific prime $`1009`$
[S4:8–13] is a concrete witness that the scheme reaches the fourth
height. Choosing a large prime for a given height is a standard move in
the arithmetic of generalized cohomology theories: the required
$`BP_*`$-algebra structures are easier to realize when the prime has room
to accommodate the relations the complex must satisfy.

**Prior (my training data, not this repo).** Smith–Toda complexes and
their role in the chromatic splitting of the stable homotopy category
are well established. The existence of finite Smith–Toda complexes at
every height with the prime allowed to vary, and the explicit
construction of $`V(4)`$ at the prime $`1009`$, are the novel contributions
claimed here; I cannot verify the chromatic $`BP_*`$-algebra
constructions independently from training alone.

## Consequences

- **Smith–Toda complexes exist at every height when the prime may vary**
  [S3:8–15, S2:712]: for each $`n \ge 0`$ there is a prime $`p = p(n)`$ and a
  finite $`p`$-local spectrum with Brown–Peterson homology
  $`BP_*/(p, v_1, \ldots, v_n)`$.
- **An explicit $`V(4)`$ is realized at the prime $`1009`$** [S4:8–13,
  S2:712]: a finite $`1009`$-local spectrum with Brown–Peterson homology
  $`BP_*/(1009, v_1, v_2, v_3, v_4)`$.
- **Each generator is killed to its first power** [S3:14–15]: the
  first $`n+1`$ chromological generators act trivially, matching the
  classical Smith–Toda definition at the chosen prime.
- **The construction is finite and $`p`$-local** [S3:9–10]: the
  resulting spectra are finite in the strong sense required of chromatic
  test objects, and live at the chosen prime.

## Section skeleton

Two manuscripts. Manuscript 1 [S3:8–15]: root `build/main.tex` (28 lines),
sections under `build/sections/` (`00-introduction` through
`08-realization`). Manuscript 2 [S4:8–13]: root `build/main.tex`
(27 lines), sections under `build/sections/` (`00-introduction`,
`01-framework`, `02a-cobar-preliminaries`, `02-lower-complexes`,
`03-may-and-first-obstruction`, `04-frobenius-elimination`,
`05-final-obstruction`, plus an appendix `appendix-resolution`). No
verification bundle.

## Comparison with the formalized statement

This family is **not formalized**. It sits at tier **T0** in the ledger
[S5]: no scope note, no comparator stub, no `main_results` entry, no
proved OAI tree. The T0 shape is "no formalization at all in the
release."

The absence is part of the coverage skew the ledger records: the
topological and chromatic families in the catalog are the thinnest
formalized, and a Smith–Toda construction at a varying prime is of just
this kind. The reading of the two manuscripts above is of source text
only.

## Coverage

The ledger row `fam=308` [S5] records the tier and the counts:
`tier=T0`, `paps=2`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `scope_chars=0`, `verification=0`, `trace=`. The T0
shape is "no formalization at all." The shape flag is
`shapes=uniform`, and `resolves_named=0`, `counterex_broad=0`,
`covmd=0` — no named resolution, no counterexample flag, no coverage
document. This is a construction/existence family with no formalization
record in the release.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7612] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 308 at [S2:712] |
| S3 | [`preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/build/main.tex`](../../../preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/build/main.tex) | 28 | manuscript 1 (varying primes); title [S3:3], date [S3:5], abstract [S3:8–15] |
| S4 | [`preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/build/main.tex`](../../../preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/build/main.tex) | 27 | manuscript 2 ($V(4)$ at $1009$); title [S4:3], date [S4:5], abstract [S4:8–13] |
| S5 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=308`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
