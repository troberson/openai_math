---
name: lean-elaborate-without-mathlib
description: Get proofs in a large Lean library to actually elaborate when Mathlib is absent — find the
  toolchain-core-only closure, build it with plain `lean` (no lake, no cache), and prove the proofs are
  real with `#print axioms`.
source: auto-skill
extracted_at: '2026-10-08T06:47:59.202Z'
---

# Elaborating Lean proofs without Mathlib

Use when someone asks "can we get one of the proofs to run?", "does this Lean build?", or "is this
proof checked?" in a repo whose Lean library depends on Mathlib that is **not installed**. Worked out
on `/home/tamara/Downloads/_Git/math` (`lean/OAI/`: 121,734 modules, 25.9M lines, 30 `require … from
git` in `lakefile.lean`, no `.lake`, Mathlib absent, 600 GB free).

The headline result: **you do not need lake, a cache, or Mathlib to elaborate a real subset.** On this
repo 19 of 121,734 modules elaborate with the toolchain core alone in 15.8 s, and 390 theorems come
out with zero `sorryAx`. The matching limit is equally worth knowing: **0 of the 180 unique
`main_results` files have a Mathlib-free closure**, so no headline theorem is reachable without
Mathlib. Measure both numbers; the second is what stops an overclaim.

## 1. Pick the buildable set by a closure rule, and name the rule

Two rules, two answers, and they are not interchangeable:

| Rule | Definition | Catalog yield |
|---|---|---|
| Mathlib-free | no module starting `Mathlib` in the transitive import closure | 46 |
| **core-only** | every import in the closure is an in-tree module **or** starts with `Init`/`Lean`/`Std` | **19** |

The gap is the trap. External git packages (`PrimeNumberTheoremAnd`, `ClassFieldTheory`,
`Schoenflies`, `StrongPNT`, `TauCeti`, `all`) are **unexpanded leaves** in an in-tree import graph:
they are not in the module index, so a Mathlib-only filter never sees that they import Mathlib
themselves. A "Mathlib-free closure" is therefore *not* "buildable without Mathlib". Use the
core-only rule for anything you intend to compile, and say which rule produced a number.

## 2. Compute the set by reverse propagation, not per-file closure

Per-file closure over 121k modules is O(n²) — I started it, it did not finish, and I stopped the
background task. The "reaches an external package" set is one BFS over the **reversed** import graph:

```python
mods = {str(f.relative_to('.').with_suffix('')).replace('/', '.'): f
        for f in pathlib.Path('OAI').rglob('*.lean')}
imports = {m: [l.split()[1] for l in mods[m].read_text(errors='replace').splitlines()
               if l.startswith('import ')] for m in mods}
CORE = ('Init', 'Lean', 'Std')
bad = {m for m, i in imports.items()
       if any(not x.startswith('OAI.') and not x.startswith(CORE) for x in i)}
reverse = collections.defaultdict(set)
for m, i in imports.items():
    for x in i:
        if x in mods: reverse[x].add(m)
stack = list(bad)
while stack:                      # anything importing a bad module is bad
    m = stack.pop()
    for dep in reverse[m]:
        if dep not in bad: bad.add(dep); stack.append(dep)
clean = sorted(set(mods) - bad)
```

Linear in edges, and it finishes in seconds.

**Module key is `str(f.relative_to('.').with_suffix('')).replace('/', '.')`.** Keying by the parent
directory (`'.'.join(parts[:-1])`) makes the walk print paths that do not exist on disk — it produced
`OAI/Geometry/Convex/GeneralMahler/Middle.lean` and `OAI/GameTheory/SnakyConditional/Regions.lean`
for me before I noticed.

## 3. Build with plain `lean`, in dependency order, into a scratch olean tree

`lake build` is not the tool here: it resolves all 30 git requires and pulls Mathlib transitively
(hours). Plain `lean` needs three things:

```bash
TC=~/.elan/toolchains/leanprover--lean4---v4.35.0-rc4      # the INSTALLED toolchain
OUT=/tmp/leanout; mkdir -p "$OUT"
for f in $(cat core_order.txt); do                          # dependencies first
  o="$OUT/${f%.lean}.olean"; mkdir -p "$(dirname "$o")"
  LEAN_PATH="$OUT" "$TC/bin/lean" -o "$o" -i "${o%.olean}.ilean" "$f"
done
```

- **`-o` takes a file, not a directory.** `-o "$OUT"` fails with
  `failed to write '/tmp/leanout': 21 Is a directory`. Lake's `-o <dir>` is a lake feature, not a lean
  one. Name the olean explicitly, mirroring the module path.
- **`LEAN_PATH` must contain the directory that holds the module prefix.** `OAI.Foo.Bar` resolves as
  `$LEAN_PATH/OAI/Foo/Bar.olean`, so the olean tree has to mirror the module path exactly. Getting
  this wrong reads `unknown module prefix 'OAI'` plus a listing of the search path.
- **Order matters.** Compute a topological order (depth-first on imports, append after recursing) and
  feed the loop that list.
- **elan proxies are not on PATH.** `lean`/`lake` live in `~/.elan/bin` as proxies. Invoke the
  installed toolchain binary directly (`~/.elan/toolchains/<toolchain>/bin/lean`) to avoid a download:
  a proxy run inside the repo reads `lean-toolchain` and auto-fetches the pinned toolchain. Here the
  repo pins `leanprover/lean4:v4.34.1` and only `v4.35.0-rc4` was installed, so the direct binary was
  the no-download path — and the honest report is "elaborates on a newer compiler than the pin", not
  "elaborates on the pinned compiler".
- Core libraries ship in the toolchain (`lib/lean/Init.olean`, `lib/lean/Lean/Elab/Tactic/Omega.olean`),
  so `omega` is available. `norm_num`, `linarith`, `positivity`, `nlinarith`, `ring`, `field_simp`,
  `norm_cast`, `simp_all`, `abel`, `aesop`, `gcongr`, `polyrith` are Mathlib tactics — a file using
  them is not core-only, and a token regex over the file text is a cheap second filter.

## 4. Prove the proofs are real: `#print axioms` on every theorem

Zero `sorry` in the source is a source-level fact. `#print axioms` is the kernel's statement: it only
succeeds for a declaration whose proof term has been type-checked, and `sorryAx` in the list means the
proof was never completed. Generate one line per theorem:

```
#print axioms OAI.PartitionPilot.Compression.RecursiveMaps.TaskSymmetry.next_composition
```

Catalog result over all 390 theorems in the 19 modules: 331 report a subset of
`[propext, Classical.choice, Quot.sound]`, 59 report **no axioms at all**, **0 mention `sorryAx`**.
Tabulate the distinct axiom sets (`tr '\n' ' ' | grep -o 'depends on axioms: \[[^]]*\]' | sort | uniq -c`)
and report `grep -c sorryAx` explicitly — that is the number the reader cares about.

**Fully-qualified names need a namespace stack, and `section` must be tracked as a sentinel.**
Reconstructing `OAI.<ns…>.<name>` from `namespace X` / `end X` lines works until a bare `end` closes a
`section`: popping the top of the stack then pops the enclosing *namespace*, and every later theorem in
the file gets the wrong prefix. First run: 80 `Unknown constant` errors, names like
`OAI.Compression.range_completion_from_accounting` missing the `PartitionPilot` segment. Fix:

```python
if re.match(r"^section\s*$", line): stack.append(SECTION)
...
elif en.group(1) == "":            # bare `end` pops the section sentinel first
    if stack: stack.pop()
...
names.append('.'.join([s for s in stack if s is not SECTION] + [th.group(1)]))
```

Also: `grep -c error` over the axiom log over-counts, because theorem *names* contain "error"
(`selected_roundCounts_error`). Check the exit code of `lean`, not the word count.

## 5. Join the buildable set to what the release calls a result

The interesting question is not "how many files compile" but "does any *named* result compile".

- `formalization.yaml` `main_results` entries are `(comparator_config, declaration, file)` triples.
  `build_catalog.parse_yaml()` returns a **tuple** `(set of manuscript paths, {config stem: count})`
  and carries **no file paths** — parse the triples yourself.
- Scope notes link the **`.lean`** stub (`[X.lean](../ComparatorChallenges/X.lean)`), not the `.json`.
  A regex for `\.json` in `lean/docs/*.md` finds nothing and the whole join silently reads empty.
- Config names contain dashes and dots: use `[A-Za-z0-9_.\-]+`. `[A-Za-z0-9_]+` lost 4 of 185 entries
  (181 reported) while declarations parsed 185 — reconcile the two counts and the gap is visible.
- Then intersect: headline files ∩ core-only = **0 of 180**. Report that, plus the reason for the
  specific family the user asked about (family 244's headline
  `OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice` in
  `Models/Separation.lean` sits behind `Mathlib.SetTheory.ZFC.Rank` ×2 and
  `Mathlib.SetTheory.Cardinal.Arithmetic` ×1 in a ~940-file closure).

## 6. Report it as a source-level fact

Say: *these 19 modules elaborate on toolchain X; the library does not build; no comparator ran; the
axiom reports are the kernel's statement about proof terms, not a review of the mathematics.* Name the
toolchain and the pin. Name the time (15.83 s) and the olean size (11 MB). Close with what was not
checked — the headline declarations, the 405 challenge stubs, the pinned toolchain, and whether any
elaborated theorem matches the manuscript's statement.
