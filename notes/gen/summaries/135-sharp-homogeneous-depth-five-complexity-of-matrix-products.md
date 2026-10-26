[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 135](../index/theoretical-computer-science/135-sharp-homogeneous-depth-five-complexity-of-matrix-products.md)

# 135 — Sharp homogeneous depth-five complexity of matrix products

[Index page](../index/theoretical-computer-science/135-sharp-homogeneous-depth-five-complexity-of-matrix-products.md)

## Original CONTENTS.md summary

[S1:3261] (family entry):

> **135. Homogeneous depth-five lower bounds for iterated matrix multiplication.** Over every characteristic-zero field, the $`(1,1)`$ entry of a product of n independent $`n\times n`$ variable matrices requires $`n^{\Theta(\sqrt n)}`$ gates in homogeneous depth-five sum–product circuits. This sharp bound allows shared gates and bottom linear forms involving all variables. ([Lean](lean/docs/135.md))

[S2:347] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Iterated matrix multiplication** ($\mathrm{IMM}_{n,n}$) is a
polynomial: take $n$ matrices, each filled with distinct variables,
multiply them in a row, and read off the $(1,1)$ corner entry. Expanding
the product, that entry is a sum of many terms, each term a path of
length $n-1$ through the matrix indices.

An **arithmetic circuit** computes a polynomial using addition and
multiplication gates. Restricting how deep the circuit is (how many
layers of gates) makes it harder to compute hard polynomials — and
proving that hardness is a central goal of complexity theory.

A **depth-five** circuit has five layers (+, ×, +, ×, + from the
output down). **Homogeneous** means every monomial reaching a gate has
the same degree, which is a natural restriction for a degree-$n$
polynomial like $\mathrm{IMM}_{n,n}$.

This family shows that, over any characteristic-zero field, every
homogeneous depth-five circuit computing $\mathrm{IMM}_{n,n}$ needs
**at least $n^{\sqrt n/400}$ gates** [S4:53–63] — a genuinely
superpolynomial number. Combined with an upper bound of
$n^{\sqrt n+4}$ gates [S6:11], this pins the depth-five gate complexity
to **$n^{\Theta(\sqrt n)}$**: a sharp, two-sided bound.

## Graduate summary

**Main theorem** ([S4:53–63], `thm:main`). "There exist absolute
constants $c>0$ and $n_0$ such that, for every integer $n\geq n_0$,
every syntactically homogeneous $\Sigma\Pi\Sigma\Pi\Sigma$ circuit over
$\mathbb C$ computing $\mathrm{IMM}_{n,n}$ has size at least $n^{c\sqrt n}$. One may
take $c=1/400$" [S4:53–63].

**The circuit model is permissive.** The lower bound allows
unrestricted bottom fan-in and support, scalar constants, and shared
subcircuits [S4:65–66]. A gate may occur repeatedly among another
gate's inputs, and repeated occurrences at a product gate are counted
with multiplicity [S4:25–27]. The lower bound is on the number of gates
(vertices, including leaves), which the analysis also bounds for
computational gates alone [S4:47–51].

**Characteristic-zero extension.** Corollary
\ref{cor:characteristic-zero} extends the $n^{\sqrt n/400}$ lower bound
from $\mathbb C$ to *every* field of characteristic zero, with the same
absolute threshold [S4:66–68].

**Matching upper bound.** Proposition \ref{prop:upper} gives an
elementary block construction of size at most $n^{\sqrt n+4}$ over
*every* field for $n\geq2$ [S4:68–71]. The construction is homogeneous
of depth four; inserting unary bottom sums makes it depth five, so the
lower and upper bounds have the matching scale.

**Unrestricted depth is polynomial.** Iterated matrix multiplication
has polynomial-size circuits when depth is unrestricted [S4:72–73] —
the hardness comes specifically from the depth-five restriction.

## History of the conjecture

**Iterated matrix multiplication** has long served as a test of the
cost of restricting arithmetic depth: its path expansion connects
matrix products with reachability, while its polynomial-size
unrestricted circuits make it a natural target for shallow-circuit
lower bounds [S4:77–80].

**Nisan and Wigderson** (1995) used dimensions of partial-derivative
spaces to prove lower bounds for homogeneous depth-three circuits and
for constant-depth set-multilinear circuits, and they asked for an
explicit homogeneous polynomial requiring superpolynomial size at
constant depth, even at depth five [S4:81–85].

**Depth reduction** sharpened the motivation: **Agrawal and Vinay**
reduced general arithmetic computation to depth four, and
**Koiran** and **Tavenas** sharpened the size bounds [S4:88–90]. For
degree $d=N^{O(1)}$, Tavenas's theorem converts a size-$N^{O(1)}$
circuit computing a homogeneous degree-$d$ polynomial into a
homogeneous depth-four circuit of size $N^{O(\sqrt d)}$
[S4:91–95] — this is the origin of the **square-root scale** in
depth-four lower bounds and in the block construction for IMM used
here.

The approach to that scale passed through several restrictions.
**Fournier, Limaye, Malod, and Srinivasan** (2015) proved IMM lower
bounds with bounded product-layer fan-ins, and for homogeneous
multilinear formulas [S4:99–102]. **Kayal, Limaye, Saha, and
Srinivasan** (2014) removed the bottom-fan-in restriction, obtaining an
exponential lower bound over characteristic zero for a Nisan–Wigderson
design family [S4:103–106]. **Kumar and Saraf** (2014) proved a
$d^{\Omega(\sqrt d)}$ lower bound for homogeneous depth-four circuits
computing $\mathrm{IMM}_{d^5,d}$ over every field [S4:107–109]; and
**Kayal, Saha, and Tavenas** (2018) obtained $w^{\Omega(\sqrt d)}$ for
syntactically multilinear depth-four circuits computing $\mathrm{IMM}_{w,d}$,
without homogeneity [S4:110–114].

At **depth five**, **Bera and Chakrabarti** (2015) proved a lower bound
with a restriction on bottom support [S4:116–123]. **Kumar and
Saptharishi** (2017) proved $\exp(\Omega_q(\sqrt d))$ lower bounds for
homogeneous depth-five circuits without a bottom-support restriction,
but over a *finite* field and for Nisan–Wigderson designs rather than
IMM [S4:131–137]. **Limaye, Srinivasan, and Tavenas** (2021) established
superpolynomial lower bounds for unrestricted-bottom depth-five
circuits over characteristic zero [S4:146–149].

The theorem here differs from the earlier depth-five results in that it
is for $\mathrm{IMM}_{n,n}$ at the square width–degree regime $w=d=n$, over
every characteristic-zero field, with no bottom-support restriction,
and gives the sharp $n^{\sqrt n/400}$ scale [S4:128–129][S4:156–158].

**Prior (my training data, not this repo).** IMM as a hard polynomial,
the partial-derivative-space method of Nisan–Wigderson, and the
Agrawal–Vinay/Koiran–Tavenas depth reductions are standard in algebraic
complexity. The square-root scale and the finite-field exponential
bounds for NW designs are well-established. The specific sharp
$n^{\Theta(\sqrt n)}$ two-sided bound for IMM at depth five over
characteristic-zero fields with a fully permissive circuit model is the
load-bearing claim of the release; I cannot independently confirm the
exact exponent $1/400$ as a prior result, and the release ships the
manuscript as proof.

## Consequences

- **A sharp depth-five lower bound for IMM.** Every homogeneous
  depth-five circuit over a characteristic-zero field computing
  $\mathrm{IMM}_{n,n}$ needs at least $n^{\sqrt n/400}$ gates
  [S4:53–63][S6:9].
- **A matching upper bound.** Over every field, a block construction
  computes $\mathrm{IMM}_{n,n}$ with at most $n^{\sqrt n+4}$ gates for
  $n\ge2$ [S6:11].
- **Sharp gate complexity.** The two-sided bound pins the homogeneous
  depth-five gate complexity to $n^{\Theta(\sqrt n)}$ [S1:3261].
- **The model is fully permissive.** Shared gates, constants, and
  bottom linear forms of arbitrary support are all allowed, so the
  hardness is not an artifact of an artificial restriction [S4:65–66].
- **The threshold is field-independent.** The absolute threshold does
  not depend on the characteristic-zero field [S6:9].
- **Unrestricted depth remains polynomial.** The hardness is specific
  to the depth-five restriction; with unrestricted depth IMM has
  polynomial-size circuits [S4:72–73].

## Section skeleton

The manuscript [S3] is a 42-line root: a preamble with a `macros` import
[S3:14], title, abstract [S3:21–32], and six section files [S3:34–39].
The sections, in order and line count: `01-introduction` (243),
`02-rank` (150), `03-circuits` (300), `04-moments` (391), `05-paths`
(204), `06-completion` (132) — 1,420 section lines. The proof develops
the rank/moment machinery for the path expansion, analyzes the circuit
layers, translates the moment bounds into gate counts along the paths,
and completes the lower bound with the matching block-construction
upper bound. The shipped PDF [S5] is the manuscript in the form the
release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note [S6:9]
and **one** comparator stub, but **no** `main_results` declaration. This
is a structural absence: the scope note links a comparator config, and
that config has no proved declaration in `lean/OAI/`.

The scope note [S6:9] states precisely what is formalized, in two
paragraphs:

- **The lower bound** [S6:9]: "The formalization proves that, over
  every characteristic-zero field, syntactically homogeneous
  depth-five $\Sigma\Pi\Sigma\Pi\Sigma$ circuits computing this
  polynomial require at least $n^{\sqrt n/400}$ gates for all
  sufficiently large $n$, with a threshold independent of the field.
  Arbitrary bottom support, finite fan-in and fan-out, and sharing are
  allowed."
- **The upper bound** [S6:11]: "It also gives, over every field and for
  $n\ge2$, circuits with at most $n^{\sqrt n+4}$ gates. These are the
  lower and upper bounds selected from the paper."

The scope note links a single comparator config [`DepthFive.lean`]
[S6:17]. That config has **no** `main_results` entry, so the
formalization stops at the challenge stub.

The `DepthFive.lean` comparator stub [S7:118–130] (136 lines) defines the
depth-five circuit machinery — `Depth5Circuit`, `circuitValue`,
`circuitSize`, `upperGateBound`, and the `imm` polynomial — inside the
namespace `Problem335`, and carries one statement, a single
conjunction of three clauses [S7:118–130]:

- `main` [S7:118–130] — (i) over $\mathbb C$, some threshold beyond which
  every depth-five circuit computing $\mathrm{IMM}$ needs
  $n^{\sqrt n/400}$ gates; (ii) the same bound over every
  characteristic-zero field; and (iii) over every field, for $n\ge2$,
  there is a depth-five circuit of size $\le n^{\sqrt n+4}$;
  `sorry` at [S7:130].

There is no `OAI/**` declaration that proves this statement, so the
formalization stops at the challenge stub. The reading is of source
text only — no `lake` or `lean` run elaborates the library, so the
claim here is that the statement and its `sorry` exist in the source,
not that the bound is proved.

## Coverage

The ledger row `fam=135` [S8] records: `tier=T2`, `paps=1`,
`paps_form=0`, `chal=1`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the single scope
note links one comparator config, but that config has no `main_results`
entry and no proved declaration under `lean/OAI/` — a T2 structural
absence. The manuscript is unformalized (`paps_form=0`). The shape
flags are `bound|classification`; `resolves_named=0`;
`counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3261], manuscript link [S1:3261] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 135 at [S2:347] |
| S3 | [`preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/paper.tex`](../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/paper.tex) | 42 | document root; `macros` import [S3:14], abstract [S3:21–32]; six section `\input` directives [S3:34–39]; 42 lines |
| S4 | [`preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/sections/01-introduction.tex`](../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/sections/01-introduction.tex) | 243 | `thm:main` [S4:53–63], circuit model [S4:20–51]; 243 lines |
| S5 | [`preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf`](../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf) | 13466 | the manuscript as shipped |
| S6 | [`lean/docs/135.md`](../../lean/docs/135.md) | 17 | scope note — Scope at [S6:7], lower bound [S6:9], upper bound [S6:11], comparator link at [S6:17] |
| S7 | [`lean/ComparatorChallenges/DepthFive.lean`](../../lean/ComparatorChallenges/DepthFive.lean) | 136 | comparator — `main` [S7:118–130], `sorry` at [S7:130]; 136 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../notes/gen/tables/catalog.tsv) | 373 | the ledger row `fam=135`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
