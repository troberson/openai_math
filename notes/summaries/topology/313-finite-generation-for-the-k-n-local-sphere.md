[Notes](../../README.md) / [Summaries](../README.md) / [Topology](../../index/disciplines/topology.md) / [Family 313](../../index/topology/313-finite-generation-for-the-k-n-local-sphere.md)

# 313 — Finite generation for the $K(n)$-local sphere

[Index page](../../index/topology/313-finite-generation-for-the-k-n-local-sphere.md)

## Original CONTENTS.md summary

The release's blurb [S1:7699] and the catalog abstract [S2:720] state
the family's claim: the degreewise finiteness question of Hovey and
Hovey--Strickland is answered — every homotopy group of the
$K(n)$-local sphere is a finitely generated $\Zp$-module, for every
prime, positive height, and integer degree; and the same conclusion
holds after $K(n)$-localizing any finite $p$-local spectrum. The
manuscript's abstract [S3:8–14]: "**abstract**
We prove that the homotopy groups of the $K(n)$-local sphere are finitely
generated $\mathbb Z_p$-modules in every integer degree, for every prime $p$
and positive height $n$. Equivalently, the same conclusion holds after
$K(n)$-localizing any finite $p$-local spectrum. This answers the degreewise
finiteness question of Hovey and Hovey–Strickland.
\endabstract"

## Undergraduate summary

Morava $K$-theory $K(n)$ isolates a single "chromatic height" in stable
homotopy theory, and $L_{K(n)}S$ is the $K(n)$-local sphere. The basic
finiteness questions in this setting ask whether the homotopy groups
of such a localized spectrum are "small" — in particular, whether each
individual group, in each individual integer degree, is a finitely
generated module over the $p$-adic integers $\Zp$. The difficulty is
that $K(n)$-local spectra are not connective, so a degree-by-degree
finiteness statement must control *every* integer degree at once, with
no assumption that the negative groups vanish. The manuscript proves
the degreewise version for the sphere [S4:3–11]:

> **theorem**
For every prime $p$, every integer $n\geq 1$, and every integer $t$,
the $\Zp$-module
\[
                 \pi_t L_{K(n)}S_p^\wedge
\]
is finitely generated. Equivalently, for every finite $p$-local
spectrum $F$, the module $\pi_t L_{K(n)}F$ is finitely generated
over $\Zp$ in every integer degree $t$.
\endtheorem

The equivalent form — applying $L_{K(n)}$ to *any* finite $p$-local
spectrum $F$ — follows because finite generation over the Noetherian
ring $\Zp$ is preserved by kernels, cokernels, and extensions, so the
sphere case extends to all finite spectra through finite cofiber
sequences, suspensions, and retracts.

## Graduate summary

**The coefficient theorem.** The algebraic engine of the proof is a
finiteness theorem for the continuous cohomology of the ordinary
stabilizer group $P_n$ of a height-$n$ formal group over a finite
field. The coefficients carry their compact deformation-parameter
topology, and the assertion is
$H^a_{\cts}(P_n;(E_n)_{2t}/p)$ is finite for every $a\ge0$ and
$t\in\Z$; the proof retains a precise larger allowed class — integer
powers of the periodicity line tensored with functions on whole finite
tuples of division points, with Frobenius-powered coordinates, under
finite sums, tensor products, equivariant summands, and finite
filtrations. The reason this suffices for the sphere: the finite
Galois quotient from $P_n$ to the extended stabilizer preserves
degreewise finiteness, Morava descent for the Moore spectrum $S/p$ has
finite second-page entries, a horizontal vanishing line on a finite
page leaves finitely many entries in each limiting stem, and compact
Nakayama then promotes finiteness modulo $p$ to $\Zp$-finite
generation [S4:35–69].

**The open-stratum argument.** Coefficient finiteness is proved by
downward induction on the height, from $A_n$ down to the first
parameter. At each step the next-height hypothesis makes the
cohomology of every finite boundary strip finite, so localization from
a compact allowed coefficient to its $x$-inversion has countable
kernel and cokernel; it remains to prove the open-stratum cohomology is
countable, so that the original is compact Hausdorff and countable,
hence finite. The geometric input is the completed marking tower,
whose quotient by $G$ is the space of independent $r$-tuples in
$H^1(\cO(-1/m))$ on the relative Fargues--Fontaine curve. Uniform
Kummer calculations and deletion of dependent tuples make the
equivariant compact-support cohomology finite, and invariant algebraic
functions on the tower are constants, which fixes a single Cartier
transfer $S$. The transfer is encoded as a Laurent module of convergent
series whose residue quotient is the transpose transfer tower; the
positive-order kernel is homologically acyclic, and a Baire-property
analytic-subgroup argument together with Frobenius contraction shows
every positive-order cycle is a boundary. A final finite-translation
representation argument closes the fixed-level countability, and the
height induction finishes [S4:73–188].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

The degreewise finite-generation question was posed by Hovey, and by
Hovey with Strickland, as the natural finiteness analogue of the
classical finiteness theorems for Morava $E$-theory. The sphere case
resisted the standard descent arguments because the localized sphere
is not connective, so the usual bounded-below hypotheses that control
each degree are unavailable. The present proof introduces an
intermediate countability theorem — that a compact Hausdorff countable
group cohomology module is finite — as the bridge from geometric
finiteness to ordinary coefficient cohomology, and develops the
completed marking tower together with its Kummer and independent-tuple
geometric outputs to supply the compact-support and fixed-level
finiteness needed at each height [S4:35–188].

## Consequences

**The $K(n)$-local sphere is degreewise finitely generated.** For every
prime $p$, every $n\ge1$, and every integer $t$,
$\pi_t L_{K(n)}S_p^\wedge$ is a finitely generated $\Zp$-module
[S4:13–22].

**The conclusion extends to all finite $p$-local spectra.** For every
finite $p$-local spectrum $F$ and every integer $t$,
$\pi_t L_{K(n)}F$ is finitely generated over $\Zp$; the equivalence is
a consequence of the Noetherian preservation of finite generation under
kernels, cokernels, and extensions [S3:8–14].

**The degreewise finiteness question of Hovey / Hovey--Strickland is
resolved.** There is no uniform bound asserted on the number of
generators or on the torsion order as $p$, $n$, or $t$ varies; the
statement is that each individual degree is finite [S4:13–22].

## Section skeleton

**Manuscript** [S3:8–14], 13 sections under `build/sections/`:
history, introduction [S4:13–22], continuous-cohomology, finite-markings,
completed-tower, kummer-supports, independent-tuples,
natural-transfers, laurent-model, residue-cutoff, pro-transfer,
coefficient-finiteness, sphere. Plus one figure
(`build/figures/support-directions.tex`). Its root is `build/main.tex`,
with a `preamble.tex` and a `references.bib` bibliography
[S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript
— 13 `.tex` files under `build/sections/`, a root `build/main.tex`,
one `preamble.tex`, one figure under `build/figures/`, and a
`references.bib` bibliography under `build/sources/` — and no
non-LaTeX evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 313 at line 7699. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 720. |
| S3 | [`preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/main.tex`](../../../preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/main.tex) | 48 | Manuscript main file: title and abstract. |
| S4 | [`preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/sections/01-introduction.tex) | 213 | Introduction: the setup, the main theorem, the coefficient theorem, the open-stratum argument, and the conventions. |
| S5 | [`preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/sources/references.bib`](../../../preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/build/sources/references.bib) | 464 | Manuscript bibliography. |

## Bibliography

- Achinger, Piotr, Gilles, Sally, Nizio{\l}, Wies{\l}awa, Compactly supported $p$-adic pro-{é}tale cohomology of analytic varieties (2025)
- The Stacks Project Authors, The Stacks Project (2026)
- Barthel, Tobias, Schlank, Tomer M., Stapleton, Nathaniel, Weinstein, Jared, On the rationalization of the $K(n)$-local sphere (2025)
- Beaudry, Agn{\`e}s, Goerss, Paul G., Hopkins, Michael J., Stojanoska, Vesna, Dualizing spheres for compact $p$-adic analytic groups and duality in chromatic homotopy (2022)
- Benson, Dave, Iyengar, Srikanth B., Krause, Henning, Module categories for group algebras over commutative rings (2013)
- Blickle, Manuel, B{ö}ckle, Gebhard, Cartier modules: finiteness results (2011)
- Boggi, Marco, Corob Cook, Ged, Continuous cohomology and homology of profinite groups (2016)
- Le Bras, Arthur-C{é}sar, Espaces de Banach–Colmez et faisceaux coh{é}rents sur la courbe de Fargues–Fontaine (2018)
- Cartier, Pierre, Une nouvelle op{é}ration sur les formes diff{é}rentielles (1957)
- Clausen, Dustin, Scholze, Peter, Condensed Mathematics and Complex Geometry (2026)
- Colmez, Pierre, Espaces de Banach de dimension finie (2002)
- Coulembier, Kevin, Some homological properties of ind-completions and highest weight categories (2020)
- Culver, Dominic Leon, Zhang, Ningchuan, Exotic Picard groups and chromatic vanishing via the Gross–Hopkins duality (2024)
- Devinatz, Ethan S., Hopkins, Michael J., Homotopy fixed point spectra for closed subgroups of the Morava stabilizer groups (2004)
- Devinatz, Ethan S., Towards the finiteness of $\pi_*L_{K(n)}S^0$ (2008)
- Devinatz, Ethan S., Homotopy groups of homotopy fixed point spectra associated to $E_n$ (2007)
- Fargues, Laurent, Scholze, Peter, Geometrization of the local Langlands correspondence (2026)
- Fargues, Laurent, Fontaine, Jean-Marc, Courbes et fibr{é}s vectoriels en th{é}orie de Hodge $p$-adique (2018)
- Heard, Drew, The $\mathrm{Sp}_{k,n}$-local stable homotopy category (2023)
- Hopkins, Michael J., $K(1)$-local $E_\infty$-ring spectra (2014)
- Hovey, Mark, Morava $K$- and $E$-theory (n.d.)
- Hovey, Mark, Strickland, Neil P., Morava $K$-theories and localisation (1999)
- Kechris, Alexander S., Classical Descriptive Set Theory (1995)
- Lazard, Michel, Groupes analytiques $p$-adiques (1965)
- Li, Guchuan, Invertible spectra of finite type (2021)
- Lipman, Joseph, Dualizing sheaves, differentials and residues on algebraic varieties (1984)
- Lubin, Jonathan, Tate, John, Formal moduli for one-parameter formal Lie groups (1966)
- Lurie, Jacob, Classification of Formal Groups (Lecture 14) (2010)
- Mathew, Akhil, The Galois group of a stable homotopy theory (2016)
- Milne, J. S., Class Field Theory (2020)
- Milne, J. S., Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field (2017)
- Ravenel, Douglas C., Complex Cobordism and Stable Homotopy Groups of Spheres (1986)
- Scholze, Peter, {É}tale cohomology of diamonds (2026)
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties (2013)
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties—corrigendum (2016)
- Scholze, Peter, Weinstein, Jared, Moduli of $p$-divisible groups (2013)
- Scholze, Peter, Perfectoid spaces (2012)
- Strauch, Matthias, Galois actions on torsion points of universal one-dimensional formal modules (2007)
- Symonds, Peter, Permutation complexes for profinite groups (2007)
- Tate, John T., $p$-Divisible Groups (1967)
- Ansch{ü}tz, Johannes, Le Bras, Arthur-C{é}sar, A Fourier transform for Banach–Colmez spaces (2025)
