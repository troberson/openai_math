Notes / Summaries / Algebra / [Family 199](../../index/algebra/199-counterexamples-to-conjectures-of-auslander-reiten-and-tachikawa.md)

# 199 — Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama

## Original CONTENTS.md summary

[S1:479] carries the family entry:

> Constructs finite-dimensional algebras over a characteristic-two rational-function field that disprove the Auslander--Reiten and Gorenstein-projective conjectures, and Tachikawa's second conjecture. An associated endomorphism algebra also disproves the classical, generalized and strong Nakayama conjectures, the Auslander--Gorenstein conjecture, and the Wakamatsu tilting conjecture. The counterexamples persist under every extension of the base field.

The entry links the two manuscripts as "Auslander–Reiten counterexample"
and "Tachikawa’s second conjecture" [S1:479].

The first manuscript's title is `An explicit counterexample to the Auslander-Reiten conjecture` [S2:1].

The README dates it September 23, 2026 [S2:5].

The second manuscript's title is `A counterexample to Tachikawa's second conjecture` [S15:1].

The README dates it September 23, 2026 [S15:5].

## Undergraduate summary

An **Artin algebra** is a finite-dimensional algebra over a field. A
**module** is a vector space on which the algebra acts, and
**$\Ext^i(M,N)$** measures how far a pair of modules is from being
projective in degree $i$. A module is **projective** when it behaves like a
free module.

The Auslander--Reiten conjecture asks whether vanishing extensions force a
module to be projective. [S4:3–4] states the question: "The Auslander--Reiten
conjecture asks whether a finitely generated module $M$ over an Artin
algebra $R$ must be projective when" — the display gives the vanishing
condition.

The first manuscript's abstract states the counterexample. [S3:48–54] says:
"We disprove the Auslander--Reiten conjecture for Artin algebras. We
construct a finite-dimensional algebra $\Lambda$ over
$k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective left
module $Z$ such that $\Ext^i_\Lambda(Z,Z)=\Ext^i_\Lambda(Z,\Lambda)=0$ for
every $i>0$. The module is Gorenstein-projective, so the same example also
disproves the Gorenstein-projective conjecture. Both counterexamples persist
after every extension of $k$."

The main theorem names the algebra and the module. [S4:26–29] gives the
setup: "Let $\kk=\mathbb F_2(q,H_1,H_2)$, where $q,H_1,H_2$ are
algebraically independent. There exist a finite-dimensional $\kk$-algebra
$\Lambda$ and a finite-dimensional nonprojective left $\Lambda$-module $Z$
such that" — the display gives the vanishing.

The theorem's structural assertions follow. [S4:34–37] states them: "The
module $Z$ is Gorenstein-projective. The semisimple quotient is
$\Lambda/\rad\Lambda\simeq\kk^8$, so the algebra is split with eight
isomorphism classes of simple modules; also $\rad(\Lambda)^4\ne0$. These
conclusions persist after every field extension of $\kk$."

The second manuscript attacks Tachikawa's second conjecture. [S16:54–61]
states the result: "We disprove Tachikawa's second conjecture by
constructing a finite-dimensional symmetric algebra over
$k=\mathbb F_2(q,H_1,H_2)$ with a finite-dimensional nonprojective module
whose self-extension groups vanish in every positive degree. The associated
endomorphism algebra also gives counterexamples to the classical,
generalized, and strong Nakayama conjectures, the Auslander--Gorenstein
conjecture, and the Wakamatsu tilting conjecture. These conclusions persist
after every extension of $k$."

A **symmetric** algebra is one isomorphic to its own dual as a bimodule,
and such an algebra is self-injective. [S17:19–21] gives the definition:
"Write $D=\Hom_k(-,k)$. An algebra $A$ is \emph{symmetric} if $A\simeq DA$
as $A$-bimodules; in particular, a symmetric algebra is self-injective. We
prove the following result in this class."

The second manuscript's theorem is the symmetric case. [S17:29–31] gives
the setup: "There exist a finite-dimensional associative unital symmetric
$k$-algebra $A$ and a finite-dimensional unital left $A$-module $M$ such
that $M$ is nonprojective and" — the display gives the vanishing.

Because a symmetric algebra is self-injective, the second manuscript's
module settles the Auslander--Reiten conjecture in that class too.
[S17:38–41] says: "Since $A$ is self-injective, the same module satisfies
$\Ext_A^i(M,M\oplus A)=0$ for every $i>0$. Thus Theorem~\ref{thm:main} also
gives a symmetric counterexample to the Auslander--Reiten conjecture."

## Graduate summary

The first manuscript also states the Gorenstein-projective form of the
conjecture. [S4:18–20] gives it: "The \emph{Gorenstein-projective
conjecture} asks whether a finite Gorenstein-projective module $M$ with
$\Ext_R^i(M,M)=0$ for every $i>0$ must be projective" — the sentence
continues into a citation.

The ambient algebra is not assumed to be Gorenstein, and total acyclicity
gives $\Ext_R^i(M,R)=0$ for $i>0$, so the Gorenstein-projective conjecture
is precisely the restriction of the Auslander--Reiten conjecture to
Gorenstein-projective modules [S4:21–24].

The generator formulation is the bridge to the Nakayama conjectures, and
the counterexample fails it as well. [S4:60–63] states it: "The generator
formulation also fails: $Z\oplus\Lambda$ is a nonprojective generator with
no positive self-extensions. Indeed Ext is additive in both arguments, and
all positive Ext groups with first argument $\Lambda$ vanish."

The construction runs through the conversion principle [S7:1], built on the
stable category and its shift [S6:1]. The symmetric algebra with its
degree-three class is [S8:1], the complete resolution of the simple module
is [S9:1], the two cones and their maps are [S10:1], lifting maps through
the cones is [S11:1], and the branch case analysis is [S12:1]. The appendix
specifies the finite cochain [S14:1], and the consequences section carries
the radical structure [S13:1].

The conversion principle is stated before the example. [S4:137–139] gives
it: "The proof has two parts. First we give a conversion principle: a
suitable stable map $v:X\to F\otimes_A X$ over a symmetric algebra $A$
produces a module over" — the display gives the triangular algebra.

The construction itself is named in the introduction. [S4:149–156] gives
it: "We then build the required $A,F,X,v$. Write $D$ for the $\kk$-linear
dual. A ten-dimensional algebra $C$ has a simple module $s$ whose Ext
groups are especially sparse. Passing to its symmetric trivial extension
$T=C\ltimes DC$ produces $\Ext_T^*(s,s)=\kk[\tau]$ with $|\tau|=3$. An
explicit Hochschild cocycle realizes $\tau$ and supplies a homotopy
compatible with twists of $T$. For $A=T\otimes T$ and $X=s\otimes s$, the
nonnegative self-extension algebra is $\kk[\tau_1,\tau_2]$."

The reduction between the two conjectures is the reason one construction
refutes both. [S4:126–130] records it: "Tachikawa's second conjecture is
the self-injective case of \eqref{eq:arc}. Enomoto proves that this
conjecture for the two-fold trivial extension of an Artin algebra implies
the Auslander--Reiten conjecture for that algebra" — the sentence continues
into the reduction.

The second manuscript's route is a transfer principle. [S17:106–111]
states it: "Two steps organize the proof. First,
Proposition~\ref{tr:transfer} gives a general transfer principle. For a
finite-dimensional algebra $\Lambda$, a doubly infinite exact complex $P_Z$
of finite projective $\Lambda$-modules is \emph{totally acyclic} if
$\Hom_\Lambda(P_Z,\Lambda)$ is also exact."

The transfer machinery is the transfer section [S19:1], built on the
homological criterion [S18:1], the algebra [S20:1], the stable category
[S21:1], the bimodule and its maps [S22:1], and the triangular algebra
[S23:1].

The second manuscript draws an algebra consequence from its module.
[S24:4–7] explains the route: "The symmetric pair constructed in
Theorem~\ref{thm:main} has a self-orthogonal generator $A\oplus M$. The
classical relation between such generators and dominant dimension turns the
module counterexample into an algebra whose entire regular injective
resolution is projective."

The scope note records what the formalization carries. [S26:10] gives the
first result: "The Auslander–Reiten conjecture predicts that a finitely
generated module $M$ over an Artin algebra $A$ is projective if
$\mathrm{Ext}^i_A(M,M\oplus A)=0$ for every $i>0$. The formalized
counterexample is a finite-dimensional algebra over
$k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective
Gorenstein-projective module with this vanishing."

The scope note's second paragraph records the structural facts. [S26:12]
says: "It also establishes $A/\mathrm{rad}\,A\cong k^8$,
$(\mathrm{rad}\,A)^4\ne0$, and preservation of the listed properties after
every field extension. The Tachikawa companion is separate."

The scope note's third paragraph gives the Tachikawa result. [S26:14]
states it: "Tachikawa's second conjecture predicts that a finite-dimensional
module over a finite-dimensional self-injective algebra is projective if all
its positive-degree self-Ext groups vanish. The formalized counterexample
gives a finite-dimensional symmetric algebra over
$\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective module $M$
with $\mathrm{Ext}^i(M,M)=0$ for every $i>0$."

The scope note names what the formalization leaves out. [S26:16] says: "The
later field-extension, endomorphism-algebra, and related homological
consequences are not included."

The two declarations are the quantified forms. `OAI.ArExplicit.main` at
[S27:738] is the Auslander--Reiten counterexample.
`OAI.Tachikawa.main_theorem` at [S28:293] is the Tachikawa counterexample.

The two comparator configs state the targets the release set itself, and
each is a stub. [S29:71] carries `sorry`; [S30:33] carries `sorry`. The
scope note's comparator table links `AuslanderReiten.lean` and
`Tachikawa.lean`, one per formalized result.

## History of the conjecture

The Auslander--Reiten conjecture was proved in several classes before this
result. [S4:71–73] records the first: "Huneke and Leuschke proved the
conjecture for excellent commutative Cohen--Macaulay normal domains
containing the rational numbers, among other classes".

The radical-cube-zero case was settled for split algebras. [S4:88–90]
records it: "Zhang and Zhou subsequently proved the conjecture for split
finite-dimensional algebras with radical cube zero". The construction here
is outside that class: [S4:93–94] says "The algebra constructed here has
nonzero fourth radical power, as proved in Proposition~\ref{prop:radical}."

The second manuscript names the earlier near-miss. [S17:44–46] records it:
"Schulz's earlier example of a nonprojective module without positive
self-extensions uses an algebra over a skew field, outside the" — the
sentence continues into the finite-dimensional-over-a-field setting.

The second manuscript also names the class results for the self-injective
case. [S17:73–74] records: "Zhang and Zhou prove the self-injective case
for split algebras with radical cube zero".

The reduction between the conjectures is recorded in both manuscripts, at
[S4:126–130] and [S17:84–86].

`notes/tables/conjecture-standing.tsv` carries no row for family 199, so
the prior on the conjectures' standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

Both conjectures fail for Artin algebras. [S4:40–42] states the reach:
"Thus both conjectures fail for Artin algebras, including finite-dimensional
algebras over an algebraically closed field of characteristic two: one can
extend scalars to an algebraic closure of $\kk$."

The second manuscript's symmetric algebra gives the self-injective case as
well [S17:38–41], and its endomorphism-algebra consequence turns the module
counterexample into an algebra whose regular injective resolution is
entirely projective [S24:4–7].

The scope note records the same reach for the formalized result, including
the structural facts and the persistence after field extension [S26:12],
and it names the endomorphism-algebra consequence as outside the
formalization [S26:16].

The two manuscripts share the characteristic-two field with three
algebraically independent parameters, and the second manuscript states that
it uses the same ten-dimensional starting algebra as the companion article
[S17:98–101].

The release's own record is source-level. The scope note says the formalized
counterexamples exist and names their declarations; the two comparator
configs carry `sorry`; no Lean run in this repository proves either
elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `overview.tex` | 859 | Family entry, line 479 |
| S2 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/README.md` | 17 | Manuscript 1 title, date, citation |
| S3 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/main.tex` | 72 | Abstract, lines 48–54 |
| S4 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/01-introduction.tex` | 268 | Theorem, history, construction outline |
| S5 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/refs.bib` | 318 | Bibliography entries |
| S6 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/01-stable.tex` | 67 | The stable category and its shift |
| S7 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/02-conversion.tex` | 308 | The conversion principle |
| S8 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/03-algebra.tex` | 234 | A symmetric algebra and a degree-three class |
| S9 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/04-resolution.tex` | 246 | The complete resolution of the simple module |
| S10 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/05-cones.tex` | 323 | The two cones and their maps |
| S11 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/06-lift.tex` | 286 | Lifting maps through the cones |
| S12 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/07-branches.tex` | 233 | The branch case analysis |
| S13 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/08-consequences.tex` | 79 | The radical structure and the consequences |
| S14 | `preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/09-cochain.tex` | 126 | The complete degree-three cochain |
| S15 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/README.md` | 17 | Manuscript 2 title, date, citation |
| S16 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/paper.tex` | 74 | Abstract, lines 54–61 |
| S17 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/introduction.tex` | 357 | Theorem, history, construction outline |
| S18 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/homological.tex` | 466 | The homological criterion |
| S19 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/transfer.tex` | 132 | The trivial extension |
| S20 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/algebra.tex` | 339 | The algebra |
| S21 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/stable.tex` | 319 | The stable category |
| S22 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/bimodule.tex` | 696 | The bimodule and its maps |
| S23 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/triangular.tex` | 320 | The triangular algebra |
| S24 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/consequences.tex` | 305 | The endomorphism algebra and consequences |
| S25 | `preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/refs.bib` | 398 | Bibliography entries |
| S26 | `lean/docs/199.md` | 23 | Scope note |
| S27 | `lean/OAI/Algebra/AuslanderReiten/All.lean` | 744 | `ArExplicit.main` |
| S28 | `lean/OAI/RingTheory/Tachikawa/Counterexample.lean` | 301 | `Tachikawa.main_theorem` |
| S29 | `lean/ComparatorChallenges/AuslanderReiten.lean` | 77 | Stub, `sorry` at line 71 |
| S30 | `lean/ComparatorChallenges/Tachikawa.lean` | 39 | Stub, `sorry` at line 33 |

## Links

- [S1](../../../overview.tex)
- [S2](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/README.md)
- [S3](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/main.tex)
- [S4](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/01-introduction.tex)
- [S5](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/refs.bib)
- [S6](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/01-stable.tex)
- [S7](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/02-conversion.tex)
- [S8](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/03-algebra.tex)
- [S9](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/04-resolution.tex)
- [S10](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/05-cones.tex)
- [S11](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/06-lift.tex)
- [S12](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/07-branches.tex)
- [S13](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/08-consequences.tex)
- [S14](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/09-cochain.tex)
- [S15](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/README.md)
- [S16](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/paper.tex)
- [S17](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/introduction.tex)
- [S18](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/homological.tex)
- [S19](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/transfer.tex)
- [S20](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/algebra.tex)
- [S21](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/stable.tex)
- [S22](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/bimodule.tex)
- [S23](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/triangular.tex)
- [S24](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/consequences.tex)
- [S25](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/refs.bib)
- [S26](../../../lean/docs/199.md)
- [S27](../../../lean/OAI/Algebra/AuslanderReiten/All.lean)
- [S28](../../../lean/OAI/RingTheory/Tachikawa/Counterexample.lean)
- [S29](../../../lean/ComparatorChallenges/AuslanderReiten.lean)
- [S30](../../../lean/ComparatorChallenges/Tachikawa.lean)
