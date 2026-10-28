[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 341](../index/differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md)

# 341 — Donaldson's hypersymplectic deformation conjecture

[Index page](../index/differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:8288] and the catalog abstract [S2:780] state
the family's claim: every positive triple of smooth closed two-forms on
a closed connected oriented four-manifold, normalized by
$\int\omega_i\wedge\omega_j=\delta_{ij}$, deforms through positive
closed triples to a hyperkähler triple while preserving all three
cohomology classes. The manuscript's abstract "Every smooth normalized positive triple of closed two-forms on a closed
connected oriented four-manifold admits a smooth deformation, with each
cohomology class fixed, to a hyperkähler triple.
This resolves Donaldson's hypersymplectic deformation conjecture. [S3:7–12]"

## Undergraduate summary

A hypersymplectic structure on an oriented four-manifold is a triple
of closed two-forms whose pointwise span is positive definite for the
wedge product. Such a triple determines a conformal structure, but
its forms need not be parallel. Donaldson's Question 3 (2006) asks
whether a compact oriented four-manifold carrying a positive closed
triple admits a hyperkähler structure. Fine and Yao formulated the
normalized deformation problem as their Conjecture 1.1 (2017). The
manuscript resolves this deformation conjecture 

> **theorem**
Let $X$ be a closed connected oriented smooth four-manifold, and let
$\omega=(\omega_1,\omega_2,\omega_3)$ be a smooth hypersymplectic structure
normalized by
$$\int_X\omega_i\wedge\omega_j=\delta_{ij}.$$
There is a smooth family of hypersymplectic structures $\omega(t)$,
$0\le t\le1$, such that
$$\omega(0)=\omega,\qquad [\omega_i(t)]=[\omega_i]
 \quad (i=1,2,3),$$
and a positive volume form $\mu_1$ with
$$\omega_i(1)\wedge\omega_j(1)=2\delta_{ij}\mu_1.$$
The endpoint forms are parallel and self-dual for a hyperkähler metric. [S4:11–29]

A corollary identifies the smooth type: any closed connected
four-manifold admitting a positive closed triple is diffeomorphic to
the standard K3 manifold or to $T^4$ [S4:77–90].

## Graduate summary

**The lattice and $b^+=3$.** The topology of a positive closed triple
is rigid: any two forms determine an almost-complex structure whose
canonical line is trivial, and the third form tames it. Bauer's bound
plus the three positive period classes gives $b^+=3$; the lattice is
the K3 lattice or three hyperbolic planes [S4:153–170].

**Currents and the prescribed taming class.** Cone separation of
positive forms gives a positive current obstructing a desired closed
form. Quadratic mass estimates and resolvent regularization prove
closedness after density-weighting. Normalized thresholds yield
integral pseudoholomorphic cycles, giving a taming class in the
intersection-orthogonal complement of the pair [S4:201–217].

**The torus fibration.** The initial triple supplies a sphere of
almost-complex structures. Compatible forms are selected smoothly
over this sphere; their classes project to a degree-one map to the
unit sphere. Li–Liu wall-crossing and Taubes curve extraction give
curves through every point in a chosen integral square-zero class.
Adjunction and positivity reduce fibers to tori and
one-nodal rational curves [S4:218–252].

**The auxiliary volume equation and two Kähler steps.** Near a
nodal fiber, a Gibbons–Hawking/Ooguri–Vafa model glues to an
auxiliary form of small fiber area. An exact-form identity controls
the inverse while fibers collapse, producing a closed equal-square
pair $A,D$. Two Kähler steps in the original classes — Buchdahl–Lamari
criteria plus Yau's volume theorem — complete the hyperkähler
triple with every class preserved [S4:281–310].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Donaldson formulated the question in his 2006 study of closed
two-forms on four-manifolds. Fine and Yao (2017) obtained the
hypersymplectic flow from the $G_2$-Laplacian flow and proved
finite-time extension under bounded torsion; their later work gives
an integral torsion extension criterion and subsequential convergence
under geometric bounds. Complete convergence is known for restricted
classes: Huang–Wang–Yao for simple-type structures on $T^4$;
Picard–Suan for $G_2$ flows from Kähler Calabi–Yau data;
Fine–He–Yao for $T^3$-invariant triples in symmetric normal form and
for triples preserved by a smooth circle action [S4:103–152]. The
path constructed here starts from an arbitrary positive closed triple;
its existence is separate from convergence or uniqueness for the
hypersymplectic flow [S4:152].

## Consequences

**Donaldson's hypersymplectic deformation conjecture is resolved
in the cohomology-preserving form.** Every smooth normalized positive
triple deforms through positive closed triples to a hyperkähler
triple with all three cohomology classes fixed [S4:11–29].

**The smooth type is K3 or $T^4$.** Any closed connected
four-manifold admitting a positive closed triple is diffeomorphic to
the standard K3 manifold or to $T^4$ [S4:77–90].

**Every linear combination is Kähler for some hyperkähler metric.**
For every fixed nonzero $c\in\mathbb R^3$, the form $\alpha_c=\sum c_i\omega_i$
is a Kähler form for a parallel integrable complex structure of some
hyperkähler metric [S4:55–76].

## Section skeleton

**Manuscript** [S3:7–12], 11 sections under `build/sections/`:
introduction [S4:11–29], definite pairs, current energy, density splitting,
families, lattice chamber, pencil, local models, regular preparation,
auxiliary volume, endpoint. Its root is `build/main.tex`, with a
`preamble.tex` and a `references.bib` bibliography. One figure file
(`figures/endpoint-path.tex`).

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, a `preamble.tex`, 11 `.tex`
files under `build/sections/`, one figure `.tex`, and a
`references.bib` bibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 341 at line 8288. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 780. |
| S3 | [`preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/build/main.tex`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/build/main.tex) | 28 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/build/sections/01-introduction.tex`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/build/sections/01-introduction.tex) | 335 | Introduction: the main theorem, corollaries, history, and proof strategy. |
