#!/usr/bin/env python3
"""Verify notes/counterexample-crosscheck.md against the shipped files.

Report-only; writes nothing; runs nothing. Lean files are read as text — lake, lean, and comparator
are never invoked here, so no verdict in the page can mean "a proof was checked".

1. Population. The 28-family population, its tier split, its ledger sums, the main_results entry and
   config counts, the per-family linked-config / entry / gap counts, the carrier-typed count, and the
   stub and sorry counts are all recomputed from notes/catalog.tsv, overview.tex,
   lean/formalization.yaml, lean/docs/, and lean/ComparatorChallenges/. Every count phrase the page
   asserts is matched against that recomputation.
2. Anchors. Every backticked `path:line` anchor must resolve inside its file.
3. Fenced blocks. A block is attributed to the nearest preceding anchor and every block line must
   match that file at consecutive line numbers. Whitespace runs are collapsed on both sides:
   indentation in a quoted Lean or yaml line is markup, not part of the quotation.
4. Quotations. Each *"..."* quote is pinned to the anchor in its own line and must occur verbatim at
   that line — so a claim sentence moved to another family's resultentry line is caught.
5. Tables. The 28-row summary table must have one row per population family, in population order,
   with tier, configs, entries, and gaps equal to the recomputation. The 12-row gap table must list
   exactly the T3 configs with no entry, each anchored at a scope-note line that names it. The
   9-row T2 table must list exactly the T2 population with its no-entry configs.
6. Entries. For each of the 28 entries the page must cite its yaml block at the
   `- comparator_config:` line, its statement anchor at the line where the declaration opens, and —
   for the 11 carrier-typed statements — the carrier's definition anchor. Each cited line is checked
   against the file.
7. Per-family blocks. Each T3 block must name exactly its own family's linked configs and state the
   right number of no-entry configs.

--mutant runs the built-in mutations and fails if any goes uncaught.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_catalog
import extract_counterexample_crosscheck as cx
import extract_subfinding_pairs as ep

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "counterexample-crosscheck.md"
ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json|txt|lean|yaml)):(\d+)`")
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(T\d)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|")
GAPROW = re.compile(r"^\|\s*`([A-Za-z0-9_]+)`\s*\|\s*(\d{3})\s*\|\s*`([\w./+-]+\.md):(\d+)`\s*\|")
T2ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*`([\w./+-]+\.md):(\d+)`\s*\|")
CONFIGS_DIR = ROOT / "lean" / "ComparatorChallenges"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def population():
    rows = {r["fam"]: r for r in cx.ledger_rows()}
    order, fams = build_catalog.parse_overview()
    shape = [f for f in order if "counterexample" in build_catalog.shapes_of(fams[f]["abstract"])]
    pop = [f for f in shape if rows[f]["tier"] != "T0"]
    mr, entries = cx.main_results()
    per = {}
    for f in pop:
        _doc, links = cx.scope_note(f)
        cfgs = sorted({c for _, c in links})
        per[f] = {
            "tier": rows[f]["tier"],
            "links": links,
            "configs": cfgs,
            "entries": sorted(c for c in cfgs if c in mr),
            "gaps": sorted(c for c in cfgs if c not in mr),
            "mainres": int(rows[f]["mainres"]),
            "line": ep.resultentry_lines()[f],
        }
    stubs = {c for f in pop for c in per[f]["configs"]}
    sorries = sum((CONFIGS_DIR / f"{c}.lean").read_text(encoding="utf-8", errors="replace").count("sorry")
                  for c in stubs)
    carriers = 0
    for f in pop:
        for c in per[f]["entries"]:
            decl, rel, _ = mr[c]
            at, block = cx.declaration_statement(decl, rel)
            if at and re.search(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=", " ".join(block)):
                carriers += 1
    allrows = list(cx.ledger_rows())
    return {
        "rows": rows, "fams": fams, "pop": pop, "per": per, "mr": mr,
        "shape": len(shape), "t0": len(shape) - len(pop),
        "t3": sum(1 for f in pop if rows[f]["tier"] == "T3"),
        "t2": sum(1 for f in pop if rows[f]["tier"] == "T2"),
        "mainres": sum(int(rows[f]["mainres"]) for f in pop),
        "chal": sum(int(rows[f]["chal"]) for f in pop),
        "paps_form": sum(int(rows[f]["paps_form"]) for f in pop),
        "paps": sum(int(rows[f]["paps"]) for f in pop),
        "entries": len(entries), "unique": len(set(entries)),
        "with_entry": sum(1 for f in pop if per[f]["entries"]),
        "no_entry": sum(1 for f in pop if not per[f]["entries"]),
        "configs": len(stubs), "sorries": sorries, "carriers": carriers,
        "t3_gaps": sorted(c for f in pop if per[f]["tier"] == "T3" for c in per[f]["gaps"]),
        "t3_gap_fams": len({f for f in pop if per[f]["tier"] == "T3" and per[f]["gaps"]}),
        "t2_gaps": sum(len(per[f]["gaps"]) for f in pop if per[f]["tier"] == "T2"),
        "broad": sum(1 for r in allrows if r["counterex_broad"] == "1"),
        "broad_t0": sum(1 for r in allrows if r["counterex_broad"] == "1" and r["tier"] == "T0"),
        "broad_t3": sum(1 for r in allrows if r["counterex_broad"] == "1" and r["tier"] == "T3"),
        "broad_t2": sum(1 for r in allrows if r["counterex_broad"] == "1" and r["tier"] == "T2"),
    }


def count_phrases(v):
    return [
        (f"**{v['pop'] and len(v['pop'])}** families", "population"),
        (f"**{v['t3']}** at T3 and **{v['t2']}** at T2", "tier split"),
        (f"**{v['shape']}** families overall", "shape total"),
        (f"**{v['t0']}** carry the tag at T0", "T0 shape"),
        (f"**{v['mainres']}** `main_results` declarations", "ledger mainres"),
        (f"**{v['chal']}** comparator configs", "ledger chal"),
        (f"**{v['paps_form']}** formalized manuscripts out of **{v['paps']}**", "ledger paps_form/paps"),
        (f"**{v['entries']}** `main_results` entries over **{v['unique']}** unique configs", "yaml entries"),
        (f"**{v['with_entry']}** have at least one entry and **{v['no_entry']}** have none", "entry split"),
        (f"All **{v['mainres']}** declarations resolve", "declarations resolved"),
        (f"**{v['carriers']}** of the {v['mainres']} are written", "carrier-typed"),
        (f"all **{v['carriers']}** carriers resolve", "carriers resolved"),
        (f"**{v['configs']}** distinct configs", "linked configs"),
        (f"**{v['mainres']}** of them carry an entry and "
         f"**{v['configs'] - v['mainres']}** carry none", "config entry split"),
        (f"**{len(v['t3_gaps'])}** configs in **{v['t3_gap_fams']}** families", "T3 gaps"),
        (f"**{v['t2_gaps']}** configs in all **{v['t2']}** families", "T2 gaps"),
        (f"carrying **{v['sorries']}** `sorry` occurrences", "stub sorries"),
        (f"fires on **{v['t0']}** T0 families", "bead T0 shape"),
        ("The **21** is the count", "bead prose 21"),
        (f"{v['broad']} families corpus-wide: {v['broad_t0']} T0, {v['broad_t3']} T3, {v['broad_t2']} T2",
         "broad rule"),
    ]


def check(text):
    problems = []
    v = population()
    n_anchor = n_block = n_quote = 0
    lines = text.split("\n")

    # 1. anchors resolve
    for m in ANCHOR.finditer(text):
        rel, at = m.group(1), int(m.group(2))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist")
            continue
        src = f.read_text(encoding="utf-8", errors="replace").split("\n")
        n_anchor += 1
        if not 1 <= at <= len(src):
            problems.append(f"anchor {rel}:{at} is outside the file ({len(src)} lines)")

    # 2. fenced blocks -> nearest preceding anchor
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            j, blk = i + 1, []
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
                problems.append(f"line {i + 1}: fenced block has no preceding file:line anchor")
            elif not (ROOT / anchor[0]).exists():
                problems.append(f"line {i + 1}: anchor file {anchor[0]} does not exist")
            else:
                rel, at = anchor
                src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                for n, want in enumerate(blk):
                    got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
                    n_block += 1
                    if norm(got) != norm(want):
                        problems.append(
                            f"line {i + 2}: block line {n} != {rel}:{at + n}\n"
                            f"    want {want!r}\n    got  {norm(got)!r}")
            i = j + 1
        else:
            i += 1

    # 3. quotations pinned to the anchor in their own line
    for m in QUOTE.finditer(text):
        quote = norm(m.group(1))
        row = lines[text[: m.start()].count("\n")]
        span = row.find(m.group(0))
        found = ANCHOR.findall(row[span + len(m.group(0)):])[:1] or ANCHOR.findall(row[:span])[-1:]
        if not found:
            problems.append(f"quote has no anchor in its line: {quote[:60]!r}")
            continue
        rel, at = found[0][0], int(found[0][1])
        if not (ROOT / rel).exists():
            problems.append(f"quote anchor file {rel} does not exist")
            continue
        src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        if not (1 <= at <= len(src)) or quote not in norm(src[at - 1]):
            problems.append(f"quote not on {rel}:{at}: {quote[:60]!r}")
        else:
            n_quote += 1

    # 4. count phrases
    flat = norm(text)
    for phrase, label in count_phrases(v):
        if norm(phrase) not in flat:
            problems.append(f"count mismatch ({label}): page does not contain {phrase!r}")

    # 5. summary table
    rows = [m.groups() for ln in lines if (m := ROW.match(ln))]
    want = [(f, v["per"][f]["tier"], len(v["per"][f]["configs"]),
             len(v["per"][f]["entries"]), len(v["per"][f]["gaps"])) for f in v["pop"]]
    got = [(f, t, int(c), int(e), int(g)) for f, t, c, e, g in rows]
    if got != want:
        for n, (w, g) in enumerate(zip(want, got + [("<none>",)] * len(want), strict=False)):
            if w != g:
                problems.append(f"summary table row {n + 1}: {g} != {w}")
        if len(got) != len(want):
            problems.append(f"summary table has {len(got)} rows, population has {len(want)}")

    # 6. gap table
    gap_rows = [(m.group(1), m.group(2), m.group(3), int(m.group(4)))
                for ln in lines if (m := GAPROW.match(ln))]
    want_gaps = sorted((c, f) for f in v["pop"] if v["per"][f]["tier"] == "T3"
                       for c in v["per"][f]["gaps"])
    if sorted((c, f) for c, f, _, _ in gap_rows) != want_gaps:
        problems.append(f"gap table lists {sorted((c, f) for c, f, _, _ in gap_rows)}, "
                        f"expected {want_gaps}")
    for c, f, rel, at in gap_rows:
        src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        if not (1 <= at <= len(src)) or f"ComparatorChallenges/{c}.lean" not in src[at - 1]:
            problems.append(f"gap row {c} ({f}): {rel}:{at} does not name that config")

    # 7. T2 table
    t2_rows = [(m.group(1), m.group(2), m.group(3), int(m.group(4)))
               for ln in lines if (m := T2ROW.match(ln))]
    t2_pop = [f for f in v["pop"] if v["per"][f]["tier"] == "T2"]
    if [f for f, _, _, _ in t2_rows] != t2_pop:
        problems.append(f"T2 table families {[f for f, _, _, _ in t2_rows]} != {t2_pop}")
    for f, cell, rel, at in t2_rows:
        cfgs = re.findall(r"`([A-Za-z0-9_]+)`", cell)
        if cfgs != v["per"][f]["gaps"]:
            problems.append(f"T2 row {f}: configs {cfgs} != {v['per'][f]['gaps']}")
        src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        if not (1 <= at <= len(src)) or not any(f"ComparatorChallenges/{c}.lean" in src[at - 1]
                                               for c in cfgs):
            problems.append(f"T2 row {f}: {rel}:{at} names none of {cfgs}")

    # 8. every entry's yaml block, statement anchor, and carrier anchor
    for f in v["pop"]:
        for c in v["per"][f]["entries"]:
            decl, rel, yline = v["mr"][c]
            start = yline - 2
            if f"`lean/formalization.yaml:{start}`" not in text:
                problems.append(f"family {f} config {c}: no yaml anchor at "
                                f"lean/formalization.yaml:{start}")
            ysrc = (ROOT / "lean" / "formalization.yaml").read_text(
                encoding="utf-8", errors="replace").split("\n")
            trio = "\n".join(ysrc[start - 1:start + 2])
            if f"ComparatorChallenges/{c}.json" not in trio or decl not in trio or rel not in trio:
                problems.append(f"family {f} config {c}: yaml:{start} is not its entry")
            at, block = cx.declaration_statement(decl, rel)
            if at is None:
                problems.append(f"family {f} config {c}: statement not found in {rel}")
                continue
            if f"`lean/{rel}:{at}`" not in text:
                problems.append(f"family {f} config {c}: no statement anchor at lean/{rel}:{at}")
            tail = decl.split(".")[-1]
            ssrc = (ROOT / "lean" / rel).read_text(encoding="utf-8", errors="replace").split("\n")
            if not re.match(rf"^\s*(theorem|lemma|proposition|corollary|def|example)\s+{re.escape(tail)}\b",
                            ssrc[at - 1]):
                problems.append(f"family {f} config {c}: {rel}:{at} does not open {decl}")
            m = re.search(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=", " ".join(block))
            if not m:
                continue
            cname = m.group(1).split(".{")[0].split(".")[-1]
            cfile, cline, _ = cx.carrier(cname, rel)
            if cfile is None:
                problems.append(f"family {f} config {c}: carrier {cname} not found")
                continue
            if f"`lean/{cfile}:{cline}`" not in text:
                problems.append(f"family {f} config {c}: no carrier anchor at lean/{cfile}:{cline}")

    # 9. per-family blocks name exactly their own configs and the right gap count
    t3_pop = [f for f in v["pop"] if v["per"][f]["tier"] == "T3"]
    heads = re.findall(r"^### (\d{3}) —", text, re.M)
    if heads != t3_pop:
        problems.append(f"T3 blocks {heads} != {t3_pop}")
    universe = {p.stem for p in CONFIGS_DIR.glob("*.json")}
    for _n, f in enumerate(heads):
        start = text.index(f"### {f} —")
        nxt = re.search(r"^### |^## ", text[start + 5:], re.M)
        body = text[start + 5:start + 5 + (nxt.start() if nxt else len(text))]
        named = sorted({c for c in re.findall(r"`([A-Za-z0-9_]+)`", body) if c in universe})
        if named != v["per"][f]["configs"]:
            problems.append(f"block {f}: configs {named} != {v['per'][f]['configs']}")
        stated = body.count("no `main_results` entry")
        if stated != len(v["per"][f]["gaps"]):
            problems.append(f"block {f}: {stated} no-entry statements, gaps are "
                            f"{len(v['per'][f]['gaps'])}")

    return problems, n_anchor, n_block, n_quote, v


MUTANTS = {
    "tier swap": lambda t: t.replace("| 047 | T3 | 1 | 1 | 0 |", "| 047 | T2 | 1 | 1 | 0 |", 1),
    "config count": lambda t: t.replace("| 172 | T3 | 7 | 2 | 5 |", "| 172 | T3 | 6 | 2 | 4 |", 1),
    "statement anchor shifted": lambda t: t.replace("`lean/OAI/Algebra/AffineCancellation/Main.lean:32`",
                                                    "`lean/OAI/Algebra/AffineCancellation/Main.lean:33`", 1),
    "carrier body word": lambda t: t.replace("ringKrullDim A = 4", "ringKrullDim A = 5", 1),
    "claim quote word": lambda t: t.replace("disproving affine-space cancellation",
                                            "disproving affine-space duality", 1),
    "yaml anchor shifted": lambda t: t.replace("`lean/formalization.yaml:1041`",
                                               "`lean/formalization.yaml:1042`", 1),
    "gap row family": lambda t: t.replace("| `BalancedRyser` | 162 |", "| `BalancedRyser` | 185 |", 1),
    "sorry count": lambda t: t.replace("carrying **55** `sorry` occurrences",
                                        "carrying **57** `sorry` occurrences", 1),
    "T2 row deleted": lambda t: t.replace("| 151 | `C1EntropyCounterexample` | `lean/docs/151.md:15` |\n", "", 1),
    "T2 config from another family": lambda t: t.replace("`C1EntropyCounterexample` | `lean/docs/151.md:15`",
                                                          "`Naimark` | `lean/docs/151.md:15`", 1),
    "carrier paraphrase": lambda t: t.replace("¬ Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)",
                                              "Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)", 1),
    "anchor file absent": lambda t: t.replace("`lean/OAI/Geometry/Arnold/Main.lean:14`",
                                              "`lean/OAI/Geometry/Arnold/Nope.lean:14`", 1),
    "quote moved to another family": lambda t: t.replace(
        "Claim 2 (`overview.tex:170`) — *\"It also disproves the Dolgachev",
        "Claim 2 (`overview.tex:218`) — *\"It also disproves the Dolgachev", 1),
}


def main():
    mutant = "--mutant" in sys.argv
    text = PAGE.read_text(encoding="utf-8")
    problems, n_anchor, n_block, n_quote, v = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"population {len(v['pop'])}  T3 {v['t3']}  T2 {v['t2']}  shape {v['shape']}  T0 shape {v['t0']}")
    print(f"ledger mainres {v['mainres']}  chal {v['chal']}  paps_form {v['paps_form']}  paps {v['paps']}")
    print(f"yaml entries {v['entries']}  unique configs {v['unique']}  carriers {v['carriers']}")
    print(f"linked configs {v['configs']}  T3 gaps {len(v['t3_gaps'])} in {v['t3_gap_fams']} families  "
          f"T2 gaps {v['t2_gaps']}  stub sorries {v['sorries']}")
    print(f"anchors {n_anchor}  block lines {n_block}  quotations {n_quote}")
    print(f"problems {len(problems)}")

    if mutant:
        failed = []
        for name, fn in MUTANTS.items():
            mtext = fn(text)
            if mtext == text:
                print(f"MUTANT {name}: NOT INJECTED (page text changed — fix the mutant)")
                failed.append(name)
                continue
            mp, _, _, _, _ = check(mtext)
            status = "caught" if mp else "MISSED"
            print(f"MUTANT {name}: {status} ({len(mp)} problems)")
            if not mp:
                failed.append(name)
        print(f"mutants {len(MUTANTS)}  uncaught {len(failed)} {failed}")
        return 1 if (problems or failed) else 0
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
