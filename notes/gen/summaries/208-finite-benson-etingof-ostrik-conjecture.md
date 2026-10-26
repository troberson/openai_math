[Notes](../../README.md) / [Summaries](README.md) / [Algebra](../index/disciplines/algebra.md) / [Family 208](../index/algebra/208-finite-benson-etingof-ostrik-conjecture.md)

# 208 — The finite Benson–Etingof–Ostrik conjecture

[Index page](../index/algebra/208-finite-benson-etingof-ostrik-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:4748] and the catalog abstract [S2:497] state
the family's claim: every finite symmetric tensor category over an
algebraically closed field of characteristic $p>0$ admits a $k$-linear
exact faithful strong symmetric monoidal fiber functor to a higher
Verlinde category $\mathrm{Ver}_{p^n}$, with the level $n$ allowed to
depend on the category, including characteristic two — resolving the
finite case of the Benson–Etingof–Ostrik conjecture. The manuscript's
abstract "We prove the finite case of the Benson–Etingof–Ostrik conjecture:
every finite symmetric tensor category over an algebraically closed field
$k$ of characteristic $p>0$ admits a $k$-linear exact faithful strong symmetric
monoidal functor to a finite higher Verlinde category
$\mathrm{Ver}_{p^n}(k)$. The result includes characteristic two,
and the level $n$ may depend on the category. [S3:11–18]"

## Undergraduate summary

In representation theory a fiber functor from a symmetric tensor category
$\mathcal C$ to vector spaces is an exact, faithful, monoidal functor that
"forgets" the tensor structure while preserving it — it is the categorical
analogue of a representation of the group a category classifies. Tannaka's
theorem says that, in characteristic zero, such a functor realizes
$\mathcal C$ as the representations of an affine group scheme. In positive
characteristic the target must be larger: the higher Verlinde categories
$\mathrm{Ver}_{p^n}(k)$ form a tower of finite symmetric tensor
categories, each a finite abelian envelope of a quotient of tilting
$SL_2$-modules [S4:4–33]. The manuscript proves that every finite
symmetric tensor category lands in some level of this tower 

> **theorem**
For every prime $p$, every algebraically closed field $k$ of
characteristic $p$, and every finite symmetric tensor category
$\mathcal C$ over $k$, there are an integer $n\geq1$ and a fiber functor
\[
 \mathcal C\longrightarrow\operatornameVer_p^n(k).
\] [S4:35–42]

The level $n$ may depend on the category; the theorem makes no assertion
about the growth of $n$ or about nonfinite categories of moderate growth.

## Graduate summary

**The Verlinde tower and the incompressible classification.** The higher
Verlinde categories are needed because the ordinary Frobenius functor
need not be exact in positive characteristic. The theorem, combined with
the higher Verlinde subcategory classification of Benson–Etingof–Ostrik,
classifies the incompressible finite symmetric tensor categories — those
for which every exact symmetric tensor functor out is fully faithful —
giving the finite case of Coulembier–Etingof–Ostrik's Conjecture B. In
characteristic two, their subterminality theorem further gives uniqueness
up to tensor isomorphism of the functor into the tower union [S4:44–67].

**The restricted-tilting conjecture.** The proof's key
representation-theoretic input is the full restricted-tilting conjecture,
proved in the manuscript: for $r\ge1$ and suitable $p$-power $q$, the
Steinberg module of highest weight $p^n-1$ is a direct summand of a
suitable tensor product. This conjecture was known in the rank-one case
and for $p=r=2$; the manuscript proves it in full, which is what makes
the higher Frobenius constructions of Coulembier–Flake symmetric monoidal
[S4:71–127].

**The descent and projectivity arguments.** The remaining steps reduce
the general category to a projective-generator setting, establish a
support-theoretic bound, and carry out the descent from the tower level
to the finite category [S4:131–169].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

In characteristic zero, Deligne's theorem makes supervector spaces a
common target for fiber functors from symmetric tensor categories of
moderate growth. In positive characteristic, Ostrik proved that symmetric
fusion categories admit fiber functors to $\mathrm{Ver}_p$.
Etingof–Ostrik constructed the ordinary Frobenius functor for
nonsemisimple categories and characterized the finite categories on which
it is exact by the existence of a fiber functor to
$\mathrm{Ver}_p$; Coulembier–Etingof–Ostrik extended that
characterization to categories of moderate growth [S4:71–100]. The
characteristic-two examples of Benson–Etingof led to the all-prime tower
of Benson–Etingof–Ostrik, constructed independently through abelian
envelopes by Coulembier. The present result resolves the finite case for
every prime [S4:100–127].

## Consequences

**The finite incompressible classification.** The theorem, together
with the subcategory classification, gives a complete classification of
finite symmetric tensor categories with no proper exact quotient, and
the finite case of Conjecture B. In characteristic two, uniqueness up
to tensor isomorphism of the fiber functor into the tower union follows
from the subterminality theorem [S4:44–67].

**The generalized Tannaka realization.** The theorem realizes every
finite symmetric tensor category as representations of an affine group
scheme internal to a chosen finite Verlinde level, with the canonical
fundamental-group compatibility — a positive-characteristic analogue of
the classical Tannaka duality [S4:44–67].

## Section skeleton

**Manuscript** [S3:11–18], 8 sections under `build/sections/`:
introduction [S4:35–42], preliminaries, restricted, higher, projectivity,
support, descent, consequences. Plus one figure under `build/figures/`
and a `preamble.tex`.

The manuscript's root is `build/main.tex`, with a `references.bib`
bibliography [S5]. It ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorem is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX
manuscript — 10 `.tex` files under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 208 at line 4748. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 497. |
| S3 | [`preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/main.tex`](../../../preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/main.tex) | 32 | Main file: title and abstract. |
| S4 | [`preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/sections/introduction.tex`](../../../preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/sections/introduction.tex) | 169 | The main theorem, the Verlinde tower setup, the structural consequences, the background, and the proof strategy. |
| S5 | [`preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/references.bib`](../../../preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/build/references.bib) | 160 | The manuscript's bibliography. |

## Bibliography

- The Stacks Project Authors, The Stacks Project (2026)
- Benson, Dave, Etingof, Pavel, Ostrik, Victor, New incompressible symmetric tensor categories in positive characteristic (2023)
- Benson, Dave, Etingof, Pavel, Symmetric tensor categories in characteristic 2 (2019)
- Benson, David J., Modules for elementary abelian groups and hypersurface singularities (2015)
- Benson, David J., Representations of Elementary Abelian $p$-Groups and Vector Bundles (2017)
- Chouinard, II, Leo G., Projectivity and relative projectivity over group rings (1976)
- Coulembier, Kevin, Etingof, Pavel, Ostrik, Victor, On Frobenius exact symmetric tensor categories (2023)
- Coulembier, Kevin, Etingof, Pavel, Ostrik, Victor, Incompressible tensor categories (2024)
- Coulembier, Kevin, Tannakian categories in positive characteristic (2020)
- Coulembier, Kevin, Flake, Johannes, Towards higher Frobenius functors for symmetric tensor categories (2026)
- Coulembier, Kevin, Flake, Johannes, A conjecture on the tensor ideal for an elementary $p$-group generated by the restriction of a Steinberg module (2025)
- Coulembier, Kevin, Monoidal abelian envelopes (2021)
- Deligne, Pierre, Catégories tensorielles (2002)
- Deligne, Pierre, Milne, James S., Tannakian categories (1982)
- Donkin, Stephen, On tilting modules for algebraic groups (1993)
- Doty, Stephen, Henke, Anne, Decomposition of tensor products of modular irreducibles for $SL_2$ (2005)
- Etingof, Pavel, Ostrik, Victor, On the Frobenius functor for symmetric tensor categories in positive characteristic (2021)
- Etingof, Pavel, Gelaki, Shlomo, Finite symmetric tensor categories with the Chevalley property in characteristic 2 (2021)
- Etingof, Pavel, Gelaki, Shlomo, Nikshych, Dmitri, Ostrik, Victor, Tensor Categories (2015)
- Jantzen, Jens Carsten, Representations of Algebraic Groups (2003)
- Ostrik, Victor, On symmetric fusion categories in positive characteristic (2020)
- Riche, Simon, Lectures on modular representation theory of reductive algebraic groups
