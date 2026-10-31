# Proof-level faithfulness audits

2 per-family audits comparing a preprint's proof with its Lean formalization. The
statement-level comparison is family-specific; the proof-level comparison follows the
shared protocol in the data file [`README.md`](../../data/proofs/README.md) — the
"lost in translation" failure modes, the seven extraction targets, the reparameterization
test, and the sign audit.

Each page is rendered by `build_proofs.py` from a hand-edited data file
(`notes/data/proofs/<NNN>.md`) and the page skeleton; the checker
(`verify_proofs.py`) measures the rendered bytes and writes nothing.

## The pages

- [072](./072.md) — Brennan's conjecture and a counterexample to Kraetzer's prediction
- [091](./091.md) — The logarithmic Brunn–Minkowski conjecture

## Not checked

- A green page proves the citation surface, not the mathematics: it names the lines each
  quote sits on, and those lines are what they say. It does not re-derive the proof.
- Nothing in this repo builds, and no Lean run was made here; a Lean statement is evidence
  the claim was stated and proved by the agent, not independently verified.
