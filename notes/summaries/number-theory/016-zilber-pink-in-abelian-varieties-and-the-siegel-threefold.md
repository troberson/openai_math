# 016 — Zilber–Pink in abelian varieties and the Siegel threefold (Number theory, 4 manuscripts, tier T0)

## Original CONTENTS.md summary

The release entry for the family is two sentences, and the second is quoted here in full [S1:445]: "It also proves the full curve case in the Siegel threefold". The entry names four manuscripts; the triage record files the family as a four-paper resolution [S22:129–130], and the release overview carries the same entry with the four manuscript links [S2:108].

The abelian manuscript's blurb [S1:454]:

> Every irreducible subvariety of an abelian variety has only finitely many maximal atypical subvarieties, where atypicality is measured inside its smallest containing torsion coset.

The E×CM manuscript's blurb [S1:463]:

> Each such curve contains only finitely many points whose abelian surface is isogenous to a product of elliptic curves with at least one factor having complex multiplication.

The quaternionic manuscript's blurb [S1:472]:

> A Hodge-generic algebraic curve contains only finitely many points whose full geometric rational endomorphism algebra is an indefinite quaternion division algebra over ℚ. No boundary or reduction hypothesis is required.

The elliptic-square manuscript's blurb [S1:481]:

> We prove that every Hodge-generic algebraic curve in $`\mathcal A_2`$ over $`\overline{\mathbb Q}`$ contains only finitely many points whose abelian surface is isogenous to the square of an elliptic curve without complex multiplication (CM). Combining this result with the companion $`E\times\mathrm{CM}`$ and quaternionic-division finiteness theorems, we prove the curve case of Zilber–Pink in $`\mathcal A_2`$ over $`\overline{\mathbb Q}`$, without a boundary hypothesis.

## Undergraduate summary

One conjecture, four shapes. Zilber and Pink predicted, in two settings, that an algebraic variety inside a rich ambient space cannot meet the "special" locus more often than a dimension count allows. Manuscript A works inside an abelian variety, where the special loci are torsion cosets — abelian subvarieties translated by torsion points. Manuscripts B, C and D work inside $\mathcal A_2$, the three-dimensional moduli space of principally polarized abelian surfaces, where the special loci of dimension one are curves parametrizing surfaces with extra endomorphisms. In both settings the question is the same: intersect a Hodge-generic object with every special locus of small dimension, allowing all of them to vary, and ask whether what you get is finite.

The abelian case is the older one. Its zero-dimensional version is the Manin–Mumford theorem, proved by Raynaud: a subvariety of an abelian variety containing densely many torsion points is itself a torsion coset. Allowing the torsion cosets to have positive dimension makes the intersections larger than the dimension count predicts, and those excess intersections are the "atypical" ones. The claim this manuscript makes is about the *maximal* atypical pieces, which is the right unit: a positive-dimensional atypical intersection can sit inside a bigger one.

The Siegel case splits by what the extra endomorphisms look like. An abelian surface whose rational endomorphism algebra is as small as possible is a product of two non-CM elliptic curves; the *elliptic square* locus is the case where the two factors are isogenous to each other. The three generic types of special curve in $\mathcal A_2$ are products with a CM factor, non-CM elliptic squares, and surfaces with quaternion multiplication. Manuscripts B, C and D each take one of the three, and manuscript D then assembles all three into the full curve case.

**The shape of the argument, in both settings, is a contradiction built from a hypothetical infinite sequence.** Take a sequence of intersection points that is generic in the ambient variety. Arithmetic gives a lower bound on how large the Galois orbit of each point must be, because a point with many endomorphisms has many conjugates. Geometry, via o-minimal counting of rational points in definable sets, gives an upper bound that is much smaller once the height is controlled. The two bounds are compatible only if the height is polynomially bounded in the degree, and the manuscripts spend almost all of their length proving exactly that polynomial bound. In the abelian case the height input is a Vojta-type inequality with a bounded-scale argument standing in for the cases it does not cover; in the Siegel case it is an auxiliary-function interpolation argument built from period equations that are invariant under Frobenius.

## Graduate summary

Manuscript A states the abelian conjecture as a finiteness statement about maximal atypical subvarieties [S5:43–50]:

> For every number field $K$, every abelian variety $A/K$, and every
> irreducible subvariety $X\subseteq A_{\bar K}$, there are only finitely
> many maximal atypical subvarieties of $X$ in
> $S=\langle X\rangle_{\mathrm{sp}}$. Equivalently, there are finitely many
> proper atypical subvarieties $Y_1,\ldots,Y_m\subsetneq X$ such that every
> atypical subvariety is contained in one of the $Y_j$.

Its non-density input is a theorem with universal quantifiers on the ambient variety [S5:67–71]:

> Let $A$ be an abelian variety over $\Qbar$, and let $X\subseteq A$ be an
> irreducible subvariety contained in no proper torsion coset. Then
> $X\cap A^{[\dim X+1]}$ is not Zariski dense in $X$.

The passage from non-density to the finiteness theorem is made through the optimal-subvariety reduction of Barroero and Dill, and the manuscript states that the proof does not stop at non-density for one fixed subvariety [S5:73–77]. A corollary covers translation by finite-rank subgroups, which the manuscript identifies as the abelian algebraic-point case of Pink's Conjecture 5.2 [S5:100–101].

Manuscript B states its component as a theorem about curves in $\mathcal A_2$ [S9:81–92]:

> Let \(C\subset\A_2\) be a reduced, irreducible, closed algebraic curve
> defined over \(\Qbar\). Suppose that \(C\) is Hodge generic, meaning that
> it is contained in no proper special subvariety of \(\A_2\).
> Then the set
> \[
>  \bigl\{s\in C(\Qbar):
>  A_s\text{ is isogenous to }E_1\times E_2
>  \text{ with at least one }E_i\text{ having CM}\bigr\}
> \]
> is finite.

Manuscript C states the quaternionic component with the endomorphism condition stated as equality of the full algebra [S13:11–20]:

> Let \(C\subset\Acal_{2,\Qbar}\) be a reduced irreducible closed Hodge-generic algebraic curve. Then
> \[
>  \Sigma_{\mathrm{QM}}(C)=
>  \bigl\{s\in C(\Qbar):
>    \End^0(A_s)\text{ is an indefinite quaternion division algebra over }\Q
>  \bigr\}
> \]
> is finite.

Manuscript D proves the remaining branch [S18:24–28]:

> Let $C\subset\A_2$ be a nonempty reduced irreducible closed algebraic
> curve over $\Qbar$. If $C$ is Hodge generic, then $\Sigma_{E^2}(C)$ is
> finite.

and then combines the three branches into the full curve case [S18:66–76]:

> For every nonempty reduced irreducible
> closed Hodge-generic curve $C\subset\A_2$ over $\Qbar$, the set
> \[
>  \Sigma(C)=C(\Qbar)\cap
>  \bigcup_{\substack{Z\subset\A_2\ \mathrm{special}\mathstrut\\
>                      \dim Z\le 1}} Z(\Qbar)
> \]
> is finite.

The numbered moves, as the manuscripts describe them:

1. Manuscript A separates the ambient variety by height. Repeatedly taking the quotient of largest dimension on which the height is smaller splits the variety, up to isogeny, into at most one bounded height level and finitely many successively larger unbounded levels; normalizing each level makes the point vectors bounded, and their subgroup relations converge to a real-endomorphism projector [S5:202–210].
2. Manuscript A's unbounded level uses a generalized Vojta–Rémond inequality whose multiplicative constant is independent of the accuracy of the rational approximation to that limiting projector [S5:219–224].
3. Manuscript A's bounded level chooses auxiliary products of minimal dimension with bounded degrees and fields of definition, compares two limiting measures on that fixed factor — one from a product map, one from a consecutive difference map — and converts their disagreement into arithmetic positivity [S5:226–236]; the small sections supplied by the resulting positivity then carry a weighted vanishing index at the marked points, and the product theorem contradicts minimality [S5:238–243].
4. Manuscripts C and D both reduce finiteness to a polynomial height bound on a fixed fine-level cover. Manuscript C states its substantive estimate as $h(t)\le c_1[K(t):K]^{c_2}$ and says of it: "This estimate is proved in \Cref{thm:height}; it is not an assumed Galois-orbit bound." [S13:56–60]
5. Manuscript D states two arithmetic estimates, a height bound $h(t)\leq c d^{\kappa}$ and a discriminant bound $\Delta_s\leq c\bigl(dh(t)\bigr)^{\kappa'}$, and notes that combining them gives the orbit bound $[K(s):K]\geq c'\Delta_s^{\delta}$ for some $\delta>0$ [S18:157–167].
6. Manuscript D's interpolation mechanism is a quadratic system of trace-zero self-adjoint operators whose pairings are transported along a local parameter, and a Frobenius-invariance equation in which the residue characteristic no longer occurs, so that the labeled conjugate tuples give only polynomially many systems in the degree [S18:206–225] [S18:227–242]. Two fixed prime levels make those equations usable: at the first the marked planes reduce to a degenerate four-space, at the second their sum is nondegenerate, and both conditions are imposed on one connected finite cover [S18:244–250].
7. Manuscript C's final contradiction is a dimension count on the three-dimensional quadric of isotropic lines in the rank-five space, against the Zariski density forced by full monodromy [S13:118–128].
8. Manuscript D assembles the full theorem by removing the special points via André–Oort, classifying what remains into the three loci, and applying the two companion theorems to two of them [S19:331–339] [S19:341–344] [S19:346–356].

What the hypotheses exclude is part of the claim. Manuscript A imposes nothing on the ambient variety: "No bound on the degrees or heights of the intersection points is assumed, and no simplicity, endomorphism, or complex multiplication hypothesis is imposed on $A$." [S5:52–54] It also states its limits: "it gives no effective or uniform bound for the number of maximal atypical subvarieties." [S5:55–57] Manuscript B states that "There is no assumption on the boundary of \(C\), on an integral base point, or on reduction at any finite prime." [S9:94–99] Manuscript C states that "No condition is imposed on the boundary of \(C\), and the points are counted across all quaternionic special curves at once." [S13:22] Manuscript D states that "No condition is imposed on the closure of $C$ at the boundary of a compactification. In particular, the theorem includes complete curves." [S18:30–31]

The named resolutions the manuscripts assert are explicit. Manuscript B: "Theorem~\ref{thm:main} resolves positively the \(E\times\CM\) component of Zilber--Pink for Hodge-generic curves in \(\A_2\)." [S9:100–101] Manuscript C: "Thus \Cref{thm:main} resolves affirmatively the quaternionic-division component of the Zilber--Pink conjecture for curves in \(\Acal_2\)." [S13:22] Manuscript D: "\Cref{intro:zp} resolves positively the Hodge-generic-curve case of the Zilber--Pink conjecture in $\A_2$ over $\Qbar$." [S18:78–79] Manuscript A's title is the abelian conjecture itself, and its abstract states the proof of it [S4:9–12].

The four manuscripts' own abstracts are the release's summary of each paper [S4:9–12] [S9:53–56] [S12:20–24] [S17:9–15]; the four citation blocks are the release's citation entries [S3] [S8] [S11] [S16], and the bibliographies are external to the release except where noted below [S6] [S14].

Manuscript D's independence claim is stated twice and is load-bearing for how the family should be read. In the introduction: "Theorem~\ref{intro:squares} and its proof are independent of the two companion results." [S18:82–83] In the finiteness section: "The two companion branch theorems enter only in the final proof of the full Zilber--Pink theorem." [S19:6–7] The companion theorems enter at the last step, as Theorem 1.1 of each companion restated as items (A) and (B) of manuscript D's own branch theorem [S19:346–349], and the union of the three finite sets with the finite set of special points is what closes the proof [S19:355–356]. The argument survives a complete curve because "none of these steps requires a point of its closure on a compactification boundary" [S19:363–364].

Manuscript B's one release-to-release use is an effectivity input, and it is quarantined. Its remark on the CM bound begins "The Dirichlet assertion of \cite[Theorem~1.1]{OpenAIQuasiRH2026}" [S9:361] and ends "This concerns only the CM discriminant estimate: it does not assert effective Galois-orbit constants or effective finiteness in Theorems~\ref{thm:orbits} and~\ref{thm:main}." [S9:372–374] The manuscript separately states that "we make no effectivity claim for the constants in Theorem~\ref{thm:orbits}" [S9:185–189].

Nothing about this family is machine-checked. The ledger records 4 manuscripts and 0 formalized for family 016, with no scope note, no comparator challenge, no `main_results` config, no verification directory, and no reasoning trace [S23:17]. Every statement above is a reading of the manuscript text, not a checked proof.

## History of the conjecture

The abelian line begins with a theorem about torsion points. Manuscript A places it there: "The torsion-point case belongs to the Manin--Mumford theorem of Raynaud" [S5:113]. Allowing the torsion cosets to vary in positive dimension is what makes the intersections atypical, and the manuscript notes that "the maximality condition in Theorem~\ref{thm:main} accounts for this possibility" [S5:118–119].

The curve case in abelian varieties was settled earlier and in stages. Manuscript A records it: "For curves in powers of a CM elliptic curve, Viada proved codimension-two finiteness under the hypothesis that the curve lies in no translate of a proper algebraic subgroup" [S5:121–123], then Habegger and Pila proved finiteness for curves in arbitrary abelian varieties over number fields [S5:126–128], and Dogra and Pandit recently obtained bounded-degree results for smooth curves whose Jacobians surject onto the ambient abelian variety [S5:132–134]. The manuscript's own comparison with the prior higher-dimensional results is the sentence that states its position: "Theorem~\ref{thm:main} treats arbitrary abelian varieties and all codimensions, without the additional quotient-dimension or height restrictions." [S5:165–167]

The Siegel line is organized around a boundary hypothesis. Manuscript C states the prior state precisely: "Daw and Orr proved the conclusion when the closure of the curve meets the zero-dimensional boundary stratum of the Baily--Borel compactification" [S13:39], and "Their reduction for an arbitrary curve assumes a large-Galois-orbit estimate" [S13:39]. Manuscript C's claim against that background is one sentence: "We prove a height estimate independent of the number of supersingular proximity places." [S13:41] Manuscript D states the same boundary condition for the quaternionic locus and then separates its own input from it: "the orbit-to-finiteness implication we use has no such hypothesis." [S18:120–121] Manuscript D's comparison with the most recent product case is equally explicit: "The present height estimate permits bad reduction of the center and does not bound that number of places." [S18:140–141]

Manuscript D also names the arithmetic hypothesis it is supplying. "For the elliptic-square locus, the implication we use is Daw--Orr's \cite[Theorem~1.3]{DawOrr2022}: a suitable polynomial lower bound for Galois orbits in terms of the endomorphism-order discriminant implies finiteness." [S18:143–146] Its own contribution is the proof of that bound: "We prove the required bound for the entire elliptic-square locus before applying that theorem. The constants may depend on $C$; effectivity is not required." [S18:147–149]

Prior (my training data, not this repo). Before this release, the curve case of Zilber–Pink in $\mathcal A_2$ was the flagship open case of the unlikely-intersection program: Daw–Orr had the $E\times\mathrm{CM}$ locus unconditionally under a boundary hypothesis, Pila–Tsimerman had André–Oort for $\mathcal A_2$, and the elliptic-square branch was the one where the needed Galois-orbit lower bound was out of reach with then-available height technology. The abelian Zilber–Pink conjecture in full generality — all dimensions, no simplicity or CM hypothesis, maximal atypical subvarieties — was not on my list of open problems I expected to close in this decade, and the Barroero–Dill optimal-subvariety machinery was the recent ingredient that made a non-density statement strong enough to finish it. I rate this prior as medium confidence for the Siegel line and lower for the abelian line, and the repo supplies only the claims quoted above, not the standing of the problem.

## Consequences now that the proof has been found

The family is a hub and three spokes, and the manuscripts say so. Manuscript D is the hub: "We first prove the elliptic-square part of this prediction, then combine it with the two companion branch theorems to obtain the full conclusion." [S18:11–12] Its bibliography carries the two companions as release preprints, keyed `CompanionECM` [S20:162–168] and `CompanionQuaternion` [S20:169–175], and it cites each at Theorem 1.1 in the introduction [S18:62–63] and again in the final proof [S19:346–352]. Manuscripts B and C are the spokes that the hub consumes; each proves a branch that the other does not, and neither cites the other. Manuscript A is a separate spoke entirely: it lives in abelian varieties, not in Siegel moduli, and its bibliography carries no release-to-release link at all [S6]. Manuscript C's bibliography likewise carries none [S14].

The one edge that leaves the family is manuscript B's effectivity input, and the release records it as a release preprint in manuscript B's inline bibliography [S9:1147–1155]. The cited manuscript is the quasi-Riemann-hypothesis preprint, whose zero-free half-plane is quoted in the remark as `\(\operatorname{Re}s>7/8\)` [S9:362–363]; that is family 003, a tier T3 family, and manuscript B uses it only to make one class-number constant effective.

What the four papers buy, read carefully:

1. The curve case of Zilber–Pink in $\mathcal A_2$ over $\overline{\mathbb Q}$, with no boundary, reduction, integrality, height, or field-degree hypothesis, and with all Hecke translates included — the union of the three branch theorems plus André–Oort [S18:41–55].
2. A special-closure version for curves that are not Hodge generic, which manuscript D records as following from the same classification and André–Oort [S18:88–92].
3. The abelian conjecture in arbitrary dimension, which upgrades the known non-density results to finiteness of maximal atypical subvarieties without the quotient-dimension condition [S5:165–167], and gives the finite-rank translated non-density statement as a corollary [S5:84–98].
4. A height estimate in the Siegel threefold that does not depend on the number of supersingular proximity places, which is the input the prior finiteness results needed bounded [S13:41] [S18:140–141].

What it does not buy: effectivity, uniformity, or a bound. Manuscript A gives no effective or uniform bound [S5:55–57]; manuscript B makes no effectivity claim for its orbit constants [S9:185–189]; manuscript D requires no effectivity for its constants [S18:147–149]. The chain is only as strong as its weakest link, and the weakest link here is that none of the four is formalized: the full curve case in $\mathcal A_2$ depends on two companion manuscripts from this same family, so the assembled theorem has three unformalized papers behind it [S23:17].

## Sources

The four manuscript roots are `preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/` (15 text files, 3,639 lines), `preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/` (2 text files, 1,263 lines), `preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/` (11 text files, 3,777 lines) and `preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/` (15 text files, 5,150 lines). Each root holds a `README.md`, a `build/` directory and `paper.pdf`. Manuscripts A, C and D keep their body in `build/sections/` with a shared preamble; manuscript B is a single self-contained `build/paper.tex` whose bibliography is an inline `thebibliography` block, so it has no `.bib` file and its Sources rows are a driver row and a PDF row only. Manuscript C keeps its bibliography nested at `build/references/references.bib`. Every manuscript file below sits under the manuscript's `build/` directory, which is where this release puts its LaTeX.

| ID | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Family 016 entry at 445; manuscript blurbs at 454, 463, 472 and 481 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 016 `\resultentry` at 108 |
| S3 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/README.md`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S4 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/paper.tex`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/paper.tex) | 31 | Title at 3, date at 5, abstract at 9–12, section inputs at 19–28 |
| S5 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/sections/01-introduction.tex) | 254 | `thm:main` at 43–50, scope at 52–57, `thm:nondensity` at 67–71, Barroero–Dill passage at 73–77, `cor:finite-rank-translates` at 84–98, Pink Conjecture 5.2 at 100–101, history at 113–137, comparison at 165–167, proof strategy at 202–243 |
| S6 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/references.bib`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/build/references.bib) | 357 | No release-to-release `href`; all keys external |
| S7 | [`preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf) | — | Typeset manuscript, 623,169 bytes |
| S8 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S9 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/paper.tex`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/paper.tex) | 1,245 | Title at 44–45, date at 47, abstract at 53–56, `thm:main` at 81–92, scope at 94–101, `thm:orbits` at 174–183, effectivity caveat at 185–189, `rem:effective-cm` at 359–374, inline `thebibliography` entry `OpenAIQuasiRH2026` at 1147–1155 |
| S10 | [`preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) | — | Typeset manuscript, 413,183 bytes |
| S11 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/README.md`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S12 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/paper.tex`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/paper.tex) | 39 | Title at 3, date at 5, abstract at 20–24, section inputs at 31–36, bibliography at 38 |
| S13 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/sections/00-introduction.tex) | 148 | `thm:main` at 11–20, resolution and scope at 22, earlier results at 39–41, `eq:intro-height` at 56–60, interpolation at 92–116, counting contradiction at 118–128 |
| S14 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/references/references.bib`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/build/references/references.bib) | 477 | No release-to-release `href`; all keys external |
| S15 | [`preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf) | — | Typeset manuscript, 571,090 bytes |
| S16 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) | 18 | Author at 3, date at 5, citation block at 10–16 |
| S17 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/main.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/main.tex) | 33 | Title at 3, date at 5, abstract at 9–15, section inputs at 18–27, bibliography at 31–32 |
| S18 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/01-introduction.tex) | 330 | Setup at 3–12, `thm[intro:squares]` at 24–28, scope at 30–33, `thm[intro:branches]` at 41–55, companion citations at 62–63, `thm[intro:zp]` at 66–76, independence at 82–83, special closure at 88–92, prior results at 118–149, arithmetic estimates at 151–172, mechanism at 206–279 |
| S19 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/08-finiteness.tex`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/sections/08-finiteness.tex) | 390 | Companion scope at 6–7, `fin:orbit` at 26–35, `fin:classification` at 270, proof of `intro:zp` at 331–365, `cor:fin:special-closure` at 370–381 |
| S20 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/references.bib`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/build/references.bib) | 360 | Release entries `CompanionECM` at 162–168 and `CompanionQuaternion` at 169–175 |
| S21 | [`preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) | — | Typeset manuscript, 719,203 bytes |
| S22 | [`notes/t0-triage.md`](../../t0-triage.md) | 897 | Family 016 entry at 129–130 |
| S23 | [`notes/catalog.tsv`](../../catalog.tsv) | 373 | Ledger row for family 016 at 17 |

The PDF rows are the typeset form of each manuscript; the page quotes the LaTeX source, which is what the release ships alongside them [S7] [S10] [S15] [S21]. The four READMEs carry the release citation block for each manuscript [S3] [S8] [S11] [S16]. The four abstracts quoted from the driver files are the release's own summary of each paper [S4:9–12] [S9:53–56] [S12:20–24] [S17:9–15], and the family's own entry in the release overview is at 108 [S2:108].

Links are relative to this page's directory: `../../../` is the repository root and `../../` is `notes/`. Family pages cross-linked here: [002 — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one](002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md), [004 — Hilbert's tenth problem over ℚ](004-hilberts-tenth-problem-over-q.md), [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md), [010 — Fontaine–Mazur modularity at the prime 2](010-fontaine-mazur-modularity-at-the-prime-2.md), [011 — The Ford–Konyagin–Luca conjecture on prime predecessors](011-the-ford-konyagin-luca-conjecture-on-prime-predecessors.md), [018 — The Margulis–Platonov conjecture over global fields](018-margulis-platonov-conjecture-over-global-fields.md) and [019 — The $p$-adic section conjecture](019-p-adic-section-conjecture.md), the T0 number-theory pages already written. The upstream copies are [CONTENTS.md](../../../CONTENTS.md) and [overview.tex](../../../overview.tex); the triage record is [notes/t0-triage.md](../../t0-triage.md) and the ledger is [notes/catalog.tsv](../../catalog.tsv).

This page is checked by [notes/scripts/verify_summaries.py](../../scripts/verify_summaries.py), which resolves every `[Sn:line]` marker against the shipped file, checks every quotation verbatim against the lines it cites, counts a File cell that resolves under both roots as a problem, and writes nothing; `--mutant` corrupts one real quotation in each form this page uses and invents one.

Absent by construction (T0): `lean/docs/016.md`, any `lean/OAI/**` file, any `lean/ComparatorChallenges/` entry, any `main_results` config, any verification directory, any reasoning trace.
