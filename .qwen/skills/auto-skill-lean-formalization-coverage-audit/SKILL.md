---
name: lean-formalization-coverage-audit
description: Measure how much of a manuscript collection is actually formalized in an accompanying Lean library, and report the gap without overstating what it proves.
source: auto-skill
extracted_at: '2026-10-07T05:29:45.327Z'
---

# Auditing Lean formalization coverage

Use when asked how much of a paper/manuscript collection is formalized, how complete the
formal proofs are, or what the formalization gap is. Worked out on the OpenAI Research
Catalog (`/home/tamara/Downloads/_Git/math`): 722 manuscripts, 372 families, a 25.9M-line
`OAI/` Lean library.

## 1. Report coverage as separate layers — never as one percentage

The catalogue records coverage at four layers that **do not agree**. Averaging them, or
picking one and calling it "the coverage", is the main way to get this wrong.

| Layer | Where it lives | Catalog value |
|---|---|---|
| Manuscripts with a formalized main result | `formalization.yaml` → `sources:` (`id: ../preprints/<dir>/<file>.pdf`) | 162 / 722 |
| Families with a scope note | `lean/docs/<NNN>.md` | 235 / 372 |
| Statement/solution pairs | `lean/ComparatorChallenges/*.json` (+ matching `.lean`) | 405 |
| Catalogued main results | `formalization.yaml` → `status.main_results` (`comparator_config:` / `declaration:` / `file:`) | 185 entries, 178 unique configs |

- Count entries with `grep -c 'comparator_config:'`, then `sort -u` the extracted names —
  some configs appear 2–3× (multiple main declarations per challenge). Entries ≠ unique configs.
- Challenges not listed in `main_results` are companion/secondary statements, not failures.
  They are still linked from a family scope note.
- `status.scope`, `automation.methods`, and `review.status` are the release's own statement of
  how the proofs were produced. Quote them verbatim; they set the ceiling on any claim of verification.

## 2. `solution_module` is an import shim — follow the transitive closure

The decisive measurement (are the proofs complete?) requires resolving imports. A comparator
config points at a module whose file is often **one line**:

```json
{ "solution_module": "OAI.Geometry.BallPacking.Necessity.Main",
  "theorem_names": ["OAI.HigherDimensionalBallPacking.packing_necessity"] }
```

```console
$ cat OAI/Geometry/BallPacking/Necessity/Main.lean
import OAI.Geometry.BallPacking.Necessity.PackingNecessity
```

Checking that file for `sorry` finds nothing and proves nothing. Build a module→file index
(`mod2file`), parse `^\s*import\s+([A-Za-z0-9_.]+)` per file, and walk the closure:

```python
def closure(mod):
    seen, stack, bad = set(), [mod], []
    while stack:
        cur = stack.pop()
        f = mod2file.get(cur)
        if f is None: bad.append(cur); continue   # Mathlib / external deps: expected
        if f in seen: continue
        seen.add(f); stack.extend(imports[f])
    return seen, bad
```

Aggregate `sorry`, `axiom`, `native_decide`, line counts over the closure. Cache per-file
declaration sets — scanning 121k files once is fine; rescanning a closure per declaration name
is not.

## 3. Three false-positive traps (all three bit me)

- **Paths with parentheses.** `preprints/Sharp-integral-fillings-in-CAT(0)-spaces-.../paper.pdf`
  breaks `\(preprints/([^)]+\.pdf)\)` and silently loses a manuscript. Use
  `preprints/(?:[^\s()]|\([0-9]+\))*\.pdf`. My first pass reported 721 of 722 and I nearly
  reported a missing entry in `CONTENTS.md`.
- **Namespace-qualified declarations.** `OAI/RepresentationTheory/RowColumn/Occupied.lean:274`
  is `theorem RowColumn.occupied_overlap` inside `namespace OAI`. Matching the last dotted
  segment (`occupied_overlap`) against a captured leading identifier finds nothing → 7 phantom
  "missing declarations". Match the qualified tail against the file text, not against a
  single-token capture.
- **`axiom` in prose.** `^\s*axiom\s` matches doc-comment text
  (`/- ... the axiom of choice is used ... -/`). All 3 "axioms" in the library were comments.
  Read the matched line before reporting an axiom.

## 4. Say what a zero-`sorry` result does and does not mean

Zero `sorry` across 25.9M lines is a **source-level** fact. It does not mean the library
elaborates, and it is not verification. State the distinction explicitly, then give the
command that produces the checked fact:

```sh
lake update && lake exe cache get
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
```

That needs `comparator`, `landrun`, `lean4export` on `PATH` and a full build. If you have not
run it, say so. Do not present a source scan as a comparator pass, and never as peer review.

## 5. Attribute the gap by discipline

Map family → discipline from `overview.tex` section order (`\cataloguesection{...}{n}` sets the
current discipline; each following `\resultentry{NNN}{...}` belongs to it). Family → manuscripts
comes from `CONTENTS.md` (`**NNN. Title**` headers, then `(preprints/...pdf)` links). Then tabulate
per discipline: families, families with a scope note, manuscripts, formalized manuscripts.

Expect strong skew. Catalog result: Topology 3/18 families and 1/26 manuscripts covered,
algebraic geometry 7/36 and 7/89, versus functional analysis 10/11 and 16/19, logic 6/6 and 5/8.

Worth checking separately: **the marquee results.** Ten of the twelve headline number-theory
families (Milne, full BSD, Hilbert's tenth over ℚ, Goldfeld, Fontaine–Mazur at 2,
Ford–Konyagin–Luca, restricted geometric Langlands, Zilber–Pink, Margulis–Platonov, p-adic
section) have no scope note, while all 10 families with published reasoning traces do. Lead
with that pattern when it holds — coverage tracks what the release chose to expose to checking,
not what the community will scrutinize.

## 6. Reading the scope notes

`lean/docs/<NNN>.md` has an explicit **Scope** section stating what the Lean result covers and
what it excludes (003: the paper's later applications are not formalized; no explicit
Landau–Siegel constant). Quote exclusions when judging a result. Absence of a formalization
carries little signal in a collection where most manuscripts are unformalized — do not treat it
as a red flag.

## 7. Tooling notes

- `rg -f patterns.txt` with patterns ending in `\n` fails even with `-U` ("the literal `\n`
  is not allowed in a regex"). For per-file declaration sets, scan in Python.
- Building the graph over 121,734 files takes ~1 min; pickle it (`/tmp/graph.pkl`) so follow-up
  questions don't rescan.
- `du -sh lean/OAI` ≈ 1.7 GB. Compiling the whole library can fail on low `vm.max_map_count`;
  see `lean/README.md` (`-DMMAP=OFF`, `GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1`).
- Also worth counting: `preprints/*/verification/` dirs (reproducible arithmetic checks, 30 in
  the catalog) and their `COVERAGE.md` limits files.
