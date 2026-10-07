# 102 — The Unique Games Conjecture and optimal approximation thresholds (Theoretical computer science, 5 manuscripts, tier T3)

## Original CONTENTS.md summary

[S1:2529] (the family entry):

> **102. The Unique Games Conjecture and optimal approximation thresholds.** Proves Khot's Unique
> Games Conjecture. Independent direct reductions also establish NP-hardness, on unweighted graphs,
> of approximation beyond the Goemans–Williamson ratio for Max-Cut, below factor two for Vertex
> Cover, and within any fixed constant factor for Min-UnCut and directed feedback vertex set. These
> direct proofs use established PCP and Label Cover hardness results.
> ([Lean](../../../lean/docs/102.md))

The entry names five manuscripts; [S2:282] lists the same five, and the release attributes a
reasoning trace to this family: "Ordinary NP-hardness at the basic semidefinite threshold"
([S3:30]).

## Undergraduate summary

A **constraint system** asks you to label the vertices of a graph so that as many edges as possible
are satisfied. A **unique game** is the special case in which every edge prescribes, for each label
at one endpoint, exactly one legal label at the other — a permutation. So if you pick one label,
the whole connected component is forced. Khot's **Unique Games Conjecture** (2002) says these
systems stay computationally hard even in the regime where almost every constraint can be
satisfied: a system is either satisfiable at nearly 100%, or so broken that no strategy satisfies
more than a tiny fraction, and telling the two apart is NP-hard.

This family proves that conjecture. The main manuscript reduces 3SAT to unique games in
deterministic polynomial time, with a gap you can pick in advance: satisfiable formulas give games
satisfiable to within any prescribed ε of 100%, unsatisfiable ones give games where no strategy
beats any prescribed δ below 50%. The reduction is explicit and **unweighted** — no probability
distribution on edges, no advice string handed to the algorithm — and the alphabet is a fixed
binary vector space chosen before the formula is known.

Four companion manuscripts then turn the conjecture from a hypothesis into a theorem, and none of
them needs it. Max-Cut cannot be approximated better than the Goemans–Williamson constant
0.878567…; Vertex Cover cannot be approximated better than factor two; Min-UnCut and directed
feedback vertex set cannot be approximated within **any** fixed constant factor. Each of those four
proofs is a direct reduction from 3SAT, and each says plainly that it assumes no unproved hardness
hypothesis — the conjecture is what this family proves, not what those papers presuppose.

The shape of the proof, sketched at [S6:138–163] and [S6:299]:

1. **Start from a known gap.** Take the published 2-to-1 Games Theorem, which already gives hard
   games — but only with completeness bounded near one half, not near one.
2. **Close the completeness gap.** Keep the established degree-two inverse theorem and change the
   noise applied to the long code, using a nonlinear map, so completeness can be pushed to one.
3. **Keep one structural tool.** Use a uniform rank-one test to decode labels; the noise changes,
   the ordinary rank-one test stays as the soundness tool.
4. **Amplify.** Use the explicit projection-game repetition bound of Dinur and Steurer to drive
   soundness down to the prescribed δ.
5. **Read off the consequences.** The four threshold theorems follow from the proved conjecture
   plus the classical reductions — and, in the companion papers, from direct reductions that skip
   the conjecture entirely.

## Graduate summary

The theorem is stated in the main manuscript as the *Unique Games Theorem* ([S6:22–38]) and in the
abstract as "We prove the Unique Games Conjecture." ([S5:63]): for every fixed ε, δ in (0, 1/2), a
deterministic polynomial-time reduction from 3SAT to unique games over a fixed finite alphabet,
completeness at least 1−ε, soundness at most δ. The instance shape is pinned down: "The graph is
simple and bipartite, and every constraint is a translation" ([S6:35]) of a fixed alphabet vector,
so one label at one endpoint fixes its neighbour. The alphabet, the degree of the running-time
polynomial, and its constants depend only on ε and δ. The manuscript is explicit that this is the
standard form of the conjecture: "the result resolves the Unique Games Conjecture positively in its
usual edge-value formulation" ([S6:41–42]), and "Binary translation constraints are a known
equivalent formulation of the conjecture" ([S6:44–45]).

The load-bearing move is analytic, not combinatorial. "The central difficulty is to retain
completeness near one when every label permits only one reply." ([S6:59–60]) The published 2-to-1 and
2-to-2 program got hardness for games that are almost satisfiable in a weak sense: "These results
established hardness for almost satisfiable 2-to-1 and 2-to-2 games and, as a consequence, a Unique
Games gap with completeness close to one half and arbitrarily small soundness." ([S6:129–131])
"Obtaining Unique Games completeness arbitrarily close to one was a separate problem."
([S6:131–132]) The paper's answer is stated in one sentence: "Our proof keeps the established
degree-two inverse theorem and changes the noise using a nonlinear map." ([S6:148–150]) The
decoder is deliberately conservative: "Our test changes the noise while retaining the ordinary
rank-one test as the structural tool for soundness." ([S6:162–163]) Repetition is not a black box —
"For repetition we use the explicit projection-game bound of Dinur and Steurer" ([S6:299–300]).

What the result does **not** say matters as much. The hardness consequences are strict-threshold
statements: "the resulting hardness statements exclude deterministic polynomial-time approximations
at the indicated strict thresholds" ([S7:15–17]), i.e. every fixed factor strictly on the hard side
of the benchmark, not the benchmark itself. The main paper's consequences section derives them from
classical reductions, so they carry the usual P ≠ NP reading. The four companion manuscripts are
independent of that route: the Max-Cut paper states "The Unique Games Conjecture enters only as
historical context." ([S15:125–126]), the Min-UnCut paper states "It assumes neither the Unique
Games Conjecture nor any other unproved hardness hypothesis." ([S18:68–70]), and the directed
feedback vertex set paper states that "the proof does not consume a Unique Games hardness
theorem." ([S19:107–108])

Formalization status is partial: 3 of the 5 manuscripts appear in the release's `main_results`
list. The scope note states the formalized content per result — "a deterministic polynomial-time
reduction from binary 3SAT to nonempty unweighted simple bipartite unique games." ([S8:13]),
"The formalized result establishes hardness of approximating Max-Cut beyond the Goemans–Williamson
constant" ([S8:15]), and for Vertex Cover that any fixed-factor algorithm "would give a
polynomial-time decision algorithm for 3SAT." ([S8:17]) Min-UnCut is recorded as "establishing
hardness for every fixed approximation factor greater than one." ([S8:19]) and directed feedback
vertex set as "The formalization proves hardness of approximating the minimum such set within any
fixed constant factor." ([S8:21]) The `main_results` entries name the declarations, e.g.
"declaration: OAI.UniqueGamesTheorem.theorem11" ([S9:1630–1632]); the Min-UnCut and directed
feedback vertex set manuscripts are absent from the YAML bibliography entirely, which is consistent
with the ledger's count of 3 formalized manuscripts. Each of the five results has its own comparator
challenge configuration naming the module, the theorem and definition names, and permitting only
propext, Quot.sound and Classical.choice ([S10], [S11], [S12], [S13], [S14]). Every entry in this
family is agent-generated and unreviewed: the YAML records "status: unchecked" ([S9:1662–1663]).
The manuscript itself ships a short README carrying its title, date, and citation stub ([S4]).

## History of the conjecture

Khot posed the conjecture with an algorithm, not against one: "Khot introduced the Unique Games
Conjecture in 2002 and gave an algorithm based on semidefinite rounding" ([S6:74–75]). The Vertex
Cover companion records the same moment from the hardness side — the conjecture "proposed a
stronger source of approximation gaps" ([S17:32–34]) — and its consequences are what made it
famous. The two thresholds in this family are the canonical ones.

For Max-Cut, the algorithmic side is 1994: "Goemans and Williamson gave a semidefinite programming
algorithm with random-hyperplane rounding for Max-Cut" ([S15:15–16]) at ratio 0.878567…, and the
question this family answers was posed decades earlier — "Determining whether this ratio is
optimal under ordinary NP-hardness has been a central question in approximation algorithms."
([S15:27–28]) Håstad's parity gap plus the gadgets of Trevisan, Sorkin, Sudan and Williamson
ruled out ratios above 16/17 ([S15:29–31]). The conditional optimum is 2004: "Khot, Kindler,
Mossel, and O'Donnell established optimality of" that ratio assuming the conjecture ([S15:32]),
with the Majority Is Stablest theorem of Mossel, O'Donnell and Oleszkiewicz as the analytic input
([S15:34–35]).

For Vertex Cover, the problem is original: "Vertex Cover appeared as *Node Cover* among the
problems Karp proved NP-complete in 1972" ([S17:3–4]), and the factor-two algorithm is the
endpoints of a maximal matching. Unconditional constants improved slowly — Håstad "established
hardness for every fixed factor below" 7/6 ([S17:27–28]), Dinur and Safra raised this to every
fixed factor below 10√5 − 21 ≈ 1.36068 ([S17:29–30]), and Karakostas reached 2 − Θ(1/√log n), a
saving that shrinks with the input, so "The threshold addressed here concerns a fixed saving below
two, so it is compatible with such algorithmic improvements." ([S17:10–11]) The conditional
factor-two result is Khot and Regev: "Assuming this conjecture, Khot and Regev obtained hardness
for every fixed factor below two" ([S17:34–35]). The unconditional route ran through the 2-to-2
program: "This completed the Games Theorem with imperfect completeness and yielded unconditional
Vertex Cover hardness for every fixed factor below" √2 ([S17:48–50]) — short of the factor-two
threshold, which is exactly what the completeness gap costs.

Min-UnCut's history is a conditional gap plus a race of finite gadgets: "Under the Unique Games
Conjecture, the near-satisfiable Max-Cut gap of Khot, Kindler, Mossel and O'Donnell implies
arbitrarily large constant gaps for weighted Min-UnCut" ([S18:24–26]), while unconditionally the
known constants climbed from 11/8 to 1.45685 to ≈1.48969 ([S18:33–40]). Directed feedback vertex
set had the same shape: "Ordinary NP-hardness of approximation already follows from Vertex Cover,
which asks for a smallest vertex set meeting every edge of an undirected graph." ([S19:24–25]) and
"These results exclude particular constants; excluding every constant had required a stronger
complexity assumption." ([S19:31–33])

## Consequences now that the proof has been found

The main manuscript's consequences section is explicit about the mechanism: "Theorem 1.1 turns
established conditional hardness results into NP-hardness results." ([S7:3–4]) Applied to Max-Cut,
the result is hardness at every fixed ratio in (α_GW, 1) on simple unweighted graphs, and "This
matches the semidefinite approximation threshold of Goemans and Williamson" ([S7:26–27]) — the
semidefinite program is optimal, not merely the best known polynomial-time method. Applied to
Vertex Cover, "Khot and Regev's reduction gives NP-hardness at every fixed factor in" (1, 2)
([S7:30–31]), so the factor-two matching algorithm is the end of the story.

The general form is a semidefinite-to-hardness transfer, not a list. The corollary derived from
Raghavendra's framework says that whenever a finite constraint language has a strict gap between
its optimum and its basic semidefinite value, distinguishing the two is NP-hard at every fixed
margin inside that gap ([S7:64–73]). For ordering CSPs the consequence is a computed threshold:
"Together with the random-ordering guarantee, this gives the optimal threshold" ρ_Π
([S7:201–202]) — Maximum Acyclic Subgraph at 1/2 and Betweenness at 1/3 ([S7:220–227]), because
"forward edges form an acyclic subgraph, and every acyclic subgraph has a topological order."
([S7:222–223]) For the deletion, cutting and
clustering problems the statement is a flat exclusion: "For *Sparsest Cut*, this is hardness of the
search task under polynomial-time Cook reductions: the algorithm must output a cutset, not only an
estimate of the optimum." ([S7:265–267]) and "none of these problems admits a deterministic
polynomial-time approximation with any fixed constant factor." ([S7:268–269])

The four companions change the status of those thresholds from conditional to unconditional, and
they are the more durable half of the consequence. The Max-Cut paper's own framing is "We resolve
the unconditional optimality question for Max-Cut." ([S15:37]) The Vertex Cover paper's is "We
prove that every fixed improvement in this factor is NP-hard." ([S16:12–13]), with the gap ratio
2 − 6/(m+2) tending to two as m grows ([S16:42–44]), and its only external hardness input is the
Label Cover promise — "the only external hardness input used here." ([S17:24–25]) The Min-UnCut
paper settles the question in one direction and one sentence: "Min-UnCut measures distance from
bipartiteness." ([S18:17]) and its theorem gives the gap for every fixed integer K ≥ 2 with all
constants effective and no advice ([S18:50–66]); the reason it needed its own reduction is that
"a multiplicative approximation for Max-Cut does not give a comparable multiplicative
approximation for Min-UnCut when the graph is nearly bipartite." ([S18:18–20]) The directed
feedback vertex set paper closes the last conditional gap: "it is NP-hard to approximate minimum
directed feedback vertex set within factor" any fixed A ≥ 1 ([S19:51–53]), which "implies that a
deterministic polynomial-time algorithm with any constant approximation guarantee exists" if and
only if P = NP ([S19:64–66]).

What is *not* a consequence: none of these papers identifies the approximation factor a
polynomial-time algorithm must achieve as inputs grow, and none improves the known general
algorithms — the directed feedback vertex set paper says so about itself ([S19:68–71]). The
release's own blurb records the split correctly: the conjecture is proved, and the four threshold
results are established by "Independent direct reductions" ([S1:2529]). The release also publishes
the derivation behind the main result as a reasoning trace, "Ordinary NP-hardness at the basic
semidefinite threshold" ([S3:30], [S20]).

## Sources

Every path in the File column is repository-relative and every link resolves from this page's
directory. Line numbers are 1-based as shipped. The CONTENTS.md blurb is quoted verbatim; its
inline HTML link was rewritten to a relative one so it resolves from this page.

| Src | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,169 | Release blurb, family 102 at line 2529 |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | LaTeX entry `\resultentry{102}`, line 282 |
| S3 | [`README.md`](../../../README.md) | 50 | Trace attribution, line 30 |
| S4 | [`preprints/The-Unique-Games-Theorem-September-23-2026/README.md`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/README.md) | 18 | Manuscript README (title, date, bibtex stub) |
| S5 | [`preprints/The-Unique-Games-Theorem-September-23-2026/build/main.tex`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/build/main.tex) | 89 | Main paper: title line 56, abstract 63–66 |
| S6 | [`preprints/The-Unique-Games-Theorem-September-23-2026/build/sections/00-introduction.tex`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/build/sections/00-introduction.tex) | 323 | Theorem statement, prior work, proof strategy |
| S7 | [`preprints/The-Unique-Games-Theorem-September-23-2026/build/sections/07-consequences.tex`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/build/sections/07-consequences.tex) | 331 | Consequences of the proved conjecture |
| S8 | [`lean/docs/102.md`](../../../lean/docs/102.md) | 31 | Scope note: what is formalized, per result |
| S9 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1,668 | `main_results`, bibliography, automation and review |
| S10 | [`lean/ComparatorChallenges/UniqueGamesTheorem.json`](../../../lean/ComparatorChallenges/UniqueGamesTheorem.json) | 14 | Comparator config, main theorem |
| S11 | [`lean/ComparatorChallenges/OptimalMaxCut.json`](../../../lean/ComparatorChallenges/OptimalMaxCut.json) | 14 | Comparator config, Max-Cut |
| S12 | [`lean/ComparatorChallenges/VertexCover.json`](../../../lean/ComparatorChallenges/VertexCover.json) | 15 | Comparator config, Vertex Cover |
| S13 | [`lean/ComparatorChallenges/MinUncut.json`](../../../lean/ComparatorChallenges/MinUncut.json) | 14 | Comparator config, Min-UnCut |
| S14 | [`lean/ComparatorChallenges/DirectedFeedback.json`](../../../lean/ComparatorChallenges/DirectedFeedback.json) | 14 | Comparator config, directed FVS |
| S15 | [`preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/build/sections/introduction.tex`](../../../preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/build/sections/introduction.tex) | 207 | Max-Cut companion |
| S16 | [`preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/sections/introduction.tex) | 159 | Vertex Cover companion |
| S17 | [`preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/sections/history.tex`](../../../preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/build/sections/history.tex) | 67 | Vertex Cover companion, history section |
| S18 | [`preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/build/sections/introduction.tex`](../../../preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/build/sections/introduction.tex) | 220 | Min-UnCut companion |
| S19 | [`preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/build/sections/introduction.tex`](../../../preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/build/sections/introduction.tex) | 215 | Directed FVS companion |
| S20 | [`reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf`](../../../reasoning_traces/basic-semidefinite-threshold-np-hardness.pdf) | — | Published reasoning trace for this family |
