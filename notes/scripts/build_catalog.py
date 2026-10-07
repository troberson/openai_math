#!/usr/bin/env python3
"""Generate notes/catalog.tsv: one row per result family.

Reads only text metadata that ships in this repo:
  overview.tex, CONTENTS.md, lean/formalization.yaml, lean/docs/*.md,
  lean/ComparatorChallenges/*.json, preprints/ layout, reasoning_traces/.

Never invokes lean, lake, or comparator. Runtime is a few seconds.
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "notes" / "catalog.tsv"

# Paren-aware: preprints/Sharp-integral-fillings-in-CAT(0)-spaces-.../paper.pdf
# Braces and backslashes must stay out of the class, or a greedy match in overview.tex
# swallows the "}\\enspace\\textperiodcentered\\enspace\\href{" separator between links.
PAP = r"preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE_SUFFIX = re.compile(rf"-(?:{MONTHS})-\d{{1,2}}-\d{{4}}$")

SHAPES = {
    "resolution": r"resolv|proves the .{0,60}conjecture|answers .{0,30}question|settles",
    "counterexample": r"counterexample|disprove|refut|fails|violation",
    "bound": r"\bbound|sharp|power-saving|improv|inequalit",
    "classification": r"\bif and only if|classified|classification|characteri[sz]",
    "undecidability": r"no algorithm|undecidable|unsolvable|negative answer",
    "density": r"density",
    "conditional": r"[Aa]ssuming|we assume|under the .{0,40}hypothes|provided that|conditional",
    "partial": r"\bat most\b|\brestricted\b|\bunramified part|\bin coranks|for fixed|partial",
    "uniform": r"\buniform(ly|ly)?\b|\bfor every\b|\barbitrary\b",
}


def read_args(text, i):
    """text[i] == '{' -> (list of brace-group bodies, index after the last group)."""
    args = []
    while i < len(text) and text[i] == "{":
        depth, j, buf = 0, i + 1, []
        while j < len(text):
            c = text[j]
            back = 0
            k = j - 1
            while k >= 0 and text[k] == "\\":
                back += 1
                k -= 1
            escaped = back % 2 == 1
            if c == "{" and not escaped:
                depth += 1
                buf.append(c)
            elif c == "}" and not escaped:
                if depth == 0:
                    break
                depth -= 1
                buf.append(c)
            else:
                buf.append(c)
            j += 1
        args.append("".join(buf))
        i = j + 1
    return args, i


def parse_overview():
    """-> (families ordered, {fam: {discipline,title,abstract,paps_links}})."""
    text = (ROOT / "overview.tex").read_text(encoding="utf-8")
    start = text.index("\\begin{document}")
    discipline = None
    fams = {}
    order = []
    i = start
    while True:
        ns = text.find("\\cataloguesection{", i)
        nr = text.find("\\resultentry{", i)
        if nr == -1:
            break
        if ns != -1 and ns < nr:
            args, i = read_args(text, ns + len("\\cataloguesection"))
            discipline = args[0]
            continue
        args, i = read_args(text, nr + len("\\resultentry"))
        fam, title, abstract, links = args[0], args[1], args[2], args[3]
        fams[fam] = {
            "discipline": discipline,
            "title": title.strip(),
            "abstract": abstract.strip(),
            "tex_paps": re.findall(PAP, links),
        }
        order.append(fam)
    return order, fams


def parse_contents():
    """-> {fam: [manuscript paths]} in document order."""
    text = (ROOT / "CONTENTS.md").read_text(encoding="utf-8")
    fam = None
    paps = defaultdict(list)
    header = re.compile(r"^\*\*(\d{3})\.\s", re.M)
    link = re.compile(r"\]\((" + PAP + r")\)")
    events = [(m.start(), "fam", m.group(1)) for m in header.finditer(text)]
    events += [(m.start(), "pap", m.group(1)) for m in link.finditer(text)]
    events.sort()
    for _, kind, val in events:
        if kind == "fam":
            fam = val
        elif fam is not None and val not in paps[fam]:
            paps[fam].append(val)
    return paps


def parse_yaml():
    """-> (set of formalized manuscript paths, {config stem: count of main_results entries})."""
    text = (ROOT / "lean" / "formalization.yaml").read_text(encoding="utf-8")
    sources = set(re.findall(r"^\s*id:\s*\.\./(" + PAP + r")", text, re.M))
    main = Counter(re.findall(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json", text))
    return sources, main


def parse_challenges():
    """-> {config stem: {theorems, definitions, nanoda}}."""
    out = {}
    for p in sorted((ROOT / "lean" / "ComparatorChallenges").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        out[p.stem] = {
            "theorems": len(d.get("theorem_names") or []),
            "definitions": len(d.get("definition_names") or []),
            "nanoda": bool(d.get("enable_nanoda")),
        }
    return out


def parse_docs():
    """-> {fam: {configs, paps, scope_chars}}."""
    docs = {}
    for p in sorted((ROOT / "lean" / "docs").glob("*.md")):
        fam = p.stem
        text = p.read_text(encoding="utf-8")
        cfgs = re.findall(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean", text)
        paps = re.findall(r"\]\(\.\./\.\./(" + PAP + r")\)", text)
        m = re.search(r"^## Scope\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        docs[fam] = {
            "configs": sorted(set(cfgs)),
            "paps": sorted(set(paps)),
            "scope_chars": len(m.group(1).strip()) if m else 0,
        }
    return docs


def parse_traces():
    """-> ({fam: [trace stems]}, stems on disk that README.md does not attribute).

    README.md tabulates every released reasoning trace against its result family,
    so the mapping is read from the release rather than guessed from filenames.
    """
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*(\d{3})\s*\|\s*\[[^\]]*\]\(reasoning_traces/([^)]+?)\.(?:pdf|tex)\)", text, re.M)
    by_fam = defaultdict(list)
    for fam, stem in rows:
        if stem not in by_fam[fam]:
            by_fam[fam].append(stem)
    listed = {s for stems in by_fam.values() for s in stems}
    on_disk = {p.stem for p in (ROOT / "reasoning_traces").iterdir() if p.is_file()}
    return by_fam, sorted(on_disk - listed)


ASSUME = re.compile(
    r"\bassuming\b|\bwe assume\b|\bprovided that\b|\bconditioned on\b|\bconditional\b"
    r"|under the [^.]{0,60}?(?:hypothes|conjecture|assumption)")
NEG_BEFORE = re.compile(r"(?:without|no)\s*$")
TECH_AFTER = re.compile(
    r"^[^.]{0,60}?(?:expectation|law|laws|probability|probabilities|measure|distribution|density)")


def conditional_hits(low):
    """Assumption phrases only.

    Drops two false-positive families found by reading all nine flagged abstracts:
    "conditional expectation/law" (a technical term) and "without assuming" (a negation
    that is often the point of the result). "unconditionally" never matches, since
    \\bconditional\\b has no word boundary inside it.
    """
    hits = []
    for m in ASSUME.finditer(low):
        if m.group() == "conditional" and TECH_AFTER.match(low[m.end():m.end() + 60]):
            continue
        if NEG_BEFORE.search(low[max(0, m.start() - 12):m.start()]):
            continue
        hits.append(m.group())
    return hits


def shapes_of(abstract):
    low = abstract.lower()
    out = [n for n, pat in SHAPES.items() if n != "conditional" and re.search(pat, low)]
    if conditional_hits(low):
        out.append("conditional")
    return out


def versions_of(paths):
    """Manuscripts whose date-stripped directory slug repeats (same paper, new date)."""
    c = Counter(DATE_SUFFIX.sub("", Path(p).parts[-2]) for p in paths)
    return sum(n for n in c.values() if n > 1)


def main():
    order, fams = parse_overview()
    fam_paps = parse_contents()
    sources, main_results = parse_yaml()
    challenges = parse_challenges()
    docs = parse_docs()
    trace_by_fam, trace_unlisted = parse_traces()

    ver_dirs = {p.parent for p in (ROOT / "preprints").glob("*/verification")}
    inputs_dirs = {p.parent for p in (ROOT / "preprints").glob("*/INPUTS.md")}
    covmd_dirs = {p.parent.parent for p in (ROOT / "preprints").glob("*/verification/COVERAGE.md")}

    cols = [
        "fam", "discipline", "title", "paps", "paps_form", "tier", "chal", "mainres",
        "scope_note", "scope_chars", "verification", "inputs", "covmd", "trace",
        "shapes", "conditional", "companions", "companion_word", "versions",
    ]
    rows = []
    for fam in sorted(fams):
        info = fams[fam]
        paths = fam_paps.get(fam, [])
        tex_paths = info["tex_paps"]
        all_paths = sorted(set(paths) | set(tex_paths))
        d = docs.get(fam)
        cfgs = d["configs"] if d else []
        in_main = [c for c in cfgs if c in main_results]
        if in_main:
            tier = "T3"
        elif cfgs:
            tier = "T2"
        elif d:
            tier = "T1"
        else:
            tier = "T0"
        shapes = shapes_of(info["abstract"])
        refs = sorted(set(re.findall(r"result (\d{3})", info["abstract"])))
        dirs = {Path(p).parts[-2] for p in all_paths}
        rows.append({
            "fam": fam,
            "discipline": info["discipline"],
            "title": info["title"],
            "paps": len(all_paths),
            "paps_form": sum(1 for p in all_paths if p in sources),
            "tier": tier,
            "chal": len(cfgs),
            "mainres": len(in_main),
            "scope_note": 1 if d else 0,
            "scope_chars": d["scope_chars"] if d else 0,
            "verification": sum(1 for x in dirs if x in ver_dirs),
            "inputs": sum(1 for x in dirs if x in inputs_dirs),
            "covmd": sum(1 for x in dirs if x in covmd_dirs),
            "trace": "|".join(sorted(trace_by_fam.get(fam, []))),
            "shapes": "|".join(shapes),
            "conditional": 1 if "conditional" in shapes else 0,
            "companions": "|".join(refs),
            "companion_word": 1 if re.search(r"\bcompanion", info["abstract"], re.I) else 0,
            "versions": versions_of(all_paths),
        })

    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")

    # ---- report: every number quoted in notes/README.md comes from here ----
    paps_all = [p for fam in fams for p in set(fam_paps.get(fam, [])) | set(fams[fam]["tex_paps"])]
    print(f"families            {len(fams)}")
    print(f"manuscripts         {len(set(paps_all))}")
    print(f"formalized (yaml)   {len(sources)}")
    print(f"challenges          {len(challenges)}")
    print(f"main_results        {sum(main_results.values())} entries / {len(main_results)} unique configs")
    print(f"scope notes         {len(docs)}")
    print(f"verification dirs   {len(ver_dirs)}   INPUTS.md {len(inputs_dirs)}   COVERAGE.md {len(covmd_dirs)}")
    n_trace = sum(len(v) for v in trace_by_fam.values())
    print(f"reasoning traces    {n_trace} attributed by README.md, {len(trace_unlisted)} on disk unattributed")
    if trace_unlisted:
        print(f"  unattributed      {trace_unlisted}")
    print("\ntier                " + "  ".join(f"{t}={sum(1 for r in rows if r['tier'] == t)}"
                                              for t in ("T3", "T2", "T1", "T0")))
    print("shapes              " + "  ".join(f"{n}={sum(1 for r in rows if n in r['shapes'].split('|'))}"
                                            for n in SHAPES))
    multi = sum(1 for r in rows if len([s for s in r["shapes"].split("|") if s]) >= 3)
    plain = sum(1 for r in rows if not r["shapes"])
    print(f"                    {multi} families match >=3 shapes, {plain} match none")
    print(f"conditional         {[r['fam'] for r in rows if r['conditional']]}")
    print(f"versions>0          {sum(1 for r in rows if r['versions'])} families, "
          f"{sum(r['versions'] for r in rows)} dated re-issues")
    print(f"companion word      {sum(r['companion_word'] for r in rows)} families")

    print("\n# discipline  fams  scope_notes  paps  paps_form")
    disc = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        c = disc[r["discipline"]]
        c[0] += 1
        c[1] += r["scope_note"]
        c[2] += r["paps"]
        c[3] += r["paps_form"]
    for name, (f, s, p, pf) in sorted(disc.items(), key=lambda kv: -kv[1][0]):
        print(f"{name:38} {f:4} {s:11} {p:5} {pf:9}")

    # Cross-check the two independent family -> manuscript mappings.
    tex_only = [(f, x) for f, x in
                ((f, sorted(set(fams[f]["tex_paps"]) - set(fam_paps.get(f, [])))) for f in sorted(fams)) if x]
    md_only = [(f, x) for f, x in
               ((f, sorted(set(fam_paps.get(f, [])) - set(fams[f]["tex_paps"]))) for f in sorted(fams)) if x]
    print(f"overview.tex links absent from CONTENTS.md: "
          f"{sum(len(x) for _, x in tex_only)} across {len(tex_only)} families")
    for f, x in tex_only:
        print(f"  fam {f}: {x}")
    print(f"CONTENTS.md links absent from overview.tex: "
          f"{sum(len(x) for _, x in md_only)} across {len(md_only)} families")
    for f, x in md_only:
        print(f"  fam {f}: {x}")
    missing = [f for f in sorted(fams) if not fam_paps.get(f)]
    if missing:
        print(f"families with no CONTENTS.md manuscript link: {missing}")
    print(f"rows written        {len(rows)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
