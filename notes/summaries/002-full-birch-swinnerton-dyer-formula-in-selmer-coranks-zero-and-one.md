[Notes](../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 002](../index/number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md)

# 002 — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one

[Index page](../index/number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md)

## Original CONTENTS.md summary

The release's family entry, verbatim 

> **002. The full BSD formula from low Selmer corank.** Proves the full Birch–Swinnerton-Dyer leading-term formula for every elliptic curve over ℚ whose full *q*-power Selmer group has corank zero or one for some prime *q*, including finiteness of the Tate–Shafarevich group. With result 006, this gives full BSD for a density-one set of quadratic twists of every elliptic curve over ℚ. [S1:32]

The catalog abstract carries the same claim, names the pairing with 006 outright, and supplies the three display titles [S2:80]. The ledger records 3 manuscripts, tier T0, 0 formalized, `resolves_named` 0, claim shapes `density|uniform`, and 006 as the companion [S3:3].

The three manuscripts, in the order the release lists them, each with the display title the catalog gives it at [S2:80]. Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank 

> We prove the full Birch–Swinnerton-Dyer leading-term formula for every elliptic curve over ℚ whose full *q*-power Selmer group has corank zero or one at some prime *q*. The analytic and Mordell–Weil ranks equal that corank, and the Tate–Shafarevich group is finite. The formula includes all prime factors and requires no additional hypotheses on reduction, rational torsion, isogenies, complex multiplication, or residual Galois representations. [S1:41]

The Selmer converse for elliptic curves at every prime 

> We prove the Selmer converse in coranks zero and one for every elliptic curve over ℚ and every prime *p*: if the full *p*-power Selmer group has ℤ*p*-corank $`r\in\{0,1\}`$, then the analytic and Mordell–Weil ranks both equal *r*, and the entire Tate–Shafarevich group is finite. As an application at the additive prime 3, we prove that for every prime $`\ell\equiv4,7,8\pmod9`$, the cubic $`X^3+Y^3=\ell Z^3`$ has analytic and Mordell–Weil rank one and finite Tate–Shafarevich group. In particular, every such *ℓ* is a sum of two rational cubes. [S1:50]

The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one 

> We prove the two-primary Birch and Swinnerton-Dyer leading-term formula for every elliptic curve over the rationals whose two-power Selmer group has corank at most one. In this range, the algebraic rank, analytic rank, and Selmer corank are equal, and the Tate–Shafarevich group is finite. Combined with the quadratic-twist Selmer distribution, this gives the exact two-primary formula for a density-one set of signed squarefree twists of each fixed curve, ordered by absolute value; the common rank is zero or one, with each value having density one half. [S1:59]

Each blurb is the manuscript's own abstract, copied word for word from [S6:62–68], [S11:9–16] and [S16:60].

## Undergraduate summary

The weak Birch–Swinnerton-Dyer statement says an elliptic curve over ℚ has as many independent rational points as its L-function has orders of vanishing at s = 1. The strong statement is much more demanding: it pins the first nonzero Taylor coefficient to a product of the real period, the regulator of the rational points, the order of the Tate–Shafarevich group Sha, the Tamagawa numbers, and the rational torsion. Proving that product identity means getting every prime valuation of the quotient exactly right, which is a harder problem than proving the ranks agree.

Family 002 proves the exact formula for every curve whose full q-power Selmer group has corank 0 or 1, for some prime q chosen per curve. The hypothesis is about a Selmer group, not about rank, and the manuscript says so: "The low-Selmer-corank hypothesis is essential to the stated scope: it is not replaced here by a hypothesis on Mordell–Weil rank alone. [S7:69–71]" The covered class is not a list of special curve families; it is cut out by a cohomological size condition, and it applies to every curve that satisfies it, which is what the ledger's `uniform` tag records [S3:3].

The three manuscripts are not three attempts at one theorem. The second proves the rank-and-finiteness half — the Selmer converse — at every prime. The third proves the leading-term equality at the prime 2. The first proves the equality at every odd prime and states the division of labour in its own introduction: "The new assertion proved here is the exact valuation of the leading-term formula at every odd prime, independently of the prime $q$ in the hypothesis. [S7:67–69]" Its citation keys for the two inputs it borrows resolve to the family's own other two manuscripts [S8:150–162].

**Proof sketch (the exact-valuation manuscript).** Take the companion inputs as given: rank equality and finiteness of all of Sha from the Selmer converse, and the 2-part of the formula from the two-primary manuscript. Form the normalized quotient Q_E and the discrepancy X_p(E) = v_p(Q_E) − v_p(#Sha) [S7:141–148]. For a fixed odd prime p, prove two separate statements: X_p(E) ≥ 0 for non-CM curves of analytic rank at most one, and X_p(E) + X_p(E^D) = 0 for a suitable imaginary quadratic twist D with a(E) + a(E^D) = 1 [S7:156–161]. "Applying the first inequality to both curves in the second identity gives $X_p(E)=0$ in the non-CM case. [S7:162–163]" The integrality half is carried by finite free models of Galois cochain diagrams over Z_p[[t, u_1, …, u_m]], where t is a genuine character variable and the u_i are limits of tame characters [S7:171–174]; theta series then remove the remaining quotient divisors, so that specializing back to the center leaves a unit and the valuation comparison is exact [S7:169].

## Graduate summary

**Manuscript 1 — the exact valuation.** The theorem is stated at [S7:47–62]: for an elliptic curve E over ℚ and any prime q with s_q(E) in {0, 1}, r(E) = a(E) = s_q(E), Sha(E/ℚ) is finite, and L^(r)(E,1)/r! equals the BSD product under the normalizations fixed at [S7:26–44] — a real period over both connected components, the height convention at [S7:35–40], and no separate real-component factor. The scope sentence closes the statement: "There are no additional hypotheses on reduction, rational torsion, isogenies, complex multiplication, or residual Galois representations. [S7:60–61]" 

The division of labour is stated in the introduction 

> The rank and finiteness assertions are the unrestricted low-corank converse of  ; the two-primary leading-term equality is supplied by  . We state these inputs precisely in Section  . The new assertion proved here is the exact valuation of the leading-term formula at every odd prime, independently of the prime $q$ in the hypothesis. The low-Selmer-corank hypothesis is essential to the stated scope: it is not replaced here by a hypothesis on Mordell–Weil rank alone. [S7:64–71]

Those two citation keys are not external. \cite{C} is manuscript 2 and \cite{B} is manuscript 3, both listed in this manuscript's own bibliography with OpenAI as author [S8:150–162]; \cite{Goldfeld} is family 006's density manuscript [S8:143–148], and the entry records that its proof uses Smith's Selmer-distribution results [S8:184–188].

The mechanism is a pair comparison. The two outputs for a fixed odd prime p are the one-sided inequality X_p(E) ≥ 0 for non-CM curves of analytic rank at most one and the identity X_p(E) + X_p(E^D) = 0 for a suitable imaginary quadratic twist [S7:156–161], and the pair identity is what converts a one-sided bound into an equality [S7:162–163]. The integrality half is proved over the finite free models [S7:171–174]; residual cohomology gives divisibility of the determinant series, and theta series remove the remaining divisors so the central specialization is a unit [S7:169].

**Manuscript 2 — the converse at every prime.** The theorem at [S12:25–37] says that if the full p-power Selmer group of A_0 has ℤ_p-corank r in {0, 1}, then the analytic rank and the Mordell–Weil rank both equal r and Sha is finite. "There is no restriction on reduction type, complex multiplication, the residual representation, rational torsion, or rational isogenies. [S12:35–36]" Two sentences bound what it claims: "The finiteness conclusion concerns the entire Tate–Shafarevich group, not just its $p$-primary part. [S12:39–40]" and "it does not evaluate the leading coefficient in the refined Birch–Swinnerton-Dyer formula. [S12:42–44]" That second sentence is precisely the gap manuscript 1 fills, and manuscript 1's introduction names manuscript 2 as the source of the rank and finiteness half [S7:64–65].

**Manuscript 3 — the two-primary formula.** The scope paragraph at [S17:13–20] states the claim and its limits: "We establish the two-primary formula for every elliptic curve over \(\mathbb Q\) whose usual two-power Selmer group has corank zero or one. [S17:13–14]" and "it makes no assertion about higher Selmer corank or the remaining prime parts. [S17:19–20]" The theorem at [S17:54–71] produces a positive rational Q_E with v_2(Q_E) = v_2(#Sha), and "There is no restriction on \(E[2]\) or on the reduction of \(E\) at two. [S17:70]" Its corollary at [S17:73–82] imports the any-prime converse, and the proof at [S17:84–95] is three lines:

> By \cite[Theorem 1.1]OpenAIAllPrimeSelmer2026, \(\operatornamerankE(\mathbb Q)=r:=s_p(E)\) and the whole group \(\mathrmSha(E/\mathbb Q)\) is finite. [S17:85–87]

That citation key resolves to manuscript 2 in the same bibliography [S19:277–282], and the density input to family 006 [S19:270–275]. Three comparisons carry the proof — a positive comparison, a split-pair anchor, and a CM comparison [S17:219–241] — and the completion sits in the final section, where "The residual classification and the dyadic local comparisons cover every residual representation and every reduction type at two. [S18:76–78]" 

**What the family does not say.** No manuscript asserts BSD for a fixed curve, and none asserts the formula at Selmer corank ≥ 2. Manuscript 2 evaluates no leading coefficient [S12:42–44]; manuscript 3 speaks only at the prime 2 [S17:19–20]; manuscript 1 needs the Selmer hypothesis and not a rank hypothesis [S7:69–71]. The density statements are statements about twist families, not about a given curve.

**Formalization status.** The ledger row records tier T0 with 3 manuscripts and 0 formalized, no scope note, no comparator challenge, no `main_results` config, no verification directory, and no reasoning trace [S3:3]. Nothing about this family is machine-checked. The release describes its formalization scope as partial, its automation as agent-generated, and its review status as unchecked; for this family there is no formalization to review, so the only evidence is the LaTeX itself.

## History of the conjecture

BSD's own route was computational: "Birch and Swinnerton-Dyer formulated their conjectures from the relationship between the arithmetic of rational points and the behavior of the Euler product [S7:75–77]" , and Tate's account placed the rank prediction and the leading-term formula in the broader arithmetic of abelian varieties [S7:78–81]. The leading coefficient is a product, not a number: finite local components, torsion, the index of a point lattice, and the order of Sha must be compared simultaneously, which is why Cassels's isogeny formula is the natural invariant rather than any single factor [S7:82–86].

The rank half has a long history and the coefficient half is much younger. "Together with the work of Gross–Zagier and Kolyvagin, it shows that analytic rank zero or one implies the corresponding rational rank and finiteness of the whole Tate–Shafarevich group [S17:111–114]" , and manuscript 1 states plainly what that leaves open: "their rank and finiteness conclusions do not by themselves identify every prime valuation of the leading term. [S7:95–96]" "The converse from the full two-power Selmer group, and the exact leading coefficient at two, require additional integral information. [S17:115–117]" 

At odd primes, exact leading-term formulas in analytic ranks zero and one came with residual and local hypotheses — Skinner–Urban, Wei Zhang, and Jetchev–Skinner–Wan, through Iwasawa main conjectures and the integral theory of Heegner points [S17:122–126]. Manuscript 1 is explicit that these are not its input: "they are not used here as unrestricted odd-primary formulas. [S7:110–111]" In the CM case, Johnson–Leung–Kings establish the individual-character main conjecture "without prime exceptions [S17:132]" [S17:131–132], Burungale–Flach use that input to prove "full BSD for every CM elliptic curve over \(\mathbb Q\) of analytic rank zero [S17:133–134]" [S17:132–134], and Burungale–Tian's rank-zero p-converse, valid at every prime, shows the CM corank-zero case already follows [S17:134–137]. For CM curves of analytic rank one, "Li–Tian–Yan–Zhu prove the exact two-primary formula under good ordinary reduction at two. [S17:139–140]" 

The prime 2 is where this family's own contribution sits. Zhao, Coates–Li–Tian–Zhai, Cai–Li–Zhai, Shu–Zhai, and Kriz–Li each proved two-adic formulas under base-curve, local, isogeny, splitting, or Heegner-logarithm hypotheses [S17:147–161]; manuscript 3's contrast sentence is one line: "The present theorem permits every residual image and every reduction type at two. [S17:162–163]" The difficulty all of them are fighting is stated at "The integral difficulty is easy to describe. An Euler-system construction may produce a point or a determinant generator only after multiplication by a fixed nonzero integer. Such a bound can prove rank and finiteness, but its unknown two-adic valuation cannot determine \(v_2(Q_E)\). [S17:189–193]"

Prior (my training data, not this repo). Satgé's paired 3-isogeny descents (1987) are the classical source of rank-one finiteness at additive primes; the p-converse conjecture is usually associated with Mazur–Rubin, and Keller–Yin's formulation is the version the manuscript cites; Gross–Zagier (1986) and Kolyvagin (1990) are the standard reference for analytic rank at most one. The manuscripts name all of these and the repo supplies the citations, not the dates.

Manuscript 2's own history section is where the converse problem is placed: "The converse reverses this direction: a small Selmer group must force a nonzero central value or derivative. [S12:74–75]" Its application at the additive prime 3 uses the classical descent: "bound the full $3$-power Selmer corank by one, and the negative root sign selects analytic rank one. [S12:56–58]" 

## Consequences

The headline consequence is the pairing with 006, and the release states it inside the family entry: "With result 006, this gives full BSD for a density-one set of quadratic twists of every elliptic curve over ℚ. [S1:32]" The ledger records 006 as the companion [S3:3], and the triage note lists 002↔006 as one of three cross-family chains inside T0, with the caveat that "A chain is only as strong as its weakest, unformalized link. [S4:858–859]" The companion page is [006 — Goldfeld's analytic density conjecture and the 2-converse](006-goldfelds-conjecture.md); the chain partner of family 001 is [001 — Milne's rationality conjecture](001-milnes-rationality-conjecture.md).

The density corollary is manuscript 3's own, not a paraphrase of the blurb: corollary `cor:quadratic-twist-density` at [S18:82–118], proved at [S18:120–128]. "The proof of Theorem 1.2 in   gives density \(1/2\) for each of the usual full \(2\)-power Selmer coranks zero and one among the signed squarefree parameters ordered by absolute value. [S18:121–123]" Its non-claim sentence is equally explicit: "In particular, the exact two-primary formula holds on the density-one union of these subfamilies, whose common ranks are respectively zero and one. The density is in the full signed squarefree family for fixed \(E\); the formula asserts equality only at the prime two. [S18:113–117]" [S18:114–117] Manuscript 1 states the same dependency from its own side: "The auxiliary twist-density theorem  , whose proof uses Smith's Selmer-distribution results  , permits simultaneous choices of the two imaginary quadratic fields. [S7:118–121]" 

The family closes a dependency cycle inside the corpus. Manuscript 2 cites family 006's density theorem as a result it uses twice 

> The present proof uses two distinct results of  : the unrestricted converse at $2$ settles that prime, while the analytic twist-density theorem supplies the auxiliary fields for the odd-prime argument. [S12:126–129]

Manuscript 3 cites manuscript 2 for rank equality and finiteness [S17:85] and family 006 for the density input [S17:97–103]. Manuscript 1, dated October 7 and tied with manuscript 2 as the newest of the three [S5:5] against October 7 and October 6 for its siblings [S10:5] [S15:5], cites both of them by key [S7:64–71] and lists all three in its bibliography [S8:143–162]; manuscript 2 carries the density theorem as a bibentry of its own [S13:95–101]. So 006 → manuscript 2 → manuscript 3 → manuscript 1 is a closed chain of dependencies inside the release: no theorem outside the corpus carries the family, and the strongest link is the one with the most external support.

The concrete application is manuscript 2's: "A concrete application comes from Sylvester's cube-sum problem: which rational primes are sums of two rational cubes? [S12:46–47]" At the additive prime 3 the unrestricted converse turns a corank bound into a rank-one conclusion, and the release states the result in the manuscript's blurb: every prime ℓ ≡ 4, 7, 8 (mod 9) gives the cubic X³ + Y³ = ℓZ³ analytic and Mordell–Weil rank one with finite Tate–Shafarevich group, so every such ℓ is a sum of two rational cubes . The manuscript records that these cases "have also been treated by direct Heegner-point methods [S12:51–52]" , so the new content is the method, not the corollary.

What is not a consequence: BSD for a fixed curve; the leading coefficient at Selmer corank ≥ 2; any odd-prime statement from manuscript 3, which speaks only at 2 [S17:19–20]; the rank-and-finiteness half of manuscript 3, which it imports from manuscript 2 [S17:85]; and any density statement for a fixed curve beyond the twist-family density 006 supplies.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | Family entry at 32; manuscript blurbs at 41, 50 and 59; family 006's entry at 141, which does not name 002 |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The `\resultentry` at 80: the release's abstract for 002 and its three display titles |
| S3 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | Row 3 is family 002: tier, manuscript count, claim-shape tags, companion, and the zero evidence columns |
| S4 | [`notes/reports/t0-triage.md`](../../notes/reports/t0-triage.md) | 897 | Bucket legend at 17–25; the 002 entry at 114–116; the cross-family chain list at 858–859 |
| S5 | [`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md`](../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md) | 21 | Author line at 3, date line at 5, the release's own bibtex entry at 9–17, the version note at 19–21 naming the October-3 directory |
| S6 | [`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/main.tex`](../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/main.tex) | 82 | Title at 56, date at 58, abstract at 62–68; the ten section inputs |
| S7 | [`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/01-introduction.tex`](../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/01-introduction.tex) | 281 | Normalizations at 12–44; theorem at 47–62; inputs at 64–71; history at 75–137; discrepancy at 141–167; theta method at 169–267; organization at 269 |
| S8 | [`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/references.tex`](../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/references.tex) | 230 | The intra-corpus entries: Goldfeld at 143–148, C at 150–155, B at 157–162; Smith at 184–188 |
| S9 | [`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf`](../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf) | 25214 | The compiled exact-valuation manuscript, 874,353 bytes |
| S10 | [`preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/README.md`](../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/README.md) | 21 | Author line at 3, date line at 5, the version note at 19–21 naming the September-24 directory |
| S11 | [`preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/main.tex`](../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/main.tex) | 33 | Title at 3, date at 5, abstract at 9–16; the eleven section inputs |
| S12 | [`preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/sections/01-introduction.tex`](../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/sections/01-introduction.tex) | 269 | Theorem at 25–37; scope at 39–44; cube-sum application at 46–58; converse history at 60–134; proof strategy at 136 |
| S13 | [`preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/references.bib`](../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/build/references.bib) | 1070 | The intra-corpus entry OpenAIGoldfeldDensity2026 at 95–101, title at 97 |
| S14 | [`preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf`](../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf) | 24874 | The compiled converse manuscript, 869,458 bytes |
| S15 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/README.md`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/README.md) | 21 | Author line at 3, date line at 5, the version note at 19–21 naming the September-24 directory |
| S16 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/paper.tex`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/paper.tex) | 79 | Title at 55, date at 57, abstract at 60; the fifteen section inputs |
| S17 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/sections/01-introduction.tex`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/sections/01-introduction.tex) | 329 | Scope at 13–20; theorem at 54–71; any-prime criterion at 73–95; density paragraph at 97–103; history at 105–187; integral difficulty at 189–202; the three comparisons at 204–249 |
| S18 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/sections/15-conclusion.tex`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/sections/15-conclusion.tex) | 129 | Completion of the split-pair anchor at 3–27; proof of the theorem at 29–80; density corollary at 82–118 and its proof at 120–128 |
| S19 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/references.tex`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/references.tex) | 395 | The intra-corpus entries: OpenAIGoldfeldDensity2026 at 270–275 and OpenAIAllPrimeSelmer2026 at 277–282 |
| S20 | [`preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf`](../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf) | 37106 | The compiled two-primary manuscript, 1,279,386 bytes |

## Bibliography

- Ng{\^o}, Bao Ch{\^a}u, Le lemme fondamental pour les alg{\`e}bres de Lie (2010)
- Adams, Jeffrey, Johnson, Joseph F., Endoscopic groups and packets of non-tempered representations (1987)
- Amitsur, A. S., Levitzki, J., Minimal identities for algebras (1950)
- Andreatta, Fabrizio, Goren, Eyal Z., Hilbert modular forms: mod $p$ and $p$-adic aspects (2005)
- Arthur, James, Clozel, Laurent, Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula (1989)
- Arthur, James, A stable trace formula. I. General expansions (2002)
- Atobe, Hiraku, Gan, Wee Teck, Ichino, Atsushi, Kaletha, Tasho, Mínguez, Alberto, Shin, Sug Woo, Local Intertwining Relations and Co-tempered $A$-packets of Classical Groups (2026)
- Barnet-Lamb, Thomas, Gee, Toby, Geraghty, David, Taylor, Richard, Local-global compatibility for $l=p$, II (2014)
- Barnet-Lamb, Tom, Geraghty, David, Harris, Michael, Taylor, Richard, A Family of Calabi–Yau Varieties and Potential Automorphy II (2011)
- Bernstein, I. N., Zelevinsky, A. V., Induced representations of reductive $p$-adic groups. I (1977)
- Bernstein, J., Deligne, P., Kazhdan, D., Trace Paley–Wiener theorem for reductive $p$-adic groups (1986)
- Bertolini, Massimo, Darmon, Henri, Prasanna, Kartik, Generalized Heegner cycles and $p$-adic Rankin $L$-series (2013)
- M. Bertolini, H. Darmon, and K. Prasanna, _Generalized Heegner cycles and $p$-adic Rankin $L$-series_, with an appendix by B. Conrad, Duke Math. J. **162** (2013), no. 6, 1033–1148. doi:10.1215/00127094-2142056.
- M. Bertolini, H. Darmon, and R. Venerucci, _Heegner points and Beilinson–Kato elements: A conjecture of Perrin-Riou_, Adv. Math. **398** (2022), article 108172. doi:10.1016/j.aim.2021.108172.
- Besser, Amnon, Zerbes, Sarah Livia, Vologodsky integration on curves with semi-stable reduction (2017)
- Birch, Bryan J., Swinnerton-Dyer, H. P. F., Notes on elliptic curves. II (1965)
- F. A. Bogomolov, _Points of finite order on an abelian variety_, Izv. Akad. Nauk SSSR Ser. Mat. **44** (1980), no. 4, 782–804; English translation, Math. USSR-Izv. **17** (1981), no. 1, 55–72. English edition.
- F. A. Bogomolov, _Points of finite order on an abelian variety_, Izv. Akad. Nauk SSSR Ser. Mat. **44** (1980), 782–804; English translation, Math. USSR-Izv. **17** (1981), 55–72. English edition.
- Borade, Neelima, Franzel, Jonas, Girsch, Johannes, Yao, Wei, Yu, Qiyao, Zelingher, Elad, On tori periods of Weil representations of unitary groups (2025)
- Borel, Armand, Jacquet, Hervé, Automorphic forms and automorphic representations (1979)
- C. Breuil, B. Conrad, F. Diamond, and R. Taylor, _On the modularity of elliptic curves over $\mathbb Q$: wild $3$-adic exercises_, J. Amer. Math. Soc. **14** (2001), no. 4, 843–939. doi:10.1090/S0894-0347-01-00370-8.
- Breuil, Christophe, Conrad, Brian, Diamond, Fred, Taylor, Richard, On the modularity of elliptic curves over $\mathbf Q$: wild $3$-adic exercises (2001)
- C. Breuil, B. Conrad, F. Diamond, and R. Taylor, _On the modularity of elliptic curves over $\mathbb Q$: wild $3$-adic exercises_, J. Amer. Math. Soc. **14** (2001), no. 4, 843–939. doi:10.1090/S0894-0347-01-00370-8.
- J. P. Buhler, B. H. Gross, and D. B. Zagier, _On the conjecture of Birch and Swinnerton-Dyer for an elliptic curve of rank $3$_, Math. Comp. **44** (1985), 473–481. doi:10.2307/2007967.
- D. Bump, S. Friedberg, and J. Hoffstein, _Nonvanishing theorems for $L$-functions of modular forms and their derivatives_, Invent. Math. **102** (1990), 543–618. Article.
- Burungale, Ashay, Tian, Ye, A proof of Sylvester's conjecture (2026)
- Burungale, Ashay, Castella, Francesc, Skinner, Christopher, Tian, Ye, $p^\infty$-Selmer groups and rational points on CM elliptic curves (2022)
- Burungale, Ashay A., Skinner, Christopher, Tian, Ye, Wan, Xin, Zeta elements for elliptic curves and applications (2024)
- Burungale, Ashay, Castella, Francesc, Skinner, Christopher, Base Change and Iwasawa Main Conjectures for $\mathrm{GL}_2$ (2025)
- Burungale, Ashay A., Tian, Ye, A rank zero $p$-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin (2026)
- Burungale, Ashay, He, Wei, Tian, Ye, Ye, Xiangdong, Mod $\ell$ non-vanishing of self-dual Hecke $L$-values over CM fields and applications (2026)
- A. Burungale, F. Castella, C. Skinner, and Y. Tian, _$p^\infty$-Selmer groups and rational points on CM elliptic curves_, Ann. Math. Québec **46** (2022), no. 2, 325–346. doi:10.1007/s40316-022-00203-y.
- A. Burungale, C. Skinner, Y. Tian, and X. Wan, _Zeta elements for elliptic curves and applications_, arXiv:2409.01350v2 (2024).
- L. Cai, C. Li, and S. Zhai, _On the $2$-part of the Birch and Swinnerton-Dyer conjecture for quadratic twists of elliptic curves_, J. Lond. Math. Soc. **101** (2020), 714–734. doi:10.1112/jlms.12284.
- L. Cai, J. Shu, and Y. Tian, _Explicit Gross–Zagier and Waldspurger formulae_, Algebra Number Theory **8** (2014), no. 10, 2523–2572. Article.
- Caraiani, Ana, Monodromy and local-global compatibility for $l=p$ (2014)
- Carayol, Henri, Sur les représentations $\ell$-adiques associées aux formes modulaires de Hilbert (1986)
- Casselman, W., Introduction to the theory of admissible representations of $p$-adic reductive groups (1995)
- J. W. S. Cassels, _Arithmetic on curves of genus $1$. VIII. On conjectures of Birch and Swinnerton-Dyer_, J. Reine Angew. Math. **217** (1965), 180–199. doi:10.1515/crll.1965.217.180.
- J. W. S. Cassels, _Arithmetic on curves of genus $1$. VIII. On conjectures of Birch and Swinnerton-Dyer_, J. Reine Angew. Math. **217** (1965), 180–199. doi:10.1515/crll.1965.217.180.
- Castella, Francesc, Exceptional zeros for Heegner points and $p$-converse to the theorem of Gross–Zagier and Kolyvagin (2024)
- Castella, Francesc, Wan, Xin, Perrin-Riou's main conjecture for elliptic curves at supersingular primes (2024)
- Castella, Francesc, Grossi, Giada, Lee, Jaehoon, Skinner, Christopher, On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes (2022)
- Castella, Francesc, Liu, Zheng, Wan, Xin, Iwasawa–Greenberg main conjecture for nonordinary modular forms and Eisenstein congruences on $\mathrm{GU}(3,1)$ (2022)
- Castella, Francesc, Liu, Zheng, Wan, Xin, Addendum to: Iwasawa–Greenberg main conjecture for nonordinary modular forms and Eisenstein congruences on $\mathrm{GU}(3,1)$
- C.-L. Chai, _Families of ordinary abelian varieties: canonical coordinates, $p$-adic monodromy, Tate-linear subvarieties and Hecke orbits_, preprint, 30 July 2003. Author's manuscript.
- Chaudouard, Pierre-Henri, Laumon, Gérard, Le lemme fondamental pondéré. II. Énoncés cohomologiques (2012)
- Bellaïche, Joël, Chenevier, Gaëtan, Families of Galois Representations and Selmer Groups (2009)
- Chenevier, Gaëtan, Harris, Michael, Construction of automorphic Galois representations, II (2013)
- Clozel, Laurent, Delorme, Patrick, Le théor{\`e}me de Paley–Wiener invariant pour les groupes de Lie réductifs. II (1990)
- Cluckers, Raf, Hales, Thomas, Loeser, François, Transfer principle for the fundamental lemma (2011)
- Coates, John, Wiles, Andrew, On the conjecture of Birch and Swinnerton-Dyer (1977)
- J. Coates, Y. Li, Y. Tian, and S. Zhai, _Quadratic twists of elliptic curves_, Proc. Lond. Math. Soc. **110** (2015), 357–394. doi:10.1112/plms/pdu059.
- Colmez, Pierre, Fontaine, Jean-Marc, Construction des représentations $p$-adiques semi-stables (2000)
- B. Conrad, _Gross–Zagier revisited_, with an appendix by W. R. Mann, in _Heegner Points and Rankin $L$-Series_, H. Darmon and S.-W. Zhang (eds.), Math. Sci. Res. Inst. Publ. **49**, Cambridge University Press, 2004, 67–163. Author manuscript dated February 11, 2003.
- Tadić, Marko, Classification of unitary representations in irreducible representations of general linear group (non-Archimedean case) (1986)
- Drinfel'd, V. G., Two theorems on modular curves (1973)
- Dasgupta, Samit, Voight, John, Sylvester's problem and mock Heegner points (2018)
- Dokchitser, Tim, Dokchitser, Vladimir, On the Birch–Swinnerton-Dyer quotients modulo squares (2010)
- T. Dokchitser and V. Dokchitser, _On the Birch–Swinnerton-Dyer quotients modulo squares_, Ann. of Math. (2) **172** (2010), no. 1, 567–596. doi:10.4007/annals.2010.172.567.
- T. Dokchitser and V. Dokchitser, _Root numbers and parity of ranks of elliptic curves_, J. Reine Angew. Math. **658** (2011), 39–64. doi:10.1515/crelle.2011.060.
- V. G. Drinfeld, _Two theorems on modular curves_, Funct. Anal. Appl. **7** (1973), no. 2, 155–156. doi:10.1007/BF01078890.
- V. G. Drinfeld, _Two theorems on modular curves_, Funct. Anal. Appl. **7** (1973), no. 2, 155–156. doi:10.1007/BF01078890.
- G. Faltings, _Endlichkeitssätze für abelsche Varietäten über Zahlkörpern_, Invent. Math. **73** (1983), 349–366. doi:10.1007/BF01388432.
- A. A. Burungale and M. Flach, _The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication_, Cambridge J. Math. **12** (2024), no. 2, 357–415. Theorem locators follow arXiv:2206.09874v3, 4 September 2023.
- A. Burungale and M. Flach, _The conjecture of Birch and Swinnerton-Dyer for certain elliptic curves with complex multiplication_, Cambridge J. Math. **12** (2024), no. 2, 357–415. The theorem numbering used here is that of arXiv:2206.09874v2 (2022).
- W. T. Gan, Y. Qiu, and S. Takeda, _The regularized Siegel–Weil formula (the second term identity) and the Rallis inner product formula_, Invent. Math. **198** (2014), no. 3, 739–831. doi:10.1007/s00222-014-0509-0.
- Gan, Wee Teck, Takeda, Shuichiro, A proof of the Howe duality conjecture (2016)
- Gan, Wee Teck, Qiu, Yannan, Takeda, Shuichiro, The regularized Siegel–Weil formula (the second term identity) and the Rallis inner product formula (2014)
- Geisser, Thomas H., Suzuki, Takashi, Special values of $L$-functions of one-motives over function fields (2022)
- Gross, Benedict H., Zagier, Don B., Heegner points and derivatives of $L$-series (1986)
- Harris, Michael, Taylor, Richard, The Geometry and Cohomology of Some Simple Shimura Varieties (2001)
- Hartshorne, Robin, Algebraic Geometry (1977)
- H. Hida, _The Iwasawa $\mu$-invariant of $p$-adic Hecke $L$-functions_, Ann. of Math. (2) **172** (2010), no. 1, 41–137. doi:10.4007/annals.2010.172.41.
- Hida, Haruzo, Tilouine, Jacques, Anti-cyclotomic Katz $p$-adic $L$-functions and congruence modules (1993)
- S. Friedberg and J. Hoffstein, _Nonvanishing theorems for automorphic $L$-functions on $\mathrm{GL}(2)$_, Ann. of Math. (2) **142** (1995), no. 2, 385–423. doi:10.2307/2118638.
- Hsieh, Ming-Lun, On the non-vanishing of Hecke $L$-values modulo $p$ (2012)
- K. Česnavičius and N. Imai, _The remaining cases of the Kramer–Tunnell conjecture_, Compos. Math. **152** (2016), no. 11, 2255–2268. doi:10.1112/S0010437X16007624.
- R. Godement and H. Jacquet, _Zeta Functions of Simple Algebras_, Lecture Notes in Math. **260**, Springer-Verlag, Berlin–Heidelberg, 1972. doi:10.1007/BFb0070263.
- Jacquet, Hervé, Langlands, Robert P., Automorphic Forms on $\mathrm{GL}(2)$ (1970)
- D. Jetchev, C. Skinner, and X. Wan, _The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one_, Cambridge J. Math. **5** (2017), no. 3, 369–434. Published article.
- D. Jetchev, C. Skinner, and X. Wan, _The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one_, Cambridge J. Math. **5** (2017), no. 3, 369–434. Article.
- Kaletha, Tasho, Mínguez, Alberto, Shin, Sug Woo, White, Paul-James, Endoscopic Classification of Representations: Inner Forms of Unitary Groups (2014)
- S. Bloch and K. Kato, _$L$-functions and Tamagawa numbers of motives_, in _The Grothendieck Festschrift_, Vol. I, Progr. Math. **86**, Birkhäuser, Boston, 1990, 333–400. Publisher's reprint.
- K. Kato, _$p$-adic Hodge theory and values of zeta functions of modular forms_, Astérisque **295** (2004), 117–290. Article and bibliographic record.
- Kato, Kazuya, $p$-adic Hodge theory and values of zeta functions of modular forms (2004)
- S. Bloch and K. Kato, _$L$-functions and Tamagawa numbers of motives_, in _The Grothendieck Festschrift_, Vol. I, Progr. Math. **86**, Birkhäuser, 1990, 333–400. Reprint.
- K. Kato, _$p$-adic Hodge theory and values of zeta functions of modular forms_, Astérisque **295** (2004), 117–290. Article and bibliographic record.
- Katz, Nicholas M., $p$-adic interpolation of real analytic Eisenstein series (1976)
- Katz, Nicholas M., $p$-adic $L$-functions for CM fields (1978)
- Katz, Eric, Rabinoff, Joseph, Zureick-Brown, David, Uniform bounds for the number of rational points on curves of small Mordell–Weil rank (2016)
- Katz, Nicholas M., Serre–Tate local moduli (1981)
- Keller, Timo, Yin, Mulun, $p$-converse theorems for elliptic curves of potentially good ordinary reduction at Eisenstein primes (2024)
- Keller, Timo, Yin, Mulun, On the anticyclotomic Iwasawa theory of newforms at Eisenstein primes of semistable reduction (2024)
- J. Johnson-Leung and G. Kings, _On the equivariant main conjecture for imaginary quadratic fields_, J. Reine Angew. Math. **653** (2011), 75–114. doi:10.1515/CRELLE.2011.020.
- V. A. Kolyvagin, _Euler systems_, in _The Grothendieck Festschrift_, Vol. II, Progr. Math. **87**, Birkhäuser, Boston, 1990, 435–483. Publisher's reprint.
- Kolyvagin, V. A., Euler systems (1990)
- V. A. Kolyvagin, _Euler systems_, in _The Grothendieck Festschrift_, Vol. II, Progr. Math. **87**, Birkhäuser, 1990, 435–483. Publisher record.
- K. Kramer, _Arithmetic of elliptic curves upon quadratic extension_, Trans. Amer. Math. Soc. **264** (1981), no. 1, 121–135. doi:10.1090/S0002-9947-1981-0597871-8.
- Kriz, Daniel, Supersingular main conjectures, Sylvester's conjecture and Goldfeld's conjecture (2022)
- Kudla, Stephen S., Splitting metaplectic covers of dual reductive pairs (1994)
- Labesse, Jean-Pierre, Changement de base CM et séries discr{\`e}tes (2011)
- Lan, Kai-Wen, Arithmetic Compactifications of PEL-Type Shimura Varieties (2013)
- Lan, Kai-Wen, Compactifications of PEL-Type Shimura Varieties and Kuga Families with Ordinary Loci (2018)
- D. Kriz and C. Li, _Goldfeld's conjecture and congruences between Heegner points_, Forum Math. Sigma **7** (2019), e15, 80 pp. doi:10.1017/fms.2019.9.
- Y. Li, Y. Tian, X. Yan, and X. Zhu, _On the Birch-Swinnerton-Dyer conjecture for rational elliptic curves with complex multiplication and analytic rank one_, Pure Appl. Math. Q., online publication (2025). doi:10.4310/PAMQ.251115004959; author manuscript.
- Yu. I. Manin, _Parabolic points and zeta-functions of modular curves_, Math. USSR-Izv. **6** (1972), no. 1, 19–64. doi:10.1070/IM1972v006n01ABEH001867.
- Manin, Yu. I., Parabolic points and zeta-functions of modular curves (1972)
- N. M. Katz and B. Mazur, _Arithmetic Moduli of Elliptic Curves_, Annals of Mathematics Studies **108**, Princeton University Press, Princeton, NJ, 1985. Publisher's digital edition.
- N. M. Katz and B. Mazur, _Arithmetic Moduli of Elliptic Curves_, Annals of Mathematics Studies **108**, Princeton University Press, 1985.
- J. S. Milne, _On the arithmetic of abelian varieties_, Invent. Math. **17** (1972), 177–190. doi:10.1007/BF01425446.
- J. S. Milne, _Arithmetic Duality Theorems_, second edition, BookSurge, 2006. Author's edition and corrections.
- Milne, J. S., Arithmetic Duality Theorems (2006)
- J. S. Milne, _Arithmetic Duality Theorems_, second edition, BookSurge, 2006. Author's edition and corrections.
- Mok, Chung Pang, Endoscopic Classification of Representations of Quasi-Split Unitary Groups (2015)
- F. Knudsen and D. Mumford, _The projectivity of the moduli space of stable curves. I: Preliminaries on ``det'' and ``Div''_, Math. Scand. **39** (1976), 19–55. doi:10.7146/math.scand.a-11642.
- M. R. Murty and V. K. Murty, _Mean values of derivatives of modular $L$-series_, Ann. of Math. (2) **133** (1991), no. 3, 447–475. doi:10.2307/2944316.
- Mœglin, Colette, Waldspurger, Jean-Loup, Le spectre résiduel de $\mathrm{GL}(n)$ (1989)
- J. Nekovář, _Selmer complexes_, Astérisque **310** (2006), viii+559 pp. Book.
- J. Nekovář, _Selmer complexes_, Astérisque **310** (2006), viii+559 pp. Book.
- Neukirch, Jürgen, Schmidt, Alexander, Wingberg, Kay, Cohomology of Number Fields (2008)
- Neukirch, Jürgen, Algebraic Number Theory (1999)
- Newton, James, Towards local-global compatibility for Hilbert modular forms of low weight (2015)
- OpenAI, _Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves_, OpenAI Math Release preprint OAI:Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026, 2026.
- OpenAI, _The Selmer converse for elliptic curves at every prime_, OpenAI Math Release preprint OAI:The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026, 2026.
- OpenAI, _The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one_, OpenAI Math Release preprint OAI:The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026, 2026.
- OpenAI, {Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves} (2026)
- OpenAI, _Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves_, OpenAI Math Release preprint OAI:Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026, 2026.
- OpenAI, _The Selmer converse for elliptic curves at every prime_, OpenAI Math Release preprint OAI:The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026, 2026.
- H. Oukhaba, _Index formulas for ramified elliptic units_, Compos. Math. **137** (2003), no. 1, 1–22. doi:10.1023/A:1023667807218.
- B. Perrin-Riou, _Fonctions $L$ $p$-adiques d'une courbe elliptique et points rationnels_, Ann. Inst. Fourier **43** (1993), no. 4, 945–995. doi:10.5802/aif.1362.
- C. Fuchs and D. H. Pham, _The $p$-adic analytic subgroup theorem revisited_, $p$-Adic Numbers Ultrametric Anal. Appl. **7** (2015), no. 2, 143–156. doi:10.1134/S2070046615020065; arXiv:1502.00768v1.
- U. K. Anandavardhanan and D. Prasad, _A local-global question in automorphic forms_, Compos. Math. **149** (2013), 959–995. Author manuscript.
- Procesi, Claudio, A formal inverse to the Cayley–Hamilton theorem (1987)
- Rallis, Stephen, Injectivity properties of liftings associated to Weil representations (1984)
- E. Lapid and S. Rallis, _On the nonnegativity of $L(\tfrac12,\pi)$ for $\mathrm{SO}_{2n+1}$_, Ann. of Math. (2) **157** (2003), no. 3, 891–917. doi:10.4007/annals.2003.157.891.
- P. Deligne and M. Rapoport, _Les schémas de modules de courbes elliptiques_, in _Modular Functions of One Variable II_, Lecture Notes in Math. **349**, Springer, Berlin, 1973, 143–316. Publisher record.
- P. Deligne and M. Rapoport, _Les schémas de modules de courbes elliptiques_, in _Modular Functions of One Variable II_, Lecture Notes in Math. **349**, Springer, 1973, 143–316. Publisher record.
- Salamanca Riba, Susana, On the unitary dual of some classical Lie groups (1988)
- Ribet, Kenneth A., A modular construction of unramified $p$-extensions of $\mathbf{Q}(\mu_p)$ (1976)
- K. A. Ribet, _Galois representations attached to eigenforms with Nebentypus_, in _Modular Functions of One Variable V_, J.-P. Serre and D. B. Zagier (eds.), Lecture Notes in Math. **601**, Springer, 1977, 17–52. doi:10.1007/BFb0063943.
- D. E. Rohrlich, _$L$-functions and division towers_, Math. Ann. **281** (1988), 611–632. doi:10.1007/BF01456842.
- K. Rubin, _The ``main conjectures'' of Iwasawa theory for imaginary quadratic fields_, Invent. Math. **103** (1991), 25–68. doi:10.1007/BF01239508.
- B. Mazur and K. Rubin, _Kolyvagin systems_, Mem. Amer. Math. Soc. **168** (2004), no. 799, viii+96 pp. doi:10.1090/memo/0799.
- B. Mazur and K. Rubin, _Ranks of twists of elliptic curves and Hilbert's tenth problem_, Invent. Math. **181** (2010), 541–575. doi:10.1007/s00222-010-0252-0.
- K. Rubin, _The ``main conjectures'' of Iwasawa theory for imaginary quadratic fields_, Invent. Math. **103** (1991), 25–68. doi:10.1007/BF01239508.
- Satgé, Ph., Quelques résultats sur les entiers qui sont somme des cubes de deux rationnels (1987)
- M. Schütt, _CM newforms with rational coefficients_, Ramanujan J. **19** (2009), 187–205. doi:10.1007/s11139-008-9147-8. The theorem numbering used here is that of arXiv:math/0511228v5 (2008).
- J.-P. Serre, _Propriétés galoisiennes des points d'ordre fini des courbes elliptiques_, Invent. Math. **15** (1972), 259–331. doi:10.1007/BF01405086.
- Serre, Jean-Pierre, Abelian $\ell$-adic representations and elliptic curves (1968)
- Serre, Jean-Pierre, Propriétés galoisiennes des points d'ordre fini des courbes elliptiques (1972)
- J.-P. Serre, _Abelian $\ell$-Adic Representations and Elliptic Curves_, W. A. Benjamin, 1968.
- J.-P. Serre, _Propriétés galoisiennes des points d'ordre fini des courbes elliptiques_, Invent. Math. **15** (1972), 259–331. Article.
- Shin, Sug Woo, Galois representations arising from some compact Shimura varieties (2011)
- Shin, Sug Woo, Weak transfer from classical groups to general linear groups (2024)
- Shirshov, A. I., On rings with identity relations (1957)
- J. H. Silverman, _The Arithmetic of Elliptic Curves_, second edition, Graduate Texts in Mathematics **106**, Springer, 2009. doi:10.1007/978-0-387-09494-6.
- Skinner, Christopher, A converse to a theorem of Gross, Zagier, and Kolyvagin (2020)
- Skinner, Christopher, Urban, Eric, The Iwasawa Main Conjectures for $\mathrm{GL}_2$ (2014)
- A. Smith, _The Birch and Swinnerton-Dyer conjecture implies Goldfeld's conjecture_, arXiv:2503. 17619v1, 2025.
- B. Poonen and M. Stoll, _The Cassels–Tate pairing on polarized abelian varieties_, Ann. of Math. (2) **150** (1999), no. 3, 1109–1149. doi:10.2307/121064; corrected author version, August 23, 2014.
- B. J. Birch and H. P. F. Swinnerton-Dyer, _Notes on elliptic curves. II_, J. Reine Angew. Math. **218** (1965), 79–108. doi:10.1515/crll.1965.218.79.
- B. J. Birch and H. P. F. Swinnerton-Dyer, _Notes on elliptic curves. II_, J. Reine Angew. Math. **218** (1965), 79–108. doi:10.1515/crll.1965.218.79.
- J. Tate, _On the conjectures of Birch and Swinnerton-Dyer and a geometric analog_, Séminaire Bourbaki **9** (1966), Exp. 306, 415–440. Article and bibliographic record.
- J. Tate, _On the conjectures of Birch and Swinnerton-Dyer and a geometric analog_, Séminaire Bourbaki, Vol. 9, exp. 306 (1965/66), 415–440. Article.
- A. A. Burungale and Y. Tian, _A rank zero $p$-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin_, Ann. of Math. (2) **203** (2026), no. 1, 1–13. doi:10.4007/annals.2026.203.1.1.
- K. Kramer and J. Tunnell, _Elliptic curves and local $\epsilon$-factors_, Compos. Math. **46** (1982), no. 3, 307–352. Article.
- C. Skinner and E. Urban, _The Iwasawa main conjectures for $\mathrm{GL}_2$_, Invent. Math. **195** (2014), no. 1, 1–277. doi:10.1007/s00222-013-0448-1.
- C. Skinner and E. Urban, _The Iwasawa main conjectures for $\mathrm{GL}_2$_, Invent. Math. **195** (2014), 1–277. doi:10.1007/s00222-013-0448-1.
- J.-L. Waldspurger, _Sur les valeurs de certaines fonctions $L$ automorphes en leur centre de symétrie_, Compos. Math. **54** (1985), no. 2, 173–242. Article and bibliographic record.
- Waldspurger, Jean-Loup, Sur les valeurs de certaines fonctions L automorphes en leur centre de symétrie (1985)
- Waldspurger, Jean-Loup, A propos du lemme fondamental pondéré tordu (2009)
- S. Wang, _Le syst\`eme d'Euler de Kato_, arXiv:1211.3767v1 (2012).
- Weil, André, Sur certains groupes d'opérateurs unitaires (1964)
- R. Taylor and A. Wiles, _Ring-theoretic properties of certain Hecke algebras_, Ann. of Math. (2) **141** (1995), no. 3, 553–572. doi:10.2307/2118560.
- A. Wiles, _Modular elliptic curves and Fermat's Last Theorem_, Ann. of Math. (2) **141** (1995), no. 3, 443–551. doi:10.2307/2118559.
- Wiles, Andrew, The Iwasawa conjecture for totally real fields (1990)
- R. Taylor and A. Wiles, _Ring-theoretic properties of certain Hecke algebras_, Ann. of Math. (2) **141** (1995), no. 3, 553–572. doi:10.2307/2118560.
- A. Wiles, _Modular elliptic curves and Fermat's Last Theorem_, Ann. of Math. (2) **141** (1995), no. 3, 443–551. doi:10.2307/2118559.
- S. Yamana, _On the Siegel–Weil formula: The case of singular forms_, Compos. Math. **147** (2011), no. 4, 1003–1021. doi:10.1112/S0010437X11005379.
- Yamana, Shunsuke, On the Siegel–Weil formula: The case of singular forms (2011)
- Yin, Hongbo, A proof of the $4,7$ cases of Sylvester's conjecture on cube sums (2026)
- Yin, Hongbo, Gross–Zagier formula for the $4,7$ cases of Sylvester's conjecture (2026)
- B. H. Gross and D. B. Zagier, _Heegner points and derivatives of $L$-series_, Invent. Math. **84** (1986), no. 2, 225–320. doi:10.1007/BF01388809.
- B. H. Gross and D. B. Zagier, _Heegner points and derivatives of $L$-series_, Invent. Math. **84** (1986), 225–320. doi:10.1007/BF01388809.
- Yu. G. Zarhin, _Abelian varieties over fields of finite characteristic_, Cent. Eur. J. Math. **12** (2014), no. 5, 659–674. Theorem locators follow arXiv:1301.5594v4, 16 April 2015.
- Zelevinsky, A. V., Induced representations of reductive $p$-adic groups. II. On irreducible representations of $\mathrm{GL}(n)$ (1980)
- J. Shu and S. Zhai, _Generalized Birch lemma and the $2$-part of the Birch and Swinnerton-Dyer conjecture for certain elliptic curves_, J. Reine Angew. Math. **775** (2021), 117–143. arXiv:2102.11808v1.
- Zhang, Wei, Selmer groups and the indivisibility of Heegner points (2014)
- W. Zhang, _Selmer groups and the indivisibility of Heegner points_, Cambridge J. Math. **2** (2014), no. 2, 191–253. doi:10.4310/CJM.2014.v2.n2.a2.
- C. Zhao, _A criterion for elliptic curves with lowest $2$-power in $L(1)$_, Math. Proc. Cambridge Philos. Soc. **121** (1997), 385–400. doi:10.1017/S0305004196001247.
- Halleck-Dubé, Connor, The Weighted Fundamental Lemma for Non-Split Groups (n.d.)
- Nekovář, Jan, Selmer complexes (2006)
