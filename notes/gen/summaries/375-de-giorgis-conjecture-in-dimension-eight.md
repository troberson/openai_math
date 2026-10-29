[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 375](../index/partial-differential-equations/375-de-giorgis-conjecture-in-dimension-eight.md)

# 375 — De Giorgi's conjecture in dimension eight

[Index page](../index/partial-differential-equations/375-de-giorgis-conjecture-in-dimension-eight.md)

## Original CONTENTS.md summary

The release's blurb [S1:9025] and the catalog abstract [S2:852] state
the family's claim: De Giorgi's conjecture is proved at its sharp
dimension-eight endpoint. Every entire $`C^2`$ solution of
$`\Delta u=u^3-u`$ in $`\mathbb R^8`$ that is strictly increasing in one
direction depends on only one linear coordinate. A stronger companion
theorem classifies all stable entire solutions in $`\mathbb R^7`$ as constant
wells or planar transitions, without an energy-growth assumption.
The manuscript's abstract "We resolve De Giorgi's conjecture positively in dimension eight:
every entire $`C^2`$ solution $`u:\mathbb R^8\to(-1,1)`$ of
$`\Delta u=u^3-u`$ with an everywhere positive directional derivative
is a planar heteroclinic. We prove that every stable solution
$`v:\mathbb R^7\to[-1,1]`$ of this equation is a constant well or a planar heteroclinic,
without an energy-growth assumption. [S3:112–119]"

## Undergraduate summary

The Allen–Cahn equation $`\Delta u = u^3 - u`$ models phase
transitions: $`u`$ interpolates between the two wells $`\pm1`$ across
a thin interface. De Giorgi (1979) conjectured that in dimensions
up to eight, every bounded solution that is monotone in some
direction is a one-dimensional planar transition — its level sets
are parallel hyperplanes. The manuscript proves this at the
critical endpoint dimension eight 

> **Theorem 1.1**
Let $`u\in C^2(\mathbb R^8,(-1,1))`$ satisfy
$$\Delta u=u^3-u,\qquad \partial_8u>0\quad\text{in }\mathbb R^8.$$
Then there are $`e\in\mathbb S^7`$ with $`e_8>0`$ and $`c\in\mathbb R`$ such that
$$u(x)=\tanh\!\left(\frac{e\cdot x-c}{\sqrt2}\right)
 \qquad\text{for every }x\in\mathbb R^8.$$ [S4:59–70]

No energy growth, minimization, or well-limit assumption is required
[S4:72–73].

## Graduate summary

**The stable classification in dimension seven.** The analytic core
is the stable rigidity theorem: every stable solution
$`v:\mathbb R^7\to[-1,1]`$ of $`\Delta v=v^3-v`$ is a constant well or a
planar heteroclinic, with no energy-growth hypothesis [S4:103–112].
This endpoint is sharp — Pacard and Wei constructed stable
nonplanar solutions in dimension eight [S4:114–115].

**The geometric deduction.** A monotone solution's directional
limits are stable seven-dimensional solutions. The stable
classification gives planar transitions at both ends. Energy
monotonicity makes the limiting boundary a cone; in dimension eight
the minimizing-boundary regularity theory allows only a vertex
singularity, and the directed-cone argument forces a hyperplane
[S4:130–160].

**Removing the density bound.** The finite-density step proves
stable rigidity in dimensions $`4\le n\le7`$ under a bounded-energy
density hypothesis [S4:197–207]. The remaining work removes this
hypothesis using radial monotonicity, interface geometry, and
growth estimates in the interface and reach sections
[S4:230–249].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace.

## History of the conjecture

Ghoussoub–Gui (dimension two), Ambrosio–Cabré (dimension three),
and Savin (through dimension eight, under a well-limit assumption)
proved the conjecture in lower dimensions [S4:33–44]. Del Pino,
Kowalczyk, and Wei constructed nonplanar monotone solutions in
dimension $`\ge9`$ near dilations of nonaffine minimal graphs
[S4:45–49]. The dimension-eight endpoint is the sharp boundary:
in dimension nine, nonaffine entire minimal graphs exist, and
the corresponding Allen–Cahn solutions are nonplanar.

## Consequences

**De Giorgi's conjecture is resolved at dimension eight.** Every
entire $`C^2`$ solution of $`\Delta u=u^3-u`$ in $`\mathbb R^8`$ with
$`\partial_8 u>0`$ is a planar heteroclinic [S4:59–70].

**Stable rigidity in dimension seven without density bound.**
Every stable solution in $`\mathbb R^7`$ is a constant well or a planar
transition [S4:103–112].

**The dimension is sharp.** Nonplanar monotone solutions exist
in dimension nine [S4:45–49].

## Section skeleton

**Manuscript** [S3:112–119], 11 sections under `build/sections/`:
introduction [S4:59–70], classical estimates, monotone, strategy, diffuse,
finite-density, reach, interface, growth, radial, and
dimension-nine appendix. Its root is `build/main.tex` with a
`refs.bib` bibliography.

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, 11 `.tex` files under
`build/sections/`, and a `refs.bib` bibliography — and no
non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 375 at line 9025. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 852. |
| S3 | [`preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/main.tex`](../../../preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/main.tex) | 147 | Manuscript main file: title and abstract. |
| S4 | [`preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex`](../../../preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex) | 249 | Introduction: the Allen–Cahn equation, the monotone and stable theorems, and the proof strategy. |
