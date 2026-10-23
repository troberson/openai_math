[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 062](../../index/algebraic-and-complex-geometry/062-lebrun-salamon-conjecture-and-projective-contact-classification.md)

# 062 — The LeBrun–Salamon conjecture and projective contact classification

[Index page](../../index/algebraic-and-complex-geometry/062-lebrun-salamon-conjecture-and-projective-contact-classification.md)

## Original CONTENTS.md summary

The release's blurb [S1:1581]: "**062. Projective contact classification and the LeBrun–Salamon conjecture.** Proves the LeBrun–Salamon conjecture: every closed connected positive quaternionic-Kähler manifold of real dimension at least eight is homothetic to a compact symmetric Wolf space. It also proves contact-Fano homogeneity and classifies smooth connected complex projective contact manifolds of complex dimension at least three: those with $`b_2=1`$ are adjoint varieties with their canonical contact structures, while those with $`b_2\ge2`$ have underlying manifold $`\mathbb P(T^*Z)`$ for a smooth projective variety *Z*."

The manuscript, *Contact Fano manifolds and the LeBrun--Salamon
conjecture* [S2], has the abstract [S2:60–66]: "We resolve the contact-Fano homogeneity conjecture and the Riemannian"

## Undergraduate summary

A contact structure on a smooth complex projective variety of
dimension $2n+1$ is an exact sequence of vector bundles with a
nondegenerate Levi pairing [S3:3–18]: "3"

When $-K_X$ is ample, the pair $(X,F)$ is a contact Fano manifold.
The main theorem classifies them all [S3:30–43]:

> **theorem**


Every contact Fano manifold is the adjoint variety of a simple
complex Lie algebra, with its canonical contact structure.

## Graduate summary

**The projective contact classification.** Extending beyond
Fano, the second Betti number determines the model [S3:75–96]:

> **corollary**


The $b_2=1$ case is the adjoint variety; the $b_2\ge 2$ case is a
projectivized cotangent bundle. The reduction from general projective
contact to the Fano case uses Demailly's integrability theorem
(canonical bundle not pseudoeffective) and the Kebekus--Peternell--
Sommese--Wiśniewski classification [S3:71–73, S3:142–150].

**The LeBrun--Salamon conjecture.** The Riemannian application
follows from the twistor construction [S3:105–114]:

> **corollary**


A positive quaternionic-Kähler manifold has a twistor space that
is contact Fano. The algebraic classification identifies the twistor
space as an adjoint variety, and the metric is recovered from its
Kähler--Einstein structure [S11:4–12]:

> 8

The holonomy condition makes the metric Einstein. After fixing the
scale, the twistor bundle carries a Kähler--Einstein metric whose
curvature determines the original Riemannian connection.

**The proof structure.** The algebraic argument proceeds through
nine sections: the Picard reduction separates the two model
alternatives [S4], contact lines and their spanning identify the
distribution [S5], smoothing handles the singular locus [S6],
tensor extension recovers the full tangent bundle [S7], descent
identifies the adjoint-variety embedding [S8], first-jet generation
supplies the holomorphic immersion [S9], and the homogeneous
classification completes the algebraic side [S10].

## History of the conjecture

Wolf related compact quaternionic symmetric spaces to homogeneous
complex contact spaces in 1965. Salamon and Bérard-Bergery
independently developed the twistor construction associating a
contact Fano manifold to a positive quaternionic-Kähler manifold.
LeBrun characterized the contact Fano manifolds arising from twistor
spaces by the existence of a Kähler--Einstein metric, and the
LeBrun--Salamon finiteness and rigidity program set the stage for the
homogeneity conjecture [S3:128–140]:

> Wolf's work

Poon and Salamon classified the dimension-eight case; Ye and Druel
handled complex dimensions three and five. Buczyński and Wiśniewski
classified dimensions twelve and sixteen with reductive automorphism
groups [S3:164–180].

## Consequences

**The LeBrun--Salamon conjecture is proved in every dimension.**
Every closed connected positive quaternionic-Kähler manifold of real
dimension $4m \ge 8$ is homothetic to a compact symmetric Wolf
space [S3:105–114].

**The contact-Fano homogeneity conjecture is proved.** Every
smooth connected complex projective contact Fano manifold of
dimension $2n+1 \ge 3$ is contact-isomorphic to the adjoint
variety of a simple complex Lie algebra [S3:30–43].

**The projective contact classification is complete.** Smooth
connected complex projective contact manifolds of dimension $2n+1 \ge
3$ are either adjoint varieties ($b_2 = 1$) or projectivized
cotangent bundles ($b_2 \ge 2$) [S3:75–96].

**Kähler--Einstein existence follows.** Every contact Fano manifold
admits a Kähler--Einstein metric of positive scalar curvature
[S3:64–69].

## Section skeleton

**Main file** [S2], 9 sections under `build/sections/`:

1. Introduction [S3]
2. Reduction (Picard alternatives) [S4]
3. Contact lines [S5]
4. Smoothing [S6]
5. Extension [S7]
6. Descent [S8]
7. Jets [S9]
8. Homogeneous classification [S10]
9. Twistor spaces and quaternionic Kähler metric [S11]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace.
Nothing about this family is machine-checked. The ledger reads `paps_form 0`,
`mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The manuscript ships
11 `.tex` files under `build/` (9 sections plus main and references).

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 062 at line 1581. |
| S2 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/main.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/main.tex) | 78 | Main file: title, abstract, and section inputs. |
| S3 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/introduction.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/introduction.tex) | 335 | The contact Fano setup, the main theorem, the projective and quaternionic corollaries, and prior work. |
| S4 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/reduction.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/reduction.tex) | 176 | The Picard alternatives and the simply-connectedness lemma. |
| S5 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/lines.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/lines.tex) | 323 | The contact lines and their spanning. |
| S6 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/smoothing.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/smoothing.tex) | 365 | The smoothing of the contact-line variety. |
| S7 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/extension.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/extension.tex) | 642 | The tensor extension to the full distribution. |
| S8 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/descent.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/descent.tex) | 331 | The descent to the adjoint-variety model. |
| S9 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/jets.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/jets.tex) | 375 | The first-jet generation argument. |
| S10 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/homogeneous.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/homogeneous.tex) | 287 | The homogeneous classification. |
| S11 | [`preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/twistor.tex`](../../../preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/build/sections/twistor.tex) | 134 | The twistor space construction and metric recovery. |
