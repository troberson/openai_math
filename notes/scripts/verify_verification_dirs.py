#!/usr/bin/env python3
"""Verify notes/verification-dirs.md against the shipped files.

Report-only; writes nothing. Two sections are checked, each for anchors, quotations, fenced blocks, and
count phrases:

A. "## Every bundle and its own entry point" — the 30-bundle population, the README-section
   reconciliation, the entry-point class counts, the per-bundle table, and the ledger join.
B. "## What the 348 bundle checks, and what it omits" — the family-348 reading.

1. Ledger claims. The page's counts of verification dirs, `covmd`, `inputs`, and family 348's
   `verification` value are recomputed from notes/catalog.tsv.
2. Citations. Every `path:line` anchor must resolve. A fenced block is attributed to the nearest
   preceding anchor and every block line must match that file at consecutive line numbers. A quotation
   in *"..."* form is attributed to an anchor on the same line when one follows it (a table row: the
   quote must occur exactly at the anchored line, so a shifted anchor is caught); otherwise it is
   attributed to the nearest anchor that follows within 4 lines and must occur near that line.
   Whitespace runs are collapsed on both sides: line-wrapping in the page is markup, not part of the
   quote, so a quote spanning two source lines resolves against the join. A plain `"..."` quote
   introduced by "`FILE` says" is checked against the family-348 bundle.
3. Counts. Each bold count is compared with an independent recomputation from the files on disk, by
   matching the exact phrase the page must contain. The entry-point table is additionally checked
   structurally: one row per bundle, in slug order, with the family the slug belongs to.

Line counts in the family-348 section follow len(text.split("\n")), the rule the
extract_verification_348.py report uses; the entry-point section's file line count follows
splitlines(), the rule the extract_verification_dirs.py report uses. The page matches each.

--mutant runs the built-in mutations and fails if any goes uncaught.
"""
import hashlib
import json
import re
import sys

import extract_verification_dirs as evd
from catlib import anchors
from catlib.paths import LEDGER_TSV, NOTES, PREPRINTS, ROOT
from catlib.text import collapse_ws
from catlib.tsv import read_rows

PAGE = NOTES / "verification-dirs.md"
POS = PREPRINTS / "Positively-curved-Einstein-four-manifolds-September-23-2026"
ZERO = PREPRINTS / "Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026"
VPOS, VZERO = POS / "verification", ZERO / "verification"
SECTION = "## What the 348 bundle checks, and what it omits"
ENTRY = "## Every bundle and its own entry point"
FOCK = PREPRINTS / "A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026"
UNIF = PREPRINTS / "Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026"

ANCHOR = anchors.anchor_pattern(anchors.EXT_MD)
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
SAYS = re.compile(r"`([A-Za-z0-9_.-]+\.(?:md|json|py|tex))`\s+\w+\s*(?:the\s+)?[\w, ]*?\"([^\"]{12,})\"")

norm = collapse_ws


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def section_bodies(text):
    """The two checked sections as (label, body), entry-point section first."""
    out = []
    for label in (ENTRY, SECTION):
        start = text.index(label)
        nxt = text.find("\n## ", start + len(label))
        out.append((label, text[start:nxt if nxt != -1 else len(text)]))
    return out


def ledger_rows():
    return read_rows(LEDGER_TSV)


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


def entry_measure():
    """Independent recomputation of the entry-point section's population and classes.

    The population is the 30 bundles, not the 749 preprint dirs on disk (719 of them listed in
    overview.tex): a README section is read as naming a bundle only for a dir that ships one.
    """
    fam_by_slug, _order, _fams = evd.families_by_slug()
    dirs = sorted(p for p in evd.PRE.iterdir() if p.is_dir())
    bundles = [p for p in dirs if (p / "verification").is_dir()]
    named, runsec, unnamed = [], [], []
    for p in bundles:
        heads = evd.headings(p / "README.md")[1]
        if any("Verification" in h for _, h in heads):
            named.append(p.name)
        elif any("Run the verification code" in h for _, h in heads):
            runsec.append(p.name)
        else:
            unnamed.append(p.name)
    classes, no_entry, declaring = {}, [], []
    for p in bundles:
        bundle = p / "verification"
        _, rule, _ = evd.entry_point(bundle)
        classes[rule] = classes.get(rule, 0) + 1
        if rule == "none":
            no_entry.append(p)
        if evd.main_command(bundle)[0] is not None:
            declaring.append(p)
    a, b = FOCK / "verification/rows.txt", UNIF / "verification/rows.txt"
    ta = a.read_text(encoding="utf-8", errors="replace")
    return {
        "dirs": len(bundles),
        "fams": len({fam_by_slug.get(p.name) for p in bundles}),
        "named": len(named) + len(runsec),
        "ver": len(named),
        "run": len(runsec),
        "unnamed": sorted(unnamed),
        "classes": classes,
        "no_entry": len(no_entry),
        "no_entry_fams": [fam_by_slug.get(p.name) for p in no_entry
                          if fam_by_slug.get(p.name) != "269"],
        "rule4": sum(v for k, v in classes.items() if k.startswith("manifest")),
        "declaring": len(declaring),
        "rows_lines": len(ta.splitlines()),
        "rows_bytes": a.stat().st_size,
        "rows_identical": a.read_bytes() == b.read_bytes(),
        "rows_pair": a.exists() and b.exists(),
        "table": [fam_by_slug.get(p.name) for p in bundles],
    }


def entry_phrases(v):
    """Exact phrases the entry-point section must contain for its counts to be honest."""
    c = v["classes"]
    return [
        (f"A README section names **{v['named']}** of the **{v['dirs']}** bundles", "named/dir counts"),
        (f"**{v['ver']}** carry `## Verification` and **{v['run']}** carries", "README heading counts"),
        (f"**{len(v['unnamed'])}** bundles ship a `verification/` tree their README never mentions",
         "unnamed bundle count"),
        (f"Each is {v['rows_lines']} lines and {v['rows_bytes']} bytes, and the two files are "
         "**byte-identical**", "rows.txt size and identity"),
        (f"**{c.get('top-level README.md', 0)}** top-level `README.md`, "
         f"**{c.get('subdirectory README.md', 0)}** a subdirectory `README.md`, "
         f"**{c.get('top-level script by name', 0)}** a top-level script by name, "
         f"**{c.get('subdirectory README.txt', 0)}** a subdirectory `README.txt`, "
         f"**{v['no_entry']}** with **no entry point**", "entry-point class counts"),
        (f"Rule 4 fires for **{v['rule4']}** bundles", "rule 4 firing count"),
        (f"the {WORDS[v['declaring']]} family-348 dirs that declare `main_command` are claimed by "
         "rule 1 first", "manifest main_command count"),
        (f"The {v['no_entry']} with no entry point are the two 269 dirs above plus "
         f"{', '.join(v['no_entry_fams'][:-1])} and {v['no_entry_fams'][-1]}",
         "no-entry-point family list"),
    ]


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
    n_anchor = n_block_lines = n_prose = n_row_quotes = n_says = 0

    for _label, body in section_bodies(text):
        lines = body.split("\n")

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
        for i, blk in anchors.fenced_blocks(lines, dedent=True):
            anchor = anchors.nearest_anchor(lines, i, ANCHOR, window=9)
            if anchor is None:
                problems.append(f"section line {i + 1}: fenced block has no preceding file:line anchor")
            elif not (ROOT / anchor[0]).exists():
                problems.append(f"section line {i + 1}: anchor file {anchor[0]} does not exist")
            else:
                rel, at = anchor[0], int(anchor[1])
                src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                for n, want in enumerate(blk):
                    got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
                    n_block_lines += 1
                    if got != want:
                        problems.append(
                            f"section line {i + 2}: block line {n} != {rel}:{at + n}\n"
                            f"    want {want!r}\n    got  {got!r}")

        # quotations: an anchor in the quote's own line (a table row) pins it to that line exactly;
        # otherwise the nearest anchor that follows within 4 lines, with the old proximity rule.
        for m in QUOTE.finditer(body):
            quote = norm(m.group(1))
            row = lines[body[: m.start()].count("\n")]
            span = row.find(m.group(0))
            same = []
            if span != -1:
                same = ANCHOR.findall(row[span + len(m.group(0)):])[:1] \
                    or ANCHOR.findall(row[:span])[-1:]
            anchor = None
            if same:
                anchor = (same[0][0], int(same[0][1]))
            else:
                for ln in body[m.end():].split("\n")[:4]:
                    found = ANCHOR.findall(ln)
                    if found:
                        anchor = (found[0][0], int(found[0][1]))
                        break
            if anchor is None:
                problems.append(f"quote has no anchor in its line or within 4 lines after it: {quote[:60]!r}")
                continue
            rel, at = anchor
            if not (ROOT / rel).exists():
                problems.append(f"quote anchor file {rel} does not exist")
                continue
            src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
            hits = [k + 1 for k, ln in enumerate(src) if quote in norm(ln)]
            if not hits:
                # multi-line quote: join consecutive lines
                hits = [k + 1 for k in range(len(src) - 1)
                        if quote in norm(src[k] + " " + src[k + 1])]
            if not hits:
                problems.append(f"quote not found in {rel}: {quote[:60]!r}")
            elif same:
                n_row_quotes += 1
                if at not in hits:
                    problems.append(f"row quote anchored at {rel}:{at} occurs only at lines {hits}")
            elif not any(abs(h - at) <= 4 for h in hits):
                problems.append(f"prose quote anchored at {rel}:{at} occurs only at lines {hits}")
            else:
                n_prose += 1

    for label, body in section_bodies(text):
        if label != SECTION:
            continue
        for m in SAYS.finditer(body):
            rel, quote = m.group(1), norm(m.group(2))
            f = next((c for c in (VPOS / rel, VZERO / rel) if c.exists()), None)
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

    e = entry_measure()
    for phrase, label in entry_phrases(e):
        if norm(phrase) not in flat:
            problems.append(f"entry-point count mismatch ({label}): page does not contain {phrase!r}")
    for phrase, label in [(f"sums to {lv['dirs']} dirs over {lv['fams']} families",
                           "entry-section ledger join")]:
        if norm(phrase) not in flat:
            problems.append(f"entry-point count mismatch ({label}): page does not contain {phrase!r}")

    entry_body = section_bodies(text)[0][1]
    rows = re.findall(r"^\| (\d{3}) \|", entry_body, re.M)
    if len(rows) != e["dirs"]:
        problems.append(f"entry-point table has {len(rows)} rows, the bundle count is {e['dirs']}")
    elif rows != e["table"]:
        bad = [f"{i + 1}: {r} != {t}" for i, (r, t) in enumerate(zip(rows, e["table"], strict=False)) if r != t]
        problems.append(f"entry-point table family order: {'; '.join(bad)}")
    bullets = re.findall(r"^- `preprints/([^`]+)`", entry_body, re.M)
    if len(bullets) != len(e["unnamed"]):
        problems.append(f"unnamed-bundle list has {len(bullets)} bullets, the count is {len(e['unnamed'])}")
    for slug in bullets:
        if not (ROOT / "preprints" / slug).exists():
            problems.append(f"unnamed bundle preprints/{slug} does not exist")
    if not e["rows_pair"]:
        problems.append("the two family-269 rows.txt files are not both present")
    if not e["rows_identical"]:
        problems.append("the two family-269 rows.txt files are not byte-identical")

    counts = (n_anchor, n_block_lines, n_prose, n_row_quotes, n_says,
              len(count_phrases(v)), len(ledger_phrases(lv)), len(entry_phrases(e)) + 1,
              len(rows))
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
    "entry class count altered": lambda t: t.replace(
        "**12** top-level `README.md`", "**13** top-level `README.md`", 1),
    "unnamed bundle count altered": lambda t: t.replace(
        "**2** bundles ship a `verification/` tree", "**3** bundles ship a `verification/` tree", 1),
    "entry-section quote altered": lambda t: t.replace(
        "*\"They verify finite scalar, thermal, and trial calculations, not the analytic proof.\"*",
        "*\"They verify finite scalar, thermal, and trial calculations, not the analytic argument.\"*", 1),
    "entry-section anchor shifted": lambda t: t.replace(
        "chain-September-24-2026/verification/README.md:54`",
        "chain-September-24-2026/verification/README.md:53`", 1),
    "rows.txt size altered": lambda t: t.replace("20 lines and 1436 bytes", "20 lines and 1437 bytes", 1),
    "table row family altered": lambda t: t.replace("| 371 | `Stable-Self-Similar", "| 372 | `Stable-Self-Similar", 1),
    "rule 4 firing count altered": lambda t: t.replace("Rule 4 fires for **0** bundles",
                                                       "Rule 4 fires for **1** bundles", 1),
    "entry-section ledger sum altered": lambda t: t.replace("sums to 30 dirs over 22 families",
                                                            "sums to 31 dirs over 22 families", 1),
    "table row deleted": lambda t: re.sub(r"^\| 371 \| .*$\n", "", t, count=1, flags=re.M),
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

    problems, (n_anchor, n_block_lines, n_prose, n_row, n_says, n_counts, n_ledger,
               n_entry, n_rows) = check(text, text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"\nanchors {n_anchor}  block lines {n_block_lines}  prose quotes {n_prose}"
          f"  row quotes {n_row}  says-quotes {n_says}  count phrases {n_counts}"
          f"  ledger phrases {n_ledger}  entry phrases {n_entry}  table rows {n_rows}"
          f"  problems {len(problems)}")
    raise SystemExit(1 if problems else 0)


main()
