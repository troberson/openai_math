[Notes](../../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 285](../index/operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md)

# 285 — Counterexamples to Baum–Connes and Kadison–Kaplansky

[Index page](../index/operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md)

## Original CONTENTS.md summary

The release's blurb [S1:7100] and the catalog abstract [S2:662] state
the family's claim: the coefficient-free reduced Baum--Connes conjecture
is false — once through a failure of rational injectivity of assembly
witnessed by a finitely generated torsion-free group, and separately
through the existence of a torsion-free group whose reduced group
$`C^*`$-algebra carries a nontrivial projection, which also disproves the
Kadison--Kaplansky projection conjecture. The three manuscripts make
three related claims. The injectivity manuscript "We disprove rational injectivity of the coefficient-free reduced
Baum–Connes assembly map for torsion-free groups. Specifically, we construct
a finitely generated torsion-free discrete group whose degree-zero assembly
map has a kernel class of infinite order. [S3:57–62]"
The projection manuscript "We construct a finitely generated torsion-free discrete group whose reduced
group $`C^*`$-algebra contains a projection other than zero and the identity.
This disproves the Kadison–Kaplansky projection conjecture. [S5:9–13]" The irrational-trace
manuscript "We construct a finitely generated discrete group whose reduced group
$`C^*`$-algebra contains a projection of irrational canonical trace. Its
$`K_0`$-class lies outside the image of the coefficient-free reduced
Baum–Connes assembly map. This disproves the coefficient-free reduced
Baum–Connes conjecture for countable discrete groups. [S7:8–14]"

## Undergraduate summary

Two long-standing conjectures in operator algebra and index theory
make the same prediction for torsion-free discrete groups, and this
family refutes both. The Baum--Connes assembly map sends the
topology of a group — the $`K`$-homology of its classifying space
$`B\G`$ — to the $`K`$-theory of its reduced group $`C^*`$-algebra
$`C_r^*(\G)`$, the completion of the group's left regular
representation on $`\ell^2(\G)`$. The conjecture asserts this map is an
isomorphism in the (coefficient-free) case. A separate
prediction, the Kadison--Kaplansky projection conjecture, says the
reduced group $`C^*`$-algebra of a torsion-free group contains no
projections other than zero and the identity — the group's canonical
trace $`\tau(x)=\langle x\delta_1,\delta_1\rangle`$ being integral on
the assembly image is the standard route to that conclusion [S4:4–16].
The first manuscript disproves injectivity of the assembly map by
constructing a torsion-free group whose degree-zero assembly map has a
kernel class of infinite order. The other two construct torsion-free
groups whose reduced $`C^*`$-algebras carry a projection: the second
wants any projection $`e`$ with $`0<\tau(e)<1`$ 

> **theorem**
There exist a finitely generated torsion-free discrete group $`G_{\mathrm{proj}}`$
and a projection $`e\in C_r^*(G_{\mathrm{proj}})`$ such that
$$0<\tau_{G_{\mathrm{proj}}}(e)<\frac12.$$
In particular, $`e`$ is neither zero nor the identity. [S6:13–21]

The third wants a projection whose trace is *irrational*, a stronger
property that places its $`K_0`$-class outside the assembly image and so
disproves the coefficient-free Baum--Connes conjecture directly


> **theorem**
There exist a finitely generated discrete group $`G_{\mathrm{sur}}`$ and a projection
$`b_0\in C_r^*(G_{\mathrm{sur}})`$ with irrational canonical trace. Moreover,
$$[b_0]\notin\mu_0^{G_{\mathrm{sur}}}\bigl(K_0^{G_{\mathrm{sur}}}(\underline EG_{\mathrm{sur}})\bigr).$$
In particular, the coefficient-free reduced Baum–Connes conjecture for
countable discrete groups is false. [S8:57–65]

## Graduate summary

**The injectivity failure.** The Baum--Connes manuscript embeds the
torus $`\mathbb Z^2`$ into a finitely generated torsion-free group and tracks
the torus's rank-zero Bott class through the assembly map. A
cohomology class that pairs to one with the embedded torus's Dirac
class detects a class $`h`$ of infinite order in $`K_0(B\G)`$; a
separate operator-algebra construction then shows the corresponding
Bott class vanishes in $`K_0(C_r^*(\G))`$, so $`h`$ maps to zero. The
group is built by a layered graph labeled by interleaved finite
streams, given voltages in the integral Heisenberg group, and completed
to a finitely generated torsion-free group; finite additivity of the
rank-zero Bott representatives forces the height-zero term to vanish
[S4:138–224].

**The two projection constructions.** The Kadison--Kaplansky
manuscript builds a torsion-free group from an infinite graphical
presentation followed by a free product with a finitely generated free
group; every parameter is finite, and the resulting reduced
$`C^*`$-algebra carries a projection of trace strictly between zero and
one half. The group's geometry encodes an infinite tower through
embedded nilpotent covers, so the standard integrality route to
projectionlessness does not apply [S6:34–70]. The irrational-trace
manuscript produces a torsion-free group with a projection of
irrational canonical trace; because the trace is irrational the
projection's $`K_0`$-class cannot lie in the image of the
coefficient-free reduced assembly map, which is the precise failure
the conjecture forbids.

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under each `build/` is the only source.

## History of the conjecture

The Baum--Connes conjecture was introduced in a 1982 preprint
published in 2000 and developed with Higson into the coefficient-free
form stated here. It is known for substantial classes of groups:
Higson--Kasparov with separable coefficients for groups acting
properly by affine isometries, Mineyev--Yu and Lafforgue for
hyperbolic groups, and Guentner--Higson--Weinberger for split
injectivity with coefficients for countable linear groups. Higson,
Lafforgue, and Skandalis constructed counterexamples to surjectivity
with nontrivial coefficients, but their group examples are distinct
from the coefficient-free group injectivity addressed here. The
projection form of Kadison--Kaplansky goes back to Kaplansky's
question about idempotents in simple unital $`C^*`$-algebras; Pimsner
and Voiculescu proved the free-group case, and the integrality of the
canonical trace on the assembly image gives projectionlessness for
the same hyperbolic and affine-isometry classes [S4:39–83]
[S6:34–70].

## Consequences

**The coefficient-free reduced Baum--Connes conjecture is false.** The
family provides two independent counterexamples: a torsion-free group
with an infinite-order kernel class of the assembly map, and a torsion-free
group with a projection of irrational trace whose $`K_0`$-class lies
outside the assembly image [S4:18–26] [S8:57–65].

**The Kadison--Kaplansky projection conjecture is false.** A
finitely generated torsion-free discrete group has a reduced group
$`C^*`$-algebra containing a projection $`e`$ with
$`0<\tau(e)<1/2`$, so the algebra carries a nontrivial scalar
projection [S6:13–21].

## Section skeleton

**Baum--Connes injectivity manuscript** [S3:57–62], 9 sections under
`build/sections/`: 00-introduction [S4:18–26], 01-labeling, 02-expansion,
03-pruning, 04-analysis, 05-geometry, 05b-domains, 06-assembly,
07-completion. Its root is `build/main.tex`, with a `references.bib`
bibliography.

**Kadison--Kaplansky manuscript** [S5:9–13], 11 sections under
`build/sections/`: introduction [S6:13–21], scalar, setup, tower,
expansion, pruning, geometry, nilpotent, sampling, spectral,
conclusion. Plus one figure under `build/figures/`. Its root is
`build/paper.tex`, with a `references.bib` bibliography.

**Irrational-trace manuscript** [S7:8–14], built flat under `build/`:
introduction [S8:57–65], geometry, data, module, spectrum, trace. Plus one
figure under `build/figures/`. Its root is `build/paper.tex`, with a
`references.bib` bibliography.

None of the three manuscripts ships a `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships three LaTeX
manuscripts — 10 `.tex` files in the injectivity `build/`, 12 plus a
preamble and a figure in the projection `build/`, and 7 plus a
preamble and a figure in the irrational-trace `build/` — and no
non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | The release's blurb for family 285 at line 7100. |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | The catalog abstract at line 662. |
| S3 | [`preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/build/main.tex`](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/build/main.tex) | 77 | Baum--Connes injectivity manuscript: title and abstract. |
| S4 | [`preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/build/sections/00_introduction.tex`](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/build/sections/00_introduction.tex) | 248 | Baum--Connes injectivity introduction: the setup, the main theorem, the distinction from earlier counterexamples, and the construction. |
| S5 | [`preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/build/paper.tex`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/build/paper.tex) | 30 | Kadison--Kaplansky manuscript: title and abstract. |
| S6 | [`preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/build/sections/introduction.tex`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/build/sections/introduction.tex) | 176 | Kadison--Kaplansky introduction: the setup, the main theorem, and the context. |
| S7 | [`preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/build/paper.tex`](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/build/paper.tex) | 29 | Irrational-trace manuscript: title and abstract. |
| S8 | [`preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/build/introduction.tex`](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/build/introduction.tex) | 195 | Irrational-trace introduction: the main theorem on the projection outside the assembly image. |
