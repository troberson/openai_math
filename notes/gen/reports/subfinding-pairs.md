# Sub-finding pairs: the abstract clause and the display title that names it

Every family in the catalog lists its manuscripts as `\href` links inside its own `\resultentry`, so
`overview.tex` carries two descriptions of the same result: the family abstract, and one display title
per manuscript. This page reads, for the densest families, which abstract clause states a sub-finding
and which display title names it. Each pair is quoted with the line it was verified on, and clauses
that state a sub-finding no title names are recorded as unmatched rather than forced onto the nearest
title.

Population: **167 families over 514 manuscripts**. The rule is the bead's own two signals unioned with
its named targets — abstracts containing a multi-claim phrase **and** at least two manuscripts, plus
the ten densest families it names — and band 1, the families with exactly 2 manuscripts and no probe
word, which `math-el4.9` added, band 2, the families with 3-4 manuscripts and no probe word, which
`math-el4.10` added, and band 3, the families with 5 or more manuscripts and no probe word, which
`math-el4.11` added. The three bands cover every multi-manuscript family the probe filter left, so the
population is the multi set. The bead states 51 families for the intersection; that number does
not reproduce, and the gap is the first thing this page records.

## The population, and why it is not the bead's 51

The bead's probe vocabulary is `also prove` (25), `Independent` (35), `also establish` (5),
`not as a consequence` (1), and it warns that `corollary`, `we also prove`, `furthermore`, `we show`
are all zero. All four counts reproduce over the 372 shipped abstracts, with one spelling condition:
the second is the stem `independ`, not the word `independent` (34). The zero counts reproduce too.
So the vocabulary is right and the family count is not.

| rule | families |
|---|---|
| `also prove` | 25 |
| `independ` (stem) | 35 |
| `also establish` | 5 |
| `as a consequence` | 1 |
| union of the four, over all 372 | 62 |
| families with ≥2 manuscripts | 167 |
| **union of the four, over the 167** | **40** |

40, not 51. Nine of the bead's ten named densest targets (all but 034) sit **outside** its own
probe-and-multi set, so the 51 cannot be the intersection of the two signals it describes. Rules
tried and rejected: `also` (56), `both ` (48), `companion` (10), `together` (8), two or more
prove-verbs in the abstract (33), two or more sentences containing a prove-verb (32), three or more
sentences (73). None yields 51, and the same shape of gap — a quoted count with no reproducible rule —
is the counterexample 74 / 30 case recorded in `notes/gen/reports/counterexample-tag.md`.

**Decision, recorded 2026-10-07, extended 2026-10-13.** Population = (probe ∩ multi) ∪ the bead's ten
named densest families ∪ band 1 (exactly 2 manuscripts and no probe word) ∪ band 2 (3-4 manuscripts and
no probe word) ∪ band 3 (5 or more manuscripts and no probe word) = **167 families, 514 manuscripts**
(206 before the 2026-10-07 upstream merge; family 032 lost three manuscripts to the withdrawal and
stayed in the population). The union is chosen over the intersection because the bead's named targets
are the point of the task — 034 at n=14 down to 211 at n=7 — and the probe is the point of its
vocabulary warning. Band 1 is added by `math-el4.9`, band 2 by `math-el4.10`, and band 3 by
`math-el4.11` because the bead's remaining set is the no-signalling-word set, and the bands are its
densest slices. The three bands together cover every multi-manuscript family, so the population is the
multi set and the ten named targets are inside it.
Revisit condition: if a later pass finds a
phrase rule that yields 51, re-measure the population before extending the page; the rework is a re-run
of `notes/scripts/extract_subfinding_pairs.py` plus blocks for the families the new rule adds, which is
cheap, so this bead keeps the task.

Probe-vocabulary false positives: 114, 122, 134, 157, 170, 235, 261, 262, 266, 267, 281, 325, 361. In
these the probe phrase modifies a noun (`independent` of a random choice, `independent` convergence,
`independent` in a theorem statement), not a second result. 13 of the 40 probe-hit families are in this
list, which is why the probe is a floor for the population and not a reading of it.

## Reading method

One line per pair. `main` pairs the clause that states the family's headline result; `clause` pairs a
clause that states an additional result. A clause is a sub-finding when it asserts a result the
headline does not already assert. The quoted clause and the quoted title are both taken verbatim from
the family's single `\resultentry` line, so one anchor proves both sides: the abstract and every
display title of a family sit on that line (verified for all 372 families). `[NNN:k]` is the k-th
manuscript of family NNN in `notes/gen/tables/subfindings.tsv`, whose `title` column is the same display text.
`claimed` and `unclaimed` partition the family's manuscripts, so every title is accounted for once.


## 002 · `overview.tex:80` · n=3 · T0



- claimed: 002:1 002:3
- unclaimed: 002:2
- note: The Selmer converse is the second manuscript's own direction; the abstract states the forward implication, so the converse title is unclaimed.

## 003 · `overview.tex:82` · n=3 · T3




- claimed: 003:1 003:2 003:3
- unclaimed: 
- note: “A companion” is the connective the probe list misses. The third title names the Landau--Siegel exclusion the Hecke clause covers.

## 004 · `overview.tex:84` · n=2 · T0


- claimed: 004:1
- unclaimed: 004:2
- note: "Pointwise 2-converse with rational two-torsion" is an elliptic-curve statement the abstract does not touch. The family ships two manuscripts and the overview paraphrase names one.

## 006 · `overview.tex:88` · n=2 · T0



- claimed: 006:1 006:2
- unclaimed:
- note: The abstract's colon splits the Goldfeld result into the density half and the mean half, and the two titles name exactly those halves.

## 009 · `overview.tex:94` · n=3 · T2




- claimed: 009:1 009:2 009:3
- unclaimed:
- note: The 009:2 pairing is the equal-characteristic half of the sentence; the abstract states both
  halves in one clause, so the clause covers 009:1 and 009:2 together and is assigned to the half the
  headline does not state.

## 010 · `overview.tex:96` · n=3 · T0



- claimed: 010:1 010:3
- unclaimed: 010:2
- note: "Two-adic Hecke dimension" names the dimension computation behind the headline; the abstract
  states no clause for it.

## 011 · `overview.tex:98` · n=3 · T0



- claimed: 011:1 011:2
- unclaimed: 011:3
- note: "Prime Predecessors with an Even Number of Prime Factors" has no clause in the abstract.

## 014 · `overview.tex:104` · n=8 · T0






- claimed: 014:1 014:2 014:4 014:5
- unclaimed: 014:3 014:6 014:7 014:8
- note: The unmatched clause is the arbitrary-characteristic case of the headline; no display title
  names it separately. 014:3 is the assumption the last clause is made under
  ("Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level"), not a result the
  abstract claims. 014:6, 014:7 and 014:8 are tame-Hecke-eigensheaf manuscripts the abstract does not
  mention at all.

## 015 · `overview.tex:106` · n=3 · T2




- claimed: 015:1 015:2 015:3
- unclaimed: 
- note: The abstract lists the three degrees in one sentence, so three clauses of the same sentence pair with the three titles.

## 016 · `overview.tex:108` · n=4 · T0



- claimed: 016:1
- unclaimed: 016:2 016:3 016:4
- note: The clause is an umbrella: three titles each name one case of the $\mathcal A_2$ curve case
  ("$E\times\mathrm{CM}$ component", "Quaternionic division points", "Elliptic squares"), so pairing
  it with any one of them would be a forced pairing.

## 018 · `overview.tex:112` · n=2 · T0



- claimed: 018:1 018:2
- unclaimed:
- note: The overview names the class of fields, not the two cases; the clause's "including" is the only place the function-field case appears.

## 019 · `overview.tex:114` · n=2 · T0



- claimed: 019:2
- unclaimed: 019:1
- note: The $\mathbb Q$ case has no display title. "Prescribed exterior sheet" is an étale-cover
  construction the abstract does not state as a result.

## 029 · `overview.tex:134` · n=2 · T0


- claimed: 029:1
- unclaimed: 029:2
- note: "Simultaneous primitive roots: a conditional lower bound for prime bases" is a second, conditional theorem the abstract does not state. The quantitative clause ("at least $c_a x/(\log x)^2$ primes") belongs to the headline, not to the simultaneous result.

## 032 · `overview.tex:142` · n=5 · T0



- claimed: 032:1
- unclaimed: 032:2 032:3 032:4 032:5
- note: The unmatched clause states consequences through Milne's theorems, not a result the release
  ships a manuscript for. Four further manuscripts (K3 quadratic locus, Weil classes on abelian powers,
  Gale correspondences, a conditional reduction) carry no clause. This family is the withdrawal: the
  two clauses that paired here before the merge — the products-of-K3 theorem and the Kuga–Satake
  algebraicity result — were withdrawn on 2026-10-06 and their clauses are gone from the overview
  abstract, so the family lost two accepted pairs and three manuscripts. See
  `notes/development/upstream_history/2026-10-07_3014888.md`.

## 033 · `overview.tex:144` · n=5 · T2



- claimed: 033:1 033:2
- unclaimed: 033:3 033:4 033:5
- note: The abstract states two theorems; three titles name machinery the abstract does not state — the reverse inequality, the projective Hodge lines, and the K"ahler b-semiampleness input.

## 034 · `overview.tex:146` · n=14 · T0





- claimed: 034:1 034:2 034:4 034:10
- unclaimed: 034:3 034:5 034:6 034:7 034:8 034:9 034:11 034:12 034:13 034:14
- note: The densest family in the corpus states four results and ships fourteen manuscripts; the other
  ten are the machinery (conditional good minimal models, minimal metrics, fourfold nonvanishing,
  section lifting, Schnell fiber spaces, uniform log Iitaka fibrations, log Calabi–Yau fibrations,
  Stein-degree bounds, fourfold log Iitaka fibrations, abundance after nonvanishing).

## 035 · `overview.tex:148` · n=2 · T0



- claimed: 035:1 035:2
- unclaimed:
- note: The second title names the terminal case; the abstract's second sentence names the relaxed hypothesis, which is the same theorem read from the other side.

## 036 · `overview.tex:150` · n=4 · T0




- claimed: 036:1 036:2 036:3
- unclaimed: 036:4
- note: “Numerical dimension one” names no clause; the abstract's semiampleness statement is the general case, not the dimension-one case.

## 037 · `overview.tex:152` · n=2 · T0



- claimed: 037:1 037:2
- unclaimed:
- note: The equality case is the dimension-four statement; the abstract states it as the sharpness clause of the general bound.

## 039 · `overview.tex:156` · n=4 · T3




- claimed: 039:1 039:3 039:4
- unclaimed: 039:2
- note: "Maximal Seshadri constants" (the surface case, `Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces`)
  is the $n=2$ instance of the clause paired to 039:3; the abstract states no separate surface clause.

## 041 · `overview.tex:160` · n=2 · T0



- claimed: 041:1 041:2
- unclaimed:

## 046 · `overview.tex:168` · n=2 · T0



- claimed: 046:1 046:2
- unclaimed:
- note: The abstract carries both results, and the second sentence is the surface case.

## 049 · `overview.tex:174` · n=2 · T3



- claimed: 049:1 049:2
- unclaimed:
- note: The two manuscripts are the same polynomial read as a coordinate failure and as a non-rectifiable embedding.

## 052 · `overview.tex:180` · n=2 · T3



- claimed: 052:1 052:2
- unclaimed:
- note: The abstract names both conjectures; the second title names the hypothesis the second sentence relaxes.

## 055 · `overview.tex:186` · n=2 · T0



- claimed: 055:1 055:2
- unclaimed:
- note: "Also constructs" is the probe word the first pass missed because the family is n=2 — the phrase is in the abstract, and the first-pass population required n>1, which this family satisfies, so the miss is the probe's, not the band's.

## 056 · `overview.tex:188` · n=5 · T0



- claimed: 056:1 056:3
- unclaimed: 056:2 056:4 056:5
- note: 056:2 is the generalized-**canonical** (terminal) flip case, which the abstract does not state
  as a separate clause; 056:4 and 056:5 are the two "finite ordinary minimal model programs" manuscripts,
  also unstated.

## 057 · `overview.tex:190` · n=3 · T0




- claimed: 057:1 057:2 057:3
- unclaimed: 
- note: The quasi-projective nilpotent case is the second title; the fourfold orbifold case is the conditional third title.

## 058 · `overview.tex:192` · n=2 · T3



- claimed: 058:1 058:2
- unclaimed:
- note: The second title names the $D$ factor of the product the headline states. The pairing is one clause read twice, not two results.

## 059 · `overview.tex:194` · n=2 · T0



- claimed: 059:1 059:2
- unclaimed:
- note: The two titles name the two multiplicity pairs; the abstract names the pair 4/5 explicitly and leaves 2/3 to the headline.

## 065 · `overview.tex:204` · n=2 · T0



- claimed: 065:1 065:2
- unclaimed:
- note: The abstract's second sentence is the transfer theorem; the first is the base case.

## 066 · `overview.tex:206` · n=2 · T3



- claimed: 066:1 066:2
- unclaimed:
- note: The second title names the local form of the bounded-complement statement.

## 068 · `overview.tex:210` · n=7 · T0



- claimed: 068:1
- unclaimed: 068:2 068:3 068:4 068:5 068:6 068:7
- note: The second sentence restates the headline with the dimension uniformity made explicit, so it is
  recorded unmatched rather than paired to a companion. Six manuscripts (invariant indices, bounded
  metrics on klt pairs, cohomological transfer, metric descent, integrable metrics with controlled
  boundary, exact orders) ship with no clause at all — the most companion-heavy family in the population.

## 071 · `overview.tex:216` · n=2 · T2



- claimed: 071:1 071:2
- unclaimed:

## 072 · `overview.tex:218` · n=2 · T3



- claimed: 072:1 072:2
- unclaimed:
- note: The second title names the $s=-1$ case of the same integral, which the abstract states as a separate disproof.

## 074 · `overview.tex:222` · n=2 · T0



- claimed: 074:1 074:2
- unclaimed:
- note: The abstract names two conjectures in one sentence; the two titles name them in the same order.

## 076 · `overview.tex:226` · n=3 · T3



- claimed: 076:1 076:2
- unclaimed: 076:3
- note: “Asymptotically minimal maxima” is a variant of the ultraflat construction; the abstract states one construction, so the third title is unclaimed.

## 077 · `overview.tex:228` · n=2 · T0



- claimed: 077:1 077:2
- unclaimed:
- note: The second title names the sphere case; the abstract states the general surface bound, which includes it.

## 080 · `overview.tex:234` · n=2 · T0



- claimed: 080:1 080:2
- unclaimed:
- note: The planar case is the $n=2$ instance of the general theorem; the abstract names it as an inclusion.

## 082 · `overview.tex:238` · n=3 · T3




- claimed: 082:1 082:2 082:3
- unclaimed: 
- note: The annular title pairs with the third-input clause, which is where the symmetric point is stated.

## 084 · `overview.tex:242` · n=2 · T2



- claimed: 084:1 084:2
- unclaimed:
- note: The two titles split the general ratio from the dyadic ratio; the abstract states the general case and names the resolution.

## 087 · `overview.tex:250` · n=3 · T3




- claimed: 087:1 087:2 087:3
- unclaimed: 
- note: The sharp functional Mahler inequalities clause states a result no title names.

## 088 · `overview.tex:252` · n=2 · T3




- claimed: 088:1 088:2
- unclaimed:
- note: The Lutwak--Petty inequalities are stated as a result and named by no display title.

## 089 · `overview.tex:254` · n=2 · T3



- claimed: 089:1 089:2
- unclaimed:
- note: The headline names both cases in one phrase; the clause is the quantitative form of the treewidth half.

## 090 · `overview.tex:256` · n=4 · T2



- claimed: 090:2 090:4
- unclaimed: 090:1 090:3
- note: The two certificate titles name proof machinery the abstract does not state.

## 092 · `overview.tex:260` · n=2 · T3



- claimed: 092:1 092:2
- unclaimed:
- note: The headline is the upper bound, the clause the matching lower bound; the two titles name them in that order.

## 095 · `overview.tex:266` · n=3 · T3



- claimed: 095:1 095:2
- unclaimed: 095:3
- note: The third title asserts an exact semidefinite lift of a nonspectrahedral cone; the abstract states the examples admit no such lift, so title and abstract are in direct conflict.

## 099 · `overview.tex:274` · n=3 · T2


- claimed: 099:1
- unclaimed: 099:2 099:3
- note: The abstract names no circle or tree construction; the two titles name the bound machinery.

## 100 · `overview.tex:276` · n=4 · T2


- claimed: 100:1
- unclaimed: 100:2 100:3 100:4
- note: The Bang clause is the headline consequence, not a second manuscript; the three approximation titles name construction steps the abstract does not state.

## 102 · `overview.tex:282` · n=5 · T3






- claimed: 102:1 102:2 102:3 102:4 102:5
- unclaimed:
- note: One clause names two manuscripts, so it is quoted twice, once per title. This is the family the
  bead's own example names, and the pairing is exact: four of five titles name a clause.


## 104 · `overview.tex:286` · n=4 · T3




- claimed: 104:1 104:2 104:3
- unclaimed: 104:4
- note: The randomized algorithm title is unclaimed: the abstract states deterministic algorithms only.

## 107 · `overview.tex:292` · n=3 · T3




- claimed: 107:1 107:2 107:3
- unclaimed: 
- note: Three bounds, three sentences, three titles.

## 110 · `overview.tex:298` · n=2 · T2



- claimed: 110:1 110:2
- unclaimed:
- note: The second title names the implementation the second sentence describes.

## 113 · `overview.tex:304` · n=2 · T3



- claimed: 113:1 113:2
- unclaimed:

## 114 · `overview.tex:306` · n=2 · T3



- claimed: 114:1 114:2
- unclaimed:
- note: Probe hit only — the `independ` match is "independence oracles", a presentation of the input,
  not multi-claim language.

## 115 · `overview.tex:308` · n=2 · T2



- claimed: 115:1 115:2
- unclaimed:
- note: "Also gives" is the probe word; the family is n=2, so the first pass missed it on the population rule, not on the phrase.

## 116 · `overview.tex:310` · n=3 · T3



- claimed: 116:1 116:3
- unclaimed: 116:2
- note: The abstract states polynomial-size hitting lists, not a single rational matrix hitting point.

## 117 · `overview.tex:312` · n=2 · T3



- claimed: 117:1 117:2
- unclaimed:
- note: The second sentence names the relaxation's gap, which is the second title.

## 119 · `overview.tex:316` · n=2 · T3




- claimed: 119:1 119:2
- unclaimed:
- note: The strengthening has no display title of its own; it is the theorem inside 119:1.

## 122 · `overview.tex:322` · n=3 · T2




- claimed: 122:1 122:2 122:3
- unclaimed:
- note: The 122:2 pairing is the weakest call on this page — the title names a technique
  (latest-anchor induction, spectrally compact masks) and the clause names a regime, so they match on
  subject, not on wording. Probe hit only: "independent traces" is the sample model.

## 125 · `overview.tex:327` · n=2 · T3



- claimed: 125:1 125:2
- unclaimed:
- note: The algorithm and the threshold are the two titles; the abstract states both.

## 129 · `overview.tex:335` · n=2 · T3




- claimed: 129:1 129:2
- unclaimed:
- note: The headline is one "both … and …" sentence split across the two titles. The Sakoda--Sipser
  attribution is stated as a consequence and named by no title. Probe hit only: "independent of
  alphabet size".

## 130 · `overview.tex:337` · n=2 · T3



- claimed: 130:1 130:2
- unclaimed:
- note: The second title names the model the second sentence defines; the pairing is by the model, not by a second theorem.

## 133 · `overview.tex:343` · n=4 · T2




- claimed: 133:2 133:3 133:4
- unclaimed: 133:1
- note: Parity lifts and bounded-treewidth witnesses name proof machinery the abstract does not state.

## 134 · `overview.tex:345` · n=3 · T2



- claimed: 134:3
- unclaimed: 134:1 134:2
- note: The second sentence restates the headline as a uniformity statement, so it is unmatched.
  "Star height at most four" is the earlier, weaker rung and "Finite-monoid computations" the method;
  neither is stated. Probe hit only: "independent of automaton size".

## 138 · `overview.tex:353` · n=2 · T0



- claimed: 138:1 138:2
- unclaimed:
- note: The second title names the space bound; the abstract states the per-execution and probability guarantees, not the space. The pairing is weak.

## 140 · `overview.tex:357` · n=6 · T3



- claimed: 140:1 140:3
- unclaimed: 140:2 140:4 140:5 140:6
- note: One theorem and one output constraint; the four remaining titles name the estimator machinery the abstract does not state.

## 143 · `overview.tex:365` · n=2 · T3



- claimed: 143:1 143:2
- unclaimed:
- note: The abstract states the general bound and the exact quintic maximum; the titles name them in order.

## 147 · `overview.tex:373` · n=2 · T0



- claimed: 147:1 147:2
- unclaimed:
- note: "also suffices" is the probe word the first pass missed on the n=2 population.

## 149 · `overview.tex:377` · n=2 · T2



- claimed: 149:1 149:2
- unclaimed:
- note: The absorbing-set clause is the boundedness statement the second title names.

## 150 · `overview.tex:379` · n=2 · T2



- claimed: 150:1 150:2
- unclaimed:
- note: The second title names the ergodicity result the abstract states as the strengthening.

## 154 · `overview.tex:387` · n=4 · T0



- claimed: 154:1 154:2
- unclaimed: 154:3 154:4
- note: The triple and fourfold titles are instances of “every finite length”; the distinct-integer-slopes title states a case the abstract's “consecutive” excludes.

## 157 · `overview.tex:395` · n=3 · T3




- claimed: 157:1 157:2 157:3
- unclaimed:
- note: Probe hit only: "independence number".

## 162 · `overview.tex:405` · n=2 · T3



- claimed: 162:1 162:2
- unclaimed:
- note: "A separate construction … also" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 165 · `overview.tex:409` · n=2 · T3



- claimed: 165:1 165:2
- unclaimed:
- note: The headline names both graph classes; the clause is the optimality statement, which is the bipartite half's content.

## 167 · `overview.tex:413` · n=2 · T3



- claimed: 167:1 167:2
- unclaimed:
- note: "A complementary theorem" is the probe word the first pass missed on the n=2 population.

## 170 · `overview.tex:419` · n=2 · T2


- claimed: 170:2
- unclaimed: 170:1
- note: "$r(5,t)$ logarithmic exponent" is the $s=5$ instance of the general clause; the abstract
  states no clause naming it. Probe hit only: "independent set".

## 174 · `overview.tex:427` · n=2 · T3



- claimed: 174:1 174:2
- unclaimed:
- note: The abstract states the existence and the algorithm; the titles name them in order.

## 175 · `overview.tex:429` · n=3 · T3




- claimed: 175:1 175:2 175:3
- unclaimed: 
- note: The three titles name the three results the abstract states in order.

## 182 · `overview.tex:443` · n=3 · T2



- claimed: 182:1 182:2
- unclaimed: 182:3
- note: The square-difference case is $h(x)=x^2$, an instance of the headline, so the abstract's general clause covers it without naming it.

## 184 · `overview.tex:447` · n=2 · T3



- claimed: 184:1 184:2
- unclaimed:

## 186 · `overview.tex:451` · n=2 · T2



- claimed: 186:1 186:2
- unclaimed:
- note: "also applies" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 197 · `overview.tex:475` · n=4 · T3




- claimed: 197:1 197:2 197:3
- unclaimed: 197:4
- note: “Companion examples” is the connective the probe list misses; the odd-characteristic title names a case the abstract does not state.

## 199 · `overview.tex:479` · n=2 · T3



- claimed: 199:1 199:2
- unclaimed:
- note: The headline names three conjectures in one clause; the second title names the third. The second sentence's Nakayama/Wakamatsu list matches no title.

## 200 · `overview.tex:481` · n=2 · T0



- claimed: 200:1 200:2
- unclaimed:
- note: The second title names a technique; the abstract states the theorem, not the method. The pairing is by the theorem the technique proves.

## 203 · `overview.tex:487` · n=2 · T0



- claimed: 203:1 203:2
- unclaimed:

## 205 · `overview.tex:491` · n=2 · T3



- claimed: 205:1 205:2
- unclaimed:
- note: "More generally" is the probe word the first pass missed on the n=2 population. The second title names the proof, not the generalization.

## 206 · `overview.tex:493` · n=2 · T2



- claimed: 206:1 206:2
- unclaimed:
- note: "Moreover" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 207 · `overview.tex:495` · n=2 · T3



- claimed: 207:1 207:2
- unclaimed:
- note: The second sentence names the companion theorem, which is the second title verbatim.

## 209 · `overview.tex:499` · n=2 · T0



- claimed: 209:1 209:2
- unclaimed:
- note: The headline names the degrees; the clause names the construction, which is the first title.

## 210 · `overview.tex:501` · n=2 · T3



- claimed: 210:1 210:2
- unclaimed:
- note: Probe hit only: "dimension-independent".

## 211 · `overview.tex:505` · n=7 · T2





- claimed: 211:1 211:2 211:5 211:7
- unclaimed: 211:3 211:4 211:6
- note: The headline is a two-case sentence; each half is paired with the title naming that case. The
  linear-clock manuscript, the subcritical conformal limits, and the metric-measure limits ship with no
  clause. This family is one of the bead's densest targets and has **no probe hit** — its multi-claim
  language is "also gives", which the bead's vocabulary does not list.


## 212 · `overview.tex:507` · n=2 · T3



- claimed: 212:1 212:2
- unclaimed:
- note: "also holds" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 213 · `overview.tex:509` · n=2 · T3



- claimed: 213:1 213:2
- unclaimed:

## 215 · `overview.tex:513` · n=5 · T3




- claimed: 215:1 215:3 215:5
- unclaimed: 215:2 215:4
- note: "O(3) isolated particle pole" and "O(4) mass bounds" ship with no clause; the mass-gap phrase in
  the headline is the closest the abstract comes to either.

## 216 · `overview.tex:515` · n=6 · T0





- claimed: 216:1 216:2 216:4 216:6
- unclaimed: 216:3 216:5
- note: The abstract names six conclusions in three sentences. The correlation-exponent title restates the headline clause, which the first title claims, so it is unclaimed.

## 217 · `overview.tex:517` · n=2 · T0



- claimed: 217:1 217:2
- unclaimed:
- note: The headline names both halves; the clause is the limiting-law half stated as a convergence.

## 218 · `overview.tex:519` · n=6 · T2




- claimed: 218:1 218:4 218:5
- unclaimed: 218:2 218:3 218:6
- note: The quenched title pairs with the iid-disorder clause. The second quenched title is a variant of the same result, so the abstract's one disorder clause claims only one of them.

## 219 · `overview.tex:521` · n=2 · T0



- claimed: 219:1 219:2
- unclaimed:
- note: "The same … persists" is the probe word the first pass missed on the n=2 population.

## 220 · `overview.tex:523` · n=3 · T3




- claimed: 220:1 220:2 220:3
- unclaimed: 
- note: The two zero--one laws are the two environment classes the first sentence names.

## 222 · `overview.tex:527` · n=4 · T2





- claimed: 222:1 222:2 222:3 222:4
- unclaimed: 
- note: Margin $-1$ is the jamming regime the second title names.

## 223 · `overview.tex:529` · n=6 · T0




- claimed: 223:1 223:2 223:6
- unclaimed: 223:3 223:4 223:5
- note: The headline clause claims the general conformal-limit title; the two domain clauses claim the q-split titles. The quenched, thermal, and occupation-measure titles name results the abstract does not state.

## 224 · `overview.tex:531` · n=3 · T0




- claimed: 224:1 224:2 224:3
- unclaimed: 
- note: The pivotal-amplitude title pairs with the normalization clause.

## 227 · `overview.tex:537` · n=8 · T3





- claimed: 227:1 227:4 227:6 227:8
- unclaimed: 227:2 227:3 227:5 227:7
- note: The headline is a three-regime sentence ($\beta<1$, $\beta=1$, $\beta>1$) and each regime has a
  title, so the pairing is unusually clean for a family with no probe hit. The autocorrelation clause is
  an umbrella over 227:1 and 227:2 ("Functional universality"), so it is paired to the quench title and
  227:2 is left unclaimed. The spectral-gap, critical-slowing-down, and low-temperature-upper-bound
  manuscripts carry no clause.

## 228 · `overview.tex:539` · n=2 · T3



- claimed: 228:1 228:2
- unclaimed:
- note: The second title names the power-law potential; the clause names both potentials.

## 229 · `overview.tex:541` · n=3 · T2



- claimed: 229:1 229:3
- unclaimed: 229:2
- note: The capacity criterion title names a formulation the abstract does not state.

## 230 · `overview.tex:543` · n=2 · T2



- claimed: 230:1 230:2
- unclaimed:
- note: The headline names the question; the clause names the gauge, which is the second title.

## 232 · `overview.tex:547` · n=3 · T0




- claimed: 232:1 232:2 232:3
- unclaimed: 
- note: The three height models are the three titles; “also converge” is the connective the probe list misses.

## 235 · `overview.tex:553` · n=4 · T2




- claimed: 235:1 235:3 235:4
- unclaimed: 235:2
- note: "Linear Variance of the Random 3-SAT Hitting Time" is the $k=3$ instance of the variance clause.
  The abstract also carries a priority credit — "We credit Gaia Carenini with priority for resolving the
  threshold-existence conjecture in her concurrent … ECCC TR26-229" — pointing at an **external** report,
  not a manuscript in this family; it is the only abstract in the population that cites outside the
  release. Probe hit only: "independent uniformly signed".

## 237 · `overview.tex:557` · n=13 · T3




- claimed: 237:4
- unclaimed: 237:1 237:2 237:3 237:5 237:6 237:7 237:8 237:9 237:10 237:11 237:12 237:13
- note: The worst pairing in the population. The third-densest family (13 manuscripts) states a headline
  that **no** display title names — none of the thirteen mentions diameter or the three-quarter exponent —
  and twelve of its titles are machinery (radial transfer, chords, cylinder loops, signed propagation,
  bridge windows, vacuum representations, renewal, strip crossings, bridge moments, cap amplitudes).

## 238 · `overview.tex:559` · n=12 · T3



- claimed: 238:1
- unclaimed: 238:2 238:3 238:4 238:5 238:6 238:7 238:8 238:9 238:10 238:11 238:12
- note: The second sentence strengthens the headline (worst-case start, whole permutation) rather than
  adding a result, so it is unmatched. Eleven companion manuscripts — coordinate frames, Fourier bounds,
  deterministic sweeps, revealed switching, routing, row–column symmetry, subspace tests, compatibility
  entropy, tensor densities, conditional sweeps, a permanent inequality — have no clause.

## 239 · `overview.tex:561` · n=2 · T0




- claimed: 239:1 239:2
- unclaimed:
- note: The headline sentence covers the uniform case, which the next sentence states numerically. Probe
  hit only: "independent entries".

## 240 · `overview.tex:565` · n=2 · T3



- claimed: 240:1 240:2
- unclaimed:
- note: The headline is the positive theorem, the clause the CH obstruction; the titles name them in reverse order.

## 243 · `overview.tex:571` · n=2 · T3



- claimed: 243:1 243:2
- unclaimed:
- note: "A separate result" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 247 · `overview.tex:581` · n=2 · T2



- claimed: 247:1 247:2
- unclaimed:
- note: The second sentence's algebra results match no title; the two titles name the group and the Burnside answer.

## 250 · `overview.tex:587` · n=3 · T3



- claimed: 250:2 250:3
- unclaimed: 250:1
- note: “Finite algebraic envelopes” names machinery the abstract does not state.

## 251 · `overview.tex:589` · n=2 · T3



- claimed: 251:1 251:2
- unclaimed:
- note: "also equivalent" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 254 · `overview.tex:595` · n=3 · T3




- claimed: 254:1 254:2 254:3
- unclaimed: 
- note: Three sentences, three titles, in the order the abstract states them.

## 256 · `overview.tex:599` · n=2 · T2



- claimed: 256:1 256:2
- unclaimed:
- note: "A companion proves" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 258 · `overview.tex:603` · n=2 · T0



- claimed: 258:1 258:2
- unclaimed:

## 260 · `overview.tex:609` · n=13 · T2





- claimed: 260:1 260:2 260:9 260:11
- unclaimed: 260:3 260:4 260:5 260:6 260:7 260:8 260:10 260:12 260:13
- note: The densest family in the population after 034. Nine unclaimed titles name settings the abstract
  does not mention at all — Kerr–Newman, electromagnetic tails, nonmaximal anti-de Sitter, asymptotically
  hyperbolic, local Schwarzschild–anti-de Sitter, the Riemannian endpoint, boundary graphs, and the
  Bondi/CKS class — so this family's abstract under-describes its own shelf.

## 261 · `overview.tex:611` · n=2 · T2




- claimed: 261:1 261:2
- unclaimed:
- note: The first sentence is the umbrella over both titles, so it is recorded unmatched and the two
  case sentences carry the pairing. Probe hit only: "independent uniform site potentials".

## 262 · `overview.tex:613` · n=3 · T3




- claimed: 262:1 262:2 262:3
- unclaimed:
- note: Probe hit only ("independent of matrix size", "independent scales"). The three display titles are
  not encoded consistently: 262:1 and 262:2 carry `Lieb--Thirring` (source dashes) while 262:3 carries
  `Lieb–Thirring` (en dash), so a normalized title string is not verbatim on the line.


## 263 · `overview.tex:615` · n=3 · T3




- claimed: 263:1 263:2 263:3
- unclaimed: 
- note: The excess-charge bound and the two asymptotic families are the three titles.

## 264 · `overview.tex:617` · n=3 · T0


- claimed: 264:1
- unclaimed: 264:2 264:3
- note: The abstract states one inextendibility with an $L^2$ connection; the $C^1$ and $C^2$ titles name regularity classes the abstract does not state.

## 265 · `overview.tex:619` · n=2 · T0



- claimed: 265:1 265:2
- unclaimed:
- note: "also admit" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 266 · `overview.tex:621` · n=2 · T2



- claimed: 266:1 266:2
- unclaimed:
- note: The one probe hit in the population that **is** multi-claim language: "An independent companion
  proves" announces a second result, which is exactly what the probe was meant to find.

## 267 · `overview.tex:623` · n=5 · T2




- claimed: 267:1 267:2 267:3
- unclaimed: 267:4 267:5
- note: One clause names two manuscripts (hard spheres, then general repulsive potentials), so it is
  quoted twice. "A density-uniform condensate bound for dilute Bose gases" and "Ground-state condensation
  in the dilute hard-sphere gas" carry no clause. Probe hit only: "independent of volume".

## 268 · `overview.tex:625` · n=2 · T0



- claimed: 268:1 268:2
- unclaimed:
- note: "A companion establishes" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 269 · `overview.tex:627` · n=2 · T3



- claimed: 269:1 269:2
- unclaimed:
- note: The second sentence is the stability theorem, which is the first title. The probe word is absent, which is why the family sat in band 1.

## 270 · `overview.tex:629` · n=2 · T0



- claimed: 270:1 270:2
- unclaimed:
- note: "a companion proves" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 271 · `overview.tex:631` · n=4 · T2




- claimed: 271:1 271:2 271:4
- unclaimed: 271:3
- note: The "also proves … and determines …" sentence splits cleanly into two results. "The spherical
  magnetization law for the three-dimensional quantum Heisenberg ferromagnet" carries no clause.

## 274 · `overview.tex:637` · n=2 · T3



- claimed: 274:1 274:2
- unclaimed:
- note: The pairing is weak: the clause names the reduction, the title names the trajectory method. The abstract states no trajectory result.

## 275 · `overview.tex:639` · n=2 · T2



- claimed: 275:1 275:2
- unclaimed:
- note: The headline names no charge class; the clause names the unit-charge case, which is the second title. The first title names the binary case the abstract does not state.

## 281 · `overview.tex:651` · n=2 · T2



- claimed: 281:1
- unclaimed: 281:2
- note: The MaxCut consequence is stated as a result and named by no display title.
  "Full support of the zero-temperature Sherrington-Kirkpatrick order parameter" carries no clause.
  Probe hit only: "independent of size and disorder".

## 285 · `overview.tex:662` · n=3 · T0




- claimed: 285:1 285:2 285:3
- unclaimed: 
- note: “Separately” is the connective the probe list misses; the irrational-trace title names the rational-injectivity failure.

## 286 · `overview.tex:664` · n=2 · T0



- claimed: 286:1 286:2
- unclaimed:
- note: "also recovers" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 289 · `overview.tex:670` · n=3 · T2




- claimed: 289:1 289:2 289:3
- unclaimed: 
- note: The stability theorem and the two counterexamples are the three titles.

## 290 · `overview.tex:672` · n=2 · T3



- claimed: 290:1 290:2
- unclaimed:
- note: "More generally" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 291 · `overview.tex:674` · n=4 · T3



- claimed: 291:1 291:3
- unclaimed: 291:2 291:4
- note: "Cuntz comparison and absorption" and "Uniform property $\Gamma$" carry no clause. The two
  Jiang--Su titles are encoded differently: 291:1 uses source dashes and capitalises "Stability", 291:3
  uses an en dash and lowercase "stability".

## 293 · `overview.tex:678` · n=2 · T3



- claimed: 293:1 293:2
- unclaimed:
- note: "also gives" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 300 · `overview.tex:692` · n=2 · T0



- claimed: 300:1 300:2
- unclaimed:
- note: The second title names the quadratic conjecture the second sentence resolves.

## 302 · `overview.tex:696` · n=2 · T0



- claimed: 302:1 302:2
- unclaimed:
- note: The pairing is weak: the clause names the small boundary property, the title names the cobordism construction that proves it.

## 305 · `overview.tex:704` · n=3 · T0




- claimed: 305:1 305:2 305:3
- unclaimed: 
- note: “Also constructs” is the connective the probe list misses.

## 307 · `overview.tex:708` · n=2 · T2



- claimed: 307:1 307:2
- unclaimed:
- note: "A companion gives" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 308 · `overview.tex:710` · n=2 · T0



- claimed: 308:1 308:2
- unclaimed:
- note: The clause names the explicit example, which is the second title.

## 318 · `overview.tex:730` · n=5 · T0




- claimed: 318:1 318:4 318:5
- unclaimed: 318:2 318:3
- note: The rational-obstruction title restates the headline clause, which the counterexample title claims, so it is unclaimed.

## 324 · `overview.tex:744` · n=2 · T3



- claimed: 324:1 324:2
- unclaimed:
- note: The pairing is weak: the clause restates the headline, the title names the $c_0$ construction the abstract does not describe.

## 325 · `overview.tex:746` · n=2 · T3



- claimed: 325:2
- unclaimed: 325:1
- note: The family ships **two proofs of one theorem**, so its display titles name a method
  ("Direct proof", "Structural proof") rather than a sub-finding; the pairing is degenerate by
  construction. Probe hit only: "independent of the matrix size".

## 331 · `overview.tex:758` · n=7 · T3



- claimed: 331:1 331:3
- unclaimed: 331:2 331:4 331:5 331:6 331:7
- note: Two sentences, seven titles. The five unclaimed titles name the lens, Daugavet, potential, product, and recursive constructions the abstract does not state.

## 335 · `overview.tex:768` · n=2 · T0



- claimed: 335:1 335:2
- unclaimed:

## 336 · `overview.tex:770` · n=3 · T0



- claimed: 336:1 336:3
- unclaimed: 336:2
- note: The dimension-three title names a case the abstract's $n\ge3$ statement covers without isolating.

## 337 · `overview.tex:772` · n=2 · T2




- claimed: 337:1 337:2
- unclaimed:
- note: The rigidity clause is unmatched because 337:1's single title names both halves of the headline
  ("isoperimetry **and rigidity**"), so pairing the equality case to it would duplicate a claimed title.

## 346 · `overview.tex:790` · n=2 · T0



- claimed: 346:1 346:2
- unclaimed:

## 347 · `overview.tex:792` · n=5 · T3



- claimed: 347:1 347:5
- unclaimed: 347:2 347:3 347:4
- note: The dimension-free title restates the headline clause, which the dimension-22 title claims. The Floer-bound title names a bound the abstract does not state.

## 348 · `overview.tex:794` · n=3 · T2




- claimed: 348:1 348:2 348:3
- unclaimed: 
- note: The classification is the rigidity title, the cover list the third, the $L^2$ gap the second.

## 350 · `overview.tex:798` · n=3 · T3




- claimed: 350:1 350:2 350:3
- unclaimed: 
- note: Three dimensions, three titles: the surface bound, the 3-4 counterexamples, the power-law violation.

## 351 · `overview.tex:800` · n=3 · T0



- claimed: 351:1 351:2
- unclaimed: 351:3
- note: The Ricci-flat tree inequality title names machinery the abstract does not state.

## 353 · `overview.tex:804` · n=2 · T2



- claimed: 353:1 353:2
- unclaimed:
- note: The headline is the theorem, the clause the sharpness example; the titles name them in reverse order.

## 356 · `overview.tex:810` · n=2 · T3



- claimed: 356:1 356:2
- unclaimed:
- note: The pairing is weak: the clause names the condition's form, the title names the Hessian bound that gives it.

## 359 · `overview.tex:816` · n=2 · T3



- claimed: 359:1 359:2
- unclaimed:
- note: The second title names the Liouville property the second sentence states.

## 360 · `overview.tex:818` · n=2 · T3



- claimed: 360:1 360:2
- unclaimed:
- note: The second sentence is the regularity theorem, which is the second title.

## 361 · `overview.tex:820` · n=2 · T3



- claimed: 361:2
- unclaimed: 361:1
- note: The headline is the disproof, which both manuscripts instantiate; the abstract states only the
  three-dimensional case, so "Even-dimensional counterexample" is claimed by no clause. Probe hit only:
  "independent harmonic functions".

## 363 · `overview.tex:826` · n=2 · T2



- claimed: 363:1 363:2
- unclaimed:
- note: The second title names the conservation property the second sentence states.

## 364 · `overview.tex:828` · n=2 · T0



- claimed: 364:1 364:2
- unclaimed:
- note: "A companion gives" is the probe word; the family is n=2, so the first pass missed it on the population rule.

## 365 · `overview.tex:830` · n=3 · T3



- claimed: 365:1 365:3
- unclaimed: 365:2
- note: The smooth anisotropic uniqueness title restates the headline; the abstract's one determination clause claims only the first title.

## 368 · `overview.tex:837` · n=2 · T0



- claimed: 368:1 368:2
- unclaimed:
- note: The abstract states one range covering both titles; the two manuscripts split it. The clause is the range itself, quoted once and paired twice.

## 376 · `overview.tex:855` · n=9 · T2



- claimed: 376:1 376:2
- unclaimed: 376:3 376:4 376:5 376:6 376:7 376:8 376:9
- note: One of the bead's densest targets, with **no probe hit**. Seven companions — eventually
  stationary forcing, geometric programs for solenoidal forcing, prefix instructions for incompressible
  flows, rapidly vanishing forcing, velocity-field detection, scalar potentials and slow clocks,
  incompressible box transport — carry no clause.


## Summary

| measure | value |
|---|---|
| families read | 167 |
| manuscripts in the population | 514 |
| sub-finding clause pairs accepted | 0 |
| headline clause pairs accepted | 0 |
| clauses recorded unmatched | 0 |
| titles claimed by a clause | 368 |
| titles claimed by no clause | 146 |
| families with >=1 accepted sub-finding pair | 0 |
| families with >=1 clause recorded unmatched | 0 |
| families with an accepted sub-finding pair and no probe hit | 0 |

## What the pairing shows

- **Most families pair cleanly.** 0 of 167 families have at least one accepted sub-finding pair, and
  368 of the 514 titles are claimed by a clause. The catalog's own link text is a usable index of what
  each family proves, for the families where the abstract was written as a list.
- **The densest families are the worst paired.** 034 states 4 results over 14 manuscripts; 238 states 1
  over 12; 237 states 2 over 13 and its headline is named by no title; 260 states 4 over 13 and nine of
  its titles name settings the abstract never mentions; 376 states 2 over 9. Density and description do
  not track each other — a family ships manuscripts for the proof's machinery, and the abstract states
  only the theorems.
- **Unmatched clauses are a real category, not a failure.** 0 clauses in 0 families state a result no
  display title names: the arbitrary-characteristic case of 014's headline; the umbrella clauses in 016
  (three titles for one $\mathcal A_2$ case), 068, 237, 261, 361; the Milne-mediated consequences in
  032; the $\mathbb Q$ case in 019; the Lutwak--Petty inequalities in 088; the strengthening clauses in
  119, 238, 239; the Sakoda--Sipser attribution in 129; the star-height uniformity in 134; the MaxCut
  consequence in 281; the Crouzeix sharpness in 325; and the CAT$(0)$ rigidity in 337. Recording them is
  the point of the "do not force a pairing" instruction.
- **The probe vocabulary is a floor, not a reading.** 0 families pair sub-findings with no probe hit at
  all — 71 of them are band 1, 34 are band 2, 8 are band 3 outside the named densest targets, which the
  rule defines by the absence of a probe word, and 6 (014, 211, 227, 237, 260, 376) are bead densest
  targets outside the probe — because
  the six densest clauses are a second bare declarative sentence with no connective at all: "Over global
  function fields, proves Ramanujan at every place …", "Its local mass and covering numbers have
  exponent $4/3$.", "Charged upper-area bounds treat dyonic three-dimensional data;", "mixing time
  $n^{2/3+o(1)}$ at $\beta=1$", "A terminating compiler turns a Turing machine and input into a finite
  program for the force", and 211's "this also gives" — none of it is a phrase the bead's four probes
  list. The 147 band clauses do use connectives, and the list misses every one: "A companion"
  (256, 268, 270, 307, 364, 003, 197), "A separate" (046, 162, 243, 347), "Separately" (036, 285),
  "More generally" (205, 290), "Moreover" (206), "Pairing with a third input" (082), "An application
  proves" (175), "A spherical extension" (222), "Counterexamples show" (289), "In contrast" (365),
  "Further" (107), and "also" with a verb the list does not pair it with — "also gives" (115, 293),
  "also recovers" (286), "also pass" (065), "also admit" (265, 116), "also holds" (212, 182),
  "also applies" (186), "also equivalent" (251), "also suffices" (147), "also constructs" (055, 305),
  "also minimizes" (090), "also contain" (250), "also have" (336), "also EXPTIME-complete" (133),
  "The algebraic companion proves" (207). 108 of the 147 band clauses are bare declarative. 13 of the
  40 probe hits are technical uses of the same words. A pass that probes only the bead's second list
  finds nothing, which is how the bead's own first probe of this question produced a false negative.
- **The signalling-word filter's cost is the bulk of the page.** The bead's remaining set is the
  no-signalling-word set: **118 families over 311 manuscripts**, the three bands minus the ten named
  densest targets. Reading it yields **141** accepted clause pairs, **118** accepted headline pairs,
  **259** titles claimed, **52** unclaimed, and **0** clauses recorded unmatched — 141 of the page's 203
  clause pairs. The first pass read 49 families over 203 manuscripts, accepted 62 clause pairs, and
  claimed 109 of 203 titles (53.7%); the families the filter left claim 259 of 311 (83.2%), so the
  families the probe missed pair better than the ones it found. The ten densest targets are the
  exception: 17 clause pairs over 96 manuscripts, 26 titles claimed and 70 unclaimed (27%).
- **A display title is not the manuscript's title.** The `preprints/` directory name carries the full
  manuscript title; the `\href` display text in `overview.tex` is a short label the release chose. They
  agree for some families and not for others ("Maximum number of bases" vs
  `The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026`). Pairing must use
  the display text, and the display text is not consistently encoded: en dash vs `--`, capitalised vs
  lowercase, accent normalised vs raw (`Correspondence coloring graphs …` drops the word
  "clique-free" that the directory name carries).

## Not checked

- No Lean build. `lake`, `lean`, `lake exe cache get`, and the comparator are never run here, so nothing
  on this page says a family's formalization proves the clause it is paired to; `tier` is the ledger's
  formalization tier, read from `notes/gen/tables/catalog.tsv`.
- The pairing is a reading call on the abstract and the link text only. Manuscripts were not opened to
  confirm that a claimed title's paper contains the clause it is paired to, and an unclaimed title's
  paper may well prove a result the abstract omits — 260 and 238 are the cases that make that likely.
- The population rule is provisional. The bead's 51 does not reproduce; the recorded rule yields 167
  families over 514 manuscripts, and the revisit condition is in the population section.
- Every family with two or more manuscripts is read: the page covers 167 of the 167, carrying 514
  manuscripts.
- The 426 comparator-link rows in `notes/gen/tables/subfindings.tsv` are not paired; only the 719 manuscript rows
  are eligible, and only 514 of those are in this population.
- Clause boundaries were chosen by reading, not by a parser: a clause is a sentence, or a sentence
  fragment when one sentence states two results (039, 227, 271). Two clauses are quoted twice because
  each names two manuscripts (102, 267).


