[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 004](../index/number-theory/004-hilberts-tenth-problem-over-q.md)

# 004 — Hilbert's tenth problem over $\mathbb Q$

[Index page](../index/number-theory/004-hilberts-tenth-problem-over-q.md)

## Original CONTENTS.md summary

The release entry for the family reads [S1:100]:

> **004. Hilbert's tenth problem over ℚ.** Proves that no algorithm decides whether an integer-coefficient polynomial in an arbitrary number of variables has a rational zero, resolving Hilbert's tenth problem over ℚ negatively.

The family ships two manuscripts, and the release describes them as two different kinds of theorem. The first 

> We give a negative answer to Hilbert's tenth problem over the rational numbers: no algorithm decides whether a polynomial with integer coefficients has a rational zero. The number of variables is part of the input. [S4:64–66]

The second 

> We prove a pointwise $2$-converse for elliptic curves over $\mathbf Q$ with nonzero rational two-torsion: if the $2^\infty$-Selmer corank is zero or one, then the analytic rank and Mordell–Weil rank equal that corank, and the Shafarevich–Tate group is finite. The result allows arbitrary reduction at $2$. [S9:60–64]

The pairing is not two versions of one claim. The undecidability manuscript is the headline; the elliptic-curve manuscript is an arithmetic input that headline's proof consumes. The roadmap says so — "its passage from two-descent data to rational points uses the pointwise $2$-converse [S5:232–234]" — and the undecidability manuscript carries that result in its own bibliography, under the key `PointwiseTwoConverse` [S7:16–23].

## Undergraduate summary

Hilbert's tenth problem asks for an algorithm that, given a polynomial with integer coefficients, decides whether it has an integer solution. That question was closed in 1970: no such algorithm exists. Family 004 answers the rational version — same input, same question, with a solution in ℚ replacing a solution in ℤ. The manuscript states its result as 

> There is no algorithm which, given a polynomial $f\in\mathbb Z[X_1,\ldots,X_n]$, with $n$ part of the input, decides whether $f$ has a zero in $\mathbb Q^n$. [S5:8–10]

The clause "with $n$ part of the input [S5:9]" is load-bearing. If the number of variables were fixed in advance, the question would be a different one; the theorem is about the full problem, where the polynomial arrives with any number of variables attached.

The proof is a reduction, not a machine that fails. It shows that the integer problem — already known to be undecidable — can be answered by asking the rational problem a bounded number of times. The mechanism is a parallel search 

> An integer zero supplies witnesses for all the tests. If a rational-solvability algorithm existed, we could run two searches in parallel: enumeration of integer zeros, and enumeration of tests until one fails. The arithmetic work is to prove that a failed test exists whenever \(f\) has no integer zero. [S5:181]

So the entire burden is one implication: if a polynomial has no integer zero, then at least one of a finite list of effectively computable tests fails. The reduction produces that list as the equivalence at [S5:176–180], and everything else in the paper exists to force a failure.

The tests are comparisons of size. Each candidate solution is attached to a point on an elliptic curve, and the proof needs an upper bound on the height of the ring element representing that point — "let \(M(s)\) be the product, without repetition, of the nonexceptional primes at which one of these forms has odd valuation [S5:192]" , with the estimate "h(s)\le H M(s)^c [S5:194]" displayed just below it — and a lower bound coming from the canonical height of the attached point. The two bounds collide unless the modelled root coordinates are an ordinary finite interval of integers, which is the elementarity the reduction needs 

> If \(\delta=0\), elementarity gives an ordinary integer zero of \(f\). [S5:213]

The arithmetic that makes the height bound uniform is a 2-converse statement about Selmer groups, and that is why the family's second manuscript sits in this family rather than beside it.

**The shape of the proof, in six moves.** (1) Encode the integers inside a ring whose elements are built from ℚ, and attach to each candidate root a point on an elliptic curve. (2) Produce the finite test family: "we construct an effectively generated sequence of finite tests [S5:174]" , each a finite computation in a residue ring, a height box, and local solvability conditions. (3) Prove the pole-parity condition, which is where two-descent data becomes rational points . (4) Prove the five-point height estimate, whose modularity step is a Fontaine–Mazur theorem at 2 . (5) Force the contradiction \(B^2\ll_f B\) [S5:224–225]. (6) Read off undecidability, and record the exact complexity .

## Graduate summary

**The headline theorem.** — no algorithm decides, for a polynomial in $\mathbb Z[X_1,\ldots,X_n]$ with $n$ part of the input, whether it has a zero in $\mathbb Q^n$. The abstract of the manuscript states the same claim in prose 

> We give a negative answer to Hilbert's tenth problem over the rational numbers: no algorithm decides whether a polynomial with integer coefficients has a rational zero. The number of variables is part of the input. [S1:109]

**The moves, as the paper organises them.**

1. **The finite-test interface.** The reduction is stated as an interface, not as a definition of ℤ inside ℚ: "For each nonconstant integral polynomial \(f\), we construct an effectively generated sequence of finite tests [S5:173–174]" , and the interface is the equivalence "f has an integer zero [S5:177]" ⟺ "every test succeeds [S5:179]" [S5:176–180], each test answerable by finitely many rational-solvability queries.
2. **The parity step.** Section 3 of the manuscript proves the pole-parity condition, and its passage from two-descent data to rational points is the pointwise 2-converse [S5:232–234], paired with the Cassels–Tate pairing. This is the family's internal dependency: the headline proof consumes the family's second manuscript.
3. **The height step.** Section 4 proves the five-point height estimate, and "Its modularity step uses the odd regular Fontaine–Mazur theorem at $2$ [S5:236–237]" , "whose statement has no hypothesis on the residual image [S5:238–239]" . Both inputs are inside the release: the 2-converse is this family's own second manuscript [S7:16–23], the Goldfeld-form 2-converse is family 006 [S7:24–31], and the Fontaine–Mazur theorem at 2 is family 010 [S7:32–39].
4. **The quantitative core.** Two parameters carry the contradiction: \(\delta=f(\eta(a_1),\ldots,\eta(a_n))\) and \(B=\max(1,|\eta(a_1)|,\ldots,|\eta(a_n)|)\) are set at [S5:208–212], and the paper states what \(\delta\) is worth — "Otherwise \(\delta\) is a nonzero ambient integer whose size is bounded by a fixed polynomial in \(B\) [S5:213]" — and what the collision is — "the two bounds give \(B^2\ll_f B\) [S5:225]" . The left side is the canonical height of the attached point, growing quadratically in $|\eta(a_j)|$; the right side is the reduction's uniform height bound.
5. **The closure.** The root-coordinate contradiction 

> For each nonzero root coordinate \(a_j\), consider its attached point \(T_a_j\). Applying the uniform bound to the ring elements representing \(x(T_a_j)\) gives \(h(x(\eta(a_j)P))\ll_f B\). The transferred canonical-height comparison for \(P\) makes this height grow quadratically in \(|\eta(a_j)|\). If \(B>1\), choose \(j\) with \(|\eta(a_j)|=B\); the two bounds give \(B^2\ll_f B\). If \(B=1\), the required bound is immediate. Thus all root indices lie in an ordinary finite interval. Additivity and injectivity identify the modeled root coordinates with those ordinary integers, contradicting \(\delta\ne0\). This proves the finite-test equivalence and hence the undecidability theorem. [S5:220–229]

6. **The exact complexity.** The consequences section fixes the Turing degree 

> With the usual effective coding, let \(\mathrmH10(\mathbb Q)\) be the set of integral polynomials having a rational zero, with the number of variables part of the input. Then \(\mathrmH10(\mathbb Q)\) has Turing degree \(0'\), the degree of the halting problem. [S6:9–12]

The proof of that corollary runs in both directions: $\mathrm{H10}(\mathbb Z)\le_T\mathrm{H10}(\mathbb Q)$ from the reduction, and the converse from enumerability — "Rational solvability is also computably enumerable [S6:49]" — and it ends by normalising the presentation to degree four, "The expanded polynomial has integral coefficients and total degree at most four [S6:95–96]" .

**The companion theorem.** The second manuscript's headline is a pointwise 2-converse 

> Let $E/\mathbb Q$ be an elliptic curve with $E(\mathbb Q)[2]\ne0$ and $s_2(E)\in\{0,1\}$. Then \[ \mathrmord_s=1L(E,s)=\mathrmrank_{\mathbb Z}E(\mathbb Q)=s_2(E), \qquad \operatornameSha(E/\mathbb Q) is finite. \] [S10:23–29]

Its abstract states the same claim in prose 

> We prove a pointwise 2-converse for elliptic curves over $`\mathbf Q`$ with nonzero rational two-torsion: if the $`2^\infty`$-Selmer corank is zero or one, then the analytic rank and Mordell–Weil rank equal that corank, and the Shafarevich–Tate group is finite. The result allows arbitrary reduction at 2. [S1:118]

Its scope is stated as a range, not as a hypothesis on the curve [S10:32–37]:

> The statement includes one rational two-torsion line and full rational two-torsion, CM and non-CM curves, every rational isogeny configuration, and every reduction type at $2$ and at the bad primes. [S10:32–34]

and its relation to the family's other 2-converse is explicit 

> The broader companion \cite[Theorem 1.1]OpenAIGoldfeldTwoConverse2026 proves the $2$-converse without the rational-two-torsion hypothesis. Here we give a separate full treatment of the rational-two-torsion case, developing its integral interpolation and finite twist constructions within this paper; the broader converse is not an input to the proof. [S10:39–43]

So the dependency inside family 004 runs one way: the undecidability manuscript uses the pointwise converse; the pointwise converse does not use the broader converse of family 006, even though it cites it [S11:349–355].

**What the pair does not say.** The undecidability result is a negative answer, not an exhibited object, and the release's own reading record says so: "004 is a negative *resolution* of Hilbert's tenth problem over **Q**, not an exhibited object [S14:534]" . The corollary section is equally explicit about its own limits 

> The many-one reduction to the restricted problems starts from \(\mathrmH10(\mathbb Q)\); the reduction from \(\mathrmH10(\mathbb Z)\) remains a Turing reduction. This argument does not establish many-one completeness of \(\mathrmH10(\mathbb Q)\). The list in (ii) is supplied as part of the input, so no recognition of sum-of-squares presentations is needed. The construction supplies no bound on the number of variables or coefficient heights, and it gives no single existential definition of \(\mathbb Z\) in \(\mathbb Q\). [S6:100–107]

That last clause is the one to hold onto: this proof does not produce an existential definition of ℤ in ℚ, which is the route the number-field results take [S5:129–134], and the manuscript says plainly that ℚ is outside the class of rings those results cover — "The field \(\mathbb Q\) is not a finitely generated \(\mathbb Z\)-algebra [S5:141–142]" . On the elliptic-curve side, the companion theorem bounds its own claim "It is a $2$-converse in this residual range. It does not assert the full Birch–Swinnerton-Dyer leading-coefficient formula, nor does a bound $\mathrm{rank} E(\mathbb Q)\le1$ alone imply its Selmer hypothesis. [S10:34–37]"

**Formalization status.** The ledger row for 004 records 2 manuscripts, 0 formalized, no scope note, no comparator challenge, no `main_results` config, no verification directory, no reasoning trace, tier T0 [S15:5]. Nothing about this family is machine-checked. It is the only T0 family carrying the `undecidability` claim-shape tag [S14:117–118], and it is one of the six T0 families that the narrow counterexample tag misses and the wider phrase rule catches [S16:145–146]. The rule matches the release's own wording — "resolving Hilbert's tenth problem over $\mathbb Q$ negatively [S2:84]" — and the reading verdict recorded for the family is "a negative resolution, not an exhibited object [S16:65]" [S16:65–67].

## History of the conjecture

Prior (my training data, not this repo.) Hilbert's tenth problem dates to 1900. The chain that settled the integer case runs Davis–Putnam–Robinson–Matiyasevich, with Matiyasevich's 1970 theorem on recursively enumerable sets supplying the last step; after that, the rational case became the standard open transfer problem. Julia Robinson's own work on the rationals predates the integer resolution. Poonen's 2009 conditional result — ℤ Diophantine in ℚ assuming squarefree rank for a specific elliptic curve — is the form the question took in the twenty-first century, and the Mazur–Rubin conjecture on ranks in quadratic-twist families became the standard hypothesis under which the transfer goes through.

The manuscript's own history section is the check on that. It opens with the integer case: "Davis, Putnam, and Robinson proved in 1961 that every recursively enumerable relation has such a representation if exponentiation is also allowed [S5:27–29]" , and "Matiyasevich supplied the required growth in 1970 through a Diophantine description of a Fibonacci relation [S5:32–33]" , which completes "the theorem that every recursively enumerable relation on the positive integers is Diophantine [S5:33–35]" — "The equivalent all-integer decision problem is therefore undecidable [S5:35–36]" . Definability inside ℚ was settled long before that, and the manuscript is explicit that it is not the transfer: "Julia Robinson showed in 1949 that the integers are first-order definable in the rationals using addition and multiplication [S5:59–60]" , Poonen's positive formula used "two universal quantifiers followed by seven existential quantifiers [S5:65–66]" , and Koenigsmann "gave a universal definition of \(\mathbb Z\); equivalently, its complement in \(\mathbb Q\) is Diophantine [S5:67–69]" . The geometric obstruction is recorded too — Mazur's conjecture on the closure of rational points "would rule out a Diophantine definition of \(\mathbb Z\) in \(\mathbb Q\) [S5:81–82]" [S5:80–82], and the manuscript notes that "These obstructions to definitions and models do not by themselves rule out a negative answer to the rational decision problem [S5:85–87]" . The subring line reaches proper subrings of ℚ: Poonen built them from "selected multiples of a point on a rank-one elliptic curve whose real coordinates approximate integers [S5:98–100]" , and Eisenträger–Miller–Park–Shlapentokh produced rings whose "Hilbert's tenth problem is Turing equivalent to that over \(\mathbb Q\) [S5:104–105]" , with the caveat that "The density of the inverted primes alone therefore does not settle the relation to the field problem [S5:109–111]" .

The number-field route is the one that closed first. Mazur and Rubin proposed the rank bound for quadratic twists and, "Assuming this for every elliptic curve over every number field, they obtained undecidability for every infinite finitely generated \(\mathbb Z\)-algebra [S5:125–126]" [S5:125–127]. That conditional was removed after this release's own manuscripts: "Koymans and Pagano combined two-descent with additive combinatorics to prove that \(\mathbb Z\) is Diophantine in the ring of integers of every number field [S5:130–132]" [S5:129–132], and Alpöge–Bhargava–Ho–Shnidman settled the corresponding density statement [S5:135–140]. The manuscript is precise about why none of that touches ℚ 

> The field \(\mathbb Q\) is not a finitely generated \(\mathbb Z\)-algebra, so these results concern a different class of rings from the field in Theorem [S5:141–143]

The prior work on definability inside ℚ is summarised as control, not as a solution: "These results give substantial control of definitions inside \(\mathbb Q\), but do not supply the existential membership condition for the direct transfer above [S5:71–74]" .

On the elliptic-curve side, the 2-converse has its own history, and the companion manuscript states the boundary it sits on. Smith's theorem is a density statement, not a pointwise one: "Smith's theorem gives the $50/50$ distribution of $2^\infty$-Selmer coranks in every fixed quadratic-twist family, counting twist parameters of both signs [S10:56–58]" , and "this density statement does not decide a prescribed member [S10:59]" [S10:58–59]. The pointwise results that preceded this one are compared, not dismissed 

> These results already treat individual curves in their stated ranges; the theorem here includes non-CM curves with rational two-torsion and imposes no reduction condition at $2$. [S10:74–76]

## Consequences

**The complexity is pinned, not just the undecidability.** The corollary fixes the exact degree — $\mathrm{H10}(\mathbb Q)$ has Turing degree $0'$ — and the same corollary recasts the problem in a bounded-degree form, with the caveat attached "No bound is imposed on the number of variables, the number of summands in (ii), or the coefficient heights. [S6:21–22]" The caveats paragraph is the honest boundary of the whole construction , quoted above: no many-one completeness, no single existential definition of ℤ in ℚ.

**The chain inside the release.** Family 004 sits downstream of two other families, and the citations are in the manuscript's own bibliography. The undecidability manuscript cites family 006's Goldfeld-form 2-converse as `UnrestrictedTwoConverse` — "Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves [S7:26]" — and family 010's Fontaine–Mazur theorem as `OddRegularFontaineMazurAtTwo` — "Fontaine–Mazur modularity at the prime 2 [S7:34]" — using both in the parity and height steps , . Its own second manuscript cites the same family-006 paper as `OpenAIGoldfeldTwoConverse2026` [S11:349–355], under the same title [S11:351], and says that companion is not an input to its proof . The pair pages are cross-linked the way 001 and 032 are: [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md) is the upstream link, and [002 — the full Birch–Swinnerton-Dyer formula from low Selmer corank](002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) is the BSD-side neighbour of the same Selmer machinery. A chain is only as strong as its weakest link, and every link in this one is unformalized.

**What the result changes for the transfer problem.** The number-field case is settled by a Diophantine definition of ℤ; this family settles ℚ without one, so the two routes are now visibly different, and the manuscript's own framing of the difference is the finite-test interface [S5:176–180] rather than a definition. The consequence for the Selmer side is narrower and stated by the companion: its construction is finite and its job is simultaneous control at every address — "The finite construction has a different task: it must make the required coefficient tests nonzero at every nonzero address simultaneously [S10:151–152]" , where "The variables are quadratic residue symbols between auxiliary primes [S10:153]" — and the difficulty it overcomes is named "The arithmetic difficulty is uniform integral control at the prime $2$. Residual irreducibility is unavailable here. [S10:141–142]"

**Standing in the ledger.** The triage record lists the family as "no algorithm for rational zeros: Hilbert's tenth over Q has a negative answer [S14:117]" and as "The only T0 family tagged `undecidability` [S14:118]" [S14:117–118]. The counterexample-tag measurement is where its shape gets explained: the phrase rule `negative (?:answer|resolution)` "is what catches **004**, whose result is a negative *resolution* of Hilbert's tenth problem over **Q** with no counterexample object exhibited [S16:53–55]" — inside T0 that wider column flags 22 of 137 families [S16:183–184], and 004 is one of the six the narrow tag moves into the counterexample bucket [S16:145–146].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Release entry for family 004 (100); manuscript blurbs (109, 118) |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | `\resultentry{004}` — title, abstract, manuscript paths (84) |
| S3 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/README.md`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/README.md) | 21 | Provenance: author (3), date (5), citation block (9–17), version note (19–21) naming the superseded directory |
| S4 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/main.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/main.tex) | 81 | Title (58), date (60), abstract (63–67), section inputs (71–77) |
| S5 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/sections/01-introduction.tex) | 250 | Theorem (7–11); history (13–169); proof strategy (171–243) |
| S6 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/sections/07-consequences.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/sections/07-consequences.tex) | 108 | Turing-degree and quartic corollary (8–23) and its proof (25–108) |
| S7 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/references/references.bib`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/build/references/references.bib) | 1078 | Intra-corpus entries: `PointwiseTwoConverse` (16–23), `UnrestrictedTwoConverse` (24–31), `OddRegularFontaineMazurAtTwo` (32–39) |
| S8 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/README.md`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/README.md) | 21 | Provenance: author (3), date (5), citation block (9–17), version note (19–21) naming the superseded directory |
| S9 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/paper.tex`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/paper.tex) | 80 | Title (54), date (56), abstract (59–65), section inputs (69–77) |
| S10 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/introduction.tex`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/introduction.tex) | 173 | Theorem 1.1 (22–29); scope (32–37); companion (39–43); history (45–76); method (78–171) |
| S11 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/references.bib`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/references.bib) | 355 | `OpenAIGoldfeldTwoConverse2026` — family 006 (349–355) |
| S12 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf) | 20041 | Typeset manuscript, 701,017 bytes |
| S13 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf) | 25738 | Typeset manuscript, 893,027 bytes |
| S14 | [`notes/gen/reports/t0-triage.md`](../../../notes/gen/reports/t0-triage.md) | 897 | Bucket entry (117–118); flag-only reading (534) |
| S15 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 373 | Ledger row 5 — tier, counts, claim-shape tags |
| S16 | [`notes/gen/reports/counterexample-tag.md`](../../../notes/gen/reports/counterexample-tag.md) | 203 | Phrase rule (39–44); 004 catch (53–55); 004 verdict (65–67); T0 counts (183–184) |

## Bibliography

- Birch, Bryan J., Swinnerton-Dyer, H. P. F., Notes on elliptic curves. II (1965)
- Bogomolov, F. A., Points of finite order on an Abelian variety (1981)
- Bombieri, Enrico, Gubler, Walter, Heights in Diophantine Geometry (2006)
- Bosch, Siegfried, Lütkebohmert, Werner, Raynaud, Michel, Néron Models (1990)
- Bost, Jean-Beno{\^ı}t, Intrinsic heights of stable varieties and abelian varieties (1996)
- Bost, Jean-Beno{\^ı}t, {Périodes et isogénies des variétés abéliennes sur les corps de nombres (d'apr{\`e}s D. Masser et G. Wüstholz)} (1996)
- Breuil, Christophe, Conrad, Brian, Diamond, Fred, Taylor, Richard, On the modularity of elliptic curves over $\mathbf Q$: wild 3-adic exercises (2001)
- Burungale, Ashay A., Tian, Ye, A rank zero $p$-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin (2026)
- Burungale, Ashay, Skinner, Christopher, A $p$-converse theorem for CM elliptic curves (2024)
- Burungale, Ashay, Castella, Francesc, Skinner, Christopher, Tian, Ye, $p^{\infty}$-Selmer groups and rational points on CM elliptic curves (2022)
- Cai, Li, Shu, Jie, Tian, Ye, Explicit Gross–Zagier and Waldspurger formulae (2014)
- Carayol, Henri, Sur les représentations $l$-adiques associées aux formes modulaires de Hilbert (1986)
- Carayol, Henri, Sur les représentations $\ell$-adiques associées aux formes modulaires de Hilbert (1986)
- Cassels, J. W. S., Arithmetic on curves of genus 1. IV. Proof of the Hauptvermutung (1962)
- Cassels, J. W. S., Arithmetic on curves of genus 1. VIII. On conjectures of Birch and Swinnerton-Dyer (1965)
- Castella, Francesc, Grossi, Giada, Lee, Jaehoon, Skinner, Christopher, On the anticyclotomic Iwasawa theory of rational elliptic curves at Eisenstein primes (2022)
- Chaiken, Seth, A combinatorial proof of the all minors matrix tree theorem (1982)
- Chevalley, Claude, Démonstration d'une hypoth{\`e}se de M. Artin (1935)
- Cornelissen, Gunther, Zahidi, Karim, Elliptic divisibility sequences and undecidable problems about rational points (2007)
- Cornelissen, Gunther, Zahidi, Karim, Topology of Diophantine sets: remarks on Mazur's conjectures (2000)
- Cornelissen, Gunther, Shlapentokh, Alexandra, Defining the integers in large rings of a number field using one universal quantifier (2009)
- Cornut, Christophe, Jetchev, Dimitar, Liftings of reduction maps for quaternion algebras (2013)
- Cox, David A., Primes of the Form $x^2+ny^2$: Fermat, Class Field Theory, and Complex Multiplication (2013)
- Darmon, Henri, Granville, Andrew, On the equations $z^m=F(x,y)$ and $Ax^p+By^q=Cz^r$ (1995)
- Davenport, Harold, Multiplicative Number Theory (2000)
- Davis, Martin, Putnam, Hilary, Robinson, Julia, The decision problem for exponential Diophantine equations (1961)
- Davis, Martin, Hilbert's tenth problem is unsolvable (1973)
- Deligne, Pierre, Travaux de Shimura (1971)
- Deligne, Pierre, Variétés de Shimura: interprétation modulaire, et techniques de construction de mod{\`e}les canoniques (1979)
- Deligne, Pierre, Formes modulaires et représentations $\ell$-adiques (1971)
- Deligne, Pierre, Formes modulaires et représentations $\ell$-adiques (1971)
- Demeyer, Jeroen, Van Geel, Jan, An existential divisibility lemma for global fields (2006)
- Dokchitser, Tim, Dokchitser, Vladimir, On the Birch–Swinnerton-Dyer quotients modulo squares (2010)
- Drinfeld, V. G., Two theorems on modular curves (1973)
- Faltings, Gerd, Endlichkeitssätze für abelsche {Varietäten} über {Zahlkörpern} (1983)
- Faltings, Gerd, Crystalline cohomology and $p$-adic Galois representations (1989)
- Faltings, Gerd, $p$-adic Hodge theory (1988)
- Faltings, Gerd, Endlichkeitssätze für abelsche {Varietäten} über {Zahlkörpern} (1983)
- Ferrero, Bruce, Washington, Lawrence C., The Iwasawa invariant $\mu_p$ vanishes for abelian number fields (1979)
- Fontaine, Jean-Marc, Représentations $p$-adiques semi-stables (1994)
- Friedlander, John, Iwaniec, Henryk, Opera de cribro (2010)
- Garcia-Fritz, Natalia, Pasten, Hector, Vidaux, Xavier, Effectivity for existence of rational points is undecidable (2025)
- Gaudron, Éric, Rémond, Gaël, Polarisations et isogénies (2014)
- Gaudron, Éric, Rémond, Gaël, Théor{\`e}me des périodes et degrés minimaux d'isogénies (2014)
- Alpöge, Levent, Modularity and effective Mordell I (2021)
- Alpöge, Levent, Bhargava, Manjul, Ho, Wei, Shnidman, Ari, Rank stability in quadratic extensions and Hilbert's tenth problem for the ring of integers of a number field (2026)
- Gelbart, Stephen, Jacquet, Hervé, A relation between automorphic representations of $\mathrm{GL}(2)$ and $\mathrm{GL}(3)$ (1978)
- Eisenträger, Kirsten, Miller, Russell, Park, Jennifer, Shlapentokh, Alexandra, As easy as $\mathbb{Q}$: Hilbert's tenth problem for subrings of the rationals and number fields (2017)
- Green, Benjamin, Tao, Terence, Linear equations in primes (2010)
- Green, Ben, Tao, Terence, The {Möbius} function is strongly orthogonal to nilsequences (2012)
- Green, Ben, Tao, Terence, Ziegler, Tamar, An inverse theorem for the Gowers $U^{s+1}[N]$-norm (2012)
- Green, Ben, Tao, Terence, Ziegler, Tamar, Erratum for {An inverse theorem for the Gowers $U^{s+1}[N]$-norm} (2024)
- Gross, Benedict H., Zagier, Don B., Heegner points and derivatives of $L$-series (1986)
- Gross, Benedict H., Heights and the special values of $L$-series (1987)
- Guitart, Xavier, Molina, Santiago, Parametrization of Abelian $K$-surfaces with quaternionic multiplication (2009)
- Heath-Brown, D. R., The size of Selmer groups for the congruent number problem, II (1994)
- Heath-Brown, D. R., A mean value estimate for real character sums (1995)
- Heath-Brown, D. R., A note on the Chevalley–Warning theorems (2011)
- Hilbert, David, Mathematische Probleme. Vortrag, gehalten auf dem internationalen Mathematiker-Kongreß zu Paris 1900 (1900)
- Hoffstein, Jeffrey, Luo, Wenzhi, Nonvanishing of $L$-series and the combinatorial sieve (1997)
- Howard, Benjamin, The Heegner point Kolyvagin system (2004)
- Iwaniec, Henryk, On the order of vanishing of modular $L$-functions at the critical point (1990)
- Javanpeykar, Ariyan, Polynomial bounds for Arakelov invariants of Belyi curves (2014)
- Jetchev, Dimitar, Kane, Ben, Equidistribution of Heegner points and ternary quadratic forms (2011)
- Kato, Kazuya, $p$-adic Hodge theory and values of zeta functions of modular forms (2004)
- Keller, Timo, Yin, Mulun, $p$-converse theorems for elliptic curves of potentially good ordinary reduction at Eisenstein primes (2024)
- Kim, Chan-Ho, On the soft $p$-converse to a theorem of Gross–Zagier and Kolyvagin (2023)
- Koenigsmann, Jochen, Defining $\mathbb{Z}$ in $\mathbb{Q}$ (2016)
- Kolyvagin, Viktor A., Euler systems (1990)
- Koymans, Peter, Pagano, Carlo, Hilbert's tenth problem via additive combinatorics (2026)
- Kriz, Daniel, Supersingular main conjectures, Sylvester's conjecture and Goldfeld's conjecture (2022)
- Long, D. D., Maclachlan, C., Reid, A. W., Arithmetic Fuchsian groups of genus zero (2006)
- Manin, Yu. I., Parabolic points and zeta-functions of modular curves (1972)
- Marker, David, Model Theory: An Introduction (2002)
- Matiyasevich, Yu. V., Diofantovost' perechislimykh mnozhestv (1970)
- Mazur, Barry, Speculations about the topology of rational points: an up-date (1995)
- Mazur, Barry, Rubin, Karl, Ranks of twists of elliptic curves and Hilbert's tenth problem (2010)
- Milne, James S., Arithmetic Duality Theorems (2006)
- Milne, James S., Abelian Varieties (2008)
- Milne, James S., Class Field Theory (2020)
- Milne, James S., {Lectures on Étale Cohomology} (2013)
- Milne, J. S., Arithmetic Duality Theorems (2006)
- Mokrani, Youcef, Adaptation of Monsky matrices for $\theta$-congruent numbers (2020)
- Monsky, Paul, Generalizing the Birch–Stephens theorem. I. Modular curves (1996)
- Montgomery, Hugh L., Vaughan, Robert C., Multiplicative Number Theory I: Classical Theory (2007)
- Mumford, David, Abelian Varieties (1970)
- Murty, M. Ram, Pasten, Hector, Modular forms and effective Diophantine approximation (2013)
- von Känel, Rafael, The effective Shafarevich conjecture for abelian varieties of $\mathrm{GL}_2$-type (2021)
- von Känel, Rafael, Modularity and integral points on moduli schemes (2013)
- von Känel, Rafael, Kret, Arno, Integral points on coarse Hilbert moduli schemes (2023)
- Neukirch, Jürgen, Algebraic Number Theory (1999)
- OpenAI, {A pointwise $2$-converse for elliptic curves with rational two-torsion} (2026)
- OpenAI, {Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves} (2026)
- OpenAI, Fontaine–Mazur modularity at the prime 2 (2026)
- OpenAI, {Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves} (2026)
- Pazuki, Fabien, Theta height and Faltings height (2012)
- Poonen, Bjorn, Stoll, Michael, The Cassels–Tate pairing on polarized abelian varieties (1999)
- Poonen, Bjorn, Characterizing integers among rational numbers with a universal-existential formula (2009)
- Poonen, Bjorn, Hilbert's tenth problem and Mazur's conjecture for large subrings of $\mathbb{Q}$ (2003)
- Poonen, Bjorn, Undecidability in number theory (2008)
- Poonen, Bjorn, Using elliptic curves of rank one towards the undecidability of Hilbert's tenth problem over rings of algebraic integers (2002)
- Pyle, Elisabeth Eve, Abelian Varieties over $\mathbf{Q}$ with Large Endomorphism Algebras and Their Simple Components over $\overline{\mathbf{Q}}$ (1995)
- Quer, Jordi, $\mathbf{Q}$-curves and abelian varieties of $\mathrm{GL}_2$-type (2000)
- Quer, Jordi, Fields of definition of $\mathbf{Q}$-curves (2001)
- Radziwiłł, Maksym, Soundararajan, K., Moments and distribution of central $L$-values of quadratic twists of elliptic curves (2015)
- Ramsey, Nick, Geometric and $p$-adic modular forms of half-integral weight (2006)
- Ribet, Kenneth A., Abelian varieties over $\mathbf{Q}$ and modular forms (1992)
- Ribet, Kenneth A., Galois representations attached to eigenforms with nebentypus (1977)
- Nualart Riera, Joan, On the Hyperbolic Uniformization of Shimura Curves with an Atkin–Lehner Quotient of Genus 0 (2015)
- Robinson, Julia, Definability and decision problems in arithmetic (1949)
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties (2013)
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties—corrigendum (2016)
- Selberg, Atle, On an elementary method in the theory of primes (1947)
- Serre, Jean-Pierre, Tate, John, Good reduction of abelian varieties (1968)
- Serre, Jean-Pierre, Local Fields (1979)
- Serre, Jean-Pierre, Galois Cohomology (1997)
- Serre, Jean-Pierre, Abelian $\ell$-adic Representations and Elliptic Curves (1968)
- Serre, Jean-Pierre, Propriétés galoisiennes des points d'ordre fini des courbes elliptiques (1972)
- Shimura, Goro, On modular forms of half integral weight (1973)
- Siegel, Carl Ludwig, {Über die Classenzahl quadratischer Zahlkörper} (1935)
- Silverberg, Alice, Zarhin, Yuri G., Semistable reduction and torsion subgroups of abelian varieties (1995)
- Silverman, Joseph H., The Arithmetic of Elliptic Curves (2009)
- Skinner, Christopher, A converse to a theorem of Gross, Zagier, and Kolyvagin (2020)
- Smith, Alexander, The Birch and Swinnerton-Dyer conjecture implies Goldfeld's conjecture (2025)
- Tate, John, On the conjectures of Birch and Swinnerton-Dyer and a geometric analog (1966)
- Voight, John, Quaternion Algebras (2021)
- Waldspurger, Jean-Loup, Sur les coefficients de Fourier des formes modulaires de poids demi-entier (1981)
- Waldspurger, Jean-Loup, Correspondances de Shimura (1984)
- Warning, Ewald, Bemerkung zur vorstehenden Arbeit von Herrn Chevalley (1935)
- Wei, Tao, Guo, Xuejun, The rank of $2$-Selmer group associate to $\theta$-congruent numbers (2022)
- Weil, André, Sur certains groupes d'opérateurs unitaires (1964)
- Williams, Kenneth S., Mertens' theorem for arithmetic progressions (1974)
- Wu, Chenyan, Virtual Abelian varieties of $\mathrm{GL}_2$-type (2020)
- Zarhin, Yu. G., A remark on endomorphisms of abelian varieties over function fields of finite characteristic (1974)
- Zarhin, Yuri G., Abelian varieties, quaternion trick and endomorphisms (2023)
- Zhang, Wei, Selmer groups and the indivisibility of Heegner points (2014)
- Nekovář, Jan, Selmer complexes (2006)
