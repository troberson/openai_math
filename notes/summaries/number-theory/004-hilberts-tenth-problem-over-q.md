# 004 — Hilbert's tenth problem over ℚ (Number theory, 2 manuscripts, tier T0)

## Original CONTENTS.md summary

The release entry for the family reads [S1:100]:

> **004. Hilbert's tenth problem over ℚ.** Proves that no algorithm decides whether an integer-coefficient polynomial in an arbitrary number of variables has a rational zero, resolving Hilbert's tenth problem over ℚ negatively.

The family ships two manuscripts, and the release describes them as two different kinds of theorem. The first [S1:109]:

> We give a negative answer to Hilbert's tenth problem over the rational numbers: no algorithm decides whether a polynomial with integer coefficients has a rational zero. The number of variables is part of the input.

The second [S1:118]:

> We prove a pointwise 2-converse for elliptic curves over $`\mathbf Q`$ with nonzero rational two-torsion: if the $`2^\infty`$-Selmer corank is zero or one, then the analytic rank and Mordell–Weil rank equal that corank, and the Shafarevich–Tate group is finite. The result allows arbitrary reduction at 2.

The pairing is not two versions of one claim. The undecidability manuscript is the headline; the elliptic-curve manuscript is an arithmetic input that headline's proof consumes. The roadmap says so — "its passage from two-descent data to rational points uses the pointwise $2$-converse" [S5:232–234] — and the undecidability manuscript carries that result in its own bibliography, under the key `PointwiseTwoConverse` [S7:16–23].

## Undergraduate summary

Hilbert's tenth problem asks for an algorithm that, given a polynomial with integer coefficients, decides whether it has an integer solution. That question was closed in 1970: no such algorithm exists. Family 004 answers the rational version — same input, same question, with a solution in ℚ replacing a solution in ℤ. The manuscript states its result as [S5:8–10]:

> There is no algorithm which, given a polynomial $f\in\Z[X_1,\ldots,X_n]$, with $n$ part of the input, decides whether $f$ has a zero in $\Q^n$.

The clause "with $n$ part of the input" [S5:8–10] is load-bearing. If the number of variables were fixed in advance, the question would be a different one; the theorem is about the full problem, where the polynomial arrives with any number of variables attached.

The proof is a reduction, not a machine that fails. It shows that the integer problem — already known to be undecidable — can be answered by asking the rational problem a bounded number of times. The mechanism is a parallel search [S5:181]:

> An integer zero supplies witnesses for all the tests. If a rational-solvability algorithm existed, we could run two searches in parallel: enumeration of integer zeros, and enumeration of tests until one fails. The arithmetic work is to prove that a failed test exists whenever \(f\) has no integer zero.

So the entire burden is one implication: if a polynomial has no integer zero, then at least one of a finite list of effectively computable tests fails. The reduction produces that list as the equivalence at [S5:176–180], and everything else in the paper exists to force a failure.

The tests are comparisons of size. Each candidate solution is attached to a point on an elliptic curve, and the proof needs an upper bound on the height of the ring element representing that point — "let \(M(s)\) be the product, without repetition, of the nonexceptional primes at which one of these forms has odd valuation" [S5:192], with the estimate "h(s)\le H M(s)^c" [S5:194] displayed just below it — and a lower bound coming from the canonical height of the attached point. The two bounds collide unless the modelled root coordinates are an ordinary finite interval of integers, which is the elementarity the reduction needs [S5:213]:

> If \(\delta=0\), elementarity gives an ordinary integer zero of \(f\).

The arithmetic that makes the height bound uniform is a 2-converse statement about Selmer groups, and that is why the family's second manuscript sits in this family rather than beside it.

**The shape of the proof, in six moves.** (1) Encode the integers inside a ring whose elements are built from ℚ, and attach to each candidate root a point on an elliptic curve. (2) Produce the finite test family: "we construct an effectively generated sequence of finite tests" [S5:173–174], each a finite computation in a residue ring, a height box, and local solvability conditions. (3) Prove the pole-parity condition, which is where two-descent data becomes rational points [S5:232–234]. (4) Prove the five-point height estimate, whose modularity step is a Fontaine–Mazur theorem at 2 [S5:236–237]. (5) Force the contradiction \(B^2\ll_f B\) [S5:224–225]. (6) Read off undecidability, and record the exact complexity [S6:9–12].

## Graduate summary

**The headline theorem.** [S5:8–10] — no algorithm decides, for a polynomial in $\Z[X_1,\ldots,X_n]$ with $n$ part of the input, whether it has a zero in $\Q^n$. The abstract of the manuscript states the same claim in prose [S4:64–66]:

> We give a negative answer to Hilbert's tenth problem over the rational numbers: no algorithm decides whether a polynomial with integer coefficients has a rational zero. The number of variables is part of the input.

**The moves, as the paper organises them.**

1. **The finite-test interface.** The reduction is stated as an interface, not as a definition of ℤ inside ℚ: "For each nonconstant integral polynomial \(f\), we construct an effectively generated sequence of finite tests" [S5:173–174], and the interface is the equivalence "f\text{ has an integer zero}" ⟺ "every test succeeds" [S5:176–180], each test answerable by finitely many rational-solvability queries.
2. **The parity step.** Section 3 of the manuscript proves the pole-parity condition, and its passage from two-descent data to rational points is the pointwise 2-converse [S5:232–234], paired with the Cassels–Tate pairing. This is the family's internal dependency: the headline proof consumes the family's second manuscript.
3. **The height step.** Section 4 proves the five-point height estimate, and "Its modularity step uses the odd regular Fontaine--Mazur theorem at $2$" [S5:236–237], "whose statement has no hypothesis on the residual image" [S5:238–239]. Both inputs are inside the release: the 2-converse is this family's own second manuscript [S7:16–23], the Goldfeld-form 2-converse is family 006 [S7:24–31], and the Fontaine–Mazur theorem at 2 is family 010 [S7:32–39].
4. **The quantitative core.** Two parameters carry the contradiction: \(\delta=f(\eta(a_1),\ldots,\eta(a_n))\) and \(B=\max(1,|\eta(a_1)|,\ldots,|\eta(a_n)|)\) are set at [S5:208–212], and the paper states what \(\delta\) is worth — "Otherwise \(\delta\) is a nonzero ambient integer whose size is bounded by a fixed polynomial in \(B\)" [S5:213] — and what the collision is — "the two bounds give \(B^2\ll_f B\)" [S5:225]. The left side is the canonical height of the attached point, growing quadratically in $|\eta(a_j)|$; the right side is the reduction's uniform height bound.
5. **The closure.** The root-coordinate contradiction [S5:220–229]:

> For each nonzero root coordinate \(a_j\), consider its attached point \(T_{a_j}\). Applying the uniform bound to the ring elements representing \(x(T_{a_j})\) gives \(h(x(\eta(a_j)P))\ll_f B\). The transferred canonical-height comparison for \(P\) makes this height grow quadratically in \(|\eta(a_j)|\). If \(B>1\), choose \(j\) with \(|\eta(a_j)|=B\); the two bounds give \(B^2\ll_f B\). If \(B=1\), the required bound is immediate. Thus all root indices lie in an ordinary finite interval. Additivity and injectivity identify the modeled root coordinates with those ordinary integers, contradicting \(\delta\ne0\). This proves the finite-test equivalence and hence the undecidability theorem.

6. **The exact complexity.** The consequences section fixes the Turing degree [S6:9–12]:

> With the usual effective coding, let \(\mathrm{H10}(\Q)\) be the set of integral polynomials having a rational zero, with the number of variables part of the input. Then \(\mathrm{H10}(\Q)\) has Turing degree \(0'\), the degree of the halting problem.

The proof of that corollary runs in both directions: $\mathrm{H10}(\Z)\le_T\mathrm{H10}(\Q)$ from the reduction, and the converse from enumerability — "Rational solvability is also computably enumerable" [S6:49] — and it ends by normalising the presentation to degree four, "The expanded polynomial has integral coefficients and total degree at most four" [S6:95–96].

**The companion theorem.** The second manuscript's headline is a pointwise 2-converse [S10:23–29]:

> Let $E/\Q$ be an elliptic curve with $E(\Q)[2]\ne0$ and $s_2(E)\in\{0,1\}$. Then \[ \ord_{s=1}L(E,s)=\rank_{\Z}E(\Q)=s_2(E), \qquad \Sha(E/\Q)\text{ is finite}. \]

Its abstract states the same claim in prose [S9:60–64]:

> We prove a pointwise $2$-converse for elliptic curves over $\mathbf Q$ with nonzero rational two-torsion: if the $2^\infty$-Selmer corank is zero or one, then the analytic rank and Mordell--Weil rank equal that corank, and the Shafarevich--Tate group is finite. The result allows arbitrary reduction at $2$.

Its scope is stated as a range, not as a hypothesis on the curve [S10:32–37]:

> The statement includes one rational two-torsion line and full rational two-torsion, CM and non-CM curves, every rational isogeny configuration, and every reduction type at $2$ and at the bad primes.

and its relation to the family's other 2-converse is explicit [S10:39–43]:

> The broader companion \cite[Theorem~1.1]{OpenAIGoldfeldTwoConverse2026} proves the $2$-converse without the rational-two-torsion hypothesis. Here we give a separate full treatment of the rational-two-torsion case, developing its integral interpolation and finite twist constructions within this paper; the broader converse is not an input to the proof.

So the dependency inside family 004 runs one way: the undecidability manuscript uses the pointwise converse; the pointwise converse does not use the broader converse of family 006, even though it cites it [S11:349–355].

**What the pair does not say.** The undecidability result is a negative answer, not an exhibited object, and the release's own reading record says so: "004 is a negative *resolution* of Hilbert's tenth problem over **Q**, not an exhibited object" [S14:529–531]. The corollary section is equally explicit about its own limits [S6:100–107]:

> The many-one reduction to the restricted problems starts from \(\mathrm{H10}(\Q)\); the reduction from \(\mathrm{H10}(\Z)\) remains a Turing reduction. This argument does not establish many-one completeness of \(\mathrm{H10}(\Q)\). The list in (ii) is supplied as part of the input, so no recognition of sum-of-squares presentations is needed. The construction supplies no bound on the number of variables or coefficient heights, and it gives no single existential definition of \(\Z\) in \(\Q\).

That last clause is the one to hold onto: this proof does not produce an existential definition of ℤ in ℚ, which is the route the number-field results take [S5:129–134], and the manuscript says plainly that ℚ is outside the class of rings those results cover — "The field \(\mathbb Q\) is not a finitely generated \(\mathbb Z\)-algebra" [S5:141–143]. On the elliptic-curve side, the companion theorem bounds its own claim [S10:34–37]: "It is a $2$-converse in this residual range. It does not assert the full Birch--Swinnerton-Dyer leading-coefficient formula, nor does a bound $\rank E(\Q)\le1$ alone imply its Selmer hypothesis."

**Formalization status.** The ledger row for 004 records 2 manuscripts, 0 formalized, no scope note, no comparator challenge, no `main_results` config, no verification directory, no reasoning trace, tier T0 [S15:5]. Nothing about this family is machine-checked. It is the only T0 family carrying the `undecidability` claim-shape tag [S14:113–114], and it is one of the six T0 families that the narrow counterexample tag misses and the wider phrase rule catches [S16:145–146]. The rule matches the release's own wording — "resolving Hilbert's tenth problem over $\mathbb Q$ negatively" [S2:84] — and the reading verdict recorded for the family is "a negative resolution, not an exhibited object" [S16:65–67].

## History of the conjecture

Prior (my training data, not this repo.) Hilbert's tenth problem dates to 1900. The chain that settled the integer case runs Davis–Putnam–Robinson–Matiyasevich, with Matiyasevich's 1970 theorem on recursively enumerable sets supplying the last step; after that, the rational case became the standard open transfer problem. Julia Robinson's own work on the rationals predates the integer resolution. Poonen's 2009 conditional result — ℤ Diophantine in ℚ assuming squarefree rank for a specific elliptic curve — is the form the question took in the twenty-first century, and the Mazur–Rubin conjecture on ranks in quadratic-twist families became the standard hypothesis under which the transfer goes through.

The manuscript's own history section is the check on that. It opens with the integer case: "Davis, Putnam, and Robinson proved in 1961 that every recursively enumerable relation has such a representation if exponentiation is also allowed" [S5:27–29], and "Matiyasevich supplied the required growth in 1970 through a Diophantine description of a Fibonacci relation" [S5:32–33], which completes "the theorem that every recursively enumerable relation on the positive integers is Diophantine" [S5:33–35] — "The equivalent all-integer decision problem is therefore undecidable" [S5:35–36]. Definability inside ℚ was settled long before that, and the manuscript is explicit that it is not the transfer: "Julia Robinson showed in 1949 that the integers are first-order definable in the rationals using addition and multiplication" [S5:59–60], Poonen's positive formula used "two universal quantifiers followed by seven existential quantifiers" [S5:65–66], and Koenigsmann "gave a universal definition of \(\mathbb Z\); equivalently, its complement in \(\mathbb Q\) is Diophantine" [S5:67–69]. The geometric obstruction is recorded too — Mazur's conjecture on the closure of rational points "would rule out a Diophantine definition of \(\mathbb Z\) in \(\mathbb Q\)" [S5:80–82], and the manuscript notes that "These obstructions to definitions and models do not by themselves rule out a negative answer to the rational decision problem" [S5:85–87]. The subring line reaches proper subrings of ℚ: Poonen built them from "selected multiples of a point on a rank-one elliptic curve whose real coordinates approximate integers" [S5:98–100], and Eisenträger–Miller–Park–Shlapentokh produced rings whose "Hilbert's tenth problem is Turing equivalent to that over \(\mathbb Q\)" [S5:104–105], with the caveat that "The density of the inverted primes alone therefore does not settle the relation to the field problem" [S5:109–111].

The number-field route is the one that closed first. Mazur and Rubin proposed the rank bound for quadratic twists and, "Assuming this for every elliptic curve over every number field, they obtained undecidability for every infinite finitely generated \(\mathbb Z\)-algebra" [S5:125–127]. That conditional was removed after this release's own manuscripts: "Koymans and Pagano combined two-descent with additive combinatorics to prove that \(\mathbb Z\) is Diophantine in the ring of integers of every number field" [S5:129–132], and Alpöge–Bhargava–Ho–Shnidman settled the corresponding density statement [S5:135–140]. The manuscript is precise about why none of that touches ℚ [S5:141–143]:

> The field \(\mathbb Q\) is not a finitely generated \(\mathbb Z\)-algebra, so these results concern a different class of rings from the field in Theorem

The prior work on definability inside ℚ is summarised as control, not as a solution: "These results give substantial control of definitions inside \(\mathbb Q\), but do not supply the existential membership condition for the direct transfer above" [S5:71–74].

On the elliptic-curve side, the 2-converse has its own history, and the companion manuscript states the boundary it sits on. Smith's theorem is a density statement, not a pointwise one: "Smith's theorem gives the $50/50$ distribution of $2^\infty$-Selmer coranks in every fixed quadratic-twist family, counting twist parameters of both signs" [S10:56–58], and "this density statement does not decide a prescribed member" [S10:58–59]. The pointwise results that preceded this one are compared, not dismissed [S10:74–76]:

> These results already treat individual curves in their stated ranges; the theorem here includes non-CM curves with rational two-torsion and imposes no reduction condition at $2$.

## Consequences now that the proof has been found

**The complexity is pinned, not just the undecidability.** The corollary fixes the exact degree [S6:9–12] — $\mathrm{H10}(\Q)$ has Turing degree $0'$ — and the same corollary recasts the problem in a bounded-degree form, with the caveat attached [S6:21–22]: "No bound is imposed on the number of variables, the number of summands in (ii), or the coefficient heights." The caveats paragraph is the honest boundary of the whole construction [S6:100–107], quoted above: no many-one completeness, no single existential definition of ℤ in ℚ.

**The chain inside the release.** Family 004 sits downstream of two other families, and the citations are in the manuscript's own bibliography. The undecidability manuscript cites family 006's Goldfeld-form 2-converse as `UnrestrictedTwoConverse` — "Goldfeld's analytic density conjecture and the $2$-converse for elliptic curves" [S7:26] — and family 010's Fontaine–Mazur theorem as `OddRegularFontaineMazurAtTwo` — "Fontaine--Mazur modularity at the prime 2" [S7:34] — using both in the parity and height steps [S5:232–234], [S5:236–237]. Its own second manuscript cites the same family-006 paper as `OpenAIGoldfeldTwoConverse2026` [S11:349–355], under the same title [S11:351], and says that companion is not an input to its proof [S10:39–43]. The pair pages are cross-linked the way 001 and 032 are: [006 — Goldfeld's conjecture](006-goldfelds-conjecture.md) is the upstream link, and [002 — the full Birch–Swinnerton-Dyer formula from low Selmer corank](002-full-birch-swinnerton-dyer-formula-from-low-selmer-corank.md) is the BSD-side neighbour of the same Selmer machinery. A chain is only as strong as its weakest link, and every link in this one is unformalized.

**What the result changes for the transfer problem.** The number-field case is settled by a Diophantine definition of ℤ; this family settles ℚ without one, so the two routes are now visibly different, and the manuscript's own framing of the difference is the finite-test interface [S5:176–180] rather than a definition. The consequence for the Selmer side is narrower and stated by the companion: its construction is finite and its job is simultaneous control at every address — "The finite construction has a different task: it must make the required coefficient tests nonzero at every nonzero address simultaneously" [S10:151–152], where "The variables are quadratic residue symbols between auxiliary primes" [S10:153] — and the difficulty it overcomes is named [S10:141–142]: "The arithmetic difficulty is uniform integral control at the prime $2$. Residual irreducibility is unavailable here."

**Standing in the ledger.** The triage record lists the family as "no algorithm for rational zeros: Hilbert's tenth over Q has a negative answer" and as "The only T0 family tagged `undecidability`" [S14:113–114]. The counterexample-tag measurement is where its shape gets explained: the phrase rule `negative (?:answer|resolution)` "is what catches **004**, whose result is a negative *resolution* of Hilbert's tenth problem over **Q** with no counterexample object exhibited" [S16:53–55] — inside T0 that wider column flags 22 of 137 families [S16:183–184], and 004 is one of the six the narrow tag moves into the counterexample bucket [S16:145–146].

## Sources

| # | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release entry for family 004 (100); manuscript blurbs (109, 118) |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | `\resultentry{004}` — title, abstract, manuscript paths (84) |
| S3 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/README.md`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/README.md) | 18 | Provenance: author (3), date (5), citation block (9–16) |
| S4 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/main.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/main.tex) | 81 | Title (58), date (60), abstract (63–67), section inputs (71–77) |
| S5 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/sections/01-introduction.tex) | 250 | Theorem (7–11); history (13–169); proof strategy (171–243) |
| S6 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/sections/07-consequences.tex`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/sections/07-consequences.tex) | 108 | Turing-degree and quartic corollary (8–23) and its proof (25–108) |
| S7 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/references/references.bib`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/build/references/references.bib) | 1,078 | Intra-corpus entries: `PointwiseTwoConverse` (16–23), `UnrestrictedTwoConverse` (24–31), `OddRegularFontaineMazurAtTwo` (32–39) |
| S8 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/README.md`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/README.md) | 18 | Provenance: author (3), date (5), citation block (9–16) |
| S9 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/paper.tex`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/paper.tex) | 80 | Title (54), date (56), abstract (59–65), section inputs (69–77) |
| S10 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/sections/introduction.tex`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/sections/introduction.tex) | 173 | Theorem 1.1 (22–29); scope (32–37); companion (39–43); history (45–76); method (78–171) |
| S11 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/references.bib`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/references.bib) | 355 | `OpenAIGoldfeldTwoConverse2026` — family 006 (349–355) |
| S12 | [`preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf) | — | Typeset manuscript, 701,416 bytes |
| S13 | [`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf) | — | Typeset manuscript, 893,281 bytes |
| S14 | [`notes/t0-triage.md`](../../t0-triage.md) | 897 | Bucket entry (113–114); flag-only reading (529–531) |
| S15 | [`notes/catalog.tsv`](../../catalog.tsv) | 373 | Ledger row 5 — tier, counts, claim-shape tags |
| S16 | [`notes/counterexample-tag.md`](../../counterexample-tag.md) | 201 | Phrase rule (39–44); 004 catch (53–55); 004 verdict (65–67); T0 counts (183–184) |

Both manuscripts ship their LaTeX source under a `build/` tree and their PDF at the directory root; the provenance blocks [S3:9–16], [S8:9–16] give the citation keys, and the typeset PDFs are [S12] and [S13]. The release's own entry for the family is [S2:84], which names both manuscript paths.

Checked with `python3 notes/scripts/verify_summaries.py --mutant`, which resolves every `[S#:line]` marker against the shipped file, matches every quotation against the lines it cites, and injects four mutants (an altered inline quotation, a quotation wrapped across source lines, a block quote attributed to the wrong source, and a fabricated quotation) to prove the checks bite.

Absent by construction (T0): `lean/docs/004.md`, any `lean/OAI/**` file, any `lean/ComparatorChallenges/` entry, any `main_results` config, any verification directory, any reasoning trace.
