[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 055](../../index/algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md)

# 055 — Toda's Gepner conjecture and large-volume stability

[Index page](../../index/algebraic-and-complex-geometry/055-todas-gepner-conjecture-and-large-volume-stability.md)

## Original CONTENTS.md summary

The release's blurb "**055. Gepner symmetry and large-volume stability on threefolds.** Proves Toda's Gepner conjecture for every smooth complex quintic threefold, constructing a numerical Bridgeland stability condition with the prescribed phase shift 2/5. Also constructs numerical Bridgeland stability conditions at every sufficiently large volume on all smooth projective complex threefolds with trivial canonical bundle, with the exact ordinary and square-root-Todd central charges. [S1:1404]" The first manuscript,
*A Gepner stability condition on every smooth quintic threefold* [S2],
has the abstract "We prove Toda's normalized quintic Gepner conjecture. On every smooth complex
quintic threefold, we construct a numerical Bridgeland stability condition for
which tensoring by the hyperplane bundle, followed by the spherical twist at
the structure sheaf, increases phase by $2/5$. [S3:48–51]"
The second manuscript, *Prescribed large-volume charges on threefolds
with trivial canonical bundle* [S8], has the abstract [S9:78–86]:
"Let $X$ be a smooth projective complex threefold with trivial canonical
bundle. We construct numerical Bridgeland stability conditions with the exact
ordinary and square-root-Todd central charges at every sufficiently large
volume. One volume threshold works on an open set of real twists and ample
directions. The resulting stability conditions have the support property on
the full numerical Grothendieck group and stable point sheaves. Separately, on
every smooth projective complex threefold we prove a strong tilt inequality
above a volume threshold uniform in the object and twist along a fixed
polarization. [S9:78–86]"

## Undergraduate summary

Stability conditions organize the objects of a derived category by a
complex central charge and a real phase, with finite filtrations into
semistable objects. At a Gepner point, one seeks a stability condition
compatible with a distinguished autoequivalence: the functor should
rotate the central charge and translate every semistable phase by a fixed
amount . "Stability conditions organize the objects of a derived category by a complex
central charge and a real phase, with finite filtrations into semistable
objects. Their physical antecedent is Douglas's proposal of $\Pi$-stability
for D-branes  ; Bridgeland gave the mathematical framework
used here  . At a Gepner point, one seeks a stability
condition compatible with a distinguished autoequivalence: the functor should
rotate the central charge and translate every semistable phase by a fixed
amount. We construct such a condition for every smooth quintic threefold. [S4:3–10]"

The theorem 

> **theorem**
Every smooth complex quintic threefold admits a numerical Bridgeland stability
condition $\sigma=(Z,\mathcal P)$ with the support property on $K_{\mathrm{num}}(X)_{\mathbb R}$
such that, for every $E\in\mathcal D$ and $\varphi\in\mathbb R$,
\[
 Z(\Phi E)=e^{2\pi i/5}Z(E),\qquad
 \Phi\bigl(\mathcal P(\varphi)\bigr)=\mathcal P(\varphi+2/5),\qquad
 Z(\mathcal O_x)=-1
\]
for every closed point $x\in X$. [S4:52–62]

The autoequivalence $\Phi$ is the composition of tensoring by the
hyperplane bundle with the spherical twist at the structure sheaf. The
periodicity $\Phi^5\simeq[2]$ [S5:28–35] is what makes the phase
rotation by $2/5$ consistent: applying $\Phi$ five times shifts phase by
$2$ (one full cycle), so the eigenvalue $e^{2\pi i/5}$ has order five.

## Graduate summary

**The two-perturbation strategy.** The central step is to retain two
independent perturbations of Toda's second cut. They give inequalities
controlling rank and first Chern character; the complex charge then
controls the other two numerical coordinates. The support estimate is
obtained before defining semistable objects 

> The central step is to retain two independent perturbations of Toda's second
cut. They give inequalities controlling rank and first Chern character; the
complex charge then controls the other two numerical coordinates. We obtain
this support estimate before defining semistable objects. It makes finite
refinement possible even though the image of the numerical lattice under the
charge need not be discrete. [S4:95–100]

**The uniform aisle family.** The construction tilts $\Coh(X)$ twice,
beginning at slope $-1/2$, and varies the rank and first-Chern
coefficients of the second cut over a fixed open square. Xu's stronger
Bogomolov–Gieseker inequality supplies strict margins 

> Our goal is to construct bounded aisles $U_\eta$ for which
$\Phi U_\eta\subset U_\theta$ holds uniformly with independent parameters.
We begin with Toda's proposed two tilts for the quintic Gepner charge
\cite[Sections 3.4–3.6]TodaQuintic2013, and vary the second cut in two
numerical directions. The slope estimate below supplies the strict margins
that make the comparison survive these variations.
The two first-tilt slopes $-1/2$ and $1/2$ reflect the order of the factors
in $\Phi$: tensoring by $\mathcal O_X(1)$ moves the first cut from $-1/2$ to
$1/2$, and the spherical twist will take the resulting aisle into one
constructed at $-1/2$. [S6:4–13]

The crucial conclusion is $\Phi U_\eta\subset U_\theta$ with both
parameters varying independently throughout the same square.

**From aisles to a slicing.** Simultaneous positivity in fixed middle
hearts improves the coarse nesting to a grid with spacing $1/5$, and
positivity in every perturbed preceding heart bounds the full numerical
class of each grid block by its charge 

> The decisive use of the perturbations is twofold. Simultaneous positivity
in fixed middle hearts improves the coarse nesting to a grid with spacing
$1/5$. Positivity in every perturbed preceding heart then bounds the full
numerical class of each grid block by its charge. [S7:27–30]

Each block is refined into semistable factors; support and a positive
projection of the charge bound the numerical classes of subobjects and
the length of any refinement, so maximal phases exist and refinement
stops.

**The prescribed-charge companion.** The second manuscript addresses
the prescribed-charge problem on threefolds with trivial canonical
bundle "A central charge assigns a complex number to each object of a derived
category. A stability condition organizes the objects by its argument and
requires every object to have a finite filtration by semistable factors.
Bridgeland introduced this structure and its deformation theory
 . On a projective threefold, the expected large-volume
charges are exponential expressions in the Chern character. The
prescribed-charge problem asks whether these particular expressions admit
a compatible heart, finite semistable filtrations, and a support bound
controlling the numerical classes of all semistable objects. [S10:3–11]" The theorem 

> **Theorem 1.1**
Let $X$ be a smooth projective complex threefold with
$K_X\simeq\mathcal O_X$. For any $B_*\in N^1(X)_{\mathbb R}$ and
$H_*\in\mathrm{Amp}(X)$ there are open neighborhoods $V$ of
$B_*$ and $W$ of $H_*$ and one $T>0$ such that, for all
$B\in V$, $H\in W$ and $t\geq T$, the following hold.
\beginenumerate[label=\textup{(\roman*)}]
\item $(Z_{B,tH},\mathcal A_{B,tH})$ is a geometric numerical
stability condition with support on $K_{\mathrm{num}}(X)_{\mathbb R}$.
\item There is a geometric numerical stability condition, with support
on the same full numerical space, whose charge is exactly
\[
 Z^{\mathrmLV}_B,tH(E)
 =-\int_Xe^-B-itH\ch(E)\sqrt{\td(X)},
 \qquad \sqrt{\td(X)}=1+\fracc_2(X)24.
\]
Its heart is the one constructed in Section  .
\endenumerate [S10:103–122]

Only triviality of $K_X$ is assumed; the additional vanishings in the
strict Calabi–Yau convention are unnecessary. The Todd-corrected charge
uses the heart constructed by a product-embedding route [S12].

**The uniform tilt inequality.** Separately, on every smooth projective
complex threefold (no canonical-bundle hypothesis), a strong tilt
inequality holds 

> **Theorem 1.2**
Let $X$ be a smooth projective complex threefold, $H$ an ample integral
divisor, and $B_0\in N^1(X)_{\mathbb Q}$.
There are constants $k\in\mathbb Q_{\geq0}$ and $R_*>0$, depending only on
$(X,H,B_0)$, such that every finite-slope $\nu_{a,b}$-semistable
$E\in\mathcal B_{H,B_0+bH}$ with $\nu_{a,b}(E)=0$ satisfies
$$\label{eq:intro-corrected}
 \ch_3^{B_0+bH}(E)
 \leq \left(\frac{a^2}{6}+k\right)H^2\ch_1^{B_0+bH}(E)
 \qquad(a>0,\ b\in\mathbb R).$$
For the same fixed data, the stronger bound
$$\label{eq:intro-tail}
 \ch_3^{B_0+bH}(E)
 \leq \frac{a^2}{6}H^2\ch_1^{B_0+bH}(E)$$
holds whenever $a>R_*$, for every $b\in\mathbb R$. [S10:167–184]

Both constants are independent of the rank and Chern character of $E$.
The curve class $\Gamma=kH^2$ gives the correction and satisfies
$\Gamma\cdot H\geq 0$. Beyond the threshold $R_*$ the correction
vanishes.

## History of the conjecture

Douglas proposed $\Pi$-stability for D-branes; Bridgeland gave the
mathematical framework. Toda formulated Gepner-type stability for
graded matrix factorizations and gave the normalized quintic
formulation. The functor relation $\Phi^5\simeq[2]$ and its
eigencharge are established through Orlov's equivalence and
Ballard–Favero–Katzarkov's grade-shift compatibility. The double-tilt
approach to threefold stability was developed by Bayer–Macrì–Toda.
Li established existence of numerical Bridgeland stability conditions
on every smooth quintic [S4:67–92].

The prescribed-charge problem has large-volume antecedents in Bayer's
polynomial stability conditions. Bayer–Macrì–Stellari established the
third-character inequality for abelian threefolds and Calabi–Yau
threefolds of abelian type, and developed the discriminants,
deformation and wall framework [S10:124–152]. Bernardara–Macrì–Schmidt–Zhao
proved a corrected inequality for Fano threefolds and asked for such a
correction on every polarized threefold; Martinez–Schmidt stated the
version allowing a fixed rational transverse twist [S10:191–196].

## Consequences

**Toda's normalized quintic Gepner conjecture is resolved.** Every
smooth complex quintic threefold admits a numerical Bridgeland
stability condition with the prescribed phase shift $2/5$ and
$Z(\mathcal O_x)=-1$ [S4:52–62].

**The square-root-Todd charge is realized.** For every smooth projective
complex threefold with trivial canonical bundle, there is a stability
condition whose charge is exactly
$-\int_X e^{-B-itH}\ch(E)\sqrt{\td(X)}$ on an open sector [S10:103–122].

**The corrected-inequality questions are answered affirmatively.** The
uniform strong inequality gives a curve-class correction on every
polarized threefold and a volume threshold beyond which the correction
vanishes [S10:167–184]. This answers the questions of
Bernardara–Macrì–Schmidt–Zhao and Martinez–Schmidt.

## Section skeleton

**Manuscript 1** [S3:48–51], 4 sections under `build/sections/` plus an appendix:

1. Introduction [S4]
2. Periodicity and the numerical central charge [S5:28–35]
3. A uniform family of double-tilt aisles [S6:4–13]
4. From uniform aisle inclusions to a slicing [S7:27–30]
5. Appendix: periodicity [S3:48–51]

**Manuscript 2** [S9:78–86], 8 sections under `build/`:

1. Introduction [S10]
2. Tilt stability [S11]
3. Analysis [S9:78–86]
4. Apex [S9:78–86]
5. Wall [S9:78–86]
6. Ambient construction [S12]
7. Heart [S9:78–86]
8. Counterexamples [S9:78–86]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The two manuscripts ship
5 and 9 `.tex` files respectively.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 055 at line 1404. |
| S2 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/README.md`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/README.md) | 16 | Manuscript readme: title, date. |
| S3 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/paper.tex`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/paper.tex) | 61 | The main file: abstract and section inputs. |
| S4 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/introduction.tex`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/introduction.tex) | 147 | The Gepner functor, the theorem, the prior work, and the four-stage proof roadmap. |
| S5 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/numerical.tex`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/numerical.tex) | 207 | Periodicity, the numerical lattice, and the eigencharge. |
| S6 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/aisles.tex`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/aisles.tex) | 492 | The uniform family of double-tilt aisles and the inclusion. |
| S7 | [`preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/grid.tex`](../../../preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/build/sections/grid.tex) | 647 | The nested grid, the blocks, and the support estimate. |
| S8 | [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/README.md`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/README.md) | 17 | Manuscript readme: title, date. |
| S9 | [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/main.tex`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/main.tex) | 99 | The main file: abstract and section inputs. |
| S10 | [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/01-introduction.tex`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/01-introduction.tex) | 404 | The prescribed-charge theorem and the uniform tilt inequality. |
| S11 | [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/02-tilt.tex`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/02-tilt.tex) | 366 | The tilt stability framework. |
| S12 | [`preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/06-ambient.tex`](../../../preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/build/06-ambient.tex) | 695 | The ambient product-embedding construction. |
