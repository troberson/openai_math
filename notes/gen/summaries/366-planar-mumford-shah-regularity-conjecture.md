[Notes](../../README.md) / [Summaries](README.md) / [Partial differential equations](../index/disciplines/partial-differential-equations.md) / [Family 366](../index/partial-differential-equations/366-planar-mumford-shah-regularity-conjecture.md)

# 366 — The planar Mumford–Shah regularity conjecture

[Index page](../index/partial-differential-equations/366-planar-mumford-shah-regularity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:8872] and the catalog abstract [S2:832] state
the family's claim: the interior regularity conjecture for reduced
absolute planar Mumford–Shah minimizers with bounded fidelity data is
resolved. Locally, the closed discontinuity set is a $`C^{1,\alpha}`$
arc, a regular crack tip, or three arcs meeting at $`120^\circ`$; only
finitely many global connected components meet any compact interior
region. The manuscript's abstract "We prove the interior regularity assertion of the planar Mumford–Shah
conjecture for reduced absolute minimizers with bounded fidelity data.
Every interior point of the closed discontinuity set has a neighborhood
consisting of a $`C^{1,\alpha}`$ arc, an arc ending at that point, or three
such arcs meeting at $`120`$ degrees. Only finitely many global connected
components meet any relatively compact open set. [S3:26–33]"

## Undergraduate summary

The planar Mumford–Shah problem balances the smoothness of a function
against the length of a set across which it may jump. The energy is
the Dirichlet integral away from the set, plus the one-dimensional
Hausdorff measure of the set, plus a fidelity penalty. Mumford and
Shah (1989) introduced this functional as a model for image
segmentation and conjectured that, in the interior, the discontinuity
set consists of regular arcs with only free endpoints and triple
junctions. The manuscript proves this 

> **Theorem 1.1**
Let $`(u,K)`$ be a reduced absolute minimizer of
 in a bounded Lipschitz domain
$`\Omega\subset\mathbb R^2`$, with $`g\in L^\infty(\Omega)`$.
Every $`x\in K`$ has an interior neighborhood in which $`K`$ has one of the
following forms, with $`C^{1,\alpha}`$ arcs for some $`\alpha>0`$:
\beginenumerate[label=\textup{(\roman i)},nosep]
 \item a single embedded arc with $`x`$ in its interior;
 \item a single embedded arc ending at $`x`$;
 \item three embedded arcs meeting only at $`x`$, with pairwise angles
 $`120`$ degrees.
\endenumerate
Moreover, for every open $`U\Subset\Omega`$,
$$\\\#\{C\in\pi_0(K):C\cap U\ne\varnothing\}<\infty,$$
where $`\pi_0(K)`$ denotes the set of global connected components of $`K`$. [S4:46–63]

The geometric conclusion gives an endpoint integrability estimate:
$`\nabla u\in L^{4,\infty}_{\mathrm{loc}}`$ [S4:72–77].

## Graduate summary

**Reduction.** The proof passes from the stated finite-length
formulation to a locally bounded, rectifiable minimizing pair
[S4:137–142].

**Blow-up and the compact-piece exclusion.** Rescaled sets have
global generalized limits. The known classification results reduce
the problem to excluding a bounded component. A compact piece $`A`$
at positive distance from the rest is translated; the interaction
between the jump field and a harmonic potential is harmonic in the
translation parameter, and minimality forces it constant. Value
variations force the potential affine, the energy bound makes its
gradient zero, and the value-variation identity makes the jump field
zero. Removing $`A`$ saves positive length [S4:143–160].

**Completion.** The classification gives a line, half-line, or three
rays. Epsilon regularity transfers these to the original minimizer;
a finite cover proves component finiteness [S4:162–170].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace.

## History of the conjecture

Mumford–Shah (1989); De Giorgi–Ambrosio and Ambrosio (BV framework);
Bonnet (planar blow-up, global minimizer classification); David and
Ambrosio–Fusco–Pallara (regular arcs, triple junctions); Bonnet–David
(crack tip); David–Léger (line or triod for disconnecting cracks);
De Lellis–Focardi (higher integrability, 2025 monograph);
Labourie–Lemenant (2026, at most three limiting values); Deangelis
(2026, global classification via compact translations)
[S4:101–136].

## Consequences

**The interior regularity conjecture is resolved.** Every interior
point of $`K`$ has a neighborhood that is a $`C^{1,\alpha}`$ arc, an
arc ending at that point, or three arcs meeting at $`120^\circ`$
[S4:46–63].

**Local finiteness of connected components.** Only finitely many
global components of $`K`$ meet any relatively compact open set
[S4:58–63].

**Endpoint weak-$`L^4`$ gradient bound.** $`\nabla u\in
L^{4,\infty}_{\mathrm{loc}}`$ and $`\nabla u\in L^p_{\mathrm{loc}}`$
for $`0<p<4`$ [S4:72–77].

## Section skeleton

**Manuscript** [S3:26–33], 6 sections under `build/sections/`: introduction
[S4:46–63], reductions, blowup, geometry, interaction, completion. Its root
is `build/main.tex`. One figure file. No bibliography file.

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — a root `build/main.tex`, 6 `.tex` files under
`build/sections/`, one figure `.tex` — and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 366 at line 8872. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 832. |
| S3 | [`preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/build/main.tex`](../../../preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/build/main.tex) | 46 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/build/sections/introduction.tex`](../../../preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/build/sections/introduction.tex) | 185 | Introduction: the variational problem, the main theorem, history, and proof strategy. |
