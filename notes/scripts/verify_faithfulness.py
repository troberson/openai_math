#!/usr/bin/env python3
"""Verify notes/formalization-faithfulness.md against the shipped files.

Report-only; writes nothing; runs nothing. Lean files are read as text — lake, lean, and comparator
are never invoked here, so no verdict in the page can mean "a statement was compiled" or "a proof
was checked". The release's review status is `unchecked`.

The checker's recomputation is its own: it carries its own declaration, carrier, environment and
literal rules, so a count the page asserts is proved against a second implementation, not against
`measure_faithfulness.py`'s. The two rules the page names as widenings (a qualified declaration
name, a `noncomputable` carrier) are in the checker too, so a mutant that removes one is caught.

1. Population. The entry and config counts, the resolved-declaration count, the carrier-typed and
   resolved-carrier counts, the carrier body sizes, the literal census, the four pairing classes,
   the `a.e.` environment census and the family/config intersection are recomputed from
   lean/formalization.yaml, lean/docs/, lean/OAI/, and preprints/. Every count phrase the page
   asserts is matched against that recomputation.
2. Anchors. Every backticked `path:line` (and `path:a-b`) anchor must resolve inside its file.
3. Fenced blocks. A block is attributed to the nearest preceding anchor and every block line must
   match that file at consecutive line numbers, with whitespace runs collapsed on both sides.
4. Quotations. Each *"…"* quote is pinned to the anchor in its own line and must occur verbatim
   at that line.
5. Tables. The disjoint table, the overlap table, and the `a.e.` table must each equal the
   recomputation, row for row.
6. Sync. The page is compared with render_reports.py's render of it, so prose that no count phrase
   covers cannot drift from the writer's template.

--mutant runs the built-in mutations and fails if any goes uncaught, the last of them a prose count
outside every count phrase — visible only to check 6.
"""
import collections
import re
import sys
from fractions import Fraction

from catlib import anchors, render as RD
from catlib.paths import DOCS_DIR, LEAN, NOTES, PREPRINTS, ROOT
from catlib.text import collapse_ws

PAGE = NOTES / "formalization-faithfulness.md"
ANCHOR = anchors.anchor_pattern(anchors.EXT_YAML, ranges=True)
QUOTE = re.compile(r'\*"([^"]{12,})"\*')
KEY = re.compile(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json")
DECL = re.compile(r"^\s*declaration:\s*(\S+)")
FILE = re.compile(r"^\s*file:\s*(\S+)")
LINK = re.compile(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean")
STMT = re.compile(r"^\s*(theorem|lemma|proposition|corollary|def|example)\s+")
TYPE = re.compile(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=")
CARR = re.compile(r"^\s*(?:private\s+|protected\s+|noncomputable\s+)?(?:def|abbrev|structure)\s+"
                  r"([A-Za-z0-9_.]+)\s*:\s*(?:Prop\s*)?[:=]")
IMP = re.compile(r"^\s*import\s+(OAI[\w.]*)\s*$")
ENV = re.compile(r"\\begin\{(theorem|maintheorem|thm)\}")
END = re.compile(r"\\end\{(theorem|maintheorem|thm)\}")
AE = re.compile(r"a\.e\.|almost every|almost all|a\.s\.|measure zero|null set", re.I)
LIT = re.compile(r"(?<![\w.])\d+(?:\s*/\s*\d+)?(?![\w.])")
FRAC = re.compile(r"\\frac\s*\{?(\d+)\}?\s*\{?(\d+)\}?")
DISROW = re.compile(r"^\|\s*`([A-Za-z0-9_]+)`\s*\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*$")
OVROW = re.compile(r"^\|\s*`([A-Za-z0-9_]+)`\s*\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
AEROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|")
OVERVIEW_TEX = ROOT / "overview.tex"

norm = collapse_ws


def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def entries():
    """config stem -> (declaration, file), first entry wins, from the yaml text."""
    out, cur = {}, {}
    for ln in read(FYAML).splitlines():
        m = KEY.search(ln)
        if m:
            cur = {"c": m.group(1)}
            out.setdefault(m.group(1), cur)
            continue
        m = DECL.match(ln)
        if m and cur:
            cur["d"] = m.group(1)
            continue
        m = FILE.match(ln)
        if m and cur:
            cur["f"] = m.group(1)
            cur = {}
    return {c: (d.get("d"), d.get("f")) for c, d in out.items()}


FYAML = ROOT / "lean" / "formalization.yaml"


def stmt_line(decl, rel):
    """The line a declaration's statement opens on, matched by full name and by bare tail."""
    p = LEAN / rel
    if not p.is_file():
        return None
    lines = read(p).splitlines()
    tail, full = decl.split(".")[-1], decl.removeprefix("OAI.")
    pat = rf"^\s*(theorem|lemma|proposition|corollary|def|example)\s+(?:{re.escape(full)}|{re.escape(tail)})\b"
    for i, ln in enumerate(lines, 1):
        if re.match(pat, ln):
            return i
    return None


def closure(rel, cap=400):
    seen, order, q = set(), [], [rel]
    while q and len(order) < cap:
        r = q.pop(0)
        p = LEAN / r
        if not p.is_file() or r in seen:
            continue
        seen.add(r)
        order.append(r)
        for ln in read(p).splitlines():
            m = IMP.match(ln)
            if m:
                q.append("/".join(m.group(1).split(".")) + ".lean")
    return order


def carrier(name, rel):
    for r in closure(rel):
        lines = read(LEAN / r).splitlines()
        for i, ln in enumerate(lines, 1):
            m = CARR.match(ln)
            if not m or m.group(1).split(".")[-1] != name:
                continue
            body = [ln.strip()]
            for nxt in lines[i:]:
                if not nxt.strip() or not nxt.startswith((" ", "\t")):
                    break
                body.append(nxt.strip())
            return r, i, body
    return None, None, []


def fams_manuscripts():
    """family -> manuscript directory names, from the overview's \\resultentry paths."""
    out = collections.defaultdict(set)
    fam = None
    for ln in read(OVERVIEW_TEX).splitlines():
        if ln.startswith("\\resultentry"):
            fam = re.search(r"\{\s*(\d{3})\s*\}", ln).group(1)
        for m in re.finditer(r"preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf", ln):
            parts = m.group(0).split("/")
            if fam and len(parts) > 1:
                out[fam].add(parts[1])
    return out


def env_bodies(dirs):
    out = []
    for d in sorted(dirs):
        for p in sorted((PREPRINTS / d).rglob("*.tex")):
            t = read(p)
            for m in ENV.finditer(t):
                c = END.search(t, m.end())
                if c:
                    out.append(t[m.end():c.start()])
    return out


def lits(text, tex=False):
    out = set()
    for tok in LIT.findall(text):
        t = tok.replace(" ", "")
        if "/" in t:
            a, b = t.split("/", 1)
            if int(b):
                out.add(Fraction(int(a), int(b)))
        else:
            out.add(Fraction(int(t)))
    if tex:
        out |= {Fraction(int(a), int(b)) for a, b in FRAC.findall(text) if int(b)}
    return out


def population():
    mr = entries()
    cfg2fam = collections.defaultdict(set)
    for p in DOCS_DIR.glob("*.md"):
        for ln in read(p).splitlines():
            for c in LINK.findall(ln):
                cfg2fam[c].add(p.stem)
    fammap = fams_manuscripts()

    bodies, unresolved, missing = {}, [], []
    typed = 0
    for c in sorted(mr):
        decl, rel = mr[c]
        at = stmt_line(decl, rel)
        if at is None:
            unresolved.append(c)
            continue
        lines = read(LEAN / rel).splitlines()
        block = [lines[at - 1]]
        j = at
        while len(block) < 12 and j < len(lines) and not block[-1].rstrip().endswith(":="):
            nxt = lines[j].strip()
            if not nxt:
                break
            block.append(nxt)
            j += 1
        m = TYPE.search(" ".join(block))
        if not m:
            continue
        typed += 1
        cf, cl, cb = carrier(m.group(1).split(".{")[0].split(".")[-1], rel)
        if cf is None:
            missing.append(c)
            continue
        bodies[c] = (cf, cl, cb)

    sizes = sorted(len(b[2]) for b in bodies.values())
    clits = {c: lits("\n".join(b[2])) for c, b in bodies.items()}
    with_lit = sum(1 for s in clits.values() if s)
    lit_total = sum(len(s) for s in clits.values())

    pair = collections.Counter()
    disjoint, overlap = [], []
    for c in sorted(bodies):
        fams_c = sorted(cfg2fam[c])
        if not fams_c:
            pair["no_family"] += 1
            continue
        if not clits[c]:
            pair["carrier_no_literal"] += 1
            continue
        mlits = set()
        for f in fams_c:
            for body in env_bodies(fammap[f]):
                mlits |= lits(body, tex=True)
        if not mlits:
            pair["no_headline_literal"] += 1
            continue
        if clits[c] == mlits:
            pair["exact"] += 1
        elif clits[c] <= mlits:
            pair["subset"] += 1
        elif not clits[c] & mlits:
            pair["disjoint"] += 1
            disjoint.append((c, fams_c[0], sorted(clits[c])))
        else:
            pair["overlap"] += 1
            extra = sorted(clits[c] - mlits)
            if extra:
                overlap.append((c, fams_c[0], extra, sorted(clits[c] & mlits)))

    ae = collections.defaultdict(int)
    env_total = 0
    for f, dirs in fammap.items():
        for body in env_bodies(dirs):
            env_total += 1
            if AE.search(body):
                ae[f] += 1
    ae_fams = sorted(ae)
    linked = {f for fs in cfg2fam.values() for f in fs}
    inter = sorted(set(ae_fams) & linked)
    cfgs = sorted(c for c, fs in cfg2fam.items() if fs & set(ae_fams))
    ae_table = []
    for f in ae_fams:
        cs = sorted(c for c, fs in cfg2fam.items() if f in fs)
        ae_table.append((f, ae[f], len(cs), len([c for c in cs if c in mr]),
                         len([c for c in cs if c not in mr])))

    return {
        "entries": len(KEY.findall(read(FYAML))), "unique": len(mr),
        "resolved": len(mr) - len(unresolved), "unresolved": unresolved,
        "typed": typed, "carriers_ok": len(bodies), "missing": missing,
        "size_min": sizes[0], "size_med": sizes[len(sizes) // 2],
        "size_max": sizes[-1], "size_sum": sum(sizes),
        "with_lit": with_lit, "lit_total": lit_total,
        "pair": pair, "disjoint": disjoint, "overlap": overlap,
        "env_total": env_total, "ae_envs": sum(ae.values()), "ae_fams": ae_fams,
        "inter": inter, "cfgs": cfgs,
        "ae_with": len([c for c in cfgs if c in mr]),
        "ae_without": len([c for c in cfgs if c not in mr]),
        "ae_table": ae_table,
    }


def count_phrases(v):
    pr = v["pair"]
    return [
        (f"Over the **{v['entries']}** `main_results` entries over **{v['unique']}** unique configs",
         "entries"),
        (f"**{v['resolved']}** of the {v['unique']} declarations resolve", "resolved"),
        (f"**{v['typed']}** of the {v['resolved']} statements are opaque", "carrier-typed"),
        (f"All **{v['carriers_ok']}** carriers resolve", "carriers resolved"),
        (f"min **{v['size_min']}** line, median **{v['size_med']}**, max **{v['size_max']}**, "
         f"sum **{v['size_sum']}** lines", "body sizes"),
        (f"**{v['with_lit']}** of the **{v['carriers_ok']}** carriers carry at least one integer "
         f"literal; **{v['lit_total']}** distinct literals in total", "literals"),
        (f"Over the **{v['carriers_ok']}** carriers, all **{v['carriers_ok']}** have a scope-note "
         f"family:", "pairing population"),
        (f"**{pr['exact']}** exact, **{pr['subset']}** lean-subset,", "pairing a"),
        (f"**{pr['overlap']}** overlap, **{pr['disjoint']}** disjoint, "
         f"**{pr['carrier_no_literal']}** carriers with no literal, "
         f"**{pr['no_headline_literal']}** families with no headline", "pairing b"),
        (f"**{v['env_total']:,}** theorem environments; **{v['ae_envs']}** carry an `a.e.`-style "
         f"phrase", "a.e. census"),
        (f"over **{len(v['ae_fams'])}** families. **{len(v['inter'])}** of those {len(v['ae_fams'])} "
         f"families", "a.e. families"),
        (f"have a scope-note config; the {len(v['inter'])} link **{len(v['cfgs'])}** configs, of "
         f"which **{v['ae_with']}** have a `main_results` entry and", "a.e. configs"),
        (f"**{v['ae_without']}** have none", "a.e. without"),
    ]


def check(text):
    problems = []
    v = population()
    n_anchor = n_block = n_quote = 0
    lines = text.split("\n")

    for m in ANCHOR.finditer(text):
        rel, at = m.group(1), int(m.group(2))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist")
            continue
        src = read(f).split("\n")
        n_anchor += 1
        hi = int(m.group(3)) if m.group(3) else at
        if not 1 <= at <= len(src) or not 1 <= hi <= len(src):
            problems.append(f"anchor {rel}:{at}-{hi} is outside the file ({len(src)} lines)")

    for i, blk in anchors.fenced_blocks(lines, dedent=True):
        found = anchors.nearest_anchor(lines, i, ANCHOR)
        if found is None:
            problems.append(f"line {i + 1}: fenced block has no preceding file:line anchor")
            continue
        rel, at = found[0], int(found[1])
        if not (ROOT / rel).exists():
            problems.append(f"line {i + 1}: anchor file {rel} does not exist")
            continue
        src = read(ROOT / rel).split("\n")
        for n, want in enumerate(blk):
            got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
            n_block += 1
            if norm(got) != norm(want):
                problems.append(f"line {i + 2}: block line {n} != {rel}:{at + n}\n"
                                f"    want {want!r}\n    got  {norm(got)!r}")

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
        src = read(ROOT / rel).split("\n")
        if not (1 <= at <= len(src)) or quote not in norm(src[at - 1]):
            problems.append(f"quote not on {rel}:{at}: {quote[:60]!r}")
        else:
            n_quote += 1

    flat = norm(text)
    for phrase, label in count_phrases(v):
        if norm(phrase) not in flat:
            problems.append(f"count mismatch ({label}): page does not contain {phrase!r}")

    d_rows = [(m.group(1), m.group(2), norm(m.group(3))) for ln in lines if (m := DISROW.match(ln))]
    want_d = [(c, f, norm(", ".join(str(x) for x in lits))) for c, f, lits in v["disjoint"]]
    if d_rows != want_d:
        problems.append(f"disjoint table {d_rows} != {want_d}")

    o_rows = [(m.group(1), m.group(2), norm(m.group(3)), norm(m.group(4)))
              for ln in lines if (m := OVROW.match(ln))]
    want_o = [(c, f, norm(", ".join(str(x) for x in extra)),
               norm(", ".join(str(x) for x in shared))) for c, f, extra, shared in v["overlap"]]
    if o_rows != want_o:
        problems.append(f"overlap table has {len(o_rows)} rows, recomputation has {len(want_o)}")
        for w, g in zip(want_o, o_rows, strict=False):
            if w != g:
                problems.append(f"overlap row {g[0]}: {g} != {w}")

    ae_rows = [tuple(int(x) for x in m.groups()) for ln in lines if (m := AEROW.match(ln))]
    if ae_rows != v["ae_table"]:
        problems.append(f"a.e. table has {len(ae_rows)} rows, recomputation has {len(v['ae_table'])}")
        for w, g in zip(v["ae_table"], ae_rows, strict=False):
            if w != g:
                problems.append(f"a.e. row {g[0]}: {g} != {w}")

    problems.extend(RD.sync_problems(PAGE, text))
    return problems, n_anchor, n_block, n_quote, len(RD.sync_problems(PAGE, text)), v


MUTANTS = {
    "entries count": lambda t: t.replace("Over the **200** `main_results` entries",
                                          "Over the **201** `main_results` entries", 1),
    "resolved count": lambda t: t.replace("**189** of the 189 declarations resolve",
                                           "**188** of the 189 declarations resolve", 1),
    "carrier-typed count": lambda t: t.replace("**61** of the 189 statements are opaque",
                                                "**60** of the 189 statements are opaque", 1),
    "median body size": lambda t: t.replace("median **6**, max **17**", "median **7**, max **17**", 1),
    "literal census": lambda t: t.replace("**126** distinct literals in total",
                                           "**127** distinct literals in total", 1),
    "pairing class count": lambda t: t.replace("**31** lean-subset,", "**32** lean-subset,", 1),
    "disjoint family": lambda t: t.replace("| `AuslanderReiten` | 199 | 2 |",
                                            "| `AuslanderReiten` | 198 | 2 |", 1),
    "overlap extra literal": lambda t: t.replace("| `GrahamSpherical` | 172 | 2, 12, 50 | 0, 1 |",
                                                  "| `GrahamSpherical` | 172 | 2, 12 | 0, 1 |", 1),
    "a.e. census": lambda t: t.replace("**2,288** theorem environments", "**2,289** theorem environments", 1),
    "a.e. row deleted": lambda t: t.replace("| 154 | 6 | 0 | 0 | 0 |\n", "", 1),
    "a.e. row count": lambda t: t.replace("| 238 | 1 | 13 | 4 | 9 |", "| 238 | 1 | 12 | 4 | 8 |", 1),
    "statement anchor shifted": lambda t: t.replace("`lean/OAI/Analysis/IntegralMeans/Model.lean:33`",
                                                    "`lean/OAI/Analysis/IntegralMeans/Model.lean:34`", 1),
    "carrier rule narrowed": lambda t: t.replace("allows `private` and `protected` but not `noncomputable`",
                                                  "allows `private` and `protected` only", 1),
    "quote anchor shifted": lambda t: t.replace("`lean/docs/260.md:11`", "`lean/docs/260.md:10`", 1),
    # Prose no count phrase reads: the comparator-sorry figure in the limitations list.
    # Only the render diff can see it.
    "prose count": lambda t: t.replace("The 416 comparator files carry 539 `sorry`s",
                                       "The 416 comparator files carry 540 `sorry`s", 1),
}


def main():
    mutant = "--mutant" in sys.argv
    text = PAGE.read_text(encoding="utf-8")
    problems, n_anchor, n_block, n_quote, n_sync, v = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"entries {v['entries']}  unique {v['unique']}  resolved {v['resolved']}  "
          f"unresolved {len(v['unresolved'])} {v['unresolved']}")
    print(f"carrier-typed {v['typed']}  carriers resolved {v['carriers_ok']}  "
          f"carrier definitions not found {len(v['missing'])} {v['missing']}")
    print(f"bodies min {v['size_min']} median {v['size_med']} max {v['size_max']} sum {v['size_sum']}  "
          f"with literal {v['with_lit']}  literals {v['lit_total']}")
    pr = v["pair"]
    print(f"exact {pr['exact']}  subset {pr['subset']}  overlap {pr['overlap']}  disjoint {pr['disjoint']}  "
          f"carrier-no-literal {pr['carrier_no_literal']}  no-headline {pr['no_headline_literal']}  "
          f"no-family {pr['no_family']}")
    print(f"a.e. envs {v['env_total']}  hits {v['ae_envs']}  families {len(v['ae_fams'])}  "
          f"inter {len(v['inter'])}  cfgs {len(v['cfgs'])}  with {v['ae_with']}  without {v['ae_without']}")
    print(f"anchors {n_anchor}  block lines {n_block}  quotations {n_quote}  sync problems {n_sync}")
    print(f"problems {len(problems)}")

    if mutant:
        failed = []
        for name, fn in MUTANTS.items():
            mtext = fn(text)
            if mtext == text:
                print(f"MUTANT {name}: NOT INJECTED (page text changed — fix the mutant)")
                failed.append(name)
                continue
            mp, _, _, _, _, _ = check(mtext)
            status = "caught" if mp else "MISSED"
            print(f"MUTANT {name}: {status} ({len(mp)} problems)")
            if not mp:
                failed.append(name)
        print(f"mutants {len(MUTANTS)}  uncaught {len(failed)} {failed}")
        return 1 if (problems or failed) else 0
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
