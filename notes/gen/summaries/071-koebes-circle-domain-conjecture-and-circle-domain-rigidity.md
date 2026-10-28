[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 071](../index/real-and-complex-analysis/071-koebes-circle-domain-conjecture-and-circle-domain-rigidity.md)

# 071 — Koebe's circle-domain conjecture and circle-domain rigidity

[Index page](../index/real-and-complex-analysis/071-koebes-circle-domain-conjecture-and-circle-domain-rigidity.md)

## Original CONTENTS.md summary

The release blurb 

> **071. Koebe’s circle-domain conjecture.** Resolves the existence part of Koebe's circle-domain conjecture: every domain in the Riemann sphere is conformally equivalent to a domain whose complementary components are round disks or points. It also proves that circle domains with conformally removable boundary are rigid, meaning every conformal equivalence to another circle domain is Möbius, establishing this direction of the He–Schramm conjecture. [S1:1781]

This family ships **two** companion manuscripts answering the two halves
of the same conjectural program. The uniformization half (every domain
is a circle domain):

Manuscript 2, Koebe's circle-domain conjecture 

> We prove that every domain in the Riemann sphere is conformally equivalent
to a circle domain, resolving Koebe's circle-domain conjecture positively. [S4:52–55]

The rigidity half (circle domains with removable boundary are rigid):

Manuscript 1, removable boundaries and rigidity 

> We prove that a circle domain with conformally removable boundary is
conformally rigid, with no restriction on the number of complementary
components. This establishes the removability-to-rigidity direction of
the He–Schramm Conjecture. [S2:53–58]

## Undergraduate summary

A **circle domain** is a region of the Riemann sphere whose boundary
pieces are, individually, either round disks or single points. **Koebe's
circle-domain conjecture** (the "existence" part) asks: is *every*
domain in the Riemann sphere conformally equivalent — reshaped by a
biholomorphic map — to some circle domain? The "rigidity" part, tied to
the **He–Schramm conjecture**, asks something different: if two circle
domains are conformally equivalent and the boundary of the source is
**conformally removable** (the property that any conformal self-map of
the sphere agreeing with the identity off the boundary is itself a
Möbius transformation), then must that equivalence be a Möbius
transformation? In plain terms: a circle domain with a "tame" boundary
has no hidden conformal automorphisms — the only way to conformally map
it onto another circle domain is a projective symmetry of the sphere.

This family proves both: manuscript 2 gives every domain a circle-domain
representative (resolving Koebe's conjecture), and manuscript 1 proves
the removable-boundary rigidity statement (the He–Schramm direction).
The two are linked through the same circle-domain geometry; the
comparator stub [S7] states both as a single challenge.

## Graduate summary

**Circle-domain uniformization.** 

> **Theorem 1.1**
Every nonempty connected open set $G\subset\widehat{\mathbb C}$ is conformally equivalent
to a circle domain. [S5:9–12]

Every nonempty connected open set $G \subset \widehat{\mathbb C}$ is
conformally equivalent to a circle domain. The difficulty, as the
manuscript's introduction puts it, is to control **all** complementary
components at once — there may be uncountably many, with no regularity
or separation, and a limiting component can contain more than the disk
obtained by following one of its finite approximations.

**Removable-boundary rigidity.** 

> **Theorem 1.1**
Every circle domain with conformally removable boundary is conformally
rigid. More explicitly, if $\Omega,\Omega'\subset\widehat{\mathbb C}$ are circle
domains, $\partial\Omega$ is conformally removable, and
$f\colon\Omega\to\Omega'$ is a conformal equivalence, then there is a
Möbius transformation $M$ such that $f=M|_\Omega$. [S3:22–28]

Every circle domain with conformally removable boundary is conformally
rigid: if $\Omega, \Omega' \subset \widehat{\mathbb C}$ are circle
domains, $\partial \Omega$ is conformally removable, and
$f : \Omega \to \Omega'$ is a conformal equivalence, then $f$ is the
restriction of a Möbius transformation. The theorem allows arbitrary
cardinality of the complementary component set, and the required
boundary control is a conclusion of the argument — no boundary
extension of $f$ is part of the hypothesis.

## history of the conjecture

**Koebe's circle-domain conjecture** (the "existence" part) asks
whether every domain in the Riemann sphere is conformally equivalent to
a circle domain; the classical Koebe uniformization theorem gives a
round disk for simply connected planar domains, and the circular
version for finitely connected domains was proved by Koebe (1907),
Teichmüller (1935), and others. The **unrestricted** form — arbitrary
domains, uncountably many complementary components — is the open
direction manuscript 2 closes. **The He–Schramm conjecture** (He and
Schramm, 1990s) concerns rigidity of circle domains: a conformal
equivalence between two circle domains, with a conformally removable
source boundary, should be a Möbius transformation. The removability
hypothesis is the precise condition under which the boundary data
determine the map. Manuscript 1 proves this direction, with no bound on
the number of complementary components.

## Consequences

**Koebe's circle-domain conjecture** is resolved positively in its
unrestricted form: every domain in the Riemann sphere is conformally
equivalent to a circle domain [S5:9–12].

**The removability-to-rigidity direction of the He–Schramm
conjecture**: a circle domain with conformally removable boundary is
conformally rigid — every conformal equivalence to another circle
domain is a Möbius transformation on the source [S3:22–28].

**No bound on complementary components** is needed in the rigidity
statement; the boundary control is a conclusion, not a hypothesis
[S3:30–31].

## section skeleton

Two manuscripts, each a single `build/main.tex` root with a flat
section list.

Manuscript 1 [S2:53–58] `build/main.tex`: abstract at [S2:53–58], sections
for introduction (theorem at [S3:22]), preliminaries, models,
conductivity, Sobolev, traces, and rigidity.

Manuscript 2 [S4:52–55] `build/main.tex`: abstract at [S4:52–55], sections
for introduction (theorem at [S5:9]), topology, transfer, barriers,
laws, selection, streams, and hyperbolic surfaces.

## Coverage

T2: two manuscripts, zero formalized, one comparator challenge, one
scope note, zero `main_results` entries. The ledger reads `paps 2`,
`paps_form 0`, `mainres 0`, `chal 1`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes resolution|bound`, `resolves_named 1`. The scope
note describes the *intended* formalization target:

> The formalization proves the removability-to-rigidity direction of the He–Schramm conjecture. If a circle domain has conformally removable boundary, then every conformal equivalence from it to another circle domain agrees on the source with a Möbius transformation. There is no bound on the number of complementary components. [S6:10]

The comparator stub [S7] states both theorems as a single challenge:
`koebe_circle_domain` [S7:62] and `removability_implies_rigidity`
[S7:68], each ending in `sorry` (at [S7:66] and [S7:73] respectively).
There is no `main_results` entry and no landed Lean proof for this
family — the scope note states the target, and the comparator states
the target, but neither has a proved version. The catalog entry
[S8:216] names both PDFs.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 071 at line 1781) |
| S2 | [`preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/build/main.tex`](../../../preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/build/main.tex) | 68 | Manuscript 1: abstract, section inputs (circle-domain rigidity) |
| S3 | [`preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/build/sections/introduction.tex`](../../../preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/build/sections/introduction.tex) | 145 | Manuscript 1: main theorem (removable-boundary rigidity) |
| S4 | [`preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/build/main.tex`](../../../preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/build/main.tex) | 71 | Manuscript 2: abstract, section inputs (circle-domain uniformization) |
| S5 | [`preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/build/sections/00-introduction.tex) | 189 | Manuscript 2: main theorem (circle-domain uniformization) |
| S6 | [`lean/docs/071.md`](../../../lean/docs/071.md) | 21 | Scope note (the intended formalization target: removability-to-rigidity plus the circle-domain theorem) |
| S7 | [`lean/ComparatorChallenges/KoebeCircleDomains.lean`](../../../lean/ComparatorChallenges/KoebeCircleDomains.lean) | 79 | Comparator stub (both theorems end in sorry) |
| S8 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 071 at line 216) |
