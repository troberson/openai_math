# 007 — Two-point Chowla and the corrected binary Elliott conjecture (Number theory, 1 manuscript, tier T2)

## Original CONTENTS.md summary

[S1:166] (the family entry, first half):

> **007. Ordinary two-point correlations and the corrected Elliott conjecture.** Proves the ordinary
> two-point Chowla conjecture, with a bound $`O(X/(\log X)^c)`$ for Liouville correlation sums along
> fixed nonproportional affine forms,

The release marks the exponent's positivity with inline HTML, so the entry is quoted here in two
halves around it.

[S1:166] (the same entry, second half):

> More generally, proves the binary corrected Elliott conjecture for complex multiplicative
> functions bounded by one when one factor is uniformly nonpretentious against each fixed Dirichlet
> character times $`n^{it}`$ for $`|t|\le X`$.
> ([Lean](../../../lean/docs/007.md))

The release's own LaTeX entry gives the family the shorter title "Two-point Chowla and the corrected
binary Elliott conjecture" ([S2:90]), and the release attributes a reasoning trace to it: "Ordinary
two-point correlations of multiplicative functions" ([S3:28], [S24]). One manuscript carries the
whole family ([S4]), dated September 24, 2026 ([S4:5], [S5:46]).

## Undergraduate summary

Write *λ*(*n*) = (−1)^*Ω*(*n*), where *Ω*(*n*) counts the prime factors of *n* with multiplicity: *λ*(*n*)
is +1 when *n* has an even number of prime factors and −1 when it has an odd number. **Chowla's
conjecture** says these parities behave independently — that the average of *λ*(*n*)*λ*(*n*+*h*) over
*n* ≤ *X* tends to zero for every fixed shift *h*. It is the parity analogue of the prime-pair
conjectures, and even the two-point case was open.

What this paper proves is the **ordinary** version, and the adjective is the hard part. A
logarithmically averaged correlation weights each *n* by 1/*n*; an ordinary average weights every
integer up to the cutoff equally. As the manuscript puts it, "Logarithmic weighting combines
information from many multiplicative scales; an ordinary estimate must control the terminal scale
itself." ([S6:15–16]) Every previous two-point result for this problem kept the logarithmic weight.
The theorem is stated for every fixed pair of nonproportional affine forms *a*₁*n*+*b*₁, *a*₂*n*+*b*₂, and
it gives a saving of a power of log at *every* cutoff: the sum is at most *C**X*/(log *X*)^*c* with *c* > 0
absolute, so the exponent does not depend on the forms ([S6:20–34]). Taking *a*₁ = *a*₂ = 1, *b*₁ = 0,
*b*₂ = *h*, "this resolves the ordinary two-point Chowla conjecture, with a logarithmic saving."
([S6:36–37])

The second theorem is about general multiplicative functions, and it is qualitative. Elliott asked
whether the average of *f*₁(*n*+*h*₁)*f*₂(*n*+*h*₂) tends to zero for bounded multiplicative functions.
The obstruction is a function that *pretends* to be a twist *χ*(*n*)*n*^*it*: it correlates with that
twist at every scale, and then its correlation with *f*₂ need not vanish. The corrected hypothesis,
due to Matomäki–Radziwiłł–Tao, requires that *f* be far from *every* twist *χ**n*^*it* simultaneously,
for every fixed character *χ* and all |*t*| ≤ *N* as *N* grows — the manuscript calls this being
**uniformly nonpretentious** ([S6:58–61]). Under that assumption on just one of the two functions,
the shifted averages tend to zero ([S6:64–72]): "This proves the binary corrected Elliott conjecture
for ordinary averages. The functions may be complex, need not have modulus one, and need not be
completely multiplicative." ([S6:74–76])

The shape of the proof, sketched at [S6:188–252], [S7:7–18], [S8:24–40], [S9:1–9], [S10:19–23],
[S11:7–50], [S12:86–102] and [S13:83–101]:

1. **Dilate, and build a graph.** Compare the correlation at *n*, *n*+*h* with the correlation at
   *dn*, *d*(*n*+*h*). Each dilation *d* becomes an edge of displacement *hd*, and the correlation
   change becomes an operator on a graph over the integers. Short-interval Fourier estimates control
   the change when divisibility indicators are replaced by signed expressions; closed-walk estimates
   bound the operator.
2. **Part I, step 1 — manufacture divisors in a short multiplicative interval.** Fix *J* disjoint
   "supplies" of primes, each with reciprocal mass comparable to a large constant *W*, plus a
   squarefree padding divisor from a disjoint prime set. The supplies contribute factors
   1*p*|*n* − 1/*p*, which have mean zero under uniform residues.
3. **Part I, step 2 — compare integer residues with independent residues.** The prime sets grow with
   *X*, so averaging over the full joint period is useless at the needed scale. The residue tests are
   encoded as a low-depth Boolean circuit and their bit law is corrected to exact bounded
   independence, which is where Braverman's theorem applies.
4. **Part I, step 3 — count the closed walks.** Arithmetic relations kill the walks with many
   unlit occurrences, large constraint rank, or many singletons. What is left is described by a
   forest, whose pattern count is uniform over all padding values, so the padding weights can be
   summed afterwards in one residue environment.
5. **Part I, step 4 — transfer the moment bound to the operator.** A nonbacktracking-style transfer
   bounds the sum of self-adjoint edge matrices; the edge normalization factor *L* buys 1/*L* per
   interval against *L* intervals. The losses are exponential in *J* with absolute bases, so choosing
   *W* large gives exponential decay in *J* — and since *J* grows like log log *X*, that is a
   power-of-logarithm saving.
6. **Part I, step 5 — deduce the affine bound.** Complete multiplicativity turns the affine product
   into a Liouville factor times a correlation in one residue class modulo *a*₁*a*₂; the progression
   estimate applies to that class with no coprimality condition, and the endpoints match exactly.
7. **Part II — fix the graph first, then take the long average.** Here the input contains a
   nonpretentiousness distance that diverges with no prescribed rate, so all graph parameters are
   fixed at a scale *B* before *X* → ∞. Two bands of primes (a weighted *core* band and a *center*
   band) turn any persistent correlation bias into a sum of size about *B*⁻¹ in one short
   multiplicative interval, while the graph estimate gives *O*(*B*⁻¹⁻^c\*/2^). The contradiction is
   taken with *B* fixed, then *B* increased.

## Graduate summary

The quantitative theorem is stated as "A logarithmic saving for affine Liouville correlations"
([S6:20–34]): there is an absolute *c* > 0 such that for every fixed *a*₁,*a*₂ ≥ 1 and *b*₁,*b*₂ ≥ 0 with
*a*₁*b*₂ − *a*₂*b*₁ ≠ 0 there is *C*_{*a*₁,*a*₂,*b*₁,*b*₂} with

|Σ_{*n*≤*X*} *λ*(*a*₁*n*+*b*₁)*λ*(*a*₂*n*+*b*₂)| ≤ *C**X*/(log *X*)^*c* for *X* ≥ 3.

Two boundary conditions are part of the statement: "The cutoff \(X\) may be any real number. No
coprimality condition is imposed on the coefficients." ([S6:32–33]) The route is stated in the
introduction — the saving is first obtained for *λ*(*n*)*λ*(*n*+*h*) in each fixed residue class modulo
each fixed modulus, "including nonunit and zero classes", and "Complete multiplicativity then gives
the affine conclusion." ([S6:41–43]) The intermediate target is the progression estimate [S7:7–18],
whose proof opens: "Our first task is to find many divisors in short multiplicative intervals,
retaining a fixed positive fraction of their total reciprocal weight." ([S7:24–25])

The qualitative theorem [S6:64–72] is the binary corrected Elliott conjecture for ordinary averages,
with the corrected hypothesis [S6:58–61] imposed on one original factor. Its scope is stated as
plainly as its content: "This proves the binary corrected Elliott conjecture for ordinary averages.
The functions may be complex, need not have modulus one, and need not be completely
multiplicative." ([S6:74–76]) and "We make no quantitative rate claim for this class of functions."
([S6:78–79]) The affine and progression consequences are collected in Part III, where "We now deduce
correlations on arbitrary fixed progressions and affine forms" from the shifted theorem
([S15:4–5]); the progression form holds "through all real $X$, including nonunit residue classes"
([S15:193]), and Liouville is verified to satisfy the hypothesis outright, with an explicit rate
([S15:268–278]).

The two graph arguments are deliberately not the same machine. "The two proofs use different vertex
weights, and their cancellation mechanisms must be matched to those weights." ([S6:194–195]) Part I
buys a rate; Part II buys a limit. Part II's graph estimate [S12:86–102] is stated for arbitrary
bounded test sequences — "Its test functions are arbitrary bounded sequences; no multiplicativity
enters its statement or proof." ([S12:3–6]) — and the analytic reduction is what imports the
arithmetic: "rules out a nonzero multiplicative correlation. The first step produces a large sum
with ordinary divisibility indicators." ([S13:3–5]) A divisor interval carrying reciprocal mass
c*L*₀/*B* is extracted from the bias ([S13:83–101]), the finite-residue bound is converted to long
integer intervals by a singular-value moment ([S14:4–6]), and the two bands split the work: the core
band gives decay from divisor size and from the count of core primes at a vertex, while the center
band, whose signed factor is not mean zero under uniform residues, supplies the extra power
([S6:241–252]). Part I's two delicate points are named in the introduction: the residue law must be
corrected to *exact* bounded independence before Braverman's theorem applies ([S6:213–218],
[S8:8–9]), and the surviving repetition patterns are counted by a forest whose bound is uniform over
padding values ([S6:218–224], [S9:3–9]). The spectral step is explicit that it is proved for
self-adjoint edge operators directly, because "distinct edge operators need not commute"
([S10:19–23]).

What the result does **not** say is delimited in the statement paragraphs. The implied constants
"need not be effective", and "no uniformity for coefficients growing with \(X\) is asserted"
([S6:38–40]); the exponent is independent of the forms, and only the implied constant depends on
them ([S11:48–49]). The qualitative theorem carries no rate ([S6:78–79]). The comparison with prior
work is framed the same way: the logarithmically weighted bounds of Helfgott–Radziwiłł and Pilatte
"retain the logarithmic weight" ([S6:138–149]), the earlier ordinary results of Tao–Teräviäinen and
of Klurman–Mangerel–Teräviäinen hold on sets of scales of logarithmic density zero and of full
upper logarithmic density respectively ([S6:160–168]), and the recent quantitative progression
estimates of Tao–Teräviäinen allow coefficients to grow slowly outside a controlled exceptional set
of scales ([S6:168–174]) — whereas "The results here concern every cutoff, with the affine forms
fixed." ([S6:173–174])

Formalization status is split, and the split is the notable fact about this family. The ledger
records 1 manuscript, 0 formalized, 0 `main_results` entries, 2 comparator challenges, 1 scope note.
Consistent with that, `lean/formalization.yaml` contains no entry for this manuscript at all
([S17]). The scope note nevertheless describes formalized content: "The formalization proves
ordinary two-point cancellation for multiplicative functions." ([S16:9]) and, for two one-bounded
multiplicative functions with one uniformly nonpretentious factor, "These are ordinary averages,
with no logarithmic averaging." ([S16:11]) Two comparator challenge configurations name the target
modules and theorem names and permit only propext, Quot.sound and Classical.choice ([S18], [S19]);
their challenge statements are the `sorry`-bearing side ([S20:43–65]). On the solution side,
`TwoPointCorrelations/FinalMain.lean` states all three target theorems by delegating to proved
results ([S21:10–32]), and the Elliott theorem is stated in
`OrdinaryCorrelations/Elliott/BinaryCorrectedElliott.lean` ([S22:37–42]). Measured on the shipped
tree, `lean/OAI/NumberTheory/OrdinaryCorrelations/` is 637 files and 71,648 lines with zero `sorry`,
and `lean/OAI/NumberTheory/TwoPointCorrelations/` is 217 files and 22,675 lines with zero `sorry`.
Those are source-level facts about the shipped text: zero `sorry` is not a comparator pass, and it
does not mean the library elaborates — nothing in this release's metadata records a run.

## History of the conjecture

Chowla's conjecture is named for a 1965 book: "Chowla's conjecture predicts vanishing Liouville
correlations at every fixed collection of distinct shifts" ([S6:102–103]), cited to Chowla's *The
Riemann Hypothesis and Hilbert's Tenth Problem* ([S23:101–109]). Its binary case "asks whether the
parities of the numbers of prime factors of \(n\) and \(n+h\) become uncorrelated for each fixed
\(h\ge1\)." ([S6:103–105]) Elliott's generalization to bounded multiplicative functions is cited to a
1992 note, "On the correlation of multiplicative functions" ([S23:111–119]), and the manuscript
records that "Elliott extended the correlation problem to bounded multiplicative functions"
([S6:110–111]).

The obstruction and the distance both predate the conjectures' correlation form. The twist
obstruction "is already central to Hal\'asz's theory of one-point mean values" ([S6:111–113]), cited
to Halász 1971 ([S23:121–128]) with the modern treatment of Granville, Harper and Soundararajan
([S23:142–148]); the distance used in the hypothesis "belongs to the pretentious approach developed
by Granville and Soundararajan" ([S6:114–116]), cited to *Large character sums: pretentious
characters and the Pólya--Vinogradov theorem*, 2007 ([S23:130–139]). The correction to Elliott's
original condition is the load-bearing historical step: Matomäki, Radziwiłł and Tao "showed why
Elliott's original condition needs correction for complex functions: a function can imitate
different twists at successive scales without imitating any one fixed twist globally."
([S6:116–119]) Their corrected condition is equivalent to the one used here ([S6:119–121]), cited to
*An averaged form of Chowla's conjecture*, 2015 ([S23:1–12]).

The immediate predecessors split by weight. Unweighted short-interval control comes from
Matomäki–Radziwiłł, *Multiplicative functions in short intervals*, 2016 ([S23:14–25]), whose
corollary gave each fixed-shift Liouville correlation a saving 1 − *δ*(*h*) at all sufficiently large
cutoffs ([S6:123–128]). The logarithmic line runs Tao 2016 ([S23:27–36]) for the logarithmically
averaged binary Elliott theorem on nonproportional affine forms ([S6:132–134]), then
Helfgott–Radziwiłł, *Expansion, divisibility and parity*, 2021 ([S23:58–64]), for
log *x*/√(log log *x*) ([S6:135–138]), then Pilatte, *Improved bounds for the two-point logarithmic
Chowla conjecture*, published electronically 10 September 2026 ([S23:66–74]), for a
power-of-logarithm saving ([S6:139–141]). The graph machinery this paper adapts is theirs:
high traces, recurrence constraints, cancellation at primes occurring once, plus proposed composite
steps and nonbacktracking operators ([S6:149–152]), developed further by Pilatte through centered
prime factors, prohibited sequences, triangular arithmetic constraints and a rank-truncated
intersection sieve ([S6:152–155]). "Our two graph arguments adapt these constructions to different
weights and orders of limits." ([S6:156–158])

On the ordinary side, the prior state was scale-restricted: Tao and Teräviäinen "obtained binary
cancellation outside a set of scales of logarithmic density zero" under the same hypothesis
([S6:161–163], cited to 2019 [S23:38–48]); Klurman, Mangerel and Teräviäinen relaxed the hypothesis
and obtained cancellation along a set of scales of full upper logarithmic density ([S6:164–168],
cited to 2023 [S23:213–219]); and Tao–Teräviäinen's quantitative progression estimates give
logarithmic savings for affine Liouville correlations with slowly growing coefficients outside a
controlled exceptional set of scales ([S6:168–173], cited to 2026 [S23:50–56]).

The combinatorial input has its own lineage, which the manuscript states in one paragraph: bounded
independence for Boolean circuits, from Linial and Nisan's *Approximate inclusion-exclusion*
([S23:184–190]) through Bazzi's depth-two theorem and Razborov's simpler proof ([S23:167–182]) to
Braverman's theorem for every fixed depth, *Polylogarithmic independence fools AC⁰ circuits*, 2010
([S23:76–87]), with the local Fourier calculation being "a form of the almost-to-exact independence
construction of Alon, Goldreich, and Mansour" ([S6:182–184], cited to 2003 [S23:154–160]).

## Consequences now that the proof has been found

The internal consequence is that the affine and progression forms are theorems, not hypotheses, at
every cutoff. The affine deduction is a short computation, and the manuscript is explicit that it
costs nothing in the exponent: "The progression estimate for Liouville gives the same logarithmic
exponent for every fixed affine pair. The finite initial interval affects only the constant."
([S11:3–5]) Complete multiplicativity gives the identity *λ*(*a*₁*n*+*b*₁)*λ*(*a*₂*n*+*b*₂) =
*λ*(*l*)*λ*(*ln*+*c*₀)*λ*(*ln*+*c*₀+*h*) with *l* = *a*₁*a*₂ and *h* = |*a*₁*b*₂ − *a*₂*b*₁| ([S11:10–19]), and the
endpoints match exactly, an identity that "includes both determinant signs and noninteger cutoffs"
([S11:39]). The conclusion is stated as: "The exponent has not changed and is independent of the
affine coefficients; only the implied constant depends on them." ([S11:48–49])

For general multiplicative functions, Part III converts the shifted theorem into progressions and
affine forms by finite local expansions at the primes dividing a modulus or a dilation, so complete
multiplicativity is not needed: "We now deduce correlations on arbitrary fixed progressions and
affine forms" ([S15:4–5]), with uniform nonpretentiousness stable under character twists and
conjugation ([S15:14–28]). The progression form holds through all real cutoffs and in every residue
class ([S15:181–194]). Liouville's own qualification is quantitative, with a rate of
¼√(log log *X*) − *O*(*χ*(1)) ([S15:268–278]), proved from an argument of Granville and Soundararajan
as formulated by Matomäki, Radziwiłł and Tao ([S15:262–266]). The practical effect is that the
Chowla side and the Elliott side of the family now share one hypothesis and one proof style, and the
nonpretentiousness condition is no longer a hypothesis about Liouville — it is verified for it.

Two absences are part of the consequence and are stated by the paper itself. There is no rate for
the general class ([S6:78–79]), and no uniformity for coefficients growing with the cutoff
([S6:38–40]), so the affine theorem does not extend the slowly-growing-coefficient results of
Tao–Teräviäinen in that direction ([S6:168–174]); the two statements are complementary, each
stronger on its own side of the trade.

The release-side consequence is a coverage gap worth recording. The family ships 854 Lean files and
94,323 lines across the two solution trees, with zero `sorry` in both, and two comparator challenge
configurations naming three target theorems ([S18], [S19], [S20], [S21], [S22]) — yet the release's
own `formalization.yaml` records no entry for the manuscript, and the ledger's formalized and
`main_results` counts for this family are both zero ([S17]). Read as a source-level fact, the
formalization is present in the source tree and absent from the release's index of formalized
results; the release publishes the derivation as a reasoning trace ([S3:28], [S24]), which is the
only published derivation artifact for this family.

## Sources

Every path in the File column is repository-relative and every link resolves from this page's
directory. Line numbers are 1-based as shipped. The CONTENTS.md blurb is quoted verbatim; its
inline link was rewritten to a relative one so it resolves from this page, and the release's inline
HTML for the exponent's positivity is quoted around rather than transcribed, because this page
carries no raw HTML.

| Src | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release blurb, family 007 at line 166 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | LaTeX entry `\resultentry{007}`, line 90 |
| S3 | [`README.md`](../../../README.md) | 51 | Trace attribution, line 28 |
| S4 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/README.md`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/README.md) | 18 | Manuscript README (title, author, date, bibtex stub) |
| S5 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/main.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/main.tex) | 90 | Title line 40, date line 46, abstract 49–58, three Parts |
| S6 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex) | 278 | Theorems, prior work, main ideas, organization |
| S7 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/01-setup.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/01-setup.tex) | 199 | Progression target, prime supplies, parameters |
| S8 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/02-finite-law.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/02-finite-law.tex) | 239 | Finite residue comparison via bounded independence |
| S9 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/06-forest.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/06-forest.tex) | 378 | Forest encoding of surviving repetition patterns |
| S10 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/07-spectral.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/07-spectral.tex) | 333 | Spectral transfer, bound at every scale |
| S11 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/08-affine.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/08-affine.tex) | 51 | Proof of the affine bound |
| S12 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/graph-setup.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/graph-setup.tex) | 120 | Weighted divisor graph, graph estimate |
| S13 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/analytic-transfer.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/analytic-transfer.tex) | 671 | Reduction of a correlation bias to the graph |
| S14 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/localization.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/localization.tex) | 167 | High traces to long integer intervals |
| S15 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/affine-corollaries.tex`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/affine-corollaries.tex) | 363 | Part III: progressions, affine forms, Liouville |
| S16 | [`lean/docs/007.md`](../../../lean/docs/007.md) | 18 | Scope note: what the formalization proves |
| S17 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1,783 | Release index of formalized results; no entry for this manuscript |
| S18 | [`lean/ComparatorChallenges/OrdinaryElliott.json`](../../../lean/ComparatorChallenges/OrdinaryElliott.json) | 14 | Comparator config, Elliott challenge |
| S19 | [`lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.json`](../../../lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.json) | 16 | Comparator config, three two-point theorems |
| S20 | [`lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean`](../../../lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean) | 71 | Challenge statements, `sorry` on the challenge side |
| S21 | [`lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean`](../../../lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean) | 36 | Solution side: the three target theorems |
| S22 | [`lean/OAI/NumberTheory/OrdinaryCorrelations/Elliott/BinaryCorrectedElliott.lean`](../../../lean/OAI/NumberTheory/OrdinaryCorrelations/Elliott/BinaryCorrectedElliott.lean) | 56 | Solution side: the Elliott theorem |
| S23 | [`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/refs.bib`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/refs.bib) | 219 | Manuscript bibliography: authors, titles, years |
| S24 | [`reasoning_traces/ordinary-two-point-correlations.pdf`](../../../reasoning_traces/ordinary-two-point-correlations.pdf) | — | Published reasoning trace for this family |
