[Notes](../../README.md) / [Summaries](../README.md) / [Dynamical systems and ergodic theory](../../index/disciplines/dynamical-systems-and-ergodic-theory.md) / [Family 147](../../index/dynamical-systems-and-ergodic-theory/147-near-boundary-birkhoff-conjecture.md)

# 147 — The near-boundary Birkhoff conjecture

[Index page](../../index/dynamical-systems-and-ergodic-theory/147-near-boundary-birkhoff-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:3516]:

> Resolves the near-boundary Birkhoff conjecture for smooth strictly convex planar billiards of positive curvature. Such a billiard is an ellipse whenever a full grazing annulus is continuously foliated by individually invariant essential curves. A continuous physical collar of smooth closed convex caustics also suffices.

The overview's paraphrase [S2:373] says the same: "Resolves the near-boundary Birkhoff conjecture for smooth strictly convex planar billiards of positive curvature. Such a billiard is an ellipse whenever a full grazing annulus is continuously foliated by individually invariant essential curves. A continuous physical collar of smooth closed convex caustics also suffices." The result is split across two manuscripts: the first [S6:42–50] supplies the dynamical and geometric steps that turn a merely continuous phase foliation into a smooth physical collar, and the companion [S10:4–8] supplies the analytic inputs and the final rigidity theorem.

## Undergraduate summary

A billiard table is a convex region; a ball travels in straight lines inside
it and reflects off the boundary. The Birkhoff conjecture asks: if the
motion is integrable — the trajectories organize into a family of closed
curves filling the region — must the table be an ellipse?

The manuscript answers a local version. It asks only that the integrable
structure exist near the boundary. The region is a bounded, strictly convex
open set whose boundary is a smooth simple closed curve with positive
curvature, and the assumption is a foliation of a full grazing annulus: a
band of trajectories just inside the boundary, swept out by closed curves
that the billiard map leaves invariant.

The first manuscript's theorem is the rigidity statement: "Suppose a"
billiard-invariant open annulus contains a grazing band, and there is a
homeomorphism "whose leaves are essential simple closed curves, each
individually invariant under" the billiard map. Then the table is an
ellipse. [S6:17–31] Circles are included. [S10:38]

The point that makes the local version hard is the regularity of the
foliation. "Only continuity of the leaves and of their transverse
dependence is assumed. The foliation need not extend to the rest of the
phase cylinder, and the width" of the annulus "may be arbitrarily small.
The main issue is that a continuous essential phase curve need not
initially be given as the tangent lines of a smooth convex caustic."
[S6:36–40]

The companion manuscript states the same result in its own words: "The
Birkhoff conjecture asks whether an integrable planar convex billiard must
be an ellipse. We prove the version in which integrability is assumed only
in a neighborhood of the boundary, with continuous dependence of the
caustics. The individual leaves and the billiard boundary are smooth; no
differentiability of the foliation across its leaves is required."
[S10:4–8]

The scope is stated as a boundary result. "The hypothesis makes no
assertion about the billiard dynamics farther inside the domain."
[S10:45–46]

## Graduate summary

The two-manuscript structure. The first manuscript proves the regularity
reduction: a continuous phase foliation of a grazing annulus produces a
smooth physical caustic collar. The companion proves that a smooth physical
caustic collar forces the table to be an ellipse. The first manuscript
names the division of labor: the companion "supplies three analytic inputs
and the final physical-collar rigidity theorem." The first manuscript
establishes "the additional dynamical and geometric steps needed to apply
them to a merely continuous phase foliation." It constructs "the physical
collar before invoking the companion's ellipse theorem." [S6:43–50]

The collar. A continuous physical caustic collar is a relatively open set
containing the boundary, together with a homeomorphism from the cylinder
whose zero leaf is the boundary and whose positive leaves are smooth convex
caustics. [S6:109–116] The collar contains every intermediate leaf; a
Cantor family of invariant curves, even one accumulating at the boundary,
does not satisfy the assumption. [S10:43–44]

The mechanism, in three parts. First, rational caustics force analytic
regularity: nesting and area recurrence imply that every sufficiently small
rational rotation occurs on a curve entirely made of periodic orbits.
[S10:103–106] Second, finite reflected chains determine their intermediate
lines algebraically from endpoint jets, and this local determination
controls monodromy: "a finite first continuation wall cannot have even one
local joint meromorphic patch." [S10:115–116] Third, the complexified
boundary is studied through its meromorphic normal and two analytic
derivative fields; growth estimates exclude most possible behaviors at the
edge of its strip, leaving a critical finite-width case, where moment
bounds and paths through regions where the fields are large limit the total
angular change. [S10:158–163]

The probability step. For one fixed odd periodic chain, matrix identities
transfer that control to Brownian paths stopped before the shape boundary.
A horizontal row is found on which the first field is robustly small or
large outside a set of vanishing relative measure, and the sign test on this
row keeps the last moving impact away from the boundary, contradicting the
assumed first wall. [S10:164–168]

The regularity gap. The analytic inversion needs a complex continuation,
and the hypothesis supplies only smooth geometry and a continuous foliation.
"we must obtain analytic regularity from the given smooth geometry and
merely continuous foliation. The proof below does so before using complex
continuation." [S10:91–93]

Graphness. Birkhoff's invariant-curve theorem for twist maps explains why
graphs are the natural intermediate objects; here the initial leaves are
only continuous essential curves, and the entire annulus is foliated, so
graphness is proved directly from both billiard twist signs and finite-area
recurrence. [S6:83–87] The full collar then supplies a wholly periodic
graph at every sufficiently small rational rotation, and the stationary
actions of those graphs yield high-frequency equations for the boundary.
[S6:87–90]

The scope of the method. The analytic inversion uses the companion's
arbitrary-input estimates without a perturbative assumption. [S6:93–94] The
passage from continuous phase leaves to the smooth physical caustic
hypothesis requires neither a symmetry assumption nor closeness to a circle
or ellipse. [S6:99–102]

## History of the conjecture

Birkhoff developed the convex billiard as a dynamical model, and Poritsky's
early printed formulation studied compatible string constructions under
hypotheses stronger than a foliation alone. [S6:55–58] Lazutkin's theorem
guarantees a Cantor family of near-boundary invariant curves for
sufficiently smooth positively curved tables, rather than a full foliation;
Marvizi and Melrose constructed a grazing first integral modulo a flat
error, not an exact invariant foliation; Mather excluded grazing caustics
when boundary curvature vanishes, so positive curvature is substantive.
[S6:59–66]

Stronger or different integrability hypotheses give complementary rigidity
results. Bialy proved that foliation of the entire phase cylinder by
noncontractible invariant circles forces a circle. Avila, De Simoi, and
Kaloshin proved local rigidity near small-eccentricity ellipses, and
Kaloshin and Sorrentino treated perturbations of ellipses of arbitrary
eccentricity. Bialy and Mironov allowed a continuous phase foliation under
central symmetry when the foliated region reaches the invariant four-periodic
curve. Koval's local strong result treats caustics at all rational rotations
in an arbitrarily small interval above zero, under closeness to almost every
ellipse and high-regularity bounds. The manuscript states what these share:
they "impose geometric restrictions or require invariant curves extending
beyond an arbitrarily thin grazing annulus." [S6:68–81]

The bibliography of the first manuscript carries the Lazutkin, Marvizi–Melrose,
Mather, Bialy, Avila–De Simoi–Kaloshin, Kaloshin–Sorrentino, Bialy–Mironov,
and Koval entries, and the companion's bibliography carries the Birkhoff,
Poritsky, Lazutkin, and the same later entries. [S7:2–184] [S11:2–287]

Prior (my training data, not the manuscript's record): the Birkhoff
conjecture in its full form was open, and the local and perturbative
versions had substantial progress — Bialy's global circle theorem, the
small-eccentricity and perturbative ellipse results, and the continuous
foliation results under symmetry. The near-boundary version with a merely
continuous grazing foliation, with no symmetry and no closeness hypothesis,
is the part I would have recorded as open. The manuscript's own citations
are the record; this paragraph is my prior on the conjecture's standing, and
the manuscript does not state it.

## Consequences

The result resolves the near-boundary Birkhoff conjecture positively in the
smooth positively curved class, in the continuous phase-foliation
formulation. [S6:96–98] The consequence is that the integrable structure
near the boundary is enough: the table is an ellipse.

The method separates two things that are usually combined in this problem:
the passage from a continuous foliation to a smooth physical collar, which
is dynamical and geometric, and the analytic inversion that turns the
collar into an ellipse, which is complex-analytic. The first manuscript
proves the passage; the companion proves the inversion. The manuscript
states that the analytic inversion uses the companion's arbitrary-input
estimates without a perturbative assumption, so the result is not a
perturbative one.

Open directions the manuscripts leave: the hypothesis makes no assertion
about the dynamics farther inside the domain, so the full Birkhoff
conjecture is not resolved; the positive-curvature assumption is
substantive, because Mather excluded grazing caustics when boundary
curvature vanishes; the collar must contain every intermediate leaf, so a
Cantor family accumulating at the boundary is not covered; and the two
aspects the companion names as separable — the finite-chain algebraic
determination principle with its monodromy consequence, and the combination
of an individual-center quiet-profile obstruction with moment bounds — are
stated as method ancestry, not as formal inputs to the arguments proved.

## Comparison with the formalized statement

Nothing. The ledger records tier T0 for this family, with no scope note, no
comparator challenge, no `main_results` entry, no reasoning trace, and no
verification bundle. The two manuscripts' LaTeX is the only source, and the
release's `formalized` flag for both is 0. The repo readme's reasoning-summary
table, "We are also releasing abridged summaries of the model's reasoning,
covering the following results:" [S3:24], lists ten families and 147 is not
among them. The claim is a rigidity statement for a planar billiard; nothing
in the Lean library reaches it, and no certificate ships with it.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 147 at line 3516. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 373. |
| S3 | [`README.md`](../../../README.md) | 51 | The repo readme, which attributes no reasoning trace to this family. |
| S4 | [`preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/README.md`](../../../preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/README.md) | 18 | Citation-only manuscript readme: the title, the date, the BibTeX block, no provenance. |
| S5 | [`preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/main.tex`](../../../preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/main.tex) | 63 | The main file: the abstract and the section order. |
| S6 | [`preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/sections/introduction.tex`](../../../preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/sections/introduction.tex) | 205 | The phase-foliation theorem, the regularity reduction, the context, the prior results, and the graphness step. |
| S7 | [`preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/references.bib`](../../../preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/references.bib) | 184 | The bibliography: Birkhoff, Poritsky, Lazutkin, Marvizi–Melrose, Mather, Bialy, ADK, Kaloshin–Sorrentino, Bialy–Mironov, Koval. |
| S8 | [`preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/README.md`](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/README.md) | 18 | Citation-only companion readme: the title, the date, the BibTeX block, no provenance. |
| S9 | [`preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/main.tex`](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/main.tex) | 92 | The companion main file: the abstract and the section order. |
| S10 | [`preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/sections/01-introduction.tex) | 193 | The collar definition, the rigidity theorem, the three-part mechanism, the regularity gap, and the separable aspects. |
| S11 | [`preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/references/references.bib`](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/build/references/references.bib) | 287 | The companion bibliography. |

## Bibliography

- Arnaud, Marie-Claude, Three results on the regularity of the curves that are invariant by an exact symplectic twist map (2009)
- Arnaud, Marie-Claude, Three results on the regularity of the curves that are invariant by an exact symplectic twist map (2009)
- Arnold, Maxim, Bialy, Misha, Nonsmooth convex caustics for Birkhoff billiards (2018)
- Avila, Artur, De Simoi, Jacopo, Kaloshin, Vadim, An integrable deformation of an ellipse of small eccentricity is an ellipse (2016)
- Avila, Artur, De Simoi, Jacopo, Kaloshin, Vadim, An integrable deformation of an ellipse of small eccentricity is an ellipse (2016)
- Bialy, Misha, Convex billiards and a theorem by {E. Hopf} (1993)
- Bialy, Misha, Mironov, Andrey E., Angular billiard and algebraic Birkhoff conjecture (2017)
- Bialy, Misha, Mironov, Andrey E., The Birkhoff–Poritsky conjecture for centrally-symmetric billiard tables (2022)
- Bialy, Misha, Convex billiards and a theorem by {E. Hopf} (1993)
- Bialy, Misha, Mironov, Andrey E., Angular billiard and algebraic Birkhoff conjecture (2017)
- Bialy, Misha, Mironov, Andrey E., The Birkhoff–Poritsky conjecture for centrally-symmetric billiard tables (2022)
- Birkhoff, George D., On the periodic motions of dynamical systems (1927)
- Birkhoff, George D., On the periodic motions of dynamical systems (1927)
- Durrett, Rick, Probability: Theory and Examples (2019)
- Fierobe, Corentin, Sorrentino, Alfonso, On the existence of periodic invariant curves for analytic families of twist maps and billiards (2026)
- Fierobe, Corentin, Sorrentino, Alfonso, On the existence of periodic invariant curves for analytic families of twist maps and billiards (2026)
- Forster, Otto, Lectures on Riemann Surfaces (1981)
- Garnett, John B., Bounded Analytic Functions (2007)
- Glutsyuk, Alexey, On infinitely many foliations by caustics in strictly convex open billiards (2024)
- Glutsyuk, A. A., On complex algebraic caustics in planar and projective billiards (2026)
- Innami, Nobuhiro, Geometry of geodesics for convex billiards and circular billiards (2002)
- Kaloshin, Vadim, Sorrentino, Alfonso, On the local Birkhoff conjecture for convex billiards (2018)
- Kaloshin, Vadim, Sorrentino, Alfonso, On the local Birkhoff conjecture for convex billiards (2018)
- Kaloshin, V., Koudjinan, C. E., Zhang, Ke, Birkhoff conjecture for nearly centrally symmetric domains (2024)
- Koval, Illya, Local strong Birkhoff conjecture and local spectral uniqueness of almost every ellipse (2026)
- Koval, Illya, Local strong Birkhoff conjecture and local spectral uniqueness of almost every ellipse (2026)
- Lazutkin, V. F., The existence of caustics for a billiard problem in a convex domain (1973)
- Lazutkin, V. F., The existence of caustics for a billiard problem in a convex domain (1973)
- Marvizi, Shahla, Melrose, Richard B., Spectral invariants of convex planar regions (1982)
- Marvizi, Shahla, Melrose, Richard, Spectral invariants of convex planar regions (1982)
- Mather, John N., Glancing billiards (1982)
- Mather, John N., Glancing billiards (1982)
- McMullen, C., Advanced Complex Analysis (2017)
- OpenAI, Rigidity of Smooth Billiards with a Continuous Caustic Collar (2026)
- Pollard, David, A User's Guide to Measure Theoretic Probability (2002)
- Poritsky, Hillel, The billard ball problem on a table with a convex boundary—an illustrative dynamical problem (1950)
- Poritsky, Hillel, The billard ball problem on a table with a convex boundary—an illustrative dynamical problem (1950)
- Revuz, Daniel, Yor, Marc, Continuous Martingales and Brownian Motion (1999)
- Ram{í}rez-Ros, Rafael, Break-up of resonant invariant curves in billiards and dual billiards associated to perturbed circular tables (2006)
- H{ö}rmander, Lars, An Introduction to Complex Analysis in Several Variables (1990)
