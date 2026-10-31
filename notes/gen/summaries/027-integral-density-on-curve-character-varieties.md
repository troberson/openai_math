[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 027](../index/number-theory/027-integral-density-on-curve-character-varieties.md)

# 027 — Integral density on curve character varieties

[Index page](../index/number-theory/027-integral-density-on-curve-character-varieties.md)

## Original CONTENTS.md summary

The release blurb 

> **027. Potential integral density on curve character varieties.** Resolves the determinant-one curve case of Litt's integral-density question. For every smooth connected complex algebraic curve and every rank, integral points become Zariski dense in every component of its SL*r* character variety over the full ring of integers of one number field. Prescribed quasi-unipotent boundary conjugacy classes are allowed, including nonsemisimple classes. [S1:666]

The manuscript abstract 

> We prove potential Zariski density of integral points on $`\mathrm{SL}_r`$-character
varieties of smooth complex curves in every rank. The result allows
prescribed quasi-unipotent boundary monodromy, including exact nonsemisimple
conjugacy classes, and holds on every component over the full ring of
integers of one finite extension. Here integrality is measured in the
ambient character variety, while the exact boundary conditions are imposed
on the complex representation. [S2:72–80]

## Undergraduate summary

A "character variety" of a curve $`X`$ is the space of representations
of the curve's fundamental group into a matrix group (here
$`\mathrm{SL}_r`$), up to conjugacy — a geometric object whose points encode how
the curve's loops can be assigned $`r \times r`$ matrices that multiply
the right way. The "integral points" of this variety are the
representations whose matrices have entries in a number field's ring of
integers, rather than arbitrary complex numbers.

The question is whether these integral points are *dense* in the
variety — do they come close enough to every point that, over a single
finite extension of the number field, they fill out the whole
space? The paper proves they do, in every rank, for every smooth
connected complex curve, and it allows you to *prescribe* the boundary
behavior (the monodromy around punctures) — including the
non-diagonalizable "nonsemisimple" classes, which are the harder case.
This resolves the determinant-one curve case of a question Litt asked
about integral density on character varieties.

The main statement 

> Let $`X`$ be a smooth connected complex algebraic curve and let $`r\geq1`$.
For prescribed quasi-unipotent conjugacy classes $`C_1,\ldots,C_s`$ as above,
let $`K\subset\mathbb C`$ be a number field containing their eigenvalues. There is
a finite extension $`L/K`$ such that
$$M_r(X)(\mathcal O_L)\cap Y(\mathbb C)$$
is Zariski dense in $`Y`$, and hence in every irreducible component of $`Y`$.
The same conclusion holds when only the characteristic polynomial of
each boundary monodromy is prescribed, with all its roots roots of unity.
It also holds for the entire character variety without boundary
conditions; in that case one may take $`K=\mathbb Q`$. [S3:35–57]

## Graduate summary

The theorem is a potential Zariski-density statement for integral
points on $`\mathrm{SL}_r`$-character varieties, uniform in rank and in the
curve.

**Main theorem.** 

> Let $`X`$ be a smooth connected complex algebraic curve and let $`r\geq1`$.
For prescribed quasi-unipotent conjugacy classes $`C_1,\ldots,C_s`$ as above,
let $`K\subset\mathbb C`$ be a number field containing their eigenvalues. There is
a finite extension $`L/K`$ such that
$$M_r(X)(\mathcal O_L)\cap Y(\mathbb C)$$
is Zariski dense in $`Y`$, and hence in every irreducible component of $`Y`$.
The same conclusion holds when only the characteristic polynomial of
each boundary monodromy is prescribed, with all its roots roots of unity.
It also holds for the entire character variety without boundary
conditions; in that case one may take $`K=\mathbb Q`$. [S3:35–57]

For a smooth connected complex curve $`X`$ and rank $`r \ge 1`$, with
prescribed quasi-unipotent boundary conjugacy classes and a number field
$`K`$ containing their eigenvalues, there is a *single* finite extension
$`L/K`$ (fixed for the whole locus, all components included) such that
integral points $`M_r(X)(\mathcal O_L) \cap Y(\mathbb C)`$ are Zariski dense in $`Y`$ —
hence in every irreducible component. The density is "potential"
because it holds after one finite extension, not over $`K`$ itself. The
same conclusion holds for characteristic-polynomial boundary data with
all roots of unity, and for the boundary-free variety where one may
take $`K = \mathbb Q`$.

**The precise field.** [S3:49–56]: for relative and projective $`X`$ one
may take distinct primes $`p, q > r`$ and the explicit field
$`F = K(\sqrt{2}, \zeta_{pq})`$ with
$`L = F(\zeta_r, \{u^{1/r} : u \in \mathcal O_F^\times\})`$; the extension is
finite because the unit group of $`\mathcal O_F`$ is finitely generated. No
restriction on the genus or the Jordan forms is imposed.

## history of the conjecture

Prior (my training data, not this repo): Zariski density of integral
points on character varieties is a hard arithmetic-geometric question
in the orbit of the "integral points on varieties" program
(Hirzebruch, Vojica's work on Mordell--Lang, and the
character-variety density of Lubotzky and collaborators). Litt framed an
integral-density question for curve character varieties asking whether
integral points become dense after one finite extension; the
determinant-one ($`\mathrm{SL}_r`$) curve case, with prescribed quasi-unipotent
boundary data including exact nonsemisimple classes, is the content
here. The quasi-unipotent boundary condition and the nonsemisimple
classes are the difficult part: they force the marked-surface
construction to stay compatible across every seam of a diagram, which
is the supporting lemma the formalization lands.

## Consequences

**Potential integral density on $`\mathrm{SL}_r`$ curve character varieties.**
For every smooth connected complex curve and every rank, integral
points are Zariski dense in every component after one finite extension
[S3:35–57].

**Prescribed quasi-unipotent boundary data, including nonsemisimple
classes.** The density holds with the boundary monodromy fixed, not
just for the boundary-free variety [S2:72–80].

## section skeleton

Single main file [S2:72–80] with eight section inputs [S2:82–89]
(introduction, model, arithmetic, diagrams, reduction, surfaces,
dynamics, descent), one `.bib` file [S7], and two figure files under
`build/figures/` (diagram-band.tex, diagram-swap.tex).

**Sections** [S2:82–89]: Introduction (introduction.tex) with the main
theorem (line 35); model (model.tex); arithmetic (arithmetic.tex);
diagrams (diagrams.tex); reduction (reduction.tex); surfaces
(surfaces.tex); dynamics (dynamics.tex); descent (descent.tex).

## Comparison with the formalized statement

The scope note [S4:9] states exactly what the linked formalization
proves: "The integral-density question asks whether integral points become Zariski dense in every component of a curve character variety after one finite extension of the number field. The linked formalization proves a supporting compatibility result for its marked-surface construction. Given a proper diagram with finitely many vertices, a chosen seam with maximal adjacent facet rank and a positive-genus parent, puncture data, an existing solution over a field, and a chosen boundary occurrence, the produced marked values satisfy every seam equation. [S4:9]" — a *supporting* compatibility result for the
marked-surface construction (the produced marked values satisfy every
seam equation), not the headline theorem.

The comparator stub [S5:17–19] states the same seam-equation target and
ends in `sorry`:

```lean
theorem producedMarkedValues_allSeams :
    D.ProducedMarkedSeamEquations q hproper hmax hg P x b0 i0 := by
  sorry
```
[S5:17–19]

The proof lands in
`OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean`
[S6], which carries **zero** `sorry` occurrences; the single
`main_results` entry
(`OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams`)
is in that file (ledger `paps_form 1`, `mainres 1`, `chal 1`).

The scope note is explicit that the headline is *not* landed [S4:11]:
"Existence of integral points and Zariski density are not established.
The paper's main theorem—potential integral density for $`\mathrm{SL}_r`$
curve character varieties over one finite extension, including
prescribed quasi-unipotent boundary data and every irreducible
component—is outside this comparison." So the formalization proves the
supporting seam-equation lemma the density proof builds on, while the
Zariski-density statement itself remains a manuscript result.

**Tree measurement (source-level).**

The `main_results` entry OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams resolves to `OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean` (158 lines); the top-level theorem is `theorem producedMarkedValues_allSeams`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 13 files with 2 theorems and 98 defs.

The preprint states 15 theorem environments while the tree carries only 2 (0.13×), indicating a focused sub-formalization (source-level).

## Coverage

T3: one manuscript, one comparator challenge, one `main_results`
entry, one scope note. The ledger reads `paps 1`, `paps_form 1`,
`mainres 1`, `chal 1`, `scope_note 1`, `verification 0`, `trace`
empty, `shapes resolution|bound|density|uniform`, `resolves_named 1`.
The family ships a twelve-file LaTeX manuscript (main file plus eight
sections plus `references.bib` [S7] plus two figure files) and a
compiled `paper.pdf` [S8]. The catalog entry [S9:130] names the single
PDF. No `verification/` bundle, no reasoning trace. The one landed
result is the supporting seam-equation compatibility lemma; the
headline potential-integral-density theorem is outside the comparison
per the scope note [S4:11].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 027 at line 666) |
| S2 | [`preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/main.tex`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/main.tex) | 92 | Main file: abstract, section inputs |
| S3 | [`preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/sections/introduction.tex`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/sections/introduction.tex) | 194 | Main theorem (potential integral density) |
| S4 | [`lean/docs/027.md`](../../../lean/docs/027.md) | 17 | Scope note |
| S5 | [`lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.lean`](../../../lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.lean) | 25 | Challenge stub (seam-equation compatibility, sorry) |
| S6 | [`lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean`](../../../lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean) | 158 | Proved supporting result in the Lean tree (0 sorry) |
| S7 | [`preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/references.bib`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/references.bib) | 242 | Bibliography |
| S8 | [`preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf) | 13064 | Compiled manuscript |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 027 at line 130) |

## Bibliography

- Bate, Michael, Martin, Benjamin, Röhrle, Gerhard, Tange, Rudolf, Complete reducibility and conjugacy classes of tuples in algebraic groups and Lie algebras (2011)
- Coccia, Simone, Litt, Daniel, Density of integral points in the Betti moduli of quasi-projective varieties (2025)
- Esnault, Hél{\`e}ne, Groechenig, Michael, Cohomologically rigid local systems and integrality (2018)
- Franjou, Vincent, van der Kallen, Wilberd, Power reductivity over an arbitrary base (2010)
- Gerstenhaber, Murray, On dominance and varieties of commuting matrices (1961)
- Ghosh, Amit, Sarnak, Peter, Integral points on Markoff type cubic surfaces (2022)
- Goldman, William M., Invariant functions on Lie groups and Hamiltonian flows of surface group representations (1986)
- Guralnick, Robert M., A note on commuting pairs of matrices (1992)
- Guralnick, Robert M., Sethuraman, B. A., Commuting pairs and triples of matrices and related varieties (2000)
- de Jong, Johan, Esnault, Hél{\`e}ne, Integrality of the Betti moduli space (2024)
- Lang, Serge, Weil, André, Number of points of varieties in finite fields (1954)
- Liebeck, Martin W., Shalev, Aner, Fuchsian groups, finite simple groups and representation varieties (2005)
- Litt, Daniel, Problems I Like, Problem 7
- Litt, Daniel, Motives, mapping class groups, and monodromy (2024)
- Mellit, Anton, Toric stratifications of character varieties (2025)
- Milne, James S., Algebraic Number Theory (2020)
- Motzkin, T. S., Taussky, Olga, Pairs of matrices with property L. II (1955)
- Mumford, David, Suominen, Kalevi, Introduction to the theory of moduli (1972)
- Poonen, Bjorn, Rational points on varieties (2017)
- Simpson, Carlos T., Higgs bundles and local systems (1992)
- Su, Tao, Cell decomposition and dual boundary complexes of character varieties (2026)
- Whang, Junho Peter, Nonlinear descent on moduli of local systems (2020)
