# 017 — The irrationality exponent of π is 2 (Number theory, 1 manuscript, tier T2)

## Original CONTENTS.md summary

The release lists one manuscript, dated September 24, 2026 [S4:5], and attributes a reasoning trace
to this family [S3:28]. Its blurb is titled "017. The
irrationality exponent of π is 2" [S1:488]. The release marks the emphasis in that blurb with inline
HTML and its inequality with an entity, so the blurb is quoted here from its tag-free tail.

[S1:488] (the family entry, tag-free tail):

> every rational $`p/q`$ satisfies $`|\pi-p/q|\ge q^{-2-\varepsilon}`$. This also proves convergence
> of the Flint–Hills series $`\sum_{n\ge1}1/(n^3\sin^2 n)`$, with angles in radians.
> ([Lean](../../../lean/docs/017.md))

The blurb is quoted verbatim; the release's inline tags and its `>` entity are quoted around rather
than transcribed, because this page carries no raw HTML, and the Lean link is rewritten so it
resolves from this page. `overview.tex` carries the entry as
`\resultentry{017}{The irrationality exponent of $\pi$ is $2$}` [S2:110].

## Undergraduate summary

**How closely can the rationals approach π?** Write μ(π) for the largest exponent for which
infinitely many fractions *p*/*q* get within 1/*q*^μ^. The pigeonhole principle forces μ(π) to be at
least 2, so the interesting question is how much larger it can be. The manuscript proves it is
exactly 2 [S5:64–71], [S8:55–130]. In the plainest form: fix any exponent bigger than 2, and once
the denominators are large enough, *no* fraction at all — reduced or not — comes closer to π than
1/*q*^ν^. The paper's own abstract states both halves of the result: "We prove the conjecture that
the irrationality exponent of \(\pi\) is \(2\)." and "As a consequence, the classical Flint--Hills
series \(\sum_{n\ge1}1/(n^3\sin^2 n)\) converges, with angles in radians." [S5:43–45]

That is a statement about *every* sufficiently large denominator, and the distinction matters. The
threshold may depend on the exponent you chose, and the paper does not compute it: "The threshold
may depend on \(\nu\), and the argument does not give it effectively. In particular, an exponent of
\(2\) is different from a uniform positive lower bound of the form \(c/q^2\), or equivalently from
bounded continued-fraction partial quotients." [S5:74–78] So this does not say the continued
fraction of π behaves tamely; it says the fractions cannot be exceptionally good, infinitely often,
at any rate faster than 1/*q*^2^ times a small slack.

**Proof sketch.** The paper describes its own shape in one sentence: "The proof uses a multivariable
interpolation theorem to construct a nonzero determinant, then compares two incompatible estimates
for its absolute value." [S5:159–161] The steps, in the order the paper fixes them:

1. Assume the opposite: for some fixed exponent ν > 2, fractions keep approximating π better than
   *q*^−ν^ at arbitrarily large denominators [S5:157–254].
2. Choose a dimension, a weight, and a collection of centers on a logarithmic curve — the
   approximations themselves — and fix all of them before letting the degree of an auxiliary
   polynomial tend to infinity [S6:1–57], [S8:55–130].
3. An interpolation theorem then produces a polynomial of that degree whose derivatives at all
   those centers are simultaneously small [S6:1–57].
4. Feed that polynomial into a determinant built from the approximations. Two estimates collide.
   Number theory says the determinant is a nonzero rational number with a controlled denominator, so
   its size has a *lower* bound [S7:1–97]. Analysis says the same determinant is *at most*
   exponentially small, because the polynomial is small at every center [S7:260–285], [S7:337–370].
5. For a suitable choice of parameters the upper bound is smaller than the lower bound, which is
   impossible. The assumption was false, so μ(π) is at most 2. Pigeonhole gives the reverse
   inequality, so μ(π) is exactly 2 [S8:55–130].

The consequence is a series that many people checked numerically and nobody could settle.
∑ *n*^−3^ sin^−2^(*n*) — angles in radians — converges [S9:47–91]. More is true: for positive *a*,
*b*, the family ∑ *n*^−*a^ |sin *n*|^−*b^ converges exactly when *a* is bigger than both 1 and *b*
[S5:102–109], [S9:97–104].

## Graduate summary

**The theorem restated.** For every ν > 2 there is a threshold *Q*(ν) such that every integer
numerator *p* and every positive integer denominator *q* ≥ *Q*(ν) satisfy |π − *p*/*q*| ≥ *q*^−ν^
[S5:64–71]. The inequality is stated for unreduced fractions, and the proof exploits that: the
contradiction "allowed unreduced fractions and zero error" [S8:137–142]. The exact supremum
characterization — μ(π) = 2, not merely an eventual lower bound — is recovered by a pigeonhole
argument on 0, π, …, *N*π modulo one, which produces approximations at error 1/*q*² and forces the
reduced denominators to be unbounded [S8:144–155]. No prior irrationality measure for π enters the
argument: "no prior irrationality bound for \(\pi\) is assumed." [S5:253–254]

**The moves.** Three of them carry the weight.

*Uniform interpolation.* The engine is a multivariable interpolation theorem whose thresholds are
independent of the interpolation points: "Its essential uniformity is that the weights can be chosen
before the interpolation points: each coordinate weight has a lower threshold depending on the
earlier weights, but not on the locations of the points." [S6:4–7] The paper is explicit that this
is not the classical form: "Our application requires a different interpolation statement, adapted to
logarithmic curves and with thresholds independent of their centers." [S5:165–166] The centers are
the approximations being contradicted, so a theorem whose thresholds moved with the centers would
not close.

*Order of quantifiers.* The dimension is fixed before the approximation scales, and everything is
fixed before the degree tends to infinity: "The order of choices is essential: the dimension is
fixed before the approximation scales, and all these data are fixed before the polynomial degree
tends to infinity." [S8:5–7] The contradiction is only available because the polynomial's degree is
the last thing to grow [S8:131–135].

*Where the determinant's upper bound comes from.* The rows are grouped by a transverse index, and
the analytic cancellation is not global: "Our rows fall into different transverse-index groups, so
this cancellation is used only inside a fixed group." [S7:263–265] The arithmetic side is a
*p*-adic size count on a nonzero rational determinant [S7:83–97]; the analytic side bounds the same
determinant after translating the data to entire functions [S7:152–192], and the two are compared
under explicit budget inequalities [S7:353–370]. The geometry stage prescribes coefficients through
jets, and the paper notes that prescribing a coefficient is not the same as prescribing a derivative
at a point [S5:178–185].

**What it does not say.** Not a uniform bound *c*/*q*², and nothing about the partial quotients of
π [S5:74–78]. Not an effective threshold. Not the equality boundary of the two-parameter series
question, which the paper locates strictly inside the bracket left by the two cited criteria
[S5:94–100]. The quantitative ladder of published exponents is context, not input: "These
quantitative bounds are context, not inputs to our proof." [S5:134–135]

**Formalization status.** Source-level, from `lean/docs/017.md`: the selected statement proves the
exponent-two claim in the form "For every $\nu>2$, all sufficiently large positive denominators
$q$ satisfy $|\pi-p/q|\ge q^{-\nu}$ for every integer numerator $p$" and "also states the exact
supremum characterization using infinitely many rational approximations" [S11:9]. The
exclusion is explicit and narrower than it first reads: "The paper's convergence consequence for the
Flint–Hills series is outside this selected statement." [S11:11] That exclusion is about the
comparator's selected statement, not about the tree. The comparator challenge
`lean/ComparatorChallenges/PiExponent.lean` states the exponent claim with `sorry` at line 15
[S13:15], permits `propext`, `Quot.sound` and `Classical.choice`, and sets `enable_nanoda: false`
[S14:1–14]. The formalized tree for this family is `lean/OAI/NumberTheory/PiExponent/`: 869 files,
94,948 lines, zero `sorry`, spread over Ampleness, Analysis, Approximation, Cohomology, Geometry,
Jets, LocalAlgebra and Polynomials. The statement itself is formalized as a supremum definition of
the exponent plus an eventual-lower-bound predicate over integer denominators [S16:13–23].
`Main.lean` proves the eventual lower bound, the integer-eventual
version, `pi_irrationalityExponent_eq_two`, the comparator `main`, and separately
`flint_hills_summable` [S15:17–32] — so the Flint–Hills consequence *is* formalized, just outside
the selected statement, via a dyadic spacing lemma and a reduction from a distance sum [S17:142–155],
[S18:138–156]. Two coverage gaps, measured. First, `lean/formalization.yaml` has no entry naming
this manuscript [S12:1–1668], which is why the ledger reports `paps_form 0` and `mainres 0` beside
those 94,948 lines; the ledger's evidence columns count bibliography entries, not Lean source.
Second, the generalized criterion *a* > max{1, *b*} is not formalized: the Analysis directory
formalizes the classical series only [S18:138–156], and a search for `max {` in it returns nothing
[S17:1–161], [S18:1–160]. Zero `sorry` in shipped source is a source-level fact, not a comparator
pass, and the library is not built here.

## History of the conjecture (if known)

The manuscript's own account, with the entries it cites.

**The exponent ladder.** Mahler "established a finite irrationality exponent for \(\pi\)" [S5:113–116]
with 42, and proved an eventual bound with exponent 30 [S10:81–90]. Mignotte brought the published
exponent to 21 and the eventual bound to 20 [S5:117–119], [S10:92–103]. Chudnovsky's 1982 thesis
attached an exponent to π for the first time [S5:119–121], [S10:105–118]. Hata reached 8.01604533…
[S5:123–124], [S10:120–130]. Salikhov's 2008 result, published in 2010, is the best published
exponent, 7.606308… [S5:127–128], [S10:1–11], [S10:140–150]. Zeilberger and Zudilin's 2020
computer-assisted bound is 7.103205334137… [S5:129–131], [S10:13–23], and Bai's 2026 preprint
improves it to 7.101862832357 [S5:132–134], [S10:221–229]. The manuscript treats all of these as
context [S5:134–135]. The general machinery behind the ladder — Laurent's method, Philippon's
criteria, Roth's theorem, Farhi's and Demailly's constructions — is in the same bibliography
[S10:152–162], [S10:164–172], [S10:174–184], [S10:186–196], [S10:198–204], [S10:206–219].

**The Flint–Hills series.** The manuscript dates the question to a Pickover column, with
Alekseyev's 2011 necessary condition and Meiburg's 2022 sufficient condition bracketing the answer
at 5/2 [S5:80–100], [S10:25–31], [S10:33–39]. It is candid that the gap is unresolved by the cited
criteria: "Neither cited criterion settles its equality boundary at \(5/2\)." [S5:99–100]

**The trigonometric side.** Dan and López Zapata's 2026 preprint is cited for the
∑ *n*^−*a^ |sin *n*|^−*b^ family [S5:139–142], [S10:231–239], [S10:241–249]. The manuscript records
a retraction plainly: the convergence claim of Mantzakouras and López Zapata "was withdrawn in
September 2026 because its proof did not establish convergence or the asserted irrationality
bound" [S5:142–145], [S10:261–269].

**The competing claim.** Carella's 2022 paper claims both exponent two and the strictly stronger
bounded-partial-quotient property; the manuscript uses neither [S5:146–147], [S10:251–259]. It
identifies a sign obstruction in the displayed proof of the stronger assertion, and limits what that
objection decides: "This objection concerns the displayed proof of the stronger assertion; it does
not decide the exponent-two claim or the truth of the stronger conclusion." [S5:147–148],
[S5:153–155]

**Prior (my training data, not this repo).** μ(π) = 2 was the expected value; the published ladder
was understood to be an artifact of method, not evidence about π.

## Consequences now that the proof has been found (if known)

**A named open question closes.** The Flint–Hills series converges, and the manuscript proves more
than the headline: a two-parameter family gets an exact criterion rather than a one-sided bound.
For fixed *a*, *b* > 0 the series ∑ *n*^−*a^ |sin *n*|^−*b^ "converges if and only if
\(a>\max\{1,b\}\)." [S9:97–104] The divergence side is a continued-fraction argument on the
convergents of π, and it settles the boundary the earlier criteria left open: the series diverges
throughout 1 < *a* ≤ *b*, including the boundary case *a* = *b* > 1 [S9:153–154]. The proof of the
corollary is short because the work is the dyadic spacing estimate that precedes it [S9:11–64].

**The quantitative ladder stops mattering for π.** Every published exponent from 42 downward is
superseded by the exact value, and the paper never depended on them [S5:134–135]. What remains open
about π is the class of statements the paper explicitly declines: a uniform *c*/*q*², bounded
partial quotients, an effective threshold [S5:74–78]. Carella's stronger claim is untouched by this
work, and the manuscript says so [S5:146–147].

**The transferable object is the interpolation theorem.** Its thresholds do not depend on the
centers [S6:4–7], [S6:24–57], which is what lets the centers be the approximations under
contradiction [S5:165–166]. Combined with the fact that no prior irrationality bound is assumed
[S5:253–254], the argument is self-contained in a way the ladder was not, and the order-of-choices
discipline is stated as part of the method [S8:5–7].

**Prior (my training data, not this repo).** The consequence is methodological, not numerical. The
open cases move to numbers where this shape of argument has no logarithmic curve to interpolate
along — the exponential values e^α^, and constants where integral constructions already reach
exponent 1, as with e. The manuscript's own bibliography points at that program, citing Zudilin's
essay on "irrationality measures of π and other logarithms" [S10:132–138], and the classical
results on logarithms at algebraic arguments are in the same list [S10:70–79].

## Sources

| ID | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,169 | Release blurb, at line 488 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Catalog entry, at line 110 |
| S3 | [`README.md`](../../../README.md) | 50 | Trace attribution, at line 28 |
| S4 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md) | 18 | Manuscript metadata; date at line 5 |
| S5 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) | 264 | Abstract, theorem statements, history, proof outline |
| S6 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/interpolation.tex) | 584 | Uniform interpolation theorem |
| S7 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/determinant.tex`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/determinant.tex) | 432 | Determinant: arithmetic lower bound, analytic upper bound, comparison |
| S8 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/conclusion.tex`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/conclusion.tex) | 156 | Parameter choices and the proof of the main theorem |
| S9 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/series.tex`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/series.tex) | 155 | Flint–Hills convergence and the generalized criterion |
| S10 | [`preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/references.bib`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/references.bib) | 269 | Cited prior work behind the history |
| S11 | [`lean/docs/017.md`](../../../lean/docs/017.md) | 17 | Scope note: selected statement and exclusion |
| S12 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1,668 | No entry naming this manuscript |
| S13 | [`lean/ComparatorChallenges/PiExponent.lean`](../../../lean/ComparatorChallenges/PiExponent.lean) | 19 | Comparator challenge, `sorry` at line 15 |
| S14 | [`lean/ComparatorChallenges/PiExponent.json`](../../../lean/ComparatorChallenges/PiExponent.json) | 14 | Challenge config: target module, axioms, `enable_nanoda` |
| S15 | [`lean/OAI/NumberTheory/PiExponent/Main.lean`](../../../lean/OAI/NumberTheory/PiExponent/Main.lean) | 36 | Formalized main theorem and Flint–Hills summability |
| S16 | [`lean/OAI/NumberTheory/PiExponent/Statement.lean`](../../../lean/OAI/NumberTheory/PiExponent/Statement.lean) | 27 | Formalized statement of the exponent claim |
| S17 | [`lean/OAI/NumberTheory/PiExponent/Analysis/DyadicSpacing.lean`](../../../lean/OAI/NumberTheory/PiExponent/Analysis/DyadicSpacing.lean) | 161 | Dyadic spacing lemma behind the series corollary |
| S18 | [`lean/OAI/NumberTheory/PiExponent/Analysis/FlintSine.lean`](../../../lean/OAI/NumberTheory/PiExponent/Analysis/FlintSine.lean) | 160 | Reduction of the series to a distance sum |
| S19 | [`reasoning_traces/irrationality-exponent-of-pi.pdf`](../../../reasoning_traces/irrationality-exponent-of-pi.pdf) | — | Published reasoning trace |

The published reasoning trace for this family is the PDF at [S19]. The manuscript also ships
`paper.pdf` (494,460 bytes) beside its LaTeX tree; the LaTeX sources are the readable form and are
what this page cites [S5:1–264].
