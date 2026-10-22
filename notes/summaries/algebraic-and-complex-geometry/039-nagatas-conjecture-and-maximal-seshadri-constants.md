[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 039](../../index/algebraic-and-complex-geometry/039-nagatas-conjecture-and-maximal-seshadri-constants.md)

# 039 — Nagata's conjecture and maximal Seshadri constants

[Index page](../../index/algebraic-and-complex-geometry/039-nagatas-conjecture-and-maximal-seshadri-constants.md)

## Original CONTENTS.md summary

[S1:156] carries the family entry:

> Proves Nagata's strict inequality

[S1:156] carries the first manuscript entry as link text:

> Plane-curve Nagata conjecture

## Undergraduate summary

**Nagata's conjecture** is about plane curves forced through points. Take $r$ points in the complex plane, and a polynomial curve of degree $d$ that passes through them with multiplicities $m_1, \ldots, m_r$ — meaning the curve touches each point to order $m_i$. The conjecture says the total multiplicity cannot be too large: the sum of the $m_i$ is strictly less than $d$ times $\sqrt r$, once $r$ is at least 10. [S14:10]

The first manuscript proves exactly that, for every nonzero effective plane curve, with arbitrary multiplicities, at $r \ge 10$ very general complex points. "We prove that a nonzero effective plane curve of degree" $d$ has total multiplicity strictly below $d\sqrt r$, and the inequality holds simultaneously for all curves, including reducible and nonreduced ones. [S2:35–41]

The second manuscript recasts the same statement in the language of **Seshadri constants**, which measure how positive a line bundle is near a set of points. For a smooth complex projective surface with an ample line bundle, the multipoint Seshadri constant at $r$ very general points equals the upper bound $\sqrt{L^2/r}$ once $r$ is large enough. "This resolves positively the qualitative Nagata–Biran conjecture for surfaces." [S4:7–13]

The third manuscript pushes the conclusion to higher dimensions. For a smooth complex projective variety of dimension $n \ge 3$ with an ample line bundle, there is a threshold beyond which the multipoint Seshadri constant at very general points equals the volume bound $(L^n/r)^{1/n}$. "This establishes the qualitative Nagata–Biran–Szemberg assertion in these dimensions." [S6:49–56]

The fourth manuscript does the same over an algebraically closed field of positive characteristic, at the geometric generic tuple of points, and notes that "The same conclusion holds in dimension two." [S8:8–17]

**Proof sketch.** [S3:31–40]

1. The plane-curve statement is proved for every nonzero effective curve of degree $d$ at $r \ge 10$ very general points, with arbitrary multiplicities, in the strict nonhomogeneous form. [S3:31–40]
2. The surface statement is proved for every smooth integral complex projective surface and every ample line bundle, giving the constant at very general points for all sufficiently large $r$. [S5:31–44]
3. The higher-dimensional statements add a threshold $r_0$ depending on the variety and the line bundle, and the conclusion is stated at very general points over $\mathbb C$ and at the geometric generic tuple in positive characteristic. [S7:29–39]
4. The formalized version states the inequality simultaneously for all curves and multiplicity vectors outside one countable union of proper Zariski-closed exceptional sets with nonempty complement. [S14:12]

## Graduate summary

**The plane-curve theorem.** For a nonzero effective plane curve of degree $d$ at $r \ge 10$ very general complex points, the sum of the multiplicities is strictly less than $d\sqrt r$. The theorem is stated in the strict, nonhomogeneous form, so it covers reducible curves and repeated components, not just irreducible ones. [S3:31–40]

**The surface theorem.** For every smooth integral complex projective surface $S$ and every ample line bundle $L$, the multipoint Seshadri constant at $r$ very general points equals $\sqrt{L^2/r}$ for every sufficiently large integer $r$. [S5:31–44]

**The higher-dimensional theorems.** For dimension $n \ge 3$ over $\mathbb C$, there is a threshold $r_0 = r_0(X,L)$ such that for every $r \ge r_0$ the ordinary multipoint Seshadri constant at $r$ very general points equals the volume bound $(L^n/r)^{1/n}$. [S7:29–39] Over an algebraically closed field of positive characteristic, the same threshold form holds at the geometric generic tuple of $r$ points, and the conclusion is also stated for dimension two. [S9:28–36]

**What the formalization says.** The scope note covers only the two September manuscripts; the two October manuscripts have no scope note. It states the conjecture as the inequality $\sum_i m_i < d\sqrt r$ for a nonzero effective plane curve of degree $d$ with multiplicities at least $m_i$ at $r \ge 10$ very general points. [S14:10]

The formalized result is stated with an exceptional-set structure: "Reducible curves, repeated components, and unequal multiplicities are included, in both effective-curve and homogeneous-polynomial formulations", and the formalization includes the passage from homogeneous effective cycles to equations. [S14:12]

For the maximality question, the formalized result gives, for every $r$ above a threshold depending on $(S,L)$, a countable union of proper closed exceptional sets with nonempty complement, outside which the constant is $\sqrt{L^2/r}$ and the boundary class defining it on the point blowup is nef. The scope note is explicit about the threshold: "The threshold is not explicit or uniform over all surfaces." [S14:16]

**The declarations.** The two formalized declarations are `OAI.Nagata.nagata_conjecture` at `lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean:148` and `OAI.MaximalSeshadri.Geometry.maximalSeshadriConstants` at `lean/OAI/AlgebraicGeometry/Seshadri/Main.lean:25`. The Nagata declaration is typed by a carrier, `FullNagata`, and `nagata_conjecture_coordinates` is discharged by `W13.nagata_full`. Both comparator JSONs declare `status: "proved"` and permit `propext`, `Quot.sound`, and `Classical.choice`. [S15:148]

**Formalization status.** The ledger records family 039 at tier T2: 4 manuscripts, 2 formalized, 1 scope note, 2 comparator challenges, 2 `main_results` entries, 0 reasoning traces, 0 verification bundles. The two formalized manuscripts are the two September-2026 ones; the two October-2026 manuscripts (higher dimensions, positive characteristic) are unformalized, and the scope note names only the September pair. A comparator file is a challenge stub stating the target the release set itself; the proved version, where it exists, lives under `lean/OAI/`. Nothing here proves the formalization elaborates — no Lean or comparator run was performed, which is the standing rule for this catalog.

## History of the conjecture

Nagata's conjecture is a classical statement in the polynomial-division regime: the strict inequality form is the one Nagata posed, and the qualitative maximal-constant form is the Nagata--Biran conjecture for surfaces, extended by Biran--Szemberg to higher dimensions. The four manuscripts in this family state the same inequality in these three registers: plane curves with arbitrary multiplicities, surfaces at very general points, and varieties of dimension at least 3 over $\mathbb C$ and in positive characteristic. [S1:156]

The manuscript READMEs record the citation keys the papers use: `NagataPlaneCurves` for the plane-curve paper, `MaximalSeshadriConstants` for the surface paper, `MaximalMultipointSeshadriHigher` for the higher-dimensional paper, and `MaximalMultipointSeshadriCharP` for the positive-characteristic paper. [S10:11–12]

## Consequences

The consequence the manuscripts state for themselves is that the qualitative form of the conjecture is settled in the ranges they cover: the strict plane-curve inequality, the maximal constant for surfaces, and the maximal constant in dimension at least 3 over the complex numbers and in positive characteristic. [S6:49–56]

The formalization's record adds a structural detail the manuscripts' statements do not: the inequality and the maximality result are stated outside a countable union of proper Zariski-closed exceptional sets with nonempty complement, and the threshold for the surface case is neither explicit nor uniform over all surfaces. That is the part of the claim the Lean code carries, and the scope note is what records it. [S14:16]

The two October manuscripts are the part of the family with no formalization and no scope note, so their claims are readable only from the manuscripts.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 156 |
| S2 | [`preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/main.tex`](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/main.tex) | 50 | Abstract, lines 35–41 |
| S3 | [`preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/sections/introduction.tex`](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/sections/introduction.tex) | 143 | Main theorem, lines 31–40 |
| S4 | [`preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/main.tex`](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/main.tex) | 26 | Abstract, lines 7–13 |
| S5 | [`preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/sections/introduction.tex`](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/sections/introduction.tex) | 167 | Main theorem, lines 31–44 |
| S6 | [`preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/main.tex`](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/main.tex) | 65 | Abstract, lines 49–56 |
| S7 | [`preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/sections/introduction.tex`](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/sections/introduction.tex) | 180 | Main theorem, lines 29–39 |
| S8 | [`preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/build/main.tex`](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/build/main.tex) | 28 | Abstract, lines 8–17 |
| S9 | [`preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/build/sections/01-introduction.tex`](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/build/sections/01-introduction.tex) | 171 | Main theorem, lines 28–36 |
| S10 | [`preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/README.md`](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/README.md) | 18 | The manuscript's citation record, lines 11–12 |
| S11 | [`preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/README.md`](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/README.md) | 18 | The manuscript's citation record, lines 11–12 |
| S12 | [`preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/README.md`](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/README.md) | 16 | The manuscript's citation record, lines 11–12 |
| S13 | [`preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/README.md`](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/README.md) | 16 | The manuscript's citation record, lines 11–12 |
| S14 | [`lean/docs/039.md`](../../../lean/docs/039.md) | 23 | Scope note: formalized claims, exceptional sets, retained hypotheses |
| S15 | [`lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean`](../../../lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean) | 169 | `nagata_conjecture` declaration, line 148 |
| S16 | [`lean/OAI/AlgebraicGeometry/Seshadri/Main.lean`](../../../lean/OAI/AlgebraicGeometry/Seshadri/Main.lean) | 42 | `maximalSeshadriConstants` declaration, line 25 |
