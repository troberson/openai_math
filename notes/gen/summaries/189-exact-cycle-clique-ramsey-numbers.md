[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 189](../index/combinatorics/189-exact-cycle-clique-ramsey-numbers.md)

# 189 — Exact cycle–clique Ramsey numbers

[Index page](../index/combinatorics/189-exact-cycle-clique-ramsey-numbers.md)

## Original CONTENTS.md summary

The release's blurb [S1:4368] and the catalog abstract [S2:459]
state the family's claim: the Erd–Faudree–Rousseau–
Schelp cycle–clique Ramsey conjecture,
$R(C_m,K_n)=(m-1)(n-1)+1$ for every $m \geq n \geq 3$,
except $R(C_3,K_3)=6$. This is the exact threshold, in a
red–blue coloring of a complete graph, forcing a red
$m$-cycle or a blue $n$-clique. The manuscript is
*Cycle–clique Ramsey numbers* [S3:26, S3:28]; its abstract


> We prove that $R(C_m,K_n)=(m-1)(n-1)+1$ for every pair of integers
$m\ge n\ge3$ other than $(m,n)=(3,3)$, for which $R(C_3,K_3)=6$.
This establishes the cycle–clique conjecture of Erdős, Faudree,
Rousseau and Schelp. The proof combines expansion in a
minimal counterexample with a large-clique lemma and an optimization of
paths joining clique vertices. These arguments reduce the remaining cases
to $3{,}099$ finite parameter-pattern instances, which are excluded by two exact
implementations of proved inference rules. Complete programs and deduction
traces accompany the paper. [S3:32–40]

## Undergraduate summary

A **Ramsey number** $R(G,H)$ is the smallest number of dots
such that, however you paint every edge connecting them
red or blue, you **must** find either a red copy of $G$ or a
blue copy of $H$. A **cycle** $C_m$ is a ring of $m$ dots
(each joined to its two neighbors and no others); a **clique**
$K_n$ is a group of $n$ dots all joined to each other.
Coloring a complete graph's edges red and blue, the question
is: what is the minimum number of dots that forces either a
red ring of $m$ dots or a blue complete set of $n$ dots?
This manuscript gives the **exact** answer — a single
formula $(m-1)(n-1)+1$ that works for every $m \geq n
\geq 3$, with one exception (the $(3,3)$ case, where the
answer is $6$) [S3:32–40, S2:459].

## Graduate summary

**The main theorem** [S3:32–40, S4:9]. For every pair
of integers $m \geq n \geq 3$ other than $(3,3)$:
$R(C_m, K_n) = (m-1)(n-1)+1$. For the exceptional case:
$R(C_3, K_3) = 6$ [S4:9, S5:23–27]. The proof combines
expansion in a minimal counterexample with a large-clique
lemma and an optimization of paths joining clique vertices;
the arguments reduce the remaining cases to $3{,}099$ finite
parameter-pattern instances, excluded by two exact
implementations of proved inference rules
[S3:32–40].

**The scope of the formalization.** The scope note states
the formalization proves $R(C_m,K_n)=(m-1)(n-1)+1$ for all
integers $m \geq n \geq 3$ except $(m,n)=(3,3)$, where it
proves $R(C_3,K_3)=6$ — the **complete parameter range**
of the paper's main theorem [S4:9]. The scope note names one
comparator [S4:15]: `CycleCliqueRamsey.lean`.

## History of the conjecture

The **cycle–clique Ramsey conjecture** was posed by
Erd–Faudree, Rousseau, and Schelp as a unification of
the cycle–cycle and clique–clique Ramsey
problems. The formula $(m-1)(n-1)+1$ is the natural
"product + one" guess for the threshold, and the conjecture
asserts it is exact. The $(3,3)$ exception — a triangle
versus a triangle — is the one case that does not fit
the formula (the answer is $6$, not $(3-1)(3-1)+1 = 5$).
Prior work established the bound for restricted ranges and
for the cycle–cycle case, but the full
cycle–clique formula was open. This manuscript closes
it, with a proof that is largely a **finite certificate**:
the arguments reduce to $3{,}099$ parameter-pattern
instances, excluded by two exact implementations of proved
inference rules, with complete programs and deduction traces
accompanying the paper [S3:32–40, S2:459].

**Prior (my training data, not this repo).** I know the
cycle–clique Ramsey conjecture of
Erd–Faudree, Rousseau, and Schelp as a named open
problem in Ramsey theory, and that the $(3,3)$ exception is
the well-known case where the formula breaks. A **complete
proof of the full parameter range** via expansion, large-
clique lemmas, and a $3{,}099$-instance finite certificate
with two exact inference-rule implementations is not
something I can independently verify from training alone.

## Consequences

**The Erd–Faudree–Rousseau–Schelp cycle–
clique Ramsey conjecture is resolved.**
$R(C_m,K_n)=(m-1)(n-1)+1$ for every $m \geq n \geq 3$
except $(3,3)$, where $R(C_3,K_3)=6$ [S3:32–40, S4:9,
S2:459].

**The proof is a finite certificate.** The general argument
reduces to $3{,}099$ parameter-pattern instances, excluded
by two exact implementations of proved inference rules,
with complete programs and deduction traces
[S3:32–40].

## Section skeleton

One manuscript [S3:32–40] (title [S3:26], date [S3:28]) —
`main.tex` (62 lines) under `build/`, with sections under
`build/sections/` including a `02-reduction` and a
`clique-figure` section. The family ships one
`verification/` **certificate bundle** (the $3{,}099$-
instance inference-rule programs and deduction traces), not
a Lean proof [S3:32–40].

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization proves
$R(C_m,K_n)=(m-1)(n-1)+1$ for all integers
$m \geq n \geq 3$ except $(m,n)=(3,3)$, where it proves
$R(C_3,K_3)=6$ — the complete parameter range of the
paper's main theorem. The scope note names one comparator
[S4:15]: `CycleCliqueRamsey.lean`.

**The structural absence.** The family is at tier T2: the
ledger row records `mainres 0` and `paps_form 0`.
`formalization.yaml` carries **no** `main_results` entry for
this family and the manuscript is **not** in its `sources:`
listing. The comparator `CycleCliqueRamsey.lean` defines
`cycleCliqueRamsey` and restates the target
`theorem thm_main` — a two-term conjunction: the
general case
$(\forall\, m\, n : \mathbb{Z},\, n \leq m \to 3
\leq n \to (m,n) \neq (3,3) \to
\text{cycleCliqueRamsey}\, m\, n = (m-1)(n-1)+1)$ and
the exceptional case
`cycleCliqueRamsey 3 3 = 6` — with a bare `sorry` body
[S5:18–27]:

```lean
theorem thm_main :
    (∀ m n : ℤ, n ≤ m → 3 ≤ n → (m, n) ≠ (3, 3) →
      (cycleCliqueRamsey m.toNat n.toNat : ℤ) = (m - 1) * (n - 1) + 1) ∧
    cycleCliqueRamsey 3 3 = 6 := by
  sorry
```
[S5:23–27]

**What the OAI tree does carry.** The
`OAI/Combinatorics/Ramsey/CycleClique` package (**443 files
over 2,795,707 lines, zero `sorry`**) carries a **real,
non-`sorry`** proof of the comparator's target. The
`MainTheorem.lean` `theorem thm_main` [S6:23–43]
discharges the conjunction by `constructor`: the first
conjunct translates the integer hypotheses to naturals via
`omega`, applies the `main` general-case lemma
`main m.toNat n.toNat hmnN hnN hneN`, and casts the
natural-arithmetic identity to integers by
`congrArg` and `simpa`; the second conjunct is discharged
by the `exceptional` lemma 

```lean
theorem thm_main :
    (∀ m n : ℤ, n ≤ m → 3 ≤ n → (m, n) ≠ (3, 3) →
      (cycleCliqueRamsey m.toNat n.toNat : ℤ) = (m - 1) * (n - 1) + 1) ∧
    cycleCliqueRamsey 3 3 = 6 := by
  constructor
  · intro m n hmn hn hne
    have hmnN : n.toNat ≤ m.toNat := by omega
    have hnN : 3 ≤ n.toNat := by omega
    have hneN : (m.toNat, n.toNat) ≠ (3, 3) := by
      intro he
      have hm3 := congrArg Prod.fst he
      have hn3 := congrArg Prod.snd he
      have hm3' : m = 3 := by omega
      have hn3' : n = 3 := by omega
      exact hne (by simp [hm3', hn3'])
    have h := main m.toNat n.toNat hmnN hnN hneN
    have hmcast : ((m.toNat - 1 : ℕ) : ℤ) = m - 1 := by omega
    have hncast : ((n.toNat - 1 : ℕ) : ℤ) = n - 1 := by omega
    have hcast := congrArg (fun a : ℕ => (a : ℤ)) h
    simpa only [Nat.cast_add, Nat.cast_mul, Nat.cast_one, hmcast, hncast] using hcast
  · exact exceptional
```
[S6:23–43]

The proof closes with `exact exceptional` for the
$(3,3)$ conjunct — a closed argument, no `sorry`
[S6:23–43].

**Registration, not proof.** The OAI tree proves the
comparator's `thm_main` in full, but the release registered
neither a `main_results` entry nor a `sources:` listing for
it — the gap between the tree and the ledger is one of
**registration**, not of proof. The comparator json names
`OAI.Combinatorics.Ramsey.CycleClique.Main` as the solution
module and `OAI.CycleClique.thm_main` as the theorem, so the
release set the target and the tree answered it; the ledger
simply does not carry that answer. The family also ships a
`verification/` certificate bundle [S3:32–40] as its
non-Lean evidence surface. The release records
`scope: "Partial progress."` and `review: status:
unchecked`; the comparator's `sorry` is the target the
release set, and the proved `thm_main` in the OAI tree is
the result the tree carries without a ledger entry.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 189 at [S1:4368] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{189} at [S2:459] |
| S3 | [`preprints/Cycle-clique-Ramsey-numbers-September-25-2026/build/main.tex`](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/build/main.tex) | 62 | the single manuscript root; title [S3:26], date [S3:28], abstract [S3:32–40] |
| S4 | [`lean/docs/189.md`](../../../lean/docs/189.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:15] |
| S5 | [`lean/ComparatorChallenges/CycleCliqueRamsey.lean`](../../../lean/ComparatorChallenges/CycleCliqueRamsey.lean) | 31 | the comparator: the `cycleCliqueRamsey` definition [S5:18–19], the `thm_main` theorem [S5:23–26] and the `sorry` [S5:27] |
| S6 | [`lean/OAI/Combinatorics/Ramsey/CycleClique/MainTheorem.lean`](../../../lean/OAI/Combinatorics/Ramsey/CycleClique/MainTheorem.lean) | 47 | the OAI tree (443 files, 2795707 lines, 0 sorry): the real `thm_main` proof [S6:23–43] via the `main` general-case lemma and the `exceptional` (3,3) case |
