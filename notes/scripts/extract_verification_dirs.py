#!/usr/bin/env python3
"""Measure the 30 verification bundles and the README sections that name them; report-only.

Every count in the "Every bundle and its own entry point" section of notes/reports/verification-dirs.md
comes from this report, and every quoted line below is printed with its file and line number so the
page can cite it. Run it twice and diff: the output must be identical. It writes nothing and runs
nothing — bundles are read as text, per the repo rule that nothing in preprints/ is executed.

Entry-point rule, applied in order per bundle (the first that fires is the entry point):
  1  verification/README.md
  2  verification/<sub>/README.md   (alphabetically first; the count of such files is printed)
  3  verification/<sub>/README.txt
  4  a main_command declared in a JSON manifest under verification/
  5  a top-level verification/ script whose name starts verify|reproduce|run|check
  6  none
The rule, its `MANIFESTS` / `SCRIPT_PREFIX` vocabulary, and the bundle walk itself live in
`catlib/preprints.py`, shared with `extract_verification_348.py`; what stays here is the report
shape — the README-section reconciliation, the numbered heading/command/scope lines, and the
ledger reconciliation.
Sections:
1. Population and the README-section reconciliation.
2. Per-bundle entry point, with the entry point's heading, command, and scope lines numbered.
3. Entry-point class counts and the ledger reconciliation.
"""
import re

from catlib.ledger import read_ledger
from catlib.overview import parse_overview
from catlib.paths import PREPRINTS, owner
from catlib.preprints import bundle_of, entry_point


def families_by_slug():
    order, fams = parse_overview()
    out: dict[str, str] = {}
    for fam in order:
        for p in fams[fam]["tex_paps"]:
            out.setdefault(owner(p), fam)
    return out, order, fams


def headings(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    return text, [(i + 1, h.group(1).strip())
                  for i, ln in enumerate(lines) if (h := re.match(r"^##\s+(.*)$", ln))]


def interesting(path):
    """Heading lines, command lines, and scope sentences, each with its line number."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out = []
    for i, ln in enumerate(lines, start=1):
        s = ln.strip()
        if not s:
            continue
        if re.match(r"^#{1,3}\s", s):
            out.append((i, "heading", s))
        elif s.startswith(("$", "g++", "make")) or "python3 " in s:
            out.append((i, "command", s))
        elif re.search(r"\bnot\b|\bdoes not\b|\bno theorem\b", s) and len(s) > 40:
            out.append((i, "scope", s))
    return lines, out


def main():
    fam_by_slug, _order, _fams = families_by_slug()
    dirs = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
    bundles = [p for p in dirs if bundle_of(p).is_dir()]
    readmes = [p for p in dirs if (p / "README.md").is_file()]

    print("== population")
    print(f"preprint dirs {len(dirs)}  with verification/ {len(bundles)}  README.md {len(readmes)}")

    named, runsec, unnamed = [], [], []
    for p in bundles:
        _, heads = headings(p / "README.md")
        ver = [ln for ln, h in heads if "Verification" in h]
        run = [ln for ln, h in heads if "Run the verification code" in h]
        if ver:
            named.append((p.name, "## Verification", ver[0]))
        elif run:
            runsec.append((p.name, "## Run the verification code", run[0]))
        else:
            unnamed.append(p.name)
    print(f"named by a README section {len(named) + len(runsec)}  "
          f"## Verification {len(named)}  ## Run the verification code {len(runsec)}  "
          f"unnamed {len(unnamed)}")
    for n in unnamed:
        print(f"   UNNAMED {n}  fam {fam_by_slug.get(n, '?')}")
    for n, _h, ln in runsec:
        print(f"   run-section bundle {n}  fam {fam_by_slug.get(n, '?')}  heading at "
              f"preprints/{n}/README.md:{ln}")

    fams_with_bundle = sorted({fam_by_slug.get(p.name) for p in bundles})
    print(f"families carrying a bundle {len(fams_with_bundle)}")

    print("== per-bundle entry point")
    classes: dict[str, int] = {}
    no_entry = []
    named_by_slug = {n: (h, ln) for n, h, ln in named}
    run_by_slug = {n: (h, ln) for n, h, ln in runsec}
    for p in bundles:
        bundle = bundle_of(p)
        ep, rule, extra = entry_point(bundle)
        classes[rule] = classes.get(rule, 0) + 1
        fam = fam_by_slug.get(p.name, "?")
        nfiles = len([x for x in bundle.rglob("*") if x.is_file()])
        sec = named_by_slug.get(p.name) or run_by_slug.get(p.name)
        sectxt = f"preprints/{p.name}/README.md:{sec[1]} {sec[0]}" if sec else "none"
        if ep is None:
            no_entry.append(p.name)
            print(f"\nfam {fam}  {p.name}\n   entry point NONE  rule {rule}  files {nfiles}")
            print(f"   manuscript section {sectxt}")
            for q in sorted(x.relative_to(bundle) for x in bundle.rglob("*") if x.is_file()):
                print(f"      {q}")
            continue
        rel = ep.relative_to(bundle)
        lines, hits = interesting(ep)
        print(f"\nfam {fam}  {p.name}")
        print(f"   entry point verification/{rel}  rule {rule}  extra {extra}  "
              f"lines {len(lines)}  bundle files {nfiles}")
        print(f"   manuscript section {sectxt}")
        for i, kind, s in hits[:14]:
            print(f"      {i} {kind} {s}")

    print("\n== entry-point classes")
    for rule, cnt in sorted(classes.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"   {cnt:3d}  {rule}")
    print(f"   bundles with no entry point {len(no_entry)} {no_entry}")

    rows = read_ledger()
    led = sum(int(r["verification"]) for r in rows)
    led_fams = sorted(r["fam"] for r in rows if int(r["verification"]) > 0)
    print("== ledger")
    print(f"ledger verification sum {led}  families with verification>0 {len(led_fams)}  "
          f"set equal to bundle families {led_fams == fams_with_bundle}")
    print(f"ledger inputs sum {sum(int(r['inputs']) for r in rows)}  "
          f"ledger covmd sum {sum(int(r['covmd']) for r in rows)}")


if __name__ == "__main__":
    main()
