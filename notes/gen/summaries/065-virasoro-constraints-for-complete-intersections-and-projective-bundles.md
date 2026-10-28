[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 065](../index/algebraic-and-complex-geometry/065-virasoro-constraints-for-complete-intersections-and-projective-bundles.md)

# 065 — Virasoro constraints for complete intersections and projective bundles

[Index page](../index/algebraic-and-complex-geometry/065-virasoro-constraints-for-complete-intersections-and-projective-bundles.md)

## Original CONTENTS.md summary

The release's blurb "**065. Virasoro constraints for complete intersections and projective-bundle towers.** Proves the full ordinary unreduced descendant Virasoro conjecture for smooth complete intersections in complex projective space, in every genus and curve class with arbitrary cohomology insertions. The constraints also pass from any smooth projective complex base satisfying them to the projectivization of every algebraic vector bundle of rank at least two, and hence to projective-bundle towers. [S1:1629]" The family ships two
manuscripts, one proving the constraints for complete
intersections [S3:93–97] and one proving they pass through
projectivization [S11:9–15]. The complete-intersections abstract
 reads: "We prove the Virasoro conjecture for the ordinary descendant
Gromov–Witten theory of smooth complete intersections in projective space,
in every genus and curve class and with arbitrary cohomology insertions.
This includes primitive and odd cohomology classes, with no semisimplicity
assumption. [S3:93–97]"

## Undergraduate summary

The Virasoro conjecture organizes the descendant Gromov–Witten
invariants of a smooth projective variety into a system of
differential equations for a single generating function. For a
Fano target the conjecture is expected to hold in every genus;
the complete-intersections manuscript proves it in full. The
theorem 

> **Theorem 1.1**
Let $X\subset\mathbb P^N_\mathbb C$ be a smooth complete intersection. Its ordinary, unreduced total descendant potential satisfies the Virasoro constraints in every genus and curve class, with arbitrary insertions from $H^*(X;\mathbb C)$. [S4:15–17]

That resolves the Virasoro conjecture positively for
projective-space complete intersections, including primitive and
odd insertions, with no semisimplicity hypothesis [S4:19].
"Thus resolves the Virasoro conjecture positively for projective-space complete intersections. Primitive and odd insertions are included, with no semisimplicity hypothesis. [S4:19]"

The second manuscript proves a structural transfer: the
constraints pass from a base to the projectivization of any
algebraic vector bundle of rank at least two 

> **theorem**
Let $B$ be a smooth connected projective variety over $\mathbb C$, and
let $E$ be an algebraic vector bundle of rank $r\geq2$ on $B$.
Let $X=\mathbb P_B(E)$ parametrize one-dimensional subspaces of
the fibers of $E$. Then
$$\mathsf V(B)\ \Longrightarrow\ \mathsf V(X).$$ [S12:36–45]

The bundle need not split and satisfies no positivity condition;
the base may have nonsemisimple quantum cohomology [S12:47–53].
"The bundle is arbitrary: it need not split or admit a filtration
by line bundles, and it is subject to no positivity condition.
The base is allowed to have nonsemisimple quantum cohomology
and arbitrary Hodge types. In particular the assertion applies
successively to towers of projective bundles once the constraints
hold on the initial base. The conclusion concerns the ordinary
theory of each total space. [S12:47–53]"

## Graduate summary

**Two-stage degeneration.** The complete-intersections proof
factors one defining equation and resolves the resulting family,
giving a degeneration $X\rightsquigarrow U\cup_D\widetilde M$
where $U$ and $M$ have smaller defining degree and the seam $D$
and blowup center $S$ have smaller dimension . "The reduction has two stages. Factoring one defining equation and resolving
the resulting family gives a degeneration
$$X\rightsquigarrow U\cup_D\widetilde M,
 \qquad \widetilde M=\mathrm{Bl}_S M.$$
Here $U$ and $M$ are complete intersections of smaller defining degree,
while the seam $D$ and blowup center $S$ have smaller dimension. We first prove the constraints for $\widetilde M$ from those for $M$ and projective-bundle towers over $S$. [S4:32–38]"
The constraints are then proved for $\widetilde M$ from those
for $M$ and the projective-bundle towers over $S$, and for $X$
from those for $U$, $\widetilde M$, and a ruled bundle over $D$.

**Three transport constructions.** The transport rests on
contractions on the first page of the weight spectral sequence
(using Steenbrink's limiting Hodge structures and Fujisawa's
ordered model), relative caps that reproduce the contact pairing
at a seam, and a positivity detector: pairing a Virasoro error
tensor with its conjugate gives its squared $H^p$ norm, and
Hodge–Riemann positivity forces it to vanish [S4:40–52],
[S6], [S7], [S9].

**Projectivization transfer.** The transfer theorem
$\mathsf V(B)\Rightarrow\mathsf V(X)$ for $X=\mathbb P_B(E)$ is stated over an
arbitrary base and bundle [S12:36–45]. The proof builds a master
space over the projective bundle [S13] and continues the
constraints from each level [S14], so the result applies
successively to towers of projective bundles.

## History of the conjecture

Witten's conjecture and Kontsevich's theorem identify the
intersection-number generating function with the distinguished
solution of the KdV hierarchy [S4:3]. Eguchi–Hori–Xiong proposed
a target-dependent Virasoro system for Fano varieties,
extended by Eguchi–Jinzenji–Xiong to odd and off-diagonal Hodge
classes, with Katz's Hodge-index grading and Getzler's
central normalization [S4:3–5]. Liu–Tian proved the decisive
$L_1$ and $L_2$ identities in genus zero [S4:21].

Getzler proved the ordinary constraints for Calabi–Yau targets
with $c_1=0$ and $H^1=0$ [S4:23]. Okounkov–Pandharipande proved
the fixed-degree relative constraints for target curves;
Givental's quantized semisimple construction with Teleman's
classification covers the semisimple geometric theories
[S4:23–25]. Guo–Zhang–Zhou proved genus-one constraints on the
ambient state space of smooth Fano complete intersections
[S4:25–27]. The present argument addresses all genera and all
insertions simultaneously [S4:27–29].

The degeneration method builds on Li's relative reconstruction
and Arg\"uz–Bousseau–Pandharipande–Zvonkine's nodal
reconstruction of complete-intersection Gromov–Witten theory by
induction on dimension and defining degrees [S4:30–31].

## Consequences

**The Virasoro conjecture for complete intersections.** The
full ordinary unreduced descendant Virasoro constraints hold for
smooth complete intersections in projective space, in every
genus and curve class, with arbitrary insertions including
primitive and odd cohomology [S4:15–17].

**Projectivization transfer.** The constraints pass from any
smooth projective base to the projectivization of every
algebraic vector bundle of rank at least two, with no
positivity or splitting condition [S12:36–45].

**Projective-bundle towers.** The transfer applies successively,
so the constraints hold on towers of projective bundles once
they hold on the initial base [S12:47–53].

## Section skeleton

**Complete-intersections manuscript** (8 `.tex` under
`build/sections/`): introduction [S4], conventions [S5],
firstpage [S6], caps [S7], sewing [S8], detection [S9],
induction [S10], evaluation.

**Projectivization manuscript** (8 `.tex` under
`build/sections/`): introduction [S12], conventions,
master-space [S13], localization, shift, spectral, fixed-block,
continuation [S14].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no
reasoning trace. Nothing about this family is machine-checked.
The ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`,
`chal 0`, `trace` empty. The two manuscripts ship 16 `.tex`
files under their `build/` trees.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 065 at line 1629. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 204. |
| S3 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/main.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/main.tex) | 111 | Complete-intersections main file: title, abstract, and section inputs. |
| S4 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/introduction.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/introduction.tex) | 65 | The main theorem, the historical context, the degeneration reduction, and the transport argument. |
| S5 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/conventions.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/conventions.tex) | 101 | The Virasoro operators, the first-Hodge grading, and the quantization conventions. |
| S6 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/firstpage.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/firstpage.tex) | 566 | The local Hodge calculation on the weight spectral sequence. |
| S7 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/caps.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/caps.tex) | 571 | The cap construction and the contact pairing at a seam. |
| S8 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/sewing.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/sewing.tex) | 572 | The switch-cancellation transport theorem. |
| S9 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/detection.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/detection.tex) | 80 | The Hodge--Riemann positivity detector for primitive tensors. |
| S10 | [`preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/induction.tex`](../../../preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/build/sections/induction.tex) | 522 | The complete-intersection induction and the curve-class argument. |
| S11 | [`preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/paper.tex`](../../../preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/paper.tex) | 27 | Projectivization main file: title, abstract, and section inputs. |
| S12 | [`preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/01-introduction.tex) | 217 | The projectivization transfer theorem and the conventions. |
| S13 | [`preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/03-master-space.tex`](../../../preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/03-master-space.tex) | 251 | The master space over the projective bundle. |
| S14 | [`preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/08-continuation.tex`](../../../preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/build/sections/08-continuation.tex) | 370 | The continuation to projective-bundle towers. |
