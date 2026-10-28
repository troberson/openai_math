[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 069](../index/algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md)

# 069 — Quantum geometric Langlands at irrational level

[Index page](../index/algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md)

## Original CONTENTS.md summary

The release blurb 

> **069. Global quantum geometric Langlands at irrational level.** Proves the unramified de Rham quantum geometric Langlands equivalence for every connected simple complex algebraic group on every smooth projective connected complex curve, at every shifted level $`c\in\mathbb C\setminus\mathbb Q`$. It identifies the full derived categories of twisted D-modules for the group and its Langlands dual, retaining all global forms and connected components. [S1:1765]

This family ships a single manuscript. The abstract:

The manuscript's abstract 

> We prove the unramified quantum geometric Langlands equivalence for every
connected simple complex algebraic group $G$ and every level
$c\in\mathbb C\setminus\mathbb Q$, including non-real levels. For every smooth
projective connected complex curve $X$, it identifies the full twisted
$D$-module categories on $\mathrm{Bun}_G(X)$ and
$\mathrm{Bun}_{G^\vee}(X)$ at the dual shifted levels $c$ and
$-1/(rc)$, where $r$ is the lacing number. The equivalence uses the given
global forms and includes all connected components. [S2:10–19]

The headline theorem (the unramified equivalence at every irrational
shifted level):

The headline theorem 

> **theorem**
For every $c\in\mathbb C\setminus\mathbb Q$ there is an equivalence of
presentable $\mathbb C$-linear DG categories
$$\label{intro:equivalence}
  D_c(\mathrm{Bun}_G(X))
    \simeq
  D_{-1/(rc)}(\mathrm{Bun}_{G^\vee}(X)).$$
The construction uses the given global forms and all connected components.
It is characterized by the localization–Whittaker comparison of
Section  , including its compatibility with families of
marked points and their collisions. It also intertwines central torsor actions
with the corresponding transgression local systems. [S3:28–41]

## Undergraduate summary

The **quantum geometric Langlands correspondence** is a family of
conjectures connecting two sides of a symmetry. On one side live the
**$G$-bundles** (maps from a curve $X$ to a Lie group $G$, up to
isomorphism, packaged into a geometric object) and their "twisted
$D$-module" categories — a way of doing linear algebra on the space of
$G$-bundles. On the other side sit the bundles for the **Langlands dual
group** $G^\vee$ (a group determined by $G$'s root data, with roles of
"long" and "short" reversed) and their own categories, with the twist
parameter sent to a dual value.

The conjecture asserts that, after a careful setup, these two categories
are **equivalent** — they carry the same information. The "level" $c$
is a number that controls how strongly the twist acts. The classical
versions are proved at special (integer or real) levels; this family
proves the **unramified de Rham version at every irrational level**
$c \in \mathbb{C} \setminus \mathbb{Q}$, including levels that are not
real. "Unramified" means the equivalence respects the natural way of
forgetting the extra structure at marked points, and "de Rham" fixes
the particular geometric realisation of the $D$-module categories. The
"lacing number" $r$ (2 for the $E_8$, $E_7$, $D_{2n}$ series, 1
otherwise) is what appears in the dual level $-1/(rc)$.

## Graduate summary

**The unramified equivalence.** 

> **theorem**
For every $c\in\mathbb C\setminus\mathbb Q$ there is an equivalence of
presentable $\mathbb C$-linear DG categories
$$\label{intro:equivalence}
  D_c(\mathrm{Bun}_G(X))
    \simeq
  D_{-1/(rc)}(\mathrm{Bun}_{G^\vee}(X)).$$
The construction uses the given global forms and all connected components.
It is characterized by the localization–Whittaker comparison of
Section  , including its compatibility with families of
marked points and their collisions. It also intertwines central torsor actions
with the corresponding transgression local systems. [S3:28–41]

For every $c \in \mathbb{C} \setminus \mathbb{Q}$ there is an
equivalence of presentable $\mathbb{C}$-linear DG categories
$D_c(\mathrm{Bun}_G(X)) \simeq
D_{-1/(rc)}(\mathrm{Bun}_{G^\vee}(X))$, where $r$ is the lacing
number. The equivalence is compatible with the given global forms and
all connected components, is characterized by the
localization–Whittaker comparison (section 13), and intertwines central
torsor actions with the corresponding transgression local systems.

The proof runs through a long chain of comparison theorems laid out in
the thirteen sections: foundations and the de Rham model (sections
2–3), the Whittaker and deformation reduction (sections 4–5), the
Plancherel identity (section 6), the loop-category and $W$-algebra
machinery (sections 7–8, with the common Whittaker target theorem at
`08-w-algebras.tex` line 712), the local comparison and period
results (sections 9–12), and the final equivalence and its
compatibility (section 13, theorems at lines 256 and 423). The
localization comparison theorem (`10-localization.tex` line 45) and the
pseudoidentity equivalence (`03-pseudoidentity.tex` line 23) are the two
structural lemmas the equivalence is built on.

## history of the conjecture

The **quantum geometric Langlands program** (Beilinson–Drinfeld,
Gaitsgory, and the surrounding work of the 2000s–2020s) seeks to make
precise, in derived algebraic geometry, the duality between the
category of $G$-bundles with $D$-modules of level $c$ and the
category of $G^\vee$-bundles of the dual level. Gaitsgory's formulation
expresses it as an equivalence of sheaves on the **spectral
Langlands** side. The integer-level and real-level cases have partial
results in the literature (the local Langlands side, and the global
version for specific groups at critical level). This family claims the
**unramified de Rham version at every irrational level** for every
connected simple complex group and every smooth projective connected
curve, retaining all global forms and connected components — the
broadest single-level statement in the family.

## Consequences

**The unramified de Rham quantum geometric Langlands equivalence** at
every irrational shifted level $c \in \mathbb{C} \setminus \mathbb{Q}$,
for every connected simple complex group $G$ and every smooth projective
connected curve $X$, with all global forms and connected components
[S3:28–41].

**The localization–Whittaker comparison** characterizes the equivalence
and is compatible with families of marked points and their collisions
[S3:37–40].

**Central torsor actions intertwine** with the corresponding
transgression local systems [S3:40–41].

## section skeleton

One manuscript, a single `build/main.tex` root with a 13-section flat
input list [S2:21–33] (introduction with the theorem at [S3:28],
foundations, pseudoidentity, Whittaker, deformation, Plancherel, loop
categories, $W$-algebras, local comparison, localization, unipotent
period, Ran period, equivalence), plus a references file. The abstract
is in `main.tex` itself at [S2:10–19].

## Coverage

T0: one manuscript, zero comparator challenges, zero `main_results`
entries, zero scope notes. The ledger reads `paps 1`, `paps_form 0`,
`mainres 0`, `chal 0`, `scope_note 0`, `verification 0`, `trace` empty,
`shapes uniform`, `resolves_named 0` — the simplest tier in the release,
carrying a single `uniform` claim-shape tag. The catalog entry [S4:212]
names the PDF. No Lean formalization, no comparator stub, and no scope
note exist for this family.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 069 at line 1765) |
| S2 | [`preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/build/main.tex`](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/build/main.tex) | 35 | Manuscript: abstract, section inputs |
| S3 | [`preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/build/sections/01-introduction.tex`](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/build/sections/01-introduction.tex) | 189 | Manuscript: headline theorem (unramified quantum geometric Langlands equivalence) |
| S4 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 069 at line 212) |
