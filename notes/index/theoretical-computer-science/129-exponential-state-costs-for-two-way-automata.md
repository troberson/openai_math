# 129 — Exponential state costs for two-way automata

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/129.md`](../../../lean/docs/129.md) |
| Comparator configs | 3 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | resolution, bound |
| Topics | [complexity-theory](../topics/complexity-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026`](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/) | [paper.pdf](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf) | [build/](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/) | [README.md](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/paper.tex) | — |
| [`An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026`](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/) | [main.pdf](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf) | [build/](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/) | [README.md](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/README.md) | yes | [main.tex](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [OneWayLiveness](../../../lean/ComparatorChallenges/OneWayLiveness.json) | `OAI.OneWayLiveness.main_theorem` | [Main.lean](../../../lean/OAI/Combinatorics/Automata/Main.lean) | [`OAI/Combinatorics/Automata`](../../../lean/OAI/Combinatorics/Automata/) |
| [TwoWayComplementation](../../../lean/ComparatorChallenges/TwoWayComplementation.json) | `OAI.TwoWayComplementation.complementation_lower_bound_finite` | [Main.lean](../../../lean/OAI/Combinatorics/TwoWayAutomata/Main.lean) | [`OAI/Combinatorics/TwoWayAutomata`](../../../lean/OAI/Combinatorics/TwoWayAutomata/) |
| [TwoWayDeterminization](../../../lean/ComparatorChallenges/TwoWayDeterminization.json) | `OAI.TwoWayComplementation.explicit_family_main` | [ExplicitFamily.lean](../../../lean/OAI/Combinatorics/TwoWayAutomata/ExplicitFamily.lean) | [`OAI/Combinatorics/TwoWayAutomata`](../../../lean/OAI/Combinatorics/TwoWayAutomata/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `OneWayLiveness` | [.json](../../../lean/ComparatorChallenges/OneWayLiveness.json) | [.lean](../../../lean/ComparatorChallenges/OneWayLiveness.lean) | 1 | 0 | no | yes |
| `TwoWayComplementation` | [.json](../../../lean/ComparatorChallenges/TwoWayComplementation.json) | [.lean](../../../lean/ComparatorChallenges/TwoWayComplementation.lean) | 1 | 0 | no | yes |
| `TwoWayDeterminization` | [.json](../../../lean/ComparatorChallenges/TwoWayDeterminization.json) | [.lean](../../../lean/ComparatorChallenges/TwoWayDeterminization.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves exponential lower bounds both for complementing two-way nondeterministic finite automata and for simulating one-way nondeterministic automata by two-way deterministic ones. The latter resolves the Sakoda--Sipser state-succinctness conjecture over growing finite alphabets; both results rule out polynomial state bounds independent of alphabet size.

