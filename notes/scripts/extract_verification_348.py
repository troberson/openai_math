#!/usr/bin/env python3
"""Measure the two family-348 verification bundles; report-only, writes nothing.

Every number quoted in the "What the 348 bundle checks, and what it omits" section of
notes/verification-dirs.md comes from this report. Run it twice and diff: the output must be
identical. No verification program is executed — the bundle is read as text, per the repo rule
that nothing in preprints/ is run.

Sections:
1. Byte identity between the two bundles, file by file.
2. Manifest audit: entries, self-hash, sha256/size against disk, files on disk the manifest omits.
3. Declared dependencies vs what the extra file imports.
4. results.json summary counts, read from the shipped file.
5. verify.py structure: check functions, where all_passed is set, printed-value literals.
6. The portability suite: check count and how many are negative tests.
7. Manuscript references to the bundle.
"""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRE = ROOT / "preprints"
DIRS = {
    "positively": PRE / "Positively-curved-Einstein-four-manifolds-September-23-2026",
    "zero-plane": PRE / "Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026",
}
FAM = "348"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def files(d):
    return {p.name: p for p in (d / "verification").iterdir() if p.is_file()}


def main():
    pos, zero = DIRS["positively"], DIRS["zero-plane"]
    fp, fz = files(pos), files(zero)

    print(f"== family {FAM}: {len(fp)} files in the positively-curved dir, "
          f"{len(fz)} in the zero-plane dir")
    shared = sorted(set(fp) & set(fz))
    same = [n for n in shared if fp[n].read_bytes() == fz[n].read_bytes()]
    diff = [n for n in shared if fp[n].read_bytes() != fz[n].read_bytes()]
    print(f"   shared {len(shared)}  byte-identical {len(same)}  differing {len(diff)} {diff}")
    print(f"   only in zero-plane {sorted(set(fz) - set(fp))}  "
          f"only in positively {sorted(set(fp) - set(fz))}")
    for n in shared:
        same_n = fp[n].read_bytes() == fz[n].read_bytes()
        print(f"      {n}: {fp[n].stat().st_size} B vs {fz[n].stat().st_size} B"
              f"  {'identical' if same_n else 'DIFFERS'}")
    for n in sorted(set(fz) - set(fp)):
        print(f"      {n}: {fz[n].stat().st_size} B (zero-plane only)")

    print("== manifest audit")
    for label, d in sorted(DIRS.items()):
        v = d / "verification"
        m = json.loads((v / "manifest.json").read_text(encoding="utf-8"))
        entries = m["files"]
        on_disk = files(d)
        listed = sorted(entries)
        missing = sorted(set(on_disk) - set(listed))
        bad = [n for n in listed
               if n not in on_disk
               or sha(on_disk[n]) != entries[n]["sha256"]
               or on_disk[n].stat().st_size != entries[n]["bytes"]]
        print(f"   {label}: entries {len(listed)} (self-hash {'yes' if 'manifest.json' in entries else 'no'})"
              f"  on-disk {len(on_disk)}  hash/size mismatches {len(bad)} {bad}")
        print(f"      manifest omits: {missing}")
        print(f"      scope: {m['scope']!r}")
        print(f"      main_command: {m['main_command']!r}  network_required: {m['network_required']}"
              f"  third_party_dependencies: {m['third_party_dependencies']}")

    print("== declared dependencies vs imports")
    for label, d in sorted(DIRS.items()):
        v = d / "verification"
        deps = json.loads((v / "dependencies.json").read_text(encoding="utf-8"))
        imports = set()
        for p in v.glob("*.py"):
            for line in p.read_text(encoding="utf-8", errors="replace").split("\n"):
                m = re.match(r"^(?:import|from)\s+([A-Za-z_][\w.]*)", line)
                if m and not m.group(1).startswith(("argparse", "fractions", "functools", "hashlib",
                                                    "json", "math", "pathlib", "platform", "shutil",
                                                    "subprocess", "sys", "tempfile", "__future__",
                                                    "polynomial")):
                    imports.add(m.group(1))
        print(f"   {label}: declared third_party {deps['third_party_dependencies']}"
              f"  undeclared imports {sorted(imports)}")
        print(f"      minimum_version {deps['runtime']['minimum_version']}"
              f"  tested_version {deps['runtime']['tested_version']}"
              f"  floating_point_decisions {deps['floating_point_decisions']}"
              f"  regenerate_command {deps['regenerate_command']!r}")

    print("== results.json (shipped, byte-identical in both dirs)")
    r = json.loads((pos / "verification/results.json").read_text(encoding="utf-8"))
    s = r["summary"]
    print(f"   scope: {r['scope']!r}")
    print(f"   arithmetic: {r['arithmetic']!r}")
    print("   summary: " + "  ".join(f"{k}={v}" for k, v in sorted(s.items())))
    print(f"   reported_interval_rows {s['reported_interval_rows']} + supplementary "
          f"{s['interval_certificate_rows'] - s['reported_interval_rows']}"
          f" = {s['interval_certificate_rows']} rows")
    supp = sum(1 for c in r["interval_certificates"] if c["supplementary"])
    strict = sum(1 for c in r["interval_certificates"] if c["strict"])
    print(f"   interval records: supplementary {supp}  strict {strict}")
    recs = sum(len(c["intervals"]) for c in r["interval_certificates"])
    print(f"   interval subinterval records {recs}")
    tri = r["triangle_certificates"]
    print(f"   triangle rows {len(tri)}  with determinant_floor "
          f"{sum(1 for t in tri if t['determinant_floor'] is not None)}"
          f"  multi-entry (2x2 minor) rows {sum(1 for t in tri if t['entry_order'] != ['scalar'])}")
    passed = json.dumps(r).count('"passed": true')
    print(f"   '\"passed\": true' occurrences in results.json {passed}")

    print("== verify.py structure")
    src = (pos / "verification/verify.py").read_text(encoding="utf-8").split("\n")
    fns = [i + 1 for i, l in enumerate(src) if l.startswith("def check_")]
    print(f"   lines {len(src)}  check_* functions {len(fns)} at lines {fns}")
    ap = [i + 1 for i, l in enumerate(src) if '"all_passed"' in l]
    print(f"   all_passed appears at lines {ap}")
    for n in ap:
        print(f"      :{n}: {src[n - 1]}")
    printed = re.findall(r'scalar_claim\("([\w.]*printed[\w.]*)', "\n".join(src))
    print(f"   scalar_claim keys naming a printed value: {len(printed)}")
    req = sum(l.count("require(") for l in src)
    ident = sum(l.count("identity(") for l in src)
    print(f"   require( occurrences {req}  identity( occurrences {ident}")
    print(f"   docstring: {src[1].strip()!r}")
    for i, l in enumerate(src):
        if "not a proof assistant" in l:
            print(f"   scope line :{i + 1}: {l.strip()}")

    print("== portability suite")
    p = json.loads((pos / "verification/portability-results.json").read_text(encoding="utf-8"))
    cs = p["checks"]
    neg = [c["name"] for c in cs if "rejected" in c["name"]]
    ends = [c["name"] for c in cs if c["name"].endswith("rejected")]
    print(f"   negative tests naming a rejection {len(neg)}  of which ending 'rejected' {len(ends)}"
          f"  exceptions {[n for n in neg if n not in ends]}")
    print(f"   checks {len(cs)}  negative tests {len(neg)}"
          f"  all_passed {p['all_passed']}  python {p['python_version']}"
          f"  network_used {p['network_used']}")
    print(f"   third_party_dependencies {p['third_party_dependencies']}"
          f"  temporary_files_outside_package {p['temporary_files_outside_package']}")

    print("== manuscript references")
    for label, d in sorted(DIRS.items()):
        hits = []
        for p in sorted(d.rglob("*.tex")):
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
                if re.search(r"verify\.py|COVERAGE\.md", line):
                    hits.append(f"{p.relative_to(d)}:{i}")
        print(f"   {label}: {len(hits)} {hits}")

    print(f"\nTOTAL family {FAM}: 2 bundles, {len(shared)} shared files, "
          f"{len(same)} byte-identical, {len(diff)} differing, "
          f"{len(s)} summary keys, {len(cs)} portability checks")


main()
