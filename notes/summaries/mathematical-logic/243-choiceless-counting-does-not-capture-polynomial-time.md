[Notes](../../README.md) / [Summaries](../README.md) / [Mathematical logic](../../index/disciplines/mathematical-logic.md) / [Family 243](../../index/mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md)

# 243 — Choiceless counting does not capture polynomial time

[Index page](../../index/mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md)

## Original CONTENTS.md summary

 carries the family entry:

> consistency of a linear system over $\mathbb F_3$ defines a polynomial-time query on unordered finite structures that choiceless polynomial time with counting cannot express. A separate result shows that adding witnessed symmetric choice strictly increases expressive power. Both separations hold for the full counting formalism, allowing hereditarily finite sets of arbitrary finite rank. [S1:571]

The entry links the two manuscripts as "Failure to capture polynomial time [S1:571]"
and "Witnessed symmetric choice [S1:571]" .

The first manuscript's title is "Choiceless polynomial time with counting does not capture polynomial time [S2:1]" .

The second manuscript's title is "Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting [S9:1]" .

## Undergraduate summary

A query on finite structures has to be invariant under isomorphism, and the
algorithm must not depend on an order the structure does not supply.
[S6:3–4] opens with the definition: "A query on finite relational structures
is a property unchanged by isomorphism." The formalism at issue is choiceless
polynomial time with counting, which works on the hereditarily finite sets
built from the input elements.

The formalism's defining constraint is that it cannot pick an order.
[S6:19–20] states it: "Its operations commute with input automorphisms and do
not provide an arbitrary choice of an ordering." The manuscript adds that the
counting operation is included and the set rank is unbounded: [S6:23–24] says
"In particular, $\mathrm{CPT}$ here always includes counting and has no imposed bound
on the rank of its sets."

The first manuscript's theorem names the separating query. [S6:81–86] states
it: "The query $Q$ on all finite structures in the fixed vocabulary $\tau$ of
eight binary relations is isomorphism-invariant and decidable in
deterministic polynomial time, but is not definable in full choiceless
polynomial time with counting." The query asks whether a linear system over
the three-element field is consistent, and its abstract says the same:
[S3:36–40] gives "A linear-consistency query over $\mathbb F_3$ in a fixed
binary vocabulary is decidable in polynomial time but not in the full counting
formalism."

The second manuscript adds witnessed symmetric choice and shows the formalism
gets stronger. [S10:65–68] gives its abstract: "We prove that witnessed
symmetric choice strictly increases the expressive power of choiceless
polynomial time with counting. A fixed sentence with one witnessed-choice
occurrence defines a Boolean query on every finite input that is not definable
in the original counting formalism."

The separation is stated as a strict inclusion. [S13:44] states the half that
matters: "no \(\mathrmCPT\) sentence over \(\tau\) has the same true-model class. [S13:44]"

The choiceless side keeps its full power. [S13:46–47] says: "The \(\CPT\) sentences in \textup{(ii)} may use counting
and hereditarily finite sets of unrestricted finite rank."

## Graduate summary

The scope note records what the formalization carries, and its wording is
narrower than the manuscript's. [S15:10] gives the noncapture result: "The
formalized result separates polynomial time from choiceless polynomial time
with counting. It gives an explicit query on finite structures with eight
relations that is invariant under isomorphism and decidable in polynomial
time, but is not definable in the stated hereditarily finite-set language with
cardinality and polynomial bounds on stages and intermediate objects. The
query applies to all finite inputs without a promise. The separate
witnessed-symmetric-choice result is not included."

The scope note's second paragraph carries the second result. [S15:12] gives
it: "The formalization proves that witnessed symmetric choice strictly
increases the expressive power of choiceless polynomial time with counting. It
constructs one fixed sentence with exactly one witnessed-choice occurrence
that gives a Boolean answer on every finite input, while no sentence of the
original counting formalism defines the same class of inputs."

The scope note's first paragraph names the resource bounds the formalized
language imposes, which the manuscript's own introduction does not: the
formalized claim is about a language with cardinality and polynomial bounds on
stages and intermediate objects, not the unbounded-rank statement the
manuscript proves. That is the gap between the manuscript theorem and the
formalized statement.

The declarations are the quantified forms. `OAI.CPTSeparation.main` at
[S16:1] is typed `NonCaptureStatement`, and the file's import closure carries
the query, its polynomial decidability, and the nondefinability.
`OAI.WitnessedChoice.main` at [S17:12] is typed `BGS.MainStatement`, an opaque
declaration whose content lives in the carrier.

The carrier is the statement the declaration proves. [S18:596] defines it:
`MainStatement` is the existence of a sentence with one witnessed symmetric
choice operator, Boolean on all inputs, whose true-model class differs from
every choiceless sentence's. The witness is a single grid pair, and the proof
reads the program's evaluation on the grid input.

The two comparator configs state the targets the release set itself, and each
is a stub. [S19:554] carries `sorry`; [S20:470] carries `sorry`. The JSON
targets name the declarations: `ChoicelessPolynomialTime` asks for
`OAI.CPTSeparation.main` in `OAI.ModelTheory.Choiceless.Separation`, and
`WitnessedChoice` asks for `OAI.WitnessedChoice.main` in
`OAI.Computability.WitnessedChoice.Main`. Both permit the same three axioms:
`propext`, `Quot.sound`, `Classical.choice`.

The separation section is where the nondefinability is proved, and the lower
bound section is where the second manuscript's grid construction carries the
weight. [S8:1] and [S14:1] name them, and the two manuscripts each ship a
figure of the construction, [S5:1] and [S12:1].

## History of the conjecture

The capture question starts with ordered structures. [S7:7–8] records the
logic-side formulation: "Gurevich formulated the question in terms of a logic
capturing polynomial time and conjectured that no such logic exists". The
history section cites Gurevich's 1988 paper for it, and the same section
states the scope of what the manuscript leaves open.

The choiceless formalism is Blass, Gurevich and Shelah's. [S7:12–14] gives
the introduction: "Blass, Gurevich and Shelah introduced choiceless polynomial
time to study computation on unordered structures using hereditarily finite
sets rather than arbitrary choices of an ordering".

The conjecture the first manuscript confirms is theirs. [S7:14–16] says
"Their original 1997 preprint explicitly conjectured that the extension by
counting is still a proper fragment of polynomial time", with the bibliography
entries at [S4:1] and [S11:2].

The second manuscript cites the same two papers, at [S11:16], and its
introduction opens by naming the expressiveness question the theorem answers.

`notes/tables/conjecture-standing.tsv` carries no row for family 243, so the
prior on the conjecture's standing is not recorded in the release's own
reading. The claim in the entry is the record.

## Consequences

The noncapture result closes the counting extension of the formalism.
[S6:81–86] proves the query is polynomial-time and not definable, and the
history section names what remains: excluding choiceless polynomial time with
counting as a candidate leaves the search for a logic that captures polynomial
time on unordered structures unresolved.

The second result separates the formalism from its extension. [S13:44] proves
the separation and [S13:46–47] states that the choiceless side keeps counting
and unbounded rank, so the added witnessed symmetric choice operator is what
makes the difference. The witness is one occurrence, which is the sharpest
form of the separation.

The two results sit in the same family because they share the vocabulary.
[S15:10] and [S15:12] describe queries in a fixed vocabulary of eight
relations, and the scope note links two comparator configs, one per result.

The release's own record is source-level. The scope note says the formalized
claims exist and names their declarations; the two comparator configs carry
`sorry`; no Lean run in this repository proves any of them elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 571 |
| S2 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/README.md`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/README.md) | 17 | Manuscript 1 title, date, citation |
| S3 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/main.tex`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/main.tex) | 55 | Abstract, lines 35–41 |
| S4 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/references.bib`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/references.bib) | 324 | Bibliography entries |
| S5 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/figures/proof-map.tex`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/figures/proof-map.tex) | 30 | Proof-map figure |
| S6 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/00-introduction.tex) | 233 | Formalism, main theorem |
| S7 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/01-history.tex`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/01-history.tex) | 112 | History of the capture question |
| S8 | [`preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/07-separation.tex`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/sections/07-separation.tex) | 44 | The nondefinability proof |
| S9 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/README.md`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/README.md) | 17 | Manuscript 2 title, date, citation |
| S10 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/main.tex`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/main.tex) | 84 | Abstract, lines 64–69 |
| S11 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/references.bib`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/references.bib) | 226 | Bibliography entries |
| S12 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/figures/grid-cycle.tex`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/figures/grid-cycle.tex) | 38 | Grid-cycle figure |
| S13 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/sections/00-introduction.tex) | 215 | Main theorem |
| S14 | [`preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/sections/08-cpt-lower-bound.tex`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/sections/08-cpt-lower-bound.tex) | 501 | The lower-bound proof |
| S15 | [`lean/docs/243.md`](../../../lean/docs/243.md) | 19 | Scope note |
| S16 | [`lean/OAI/ModelTheory/Choiceless/Separation.lean`](../../../lean/OAI/ModelTheory/Choiceless/Separation.lean) | 28 | `CPTSeparation.main` |
| S17 | [`lean/OAI/Computability/WitnessedChoice/Main.lean`](../../../lean/OAI/Computability/WitnessedChoice/Main.lean) | 43 | `WitnessedChoice.main` |
| S18 | [`lean/OAI/Computability/WitnessedChoice/Model.lean`](../../../lean/OAI/Computability/WitnessedChoice/Model.lean) | 604 | `MainStatement` carrier |
| S19 | [`lean/ComparatorChallenges/ChoicelessPolynomialTime.lean`](../../../lean/ComparatorChallenges/ChoicelessPolynomialTime.lean) | 560 | Stub, `sorry` at line 554 |
| S20 | [`lean/ComparatorChallenges/WitnessedChoice.lean`](../../../lean/ComparatorChallenges/WitnessedChoice.lean) | 474 | Stub, `sorry` at line 470 |

## Bibliography

- Andreas Blass, Yuri Gurevich, Saharon Shelah, Choiceless Polynomial Time (1999)
- Andreas Blass, Yuri Gurevich, Saharon Shelah, On Polynomial Time Computation Over Unordered Structures (2002)
- Andreas Blass, Yuri Gurevich, Saharon Shelah, Choiceless Polynomial Time (1999)
- Andreas Blass, Yuri Gurevich, Saharon Shelah, On Polynomial Time Computation over Unordered Structures (2002)
- Jin-Yi Cai, Martin Fürer, Neil Immerman, An Optimal Lower Bound on the Number of Variables for Graph Identification (1992)
- Jin-Yi Cai, Martin Fürer, Neil Immerman, An Optimal Lower Bound on the Number of Variables for Graph Identification (1992)
- Peter J. Cameron, Notes on Classical Groups (2000)
- Peter J. Cameron, Notes on Classical Groups (2000)
- Ashok K. Chandra, David Harel, Structure and Complexity of Relational Queries (1982)
- Anuj Dawar, David Richerby, Benjamin Rossman, Choiceless Polynomial Time, Counting and the {Cai–Fürer–Immerman} Graphs (2008)
- Anuj Dawar, Erich Grädel, Bjarki Holm, Eryk Kopczyński, Wied Pakusa, Definability of Linear Equation Systems over Groups and Rings (2013)
- Anuj Dawar, Erich Grädel, Leon Kullmann, Benedikt Pago, Symmetric Proofs in the Ideal Proof System (2025)
- Anuj Dawar, David Richerby, Benjamin Rossman, Choiceless Polynomial Time, Counting and the {Cai–Fürer–Immerman} Graphs (2008)
- Anuj Dawar, David Richerby, A Fixed-Point Logic with Symmetric Choice (2003)
- Erich Grädel, Wied Pakusa, Svenja Schalthöfer, Łukasz Kaiser, Characterising Choiceless Polynomial Time with First-Order Interpretations (2015)
- Erich Grädel, Wied Pakusa, Rank Logic is Dead, Long Live Rank Logic! (2019)
- Françoise Gire, H. Khanh Hoang, An Extension of Fixpoint Logic with a Symmetry-Based Choice Construct (1998)
- Martin Grohe, Pascal Schweitzer, Daniel Wiebking, Deep Weisfeiler Leman (2021)
- Shamgar Gurevich, Ronny Hadani, Notes on Canonical Quantization of Symplectic Vector Spaces over Finite Fields (2009)
- Yuri Gurevich, Logic and the Challenge of Computer Science (1988)
- Shamgar Gurevich, Ronny Hadani, Notes on Canonical Quantization of Symplectic Vector Spaces over Finite Fields (2009)
- Neil Immerman, Eric Lander, Describing Graphs: A First-Order Approach to Graph Canonization (1990)
- Neil Immerman, Relational Queries Computable in Polynomial Time (Extended Abstract) (1982)
- Neil Immerman, Eric Lander, Describing Graphs: A First-Order Approach to Graph Canonization (1990)
- Moritz Lichter, Pascal Schweitzer, Canonization for Bounded and Dihedral Color Classes in Choiceless Polynomial Time (2021)
- Moritz Lichter, Pascal Schweitzer, Choiceless Polynomial Time with Witnessed Symmetric Choice (2023)
- Moritz Lichter, Pascal Schweitzer, Canonization for Bounded and Dihedral Color Classes in Choiceless Polynomial Time (2021)
- Moritz Lichter, Witnessed Symmetric Choice and Interpretations in Fixed-Point Logic with Counting (2026)
- L. H. Loomis, H. Whitney, An Inequality Related to the Isoperimetric Inequality (1949)
- L. H. Loomis, H. Whitney, An Inequality Related to the Isoperimetric Inequality (1949)
- OpenAI, Choiceless polynomial time with counting does not capture polynomial time (2026)
- Benedikt Pago, Choiceless Computation and Symmetry: Limitations of Definability (2021)
- Benedikt Pago, Lower Bounds for Choiceless Polynomial Time via Symmetric XOR-Circuits (2023)
- Benedikt Pago, Choiceless Computation and Symmetry: Limitations of Definability (2021)
- Benedikt Pago, Lower Bounds for Choiceless Polynomial Time via Symmetric XOR-Circuits (2023)
- Wied Pakusa, Svenja Schalthöfer, Erkal Selman, Definability of {Cai–Fürer–Immerman} Problems in Choiceless Polynomial Time (2016)
- Wied Pakusa, Svenja Schalthöfer, Erkal Selman, Definability of {Cai–Fürer–Immerman} Problems in Choiceless Polynomial Time (2016)
- Benjamin Rossman, Choiceless Computation and Symmetry (2010)
- Benjamin Rossman, Choiceless Computation and Symmetry (2010)
- Saharon Shelah, Choiceless Polynomial Time Logic: Inability to Express (2000)
- Saharon Shelah, Choiceless Polynomial Time Logic: Inability to Express (2000)
- Victor Shoup, A Computational Introduction to Number Theory and Algebra (2009)
- Moshe Y. Vardi, The Complexity of Relational Query Languages (Extended Abstract) (1982)
- Faried Abu Zaid, Erich Grädel, Martin Grohe, Wied Pakusa, Choiceless Polynomial Time on Structures with Small Abelian Colour Classes (2014)
- Faried Abu Zaid, Erich Grädel, Martin Grohe, Wied Pakusa, Choiceless Polynomial Time on Structures with Small Abelian Colour Classes (2014)
