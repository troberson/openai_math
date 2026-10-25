[Notes](../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 044](../index/algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md)

# 044 — The equivariant cohomological Hikita conjecture for quivers

[Index page](../index/algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md)

## Original CONTENTS.md summary

The release's blurb "**044. The equivariant cohomological Hikita conjecture.** Proves the equivariant cohomological Hikita correspondence for every finite quiver, including loops and multiple arrows, with arbitrary dimension and framing vectors and commuting flavor torus. When every semistable point is stable and the gauge action is free, the equivariant cohomology of the Nakajima variety is canonically the coordinate ring of the scheme-theoretic cocharacter-fixed locus of its flavor-deformed Coulomb branch. [S1:1217]" The manuscript title is
"The equivariant cohomological Hikita conjecture for arbitrary quivers [S3:1]" , and its abstract reads: "We prove the equivariant cohomological Hikita conjecture for arbitrary finite
quivers, including loops and multiple arrows. For any dimension and framing
vectors, any commuting flavor torus, and a stability character whose
semistable locus is stable and has free gauge action, the equivariant
cohomology of the Nakajima variety is canonically isomorphic to the coordinate
ring of the scheme-theoretic fixed locus of the stability cocharacter on the
flavor-deformed Coulomb branch. This is an isomorphism of graded algebras over
the common coefficient ring, retaining nilpotents and including the empty case. [S4:49–56]"

## Undergraduate summary

Hikita's conjecture relates the cohomology of a symplectic resolution
to the functions on a fixed subscheme of a Coulomb branch. The scheme
structure is essential: nilpotent functions on the fixed locus encode
positive-degree cohomology . "Hikita's conjecture relates two different kinds of algebra: the cohomology
of a symplectic resolution and the functions on a fixed subscheme of a
corresponding Coulomb branch.  The scheme structure is essential.  Even
when the underlying fixed-point set is small, its nilpotent functions can
encode positive-degree cohomology.  For quiver gauge theories, the
tautological classes on the Higgs side and the equivariant parameters on
the Coulomb side give a common coefficient ring.  The question is whether
the relations among those coefficients agree. [S5:4–11]" For a finite quiver $Q$
with vector spaces $V_i, W_i$, the gauge group is
$G=\prod\GL(V_i)$ and the representation includes both arrow maps and
framing maps . "allowed.  Fix complex vector spaces $V_i,W_i$ of dimensions $v_i,w_i$, and put
$$\label{eq:gauge-data}
 G=\prod_{i\in Q_0}\GL(V_i),\qquad
 N=\bigoplus_{a:i\to j}\Hom(V_i,V_j)
       \oplus\bigoplus_{i\in Q_0}\Hom(V_i,W_i).$$ [S5:24–29]" A regular stability character $\nu$
makes the semistable locus stable with free gauge action, producing a
smooth Nakajima variety $X$. The theorem 

> **Theorem 1.1**
For every datum  , every commuting flavor torus $F$, and
every regular stability character $\nu$, both coefficient maps are
surjective and have the same kernel.  They therefore induce a canonical
isomorphism of graded
$R$-algebras
\[
 H_F^*(X;\mathbb C)\ \cong\ \mathbb C[Y_{\mathfrak f}^{\nu}].
\]
The gradings are ordinary cohomological degree and BFN homological degree,
respectively.  The assertion includes the empty case, whose ring is zero. [S5:78–89]

The gradings are cohomological degree on the Higgs side and BFN
homological degree on the Coulomb side. No finite-type, Dynkin,
conical, or good/ugly hypothesis is imposed [S5:91–94].

## Graduate summary

**The two-ideal comparison.** The proof splits into two tasks:
equalize the full-torus ideals $I_{\mathrm{top}}=I_H$, and equalize
the cocharacter and full-torus defining ideals inside $A_F$ 

> Define the intermediate coefficient algebra and the two ideals to be
compared by
$$\label{eq:intro-two-ideals}
 \begin{split}
 B_F&=\mathbb C[Y_{\mathfrak f}^{T_{\mathrm{top}}}]
      =A_F/\langle A_F^{(d)}:d\ne0\rangle,\\
 I_{\mathrm{top}}&=\ker(R\longrightarrow B_F),\qquad
 I_H=\ker(R\xrightarrow{\phi_H}H_F^*(X)),
 \end{split}$$
where $A_F^{(d)}$ is the subspace of topological charge
$d\in\pi_1(G)$; its cocharacter weight is $\nu\cdot d$.  Neither of
these is the cohomological degree used in Hilbert series.
Section   explains why the
coefficient maps to $B_F$ and to $H_F^*(X)$ are surjective.
Thus the first task is precisely the equality
$I_{\mathrm{top}}=I_H$.  The second task is the equality of the
cocharacter and full-torus defining ideals inside $A_F$. [S5:188–205]

**Stable pairs give a quotient map.** Minuscule convolution words of
total topological charge zero are realized by finite-dimensional
lattice correspondences. The stable-pair test evaluates them: after
reordering, the first modification has nonpositive character-line
degree, which stability excludes 

> \paragraph1. Stable pairs give a quotient map.
Sections   and   prove
$I_{\mathrm{top}}\subseteq I_H$ for all the data of the theorem.
The nontrivial minuscule generators used here are dressed lattice
modifications whose coweight entries are all in $\{0,1\}$ or all in
$\{0,-1\}$, with nonzero topological charge; a subset may involve several
vertices.  A convolution word is a finite product of these classes.
By minuscule generation, a coefficient in $I_{\mathrm{top}}$ is a finite
sum of positive-length convolution words, each of total topological charge zero.
Section   realizes each such word by
finite-dimensional lattice correspondences, keeping all degree shifts.
The test in Section   evaluates them on stable
cotangent pairs.  The stability character assigns an additive degree to
each modification, so the degrees in a neutral word sum to zero.
After reordering each word, its first modification is nontrivial and has
nonpositive character-line degree; stability excludes it.  On the identity
correspondence, the same test gives a split restriction onto $H_F^*(X)$,
which detects the coefficient class itself.  The tested relation therefore vanishes
in cohomology, yielding the graded coefficient-compatible surjection
$B_F\twoheadrightarrow H_F^*(X)$ of
Proposition  . [S5:210–230]

This yields the graded surjection $B_F\twoheadrightarrow H_F^*(X)$.

**Loops and counting.** Adding loops at every positive-dimension
vertex cancels Grassmannian denominators in minuscule abelianization.
A Laurent model filters $B_0$ by multipartitions; the Hilbert series
of successive quotients is identified with Hausel's Poincaré
polynomial, forcing equality in every degree.

**Deformation removes the loops.** The no-flavor isomorphism for the
looped quiver $Q^+$ is lifted to an auxiliary flavor
$H=\mathbb C^\times$ with parameter $z$. Subgroup localization at
$z=1$ gives the Higgs-side comparison; homogeneity descends the
equality to the original ideals 

> \paragraph3. Deformation returns to the original data.
For an arbitrary quiver $Q$, let $Q^+$ be obtained by adding one loop at
each vertex of positive gauge dimension.  Give the new loops the common
weight one of an auxiliary flavor torus $H=\mathbb C^\times$, with parameter
$z\in H_H^2(\mathrm{pt})$.
The comparison in Section   uses a lift of the
no-flavor isomorphism for $Q^+$ to this flavor.  Near zero gauge parameters and nonzero mass
$z=1$, the new minuscule Euler factors are invertible on the Coulomb
side.  Subgroup localization on the stable prequotient gives the
corresponding comparison on the Higgs side.  The resulting equality of
localized coefficient ideals descends to the original homogeneous ideals
in $R_0$: their equality at the graded origin determines them globally.
This homogeneity argument, not specialization of an unspecified generic
isomorphism, is the content of Proposition  .
Local constancy of regular stability, quaternionic rotation, and generic
constancy of compactly supported Betti numbers then compare all regular
characters.  A final flavor lift proves
$B_F\simeq H_F^*(X)$ in Theorem  . [S5:249–266]

**Complementary monopoles.** The cocharacter-fixed quotient is
identified with the full-torus quotient independently. Adjoining a
rank-one framing vertex, any surviving monopole has a complementary
monopole; Hall generation decomposes both into indecomposable charges,
and the resulting semistable direct sum has positive-dimensional
stabilizer, contradicting freeness 

> \paragraph4. Complementary monopoles identify the cocharacter quotient.
Section   proves, independently of the preceding
cohomology comparison, that the natural map
$\mathbb C[Y_{\mathfrak f}^{\nu}]\to B_F$ is an isomorphism.
It combines polynomial-form Hall-algebra generation
  with the monopole maps of
Lemma  , derived from
\cite[Theorem 5.7]Tsymbaliuk23Difference with explicit product signs.
The resulting finite identities can be specialized without dividing by
rotation or arrow parameters.
After adjoining a rank-one framing vertex, any surviving nontrivial minuscule
monopole has a surviving complementary monopole.  Hall generation would
then decompose both charges into indecomposable charges of the enlarged
quiver, all of weight zero for the extended character.
Lemma   realizes these charges by moment-level blocks.
Their semistable direct sum has a stabilizer that remains
positive-dimensional even after removing the ineffective diagonal
scalar.  This contradicts the freeness in regularity, including when
the semistable locus is empty.  Proposition  
therefore identifies the two defining ideals, completing the
scheme-theoretic comparison. [S5:268–288]

## History of the conjecture

The classical model is type-$A$ Springer-fiber cohomology through
scheme-theoretic intersections, developed by de Concini–Procesi and
Tanisaki. In symplectic duality, Hikita formulated the fixed-scheme
realization and proved it for the Hilbert scheme of points in the
plane . "A classical model is the description of type-$A$ Springer-fiber
cohomology through scheme-theoretic intersections of nilpotent orbit
closures with a Cartan subalgebra, developed by de Concini–Procesi and
Tanisaki  .  In the setting of
symplectic duality  , Hikita formulated a fixed-scheme
realization of cohomology and established it for the Hilbert scheme of
points in the plane, with related type-$A$ Spaltenstein and smooth
hypertoric examples  .  These examples explain why the
infinitesimal structure of the fixed locus, rather than its set of
points, is central to the question. [S5:98–107]"

The Coulomb-branch construction comes from Nakajima and
Braverman–Finkelberg–Nakajima. The coefficient-compatible formulation
has predecessors in Kamnitzer–Tingley–Webster–Weekes–Yacobi,
Hilburn–Kamnitzer–Weekes, and Krylov–Shlykov, who state the
general-quiver comparison as equality of coefficient-map kernels.
Krylov–Shlykov prove the Gieseker case; Dumanski–Krylov give the
finite-type ADE result with framing restrictions in types
$E_7, E_8$ [S5:109–148].

## Consequences

**The full equivariant cohomological Hikita conjecture.** For every
finite quiver, including loops and multiple arrows, with arbitrary
dimension and framing vectors and commuting flavor torus, the
equivariant cohomology of the Nakajima variety is canonically the
coordinate ring of the scheme-theoretic cocharacter-fixed locus of the
flavor-deformed Coulomb branch [S5:78–89]. The isomorphism retains
nilpotents and includes the empty case.

**No structural hypotheses.** The theorem imposes no finite-type,
Dynkin, conical, or good/ugly condition [S5:91–94]. It does not assert
the quantized statement nor extend to arbitrary reductive gauge groups
[S5:144–148].

## Section skeleton

**Main file** [S4:49–56], 8 sections under `build/sections/`:

1. Introduction [S5]
2. Preliminaries [S6]
3. Correspondences [S7]
4. Stable pairs [S8]
5. Laurent model [S9]
6. Counting [S10]
7. Deformations [S11]
8. Cocharacters [S12]

Proof-route figure: `figures/proof-route.tex` [S13].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
10 `.tex` files under `build/`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | The release's blurb for family 044 at line 1217. |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The catalog abstract at line 166. |
| S3 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/README.md`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/README.md) | 18 | Manuscript readme: title, author, date. |
| S4 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/main.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/main.tex) | 83 | The main file: abstract and section inputs. |
| S5 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/introduction.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/introduction.tex) | 290 | The statement, the coefficient maps, the theorem, the history, and the proof strategy. |
| S6 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/preliminaries.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/preliminaries.tex) | 254 | Surjectivity of the coefficient maps. |
| S7 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/correspondences.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/correspondences.tex) | 311 | Lattice correspondences for convolution words. |
| S8 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/stable-pairs.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/stable-pairs.tex) | 390 | The stable-pair test. |
| S9 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/laurent.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/laurent.tex) | 467 | The Laurent model and multipartition filter. |
| S10 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/counting.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/counting.tex) | 387 | Hilbert series computation and Hausel's Poincaré polynomial. |
| S11 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/deformations.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/deformations.tex) | 281 | Loop removal and flavor lift. |
| S12 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/cocharacters.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/cocharacters.tex) | 650 | Complementary monopoles and the cocharacter-fixed isomorphism. |
| S13 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/figures/proof-route.tex`](../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/figures/proof-route.tex) | 73 | The proof-route figure. |
