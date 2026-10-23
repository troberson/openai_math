[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 059](../../index/algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md)

# 059 — Counterexamples to Zariski's multiplicity conjecture

[Index page](../../index/algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:1540]: "**059. Counterexamples to Zariski's multiplicity conjecture.** Disproves Zariski's multiplicity conjecture by constructing reduced holomorphic hypersurface germs that are ambiently homeomorphic but have different multiplicities. The examples include hypersurfaces in ℂ⁴ with isolated critical points and multiplicities four and five."

Two manuscripts carry this family. The first,
*Ambiently homeomorphic isolated hypersurfaces of multiplicities
two and three* [S2], has the abstract [S2:9–15]: "2"

The second, *Ambiently homeomorphic isolated hypersurface germs in
$\C^4$ with multiplicities four and five* [S8], has the abstract
[S8:9–13]: "6"

## Undergraduate summary

Zariski's multiplicity question asks whether the embedded topological
germ of a hypersurface determines its multiplicity, the least total
degree of a nonzero term in its defining equation [S3:4–14]:
"3"

The first theorem [S3:39–51]:

> 4

A single finite ambient dimension suffices. The dimension is
determined by exact integer arithmetic; it is not intended to be
minimal. The same examples answer Arnold's corank problem
negatively and the right-topological multiplicity conjecture
negatively [S3:53–82].

The second theorem settles the question in four complex variables
[S9:31–45]:

> 7

## Graduate summary

**The Seifert form strategy.** The main difficulty is to preserve
different ordinary orders while making the integral Seifert forms
coincide [S3:152–167]:

> 5

The spectrum determines the real Seifert form for weighted
homogeneous singularities via Steenbrink and Némethi. The
integral-monodromy results of Hertling and Mase, building on Orlik
and Randell, determine the integral module with its monodromy
operator for sums of chain singularities. The arithmetic part of
the proof produces a single integral map preserving the whole
Seifert form.

**The C4 construction.** For the open books on $S^7$, a
classification theorem turns a congruence of integral Seifert forms
into an equivalence of embedded links [S9:47–54]:

> 8

The proof is organized around obtaining that integral congruence
while retaining the different orders of the equations. The
construction uses plane curve inputs [S10], a tube construction
[S11], and a lattice filling calculation [S12].

**Positive cases and the family distinction.** The A'Campo–Lê
theorem shows that a reduced hypersurface germ ambiently
homeomorphic to a smooth one is itself smooth, so multiplicity one
cannot occur in an unequal-multiplicity pair [S3:19–24]. Within a
$\mu$-constant family, equimultiplicity holds by the work of
Greuel–O'Shea and Fernández de Bobadilla–Pełka [S3:106–130].
The two different multiplicities in the theorems therefore
preclude a connecting $\mu$-constant family.

## History of the conjecture

Zariski posed the question in 1971, following his work on the
topology and equisingularity of plane curves, where the embedded
topology determines the characteristic data of the branches and
hence the multiplicity [S3:16–24, S9:13–22]. The A'Campo–Lê theorem
handles the smooth case. Yau established multiplicity invariance
for pairs of isolated quasihomogeneous surface singularities in
$\C^3$. Fernandes, Jelonek, and Sampaio proved that multiplicity
two is preserved by ambient bi-Lipschitz equivalence [S3:132–148].

For the C4 case, Koike and Parusiński proposed high-power
suspension of plane curves with isometric Seifert forms as a route
to topologically equivalent four-variable germs [S9:90–97]. The
smooth sum and tensor calculation belongs to the product theory of
Sakamoto and Kauffman–Neumann.

## Consequences

**The embedded Zariski multiplicity conjecture is false.** There
exist reduced hypersurface germs that are ambiently homeomorphic
but have different multiplicities [S3:39–51, S9:31–45].

**The right-topological version is also false.** The defining
function germs are topologically right equivalent and have
unequal multiplicities [S3:58–68].

**Arnold's corank problem has a negative answer for ambient
topological equivalence** [S3:70–82].

**The C4 case is settled.** In four complex variables, multiplicities
four and five coexist on ambiently homeomorphic germs [S9:31–45].

## Section skeleton

**Manuscript 1** [S2], 6 sections under `build/sections/` plus appendix:

1. The multiplicity problem [S3]
2. Background [S4]
3. Seeds [S5]
4. Local [S6]
5. Global [S7]
6. Conclusion [S2]
7. Appendix: certificate [S2]

**Manuscript 2** [S8], 9 sections under `build/sections/`:

1. Introduction [S9]
2. Plane [S10]
3. Ambient [S8]
4. Tube [S11]
5. Boundary [S8]
6. Collapse [S8]
7. Lattice [S12]
8. Fillings [S8]
9. Arithmetic [S8]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The two manuscripts ship
7 and 9 `.tex` files respectively.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 059 at line 1540. |
| S2 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/paper.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/paper.tex) | 27 | Manuscript 1 main file: abstract and section inputs. |
| S3 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/introduction.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/introduction.tex) | 246 | The multiplicity problem, the theorem, prior work, and the proof strategy. |
| S4 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/background.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/background.tex) | 226 | Milnor fibration, Seifert form, and weighted homogeneous background. |
| S5 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/seeds.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/seeds.tex) | 307 | The seed construction from finite relations. |
| S6 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/local.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/local.tex) | 438 | The local Seifert form identification. |
| S7 | [`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/global.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/build/sections/global.tex) | 406 | The global homeomorphism construction. |
| S8 | [`preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/paper.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/paper.tex) | 25 | Manuscript 2 main file: abstract and section inputs. |
| S9 | [`preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/01-introduction.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/01-introduction.tex) | 170 | The theorem, context, and proof strategy for the C4 case. |
| S10 | [`preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/02-plane.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/02-plane.tex) | 284 | Plane curve inputs. |
| S11 | [`preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/04-tube.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/04-tube.tex) | 100 | The tube construction. |
| S12 | [`preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/07-lattice.tex`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/build/sections/07-lattice.tex) | 348 | The lattice and filling calculation. |
