[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 009](../index/number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md)

# 009 — Bogomolov–Pop and Milnor $K$-theoretic reconstruction

[Index page](../index/number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md)

## Original CONTENTS.md summary

The release blurb 

> **009. Function-field reconstruction from Milnor K-theory and Galois data.** Reconstructs function fields of transcendence degree at least two over algebraically closed constants from $`K^{\mathrm M}_1/\ell`$, $`K^{\mathrm M}_2/\ell`$, and their product. These data recover the perfect closure and constants when ℓ differs from the characteristic, and the original field and its named base in equal characteristic. Also proves Bogomolov–Pop reconstruction from abelian-by-central pro-ℓ Galois data away from the characteristic. [S1:198]

The headline manuscript (Bogomolov–Pop) abstract 

> We prove the Bogomolov–Pop reconstruction conjecture for function fields of
transcendence degree at least two over arbitrary algebraically closed fields
of characteristic different from $`\ell`$.
The pro-$`\ell`$ abelian-by-central datum determines the perfect closure and its
constant field, with precisely the Frobenius and $`\ell`$-adic unit ambiguities. [S2:36–42]

The two October 5 companions attack the same problem from Milnor
$`K`$-theory: the mod-$`\ell`$ paper [S4:49–58] and the
mod-characteristic paper 

> Let $`K`$ and $`L`$ be finitely generated extensions of transcendence degree
at least two over algebraically closed fields of characteristic $`p`$.
We prove that every isomorphism of their first Milnor $`K`$-groups modulo
$`p`$ preserving the degree-two Steinberg relations is a nonzero scalar
multiple of the map induced by a unique field isomorphism. The proof
recovers projective lines over the subfields of $`p`$th powers by an
elementary calculation with derivations. [S6:8–16]

## Undergraduate summary

The Bogomolov–Pop question asks: can you reconstruct a function field
— the algebra of rational functions on a variety — from its Galois
group? More precisely, if you look only at the "abelian-by-central"
part of the Galois group (the part where commutators are central),
does that data determine the field up to the expected ambiguities?

This family answers yes, in three ways. The headline paper proves the
full Bogomolov–Pop reconstruction: the pro-$`\ell`$ abelian-by-central
Galois datum determines the function field (more exactly, its perfect
closure and constant field) up to exactly the Frobenius and
$`\ell`$-adic unit ambiguities. Two companion papers give a stronger
input-based version: the field is recoverable from just the Milnor
$`K`$-groups modulo $`\ell`$ (away from the characteristic) and modulo
the characteristic (in equal characteristic).

The headline statement 

> **theorem**
Let $`k`$ and $`l`$ be arbitrary algebraically closed fields of characteristics
different from $`\ell`$, and let $`K/k`$ and $`L/l`$ be function fields with
$`\mathrm{trdeg}(K/k),\mathrm{trdeg}(L/l)\ge2`$. Then
$$\Phi_{K,L}:\mathrm{Isom}_F^i(K,L)\longrightarrow
 \mathrm{Isom}^c(\Pi_L^a,\Pi_K^a)/\mathbb Z_\ell^\times,
 \qquad [\alpha]\longmapsto[\alpha^*],$$
is a bijection. [S3:55–65]

## Graduate summary

The family delivers three reconstruction theorems for function fields
of transcendence degree at least two over algebraically closed fields.

**Bogomolov–Pop (Galois data).** 

> **theorem**
Let $`k`$ and $`l`$ be arbitrary algebraically closed fields of characteristics
different from $`\ell`$, and let $`K/k`$ and $`L/l`$ be function fields with
$`\mathrm{trdeg}(K/k),\mathrm{trdeg}(L/l)\ge2`$. Then
$$\Phi_{K,L}:\mathrm{Isom}_F^i(K,L)\longrightarrow
 \mathrm{Isom}^c(\Pi_L^a,\Pi_K^a)/\mathbb Z_\ell^\times,
 \qquad [\alpha]\longmapsto[\alpha^*],$$
is a bijection. [S3:55–65]

The map $`\Phi_{K,L}`$ sends a Frobenius-compatible field isomorphism to
the class of the induced isomorphism of abelian-by-central
pro-$`\ell`$ Galois groups, modulo $`\ell`$-adic unit scaling. The
bijection is the content: no valuations, inertia groups, or curve
quotients are input, and equality of characteristics and
transcendence degrees is *forced* by the data [S3:67–71].

**Mod-$`\ell`$ Milnor $`K`$-theory.** 

> **Theorem 1.1**
Let $`\ell`$ be any prime. Let $`K/k`$ and $`L/l`$ be finitely generated
extensions of arbitrary algebraically closed fields, with
$`\mathrm{char} k,\mathrm{char} l\ne\ell`$ and
$`\mathrm{trdeg}(K/k),\mathrm{trdeg}(L/l)\ge2`$. Then is bijective.
In particular, a compatible isomorphism $`V_K\to V_L`$ forces equality
of the characteristics and of the relative transcendence degrees. [S5:64–71]

Here only the two vector spaces $`K^{\mathrm M}_1/\ell`$ and
$`K^{\mathrm M}_2/\ell`$ and their bilinear product enter. The proof
recovers the valuations and rational-subfield images from this datum;
the only ambiguity is a single global $`\mathbb F_\ell^\times`$ scalar
(trivial at $`\ell=2`$) [S5:73–76].

**Mod-characteristic Milnor $`K`$-theory.** 

> **theorem**
Let $`K/k`$ and $`L/l`$ be finitely generated extensions of algebraically
closed fields of characteristic $`p`$, with
$$\mathrm{trdeg}(K/k)\ge2,\qquad \mathrm{trdeg}(L/l)\ge2.$$
The canonical map
$$\mathrm{Isom}(K,k;L,l)\longrightarrow
 \mathrm{Isom}_{\mathrm M}(V_K,V_L)/\Lambda^\times,
 \qquad \alpha\longmapsto[\alpha_*],$$
is bijective. [S7:41–54]

In equal characteristic $`p`$, the first Milnor $`K`$-group modulo $`p`$
preserving the degree-two Steinberg relations determines the field up
to a $`\Lambda^\times`$ scalar. The proof recovers projective lines over
the subfield of $`p`$th powers by a derivation calculation
[S6:8–16].

The mod-$`\ell`$ and mod-characteristic results together cover both the
$`\ell \neq p`$ and $`\ell = p`$ regimes, complementing the Galois-data
route.

## history of the conjecture

Prior (my training data, not this repo): Bogomolov (1991) proposed the
abelian-by-central approach to birational reconstruction; Bogomolov
and Tschinkel proved the surface case over algebraic closures of
finite fields (2008) and higher-dimensional cases (2011); Pop
established a corresponding Galois-theoretic reconstruction. The
Milnor $`K`$-theory route is newer: the insight is that the Milnor
$`K`$-groups and their Steinberg relations carry the same local data
(valuations, curve quotients) that the Galois group carries, but in a
more arithmetically concrete form.

## Consequences

**Positive resolution of the Bogomolov–Pop reconstruction
conjecture** for $`\mathrm{trdeg}\ge2`$ over arbitrary
algebraically closed fields of characteristic $`\ne\ell`$, with the
ambiguities pinned to exactly Frobenius and $`\ell`$-adic units.

**Reconstruction from Milnor $`K`$-theory alone.** Both the mod-$`\ell`$
and mod-characteristic versions recover the field and its constants
from purely $`K`$-theoretic data, closing the Galois-data formulation
with a $`K`$-theoretic one.

## section skeleton

Three manuscripts, each a single-file tree.

**Bogomolov–Pop** [S2:36–42]: main file with seven flat section inputs
(introduction, preliminaries, local-theory, residual-tests,
pencil-bound, curve-recovery, reconstruction). The main theorem sits
in introduction [S3:55].

**Mod-$`\ell`$ Milnor** [S4:49–58]: main file with a `sections/` directory
(numbered 01-introduction through the reconstruction sections). The
main theorem is in 01-introduction [S5:64].

**Mod-characteristic Milnor** [S6:8–16]: a main file under a nested
`build/build/` directory with a `sections/` subdirectory. The main
theorem is in sections/01-introduction [S7:41].

## Comparison with the formalized statement

The scope note [S8:9] covers only the Bogomolov–Pop manuscript and
states a uniqueness (injectivity) result: "```lean
theorem main_graph_injective (ell : ℕ) [Fact ell.Prime]
    (k K l L : Type*) [Field k] [Field K] [Field l] [Field L]
    [IsAlgClosed k] [IsAlgClosed l] [Algebra k K] [Algebra l L]
    [Algebra.EssFiniteType k K] [Algebra.EssFiniteType l L]
    (hk : (ell : k) ≠ 0) (hl : (ell : l) ≠ 0)
    (hK : 2 ≤ Algebra.trdeg k K) (hL : 2 ≤ Algebra.trdeg l L) :
    ∀ (a a' : IsomF k K l L) (b : IsomCUnits ell K L),
      PhiGraph a b → PhiGraph a' b → a = a'  := by
  sorry
```
[S9:117–125]" If two
isomorphisms of perfect closures preserving the constant fields
induce the same Galois-data isomorphism modulo $`\ell`$-adic unit
scaling, they agree modulo Frobenius. Existence of a field
isomorphism for every admissible Galois-data isomorphism is excluded
[S8:11].

The comparator stub [S9:117–125] states the injectivity target and
ends in `sorry`. The ledger reads `paps_form 0` and `mainres 0`: none
of the three manuscripts is landed as a `main_results` entry, so the
scope note describes an intended target, not a proved Lean theorem.
The Milnor $`K`$-theory companions carry no comparator at all.

## Coverage

T2: three manuscripts, zero formalized, one comparator challenge,
zero `main_results` entries, one scope note. The ledger reads `paps
3`, `paps_form 0`, `mainres 0`, `chal 1`, `scope_note 1`,
`verification 0`, `trace` empty. The three PDFs [S11] [S12] [S13]
are named by the catalog entry [S10:94]. No `verification/` bundle,
no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 009 at line 198) |
| S2 | [`preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/paper.tex`](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/paper.tex) | 53 | Headline: Bogomolov–Pop reconstruction main file |
| S3 | [`preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/introduction.tex`](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/introduction.tex) | 164 | Bogomolov–Pop main theorem and context |
| S4 | [`preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/main.tex`](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/main.tex) | 72 | Mod-ℓ Milnor K-theory reconstruction main file |
| S5 | [`preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/sections/01-introduction.tex) | 222 | Mod-ℓ Milnor main theorem |
| S6 | [`preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/main.tex`](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/main.tex) | 26 | Mod-char Milnor K-theory main file |
| S7 | [`preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/sections/01-introduction.tex`](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/sections/01-introduction.tex) | 148 | Mod-char Milnor main theorem |
| S8 | [`lean/docs/009.md`](../../../lean/docs/009.md) | 17 | Scope note |
| S9 | [`lean/ComparatorChallenges/BogomolovPopInjectivity.lean`](../../../lean/ComparatorChallenges/BogomolovPopInjectivity.lean) | 131 | Challenge stub (injectivity, sorry) |
| S10 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 009 at line 94) |
| S11 | [`preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf`](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf) | 12578 | Compiled Bogomolov–Pop manuscript |
| S12 | [`preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf`](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf) | 15802 | Compiled mod-ℓ Milnor manuscript |
| S13 | [`preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf`](../../../preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf) | 9636 | Compiled mod-char Milnor manuscript |
