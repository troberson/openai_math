#!/usr/bin/env python3
"""Verify the family-348 section of notes/verification-dirs.md against the shipped files.

Report-only; writes nothing. Three passes over the section headed
"## What the 348 bundle checks, and what it omits":

1. Ledger claims. The section's counts of verification dirs, `covmd`, and `inputs` are
   recomputed from notes/catalog.tsv, and family 348's `verification` value is read from the ledger.
2. Citations. Every `path:line` anchor must resolve. A fenced block is attributed to the nearest
   preceding anchor and every block line must match that file at consecutive line numbers. A prose
   quotation in *"..."* form is attributed to the nearest anchor that follows it (within 4 lines) and
   must occur near the anchored line. Whitespace runs are collapsed on both sides: line-wrapping in
   the page is markup, not part of the quote. A plain `"..."` quote introduced by "`FILE` says" is
   checked against that file.
3. Counts. Each bold count in the section is compared with an independent recomputation from the
   bundle on disk, by matching the exact phrase the page must contain.

Line counts follow len(text.split("\n")), the same rule the extract_verification_348.py report uses,
so the page and that report agree.

--mutant runs the built-in mutations and fails if any goes uncaught.
"""
import csv
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "verification-dirs.md"
LEDGER = ROOT / "notes" / "catalog.tsv"
POS = ROOT / "preprints/Positively-curved-Einstein-four-manifolds-September-23-2026"
ZERO = ROOT / "preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026"
VPOS, VZERO = POS / "verification", ZERO / "verification"
SECTION = "## What the 348 bundle checks, and what it omits"

ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json)):(\d+)`")
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
SAYS = re.compile(r"`([A-Za-z0-9_.-]+\.(?:md|json|py|tex))`\s+\w+\s*(?:the\s+)?[\w, ]*?\"([^\"]{12,})\"")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def section_text(text):
    start = text.index(SECTION)
    nxt = text.find("\n## ", start + len(SECTION))
    return text[start:nxt if nxt != -1 else len(text)], start


def ledger_rows():
    with LEDGER.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def measure():
    """Independent recomputation of every count the section asserts."""
    fp = {p.name: p for p in VPOS.iterdir() if p.is_file()}
    fz = {p.name: p for p in VZERO.iterdir() if p.is_file()}
    shared = sorted(set(fp) & set(fz))
    same = [n for n in shared if fp[n].read_bytes() == fz[n].read_bytes()]
    m = json.loads((VZERO / "manifest.json").read_text(encoding="utf-8"))
    entries = m["files"]
    bad = [n for n in sorted(entries)
           if n not in fz
           or sha(fz[n]) != entries[n]["sha256"]
           or fz[n].stat().st_size != entries[n]["bytes"]]
    r = json.loads((VPOS / "results.json").read_text(encoding="utf-8"))
    s = r["summary"]
    src = (VPOS / "verify.py").read_text(encoding="utf-8").split("\n")
    port = json.loads((VPOS / "portability-results.json").read_text(encoding="utf-8"))
    cs = port["checks"]
    cov = (VPOS / "COVERAGE.md").read_text(encoding="utf-8")
    # COVERAGE.md names artifacts both as code spans (`verify.py`) and as markdown links ([README.md](...)).
    named = re.findall(r"`([\w.]+\.(?:py|json|md))`", cov) + \
        re.findall(r"\[([\w.]+\.(?:py|json|md))\]\(", cov)
    seen: set = set()
    named = [n for n in named if n not in seen and not seen.add(n)]
    present = [n for n in named if (VPOS / n).exists() and (VZERO / n).exists()]
    return {
        "cov_named": len(named),
        "cov_present": len(present),
        "shared": len(shared),
        "identical": len(same),
        "differ": len(shared) - len(same),
        "entries": len(entries),
        "mismatches": len(bad),
        "identities": s["identities"],
        "interval_rows": s["interval_certificate_rows"],
        "reported": s["reported_interval_rows"],
        "supplementary": s["interval_certificate_rows"] - s["reported_interval_rows"],
        "triangle_rows": len(r["triangle_certificates"]),
        "det_floor": sum(1 for t in r["triangle_certificates"]
                         if t["determinant_floor"] is not None),
        "exact": s["exact_value_assertions"],
        "subintervals": sum(len(c["intervals"]) for c in r["interval_certificates"]),
        "lines": len(src),
        "checkfns": len([l for l in src if l.startswith("def check_")]),
        "fnlines": [i + 1 for i, l in enumerate(src) if l.startswith("def check_")],
        "printed_keys": len(re.findall(r'scalar_claim\("([\w.]*printed[\w.]*)', "\n".join(src))),
        "require": sum(l.count("require(") for l in src),
        "passed": json.dumps(r).count('"passed": true'),
        "checks": len(cs),
        "negative": len([c for c in cs if "rejected" in c["name"]]),
        "ends_rejected": len([c for c in cs if c["name"].endswith("rejected")]),
    }


def count_phrases(v):
    """Exact phrases the page must contain for the measured counts to be honest."""
    return [
        (f"Of the {v['shared']} files they share, **{v['identical']} are byte-identical**",
         "shared/identical file counts"),
        (f"and **{v['differ']} differ**", "differing file count"),
        (f"**{v['identities']}** identities", "identities count"),
        (f"**{v['interval_rows']}** interval certificate rows (**{v['reported']}** reported + "
         f"**{v['supplementary']}** supplementary)", "interval row counts"),
        (f"**{v['triangle_rows']}** triangle certificate rows (**{v['det_floor']}** carrying a "
         "determinant floor)", "triangle row counts"),
        (f"**{v['exact']}** exact-value assertions", "exact-value count"),
        (f"over **{v['subintervals']}** subinterval records", "subinterval record count"),
        (f"`verify.py` is {v['lines']} lines with {v['checkfns']} `check_*` functions "
         f"(at lines {', '.join(str(n) for n in v['fnlines'])})", "verify.py structure counts"),
        (f"**{v['printed_keys']}** `scalar_claim` keys name a printed value", "printed-key count"),
        (f"through `require` ({v['require']} occurrences)", "require occurrence count"),
        (f"**{v['passed']}** such occurrences in `results.json`", "passed-record count"),
        (f"list {v['entries']} files", "manifest entry count"),
        (f"({v['mismatches']} mismatches)", "manifest hash mismatch count"),
        (f"ships **{v['checks']}** checks, **{v['negative']}** of them negative",
         "portability check counts"),
        (f"tests naming a rejection: **{v['ends_rejected']}** whose names end in `rejected`",
         "negative-test name counts"),
        (f"`COVERAGE.md` points at `results.json`, `verify.py`, `polynomial.py`, and `README.md`; "
         f"all {WORDS[v['cov_present']]} are present in both directories",
         "coverage-file artifact presence"),
    ]


WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}


def ledger_claims(rows):
    ver = [r for r in rows if int(r["verification"]) > 0]
    dirs = sum(int(r["verification"]) for r in rows)
    cov = [r["fam"] for r in rows if int(r["covmd"]) > 0]
    covn = sum(int(r["covmd"]) for r in rows)
    inp = sorted(r["fam"] for r in rows if int(r["inputs"]) > 0)
    inp_n = sum(int(r["inputs"]) for r in rows)
    f348 = next(r for r in rows if r["fam"] == "348")
    return {
        "dirs": dirs,
        "fams": len(ver),
        "fam_list": ", ".join(sorted(r["fam"] for r in ver)),
        "covn": covn,
        "cov_fams": sorted(set(cov)),
        "inp_n": inp_n,
        "inp_list": ", ".join(inp),
        "v348": int(f348["verification"]),
    }


def ledger_phrases(v):
    return [
        (f"**{v['dirs']} dirs over\n{v['fams']} families**", "verification dir/family totals"),
        (f"({v['fam_list']})", "verification family list"),
        (f"`covmd` counts {v['covn']} `verification/COVERAGE.md`, both in family "
         f"{v['cov_fams'][0]}", "covmd claim"),
        (f"`inputs` counts {v['inp_n']} `INPUTS.md` ({v['inp_list']})", "inputs claim"),
        (f"the ledger's `verification` value of {v['v348']} for family 348",
         "family 348 verification value"),
    ]


def check(text, full_page):
    problems = []
    body, offset = section_text(text)
    lines = body.split("\n")
    n_anchor = n_block_lines = n_prose = n_says = 0

    for m in ANCHOR.finditer(body):
        rel, at = m.group(1), int(m.group(2))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist")
            continue
        src = f.read_text(encoding="utf-8", errors="replace").split("\n")
        n_anchor += 1
        if not 1 <= at <= len(src):
            problems.append(f"anchor {rel}:{at} is outside the file ({len(src)} lines)")

    # fenced blocks -> nearest preceding anchor
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            j = i + 1
            blk = []
            while j < len(lines) and not lines[j].lstrip().startswith("```"):
                ln = lines[j]
                blk.append(ln[len(indent):] if ln.startswith(indent) and ln.strip() else ln)
                j += 1
            anchor = None
            for k in range(i - 1, max(i - 9, -1), -1):
                found = ANCHOR.findall(lines[k])
                if found:
                    anchor = (found[-1][0], int(found[-1][1]))
                    break
            if anchor is None:
                problems.append(f"section line {i + 1}: fenced block has no preceding file:line anchor")
            elif not (ROOT / anchor[0]).exists():
                problems.append(f"section line {i + 1}: anchor file {anchor[0]} does not exist")
            else:
                rel, at = anchor
                src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                for n, want in enumerate(blk):
                    got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
                    n_block_lines += 1
                    if got != want:
                        problems.append(
                            f"section line {i + 2}: block line {n} != {rel}:{at + n}\n"
                            f"    want {want!r}\n    got  {got!r}")
            i = j + 1
        else:
            i += 1

    # prose quotes -> nearest anchor that follows within 4 lines
    for m in QUOTE.finditer(body):
        quote = norm(m.group(1))
        upto = body[: m.start()].split("\n")
        after = body[m.end():].split("\n")[:4]
        anchor = None
        for k, ln in enumerate(after):
            found = ANCHOR.findall(ln)
            if found:
                anchor = (found[0][0], int(found[0][1]))
                break
        if anchor is None:
            problems.append(f"prose quote has no anchor within 4 lines after it: {quote[:60]!r}")
            continue
        rel, at = anchor
        if not (ROOT / rel).exists():
            problems.append(f"prose anchor file {rel} does not exist")
            continue
        src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        n_prose += 1
        hits = [k + 1 for k, ln in enumerate(src) if quote in norm(ln)]
        if not hits:
            # multi-line quote: join consecutive lines
            joined = norm("\n".join(src))
            hits = [k + 1 for k in range(len(src) - 1)
                    if quote in norm(src[k] + " " + src[k + 1])]
        if not hits:
            problems.append(f"prose quote not found in {rel}: {quote[:60]!r}")
        elif not any(abs(h - at) <= 4 for h in hits):
            problems.append(f"prose quote anchored at {rel}:{at} occurs only at lines {hits}")
        del upto

    for m in SAYS.finditer(body):
        rel, quote = m.group(1), norm(m.group(2))
        cands = [VPOS / rel, VZERO / rel]
        f = next((c for c in cands if c.exists()), None)
        if f is None:
            problems.append(f"`{rel} says` anchor file does not exist")
            continue
        n_says += 1
        if quote not in norm(f.read_text(encoding="utf-8", errors="replace")):
            problems.append(f"quoted text not found in {rel}: {quote[:60]!r}")

    # Phrase matching collapses whitespace: line-wrapping in the page is markup.
    flat = norm(full_page)

    v = measure()
    for phrase, label in count_phrases(v):
        if norm(phrase) not in flat:
            problems.append(f"count mismatch ({label}): page does not contain {phrase!r}")

    lv = ledger_claims(ledger_rows())
    for phrase, label in ledger_phrases(lv):
        if norm(phrase) not in flat:
            problems.append(f"ledger claim mismatch ({label}): page does not contain {phrase!r}")

    counts = (n_anchor, n_block_lines, n_prose, n_says,
              len(count_phrases(v)), len(ledger_phrases(lv)))
    return problems, counts


MUTANTS = {
    "anchor line shifted": lambda t: t.replace(
        "`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:496`",
        "`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:495`", 1),
    "anchor file renamed": lambda t: t.replace(
        "September-23-2026/build/sections/07-certificates.tex:14",
        "September-23-2026/build/sections/06-certificates.tex:14", 1),
    "block line altered": lambda t: t.replace(
        '"Recomputed exact results differ from bundled results.json")',
        '"Recomputed results differ from bundled results.json")', 1),
    "prose quote altered": lambda t: t.replace(
        "calculus, Jacobi comparison, and Sobolev arguments",
        "calculus, Jacobi comparison, and Sobolev estimates", 1),
    "count altered": lambda t: t.replace("**151** such occurrences", "**150** such occurrences", 1),
    "negative-test count altered": lambda t: t.replace(
        "ships **11** checks, **8** of them negative", "ships **11** checks, **7** of them negative", 1),
    "ledger value altered": lambda t: t.replace(
        "`verification` value of 2 for family 348",
        "`verification` value of 1 for family 348", 1),
    "abbreviated anchor": lambda t: t.replace(
        "`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:477`",
        "`.../verification/verify.py:477`", 1),
    "coverage artifact presence overstated": lambda t: t.replace(
        "all four are present in both directories", "all five are present in both directories", 1),
}


def main():
    text = PAGE.read_text(encoding="utf-8", errors="replace")

    if "--mutant" in sys.argv:
        uncaught = []
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"mutant target absent: {name}")
                uncaught.append(name)
                continue
            problems, _ = check(mutated, mutated)
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}")
        raise SystemExit(1 if uncaught else 0)

    problems, (n_anchor, n_block_lines, n_prose, n_says, n_counts, n_ledger) = check(text, text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"\nanchors {n_anchor}  block lines {n_block_lines}  prose quotes {n_prose}"
          f"  says-quotes {n_says}  count phrases {n_counts}  ledger phrases {n_ledger}"
          f"  problems {len(problems)}")
    raise SystemExit(1 if problems else 0)


main()
