Notes / Summaries / Mathematical logic / [Family 244](../../index/mathematical-logic/244-partition-principle-does-not-imply-choice.md)

# 244 — The partition principle does not imply choice

## Original CONTENTS.md summary

[S1:573] carries the family entry:

> Assuming ZF is consistent, constructs a model in which every surjective image of a set injects into that set, yet the axiom of choice fails. Choice for ordinal-indexed families still holds. From any countable transitive model of ZFC, a separate construction gives a transitive symmetric extension with these properties and no new countable sequences of ground-model elements.

The entry links the manuscript as "The Partition Principle does not imply
Choice" [S1:573].

The manuscript's title is "The Partition Principle does not imply Choice" [S2:1] and its date is [S2:5].

## Undergraduate summary

The Partition Principle says that a surjection from one set to another gives
an injection back. It is weaker than the Axiom of Choice, which picks one
element from each member of a family. The principle is about comparing
cardinals, not about picking elements. [S4:11] gives the equivalent form:
"Equivalently, every partition of a set admits an injection into that set."

The question is whether that cardinal comparison is enough. [S4:15–16] states
it: "The problem is whether this cardinal comparison alone can recover choice
for arbitrary families." The manuscript answers it with a relative-consistency
statement.

The main theorem is that statement. [S4:23–25] states it: "If $\ZF$ is
consistent, then so is $\ZF+\PP+\ACwo+\neg\AC$." The model keeps Choice for
wellorderable families while losing the full axiom.

The abstract gives the same result in prose. [S3:49–51] says: "We prove that
the Partition Principle does not imply the Axiom of Choice: if ZF is
consistent, then so is ZF with the Partition Principle, Choice for
ordinal-indexed families, and the negation of the Axiom of Choice."

The second result is the transitive-model form. [S3:52–54] gives it:
"Separately, over every countable transitive model of ZFC, we construct a
transitive symmetric model of this theory with the same ordinals and no new
countable sequences of ground elements." The manuscript states the model
conditions at [S4:29–40].

## Graduate summary

The construction is a symmetric extension, and the manuscript's structure
follows the forcing machinery: the monoid section [S5:1], the forcing section
[S6:1], the quotients section [S7:1], the conclusion [S8:1], and the
metatheory section [S9:1].

The scope note records what the formalization carries, and its reading of the
model construction is narrower than the manuscript's. [S10:9] gives the
consistency implication: "The Partition Principle says that every surjection
admits an injection in the reverse direction. The formalization proves the
relative-consistency implication: if ZF is consistent, then so is ZF with the
Partition Principle, Choice for ordinal-indexed families, and failure of the
Axiom of Choice."

The scope note's second paragraph names the extra hypothesis the selected
model construction carries. [S10:11] says: "The linked model-construction
result also constructs a transitive model of the Partition Principle without
Choice from an externally countable transitive ground model satisfying the
stated axioms, including Choice, and containing an internal strongly
inaccessible cardinal. The paper's stronger transitive-model preservation
assertions are outside that selected construction."

That is the load-bearing gap on this page. The manuscript's transitive-model
theorem at [S4:29–40] takes any countable transitive model of ZFC and
requires the same ordinals and no new countable sequences of ground elements.
The formalized construction adds an internal strongly inaccessible cardinal
and leaves the preservation assertions out.

The declaration is `OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice`
at [S11:34], typed as the existence of a transitive model of ZF satisfying
the Partition Principle, Choice for wellorderable families, and the negation
of Choice. The declaration sits in the forcing closure, not in a standalone
statement file.

The two comparator configs state the targets the release set itself, and each
is a stub. [S12:273] carries `sorry`; [S13:320] carries `sorry`. The scope
note's comparator table names the two rows: the model construction from a
ground model, and the relative consistency of the Partition Principle with
ordinal Choice and failure of Choice. Both JSON targets permit the same three
axioms: `propext`, `Quot.sound`, `Classical.choice`.

The manuscript fixes the theory its theorem is about. [S4:42–43] states it:
"Here $\ZF$ is classical first-order set theory with pure sets, Foundation,
and the full Separation and Replacement schemata." The injection the Partition
Principle supplies need not pick a member of each part, and that is why the
principle can survive while choice fails.

## History of the conjecture

The Partition Principle is a long-standing weak form of choice, and the
manuscript's introduction opens by naming the direction that is easy:
[S4:12–13] says "The Axiom of Choice implies this principle by choosing one
element of each fiber. The converse is less direct: the injection supplied by
$\PP$ need" — the injection need not satisfy $f\circ j=\id_Y$, which is the
section property choice would give.

The scope note's own first sentence gives the principle in the form the
formalization uses, at [S10:9], and the manuscript's equivalent form at
[S4:11] names the partition version. The two statements of the principle
agree, and the scope note's paragraph is where the formalized claim is
recorded.

`notes/tables/conjecture-standing.tsv` carries no row for family 244, so the
prior on the Partition Principle's standing is not recorded in the release's
own reading. The claim in the entry is the record.

## Consequences

The separation is a consistency result, not a theorem of ZF. [S4:23–25]
states it in the relative form, and [S10:9] records that the formalization
proves the same implication.

The model construction carries a hypothesis the manuscript's theorem does not.
[S10:11] names it: an internal strongly inaccessible cardinal in the ground
model, and the preservation assertions the paper makes are outside the
selected construction. The manuscript's theorem at [S4:29–40] asks only for a
countable transitive model of ZFC.

The family carries two comparator configs, one per result, and both are
stubs. [S12:273] and [S13:320] carry `sorry`, so the release has set both
targets and proved neither.

The release's own record is source-level. The scope note says the formalized
claim exists and names its declaration; the two comparator configs carry
`sorry`; no Lean run in this repository proves any of them elaborates.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 573 |
| S2 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/README.md`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/README.md) | 18 | Manuscript title, date, citation |
| S3 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/main.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/main.tex) | 67 | Abstract, lines 49–54 |
| S4 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/introduction.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/introduction.tex) | 213 | Principle, theorems, framing |
| S5 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/monoid.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/monoid.tex) | 801 | The monoid construction |
| S6 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/forcing.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/forcing.tex) | 797 | The forcing construction |
| S7 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/quotients.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/quotients.tex) | 746 | The quotient structure |
| S8 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/conclusion.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/conclusion.tex) | 303 | The conclusion |
| S9 | [`preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/metatheory.tex`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/sections/metatheory.tex) | 439 | The metatheory section |
| S10 | [`lean/docs/244.md`](../../../lean/docs/244.md) | 18 | Scope note |
| S11 | [`lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean`](../../../lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean) | 51 | The transitive-model declaration |
| S12 | [`lean/ComparatorChallenges/PartitionPrinciple.lean`](../../../lean/ComparatorChallenges/PartitionPrinciple.lean) | 277 | Stub, `sorry` at line 273 |
| S13 | [`lean/ComparatorChallenges/PartitionConsistency.lean`](../../../lean/ComparatorChallenges/PartitionConsistency.lean) | 324 | Stub, `sorry` at line 320 |
