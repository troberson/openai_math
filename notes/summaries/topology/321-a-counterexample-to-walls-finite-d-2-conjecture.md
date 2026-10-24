[Notes](../../README.md) / [Summaries](../README.md) / [Topology](../../index/disciplines/topology.md) / [Family 321](../../index/topology/321-a-counterexample-to-walls-finite-d-2-conjecture.md)

# 321 — A counterexample to Wall's finite D(2) conjecture

[Index page](../../index/topology/321-a-counterexample-to-walls-finite-d-2-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:7856] and the catalog abstract [S2:736] state
the family's claim: a finite connected three-dimensional CW complex
whose universal cover has no integral homology above degree two and
whose third cohomology vanishes for every local coefficient module, yet
which has no finite two-dimensional homotopy model — disproving Wall's
finite $D(2)$ conjecture with an infinite fundamental group. The
manuscript's abstract "We give a negative answer to Wall's finite $D(2)$ problem. We construct
a finite connected three-dimensional CW complex satisfying the $D(2)$
finiteness condition but not homotopy equivalent to any finite CW complex
of dimension at most two. The example has infinite fundamental group. [S3:8–13]"

## Undergraduate summary

Wall's finiteness conditions ask when algebraic restrictions on a CW
complex force it to have a homotopy model of a prescribed dimension.
For a finite connected CW complex $X$ with universal cover
$\widetilde X$, the $D(2)$ condition says that the universal cover has
no integral homology above degree two, and that the third cohomology of
$X$ vanishes for every finitely generated local coefficient module. The
finite $D(2)$ problem asks whether every such complex is homotopy
equivalent to a finite two-dimensional complex, with no asphericity
hypothesis imposed [S4:3–17]:

> There is a finite connected three-dimensional CW complex $X$ such that
\[
 H_i(\widetilde X;\Z)=0\quad(i>2),\qquad
 H^3(X;M)=0\quadfor every \Z[\pi_1(X)]-module M,
\]
but $X$ is not homotopy equivalent to any finite CW complex of
dimension at most two. [S4:19–27]

The answer is negative: the constructed complex satisfies both
algebraic finiteness conditions and has an infinite fundamental group,
yet no finite two-dimensional complex is homotopy equivalent to it.

## Graduate summary

**The obstruction.** The proof combines two independent ingredients.
The geometric obstruction is a character-based criterion: for a
connected finite two-dimensional complex $Y$, a character
$\rho\colon\pi_1(Y)\to\C^\times$ determines a one-dimensional complex
local system $L_\rho$, and if $H_2(Y;L_\rho)=0$ then
$\rho(g)=1$ for every finite-order element $g\in\pi_1(Y)$. The proof
lifts the argument to an infinite cyclic tower following the
cyclic-tower method of Howie, with the additional input that vanishing
of rank-one twisted second homology persists under these cyclic covers
by a Laurent-polynomial rank argument [S4:34–100].

**The plus construction.** The second ingredient is Quillen's plus
construction applied to a finite two-dimensional complex along a
finitely normally generated perfect normal subgroup. Mannan showed
directly that this produces a finite $D(2)$ complex, and proved that
every finite cohomologically two-dimensional three-dimensional complex
arises in this way up to homotopy [S4:34–100].

**The example.** The manuscript gives a five-generator, four-relator
presentation with a perfect normal subgroup generated normally by two
powers. The quotient has an element of order two detected by a complex
character. An exact four-row boundary calculation shows that the
presentation complex has zero second homology with that character. The
plus construction preserves this vanishing and gives the required
finite $D(2)$ complex; the character obstruction excludes its
two-dimensional realization [S4:106–131].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

Wall introduced the dimension conditions in his work on finiteness for
CW complexes and reduced the $D(2)$ case to a finite three-dimensional
model; the remaining question was whether its three-dimensional cells
can also be removed up to homotopy. The problem reappeared as Problem
D3 in his 1979 list. A stable form has a positive answer: Cohen showed
that adjoining sufficiently many two-spheres suffices, and Hambleton
gave a proof with the number bounded by the number of three-dimensional
cells. Positive results for particular fundamental groups exist for
finite subgroups of $\operatorname{SO}(3)$ and for the generalized
quaternion groups of orders 24 and 32, established by Hambleton and by
Hofmann and Nicholson. Candidate counterexamples have come from
relation modules: Bridson and Tweedale constructed finite $D(2)$
complexes with virtually free fundamental groups using coprime
annihilation relations, whose failure to have finite two-dimensional
models is conditional on a relation-gap assertion [S4:34–100].

## Consequences

**Wall's finite $D(2)$ problem is answered negatively.** There exists
a finite connected three-dimensional CW complex $X$ satisfying the
$D(2)$ condition — no integral homology above degree two on the
universal cover, and $H^3(X;M)=0$ for every $\Z[\pi_1(X)]$-module $M$
— that is not homotopy equivalent to any finite CW complex of
dimension at most two [S4:19–27].

**The example has infinite fundamental group.** The finiteness
assertion concerns the cell structure, not the fundamental group; the
constructed complex has infinite $\pi_1$ [S3:8–13].

**A character obstruction is established.** For any finite
two-dimensional complex $Y$, the vanishing of $H_2(Y;L_\rho)$ for a
rank-one local system $L_\rho$ forces $\rho$ to take the value one on
every finite-order element of $\pi_1(Y)$, a criterion that applies
independently of any specific construction [S4:34–100].

## Section skeleton

**Manuscript** [S3:8–13], 4 sections under `build/sections/`:
01-introduction [S4:19–27], 02-tower, 03-plus, 04-construction. One figure
(`build/figures/tower.tex`). Its root is `build/main.tex`, with a
`preamble.tex` and a `references.bib` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— a root `build/main.tex`, 4 `.tex` files under `build/sections/`,
one figure, a `preamble.tex`, and a `references.bib` bibliography —
and no non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 321 at line 7856. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 736. |
| S3 | [`preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/main.tex`](../../../preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/main.tex) | 20 | Manuscript main file: title and abstract. |
| S4 | [`preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/sections/01-introduction.tex) | 131 | Introduction: the D(2) condition, the main theorem, background on positive results and prior candidates, and the proof structure. |
| S5 | [`preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/references.bib`](../../../preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/build/references.bib) | 148 | Manuscript bibliography. |

## Bibliography

- Bridson, Martin R., Tweedale, Michael, Deficiency and abelianized deficiency of some virtually free groups (2007)
- Cohen, J. M., Complexes of cohomological dimension two (1978)
- Fox, Ralph H., Free differential calculus. I. Derivation in the free group ring (1953)
- Hambleton, Ian, Two remarks on {Wall's D2} problem (2019)
- Hofmann, Tommy, Nicholson, John, Exotic presentations of quaternion groups and {Wall's D2} problem (2027)
- Howie, James, On pairs of 2-complexes and systems of equations over groups (1981)
- Johnson, F. E. A., Stable Modules and the {D(2)}-Problem (2003)
- Louder, Larsen, Wilton, Henry, Stackings and the W-cycles conjecture (2017)
- Mannan, W. H., {Quillen's} plus construction and the {D(2)} problem (2009)
- Mannan, W. H., Popiel, Tomasz, An exotic presentation of $Q_{28}$ (2021)
- Nicholson, John, On CW-complexes over groups with periodic cohomology (2021)
- Quillen, Daniel, Cohomology of groups (1971)
- Wall, C. T. C., Finiteness conditions for CW-complexes (1965)
- Wall, C. T. C., List of problems (1979)
