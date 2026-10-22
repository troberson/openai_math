Notes / Summaries / Real and complex analysis / [Family 072](../../index/real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md)

# 072 — Brennan's conjecture and a counterexample to Kraetzer's prediction

[Index page](../../index/real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md)

## Original CONTENTS.md summary

[S1:218] carries the family entry:

> Proves Brennan's conjecture: for every conformal bijection $\phi$ from a simply connected plane domain onto the disk, $|\phi'|^s$ is area-integrable for $4/3<s<4$. The sharp universal integral-means identity is $B_{\mathcal S}(t)=|t|-1$ for $t\le-2$. A strict bound $B_b(-1)<1/4$ for bounded univalent functions disproves Kraetzer's prediction at that parameter.

The entry links the two manuscripts as "Brennan’s conjecture" and "Strict
inverse-first-power bound" [S1:218].

The first manuscript's title is "Brennan's conjecture and sharp inverse-square integral means" [S2:1], dated [S2:4].

The second manuscript's title is "A strict inverse-first-power bound for univalent functions" [S13:1], dated [S13:4].

## Undergraduate summary

A **univalent map** is an injective holomorphic map. Brennan's conjecture asks
how large the derivative of a conformal map can get near a boundary.
[S4:6–8] states the question: "Brennan's conjecture asks whether, for every
conformal bijection $\varphi:W\to\DD$ from a simply connected plane domain,
the derivative satisfies" — the display that follows asks that the integral of
$|\varphi'(z)|^s$ over the domain be finite for $4/3<s<4$.

The conjecture carries no hypothesis on the domain's boundary. [S4:13–14]
says: "There is no regularity assumption on the boundary and no boundedness
assumption on $W$." The problem measures how strongly a conformal map can
compress area near an arbitrary boundary.

The first manuscript's theorem fixes the domain class. [S4:61–63] states the
hypothesis: "Let $W\subset\CC$ be any simply connected domain whose boundary
in the Riemann sphere contains at least two points. Every conformal bijection
$\varphi:W\to\DD$ satisfies" — the display gives the integral for
$4/3<s<4$. The abstract gives the same result with the sharp endpoint added:
[S3:46–50] says "We prove Brennan's conjecture: if a simply connected plane
domain admits a conformal bijection $\varphi$ onto the unit disk, then
$|\varphi'|^s$ is area-integrable for every $4/3<s<4$. We also prove the sharp
inverse-square integral-means exponent $B_{\SSS}(-2)=1$ for the normalized
schlicht class $\SSS$."

The open interval is sharp, and the Koebe function is the example that shows
it. [S4:83–83] names the example: "The Koebe function $f(z)=z/(1-z)^2$
belongs to $\SSS$ and satisfies" — the display gives its inverse-square means
growing like $(1-r)^{-1}$. [S4:89–89] gives the consequence: "Its inverse
therefore fails area integrability at both $s=4$ and $s=4/3$." So neither
endpoint can be included.

The second manuscript attacks a prediction about the bounded subclass.
[S15:29–30] names it: "Kraetzer's experiments with conformal maps onto
bounded domains led to the prediction" — the display that follows is
$B_b(-1)=1/4$. [S15:45–45] states the theorem's shape: "There exist constants
\(0<\varepsilon<1/4\) and \(C<\infty\) such that" — the display bounds the
inverse-first-power mean with exponent $-1/4+\varepsilon$. [S15:50–51] gives
the consequence: "Consequently \(B_b(-1)<1/4\), and Kraetzer's conjectured
identity \eqref{eq:kraetzer} is false." The abstract gives the same:
[S14:41–44] says "We prove a uniform upper bound for inverse-first-power
integral means of normalized univalent disk maps with exponent strictly below
\(1/4\). Consequently, the bounded universal integral-means spectrum satisfies
\(B_b(-1)<1/4\), disproving Kraetzer's conjectured spectrum at \(p=-1\)."

## Graduate summary

The first manuscript's theorem is a package, not a single inequality. The
block at [S4:52–73] carries the uniform inverse-square radial-mean estimate
with exponent $-1-\varepsilon$, the spectrum value $B_{\SSS}(-2)=1$, the
domain integrability for $4/3<s<4$, and the disk integrability for $-2<t<2/3$.
The proof runs through the weighted affine law [S8:1], compact superlevels for
almost every target [S9:1], critical points and an equivariant pairing
[S10:1], transport between saddles and maxima [S11:1], and the integrability
conclusion [S12:1], over the preliminaries and the dyadic transfer operator at
[S7:1] and the rank-pairing figure [S6:1].

The manuscript states what the sharp form does not give. [S4:75–80] says:
"That section also derives $B_{\SSS}(t)=|t|-1$ for every $t\le-2$; the
corresponding uniform radial bounds retain an arbitrary positive loss. The
radial exponent $1$ is compatible with divergence of the area integral at
$t=-2$. The other area endpoint also fails for the same classical example."

The second manuscript's theorem is stated for the unrestricted normalized
class and the consequence is drawn for the bounded spectrum. [S15:61–61]
flags the distinction: "The distinction between bounded and unrestricted disk
maps matters." The earlier estimates do not reach the target: [S15:75–77]
says "These estimates remain above the conjectured value \(1/4\);
Theorem~\ref{thm:main} establishes a uniform exponent strictly below it."

The limits of the constants are stated plainly. [S15:54–57] records them:
"Both constants are independent of the map, including its image size. The
proof gives existence of a positive gap but does not evaluate it numerically.
The conclusion concerns the inverse first power; it does not settle the
proposed value at \(p=1\)."

The two manuscripts share machinery, and the second says what it does not
import. [S15:91–93] names the shared construction: "The affine-law and
saddle-to-maximum construction is also used for inverse-square means in the
companion article" — the companion is the first manuscript. [S15:96–99]
states the separation: "We prove every inverse-first-power estimate and every
transport assertion needed here; the companion's inverse-square endpoint
theorem is not an input." The second manuscript's own engine is the compact
model and its growth operator [S17:1], the weighted affine law [S18:1],
compact superlevels [S19:1], critical points and strict pairing [S20:1],
strict weighted transport [S21:1], and the harmonic equality barrier that
produces the uniform gap [S22:1].

The scope note records what the formalization carries. [S23:10] gives the
conjecture and the formalized interval: "Brennan's conjecture asserts that
$|\phi'|^s$ is area-integrable for $4/3<s<4$ when $\phi$ conformally maps a
simply connected plane domain with nontrivial spherical boundary onto the
disk. The formalization establishes this interval, along with area
integrability of $|f'|^t$ for univalent disk maps when $-2<t<2/3$."

The scope note's second paragraph names the sharp part. [S23:12] says: "It
also gives the uniform inverse-square radial-mean bound with exponent
$-1-\varepsilon$ for every $\varepsilon>0$ and the spectrum value
$B_{\mathcal S}(-2)=1$. The Koebe map and its inverse give divergence at all
four boundary exponents."

The third paragraph carries the counterexample. [S23:14] states it:
"Kraetzer's proposed integral-means spectrum predicts $B_b(-1)=1/4$ for
bounded univalent maps. The formalized result proves $B_b(-1)<1/4$,
contradicting that prediction."

The fourth paragraph names the estimate behind the strict bound and what it
does not fix. [S23:16] says: "The underlying estimate gives constants
$0<\varepsilon<1/4$ and $C<\infty$ such that the normalized circular mean of
$|f'|^{-1}$ is at most $C(1-r)^{-1/4+\varepsilon}$ for every normalized
univalent disk map and $1/2\le r<1$. The bound requires neither bounded image
nor boundary regularity, and no numerical value of $\varepsilon$ is
specified."

The three declarations are the quantified forms. `OAI.Brennan.main_theorem`
at [S24:10] is typed `MainStatement` and assembles the uniform estimate, the
spectrum value, and both integrability clauses. `OAI.Brennan.Sharp.sharp_endpoints`
at [S25:23] is typed `SharpEndpointStatement` and carries the Koebe divergence
at the endpoints. `OAI.StrictInverseFirstPower.main` at [S26:7] is the
conjunction of the uniform strict estimate, the strict spectrum value, and the
negation of Kraetzer's identity for all exponents.

The three comparator configs state the targets the release set itself, and
each is a stub. [S27:48] carries `sorry`; [S28:37] carries `sorry`;
[S29:41] carries `sorry`. The scope note's comparator table links
`Brennan.lean`, `BrennanSharp.lean`, and `StrictMeans.lean`, one per
formalized result.

## History of the conjecture

Brennan's conjecture is dated to 1978. [S4:15–17] records it: "The conjecture
dates to Brennan's 1978 work \cite{Brennan1978}; the domain and
integral-means formulations are recorded in \cite[Chapter~3]{Bertilsson1999}."
The first manuscript's bibliography carries the 1978 paper at [S5:45] and the
Bertilsson thesis at [S5:36].

Kraetzer's prediction is stated in his own work. [S15:38–42] records where:
"The quadratic part is stated in his 1996 paper and explicitly restated in
his thesis \cite{Kraetzer,KraetzerThesis}; the full quadratic--linear
formulation also appears in Beliaev's discussion of numerical spectra
\cite{Beliaev}." The second manuscript's bibliography carries the Kraetzer
paper at [S16:1] and the thesis at [S16:13].

The boundary condition is part of the conjecture as the first manuscript
states it, and the introduction explains what it excludes: a domain whose
spherical boundary is a single point, which is the punctured disk the sharp
endpoint theorem needs.

`notes/tables/conjecture-standing.tsv` carries no row for family 072, so the
prior on Brennan's conjecture's standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

Brennan's conjecture is settled for the full class, with no boundary
regularity and no boundedness, and the open interval cannot be widened. The
Koebe function supplies the divergence at both endpoints [S4:83–83], and its
inverse fails integrability at $s=4$ and $s=4/3$ [S4:89–89].

The strict gap is proved to exist and is not evaluated. [S15:101–102] names
the hard part: "The obstacle specific to the present theorem is strictness at
the candidate exponent \(1/4\)." The scope note records the same limit for the
formalized estimate [S23:16].

The two results sit in one family because they share the integral-means
spectrum and the transport machinery, and the second manuscript states that
the first's endpoint theorem is not an input to its proof. The family carries
three comparator configs against two manuscripts, one per formalized claim.

The release's own record is source-level. The scope note says the formalized
claims exist and names their declarations; the three comparator configs carry
`sorry`; no Lean run in this repository proves any of them elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 218 |
| S2 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/README.md`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/README.md) | 17 | Manuscript 1 title, date, citation |
| S3 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/main.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/main.tex) | 62 | Abstract, lines 46–50 |
| S4 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex) | 175 | Conjecture, theorem, corollary, history, proof outline |
| S5 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/references/references.bib`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/references/references.bib) | 285 | Bibliography entries |
| S6 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/figures/rank-pairing.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/figures/rank-pairing.tex) | 21 | Rank-pairing figure |
| S7 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/01-preliminaries.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/01-preliminaries.tex) | 331 | Preliminaries and the dyadic transfer operator |
| S8 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/02-weighted-law.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/02-weighted-law.tex) | 284 | The weighted affine law |
| S9 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/03-escape.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/03-escape.tex) | 324 | Escape estimates and compact superlevels |
| S10 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/04-critical-pairing.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/04-critical-pairing.tex) | 483 | Critical points and an equivariant pairing |
| S11 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/05-transport.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/05-transport.tex) | 193 | Transport between saddles and maxima |
| S12 | [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/06-integrability.tex`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/06-integrability.tex) | 337 | Integral means and the full integrability range |
| S13 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/README.md`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/README.md) | 17 | Manuscript 2 title, date, citation |
| S14 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/main.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/main.tex) | 57 | Abstract, lines 41–44 |
| S15 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex) | 146 | Kraetzer's prediction, theorem, limits, proof outline |
| S16 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/references/references.bib`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/references/references.bib) | 170 | Bibliography entries |
| S17 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/01-compact-model.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/01-compact-model.tex) | 152 | The compact model and its growth operator |
| S18 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/02-weighted-law.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/02-weighted-law.tex) | 126 | The weighted affine law |
| S19 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/03-escape.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/03-escape.tex) | 149 | Compact superlevels for almost every target |
| S20 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/04-strict-pairing.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/04-strict-pairing.tex) | 270 | Critical points and strict pairing |
| S21 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/05-strict-transport.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/05-strict-transport.tex) | 118 | Strict weighted transport |
| S22 | [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/06-equality-barrier.tex`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/06-equality-barrier.tex) | 54 | The harmonic equality barrier and the uniform gap |
| S23 | [`lean/docs/072.md`](../../../lean/docs/072.md) | 24 | Scope note |
| S24 | [`lean/OAI/Analysis/IntegralMeans/Main.lean`](../../../lean/OAI/Analysis/IntegralMeans/Main.lean) | 24 | `Brennan.main_theorem` |
| S25 | [`lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean`](../../../lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean) | 33 | `Brennan.Sharp.sharp_endpoints` |
| S26 | [`lean/OAI/Analysis/StrictMeans/Main.lean`](../../../lean/OAI/Analysis/StrictMeans/Main.lean) | 18 | `StrictInverseFirstPower.main` |
| S27 | [`lean/ComparatorChallenges/Brennan.lean`](../../../lean/ComparatorChallenges/Brennan.lean) | 53 | Stub, `sorry` at line 48 |
| S28 | [`lean/ComparatorChallenges/BrennanSharp.lean`](../../../lean/ComparatorChallenges/BrennanSharp.lean) | 44 | Stub, `sorry` at line 37 |
| S29 | [`lean/ComparatorChallenges/StrictMeans.lean`](../../../lean/ComparatorChallenges/StrictMeans.lean) | 45 | Stub, `sorry` at line 41 |

## Bibliography

**25 entries** from `references.bib`:
- Aleman, Alexandru, Kouroupis, Athanasios. *{Brennan}'s conjecture holds for semigroups of holomorphic functions*. (2025) [AlemanKouroupis2025]
- Beliaev, Dmitri, Smirnov, Stanislav. *Random conformal snowflakes*. (2010) [BeliaevSmirnov2010]
- Bertilsson, Daniel. *Coefficient estimates for negative powers of the derivative of univalent functions*. (1998) [Bertilsson1998]
- Bertilsson, Daniel. *On {Brennan}'s conjecture in conformal mapping*. (1999) [Bertilsson1999]
- Brennan, James E.. *The Integrability of the Derivative in Conformal Mapping*. (1978) [Brennan1978]
- Brennan, James E.. *2.6. On the integrability of the derivative of conformal mapping*. (1978) [Brennan1978LOMI]
- Carleson, Lennart, Makarov, Nikolai G.. *Some results connected with {Brennan}'s conjecture*. (1994) [CarlesonMakarov1994]
- Duren, Peter L.. *Univalent Functions*. (1983) [Duren1983]
- Folland, Gerald B.. *Real Analysis: Modern Techniques and Their Applications*. (1999) [Folland1999]
- Gentner, Daniel, Last, G{\"u}nter. *Palm pairs and the general mass-transport principle*. (2011) [GentnerLast2011]
- … and 15 more

**15 entries** from `references.bib`:
- Kraetzer, Philipp. *Experimental bounds for the universal integral means spectrum of conformal maps*. (1996) [Kraetzer]
- Kraetzer, Philipp. *Algorithmische Methoden der konformen Abbildungen auf fraktale Gebiete*. (2000) [KraetzerThesis]
- Carleson, Lennart, Jones, Peter W.. *On coefficient problems for univalent functions and conformal dimension*. (1992) [CJ]
- Makarov, Nikolai G.. *Fine structure of harmonic measure*. (1999) [Makarov]
- Hedenmalm, H{\aa}kan, Shimorin, Serguei. *Weighted {Bergman} spaces and the integral means spectrum of conformal mappings*. (2005) [HedenmalmShimorin]
- Beliaev, Dmitri, Smirnov, Stanislav. *Random conformal snowflakes*. (2010) [BeliaevSmirnov]
- Beliaev, Dmitri. *Integral means spectrum of random conformal snowflakes*. (2008) [Beliaev]
- Sola, Alan. *An Estimate of the Universal Means Spectrum of Conformal Mappings*. (2006) [Sola]
- Folland, Gerald B.. *Real Analysis: Modern Techniques and Their Applications*. (1999) [Folland]
- Duren, Peter L.. *Univalent Functions*. (1983) [Duren]
- … and 5 more
