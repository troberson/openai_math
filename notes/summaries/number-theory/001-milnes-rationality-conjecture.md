# 001 — Milne's rationality conjecture (Number theory, 1 manuscript, tier T0)

## Original CONTENTS.md summary

[S1:16] (family entry):

> **001. Milne’s rationality conjecture and algebraic specialization.** Proves Milne's rationality
> conjecture for abelian varieties over $`\overline{\mathbb Q}`$ with good reduction: specialized
> Hodge classes pair rationally with complementary divisor products, independently of cohomology
> theory. Together with result 032, every specialized Hodge class is represented by a single rational
> algebraic cycle simultaneously in all prime-to-*p* and crystalline realizations, for every
> residue characteristic *p*.

[S1:23] (the manuscript entry under that family):

> [Milne's rationality conjecture for abelian varieties](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf)

[S1:25] (its abstract):

> We prove Milne's rationality conjecture for abelian varieties, including residue characteristic 2.
> After good reduction, the pairing of a rational Hodge class with any complementary product of
> divisor classes on the reduction is the same rational number in every prime-to-*p* realization
> and in crystalline cohomology. Using the Hodge theorem for CM abelian varieties, we also show that
> every such specialized Hodge class is represented by a single rational algebraic cycle in all these
> realizations.

The manuscript's own abstract ([S3:58–64]) is identical to [S1:25], and
[S2:78] carries the [S1:16] text, so both blurbs are the release's words, not the
manuscript's framing.

## Undergraduate summary

An **abelian variety** is a projective algebraic group — the simplest example is an elliptic curve,
and higher-dimensional examples behave like higher-dimensional tori with algebraic structure. Every
such variety over the complex numbers has a cohomology theory built from differential forms, and
inside it sits a distinguished family of classes called **Hodge classes**. The Hodge conjecture says
these classes all come from algebraic subvarieties. For abelian varieties this is wide open, and it
is one of the standard forms of the conjecture.

This paper is not about the Hodge conjecture directly. It is about a subtler question. An abelian
variety over a number field can be reduced modulo a prime `p`, producing an abelian variety in
characteristic `p`. A cohomology class on the original variety then has a **specialization** on the
reduced variety. There are several cohomology theories available in characteristic `p` — étale
cohomology with ℓ-adic coefficients for each prime ℓ, and crystalline cohomology for the prime `p`
itself. They are comparison-isomorphic, so a class computed in each theory gives the same answer.
The question Milne asked is whether the numbers you get by intersecting a specialized Hodge class
against complementary classes are **rational numbers**, and the same rational number in every one of
those theories at once. "Rational" here is a strong demand: each realization naturally produces
coefficients in a different coefficient field, and asking for one common rational value is asking
for a compatibility that the formalism does not give you for free.

The paper proves this for every abelian variety with good reduction at the chosen prime, and for
every rational Hodge class on that variety — the class comes from the original variety, not an
arbitrary class on the reduced variety. Good reduction is a genuine hypothesis, not a convenience:
the reduced variety can carry divisors that the original variety did not have, which is exactly why
the specialization can be a new class. What the proof produces is a rational number, not an
algebraic cycle.

The shape of the proof, sketched at [S4:186–265]:

1. **Move the problem.** Along a map between reduced varieties, the class in question turns out to
   be the pullback of a Hodge class on a **CM** abelian variety — one with as many symmetries as
   geometry allows.
2. **Use the symmetries.** Those symmetries shrink the question to a small, highly structured kind
   of class, in which the numbers being computed are pinned down by the symmetry group.
3. **A fork.** Either every intersection number in question is zero — rational, so there is nothing
   to prove — or the class is itself built out of divisor classes, in all the cohomology theories at
   once.
4. **Force one rational number.** The second branch is handled by building an auxiliary variety
   whose structure forces a single rational identity, then pulling that identity back.

The two varieties built in steps 1 and 4 are different varieties doing different jobs. The caption
says so: "The CM and prescribed-filtration auxiliaries need not coincide" ([S4:277–278]),
and the figure source [S11] draws them as two panels labelled
"CM transport" ([S11:8]) and "Prescribed-filtration transport" ([S11:17]).

## Graduate summary

**Theorem 1** ([S4:29–56], `thm:main`). Fix `Q̄ ⊂ C`, a prime `p`, and a
`p`-adic place `w` of `Q̄`; write `F = F̄_p`, `K₀ = Frac W(F)`, `C_w = Q̄_w^`. Let `A/Q̄` have dimension
`d` and good reduction `A₀/F` at `w`, let `0 ≤ r ≤ d`, and let `γ ∈ H^{2r}(A(C), Q(r))` be a rational
Hodge class. Then for every list of Cartier divisors `D₁, …, D_{d-r}` on `A₀` there is one `q ∈ Q`
with `Tr_ℓ(γ_{0,ℓ} c_{1,ℓ}(D₁)⋯c_{1,ℓ}(D_{d-r})) = q` in `Q_ℓ` for every `ℓ ≠ p`, and
`Tr_p(γ_{0,p} c_{1,cris}(D₁)⋯c_{1,cris}(D_{d-r})) = q` in `C_w`, where `γ_{0,ℓ}` is smooth proper
specialization and `γ_{0,p}` is the de Rham–crystalline specialization. The introduction states the
scope in one line: "We prove it for every residue characteristic" ([S4:8–9]). By linearity
the same holds against every rational Lefschetz class of complementary codimension
([S4:58–60]).

The argument has four moves, sketched at [S4:186–265]:

1. **Transport.** The transport proposition ([S6:35], `prop:transport`) produces an
   integer `n`, an auxiliary abelian variety `B` of good reduction at `w`, a quasi-isogeny
   `a : A₀ⁿ → B₀`, and a rational Hodge class `κ` on `B` with `(a j)^* κ₀ = γ₀`, simultaneously in
   every realization under consideration. Item 1 of that proposition arranges `B` to be of CM type
   and defined over `Q̄` ([S6:62]). The CM case is reached through `cor:cm-transport`
   ([S6:777]) and the special-point theorem of Kisin–Zhou (`[Theorem 2.2.7]` of
   `KisinZhou2025`), with normalization by a ratio of rational divisor intersections.
2. **CM structure.** CM reduction ([S9:18], `lem:cm-reduction`) expresses the reduced
   variety in terms of a CM field `E` acting up to isogeny, with `dim_E H₁ = 2s` and Hodge
   multiplicities `(s, s)` at every embedding of `E`. The balanced Weil space `W_E^s(A)`
   ([S8:18], `def:weil-space`) is then a rational subspace of `H^{2s}` whose elements are
   automatically Hodge classes of type `(s, s)`.
3. **The filtration.** The key input is the dichotomy in `prop:weil` ([S8:55]): for the
   Rosati-symmetric, `E`-commuting endomorphisms `𝒰` of `A₀` ([S8:49–53]), either `𝒰`
   has no invertible element and every complementary pairing of `γ₀` vanishes, or `𝒰` has an
   invertible element and `γ₀` is a simultaneous rational Lefschetz class. The vanishing branch is
   `lem:weil-orthogonality` ([S8:70]); the divisor branch uses the filtration construction
   ([S7:38], `thm:filtration`), which builds a weakly admissible, `E`- and
   `u`-stable Lagrangian filtration of dimension `s` at each embedding, using Fontaine–Rapoport
   transversality, bounded-degree avoidance ([S7:87]), intersections with Lagrangians
   ([S7:130]), and a maximality argument.
4. **Lift and extract.** The invertible `u` gives a divisor `D^u` nondegenerate on each `E`-eigenspace
   separately. `lem:weil-divisor-span` ([S8:205]) shows that such a divisor generates the
   determinant classes as rational linear combinations of products of divisor classes; the lift lemma
   ([S5:158], `lem:lift-hom`) carries the projector, a finite `Q`-basis of the
   `E`-action, and the symmetric homomorphism of the divisor from `B₀` to `B`, where injectivity of
   specialization preserves `R² = R`, the multiplication table, and `R^*D = D` ([S8:392–404]).
   The resulting rational identity specializes with the same rational coefficients in every component.

Two auxiliary varieties are used for different jobs, and the distinction is load-bearing: the first is
CM, the second realizes a prescribed admissible filtration over a local field and need not be CM
([S4:157–160]). The realization machinery is named as Grothendieck–Serre–Tate deformation
theory, Tate's extension theorem, and the integral-model and local-Shimura results of Kisin–Zhou and
Pappas–Rapoport ([S4:160–164]). Supporting results: the auxiliary Hodge datum
([S6:116], `lem:auxiliary-datum`), realization of an admissible filtration
([S6:330], `lem:admissible-realization`), the divisor filtration condition
([S7:450]), and the group `G` of `E`-linear polarization similitudes with
`det_E(a) = c(a)^s` ([S8:280], `lem:weil-group`), which makes the transport target a Shimura
datum of Hodge type.

**What the theorem does not say.** [S9:361–362]: "This cohomological membership statement
alone gives no algebraic cycle and proves neither the Hodge nor the Tate conjecture." [S9:443–448]:
the conclusion concerns only the special fiber at the fixed place; it does not assert the Hodge
conjecture for abelian varieties in characteristic zero, does not lift the representing cycle to the
generic fiber, does not assert uniqueness modulo rational equivalence, and makes no comparison
between different reduction places.

**Formalization status.** None. No `lean/OAI/` file, no `lean/docs/001.md`, no comparator challenge,
no `main_results` entry — the ledger row `fam=001` records tier T0 with zero challenges, zero main
results, zero formalized manuscripts, and no reasoning trace [S14]. The manuscript ships its LaTeX
under `build/`, a typeset PDF at its root [S15], and the README named below [S12]; the release ships
nothing for this family beyond those three files. Nothing about this family is machine-checked:
"proves" in the abstract is the release's claim, and everything above is read from that LaTeX.

## History of the conjecture

- **Weak-rationality formulation** ([S4:66–69]): Milne introduced it while studying the
  reduction of Shimura varieties and the Langlands–Rapoport conjecture — Conjecture 6.1(A) of the 2000
  IHP notes `Milne2000` ([S10:159]). It asks that a specialized CM Hodge class whose
  components lie in the local spans of divisor products in every realization arise from one rational
  Lefschetz class.
- **Pairing formulation** ([S4:71–73]): Section 10 of the AIM notes `MilneAIM2007` and
  Conjecture 4.1 of *Rational Tate classes* `Milne2009` ([S10:187]).
- **The rationality conjecture as proved here** is the Conjecture 4.1 formulation. Theorem 4.5 of
  `Milne2009` proves that the rationality assertion for all CM abelian varieties is **equivalent** to
  the existence of a good theory of rational Tate classes on varieties over `F` whose connected
  components are products of abelian varieties and projective spaces ([S4:92–95]).
- **Milne's current account** ([S4:153–156]): *Abelian motives and Shimura varieties in
  nonzero characteristic* `Milne2025` ([S10:222]) gives a **conditional** criterion through
  weak lifting of Lefschetz classes on CM Weil triples, and describes the reduction from general Hodge
  classes through CM varieties to Weil classes (Introduction, Question 2.17, Theorem 2.18). The paper
  calls this its route, not a previously proved case.
- **Known positive case before this paper** ([S4:74–76]): a CM abelian variety with simple
  ordinary reduction, **together with all its powers** — in that case every divisor class on the
  reduction lifts (Example 4.2 of `Milne2009`).
- **The good theory being extended** ([S4:78–90]): Definitions 2.1 and 3.1 of `Milne2009`.
  A good theory chooses one graded `Q`-algebra per variety whose scalar extensions give the ℓ-adic
  (`ℓ ≠ p`) and crystalline Tate algebras; it is stable under pullback and pushforward, contains
  divisor classes, and contains specializations of CM Hodge classes. The proof uses axioms (R1), (R4),
  and the goodness axiom (R3) ([S9:272–277]). These correspondences are cohomological;
  their definition does not assert that they are algebraic ([S4:89–90]).
- **Antecedents** ([S4:114–184]): Deligne, Main Theorem 2.11 — every Hodge class on an
  abelian variety is absolute Hodge ([S4:116–118]); Blasius, Theorems 0.3 and 5.3 — its
  compatibility with `p`-adic comparison ([S4:118–119]); Moonen, Theorem 5.6.3 — the
  Blasius–Wintenberger comparison with Ogus's simplification, in the perfect-residue-field form needed
  for the local auxiliary lifts ([S4:120–122]); Milne's Lefschetz classes, Section 5 of
  `Milne1999` ([S10:151]) — a common rational divisor algebra with perfect complementary
  pairing, independent of the Weil cohomology ([S4:122–125]). The determinant classes used
  here belong to the Weil-class theory of Weil, Deligne and André ([S4:127–129]); André's
  refinement of the CM reduction expresses Hodge classes by pullbacks from varieties of split Weil type
  (`Andre1992`, [S4:130–132], with Theorem 1 of `Milne2020` as the detailed account), and
  the paper proves the balanced form it needs in `lem:cm-reduction`; André's motivated cycles give an
  unconditional motivic setting without identifying Hodge classes with algebraic cycles (`Andre1996`,
  [S4:137–140]). Markman, Theorem 1.2 of `Markman2026` (an ICM 2026 contribution,
  [S10:133]): algebraicity of Weil classes on abelian fourfolds of Weil type and abelian
  sixfolds of split Weil type over an imaginary quadratic field — characteristic-zero results, whereas
  the pairing argument here applies in arbitrary dimension starting only from the Hodge class and its
  good reduction ([S4:142–147]).
- **Direct antecedent for the lifting strategy** ([S4:149–152]): Milne asked whether a
  specialized CM Hodge class and a divisor could be lifted together, up to isogeny, to a CM variety,
  and explained the resulting rationality implication — Question 10.6 and Proposition 10.7 of
  `MilneAIM2007`. The paper says it follows this route.

**Prior (my training data, not this repo).** Milne's rationality conjecture is a real, named
conjecture in the arithmetic-geometry literature, and the "rational Tate classes" framework of
Milne 2009 is the standard reference for it. It sits downstream of the Hodge conjecture for abelian
varieties and upstream of the Langlands–Rapoport program on integral models of Shimura varieties,
where a good theory of rational Tate classes is a working prerequisite. The CM case being the
previously known case is consistent with the general fact that CM is where Hodge-class questions on
abelian varieties are tractable, because the extra endomorphisms pin down the Hodge tensors. The
paper's use of Kisin–Zhou's special-point theorem and of affine Deligne–Lusztig geometry is a
recent-technology dependency: `KisinZhou2025` is a 2025 preprint and `GleasonLimXu2026` a 2026
Inventiones paper, so this proof is not buildable from the toolkit available a decade ago. I have
not seen this result and cannot confirm it independently.

## Consequences now that the proof has been found

- **Extension of the goodness axiom (R3).** Milne's good theory of rational Tate classes is required
  by axiom (R3) to contain specializations of **CM** Hodge classes. This paper proves the same
  property for **every** abelian variety with good reduction, keeping one theory fixed
  ([S4:96–103]; `cor:all-hodge-specialization`, [S9:281–300]). The setup
  fixes Milne's class `S₀` of `F`-varieties whose connected components are products of abelian
  varieties and projective spaces, and one good theory `R` on `S₀` supplied by Theorem 4.5, **before**
  varying any abelian variety or Hodge class ([S9:256–264]). The corollary gives a
  unique `ρ_γ ∈ R^r(A₀)` whose ℓ-adic components and crystalline component are the specializations of
  `γ`; the assertion holds for every prime `p`, including `p = 2`, with the prime, place, and theory
  fixed before the variety varies ([S9:301–302]).
- **Algebraicity of the specialization, via family 032.** `cor:algebraic-specialization`
  ([S9:375–399]) produces one rational algebraic cycle `z_γ ∈ CH^r(A₀)_Q` whose ℓ-adic
  class and crystalline class equal the specialization of `γ` in every realization. The manuscript
  states plainly that this is **not** a consequence of the main theorem alone: [S9:372–373]
  says the companion result "is an additional input to the following consequence, not to the proof of
  Theorem 1." and [S4:111–112] repeats it. The input is `[Theorem 1.1]{OpenAICMHodge2026}`
  ([S10:238]), the OpenAI preprint *The rational Hodge conjecture for CM abelian varieties*,
  which is family 032. The proof of the corollary is short: transport gives `γ₀ = b^*κ₀` with `B` CM,
  the CM Hodge theorem makes `κ` the class of a rational cycle on `B`, and that cycle is descended and
  pulled back ([S9:404–420]). This is one of only two `companions` edges in the whole
  ledger, and it is a structural dependency, not a keyword artifact.
- **A rational intersection number, not a cycle.** The main theorem's output is that all
  complementary traces equal one rational number. Combined with the algebraicity corollary, that
  number is `deg(z_γ · y)` for the single cycle `z_γ`, for every
  `y ∈ CH^{d-r}(A₀)_Q` ([S9:394–398]).
- **Explicit non-consequences**, restated because they bound everything above: no Hodge conjecture
  in characteristic zero, no lift to the generic fiber, no Tate conjecture, no uniqueness of `z_γ`,
  no comparison between reduction places ([S9:361], [S9:443–448]).

**Prior (my training data, not this repo).** The consequence that matters in the wider program is
the first bullet. Milne's equivalence between the rationality assertion for CM abelian varieties and
the existence of a good theory of rational Tate classes means the good theory is the object the
Langlands–Rapoport reduction program needs; extending its specialization property to all abelian
varieties with good reduction strengthens that object without constructing it. Family 032's own
[S1] blurb ([S1:755]) claims that, through Milne's theorems, the CM rational
Hodge conjecture yields the Tate conjecture for all abelian varieties over finite fields and the
Hodge standard conjecture for abelian varieties in every characteristic — so the 001 + 032 pair is
the release's route from rationality of specializations to those two open problems. Both families
are tier T0, so this chain has no machine-checked link anywhere in the release. Treat it as the
release's claim.

## Sources

Body markers name a source and, where given, the lines it cites: `[S4:29–56]` is lines 29–56 of S4,
`[S4]` is the file itself. Line numbers are 1-based, as in the shipped files. File names and links
appear once, here.

Manuscript root — `preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/`
(its README carries the title as a link to that PDF, the author, the date, and a bibtex stub [S12];
3,065 lines of LaTeX across `build/`). Every File cell below is the repository-relative path, in
backticks — that is the text the checker resolves — and the hrefs stay relative to this page. S3–S12
and S15 sit under the manuscript root, S1–S2 at the repository root, S13–S14 under `notes/`.

| # | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | the release's catalog — family entry [S1:16], manuscript entry [S1:23], abstract [S1:25]; companion 032 at [S1:755] and its CM Hodge manuscript at [S1:780]. Quoted word-for-word; the release's inline HTML is rendered as markdown (its italic `p` tags became `*p*`, its leading em-space entity was dropped) and its relative PDF link was rewritten to resolve from this page |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | the release's `\resultentry` list — 001 at [S2:78] |
| S3 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/main.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/main.tex) | 73 | root (`\documentclass`); abstract at [S3:58]; section includes |
| S4 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/00_intro.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/00_intro.tex) | 280 | main theorem [S4:29–56]; origins [S4:64–112]; antecedents [S4:114–184]; proof overview [S4:186–265] |
| S5 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/01_preliminaries.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/01_preliminaries.tex) | 227 | comparisons and rational Lefschetz classes; Hodge-tensor comparison [S5:48]; common rational Lefschetz space [S5:84]; `lem:lift-hom` [S5:158] |
| S6 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/02_transport.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/02_transport.tex) | 814 | `prop:transport` [S6:35]; auxiliary Hodge datum [S6:116]; admissible realization [S6:330]; `cor:cm-transport` [S6:777] |
| S7 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/03_filtration.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/03_filtration.tex) | 482 | `thm:filtration` [S7:38]; bounded-degree avoidance [S7:87]; Lagrangian intersections [S7:130]; divisor filtration condition [S7:450] |
| S8 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/04_weil.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/04_weil.tex) | 439 | `def:weil-space` [S8:18]; `prop:weil` [S8:55]; orthogonality [S8:70]; divisor span [S8:205]; `lem:weil-group` [S8:280] |
| S9 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/05_reduction.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/sections/05_reduction.tex) | 448 | CM reduction [S9:18]; main proof [S9:225]; specialization [S9:281]; algebraicity [S9:375]; disclaimers [S9:361–362], [S9:443–448] |
| S10 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/references.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/references.tex) | 274 | 35 `\bibitem`s; Milne 1999/2000/2009/2025 at [S10:151]/[S10:159]/[S10:187]/[S10:222]; Markman [S10:133]; Kisin–Zhou [S10:124]; 032 at [S10:238] |
| S11 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/figures/two-transports.tex`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/build/figures/two-transports.tex) | 28 | figure source — panels at [S11:8], [S11:17] |
| S12 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/README.md`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/README.md) | 18 | title, author, date, bibtex citation stub |
| S13 | [`notes/t0-triage.md`](../../t0-triage.md) | 897 | 001 in the T0 **classification** bucket (K), not the resolution bucket, at [S13:107]; the 001 + 032 chain at [S13:501]. Ours, not in the release |
| S14 | [`notes/catalog.tsv`](../../catalog.tsv) | 373 | the ledger row `fam=001`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
| S15 | [`preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf) | — | the manuscript as shipped |

Links are relative to this page: `../../../` is the repository root and `../../` is `notes/`, so every
row resolves in a local checkout and in GitHub's rendering of this file. A relative link carries no
line anchor — the line numbers live in the markers. GitHub's documented anchor is `#L29` appended to a
file URL, as in `.../blob/main/CONTENTS.md?plain=1#L29` for line 29 of the release's `CONTENTS.md`;
`?plain=1` is needed for the two markdown sources because GitHub renders a markdown file as prose
without line numbers, and range anchors are not documented for markdown files, so a range resolves to
its first line.

Tooling used for this page: `python3 notes/scripts/verify_summaries.py` prints every cited line from
the shipped file, checks every quotation against the lines it cites, and with `--mutant` proves the
quote check discriminates; `.qwen/tmp/number001.py` applied the numbering above.

Absent by construction (T0): `lean/docs/001.md`, any `lean/OAI/**` file, any
`lean/ComparatorChallenges/` entry, any `main_results` config, any verification dir, any reasoning
trace.
