[Notes](../../README.md) / [Summaries](README.md) / [Mathematical logic](../index/disciplines/mathematical-logic.md) / [Family 241](../index/mathematical-logic/241-rigidity-of-the-turing-degrees.md)

# 241 — Rigidity of the Turing degrees

[Index page](../index/mathematical-logic/241-rigidity-of-the-turing-degrees.md)

## Original CONTENTS.md summary

[S1:6014] (family entry):

> **241. Rigidity of the Turing degrees.** Every order automorphism of the Turing degrees is the identity, resolving their rigidity problem. Thus no nontrivial relabeling of degrees preserves the ordering by relative computability. ([Lean](../../../lean/docs/241.md))

[S2:569] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**Rigidity of the Turing degrees** [S3:35, S3:37]:

> We prove that every order automorphism of the full partial order of
Turing degrees is the identity, resolving the rigidity conjecture for
the Turing degrees positively. [S3:40–44]

## Undergraduate summary

A **Turing degree** is an equivalence class of sets of natural
numbers under mutual computability — two sets have the
same Turing degree if each can be computed from the other.
The degrees are ordered by relative computability, forming a
massively complex partial order. The **rigidity problem**
asks: does this order have any nontrivial symmetry? That
is, can you permute the degrees in a way that preserves
the ordering structure but moves at least one degree to a
different one? The answer is **no** — the only order
automorphism is the identity map
[S3:40–44, S2:569].

## Graduate summary

**Rigidity of the Turing degrees**
[S3:40–44, S2:569]. Every order
automorphism of the
full partial
order of
Turing degrees is the identity. No nontrivial relabeling of degrees
preserves the ordering by relative computability. The proof requires no
definability or genericity assumption on the automorphism.

## History of the conjecture

The **rigidity problem** for the Turing degrees has been a central
question in computability theory since the 1950s. The partial order of
Turing degrees is extremely complex — it has antichains of every
infinite size, and its structure is far richer than the computability
hierarchy alone suggests. The question of whether this order is rigid —
whether every order automorphism is the identity — was a long-standing
open problem. The result [S3:40–44] resolves it positively: the Turing
degree structure is rigid. The proof combined a representation theorem
with a recovery argument to show that any order automorphism must fix
every degree.

**Prior (my training data, not this repo).** Turing degrees, their
partial order, and the rigidity question are standard in computability
theory. The positive resolution of the rigidity problem is the novel
contribution. I cannot confirm this independently from training alone.

## Consequences

- **The rigidity
theorem** [S3:40–44]: every order automorphism of the full Turing
degrees is the identity. No nontrivial relabeling of degrees preserves
the ordering by relative computability.

## Section skeleton

One manuscript: [S3:40–44] (title [S3:35], date [S3:37]) — `main.tex` under
`build/` with `sections/` in order: introduction, preliminaries,
rigidity, recovery, representation. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S4],
one comparator stub [S5], and one `main_results` entry [S7]. The scope
note [S4:9] states the target: every order automorphism of the full
Turing degrees of subsets of
$`\mathbb N`$
fixes every degree, with no definability or genericity assumption. The
additional representation corollaries are not included.

The `main_results` entry [S7:1176–1177] names
`OAI.TuringRigidity.ManuscriptMain.rigidity` in
`lean/OAI/Computability/DegreeRigidity/Main.lean`. In the source, the
theorem is stated and closed: "theorem rigidity : MainTheorem :=
main_of_representation borel_representation" [S6:27], which calls the
`borel_representation` theorem [S6:24] and the
`generic_program_representation` theorem [S6:10]. `grep` finds **zero**
`sorry` in the whole `lean/OAI/Computability/DegreeRigidity/` tree.

The one comparator stub [S5] states the rigidity target and ends in
`sorry`. The proved copy lives under `lean/OAI/`. A comparator stub is a
target the release set itself; the proved version, where it exists,
lives under `lean/OAI/`. The reading is of source text only — no `lake`
or `lean` run elaborates the proof.

**Tree measurement (source-level).**

The `main_results` entry OAI.TuringRigidity.ManuscriptMain.rigidity resolves to `OAI/Computability/DegreeRigidity/Main.lean` (31 lines); the top-level theorem is `theorem generic_program_representation (π`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory is large: 975 files, 4399 theorems, 1667 defs.

The preprint states 8 theorem environments; the tree carries 550× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=241` [S8] records the tier and the counts:
`tier=T3`, `paps=1`, `paps_form=1`, `chal=1`, `mainres=1`,
`scope_note=1`, `verification=0`, `trace=`. The `paps_form=1` against
`paps=1` is the coverage signature: one of the one manuscripts is named
as a formalization source, and the single `main_results` entry over that
config reaches the full rigidity claim. The comparator stub names the
same target, and the proved copy lives under `lean/OAI/`. There is no
verification bundle and no reasoning trace. The shape flags are
`resolution`, and `resolves_named=1` — the blurb names the rigidity
problem with "resolving".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6014] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 241 at [S2:569] |
| S3 | [`preprints/Rigidity-of-the-Turing-degrees-September-24-2026/build/main.tex`](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/build/main.tex) | 51 | manuscript 1 of 1; title [S3:35], date [S3:37], abstract [S3:40–44] |
| S4 | [`lean/docs/241.md`](../../../lean/docs/241.md) | 15 | scope note — the formalization's Scope at [S4:9] and its one comparator link at [S4:15] |
| S5 | [`lean/ComparatorChallenges/DegreeRigidity.lean`](../../../lean/ComparatorChallenges/DegreeRigidity.lean) | 44 | comparator stub — the rigidity target with its `sorry` |
| S6 | [`lean/OAI/Computability/DegreeRigidity/Main.lean`](../../../lean/OAI/Computability/DegreeRigidity/Main.lean) | 31 | the formalized file — `rigidity` proved at [S6:27] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming the declaration, at [S7:1176–1177] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=241`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
