[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 290](../index/operator-algebras/290-connes-bicentralizer-conjecture-and-relative-bicentralizers.md)

# 290 — Connes' bicentralizer conjecture and relative bicentralizers

[Index page](../index/operator-algebras/290-connes-bicentralizer-conjecture-and-relative-bicentralizers.md)

## Original CONTENTS.md summary

[S1:7234] (family entry):

> **290. Relative bicentralizers and modular spectral recovery.** Proves Connes' bicentralizer conjecture for every type III1 factor with separable predual and every faithful normal state. More generally, for every inclusion $`N\subset M`$ of von Neumann algebras with separable preduals admitting a faithful normal conditional expectation, constructs an amenable expected subalgebra $`P\subset N`$ with $`P'\cap c(M)=N'\cap c(M)`$, resolving the relative bicentralizer conjecture. ([Lean](../../../lean/docs/290.md))

[S2:674] carries the `\resultentry` with both manuscripts, so the release blurb and the overview agree. The two manuscripts [S3:55, S3:57, S4:3, S4:5]:

> We prove that every inclusion $`N\subset M`$ of von Neumann algebras with
separable preduals and a faithful normal conditional expectation contains
an expected amenable subalgebra $`P\subset N`$ such that
$`P'\cap c(M)=N'\cap c(M)`$, where $`c(M)`$ denotes the continuous core of $`M`$.
This resolves the relative bicentralizer conjecture in this setting. [S3:60–66]

> We prove a bounded spectral recovery theorem for a von Neumann algebra with
a faithful normal state whose centralizer consists only of scalars. A positive
averaged squared norm for an arbitrary bounded Hilbert-space operator on
shrinking modular spectral bands can be recovered on uniformly bounded algebra
elements with shrinking spectral support. We apply this theorem to spectral
intertwining rigidity and obtain an alternative proof of bicentralizer triviality
for type $`\mathrm{III}_1`$ factors with separable predual. [S4:8–16]

## Undergraduate summary

A **von Neumann algebra** on a Hilbert space is a collection of operators
closed under adjoints and limits. The **commutant** of such an algebra is
the set of operators that commute with every one of it, and the
**bicentralizer** is the commutant of the commutant — a way of measuring how
"spread out" the algebra is inside its ambient space.

Connes' bicentralizer conjecture (1970s) asked for a clean description of
this bicentralizer. For the most complicated type of factor,
**type III$`_1`$** — the one with no canonical state and a continuous flow of
weight — the conjecture says the bicentralizer is as small as it can be:
*trivial* [S4:8–16].

This family answers the conjecture two ways. The second manuscript proves a
**bounded recovery theorem**: from positive averages of a modular flow you can
reconstruct bounded elements of the algebra, and that machinery gives an
*alternative proof* of bicentralizer triviality for type III$`_1`$ factors
[S4:8–16]. The first manuscript goes further, in a **relative** form: for any
inclusion $`N\subset M`$, not just a single factor, there is a large
(amenability-preserving) subalgebra of $`N`$ that captures all of $`M`$'s
bicentralizer structure [S3:60–66].

## Graduate summary

**Manuscript 1 — relative bicentralizers** [S3:60–66].
For every inclusion $`N\subset M`$ of von Neumann algebras with separable
preduals and a faithful normal conditional expectation, the construction
yields an expected amenable subalgebra $`P\subset N`$ with
$`P'\cap c(M)=N'\cap c(M)`$, where $`c(M)`$ is the continuous (Combes) core.
This is the *relative* form of the bicentralizer problem: it recovers the
core-commutant intersection $`N'\cap c(M)`$ from a subalgebra of $`N`$ that is
amenable and carries the conditional expectation. It is the named resolution
the ledger's `resolves_named` flag records.

**Manuscript 2 — bounded recovery (formalized)** [S4:8–16].
For a von Neumann algebra with a faithful normal state whose centralizer
consists only of scalars, a positive averaged squared norm for an arbitrary
bounded operator $`T`$ on shrinking modular spectral bands is recovered on a
subsequence of uniformly bounded algebra elements with shrinking spectral
support. Applied to spectral intertwining rigidity, this gives an
*alternative proof* of bicentralizer triviality for type III$`_1`$ factors with
separable predual — an independent route to the same conclusion as the
absolute form, via the recovery mechanism rather than the relative
construction.

**The formalized core.** The Lean formalization targets manuscript 2's
recovery theorem, not the relative construction. The comparator
`BoundedRecovery.lean` states the recovery: given unit vectors in shrinking
spectral bands around a real number $`s`$ and a positive limiting symmetric
average under $`T`$, it produces a subsequence of bounded algebra elements
whose images under $`T`$ stay uniformly nonzero and whose spectral bands have
four times the original widths [S5:9, S6:88–96].

## History of the conjecture

The bicentralizer of a factor sits at the heart of Connes' classification
program: its size measures how much the factor "sees" of the ambient
operator algebra. The **absolute** bicentralizer conjecture (triviality for
type III$`_1`$ factors) is the central case, and the **relative** form —
computing $`N'\cap c(M)`$ inside a continuous core — is the generalization that
subsumes it.

Manuscript 1 supplies the relative construction via amenable expected
subalgebras [S3:60–66]. Manuscript 2 supplies a second, mechanism-based
proof of the absolute case through modular spectral averaging and bounded
recovery [S4:8–16]. The two are independent routes to overlapping territory:
the relative result is more general, the recovery result gives the formalized
target and an alternative proof.

The modular averaging machinery — unitaries from the Tomita–Takesaki modular
group, spectral bands around a real parameter, and the recovery of bounded
elements from positive limsup averages — is the analytic engine in
manuscript 2 [S4:8–16].

**Prior (my training data, not this repo).** The bicentralizer problem and
its type III$`_1`$ triviality case are classical open problems in operator
algebras, approached through Connes' cocycle and flow-of-weight machinery.
The relative construction via amenable expected subalgebras, and the
independent bounded-recovery proof, are the novel contributions claimed
here; I cannot verify the modular spectral estimates independently from
training alone.

## Consequences

- **The relative bicentralizer conjecture is resolved** [S3:60–66]: every
  inclusion $`N\subset M`$ with separable preduals and a faithful normal
  conditional expectation contains an expected amenable subalgebra $`P\subset
  N`$ with $`P'\cap c(M)=N'\cap c(M)`$.
- **Bicentralizer triviality for type III$`_1`$ factors** [S4:8–16]: the
  bounded recovery theorem gives an alternative proof, via modular spectral
  averaging, that the absolute bicentralizer is trivial for every type III$`_1`$
  factor with separable predual and every faithful normal state.
- **A bounded spectral recovery theorem** [S4:8–16]: positive modular
  spectral averages are recovered on uniformly bounded algebra elements with
  shrinking support — the analytic core the release formalizes.

## Section skeleton

Manuscript 1 [S3:60–66]: root `build/paper.tex` (1391 lines), a single-file
manuscript with the relative-bicentralizer construction inline and a
`references` bibliography. Manuscript 2 [S4:8–16]: root `build/paper.tex` (24
lines), 5 sections under `build/sections/` (01-introduction,
02-bicentralizers, 03-modular-averaging, 04-bounded-recovery,
05-spectral-rigidity), a `references` bibliography. No verification bundle
for either.

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note [S5:9], a
comparator stub [S6], a `main_results` entry
(`OAI.BoundedRecovery.bounded_recovery` from
`ComparatorChallenges/BoundedRecovery.json`), and a proved OAI tree. Only
manuscript 2 is in the formalization target set; the relative construction of
manuscript 1 is not. The scope note [S5:9] states that the formalized result
"converts positive modular spectral averages into uniformly bounded algebra
elements. Given unit vectors in shrinking spectral bands around a real number
$`s`$ and a positive limiting symmetric average for a bounded operator $`T`$, it
finds a subsequence of bounded algebra elements whose images under $`T`$ stay
uniformly nonzero and whose spectral bands have four times the original
widths," and closes with the explicit exclusion: "The absolute bicentralizer
conjecture is not included." The comparator link [S5:15] names
`BoundedRecovery.lean`.

`BoundedRecovery.lean` (102 lines) carries 1 `sorry` occurrence — the
`theorem bounded_recovery` at [S6:88] is the challenge statement
(ScalarCentralizer hypothesis, free ultrafilter, shrinking spectral bands,
positive limsup under $`T`$), and ends in `sorry` at [S6:96]. The proved copy
lives under `lean/OAI/Analysis/ModularRecovery/` — a 27-file tree with 0
`sorry` occurrences total — where `Main.lean` wraps the standard-modular-data
statement as `OAI.BoundedRecovery.bounded_recovery` through the cyclic
separating-state data. The gap is manuscript 1's relative construction and
the absolute-bicentralizer application, which the scope note excludes. The
reading is of source text only.

## Coverage

The ledger row `fam=290` [S7] records the tier and the counts:
`tier=T3`, `paps=2`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `scope_chars=559`, `verification=0`, `trace=`. The T3 shape
is "scope note, comparator, `main_results`, and a proved OAI tree exist" —
the formalization target is manuscript 2's bounded recovery theorem, with one
`sorry` in the comparator stub and 0 in the 27-file OAI tree. The shape flags
are `resolution|uniform`, `resolves_named=1` — the named resolution recorded
is the relative bicentralizer conjecture (manuscript 1), which is *not* the
formalized target; the formalized target is the absolute-bicentralizer
application the scope note explicitly excludes.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7234] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 290 at [S2:674] |
| S3 | [`preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/build/paper.tex`](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/build/paper.tex) | 1391 | manuscript 1 (relative bicentralizers); title [S3:55], date [S3:57], abstract [S3:60–66] |
| S4 | [`preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/build/paper.tex`](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/build/paper.tex) | 24 | manuscript 2 (bounded recovery, formalized); title [S4:3], date [S4:5], abstract [S4:8–16] |
| S5 | [`lean/docs/290.md`](../../../lean/docs/290.md) | 15 | scope note — the formalization's Scope at [S5:9] and its comparator link at [S5:15] |
| S6 | [`lean/ComparatorChallenges/BoundedRecovery.lean`](../../../lean/ComparatorChallenges/BoundedRecovery.lean) | 102 | comparator stub — `bounded_recovery` at [S6:88] with its `sorry` at [S6:96] |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=290`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- H. Ando, U. Haagerup, C. Houdayer, and A. Marrakchi, _Structure of bicentralizer algebras and inclusions of type III factors_, Math. Ann. **376** (2020), 1145–1194. arXiv:1804.05706v2.
- A. Connes, _Classification des facteurs_, in Operator Algebras and Applications, Part 2 (Kingston, Ontario, 1980), Proc. Sympos. Pure Math. **38**, American Mathematical Society, Providence, RI, 1982, 43–109.
- A. Connes, _Factors of type $`\mathrm{III}_1`$, property $`L'_\lambda`$, and closure of inner automorphisms_, J. Operator Theory **14** (1985), 189–211.
- H. Ando and U. Haagerup, _Ultraproducts of von Neumann algebras_, J. Funct. Anal. **266** (2014), no. 12, 6842–6913. arXiv:1212.5457v3.
- U. Haagerup, _Connes' bicentralizer problem and uniqueness of the injective factor of type $`\mathrm{III}_1`$_, Acta Math. **158** (1987), 95–148. doi:10.1007/BF02392257.
- C. Houdayer and Y. Isono, _Unique prime factorization and bicentralizer problem for a class of type III factors_, Adv. Math. **305** (2017), 402–455. arXiv:1503.01388v3.
- R. Ichihara and S. Kawakami, _Disintegration of operator valued weights_, Scientiae Mathematicae Japonicae Online **e-2007** (2007), 693–699. Publisher PDF.
- C. Houdayer and A. Marrakchi, _The classification of flows on $`\mathrm{II}_1`$ factors and Connes' bicentralizer problem_, 2026, version 1, September 10, 2026. arXiv:2609.11462v1.
- A. Marrakchi, _Full factors, bicentralizer flow and approximately inner automorphisms_, Invent. Math. **222** (2020), 375–398. arXiv:1811.10253v2.
- A. Marrakchi, _Kadison's problem for type III subfactors and the bicentralizer conjecture_, Invent. Math. **239** (2025), 79–163. arXiv:2308.15163v3.
- A. Marrakchi, _Kadison's problem and ergodicity of the bicentralizer flow_, 2026, version 2, 11 August 2026. arXiv:2606.23636v2.
- T. Masuda, _An analogue of Connes–Haagerup approach for classification of subfactors of type $`\mathrm{III}_1`$_, J. Math. Soc. Japan **57** (2005), 959–1001. doi:10.2969/jmsj/1150287301.
- OpenAI, _Bounded recovery for modular spectral averages_, OpenAI Math Release preprint OAI:Bounded-recovery-for-modular-spectral-averages-September-23-2026, 2026.
- S. Popa, _On a problem of R. V. Kadison on maximal abelian $`*`$-subalgebras in factors_, Invent. Math. **65** (1981), 269–281. doi:10.1007/BF01389015.
- M. Takesaki, _Conditional expectations in von Neumann algebras_, J. Funct. Anal. **9** (1972), 306–321. doi:10.1016/0022-1236(72)90004-3.
- M. Takesaki, _Theory of Operator Algebras II_, Encyclopaedia of Mathematical Sciences **125**, Springer-Verlag, Berlin, 2003. doi:10.1007/978-3-662-10451-4.
- A. Marrakchi and S. Vaes, _Ergodic states on type $`\mathrm{III}_1`$ factors and ergodic actions_, J. Reine Angew. Math. **809** (2024), 247–260. arXiv:2305.14217v3.
