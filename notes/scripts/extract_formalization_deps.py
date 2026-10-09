#!/usr/bin/env python3
"""Extract notes/formalization-deps.tsv: one row per upstream library.

Pure extraction over four layers that ship in the repo, stdlib only, deterministic:

  lean/lakefile.lean            require declarations, each pinned to a commit
  lean/formalization.yaml       related_formalizations, id + relationship
  lean/OAI/**/*.lean            import statements, counted by import root
  lean/patches/*.patch          compatibility patches, with line counts

The row set is the union of the declared libraries and the import roots that are
imported but not declared, so an undeclared dependency is a row, not a dropped
count. Writes the TSV and prints the reconciliation report; the report is the test.

lean/lake-manifest.json is read for the report only, never for a column: it is a
generated artifact, so its resolved revs are reconciled against the declared pins
and reported, not written into the table.
"""
import json
import re
import sys
import collections
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from catlib import yaml as Y
from catlib.paths import LAKEFILE, LAKE_MANIFEST as MANIFEST, OAI_DIR as SOURCE

REPO = Path(__file__).resolve().parents[2]
PATCHES = REPO / "lean" / "patches"
OUT = REPO / "notes" / "formalization-deps.tsv"

FIELDS = [
    "library",
    "repo_url",
    "pinned_commit",
    "lakefile_declared",
    "yaml_relationship",
    "direct_imports",
    "patch_file",
    "patch_lines",
]

# Import roots that are not core Lean and not the project's own namespace.
CORE_ROOTS = {"OAI", "Lean", "Std", "Init", "Lake", "all"}

# Import root -> repo URL. Written by hand because the three layers name the same
# library three ways (lakefile «fixed-point-theorems», yaml
# harfe/fixed-point-theorems-lean4, source `import FixedPointTheorems...`). Every
# alias is asserted below to resolve to a declared URL, so a stale alias fails loudly.
ALIAS = {
    "Mathlib": "https://github.com/leanprover-community/mathlib4",
    "PrimeNumberTheoremAnd": "https://github.com/AlexKontorovich/PrimeNumberTheoremAnd",
    "ClassFieldTheory": "https://github.com/n-yamaguchi-0729/ClassFieldTheory",
    "StrongPNT": "https://github.com/math-inc/strongpnt",
    "RellichKondrachov": "https://github.com/abenenson/rellich-kondrachov",
    "FixedPointTheorems": "https://github.com/harfe/fixed-point-theorems-lean4",
    "TauCeti": "https://github.com/TauCetiProject/TauCeti",
    "Schoenflies": "https://github.com/alonamaloh/schoenflies-lean",
    "SphereEversion": "https://github.com/leanprover-community/sphere-eversion",
    "Gromov": "https://github.com/Aaron1011/gromov",
    "AbsorptionCutoff": "https://github.com/BennyAvelin/AbsorptionCutoff",
}


def norm(name):
    """Canonical join key: lowercase alphanumerics, then drop the trailing
    'lean4' / 'lean' / digit suffixes the three layers add and drop unevenly."""
    s = re.sub(r"[^a-z0-9]", "", name.lower())
    for suffix in ("lean4", "lean"):
        if s.endswith(suffix) and len(s) > len(suffix):
            s = s[: -len(suffix)]
            break
    return re.sub(r"[0-9]+$", "", s)


def url_key(url):
    """Join key for a repo URL. The lakefile writes '.git' and formalization.yaml
    does not, so the suffix is stripped before normalizing."""
    last = url.rstrip("/").split("/")[-1]
    if last.endswith(".git"):
        last = last[: -len(".git")]
    return norm(last)


def lakefile_rows():
    """label, url, commit for every `require ... from git "url" @ "commit"`."""
    text = LAKEFILE.read_text(encoding="utf-8")
    pat = re.compile(
        r'^require\s+(?:«(?P<l1>[^»]+)»|(?P<l2>[A-Za-z0-9_.\-]+))\s+from\s+git\s*\n'
        r'\s*"(?P<url>[^"]+)"\s*@\s*"(?P<commit>[0-9a-f]+)"',
        re.M,
    )
    rows = []
    for m in pat.finditer(text):
        label = m.group("l1") or m.group("l2")
        rows.append({"label": label, "url": m.group("url"), "commit": m.group("commit")})
    return rows


def yaml_rows():
    lines = Y.yaml_lines()
    start = lines.index("related_formalizations:")
    rows, cur = [], None
    for ln in lines[start + 1 :]:
        if ln and not ln.startswith(" "):
            break
        m = re.match(r"\s+-\s+id:\s*(\S+)", ln)
        if m:
            cur = {"url": m.group(1), "relationship": None}
            rows.append(cur)
            continue
        m = re.match(r"\s+relationship:\s*(\S+)", ln)
        if m and cur is not None:
            cur["relationship"] = m.group(1)
    return rows


def import_counts():
    """Import statements in lean/OAI/**/*.lean, keyed by import root.

    The root is the first token after `import`, so `import all Mathlib` is rooted
    at `all` and is not counted as a Mathlib import.
    """
    pat = re.compile(r"^\s*import\s+([A-Za-z_][A-Za-z0-9_.]*)", re.M)
    counts = collections.Counter()
    files = 0
    for p in sorted(SOURCE.glob("**/*.lean")):
        files += 1
        for root in pat.findall(p.read_text(encoding="utf-8", errors="replace")):
            counts[root.split(".")[0]] += 1
    return counts, files


def patch_rows():
    out = {}
    for p in sorted(PATCHES.glob("*.patch")):
        out[p.name] = len(p.read_text(encoding="utf-8", errors="replace").splitlines())
    return out


def manifest_revs():
    """Resolved revs from lake-manifest.json, keyed by package name.

    Report-only: the manifest lists packages, not the lean_libs inside them, so it
    reconciles the declared pins and cannot say whether a subproject import resolves.
    """
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {p["name"].strip("«»"): p["rev"] for p in data["packages"]}, data["version"]


def yaml_order_violations(yaml, imports_by_key):
    """Positions where formalization.yaml's stated ordering fails.

    The comment above related_formalizations: claims the list is ordered by direct
    import count; a violation is an entry whose measured count exceeds the entry
    directly above it.
    """
    out, prev = [], None
    for i, y in enumerate(yaml, start=1):
        n = imports_by_key.get(url_key(y["url"]), 0)
        if prev is not None and n > prev[1]:
            out.append((i, y["url"].rsplit("/", 1)[-1], n, prev[2].rsplit("/", 1)[-1], prev[1]))
        prev = (i, n, y["url"])
    return out


def main():
    lake = lakefile_rows()
    yaml = yaml_rows()
    imports, nfiles = import_counts()
    patches = patch_rows()
    manifest, manifest_version = manifest_revs()

    problems = []

    by_norm_url = {}
    for r in lake:
        key = url_key(r["url"])
        if key in by_norm_url:
            problems.append(f"lakefile: duplicate normalized url key {key}")
        by_norm_url[key] = r
    yaml_by_norm_url = {}
    for r in yaml:
        key = url_key(r["url"])
        if key in yaml_by_norm_url:
            problems.append(f"yaml: duplicate normalized url key {key}")
        yaml_by_norm_url[key] = r

    # Every lakefile label must reach its yaml entry through the normalized URL.
    for r in lake:
        key = url_key(r["url"])
        if key not in yaml_by_norm_url:
            problems.append(f"lakefile {r['label']}: no yaml entry for {r['url']}")
    for r in yaml:
        key = url_key(r["url"])
        if key not in by_norm_url:
            problems.append(f"yaml {r['url']}: no lakefile require")

    # Every alias must resolve to a declared library.
    for root, url in ALIAS.items():
        key = url_key(url)
        if key not in by_norm_url:
            problems.append(f"alias {root}: {url} is not declared in the lakefile")

    # Every imported external root must be aliased, or recorded as undeclared.
    external = {r: c for r, c in imports.items() if r not in CORE_ROOTS}
    undeclared_roots = sorted(r for r in external if r not in ALIAS)

    rows = []
    for key, r in sorted(by_norm_url.items()):
        y = yaml_by_norm_url.get(key, {})
        root = next((k for k, v in ALIAS.items() if url_key(v) == key), None)
        patch_name, patch_lines = "none", 0
        for name, lines in patches.items():
            if norm(name[: -len("-lean4341.patch")]) == key:
                patch_name, patch_lines = name, lines
                break
        rows.append(
            {
                "library": r["label"],
                "repo_url": r["url"],
                "pinned_commit": r["commit"],
                "lakefile_declared": "y",
                "yaml_relationship": y.get("relationship") or "none",
                "direct_imports": imports.get(root, 0) if root else 0,
                "patch_file": patch_name,
                "patch_lines": patch_lines,
            }
        )
    for root in undeclared_roots:
        rows.append(
            {
                "library": root,
                "repo_url": "none",
                "pinned_commit": "none",
                "lakefile_declared": "n",
                "yaml_relationship": "none",
                "direct_imports": imports[root],
                "patch_file": "none",
                "patch_lines": 0,
            }
        )
    rows.sort(key=lambda r: (-r["direct_imports"], r["library"]))

    # yaml entries are keyed by repo URL, so import counts reach them via the alias map.
    imports_by_key = {}
    for key in by_norm_url:
        root = next((k for k, v in ALIAS.items() if url_key(v) == key), None)
        imports_by_key[key] = imports.get(root, 0) if root else 0

    # Patches must be attached to a declared library, never orphaned.
    attached = {r["patch_file"] for r in rows if r["patch_file"] != "none"}
    for name in patches:
        if name not in attached:
            problems.append(f"patch {name} is attached to no library row")

    # The manifest must resolve every declared pin to exactly the declared commit.
    for r in rows:
        if r["lakefile_declared"] != "y":
            continue
        rev = manifest.get(r["library"])
        if rev is None:
            problems.append(f"manifest: declared library {r['library']} has no package entry")
        elif rev != r["pinned_commit"]:
            problems.append(
                f"manifest: {r['library']} resolves to {rev[:12]}, declared {r['pinned_commit'][:12]}"
            )

    if problems:
        for p in problems:
            print(f"PROBLEM {p}")
        print(f"problems: {len(problems)} — TSV not written")
        return 1

    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(FIELDS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[f]) for f in FIELDS) + "\n")

    print(f"rows: {len(rows)}  fields: {len(FIELDS)}")
    print(f"lakefile require declarations: {len(lake)}")
    print(f"yaml related_formalizations: {len(yaml)}")
    print(f"source files scanned (lean/OAI): {nfiles}")
    print(f"patch files: {len(patches)}  patch lines: {sum(patches.values())}")
    commits = {len(r["commit"]) for r in lake}
    print(f"pinned commit lengths: {sorted(commits)}")
    print(f"declared in both layers: {sum(1 for r in rows if r['lakefile_declared'] == 'y' and r['yaml_relationship'] != 'none')}")
    print(f"declared in lakefile only: {sum(1 for r in rows if r['lakefile_declared'] == 'y' and r['yaml_relationship'] == 'none')}")
    print(f"undeclared rows: {[r['library'] for r in rows if r['lakefile_declared'] == 'n']}")
    print(f"external import roots: {len(external)}  external import statements: {sum(external.values())}")
    print(f"OAI import statements: {imports['OAI']}  Mathlib: {imports['Mathlib']}  'all'-prefixed: {imports['all']}")
    zero = [r["library"] for r in rows if r["lakefile_declared"] == "y" and r["direct_imports"] == 0]
    print(f"declared with zero direct imports: {len(zero)}")
    print(f"patches attached: {len(attached)}  declared with no patch: {len(lake) - len(attached)}")
    declared_names = {r["library"] for r in rows if r["lakefile_declared"] == "y"}
    transitive = sorted(set(manifest) - declared_names)
    print(f"manifest v{manifest_version} packages: {len(manifest)}  declared: {len(declared_names)}  transitive-only: {len(transitive)}")
    print(f"manifest rev lengths: {sorted({len(v) for v in manifest.values()})}")
    print(f"transitive-only packages: {transitive}")
    print(f"undeclared roots in manifest: {[r['library'] for r in rows if r['lakefile_declared'] == 'n' and r['library'] in manifest]}")
    viol = yaml_order_violations(yaml, imports_by_key)
    print(f"yaml ordering violations: {len(viol)}")
    for i, name, n, above, above_n in viol:
        print(f"  pos {i} {name} {n} > above {above} {above_n}")
    print(f"written: {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
