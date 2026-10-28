[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 057](../index/algebraic-and-complex-geometry/057-campanas-abelianity-conjecture-and-special-varieties.md)

# 057 — Campana's abelianity conjecture and special varieties

[Index page](../index/algebraic-and-complex-geometry/057-campanas-abelianity-conjecture-and-special-varieties.md)

## Original CONTENTS.md summary

The release's blurb "**057. Fundamental groups of special complex varieties and root orbifolds.** Proves Campana's abelianity conjecture: special compact Kähler manifolds have virtually abelian fundamental groups. Using this theorem, establishes the same conclusion for order-two root orbifolds of smooth projective complex fourfolds along one nonempty smooth connected divisor, when special in the stated differential-line sense. For smooth special complex quasi-projective varieties, proves that every finite-dimensional complex linear representation of the fundamental group has virtually nilpotent image of class at most two. [S1:1481]"

Three manuscripts carry this family. The first,
*The abelianity conjecture for special compact Kähler manifolds*
[S2:36–40], has the abstract "We prove that the fundamental group of every special compact Kähler
manifold is virtually abelian, resolving Campana's abelianity conjecture
in all dimensions. In particular, every smooth compact connected
Kähler manifold of Kodaira dimension zero has virtually abelian
ordinary fundamental group. [S2:36–40]"

The second, *Two-step monodromy of special quasi-projective
varieties* [S9:60–66], has the abstract "We give an independent proof that every complex linear representation
of the ordinary fundamental group of a connected smooth special complex
quasi-projective variety has virtually nilpotent image of class at most
two. This conclusion was previously announced by
Cao–Deng–Hacon–Păun. We also construct special open surfaces whose
general quasi-Albanese fibres are not special. [S9:60–66]"

The third, *A conditional abelianity theorem for special fourfold
pairs with a half-weight divisor* [S13:10], has the abstract
 "Using the abelianity theorem for special compact Kähler manifolds in every dimension, we prove virtual abelianity of the entire orbifold fundamental group of the special order-two root orbifold associated with a pair $(X,\tfrac12D)$, where $X$ is a smooth projective fourfold and $D$ is a nonempty smooth connected divisor. We construct a special smooth projective eightfold whose fundamental group surjects onto the required group. [S13:10]"

## Undergraduate summary

Campana's classification program separates compact Kähler geometry
into special varieties and bases of general type. Specialness records
the absence of differential forms that would detect such a base. One
of the program's central predictions is topological: the fundamental
group of a special compact Kähler manifold should become abelian
after passage to a finite unramified cover . "Campana's classification program separates compact Kähler geometry
into special varieties and bases of general type. Specialness records
the absence of differential forms that would detect such a base. One
of the program's central predictions is topological: the fundamental
group of a special compact Kähler manifold should become abelian
after passage to a finite unramified cover
\cite[Conjecture A.1]ClaudonHoring2013. [S3:3–9]"

The theorem 

> **theorem**
Let \(X\) be a connected smooth compact Kähler manifold of arbitrary
complex dimension. If \(X\) is special, then \(\pi_1(X)\) has an abelian
subgroup of finite index. Equivalently, \(X\) has a connected finite
unramified holomorphic cover with abelian fundamental group. [S3:26–31]

This is a positive resolution of the conjecture in the compact
Kähler setting. The conclusion concerns the entire discrete
topological fundamental group. It requires no linearity, residual
finiteness, projectivity, or prescribed Kodaira dimension [S3:33–37].
"This is a positive resolution of the conjecture in the compact
Kähler setting. The conclusion concerns the entire discrete
topological fundamental group. It requires no linearity, residual
finiteness, projectivity, or prescribed Kodaira dimension. The finite
index may depend on \(X\), and torsion in \(\pi_1(X)\) is allowed. [S3:33–37]"

## Graduate summary

**The two-step linear monodromy.** The open setting admits
nonabelian nilpotent groups. The second manuscript proves the sharp
class-two bound 

> **Theorem 1.1**
Let $V$ be a connected smooth special complex quasi-projective variety.
For every positive integer $d$ and every representation
$\rho:\pi_1(V)\to\mathrm{GL}_d(\mathbf C)$, the image $\rho(\pi_1(V))$ has a subgroup
of finite index and nilpotency class at most two. [S10:40–45]

Priority for the conclusion belongs to Cao–Deng–Hacon–Paun, who
announced it first. The proof here is independent, using the
Cadorel–Deng–Yamanoi inputs and a structural theorem about unipotent
completion 

> Cadorel–Deng–Yamanoi established virtual nilpotence of these linear
images: the identity component of their Zariski closure is a direct
product of a unipotent group and a torus
\cite[Theorem A/4.1]CDY2025. Cao–Deng–Hacon–Păun subsequently
announced the sharp class-two conclusion of Theorem 
\cite[Theorem A, equivalently Theorem 6.2]CDHP2026. Priority for that
conclusion belongs to their work. We give a different proof from the
independent CDY inputs and a structural theorem about unipotent
completion. [S10:47–55]

The bound is optimal: Cadorel–Deng–Yamanoi construct a smooth special
quasi-projective surface with a linearly two-step nilpotent
fundamental group that is not virtually abelian [S10:57–60].

**The root orbifold extension.** The third manuscript extends the
manifold abelianity theorem to order-two root orbifolds of fourfolds


> **theorem**
Assume Assumption . Let $X$ be a connected smooth projective complex fourfold and let $D\subset X$ be a nonempty smooth connected reduced divisor. If $\sqrt[2]{(X,D)}$ is special, then
$$\label{eq:target-group}
 G=\pi_1(X\setminus D,x)\big/\langle\!\langle\gamma^2\rangle\!\rangle$$
contains an abelian subgroup of finite index. Here $\gamma$ is a positively oriented meridian about $D$, transported to $x\in X\setminus D$. [S14:39–45]

The proof constructs a smooth projective eightfold $Y$ over the root
orbifold, with general fibre a product of four genus-one curves.
Specialness of the base orbifold forces specialness of $Y$, while
pullback multiplicities give the epimorphism
$\pi_1(Y)\twoheadrightarrow G$ 

> The main construction is independent of specialness. It produces a smooth projective eightfold $Y$ over $\mathcal X$ with general fibre a product of four genus-one curves. It also supplies a submersive lift at some point over the general point of _every_ base divisor. These points detect all poles in the descent of differential tensors. A direct argument then proves that specialness of $\mathcal X$ forces specialness of $Y$, while even pullback multiplicities give an epimorphism $\pi_1(Y)\twoheadrightarrow G$. These two conclusions permit the application of Assumption . [S14:49–51]

The four independent genus-one factors eliminate stabilizers over the
three-dimensional divisor. An alternative construction using branched
covers and elliptic actions is given in the appendix [S14:53].

**Consequences of the manifold theorem.** Every smooth compact
connected Kähler manifold of Kodaira dimension zero has virtually
abelian fundamental group [S3:39–55]. Campana's Conjecture S and the
bimeromorphic Iitaka uniformization follow: a special manifold with
maximal $\Gamma$-dimension, or a manifold whose universal cover is
biholomorphic to $\mathbf C^n$, has a finite cover bimeromorphic to a
torus [S3:65–121].

## History of the conjecture

Campana developed the classification program in a series of works
from the 1990s through 2011. Claudon–Horing recorded the abelianity
conjecture as Conjecture A.1 in their survey. Campana–Claudon proved
the threefold case. The compact theorem in this family is the
arbitrary-dimensional resolution.

For the open setting, Cadorel–Deng–Yamanoi established virtual
nilpotence of linear images and introduced the open-variety
specialness convention. Cao–Deng–Hacon–Paun announced the sharp
class-two conclusion. The proof here is independent and adds a
structural input on unipotent completion [S10:25–55].

For the root orbifold case, Campana's orbifold formulation records
the multiplicities of fibres and divisors. The orbifold Abelianity
Conjecture (Conjecture 12.10(1) in Campana's orbifolds paper)
predicts virtual abelianity for the fundamental group of a smooth
integral special geometric orbifold [S14:3].

## Consequences

**Campana's abelianity conjecture is resolved in all dimensions.**
Every special compact Kähler manifold has virtually abelian
$\pi_1$, with no projectivity, linearity, or residual-finiteness
hypothesis [S3:26–31].

**The Kodaira-dimension-zero case follows.** Every smooth compact
connected Kähler manifold with $\kappa(X)=0$ has virtually abelian
fundamental group [S3:39–55].

**The linear monodromy bound is class two.** Every complex
linear representation of $\pi_1(V)$ for a connected smooth special
quasi-projective variety $V$ has virtually nilpotent image of
class at most two [S10:40–45]. The bound is sharp [S10:57–60].

**The root orbifold abelianity theorem.** For a special order-two
root orbifold $\sqrt[2]{(X,D)}$ with $X$ a smooth projective
fourfold and $D$ a nonempty smooth connected divisor, the orbifold
fundamental group is virtually abelian [S14:39–45].

## Section skeleton

**Manuscript 1** [S2:36–40], 6 sections under `build/sections/`:

1. Introduction [S3]
2. Preliminaries [S4]
3. Spectral sequence [S5]
4. Hilbert scheme [S6]
5. Descent [S7]
6. Completion [S8]

**Manuscript 2** [S9:60–66], 8 sections under `build/sections/`:

1. Introduction [S10]
2. Mixed Hodge structures [S11]
3. Linear monodromy [S12]
4. Definitions [S9:60–66]
5. Specialness [S9:60–66]
6. Albanese topology [S9:60–66]
7. Composition [S9:60–66]
8. Ordinary fundamental group [S9:60–66]

**Manuscript 3** [S13:10], 3 sections plus appendix under `build/source/sections/`:

1. Introduction [S14]
2. Differentials [S15]
3. Transfer [S13:10]
4. Quadrics [S16]
5. Appendix: branched covers [S13:10]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The three manuscripts
ship 7, 9, and 9 `.tex` files respectively.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 057 at line 1481. |
| S2 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/paper.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/paper.tex) | 59 | Manuscript 1 main file: abstract and section inputs. |
| S3 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/introduction.tex) | 420 | The specialness definition, the theorem, consequences, and Campana's program context. |
| S4 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/preliminaries.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/preliminaries.tex) | 257 | Preliminaries on compact Kähler geometry. |
| S5 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/spectral.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/spectral.tex) | 857 | The spectral sequence input. |
| S6 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/hilbert.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/hilbert.tex) | 753 | The Hilbert scheme argument. |
| S7 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/descent.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/descent.tex) | 560 | The descent construction. |
| S8 | [`preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/completion.tex`](../../../preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/build/sections/completion.tex) | 615 | The completion step. |
| S9 | [`preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/main.tex`](../../../preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/main.tex) | 82 | Manuscript 2 main file: abstract and section inputs. |
| S10 | [`preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/introduction.tex`](../../../preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/introduction.tex) | 243 | The two-step theorem, prior work, and the open-variety convention. |
| S11 | [`preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/mhs.tex`](../../../preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/mhs.tex) | 223 | Mixed Hodge structure inputs. |
| S12 | [`preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/linear.tex`](../../../preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/build/sections/linear.tex) | 98 | The linear monodromy argument. |
| S13 | [`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/main.tex`](../../../preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/main.tex) | 22 | Manuscript 3 main file: abstract and section inputs. |
| S14 | [`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/introduction.tex`](../../../preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/introduction.tex) | 56 | The root orbifold theorem, the construction, and the transfer proposition. |
| S15 | [`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/differentials.tex`](../../../preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/differentials.tex) | 56 | The differential tensors and specialness transfer. |
| S16 | [`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/quadrics.tex`](../../../preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/build/source/sections/quadrics.tex) | 121 | The quadric construction of the eightfold. |
