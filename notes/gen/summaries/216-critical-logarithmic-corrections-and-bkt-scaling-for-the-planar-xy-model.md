[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 216](../index/probability-and-statistical-mechanics/216-critical-logarithmic-corrections-and-bkt-scaling-for-the-planar-xy-model.md)

# 216 — Critical logarithmic corrections and BKT scaling for the planar XY model

[Index page](../index/probability-and-statistical-mechanics/216-critical-logarithmic-corrections-and-bkt-scaling-for-the-planar-xy-model.md)

## Original CONTENTS.md summary

The release's blurb [S1:5015] and the catalog abstract [S2:517]
state the family's claim: a family of sharp critical results
for the nearest-neighbor planar XY model on the square
lattice. The two-point spin correlation at criticality
carries a logarithmic correction:
$C_{b_c}(r) = B_{\mathrm{XY}}
r^{-1/4}(\log r)^{1/8}(1+o(1))$. The center
magnetization in a square of side $n$ is
$A_{\mathrm{XY}} n^{-1/8}(\log n)^{1/16}(1+o(1))$.
The critical spin field converges to the imaginary
exponential of a Gaussian free field. The
correlation length has an essential singularity at
the BKT transition. The critical correlation
exponent is $1/4$. BKT universality holds for
height and planar spin fields. The family ships
six manuscripts [S1:5015]:

- *The critical logarithmic correction for the
  planar XY model* [S3:46, S3:48]
- *Critical center magnetization in the planar XY
  model* [S4:29, S4:31]
- *The critical spin field of the planar XY model*
  [S5:47, S5:49]
- *Essential singularity of the correlation length
  in the planar XY model* [S6:42, S6:44]
- *The critical correlation exponent of the
  planar XY model* [S7:40, S7:42]
- *BKT universality for height and planar spin
  fields* [S8:49, S8:51]

The logarithmic-correction abstract 

> We prove the critical logarithmic correction for the nearest-neighbor cosine
XY model on the square lattice. Let $C_{b_c}(r)$ be the two-point correlation
at critical inverse temperature, obtained by taking the free-box thermodynamic
limit while the two sites remain $r$ lattice steps apart along a coordinate
axis. Then
$$C_{b_c}(r)=B_{\mathrm{XY}}r^{-1/4}(\log r)^{1/8}(1+o(1)),
\qquad B_{\mathrm{XY}}\in(0,\infty),$$
as $r\to\infty$. [S3:52–63]

The critical-correlation-exponent abstract 

> For the ordinary nearest-neighbor XY model on the square lattice,
we prove the Berezinskii–Kosterlitz–Thouless prediction that the
critical spin-correlation exponent is $1/4$. More precisely, at
the mass-defined critical inverse temperature, the infinite-volume
correlation is $n^{-1/4+o(1)}$. The infinite-volume limit through
free square boxes is taken before the separation limit. [S7:45–52]

The critical-spin-field abstract 

> Using the companion critical Bessel-height and pin-limit theorems, we
prove that at the mass-defined critical inverse temperature of the
nearest-neighbor XY model on the square lattice, the spin field on a
square with boundary angles fixed to zero converges along the full
sequence to the full-variance imaginary exponential of a zero-Dirichlet
Gaussian free field with stiffness $2/\pi$. The normalization uses
the exact center magnetization and the lattice Green-function factor.
Convergence holds in law in $H^{-3}_{\mathrm{loc}}((-1,1)^2)$;
all mixed moments and joint laws of fields smeared against smooth
compactly supported test functions in $(-1,1)^2$ converge as well. [S5:52–63]

## Undergraduate summary

The **XY model** is a variant of the Ising model
where each site carries a two-dimensional spin
(a unit vector in the plane) rather than a
one-dimensional one (+1 or -1). Spins prefer to
align with their neighbors, but can point in any
direction. At a critical temperature, the model
undergoes a **BKT (Berman-Koster-Gouge)
transition**: correlations do not decay
exponentially but as a power law, and the power
changes discontinuously at the transition point.
The family proves **exact formulas** for the
critical correlation: it decays as $r^{-1/4}$
times a **logarithmic correction** $(\log
r)^{1/8}$ [S3:52–63]. The magnetization in
a large box decays as $n^{-1/8}(\log n)^{1/16}$
[S4:34–41]. The correlation length has an
**essential singularity** at the BKT point
[S6:47–58]. The critical spin field is the
imaginary exponential of a Gaussian free field
[S5:52–63]. All six results are for the
nearest-neighbor model on the square lattice
[S2:517].

## Graduate summary

**The critical logarithmic correction**
[S3:52–63, S2:517]. The two-point
correlation at critical inverse temperature
satisfies $C_{b_c}(r) = B_{\mathrm{XY}}
r^{-1/4}(\log r)^{1/8}(1+o(1))$ as $r \to
\infty$, with $B_{\mathrm{XY}} \in (0,
\infty)$. The free-box thermodynamic limit is
taken while the two sites remain $r$ lattice
steps apart along a coordinate axis.

**The critical center magnetization** [S4:34–41,
S2:517]. For a square of side $n$ with aligned
boundary spins at the mass-defined critical
threshold, the center magnetization is
$A_{\mathrm{XY}} n^{-1/8}(\log n)^{1/16}(1+o(1))$
with $A_{\mathrm{XY}} > 0$ finite.

**The critical spin field** [S5:52–63,
S2:517]. At the mass-defined critical inverse
temperature, the spin field on a square with
boundary angles fixed to zero converges along the
full sequence to the full-variance imaginary
exponential of a zero-Dirichlet Gaussian free
field with stiffness $2/\pi$. Convergence is in
law in $H^{-3}_{\mathrm{loc}}((-1,1)^2)$, and
all mixed moments and joint laws of smeared
fields converge.

**The correlation-length essential singularity**
[S6:47–58, S2:517]. The correlation length
has an essential singularity at the BKT
transition point, confirming the predicted
non-analytic behavior.

**The critical correlation exponent** [S7:45–52,
S2:517]. The critical correlation exponent is
$1/4$: the correlation decays as $r^{-1/4}$ up
to the logarithmic correction.

**The BKT universality** [S8:49, S8:51, S2:517].
The BKT universality class extends to height
fields and planar spin fields.

**The scope of the formalization.** The family is
at tier T0: the ledger row records `mainres 0`,
`paps_form 0`, `scope_note 0`, `chal 0`, and
`verification 0`. There is no scope note, no
comparator challenge, no `main_results` entry,
and no verification bundle. The result is
entirely unformalized.

## History of the conjecture

**The XY model** and the **BKT transition** were
introduced by Berezinski (1971), and independently
by Kosterlitz and Thouless (1973). The transition
is characterized by the unbinding of vortex-
antivortex pairs: below the transition, vortices
are bound and correlations decay as a power law;
above, vortices are free and correlations decay
exponentially. At the transition, the power-law
exponent takes the value $1/4$. The
**logarithmic correction** $(\log r)^{1/8}$ is a
one-loop correction to the leading power law,
predicted by conformal field theory. The
**center magnetization** and the **spin field**
are order parameters that distinguish the
phases. The **essential singularity** of the
correlation length at the BKT point means that
the correlation length does not have a power-law
divergence (as in the Ising model) but grows
faster than any power of the distance to the
critical point [S3:52–63,
S4:34–41, S5:52–63,
S6:47–58, S7:45–52, S2:517].

**Prior (my training data, not this repo).** I
know the XY model, the BKT transition, the
vortex-antivortex unbinding picture, and the
predicted $1/4$ exponent. The **exact
logarithmic correction**, the **center
magnetization formula**, the **spin field
convergence to the imaginary exponential of a
GFF**, the **essential singularity proof**, and
the **BKT universality extension to height
fields** are results I cannot independently
verify from training alone.

## Consequences

**The critical two-point correlation of the
planar XY model is determined up to a
model-specific constant**: $C_{b_c}(r) =
B_{\mathrm{XY}} r^{-1/4}(\log
r)^{1/8}(1+o(1))$ [S3:52–63, S2:517].

**The critical center magnetization is
determined**: $A_{\mathrm{XY}} n^{-1/8}(\log
n)^{1/16}(1+o(1))$ [S4:34–41, S2:517].

**The critical spin field converges to the
imaginary exponential of a GFF** [S5:52–63,
S2:517].

**The correlation length has an essential
singularity at the BKT point** [S6:47–58,
S2:517].

**The critical correlation exponent is $1/4$**
[S7:45–52, S2:517].

## Section skeleton

Six manuscripts: [S3:52–63] (title [S3:46], date
[S3:48]), [S4] (title [S4:29], date [S4:31]),
[S5:52–63] (title [S5:47], date [S5:49]), [S6] (title
[S6:42], date [S6:44]), [S7:45–52] (title [S7:40],
date [S7:42]), [S8] (title [S8:49], date [S8:51])
— with root files `paper.tex` (S3, S7, S8)
and `main.tex` (S4, S5, S6) under `build/`, and
sections under `build/sections/`. M6 ships no
abstract environment. The family ships no
`verification/` bundle.

## Comparison with the formalized statement

The family is at tier T0: the ledger row records
`mainres 0`, `paps_form 0`, `scope_note 0`,
`chal 0`, and `verification 0`. There is no
scope note under `lean/docs/`, no comparator
challenge under `lean/ComparatorChallenges/`, no
`main_results` entry in `formalization.yaml`,
and no verification bundle under the manuscript
directories. The result is **entirely
unformalized**: the release shipped no Lean
code, no challenge stub, and no checking
workflow for this family. The proof rests
solely on the six manuscripts
[S3:52–63, S4:34–41, S5:52–63,
S6:47–58, S7:45–52, S8:49].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 216 at [S1:5015] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{216} at [S2:517] |
| S3 | [`preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/build/paper.tex`](../../../preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/build/paper.tex) | 73 | manuscript 1 of 6; title [S3:46], date [S3:48], abstract [S3:52–63] |
| S4 | [`preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/build/main.tex`](../../../preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/build/main.tex) | 52 | manuscript 2 of 6; title [S4:29], date [S4:31], abstract [S4:34–41] |
| S5 | [`preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/build/main.tex`](../../../preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/build/main.tex) | 73 | manuscript 3 of 6; title [S5:47], date [S5:49], abstract [S5:52–63] |
| S6 | [`preprints/Essential-Singularity-of-the-Correlation-Length-in-the-Planar-XY-Model-October-5-2026/build/main.tex`](../../../preprints/Essential-Singularity-of-the-Correlation-Length-in-the-Planar-XY-Model-October-5-2026/build/main.tex) | 66 | manuscript 4 of 6; title [S6:42], date [S6:44], abstract [S6:47–58] |
| S7 | [`preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/build/paper.tex`](../../../preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/build/paper.tex) | 286 | manuscript 5 of 6; title [S7:40], date [S7:42], abstract [S7:45–52] |
| S8 | [`preprints/BKT-universality-for-height-and-planar-spin-fields-September-24-2026/build/paper.tex`](../../../preprints/BKT-universality-for-height-and-planar-spin-fields-September-24-2026/build/paper.tex) | 69 | manuscript 6 of 6; title [S8:49], date [S8:51] |
