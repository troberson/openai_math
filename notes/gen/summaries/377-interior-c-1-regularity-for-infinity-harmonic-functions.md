[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 377](../index/partial-differential-equations/377-interior-c-1-regularity-for-infinity-harmonic-functions.md)

# 377 — Interior $C^{1,\alpha}$ regularity for infinity-harmonic functions

[Index page](../index/partial-differential-equations/377-interior-c-1-regularity-for-infinity-harmonic-functions.md)

## Original CONTENTS.md summary

The release's blurb [S1:9138] and the catalog abstract [S2:859] state
the family's claim: a **uniform interior** estimate for bounded
infinity-harmonic functions in every dimension at least three. For some
positive exponent depending only on the dimension, the gradient's
supremum norm and Hölder seminorm on the half unit ball are bounded by
a dimension-dependent constant times the oscillation on the unit ball.
The exponent is not explicit, and no endpoint or boundary regularity
claim is made. The manuscript's abstract 

> We prove a uniform interior $`C^{1,\alpha_d}`$ estimate for bounded
infinity-harmonic functions in every dimension $`d\ge3`$. For some
$`\alpha_d\in(0,1/3]`$ depending only on the dimension, the gradient's
supremum norm and $`\alpha_d`$-Hölder seminorm on $`B_{1/2}`$ are bounded
by a dimension-dependent constant times the oscillation on $`B_1`$.
The exponent is not explicit, and no endpoint or boundary regularity
claim is made. In particular, infinity-harmonic functions are locally
$`C^1`$ on every open subset of $`\mathbb{R}^d`$, for $`d\ge3`$. [S3:48–57]

## Undergraduate summary

The **infinity Laplace equation** is what a function satisfies when it
makes the steepest part of its slope as small as possible — it is the
equation of a "least Lipschitz" extension, the kind of surface that
spreads a given edge value with minimal peak steepness. (The
ordinary Laplace equation balances *all* directions equally; this one
only controls the direction the function is already changing fastest
in, which makes it behave more oddly.) Such a function is called
**infinity-harmonic**.

A natural question: if a solution is nice *on average*, is its slope
actually a continuous function? You can know the slope has a definite
value at every point, and separately know it varies, without knowing
the two fit together smoothly. This family proves that, in three
dimensions and up, the slope **is** a continuous function — in fact it
varies in a controlled Hölder way, on the inside of the domain. The
price is that the exact rate of smoothness ("one to the alpha power")
is not given by a formula; the argument produces *some* positive
exponent, depending only on the number of dimensions, and guarantees
nothing about the boundary [S3:48–57, S4:29–39, S1:9138].

## Graduate summary

**Main theorem (uniform interior estimate)** [S3:48–57, S4:29–39,
S1:9138].
For every integer $`d\ge 3`$ there are constants
$`\alpha_d\in(0,1/3]`$ and $`C_d<\infty`$ such that every bounded
infinity-harmonic function $`u\in C(B_1)`$ (with
$`B_1\subset\mathbb R^d`$) belongs to
$`C^{1,\alpha_d}(B_{1/2})`$ and satisfies
$`\|\nabla u\|_{L^\infty(B_{1/2})} + [\nabla u]_{C^{0,\alpha_d}(B_{1/2})}
\le C_d\,\mathrm{osc}_{B_1}u`$ 

> **theorem**
For every integer $`d\ge3`$ there are constants $`\alpha_d\in(0,1/3]`$ and
$`C_d<\infty`$ such that every bounded infinity-harmonic function
$`u\in C(B_1)`$, where $`B_1\subset\mathbb{R}^d`$, belongs to
$`C^{1,\alpha_d}(B_{1/2})`$ and satisfies
$$\|\nabla u\|_{L^\infty(B_{1/2})}
       +[\nabla u]_{C^{0,\alpha_d}(B_{1/2})}
       \le C_d\mathrm{osc}_{B_1}u.$$ [S4:29–39]

The exponent is not explicit and sits at most at $`1/3`$ — Aronsson's
example, whose gradient oscillates like $`|h|^{1/3}`$ in the gradient
direction, rules out any exponent greater than one third in every
dimension at least two [S4:104–113].

**Interior $`C^1`$ corollary** [S4:44–48].
On any nonempty connected open set, every infinity-harmonic function
belongs to $`C^1_{\mathrm{loc}}`$: continuity bounds the function on a
closed ball, the rescaled function is infinity-harmonic on the unit
ball, and the main theorem applies [S4:50–55].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace. The ledger row `fam=377` records tier T0 with
`paps=1`, `paps_form=0`, `chal=0`, `mainres=0`, `scope_note=0`,
`verification=0`, and `trace` empty [S1, S2]. The manuscript ships its
LaTeX under `build/manuscript/` and a typeset PDF at its root; the
release ships nothing for this family beyond the manuscript. "Proves"
in the abstract is the release's claim, and everything above is read
from that LaTeX.

## History of the conjecture

The **infinity Laplace equation** arises from the calculus of
absolute minimizers: a function that minimizes the largest local
Lipschitz constant in every subregion. Aronsson identified the
equation for smooth such minimizers and later supplied the canonical
example that bounds the best possible exponent. Jensen established the
viscosity characterization and uniqueness of the Dirichlet problem;
Crandall, Evans, and Gariepy developed the equivalent
comparison-with-cones formulation and the associated local slope
estimates [S4:78–90].

The **first-order regularity** theory then separates two questions.
Crandall and Evans proved that infinitesimal blow-ups at a fixed point
are affine; Savin proved continuity of the gradient in the plane, and
Evans and Savin obtained planar interior Hölder estimates for some
positive universal exponent. Evans and Smart established
differentiability at every point in every dimension. A significant
higher-dimensional special class — infinity-harmonic potentials in
convex rings — was treated by Peng, Zhang, and Zhou, who proved
interior $`C^1`$ regularity and nonvanishing of the gradient
[S4:91–103].

Recent work has pressed the planar endpoint: Brustad's 2026 preprint
proves local one-third Hölder continuity of the gradient under the
extra assumptions that it never vanishes and has a Lipschitz inverse,
and Xu's 2026 preprint states the unrestricted planar $`C^{1,1/3}`$
theorem [S4:104–113]. The theorem proved here concerns **uniform
interior estimates for arbitrary solutions in dimensions at least
three** — not a special class, and not the plane [S4:110–113].

The **novel contribution** is the uniform interior Hölder regularity in
dimensions three and up with a positive, dimension-dependent exponent
at most one third, obtained non-explicitly by a compactness argument:
failure of a uniform power rate for affine approximation is reduced to
an entire nonaffine solution of a limiting equation, and a Liouville
theorem then forces that limit to be affine [S4:117–232, S4:29–39].

**Prior (my training data, not this repo).** The regularity of
solutions to the infinity Laplace equation was an active program in
fully nonlinear PDE. Differentiability of the gradient (Evans–Smart)
and planar Hölder regularity (Evans–Savin, Savin) were the established
results as of my training cutoff, with the higher-dimensional
interior Hölder estimate for general bounded solutions — and the
non-explicitness of the exponent — sitting at the frontier. I cannot
verify the compactness, envelope, and Liouville arguments
independently from training alone.

## Consequences

- **Uniform interior Hölder regularity** [S3:48–57, S4:29–39, S1:9138]:
  for every dimension at least three, a positive exponent
  (dimension-dependent, at most one third) and a dimension-dependent
  constant bound the gradient's supremum norm and Hölder seminorm on
  the half unit ball by the oscillation on the unit ball.
- **Local $`C^1`$ in every open set** [S4:44–55]: infinity-harmonic
  functions are locally $`C^1`$ on every nonempty connected open set in
  dimensions at least three.
- **The exponent is not explicit and is sharp at one third**
  [S4:104–113, S4:29–39]: Aronsson's example rules out any exponent
  greater than one third, and the compactness argument does not
  identify the endpoint value.
- **No endpoint or boundary claim** [S3:55–57, S1:9138]: the result is
  interior; no boundary, endpoint, or explicit-exponent statement is
  made.
- **The result is T0, a manuscript without Lean surface** [S1, S2]:
  no scope note, comparator challenge, `main_results` entry, OAI tree,
  verification bundle, or reasoning trace — nothing about its
  theorems is machine-checked.

## Section skeleton

One manuscript, a new root shape: `build/manuscript/main.tex` (71
lines), not the usual `build/main.tex`. The root declares the theorem
environments and macros inline [S3:21–38], the title at [S3:40], the
date at [S3:43], the abstract at [S3:48–57], and 8 `input` section
files [S3:61–68] plus a bibliography [S3:69]: `01-introduction`,
`02-flatness`, `03-reduction`, `04-limiting-tools`,
`05-envelope-contact`, `06-discrete-propagation`,
`07-contact-localization`, `08-rigidity`. The manuscript's abstract is
in the root, so the PDF link at the directory root [S2:859] is the
typeset document. **No verification bundles** (T0) [S1, S2].

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger row `fam=377` reads `tier=T0`, `paps=1`, `paps_form=0`,
`chal=0`, `mainres=0`, `scope_note=0`, `scope_chars=0`,
`verification=0`, `inputs=0`, `covmd=0`, `trace=` (empty). The shape
flags are `shapes=bound|uniform`, `resolves_named=0`,
`counterex_broad=0`, `companions=` (empty) — a **bound**-type result
(uniform interior regularity bound) with a **uniform** character (the
constant and exponent depend only on the dimension), resolving no named
conjecture and carrying no counterexample. The family ships one LaTeX
manuscript — a root `build/manuscript/main.tex` (71 lines), 8 `.tex`
section files, and a thebibliography — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:9138] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 377 at [S2:859], single manuscript |
| S3 | [`preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/build/manuscript/main.tex`](../../../preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/build/manuscript/main.tex) | 71 | `\documentclass` root — 71 lines, title [S3:40], date [S3:43], abstract [S3:48–57], 8 `input` section files [S3:61–68], bibliography [S3:69] |
| S4 | [`preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/build/manuscript/sections/01-introduction.tex`](../../../preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/build/manuscript/sections/01-introduction.tex) | 240 | introduction — the infinity Laplacian, the main theorem [S4:29–39], the interior $C^1$ corollary [S4:44–48], context and methods [S4:71–115], proof strategy [S4:117–232] |
