[Notes](../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 209](../index/algebra/209-integral-counterexamples-to-gerstens-conjecture.md)

# 209 — Integral counterexamples to Gersten’s conjecture

[Index page](../index/algebra/209-integral-counterexamples-to-gerstens-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4764] and the catalog abstract [S2:499] state
the family's claim: unrestricted integral Gersten injectivity fails in
degrees 3 and 5. Two explicit two-dimensional ramified regular local
rings of mixed characteristic $(0,5)$ have nonzero integral
$K$-theory classes that vanish over their fraction fields. The
degree-five manuscript's abstract "We construct a two-dimensional ramified regular local ring $A$ of mixed
characteristic $(0,5)$ for which $K_5(A)\to K_5(\Frac A)$ has a nonzero
kernel. This disproves Gersten's conjecture in its unrestricted integral
form. [S3:44–49]" The degree-three
manuscript's abstract "We construct a two-dimensional ramified regular local ring $A$ in mixed
characteristic $(0,5)$ for which the integral map
$K_3(A)\to K_3(\Frac A)$ has nonzero kernel. This gives a negative
answer to the unrestricted integral Gersten conjecture. [S5:30–35]"

## Undergraduate summary

In algebraic $K$-theory, Gersten's conjecture asserts that for a
regular local domain $A$ with fraction field $F$, the residue complex
$K_n(A) \to K_n(F) \to \bigoplus_{\mathfrak{p}} K_{n-1}(\kappa(\mathfrak{p})) \to \cdots$
is exact. The first map—the inclusion of $K_n(A)$ into $K_n(F)$—is
the injectivity question: a class that dies in the fraction field must
already be zero. The conjecture is known in equicharacteristic
setting (Panin) and in smooth-over-DVR cases with finite coefficients
(Geisser–Levine, Skalit), but the unrestricted integral mixed-characteristic
case was open [S4:5–16]. The degree-five manuscript constructs an
explicit counterexample 

> **theorem**
Let $V$ be the ring of integers in the unramified extension of $\mathbb Q_5$ of
degree eight, and put
\[
 A=\bigl(V[x,y]/(5+x^4+y^4)\bigr)_(5,x,y).
\]
Then $A$ is a Noetherian regular local domain of dimension two and
\[
 \ker\bigl(K_5(A)\longrightarrow K_5(\Frac A)\bigr)\ne0.
\]
Consequently the unrestricted integral Gersten conjecture has a negative
answer. [S4:18–30]

The ring is $A = (V[x,y]/(5+x^4+y^4))_{(5,x,y)}$ where $V$ is the
ring of integers in the unramified degree-eight extension of $\mathbb{Q}_5$.
The degree-three companion constructs a different ring—the local ring
at a point of a projective hypersurface over the cyclotomic
$\mathbb{Q}_5(\zeta_5)$—with a nonzero class in $K_3(A)$ that vanishes
in $K_3(\mathrm{Frac} A)$ 

> **Theorem 1.1**
The ring $A$ is a two-dimensional Noetherian regular local domain
of mixed characteristic $(0,5)$, with $\pi\in\mathfrak m_A^2$.
There is an integral class $c\in K_3(A)$ such that
\[
 c|_{\Frac A}=0,
 \qquad
 c|_{A[1/\pi]}\bmod5\ne0
 \quadin G_3(A[1/\pi];\mathbb Z/5).
\]
In particular, $K_3(A)\to K_3(\Frac A)$ is not injective. [S6:29–40]

## Graduate summary

**The degree-five construction.** The ring is chosen so that
$5 \in (x,y)^4$, making it ramified and outside the unramified and
smooth-over-$V$ settings where positive results hold. The proof
proceeds through a cyclotomic coefficient class in $K_4$ that lifts
to integral $K_5$ via a vanishing result, with two Bott factors
contributing the square of the cyclotomic character. The signs are
realized by an elliptic quotient of the Fermat quartic [S4:100–157].

**The degree-three construction.** The ring is the local ring at
$[0:0:1]$ on the hypersurface
$(X-Z)^5 - XY^4 + Y^5 + \zeta Z^5 = 0 \subset \mathbb{P}^2_V$
over $V = \mathcal{O}_{\mathbb{Q}_5(\zeta)}$ with uniformizer
$\pi = 1 - \zeta$. The class $c$ is detected nontrivially after
restriction to $A[1/\pi]$ and reduction mod 5 in coherent
$K$-theory, while its restriction to the fraction field vanishes
[S6:112–166].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

Gersten formulated the questions in 1973; Quillen proved the conjecture
for semilocalizations of finite-type algebras over a field at regular
primes. Panin established the full equicharacteristic case. In mixed
characteristic, Gillet–Levine's relative theorem reduces the smooth
local case to the DVR case, and Geisser–Levine prove finite-coefficient
exactness for essentially smooth local rings over a DVR. Skalit proves
finite-coefficient exactness for unramified regular local rings.
Feld's finite-coefficient example is the closest methodological
predecessor: a degree-two augmentation kernel at a ramified regular
local ring whose integral $K_2$ map is injective [S4:39–97]. The two
companion manuscripts close the unrestricted integral case in degrees
3 and 5 [S6:50–108].

## Consequences

**The unrestricted integral Gersten conjecture is false in degrees 3
and 5.** The two counterexamples show that the injectivity of
$K_n(A) \to K_n(\mathrm{Frac} A)$ fails for $n = 3$ and $n = 5$
at ramified regular local rings of mixed characteristic $(0,5)$.
The positive results in the unramified and smooth-over-DVR cases
remain valid; the counterexamples sit precisely outside those
settings [S4:18–30, S6:29–40].

**The construction method is reusable.** Both papers use a
cyclotomic-coefficient-lift strategy: find a coefficient class that
lifts to an integral class, then show the integral class dies in the
fraction field. The degree-five paper's vanishing result for integral
$K_4$ and the degree-three paper's detection via coherent $K$-theory
mod 5 are general tools [S4:100–157, S6:112–166].

## Section skeleton

**Degree-five manuscript** [S3:44–49], 6 sections under `build/source/sections/`:
introduction [S4:18–30], coefficients, arithmetic, specialization, geometry,
main-proof. Plus an appendix (claimed-vanishing). Its root is
`build/source/main.tex`, with a `references.bib` bibliography [S7].

**Degree-three manuscript** [S5:30–35], 5 sections under `build/sections/`:
introduction [S6:29–40], model, integral-class, field, detection. Its root
is `build/main.tex`, with a `refs/sources.bib` bibliography [S8].

Neither manuscript ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's results is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships two LaTeX
manuscripts — 8 `.tex` files in the degree-five `build/source/` and
6 in the degree-three `build/` — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | The release's blurb for family 209 at line 4764. |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The catalog abstract at line 499. |
| S3 | [`preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/main.tex`](../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/main.tex) | 63 | Degree-five manuscript main file: title and abstract. |
| S4 | [`preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/sections/introduction.tex`](../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/sections/introduction.tex) | 157 | Degree-five manuscript introduction: main theorem, history, and the construction guide. |
| S5 | [`preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/main.tex`](../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/main.tex) | 43 | Degree-three manuscript main file: title and abstract. |
| S6 | [`preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/sections/introduction.tex`](../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/sections/introduction.tex) | 166 | Degree-three manuscript introduction: main theorem, context, and the proof route. |
| S7 | [`preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/references.bib`](../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/build/source/references.bib) | 375 | Degree-five manuscript bibliography. |
| S8 | [`preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/refs/sources.bib`](../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/refs/sources.bib) | 141 | Degree-three manuscript bibliography. |

## Bibliography

- The Stacks Project Authors, The Stacks Project (2026)
- Clausen, Dustin, Mathew, Akhil, Morrow, Matthew, $K$-theory and topological cyclic homology of henselian pairs (2021)
- Druzhinin, Andrei E., Gersten conjecture for $K$-theory on Henselian schemes and $\phi$-motivic localisation (2025)
- Druzhinin, Andrei E., Gersten conjecture for $K$-theory on Henselian schemes and $\varphi$-motivic localisation (2025)
- Feld, Niels, Finite-coefficient Gersten injectivity fails in ramified mixed characteristic (2026)
- Feld, Niels, Finite-coefficient Gersten injectivity fails in ramified mixed characteristic (2026)
- Flynn, E. Victor, Wetherell, Joseph L., Covering collections and a challenge problem of Serre (2001)
- Friedlander, Eric M., Suslin, Andrei, The spectral sequence relating algebraic $K$-theory to motivic cohomology (2002)
- Friedlander, Eric M., Suslin, Andrei, The spectral sequence relating algebraic $K$-theory to motivic cohomology (2002)
- Gabber, Ofer, $K$-theory of Henselian local rings and Henselian pairs (1992)
- Geisser, Thomas, Levine, Marc, The $K$-theory of fields in characteristic $p$ (2000)
- Geisser, Thomas, Levine, Marc, The $K$-theory of fields in characteristic $p$ (2000)
- Gersten, S. M., Problems about higher $K$-functors (1973)
- Gersten, S. M., Some exact sequences in the higher $K$-theory of rings (1973)
- Gersten, S. M., Problems about higher $K$-functors (1973)
- Gillet, Henri, Levine, Marc, The relative form of Gersten's conjecture over a discrete valuation ring: The smooth case (1987)
- Gillet, Henri, Levine, Marc, The relative form of Gersten's conjecture over a discrete valuation ring: The smooth case (1987)
- Harari, David, Étale cohomology and Brauer group (2023)
- Matsumoto, Hideya, Sur les sous-groupes arithmétiques des groupes semi-simples déployés (1969)
- Matsumoto, Hideya, Sur les sous-groupes arithmétiques des groupes semi-simples déployés (1969)
- Milne, J. S., Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field (2022)
- Milne, J. S., Algebraic Number Theory (2020)
- Milne, J. S., Class Field Theory (2020)
- Mochizuki, Satoshi, Local Gersten's conjecture for regular system of parameters (2020)
- OpenAI, An integral degree-three Gersten counterexample (2026)
- OpenAI, An integral counterexample to Gersten's conjecture (2026)
- Panin, I. A., The equicharacteristic case of the Gersten conjecture (2003)
- Panin, I. A., The equicharacteristic case of the Gersten conjecture (2003)
- Quillen, Daniel, On the cohomology and $K$-theory of the general linear groups over a finite field (1972)
- Quillen, Daniel, Higher algebraic $K$-theory: I (1973)
- Quillen, Daniel, Finite generation of the groups $K_i$ of rings of algebraic integers (1973)
- Quillen, Daniel, Higher algebraic $K$-theory: I (1973)
- Quillen, Daniel, On the cohomology and $K$-theory of the general linear groups over a finite field (1972)
- Sherman, C. C., The $K$-theory of an equicharacteristic discrete valuation ring injects into the $K$-theory of its field of quotients (1978)
- Silverman, Joseph H., The Arithmetic of Elliptic Curves (2009)
- Skalit, C., Regular morphisms and Gersten's conjecture (2017)
- Skalit, C., Regular morphisms and Gersten's conjecture (2017)
- Soulé, Christophe, Éléments cyclotomiques en $K$-théorie (1987)
- Suslin, A., On the $K$-theory of algebraically closed fields (1983)
- Suslin, A., On the $K$-theory of local fields (1984)
- Suslin, A. A., On the Grayson spectral sequence (2003)
- Suslin, Andrei, Voevodsky, Vladimir, Bloch–Kato conjecture and motivic cohomology with finite coefficients (2000)
- Suslin, A. A., On the Grayson spectral sequence (2003)
- Voevodsky, Vladimir, On motivic cohomology with $\mathbf{Z}/l$-coefficients (2011)
- Voevodsky, Vladimir, On motivic cohomology with $\mathbf{Z}/l$-coefficients (2011)
- Weibel, Charles A., The $K$-book: An introduction to algebraic $K$-theory (2013)
- Weibel, Charles A., The norm residue isomorphism theorem (2009)
- Weibel, Charles A., The $K$-book: An introduction to algebraic $K$-theory (2013)
