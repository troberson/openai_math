[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 044](../../index/algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md)

# 044 — The equivariant cohomological Hikita conjecture for quivers

[Index page](../../index/algebraic-and-complex-geometry/044-equivariant-cohomological-hikita-conjecture-for-quivers.md)

## Original CONTENTS.md summary

The release's blurb [S1:1217]: "**044. The equivariant cohomological Hikita conjecture.** Proves the equivariant cohomological Hikita correspondence for every finite quiver, including loops and multiple arrows, with arbitrary dimension and framing vectors and commuting flavor torus. When every semistable point is stable and the gauge action is free, the equivariant cohomology of the Nakajima variety is canonically the coordinate ring of the scheme-theoretic cocharacter-fixed locus of its flavor-deformed Coulomb branch." The manuscript title is
"The equivariant cohomological Hikita conjecture for arbitrary quivers" [S3:1], and its abstract [S4:49–56] reads: "We prove the equivariant cohomological Hikita conjecture for arbitrary finite"

## Undergraduate summary

Hikita's conjecture relates the cohomology of a symplectic resolution
to the functions on a fixed subscheme of a Coulomb branch. The scheme
structure is essential: nilpotent functions on the fixed locus encode
positive-degree cohomology [S5:4–11]. "Hikita's conjecture relates two different kinds of algebra: the cohomology" For a finite quiver $Q$
with vector spaces $V_i, W_i$, the gauge group is
$G=\prod\GL(V_i)$ and the representation includes both arrow maps and
framing maps [S5:24–29]. "allowed.  Fix complex vector spaces $V_i,W_i$ of dimensions $v_i,w_i$, and put" A regular stability character $\nu$
makes the semistable locus stable with free gauge action, producing a
smooth Nakajima variety $X$. The theorem [S5:78–89]:

> **theorem**


The gradings are cohomological degree on the Higgs side and BFN
homological degree on the Coulomb side. No finite-type, Dynkin,
conical, or good/ugly hypothesis is imposed [S5:91–94].

## Graduate summary

**The two-ideal comparison.** The proof splits into two tasks:
equalize the full-torus ideals $I_{\mathrm{top}}=I_H$, and equalize
the cocharacter and full-torus defining ideals inside $A_F$ [S5:188–205]:

> Define the intermediate coefficient algebra and the two ideals to be

**Stable pairs give a quotient map.** Minuscule convolution words of
total topological charge zero are realized by finite-dimensional
lattice correspondences. The stable-pair test evaluates them: after
reordering, the first modification has nonpositive character-line
degree, which stability excludes [S5:210–230]:

> \paragraph{1. Stable pairs give a quotient map.}

This yields the graded surjection $B_F\twoheadrightarrow H_F^*(X)$.

**Loops and counting.** Adding loops at every positive-dimension
vertex cancels Grassmannian denominators in minuscule abelianization.
A Laurent model filters $B_0$ by multipartitions; the Hilbert series
of successive quotients is identified with Hausel's Poincaré
polynomial, forcing equality in every degree.

**Deformation removes the loops.** The no-flavor isomorphism for the
looped quiver $Q^+$ is lifted to an auxiliary flavor
$H=\C^\times$ with parameter $z$. Subgroup localization at
$z=1$ gives the Higgs-side comparison; homogeneity descends the
equality to the original ideals [S5:249–266]:

> \paragraph{3. Deformation returns to the original data.}

**Complementary monopoles.** The cocharacter-fixed quotient is
identified with the full-torus quotient independently. Adjoining a
rank-one framing vertex, any surviving monopole has a complementary
monopole; Hall generation decomposes both into indecomposable charges,
and the resulting semistable direct sum has positive-dimensional
stabilizer, contradicting freeness [S5:268–288]:

> \paragraph{4. Complementary monopoles identify the cocharacter quotient.}

## History of the conjecture

The classical model is type-$A$ Springer-fiber cohomology through
scheme-theoretic intersections, developed by de Concini–Procesi and
Tanisaki. In symplectic duality, Hikita formulated the fixed-scheme
realization and proved it for the Hilbert scheme of points in the
plane [S5:98–107]. "A classical model is the description of type-$A$ Springer-fiber"

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

**Main file** [S4], 8 sections under `build/sections/`:

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
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 044 at line 1217. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 166. |
| S3 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/README.md`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/README.md) | 18 | Manuscript readme: title, author, date. |
| S4 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/main.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/main.tex) | 83 | The main file: abstract and section inputs. |
| S5 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/introduction.tex) | 290 | The statement, the coefficient maps, the theorem, the history, and the proof strategy. |
| S6 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/preliminaries.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/preliminaries.tex) | 254 | Surjectivity of the coefficient maps. |
| S7 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/correspondences.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/correspondences.tex) | 311 | Lattice correspondences for convolution words. |
| S8 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/stable-pairs.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/stable-pairs.tex) | 390 | The stable-pair test. |
| S9 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/laurent.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/laurent.tex) | 467 | The Laurent model and multipartition filter. |
| S10 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/counting.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/counting.tex) | 387 | Hilbert series computation and Hausel's Poincaré polynomial. |
| S11 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/deformations.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/deformations.tex) | 281 | Loop removal and flavor lift. |
| S12 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/cocharacters.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/sections/cocharacters.tex) | 650 | Complementary monopoles and the cocharacter-fixed isomorphism. |
| S13 | [`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/figures/proof-route.tex`](../../../preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/figures/proof-route.tex) | 73 | The proof-route figure. |
