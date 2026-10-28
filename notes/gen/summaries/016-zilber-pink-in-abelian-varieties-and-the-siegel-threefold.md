[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 016](../index/number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md)

# 016 — Zilber–Pink in abelian varieties and the Siegel threefold

[Index page](../index/number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md)

## Original CONTENTS.md summary

The release entry for the family is two sentences, and the second is quoted here in full "It also proves the full curve case in the Siegel threefold [S1:445]". The entry names four manuscripts; the triage record files the family as a four-paper resolution [S22:129–130], and the release overview carries the same entry with the four manuscript links [S2:108].

The abelian manuscript's blurb 

> Every irreducible subvariety of an abelian variety has only finitely many maximal atypical subvarieties, where atypicality is measured inside its smallest containing torsion coset. [S1:454]

The E×CM manuscript's blurb 

> Each such curve contains only finitely many points whose abelian surface is isogenous to a product of elliptic curves with at least one factor having complex multiplication. [S1:463]

The quaternionic manuscript's blurb 

> A Hodge-generic algebraic curve contains only finitely many points whose full geometric rational endomorphism algebra is an indefinite quaternion division algebra over ℚ. No boundary or reduction hypothesis is required. [S1:472]

The elliptic-square manuscript's blurb 

> We prove that every Hodge-generic algebraic curve in $`\mathcal A_2`$ over $`\overline{\mathbb Q}`$ contains only finitely many points whose abelian surface is isogenous to the square of an elliptic curve without complex multiplication (CM). Combining this result with the companion $`E\times\mathrm{CM}`$ and quaternionic-division finiteness theorems, we prove the curve case of Zilber–Pink in $`\mathcal A_2`$ over $`\overline{\mathbb Q}`$, without a boundary hypothesis. [S1:481]

## Undergraduate summary

One conjecture, four shapes. Zilber and Pink predicted, in two settings, that an algebraic variety inside a rich ambient space cannot meet the "special" locus more often than a dimension count allows. Manuscript A works inside an abelian variety, where the special loci are torsion cosets — abelian subvarieties translated by torsion points. Manuscripts B, C and D work inside $\mathcal A_2$, the three-dimensional moduli space of principally polarized abelian surfaces, where the special loci of dimension one are curves parametrizing surfaces with extra endomorphisms. In both settings the question is the same: intersect a Hodge-generic object with every special locus of small dimension, allowing all of them to vary, and ask whether what you get is finite.

The abelian case is the older one. Its zero-dimensional version is the Manin–Mumford theorem, proved by Raynaud: a subvariety of an abelian variety containing densely many torsion points is itself a torsion coset. Allowing the torsion cosets to have positive dimension makes the intersections larger than the dimension count predicts, and those excess intersections are the "atypical" ones. The claim this manuscript makes is about the *maximal* atypical pieces, which is the right unit: a positive-dimensional atypical intersection can sit inside a bigger one.

The Siegel case splits by what the extra endomorphisms look like. An abelian surface whose rational endomorphism algebra is as small as possible is a product of two non-CM elliptic curves; the *elliptic square* locus is the case where the two factors are isogenous to each other. The three generic types of special curve in $\mathcal A_2$ are products with a CM factor, non-CM elliptic squares, and surfaces with quaternion multiplication. Manuscripts B, C and D each take one of the three, and manuscript D then assembles all three into the full curve case.

**The shape of the argument, in both settings, is a contradiction built from a hypothetical infinite sequence.** Take a sequence of intersection points that is generic in the ambient variety. Arithmetic gives a lower bound on how large the Galois orbit of each point must be, because a point with many endomorphisms has many conjugates. Geometry, via o-minimal counting of rational points in definable sets, gives an upper bound that is much smaller once the height is controlled. The two bounds are compatible only if the height is polynomially bounded in the degree, and the manuscripts spend almost all of their length proving exactly that polynomial bound. In the abelian case the height input is a Vojta-type inequality with a bounded-scale argument standing in for the cases it does not cover; in the Siegel case it is an auxiliary-function interpolation argument built from period equations that are invariant under Frobenius.

## Graduate summary

Manuscript A states the abelian conjecture as a finiteness statement about maximal atypical subvarieties [S5:43–50]:

> For every number field $K$, every abelian variety $A/K$, and every irreducible subvariety $X\subseteq A_{\bar K}$, there are only finitely many maximal atypical subvarieties of $X$ in $S=\langle X\rangle_{\mathrm{sp}}$. Equivalently, there are finitely many proper atypical subvarieties $Y_1,\ldots,Y_m\subsetneq X$ such that every atypical subvariety is contained in one of the $Y_j$. [S5:44–49]

Its non-density input is a theorem with universal quantifiers on the ambient variety [S5:67–71]:

> Let $A$ be an abelian variety over $\overline{\mathbb Q}$, and let $X\subseteq A$ be an irreducible subvariety contained in no proper torsion coset. Then $X\cap A^{[\dim X+1]}$ is not Zariski dense in $X$. [S5:68–70]

The passage from non-density to the finiteness theorem is made through the optimal-subvariety reduction of Barroero and Dill, and the manuscript states that the proof does not stop at non-density for one fixed subvariety [S5:73–77]. A corollary covers translation by finite-rank subgroups, which the manuscript identifies as the abelian algebraic-point case of Pink's Conjecture 5.2 [S5:100–101].

Manuscript B states its component as a theorem about curves in $\mathcal A_2$ [S9:81–92]:

> Let \(C\subset\mathcal A_2\) be a reduced, irreducible, closed algebraic curve defined over \(\overline{\mathbb Q}\). Suppose that \(C\) is Hodge generic, meaning that it is contained in no proper special subvariety of \(\mathcal A_2\). Then the set $$\bigl\{s\in C(\overline{\mathbb Q}): A_s\text{ is isogenous to }E_1\times E_2 \text{ with at least one }E_i\text{ having CM}\bigr\}$$ is finite. [S9:82–91]

Manuscript C states the quaternionic component with the endomorphism condition stated as equality of the full algebra [S13:11–20]:

> Let \(C\subset\mathcal A_{2,\overline{\mathbb Q}}\) be a reduced irreducible closed Hodge-generic algebraic curve. Then $$\Sigma_{\mathrm{QM}}(C)= \bigl\{s\in C(\overline{\mathbb Q}): \mathrm{End}^0(A_s)\text{ is an indefinite quaternion division algebra over }\mathbb Q \bigr\}$$ is finite. [S13:12–19]

Manuscript D proves the remaining branch [S18:24–28]:

> Let $C\subset\mathcal A_2$ be a nonempty reduced irreducible closed algebraic curve over $\overline{\mathbb Q}$. If $C$ is Hodge generic, then $\Sigma_{E^2}(C)$ is finite. [S18:25–27]

and then combines the three branches into the full curve case [S18:66–76]:

> For every nonempty reduced irreducible closed Hodge-generic curve $C\subset\mathcal A_2$ over $\overline{\mathbb Q}$, the set $$\Sigma(C)=C(\overline{\mathbb Q})\cap \bigcup_{\substack{Z\subset\mathcal A_2\ \mathrm{special}\mathstrut\\ \dim Z\le 1}} Z(\overline{\mathbb Q})$$ is finite. [S18:68–75]

The numbered moves, as the manuscripts describe them:

1. Manuscript A separates the ambient variety by height. Repeatedly taking the quotient of largest dimension on which the height is smaller splits the variety, up to isogeny, into at most one bounded height level and finitely many successively larger unbounded levels; normalizing each level makes the point vectors bounded, and their subgroup relations converge to a real-endomorphism projector [S5:202–210].
2. Manuscript A's unbounded level uses a generalized Vojta–Rémond inequality whose multiplicative constant is independent of the accuracy of the rational approximation to that limiting projector [S5:219–224].
3. Manuscript A's bounded level chooses auxiliary products of minimal dimension with bounded degrees and fields of definition, compares two limiting measures on that fixed factor — one from a product map, one from a consecutive difference map — and converts their disagreement into arithmetic positivity [S5:226–236]; the small sections supplied by the resulting positivity then carry a weighted vanishing index at the marked points, and the product theorem contradicts minimality [S5:238–243].
4. Manuscripts C and D both reduce finiteness to a polynomial height bound on a fixed fine-level cover. Manuscript C states its substantive estimate as $h(t)\le c_1[K(t):K]^{c_2}$ and says of it: "This estimate is proved in ; it is not an assumed Galois-orbit bound. [S13:60]" [S13:56–60]
5. Manuscript D states two arithmetic estimates, a height bound $h(t)\leq c d^{\kappa}$ and a discriminant bound $\Delta_s\leq c\bigl(dh(t)\bigr)^{\kappa'}$, and notes that combining them gives the orbit bound $[K(s):K]\geq c'\Delta_s^{\delta}$ for some $\delta>0$ [S18:157–167].
6. Manuscript D's interpolation mechanism is a quadratic system of trace-zero self-adjoint operators whose pairings are transported along a local parameter, and a Frobenius-invariance equation in which the residue characteristic no longer occurs, so that the labeled conjugate tuples give only polynomially many systems in the degree [S18:206–225] [S18:227–242]. Two fixed prime levels make those equations usable: at the first the marked planes reduce to a degenerate four-space, at the second their sum is nondegenerate, and both conditions are imposed on one connected finite cover [S18:244–250].
7. Manuscript C's final contradiction is a dimension count on the three-dimensional quadric of isotropic lines in the rank-five space, against the Zariski density forced by full monodromy [S13:118–128].
8. Manuscript D assembles the full theorem by removing the special points via André–Oort, classifying what remains into the three loci, and applying the two companion theorems to two of them [S19:331–339] [S19:341–344] [S19:346–356].

What the hypotheses exclude is part of the claim. Manuscript A imposes nothing on the ambient variety: "No bound on the degrees or heights of the intersection points is assumed, and no simplicity, endomorphism, or complex multiplication hypothesis is imposed on $A$. [S5:52–54]" It also states its limits: "it gives no effective or uniform bound for the number of maximal atypical subvarieties. [S5:55–57]" Manuscript B states that "There is no assumption on the boundary of \(C\), on an integral base point, or on reduction at any finite prime. [S9:98–99]" [S9:94–99] Manuscript C states that "No condition is imposed on the boundary of \(C\), and the points are counted across all quaternionic special curves at once. [S13:22]" Manuscript D states that "No condition is imposed on the closure of $C$ at the boundary of a compactification. In particular, the theorem includes complete curves. [S18:30–31]" 

The named resolutions the manuscripts assert are explicit. Manuscript B: "Theorem resolves positively the \(E\times\mathrmCM\) component of Zilber–Pink for Hodge-generic curves in \(\mathcal A_2\). [S9:100–101]" Manuscript C: "Thus resolves affirmatively the quaternionic-division component of the Zilber–Pink conjecture for curves in \(\mathcal A_2\). [S13:22]" Manuscript D: "resolves positively the Hodge-generic-curve case of the Zilber–Pink conjecture in $\mathcal A_2$ over $\overline{\mathbb Q}$. [S18:78–79]" Manuscript A's title is the abelian conjecture itself, and its abstract states the proof of it [S4:9–12].

The four manuscripts' own abstracts are the release's summary of each paper [S4:9–12] [S9:53–56] [S12:20–24] [S17:9–15]; the four citation blocks are the release's citation entries [S3] [S8] [S11] [S16], and the bibliographies are external to the release except where noted below [S6] [S14].

Manuscript D's independence claim is stated twice and is load-bearing for how the family should be read. In the introduction: "Theorem and its proof are independent of the two companion results. [S18:82–83]" In the finiteness section: "The two companion branch theorems enter only in the final proof of the full Zilber–Pink theorem. [S19:6–7]" The companion theorems enter at the last step, as Theorem 1.1 of each companion restated as items (A) and (B) of manuscript D's own branch theorem [S19:346–349], and the union of the three finite sets with the finite set of special points is what closes the proof [S19:355–356]. The argument survives a complete curve because "none of these steps requires a point of its closure on a compactification boundary [S19:363–364]" .

Manuscript B's one release-to-release use is an effectivity input, and it is quarantined. Its remark on the CM bound begins "The Dirichlet assertion of \cite[Theorem 1.1]OpenAIQuasiRH2026 [S9:361]" and ends "This concerns only the CM discriminant estimate: it does not assert effective Galois-orbit constants or effective finiteness in Theorems and . [S9:372–374]" The manuscript separately states that "we make no effectivity claim for the constants in Theorem [S9:187–188]" [S9:185–189].

Nothing about this family is machine-checked. The ledger records 4 manuscripts and 0 formalized for family 016, with no scope note, no comparator challenge, no `main_results` config, no verification directory, and no reasoning trace [S23:17]. Every statement above is a reading of the manuscript text, not a checked proof.

## History of the conjecture

The abelian line begins with a theorem about torsion points. Manuscript A places it there: "The torsion-point case belongs to the Manin–Mumford theorem of Raynaud [S5:113]" . Allowing the torsion cosets to vary in positive dimension is what makes the intersections atypical, and the manuscript notes that "the maximality condition in Theorem accounts for this possibility [S5:118–119]" .

The curve case in abelian varieties was settled earlier and in stages. Manuscript A records it: "For curves in powers of a CM elliptic curve, Viada proved codimension-two finiteness under the hypothesis that the curve lies in no translate of a proper algebraic subgroup [S5:121–123]" , then Habegger and Pila proved finiteness for curves in arbitrary abelian varieties over number fields [S5:126–128], and Dogra and Pandit recently obtained bounded-degree results for smooth curves whose Jacobians surject onto the ambient abelian variety [S5:132–134]. The manuscript's own comparison with the prior higher-dimensional results is the sentence that states its position: "Theorem treats arbitrary abelian varieties and all codimensions, without the additional quotient-dimension or height restrictions. [S5:165–167]" 

The Siegel line is organized around a boundary hypothesis. Manuscript C states the prior state precisely: "Daw and Orr proved the conclusion when the closure of the curve meets the zero-dimensional boundary stratum of the Baily–Borel compactification [S13:39]" , and "Their reduction for an arbitrary curve assumes a large-Galois-orbit estimate [S13:39]" . Manuscript C's claim against that background is one sentence: "We prove a height estimate independent of the number of supersingular proximity places. [S13:41]" Manuscript D states the same boundary condition for the quaternionic locus and then separates its own input from it: "the orbit-to-finiteness implication we use has no such hypothesis. [S18:120–121]" Manuscript D's comparison with the most recent product case is equally explicit: "The present height estimate permits bad reduction of the center and does not bound that number of places. [S18:140–141]" 

Manuscript D also names the arithmetic hypothesis it is supplying. "For the elliptic-square locus, the implication we use is Daw–Orr's \cite[Theorem 1.3]DawOrr2022: a suitable polynomial lower bound for Galois orbits in terms of the endomorphism-order discriminant implies finiteness. [S18:143–146]" Its own contribution is the proof of that bound: "We prove the required bound for the entire elliptic-square locus before applying that theorem. The constants may depend on $C$; effectivity is not required. [S18:147–149]" 

Prior (my training data, not this repo). Before this release, the curve case of Zilber–Pink in $\mathcal A_2$ was the flagship open case of the unlikely-intersection program: Daw–Orr had the $E\times\mathrm{CM}$ locus unconditionally under a boundary hypothesis, Pila–Tsimerman had André–Oort for $\mathcal A_2$, and the elliptic-square branch was the one where the needed Galois-orbit lower bound was out of reach with then-available height technology. The abelian Zilber–Pink conjecture in full generality — all dimensions, no simplicity or CM hypothesis, maximal atypical subvarieties — was not on my list of open problems I expected to close in this decade, and the Barroero–Dill optimal-subvariety machinery was the recent ingredient that made a non-density statement strong enough to finish it. I rate this prior as medium confidence for the Siegel line and lower for the abelian line, and the repo supplies only the claims quoted above, not the standing of the problem.

## Consequences

The family is a hub and three spokes, and the manuscripts say so. Manuscript D is the hub: "We first prove the elliptic-square part of this prediction, then combine it with the two companion branch theorems to obtain the full conclusion. [S18:11–12]" Its bibliography carries the two companions as release preprints, keyed `CompanionECM` [S20:162–168] and `CompanionQuaternion` [S20:169–175], and it cites each at Theorem 1.1 in the introduction [S18:62–63] and again in the final proof [S19:346–352]. Manuscripts B and C are the spokes that the hub consumes; each proves a branch that the other does not, and neither cites the other. Manuscript A is a separate spoke entirely: it lives in abelian varieties, not in Siegel moduli, and its bibliography carries no release-to-release link at all [S6]. Manuscript C's bibliography likewise carries none [S14].

The one edge that leaves the family is manuscript B's effectivity input, and the release records it as a release preprint in manuscript B's inline bibliography [S9:1147–1155]. The cited manuscript is the quasi-Riemann-hypothesis preprint, whose zero-free half-plane is quoted in the remark as `\(\operatorname{Re}s>7/8\)` [S9:362–363]; that is family 003, a tier T3 family, and manuscript B uses it only to make one class-number constant effective.

What the four papers buy, read carefully:

1. The curve case of Zilber–Pink in $\mathcal A_2$ over $\overline{\mathbb Q}$, with no boundary, reduction, integrality, height, or field-degree hypothesis, and with all Hecke translates included — the union of the three branch theorems plus André–Oort [S18:41–55].
2. A special-closure version for curves that are not Hodge generic, which manuscript D records as following from the same classification and André–Oort [S18:88–92].
3. The abelian conjecture in arbitrary dimension, which upgrades the known non-density results to finiteness of maximal atypical subvarieties without the quotient-dimension condition [S5:165–167], and gives the finite-rank translated non-density statement as a corollary [S5:84–98].
4. A height estimate in the Siegel threefold that does not depend on the number of supersingular proximity places, which is the input the prior finiteness results needed bounded [S13:41] [S18:140–141].

What it does not buy: effectivity, uniformity, or a bound. Manuscript A gives no effective or uniform bound [S5:55–57]; manuscript B makes no effectivity claim for its orbit constants [S9:185–189]; manuscript D requires no effectivity for its constants [S18:147–149]. The chain is only as strong as its weakest link, and the weakest link here is that none of the four is formalized: the full curve case in $\mathcal A_2$ depends on two companion manuscripts from this same family, so the assembled theorem has three unformalized papers behind it [S23:17].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Family 016 entry at 445; manuscript blurbs at 454, 463, 472 and 481 |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 016 `\resultentry` at 108 |
| S3 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/README.md`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S4 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/paper.tex`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/paper.tex) | 31 | Title at 3, date at 5, abstract at 9–12, section inputs at 19–28 |
| S5 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/sections/01-introduction.tex) | 254 | `thm:main` at 43–50, scope at 52–57, `thm:nondensity` at 67–71, Barroero–Dill passage at 73–77, `cor:finite-rank-translates` at 84–98, Pink Conjecture 5.2 at 100–101, history at 113–137, comparison at 165–167, proof strategy at 202–243 |
| S6 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/references.bib`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/references.bib) | 357 | No release-to-release `href`; all keys external |
| S7 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf) | 17471 | Typeset manuscript, 623,169 bytes |
| S8 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S9 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/paper.tex`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/paper.tex) | 1245 | Title at 44–45, date at 47, abstract at 53–56, `thm:main` at 81–92, scope at 94–101, `thm:orbits` at 174–183, effectivity caveat at 185–189, `rem:effective-cm` at 359–374, inline `thebibliography` entry `OpenAIQuasiRH2026` at 1147–1155 |
| S10 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) | 11872 | Typeset manuscript, 413,183 bytes |
| S11 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/README.md`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S12 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/paper.tex`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/paper.tex) | 39 | Title at 3, date at 5, abstract at 20–24, section inputs at 31–36, bibliography at 38 |
| S13 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/sections/00-introduction.tex) | 148 | `thm:main` at 11–20, resolution and scope at 22, earlier results at 39–41, `eq:intro-height` at 56–60, interpolation at 92–116, counting contradiction at 118–128 |
| S14 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/references/references.bib`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/references/references.bib) | 477 | No release-to-release `href`; all keys external |
| S15 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf) | 16443 | Typeset manuscript, 571,090 bytes |
| S16 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S17 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/main.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/main.tex) | 33 | Title at 3, date at 5, abstract at 9–15, section inputs at 18–27, bibliography at 31–32 |
| S18 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/01-introduction.tex) | 330 | Setup at 3–12, `thm[intro:squares]` at 24–28, scope at 30–33, `thm[intro:branches]` at 41–55, companion citations at 62–63, `thm[intro:zp]` at 66–76, independence at 82–83, special closure at 88–92, prior results at 118–149, arithmetic estimates at 151–172, mechanism at 206–279 |
| S19 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/08-finiteness.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/08-finiteness.tex) | 390 | Companion scope at 6–7, `fin:orbit` at 26–35, `fin:classification` at 270, proof of `intro:zp` at 331–365, `cor:fin:special-closure` at 370–381 |
| S20 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/references.bib`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/references.bib) | 360 | Release entries `CompanionECM` at 162–168 and `CompanionQuaternion` at 169–175 |
| S21 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) | 20306 | Typeset manuscript, 719,203 bytes |
| S22 | [`notes/gen/reports/t0-triage.md`](../../../notes/gen/reports/t0-triage.md) | 897 | Family 016 entry at 129–130 |
| S23 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Ledger row for family 016 at 17 |

## Bibliography

- Abhinandan, Youcis, Alex, An integral comparison of crystalline and de Rham cohomology (2025)
- André, Yves, G-Functions and Geometry (1989)
- André, Yves, Théorie des motifs et interprétation géométrique des valeurs $p$-adiques de G-functions (une introduction) (1995)
- André, Yves, Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part (1992)
- André, Yves, G-Functions and Geometry (1989)
- André, Yves, Théorie des motifs et interprétation géométrique des valeurs $p$-adiques de G-functions (une introduction) (1995)
- André, Yves, G-functions, motives, and unlikely intersections—old and new (2025)
- Aschenbrenner, Matthias, Ideal membership in polynomial rings over the integers (2004)
- Aschenbrenner, Matthias, Ideal Membership in Polynomial Rings over the Integers (2004)
- The Stacks Project Authors, The Stacks Project (2026)
- Ax, James, Some topics in differential algebraic geometry. I. Analytic subgroups of algebraic groups (1972)
- Barroero, Fabrizio, Dill, Gabriel A., On the Zilber–Pink conjecture for complex abelian varieties (2022)
- Barroero, Fabrizio, Kühne, Lars, Schmidt, Harry, Unlikely intersections of curves with algebraic subgroups in semiabelian varieties (2023)
- Basu, Saugata, Algorithms in Real Algebraic Geometry: A Survey (2017)
- Berthelot, Pierre, Ogus, Arthur, $F$-isocrystals and de Rham cohomology. I (1983)
- Berthelot, Pierre, Géométrie rigide et cohomologie des variétés algébriques de caractéristique $p$ (1981–1982)
- Berthelot, Pierre, Ogus, Arthur, $F$-isocrystals and de Rham cohomology. I (1983)
- Bertrand, Daniel, Beukers, Frits, Équations différentielles linéaires et majorations de multiplicités (1985)
- Bertrand, Daniel, Beukers, Frits, Équations différentielles linéaires et majorations de multiplicités (1985)
- Bombieri, Enrico, On G-functions (1981)
- Bombieri, Enrico, On G-functions (1981)
- Bosch, Siegfried, Lütkebohmert, Werner, Raynaud, Michel, {Néron} Models (1990)
- Bosch, Siegfried, Lütkebohmert, Werner, Raynaud, Michel, Néron Models (1990)
- Bost, Jean-Beno\^it, Gillet, Henri, Soulé, Christophe, Heights of projective varieties and positive Green forms (1994)
- Cais, Bryden, Canonical extensions of Néron models of Jacobians (2010)
- G. Faltings and C.-L. Chai, _Degeneration of Abelian Varieties_, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 22, Springer-Verlag, Berlin, 1990.
- Chai, Ching-Li, Compactification of Siegel Moduli Schemes (1985)
- Checcoli, Sara, Veneziano, Francesco, Viada, Evelina, On torsion anomalous intersections (2014)
- Y.-G. Chen, _On the Siegel–Tatuzawa–Hoffstein theorem_, Acta Arith. **130** (2007), 361–367. Publisher's PDF.
- D. A. Cox, _Primes of the Form $x^2+ny^2$: Fermat, Class Field Theory, and Complex Multiplication_, second ed., John Wiley & Sons, Hoboken, NJ, 2013. doi:10.1002/9781118400722.
- Daw, Christopher, Orr, Martin, Quantitative reduction theory and unlikely intersections (2022)
- Daw, Christopher, Orr, Martin, The large Galois orbits conjecture under multiplicative degeneration (2025)
- Daw, Christopher, Orr, Martin, Quantitative Reduction Theory and Unlikely Intersections (2022)
- Daw, Christopher, Orr, Martin, Unlikely intersections with $E\times\mathrm{CM}$ curves in $\mathcal A_2$ (2021)
- Daw, Christopher, Orr, Martin, The large Galois orbits conjecture under multiplicative degeneration (2025)
- Daw, Christopher, Orr, Martin, Zilber–Pink in a product of modular curves assuming multiplicative degeneration (2025)
- Daw, Christopher, Orr, Martin, Papas, Georgios, Some new cases of Zilber–Pink in $Y(1)^3$ (2026)
- Deligne, Pierre, Équations différentielles \`a points singuliers réguliers (1970)
- Dill, Gabriel A., Generalized Vojta–Rémond inequality (2020)
- Dogra, Netan, Pandit, Sudip, A Buium–Coleman bound for the Zilber–Pink conjecture for curves inside abelian varieties (2026)
- van den Dries, Lou, Macintyre, Angus, Marker, David, The elementary theory of restricted analytic fields with exponentiation (1994)
- Dubé, Thomas W., The Structure of Polynomial Ideals and {Gröbner} Bases (1990)
- Edixhoven, Bas, Lido, Guido, Geometric quadratic Chabauty (2023)
- Elman, Richard, Karpenko, Nikita, Merkurjev, Alexander, The Algebraic and Geometric Theory of Quadratic Forms (2008)
- Evertse, Jan-Hendrik, An explicit version of Faltings' Product Theorem and an improvement of Roth's lemma (1995)
- Faltings, Gerd, Diophantine approximation on abelian varieties (1991)
- Faltings, Gerd, Chai, Ching-Li, Degeneration of Abelian Varieties (1990)
- Faltings, Gerd, Chai, Ching-Li, Degeneration of Abelian Varieties (1990)
- Fulton, William, Intersection Theory (1998)
- Genestier, Alain, Ng{\^o}, Bao Ch{\^a}u, Lectures on Shimura varieties (2009)
- A. Grothendieck, _Mod\`eles de Néron et monodromie_, with an appendix by M. Raynaud, Exposé IX in _Groupes de monodromie en géométrie algébrique_ (SGA 7 I), Lecture Notes in Mathematics, vol. 288, Springer, Berlin, 1972, 313–523. doi:10.1007/BFb0068694.
- Grothendieck, Alexander, On the de Rham cohomology of algebraic varieties (1966)
- Habegger, Philipp, Pila, Jonathan, O-minimality and certain atypical intersections (2016)
- Habegger, Philipp, Intersecting subvarieties of abelian varieties with algebraic subgroups of complementary dimension (2009)
- Habegger, Philipp, Pila, Jonathan, O-minimality and certain atypical intersections (2016)
- Hermann, Grete, Die Frage der endlich vielen Schritte in der Theorie der Polynomideale (1926)
- Hubschmid, Patrik, Viada, Evelina, An Addendum to the elliptic torsion anomalous conjecture in codimension 2 (2019)
- Katz, Nicholas M., Nilpotent connections and the monodromy theorem: applications of a result of Turrittin (1970)
- Katz, Nicholas M., Oda, Tadao, On the differentiation of De Rham cohomology classes with respect to parameters (1968)
- Katz, Nicholas M., Nilpotent connections and the monodromy theorem: Applications of a result of Turrittin (1970)
- Krick, Teresa, Pardo, Luis Miguel, Sombra, Martín, Sharp estimates for the arithmetic Nullstellensatz (2001)
- Krick, Teresa, Pardo, Luis Miguel, Sombra, Martín, Sharp estimates for the arithmetic Nullstellensatz (2001)
- Kubrak, Dmitry, Prikhodko, Artem, Rational $p$-adic Hodge theory for $d$-de Rham-proper stacks (2022)
- K.-W. Lan, _Arithmetic Compactifications of PEL-Type Shimura Varieties_, London Mathematical Society Monographs Series, vol. 36, Princeton University Press, Princeton, 2013. Numbered references use the revised dissertation version (14 March 2021).
- Lan, Kai-Wen, Arithmetic Compactifications of PEL-Type Shimura Varieties (2013)
- Lawrence, Brian, Venkatesh, Akshay, Diophantine problems and $p$-adic period mappings (2020)
- S. Löbrich, _A gap in the spectrum of the Faltings height_, J. Théor. Nombres Bordeaux **29** (2017), 289–305. doi:10.5802/jtnb.980.
- Masser, David W., Wüstholz, Gisbert, Endomorphism estimates for abelian varieties (1994)
- Masser, David W., Wüstholz, Gisbert, Endomorphism estimates for abelian varieties (1994)
- Matthews, C. R., Vaserstein, L. N., Weisfeiler, B., Congruence properties of Zariski-dense subgroups I (1984)
- Matthews, Colin R., Vaserstein, Leonid N., Weisfeiler, Boris, Congruence Properties of Zariski-Dense Subgroups I (1984)
- Maulik, Davesh, Poonen, Bjorn, {Néron–Severi} groups under specialization (2012)
- Mazur, Barry, Messing, William, Universal Extensions and One Dimensional Crystalline Cohomology (1974)
- Milne, James S., Abelian Varieties (2008)
- Milne, James S., Abelian varieties (1986)
- Milne, James S., Shimura Varieties: The Geometric Side of the Zeta Function (1995)
- Milne, James S., Introduction to Shimura Varieties (2005)
- Milne, James S., Shimura varieties and moduli (2013)
- Milne, James S., Abelian Varieties (1986)
- Milne, James S., Shimura Varieties: The Geometric Side of the Zeta Function (1995)
- Milne, James S., Shimura varieties and moduli (2013)
- Moonen, Ben, Zarhin, Yuri G., Hodge classes on abelian varieties of low dimension (1999)
- Ogus, Arthur, $F$-isocrystals and de Rham cohomology II—Convergent isocrystals (1984)
- OpenAI, _The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\mathrm{Re}(s)>7/8$_, OpenAI Math Release preprint OAI:The-Quasi-Riemann-Hypothesis-September-30-2026, 2026.
- OpenAI, {The $E\times\mathrm{CM}$ component of Zilber–Pink for curves in $\mathcal A_2$} (2026)
- OpenAI, Quaternionic division points on curves in the Siegel threefold (2026)
- C. Daw and M. Orr, _Unlikely intersections with $E\times\CM$ curves in $\A_2$_, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) **22** (2021), 1705–1745. doi:10.2422/2036-2145.202006\_014. We use the corrected preprint, arXiv:1902.10483v4 (28 May 2021).
- C. Daw and M. Orr, _The large Galois orbits conjecture under multiplicative degeneration_, arXiv:2306.13463v2, revised 15 May 2025.
- Orr, Martin, Galois conjugates of special points and special subvarieties in Shimura varieties (2021)
- G. Papas, _On the $v$-adic values of $G$-functions I: Splittings in $\A_2$_, arXiv:2510.11806v1, 13 October 2025.
- Papas, Georgios, On the $v$-adic values of $G$-functions I: Splittings in $\mathcal A_2$ (2025)
- Papas, Georgios, On the $v$-adic values of $G$-functions III: QM points in $\mathcal A_2$ (2025)
- Papas, Georgios, Some cases of the Zilber–Pink conjecture for curves in $\mathcal A_g$ (2024)
- Papas, Georgios, On the $v$-adic values of G-functions I: Splittings in $\mathcal A_2$ (2025)
- F. Pazuki, _Theta height and Faltings height_, Bull. Soc. Math. France **140** (2012), 19–49. doi:10.24033/bsmf.2623.
- Pazuki, Fabien, Theta height and Faltings height (2012)
- Pazuki, Fabien, Theta height and Faltings height (2012)
- Petrequin, Denis, Classes de Chern et classes de cycles en cohomologie rigide (2003)
- Pila, Jonathan, Wilkie, Alex J., The rational points of a definable set (2006)
- Pila, Jonathan, O-minimality and the André–Oort conjecture for $\mathbb C^n$ (2011)
- Pila, Jonathan, Zannier, Umberto, Rational points in periodic analytic sets and the Manin–Mumford conjecture (2008)
- Pila, Jonathan, Tsimerman, Jacob, The André–Oort conjecture for the moduli space of abelian surfaces (2013)
- Pila, Jonathan, Wilkie, Alex J., The rational points of a definable set (2006)
- Pila, Jonathan, Zannier, Umberto, Rational points in periodic analytic sets and the Manin–Mumford conjecture (2008)
- Pink, Richard, A common generalization of the conjectures of André–Oort, Manin–Mumford, and Mordell–Lang (2005)
- R. Pink, _A common generalization of the conjectures of André–Oort, Manin–Mumford, and Mordell–Lang_, preprint, April 17, 2005. Author's manuscript.
- Pink, Richard, A common generalization of the conjectures of André–Oort, Manin–Mumford, and Mordell–Lang (2005)
- Pink, Richard, A Common Generalization of the Conjectures of André–Oort, Manin–Mumford, and Mordell–Lang (2005)
- Raynaud, Michel, Sous-variétés d'une variété abélienne et points de torsion (1983)
- Rémond, Gaël, Intersection de sous-groupes et de sous-variétés III (2009)
- Rémond, Gaël, Inégalité de Vojta généralisée (2005)
- Rémond, Gaël, Viada, Evelina, Probl\`eme de Mordell–Lang modulo certaines sous-variétés abéliennes (2003)
- É. Gaudron and G. Rémond, _Théor\`eme des périodes et degrés minimaux d'isogénies_, Comment. Math. Helv. **89** (2014), 343–403. doi:10.4171/CMH/322.
- Schmid, Wilfried, Variation of Hodge structure: The singularities of the period mapping (1973)
- Schmid, Wilfried, Variation of Hodge Structure: The Singularities of the Period Mapping (1973)
- M. Orr and C. Schnell, _Correction to the article Height bounds and the Siegel property_, Algebra Number Theory **17** (2023), 1231–1237. doi:10.2140/ant.2023.17.1231.
- Schulze-Pillot, Rainer, Lecture notes on quadratic forms and their arithmetic (2020)
- C. L. Siegel, _Über die Classenzahl quadratischer Zahlkörper_, Acta Arith. **1** (1935), 83–86. doi:10.4064/aa-1-1-83-86.
- J. H. Silverman, _Heights and elliptic curves_, in _Arithmetic Geometry_ (G. Cornell and J. H. Silverman, eds.), Springer, New York, 1986, 253–265. doi:10.1007/978-1-4613-8655-1\_10.
- Szpiro, Lucien, Ullmo, Emmanuel, Zhang, Shou-Wu, Équirépartition des petits points (1997)
- J.-P. Serre and J. Tate, _Good reduction of abelian varieties_, Ann. of Math. (2) **88** (1968), 492–517. doi:10.2307/1970722.
- J. Tate, _A review of non-Archimedean elliptic functions_, in _Elliptic Curves, Modular Forms, & Fermat's Last Theorem_ (Hong Kong, 1993), Series in Number Theory, vol. I, International Press, Cambridge, MA, 1995, 162–184. Author's reprint.
- J. Pila and J. Tsimerman, _The André–Oort conjecture for the moduli space of abelian surfaces_, Compos. Math. **149** (2013), 204–216. doi:10.1112/S0010437X12000589.
- J. Tsimerman, _The André–Oort conjecture for $\A_g$_, Ann. of Math. (2) **187** (2018), 379–390. doi:10.4007/annals.2018.187.2.2.
- Ullmo, Emmanuel, Positivité et discrétion des points algébriques des courbes (1998)
- Viada, Evelina, Nondense Subsets of Varieties in a Power of an Elliptic Curve (2009)
- Viada, Evelina, The intersection of a curve with algebraic subgroups in a product of elliptic curves (2003)
- Vojta, Paul, Siegel's theorem in the compact case (1991)
- J. Pila and A. J. Wilkie, _The rational points of a definable set_, Duke Math. J. **133** (2006), 591–616. doi:10.1215/S0012-7094-06-13336-7.
- D. W. Masser and G. Wüstholz, _Periods and minimal abelian subvarieties_, Ann. of Math. (2) **137** (1993), 407–458. doi:10.2307/2946542.
- Włodarczyk, Jarosław, Simple Hironaka resolution in characteristic zero (2005)
- Yuan, Xinyi, Zhang, Shou-Wu, Adelic Line Bundles on Quasi-projective Varieties (2025)
- Yuan, Xinyi, Big line bundles over arithmetic varieties (2008)
- J. Pila and U. Zannier, _Rational points in periodic analytic sets and the Manin–Mumford conjecture_, Rend. Lincei Mat. Appl. (9) **19** (2008), 149–162. doi:10.4171/RLM/514.
- Zhang, Shouwu, Small points and adelic metrics (1995)
- Zhang, Shou-Wu, Equidistribution of small points on abelian varieties (1998)
- Zhang, Shou-Wu, Small points and Arakelov theory (1998)
- Zilber, Boris, Exponential sums equations and the Schanuel conjecture (2002)
- B. Zilber, _Exponential sums equations and the Schanuel conjecture_, J. London Math. Soc. (2) **65** (2002), 27–44. doi:10.1112/S0024610701002861.
- Zilber, Boris, Exponential sums equations and the Schanuel conjecture (2002)
- Zilber, Boris, Exponential sums equations and the Schanuel conjecture (2002)
- André, Yves, Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part (1992)
- Dubé, Thomas W., The structure of polynomial ideals and {Gröbner} bases (1990)
