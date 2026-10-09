# What the dependency record implies about automated formalization

Measured 2026-10-07 from three sources only: `notes/formalization-deps.tsv` (31 rows, 8 fields),
`lean/lakefile.lean` (335 lines), and `lean/patches/` (23 `*-lean4341.patch` files plus `README.md`).
No `lake`, `lean`, `lake exe cache get`, or comparator run, and **no build was attempted** — every pin
below is a declared pin, and every patch below is an asserted-applicable patch, not a verified one.
Quote each number with the rule that yields it.

## The record is a pinned, patched, toolchain-converged tree

| Fact | Measured | Anchor |
|---|---|---|
| `require … from git "url" @ "commit"` declarations | **30**, every one pinned to a **40-char** commit | `lean/lakefile.lean:10`–`:86` |
| Patch files | **23**, **160,187** lines, **734** `diff --git` file hunks | `lean/patches/` |
| Declared libraries with **no** patch | **7** | `notes/formalization-deps.tsv` |
| Patches that rewrite the dependency's `lean-toolchain` | **22 of 23** | `lean/patches/*.patch` |
| Distinct toolchain versions the patches migrate **from** | **8**, all migrating **to** `v4.34.1` | `lean/patches/*.patch` |
| Release toolchain | `leanprover/lean4:v4.34.1` | `lean/lean-toolchain:1` |
| Toolchain pinned by the package, not by the environment | `fixedToolchain := true` | `lean/lakefile.lean:7` |

The 23 patch filenames all end `-lean4341.patch`, and the name is built by code, not chosen by hand:

> `lean/lakefile.lean:193:  let patch := root / "patches" / s!"{label}-lean4341.patch"`

so a library's compatibility patch is keyed to the toolchain version in its filename. The 22 toolchain
hunks move 8 distinct upstream versions onto the release's own: `v4.32.0` ×13, `v4.34.0` ×3, and one
each of `v4.18.0`, `v4.21.0`, `v4.29.0`, `v4.32.2`, `v4.33.0-rc2`, `v4.34.0-rc2`. The single patch
with no toolchain hunk is `rellich-kondrachov-lean4341.patch`.

**What that implies.** A 121,734-file agent-generated Lean tree does not sit on the published
ecosystem. It sits on 30 pinned commits plus 160,187 lines of release-specific edits to 23 of them,
22 of which have had their toolchain rewritten to match. The compatibility layer is 1.3 lines of patch
per source file in the tree it supports. Upstream is consumed as a starting point, not as a dependency.

## Drift is a build error, not a silent event

`planDependencyPatch` (`lean/lakefile.lean:186`) runs six checks before it will touch a checkout, and
each failure is a hard error:

| Check | Anchor | Error text |
|---|---|---|
| The dependency is a Git dependency pinned to a commit | `:188`–`:189` | `compatibility patches require a Git dependency pinned to a commit.` |
| The revision is 40 chars of lowercase hex | `:190`–`:192` | `expected a full lowercase Git commit, got {revision}.` |
| The patch file exists | `:194`–`:195` | `Missing compatibility patch: {patch}` |
| The checkout's `HEAD` equals the pinned revision | `:201`–`:202` | `expected commit {revision}, got {head.stdout}` |
| The checkout's `origin` URL equals the declared URL | `:204`–`:205` | `expected origin {url}, got {origin.stdout}` |
| The patch applies forward **or** reverses cleanly | `:206`–`:213` | `compatibility patch conflicts with local changes.` |

The last one is the interesting pair: the reverse check runs first (`:206`), the forward check next
(`:209`) — both through the same `checkPatch` helper (`:169`–`:171`) — and a checkout that is
neither patched nor patchable is an error naming both stderr streams (`:212`–`:213`). A dependency
that has drifted — a moved HEAD, a different remote, a hand-edit in the working tree — cannot be
silently absorbed. `post_update` re-runs the same plan after resolution and fails if the patch is no
longer applied:

> `lean/lakefile.lean:291:    | _ => error s!"{label}: compatibility patch was lost during dependency resolution."`

**What that implies.** The release treats its upstream tree as a reproducible artifact, not as a cache.
For an agent-generated formalization program, the binding constraint is not only "does the proof
elaborate" but "is the ecosystem it elaborates against the same one yesterday's proof ran against",
and this lakefile makes that a checked property with named failure modes.

## The tree is materialized by the build, not fetched into a cache

When a pinned checkout is absent, `preparePatchedDependencies` builds it itself
(`lean/lakefile.lean:224`): a staging directory built from `s!".{plan.label}-bootstrap-{pid}-{stamp}"`
(`:240`),
a git clone with `--no-checkout` (`:243`–`:244`), a detached checkout at the pinned revision
(`:248`), a `rev-parse` re-verification of `HEAD` against the pin (`:251`–`:253`), the patch applied
in the staging tree (`:254`), then `IO.FS.rename` into `.lake/packages/<label>` (`:255`) with
`removeDirAll` on the staging path in a `finally` (`:257`–`:259`). The patch is applied *before* the
tree becomes the package directory, and the checkout is detached at the pinned commit rather than
tracking a branch.

Both phases are two-pass: plan everything, then change anything.

> `lean/lakefile.lean:226:  -- Check all existing checkouts before changing any of them.`
> `lean/lakefile.lean:293:  -- Preflight every dependency before changing any of them.`

**What that implies.** No partial-patch state is reachable: a dependency is patched and verified
(`applyDependencyPatch` applies, then re-checks `--reverse`: `:215`–`:221`), or the build stops. That
is the property a large unattended formalization effort needs, because the failure mode it prevents is
a half-patched library — the state in which an agent's proof stops compiling for reasons that are not
in its own source.

## Two patch phases, and why the earlier one exists

| Phase | Anchor | Libraries | Patch lines |
|---|---|---|---|
| Pre-resolution (`run_cmd`) | `lean/lakefile.lean:161`–`:164`, driven at `:271`–`:275` | **11** | **6,658** |
| `post_update` preflight | `lean/lakefile.lean:295`–`:297` | **12** | **153,529** |

The two sets are **disjoint** and their union is **exactly** the 23 patched libraries — every patch
file on disk is named by one of the two arrays, and neither array names a library without a patch.

The 11 pre-resolution libraries are **exactly** the 11 declared libraries whose URL is under
`github.com/lana-agents/`. The reason that phase exists is the comment above the `run_cmd`:

> `lean/lakefile.lean:262:-- Configuration elaboration precedes dependency resolution, unlike `post_update`.`

A dependency's own configuration is elaborated as part of resolution, so a library whose manifest
picks a different mathlib has already voted before `post_update` runs. Patching before resolution is
how the release overrules that vote for the 11 libraries it controls the source of. The same
mechanism, applied by hand to a third-party library, is visible in the AINTLIB patch:

> `lean/patches/AINTLIB-lean4341.patch:9: -rev = "e4b72ca0d01c"     # daily steady-state bump 2026-08-25, toolchain v4.34.0-rc2`
> `lean/patches/AINTLIB-lean4341.patch:10: +rev = "d13f23b723b8a846827a245b89c10fc7d3f11612"     # Zauner compatibility: Lean/Mathlib v4.34.1`

The added revision is the mathlib pin OAI declares at `lean/lakefile.lean:85` and the manifest
resolves. The removed line carries upstream's own provenance — a dated "steady-state bump" onto
`v4.34.0-rc2` — so the patch is not fixing a broken pin; it is overwriting a current one.

## Ordering is used as a pin mechanism

> `lean/lakefile.lean:71:-- Declare shared dependencies last: Lake resolves later requirements first.`
> `lean/lakefile.lean:72:-- These pins override the older versions in the upstream packages' manifests.`

The block those comments introduce is **7** requires (`lean/lakefile.lean:73`–`:86`):
PrimeNumberTheoremAnd, leancert, LeanArchitect, PrimeCert, `«doc-gen4»`, checkdecls, mathlib. **6 of
those 7 ship no patch** — all except PrimeNumberTheoremAnd. The shared layer is pinned clean; the
mathematics layer is pinned *and* patched.

**What that implies.** One mathlib across 30 pinned third-party trees is not achieved by asking
upstream to agree. It is achieved by last-wins ordering plus 22 patches that rewrite each
dependency's own toolchain, plus patches that rewrite a dependency's own mathlib revision. The
release's mathlib version is imposed on the ecosystem, 22 times.

## Patch size tracks upstream surgery, not use

Direct imports come from `notes/formalization-deps.tsv` (`direct_imports`, measured over
`lean/OAI/**/*.lean`); patch lines are the file's line count. The table is all **23** declared
libraries with a patch, ordered by patch lines.

| Library | Direct imports | Patch lines |
|---|---|---|
| PrimeNumberTheoremAnd | 244 | 39,904 |
| ClassFieldTheory | 4 | 31,757 |
| StrongPNT | 12 | 26,284 |
| AINTLIB | **0** | 23,288 |
| gromov | 2 | 18,638 |
| carleson | **0** | 4,374 |
| Zeta3Irrational | **0** | 3,240 |
| rellich-kondrachov | 9 | 2,697 |
| schoenflies-lean | 2 | 2,575 |
| oka | **0** | 2,014 |
| iut | **0** | 1,164 |
| orbicurve-cores | **0** | 695 |
| elliptic-curves | **0** | 668 |
| fixed-point-theorems | 4 | 640 |
| heights | **0** | 494 |
| pi1 | **0** | 418 |
| belyi | **0** | 408 |
| tempered-fundamental-groups | **0** | 272 |
| formal-schemes | **0** | 193 |
| genl | **0** | 189 |
| tate-curves-theta | **0** | 143 |
| AbsorptionCutoff | 1 | 111 |
| SphereEversion | 2 | 21 |

Median patch lines: **2,575** for declared libraries with any direct import, **408** for declared
libraries with none. The largest patch in the release, PrimeNumberTheoremAnd at 39,904 lines, sits
beside the largest import count, mathlib at 56,196 — and mathlib itself ships **no** patch. The
largest patch on a library OAI never imports directly is AINTLIB at 23,288 lines.

**What that implies.** Patch volume is a measure of how far a library has drifted from the release's
toolchain, not of how much mathematics the release takes from it. A library can be load-bearing and
untouched (mathlib, TauCeti at 5 imports) or unused and heavily rewritten (AINTLIB, carleson).

## The pin list is a resolution list, not a usage list

**19 of the 30** declared libraries have `direct_imports = 0`: `AINTLIB`, `LeanArchitect`,
`PrimeCert`, `Zeta3Irrational`, `belyi`, `carleson`, `checkdecls`, `doc-gen4`, `elliptic-curves`,
`formal-schemes`, `genl`, `heights`, `iut`, `leancert`, `oka`, `orbicurve-cores`, `pi1`,
`tate-curves-theta`, `tempered-fundamental-groups`. **14 of those 19 ship a patch**; the 5 that do not
are `LeanArchitect`, `PrimeCert`, `checkdecls`, `doc-gen4`, `leancert`. All 11 pre-resolution
libraries are in the zero-import set, and 3 of the 12 `post_update` libraries are
(`AINTLIB`, `Zeta3Irrational`, `carleson`).

`lean/formalization.yaml` claims the list is ordered by use — the comment above
`related_formalizations:` reads, verbatim:

> `lean/formalization.yaml:878:  # Imported libraries, ordered by direct import count in project Lean sources.`

**That claim is recorded, not asserted true, and 5 entries violate it** (measured in
`notes/formalization-deps.md`: strongpnt 12 above AINTLIB 0; TauCeti 5 above fixed-point-theorems 4;
gromov 2 above heights 0; schoenflies-lean 2 above iut 0; AbsorptionCutoff 1 above
zeta_3_irrational 0). The 19 zero-import libraries sit beside that claim: an ordering-by-import
comment over a list in which 19 of 30 entries import nothing directly is a claim about a list that is
mostly not a usage list.

**Transitive imports are not measured and are not guessed here.** Counting them needs `lake` — the
resolved graph lives in the dependency graph Lake builds, and this repo ships `lean/lake-manifest.json`
(42 resolved packages) without `.lake/packages`, so no upstream source is present to walk. The
manifest's 12 transitive-only packages (`Qq`, `aesop`, `batteries`, …) are none of the 19 zero-import
libraries, so the obvious rescue — "they import nothing directly because they arrive transitively" —
is not supported by the manifest, and the direct-import counts are the floor they are: **no direct
import**, not non-use.

**What that implies.** 30 declarations, 11 with direct imports, 19 with none, 23 patched. The declared
set is what the build must *resolve*, which is a larger set than what the proofs *use*. For an
agent-generated formalization, declaring a dependency is cheap and pinning it is cheap; the cost lands
in the compatibility layer, and it lands on libraries the proofs never import.

## Not checked

- **No build was run.** No pin is verified as buildable; no patch is verified as applicable. Patch
  applicability is asserted by the release's own checks (`lean/lakefile.lean:206`–`:213`), not by this record.
- Patch hunks were counted, not classified. The 734 `diff --git` hunks are counted by filename
  suffix for `lean-toolchain` and `lakefile.*` only; the remaining hunks were not read, so nothing
  here says how much of the 160,187 lines is toolchain-compat renaming and how much is mathematics.
- Upstream repos were not fetched: no pinned commit was checked to exist, no URL was checked to resolve.
- Import counts are **direct statements only** over `lean/OAI/**/*.lean`. Transitive use is
  unmeasurable without `lake` and is not estimated here.
- The 11/12 phase split is read from two hard-coded arrays (`lean/lakefile.lean:161`–`:164`,
  `:295`–`:297`). Why a given library sits in one array and not the other is inferred from the
  `:262` comment and the AINTLIB `lakefile.toml` hunk; the release states no per-library reason.
- `lean/lake-manifest.json` was read for package/rev reconciliation only (in
  `notes/formalization-deps.md`); it carries no dependency edges, so which declared library pulls in
  each transitive-only package is not recorded.
- Whether each declared library is *needed* is not measured, and whether each patch is *needed* is
  not measured — 30 declarations, 23 patches, no build to say which are load-bearing.
