# 104 — Quasipolynomial algorithms for mean-payoff, stochastic and parity games

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 4 (1 formalized at source level) |
| Scope note | [`lean/docs/104.md`](../../../lean/docs/104.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | — |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) · [game-theory](../topics/game-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026`](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/) | [paper.pdf](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) | [build/](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/) | [README.md](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/README.md) | no | [main.tex](../../../preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex) | — |
| [`Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026`](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/) | [mean-payoff-parity.pdf](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf) | [build/](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/) | [README.md](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/README.md) | no | [main.tex](../../../preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/build/main.tex) | — |
| [`Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026`](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/) | [paper.pdf](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) | [build/](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/) | [README.md](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/build/source/main.tex) | — |
| [`Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026`](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/) | [stochastic-mean-payoff-games.pdf](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf) | [build/](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/) | [README.md](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/README.md) | no | [main.tex](../../../preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/build/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [RandomizedMeanPayoff](../../../lean/ComparatorChallenges/RandomizedMeanPayoff.json) | `OAI.randomized_quasipolynomial_mean_payoff` | [Main.lean](../../../lean/OAI/Computability/RandomMean/Main.lean) | [`OAI/Computability/RandomMean`](../../../lean/OAI/Computability/RandomMean/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `RandomizedMeanPayoff` | [.json](../../../lean/ComparatorChallenges/RandomizedMeanPayoff.json) | [.lean](../../../lean/ComparatorChallenges/RandomizedMeanPayoff.lean) | 1 | 0 | no | yes |
| `TruffetCounterexample` | [.json](../../../lean/ComparatorChallenges/TruffetCounterexample.json) | [.lean](../../../lean/ComparatorChallenges/TruffetCounterexample.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives deterministic algorithms using $2^{O((\log(L+2))^2)}$ bit operations, for complete binary input length $L$, for ordinary mean-payoff games and two separate extensions. They compute exact values and optimal positional strategies in ordinary games, the nonnegative expectation-of-liminf value set in turn-based stochastic games, and the winning set for nonnegative liminf mean payoff conjoined with parity. Signed rewards, rational chance probabilities, and parity priorities are unrestricted and binary-encoded.

