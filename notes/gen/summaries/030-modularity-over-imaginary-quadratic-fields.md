[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 030](../index/number-theory/030-modularity-over-imaginary-quadratic-fields.md)

# 030 — Modularity over imaginary quadratic fields

[Index page](../index/number-theory/030-modularity-over-imaginary-quadratic-fields.md)

## Original CONTENTS.md summary

The release's blurb "**030. Modularity of elliptic curves over imaginary quadratic fields.** Proves the modularity conjecture for elliptic curves over imaginary quadratic fields: every elliptic curve over every imaginary quadratic field is modular, with matching local parameters at every place. [S1:723]" The catalog abstract 
restates it: "Proves the modularity conjecture for elliptic curves over imaginary quadratic fields: every elliptic curve over every imaginary quadratic field is modular, with matching local parameters at every place. [S2:136]" The manuscript's title is "Modularity of elliptic curves over imaginary quadratic fields [S3:1]" , and
its abstract reads: "We prove the modularity conjecture for elliptic curves over imaginary
quadratic fields: every such curve is modular, with matching local
parameters at every place. [S4:74–76]"

## Undergraduate summary

The theorem [S5:15–38] says: for every imaginary quadratic field $K$
and every elliptic curve $E/K$, there is an automorphic representation
$\pi_E$ of $\mathrm{GL}_2(\mathbb A_K)$ whose local parameters match the $\ell$-adic
cohomology of $E$ at every place, and $L(E/K,s)=L(\pi_E,s-1/2)$.

> **theorem**
Let $K$ be an imaginary quadratic number field and $E/K$ an elliptic
curve. There is an isobaric automorphic representation $\pi_E$ of
$\mathrm{GL}_2(\mathbb A_K)$ with trivial central character and weight zero such that,
for every prime $l$ and every isomorphism
$\iota:\overline\mathbb Q_l\xrightarrow{\sim}\mathbb C$,
$$r_\iota(\pi_E)\simeq
 H^1_{\mathrm{\acute et}}(E_{\overline K},\overline\mathbb Q_l).$$
At every finite place $v\nmid l$ one has
$$\iota\mathrm{WD}\bigl(H^1_{\mathrm{\acute et}}(E_{\overline K},\overline\mathbb Q_l)
                     |_{G_{K_v}}\bigr)^{\mathrm{F\text{-}ss}}
 \simeq
 \mathrm{rec}_{K_v}\bigl(\pi_{E,v}\otimes|\det|_v^{-1/2}\bigr).$$
The unitary parameter at the complex place is
$z\mapsto\mathrm{diag}(z/|z|,\overline z/|z|)$.
In particular every local factor agrees, and
$$L(E/K,s)=L(\pi_E,s-1/2).$$
If $E$ has no complex multiplication, $\pi_E$ is cuspidal. In the CM
case it is given by automorphic induction of a Hecke character, or by
an isobaric sum when the CM field is already $K$. [S5:15–38]

If $E$ has no complex multiplication, $\pi_E$ is cuspidal. In the CM
case it is given by automorphic induction of a Hecke character.

## Graduate summary

**The method: a geometric prime switch.** Over $\mathbb Q$, modularity was
proved by lifting automorphy from a residual Galois representation,
using Wiles's $3$--$5$ switch . "Over $\mathbb Q$, Wiles and Taylor–Wiles proved modularity of semistable
elliptic curves , and
Breuil–Conrad–Diamond–Taylor proved modularity of every elliptic
curve . A central method is to lift automorphy from a residual
Galois representation. [S5:60–64]" Over imaginary
quadratic fields, the potential automorphy theorem of ACC gives
potential modularity (after extending the ground field) [S5:82–86].
"The potential automorphy theorem of
Allen–Calegari–Caraiani–Gee–Helm–Le Hung–Newton–Scholze–Taylor–Thorne
implies potential modularity of every elliptic curve over a CM
field \cite[Theorem 1.0.1]ACC. Boxer–Calegari–Gee–Pilloni also proved
potential modularity for genus-one curves over quadratic extensions of
totally real fields \cite[Theorem 1.1.4]BCGP. [S5:82–86]" Caraiani–Newton's lifting theorem removes most restrictions
but leaves the rank-zero condition on $X_0(15)(K)$ [S5:94–98].
"Their results give modularity under suitable residual-image hypotheses
in characteristic $3$ or $5$, modularity for $100\%$ of Weierstrass
equations, ordered by height, over each Galois CM field not containing $\zeta_5$, and
modularity of every elliptic curve over an imaginary quadratic field
$K$ for which $X_0(15)(K)$ has rank zero
\cite[Theorem 6.1 and Corollaries 6.1.2 and 7.1.2]CN. [S5:94–98]" The theorem removes that last restriction.

**The construction.** For a non-CM curve $E/K$, the proof builds a
family of genus-$n$ cyclic covers $C_n(t)$ of quadratic twists of $E$,
branched at two points. The cohomology $H^1(C_n(t))$ decomposes into
rank-two character pieces $V_\theta$ that form a congruence chain


> Choose characters $\eta$ and $\psi$ of orders $3$ and $p$, respectively,
and set $\chi=\eta\psi$. The order-three system $V_\eta$ comes from an
elliptic curve $A/F$, while $V_1=H^1(B_t)$. An integral description of the
cohomology gives the chain
$$\underbrace{V_\eta}_{H^1(A)}
 \ \equiv\!\!\pmod p\ \ V_\chi
 \ \equiv\!\!\pmod 3\ \ V_\psi
 \ \equiv\!\!\pmod p\ \ \underbrace{V_1}_{H^1(B_t)}.$$ [S5:116–126]

Automorphy propagates from left to right along the chain: the
order-three piece $V_\eta$ comes from an elliptic curve (so it is
modular by the classical result), and each congruence step preserves
the property. Two degenerations of the covers supply the local
conditions: the compact-type degeneration gives a free group-ring
description controlling simultaneous local reduction, and the
vanishing-cycle degeneration gives irreducibility in residual
characteristics $3$, $5$, and $p$ [S7] [S8].

**The descent.** After the three lifts (mod $3$, mod $p$, and the
final $p$-adic lift), automorphy descends from $F=K(\mu_{3p})$ to $K$
via the CM-field lifting theorem of Caraiani–Newton [S13]. The CM case
is handled by automorphic induction [S5:15–38].

## History of the conjecture

The arithmetic groups for imaginary quadratic fields originate in
Bianchi's work; their cohomology was developed by Swan and Harder
[S5:42–46]. Langlands explicitly discussed the automorphy of local
representations attached to elliptic curves [S5:48–52]. Cremona and
Whitley developed substantial computations relating elliptic curves
and automorphic forms over these fields [S5:53–55].

Over $\mathbb Q$, the modularity theorem was proved by Wiles,
Taylor–Wiles, and Breuil–Conrad–Diamond–Taylor . "Over $\mathbb Q$, Wiles and Taylor–Wiles proved modularity of semistable
elliptic curves , and
Breuil–Conrad–Diamond–Taylor proved modularity of every elliptic
curve . A central method is to lift automorphy from a residual
Galois representation. [S5:60–64]"
The central method is lifting from a residual representation, with
Wiles's $3$--$5$ switch providing the geometric mechanism.

Over CM fields, the potential automorphy theorem (ACC) and
Calegari–Geraghty patching give potential modularity [S5:82–86].
"The potential automorphy theorem of
Allen–Calegari–Caraiani–Gee–Helm–Le Hung–Newton–Scholze–Taylor–Thorne
implies potential modularity of every elliptic curve over a CM
field \cite[Theorem 1.0.1]ACC. Boxer–Calegari–Gee–Pilloni also proved
potential modularity for genus-one curves over quadratic extensions of
totally real fields \cite[Theorem 1.1.4]BCGP. [S5:82–86]" Caraiani–Newton's lifting theorem handles most cases
but leaves the rank-zero condition . "Their results give modularity under suitable residual-image hypotheses
in characteristic $3$ or $5$, modularity for $100\%$ of Weierstrass
equations, ordered by height, over each Galois CM field not containing $\zeta_5$, and
modularity of every elliptic curve over an imaginary quadratic field
$K$ for which $X_0(15)(K)$ has rank zero
\cite[Theorem 6.1 and Corollaries 6.1.2 and 7.1.2]CN. [S5:94–98]"
Theorem~\ref{thm:main} removes that restriction.

## Consequences

**Full modularity, no restrictions.** Every elliptic curve over every
imaginary quadratic field is modular, with matching local parameters
at every place. The $L$-function equality $L(E/K,s)=L(\pi_E,s-1/2)$
holds unconditionally. In the non-CM case, $\pi_E$ is cuspidal; in the
CM case it is automorphic induction of a Hecke character [S5:15–38].

**Reusable geometric machinery.** The local constancy argument and the
two-conjugate specialization argument are formulated separately from
the automorphy application, so they can be used independently
. "The feature developed here is the combination for a _prescribed_
elliptic curve: the character orders $1,p,3p,3$ occur in one integral
cohomology lattice, an elliptic curve occurs at each end of the chain,
and the compact-type degeneration and simultaneous residual specialization
make every step applicable to the CM-field lifting theorem. The local
constancy argument and the two-conjugate specialization argument are
formulated separately, so they can be used independently of the final
automorphy application. [S5:183–189]"

## Section skeleton

**Main file** [S4:74–76], 8 sections under `build/sections/`:

1. Introduction [S5]
2. Galois and automorphic conventions [S6]
3. Cyclic covers and two degenerations [S7]
4. Integral homology and explicit monodromy [S8]
5. Rank-two systems and integral congruences [S9]
6. Automorphy inputs and the remaining specialization conditions [S10]
7. Prescribing the local reduction type [S11]
8. One specialization with all residual properties [S12]
9. Propagation of automorphy and descent [S13]

Bibliography: `references.bib` [S14].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
9 `.tex` files under `build/sections/` plus 2 figure files.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 030 at line 723. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 136. |
| S3 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/README.md`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S4 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/main.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/main.tex) | 89 | The main file: the abstract, packages, and section inputs. |
| S5 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/introduction.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/introduction.tex) | 199 | The main theorem, the historical context, the geometric prime switch, and the proof organization. |
| S6 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/conventions.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/conventions.tex) | 48 | Galois and automorphic conventions. |
| S7 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/geometry.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/geometry.tex) | 262 | Cyclic covers and two degenerations. |
| S8 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/monodromy.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/monodromy.tex) | 218 | Integral homology and explicit monodromy. |
| S9 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/systems.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/systems.tex) | 285 | Rank-two systems and integral congruences. |
| S10 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/automorphy-inputs.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/automorphy-inputs.tex) | 119 | Automorphy inputs and the remaining specialization conditions. |
| S11 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/local.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/local.tex) | 372 | Prescribing the local reduction type. |
| S12 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/residual.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/residual.tex) | 343 | One specialization with all residual properties. |
| S13 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/automorphy.tex`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/sections/automorphy.tex) | 254 | Propagation of automorphy and descent. |
| S14 | [`preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/references.bib`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/build/references.bib) | 445 | The bibliography. |

## Bibliography

- , Groupes de monodromie en géométrie algébrique. II (SGA 7 II) (1973)
- Allen, Patrick B., Calegari, Frank, Caraiani, Ana, Gee, Toby, Helm, David, Le Hung, Bao V., Newton, James, Scholze, Peter, Taylor, Richard, Thorne, Jack A., Potential automorphy over CM fields (2023)
- Allen, Patrick B., Khare, Chandrashekhar, Thorne, Jack A., Modularity of $\mathrm{GL}_2(\mathbb{F}_p)$-representations over CM fields (2023)
- Arthur, James, Clozel, Laurent, Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula (1989)
- Berger, Tobias, Harcos, Gergely, $l$-adic representations associated to modular forms over imaginary quadratic fields (2007)
- Bianchi, Luigi, Sui gruppi di sostituzioni lineari con coefficienti appartenenti a corpi quadratici immaginar{\^ı} (1892)
- Bloch, Spencer, Kato, Kazuya, $L$-functions and Tamagawa numbers of motives (1990)
- Bosch, Siegfried, Lütkebohmert, Werner, Raynaud, Michel, Néron Models (1990)
- Boxer, George, Calegari, Frank, Gee, Toby, Pilloni, Vincent, Abelian surfaces over totally real fields are potentially modular (2021)
- Breuil, Christophe, Conrad, Brian, Diamond, Fred, Taylor, Richard, On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises (2001)
- Calegari, Frank, Geraghty, David, Modularity lifting beyond the Taylor–Wiles method (2018)
- Caraiani, Ana, Newton, James, On the modularity of elliptic curves over imaginary quadratic fields (2025)
- Coleman, Robert, Iovita, Adrian, The Frobenius and monodromy operators for curves and abelian varieties (1999)
- Cremona, John E., Hyperbolic tessellations, modular symbols, and elliptic curves over complex quadratic fields (1984)
- Cremona, John E., Whitley, E., Periods of cusp forms and elliptic curves over imaginary quadratic fields (1994)
- Darmon, Henri, Modularity of fibres in rigid local systems (1999)
- Darmon, Henri, Rigid local systems, Hilbert modular forms, and Fermat's Last Theorem (2000)
- Darmon, Henri, Mestre, Jean-François, Courbes hyperelliptiques {\`a} multiplications réelles et une construction de Shih (2000)
- Ellenberg, Jordan S., Endomorphism algebras of Jacobians (2001)
- Faltings, Gerd, Endlichkeitssätze für abelsche Varietäten über Zahlkörpern (1983)
- Geraghty, David, Modularity lifting theorems for ordinary Galois representations (2019)
- Grothendieck, Alexandre, Raynaud, Michel, Rim, Dock Sang, Groupes de monodromie en géométrie algébrique. I (SGA 7 I) (1972)
- Grunewald, Fritz, Helling, Hermann, Mennicke, Jens, $\mathrm{SL}_2$ over complex quadratic number fields. I (1978)
- Harder, Günter, Eisenstein cohomology of arithmetic groups. The case $\mathrm{GL}_2$ (1987)
- Harris, Michael, Lan, Kai-Wen, Taylor, Richard, Thorne, Jack, On the rigid cohomology of certain Shimura varieties (2016)
- Harris, Michael, Soudry, David, Taylor, Richard, $l$-adic representations associated to modular forms over imaginary quadratic fields. I. Lifting to $\mathrm{GSp}_4(\mathbb{Q})$ (1993)
- Langlands, Robert P., Problems in the theory of automorphic forms (1970)
- Langlands, Robert P., Base Change for $\mathrm{GL}(2)$ (1980)
- Mestre, Jean-François, Familles de courbes hyperelliptiques {\`a} multiplications réelles (1991)
- Scholze, Peter, On torsion in the cohomology of locally symmetric varieties (2015)
- Serre, Jean-Pierre, Propriétés galoisiennes des points d'ordre fini des courbes elliptiques (1972)
- Serre, Jean-Pierre, Topics in Galois Theory (2008)
- Shimura, Goro, Taniyama, Yutaka, Complex Multiplication of Abelian Varieties and Its Applications to Number Theory (1961)
- Swan, Richard G., Generators and relations for certain special linear groups (1971)
- Tautz, Walter, Top, Jaap, Verberkmoes, Alain, Explicit hyperelliptic curves with real multiplication and permutation polynomials (1991)
- Taylor, Richard, Wiles, Andrew, Ring-theoretic properties of certain Hecke algebras (1995)
- Taylor, Richard, $l$-adic representations associated to modular forms over imaginary quadratic fields. II (1994)
- Taylor, Richard, Remarks on a conjecture of Fontaine and Mazur (2002)
- Tsuji, Takeshi, $p$-adic étale cohomology and crystalline cohomology in the semi-stable reduction case (1999)
- Varma, Ila, Local-global compatibility for regular algebraic cuspidal automorphic representations when $\ell\ne p$ (2024)
- Wiles, Andrew, Modular elliptic curves and Fermat's Last Theorem (1995)
