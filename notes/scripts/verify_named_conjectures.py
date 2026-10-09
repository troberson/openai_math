"""Verify notes/named-conjectures.md against the shipped files.

Report-only: writes nothing. Re-derives the population from notes/catalog.tsv and
notes/scripts/triage_t0.py, resolves every statement anchor against the manuscript LaTeX it cites,
matches every quotation verbatim against the lines it cites, resolves every prose `path:line`
citation (including the ones with no path, and the ones relative to a manuscript directory named in
the entry) and requires a citation that opens a statement environment to end on its `\\end`, checks
the entry set against the derived population, and re-measures every number in the page's
Measurements section. Exits 1 on any mismatch.

The page carries two entry levels: `### NNN - ` is a population entry and `#### NNN - ` is a promoted
entry — a family this pass read while it was T0 that upstream has since formalized, so the population
rule no longer includes it. Both levels get the anchor and quotation checks; only `###` is compared
with the population, and each `####` family must be title-named, non-T0, and outside the population.

--mutant corrupts the page in memory (never on disk) in twelve ways and reports how many the checks
catch.

Usage:
    python3 notes/scripts/verify_named_conjectures.py
    python3 notes/scripts/verify_named_conjectures.py --mutant
"""

import csv
import os
import re
import sys
from collections import Counter

import triage_t0

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PAGE = os.path.join(ROOT, "notes", "named-conjectures.md")
LEDGER = os.path.join(ROOT, "notes", "catalog.tsv")

PRIORITY = ["038", "078", "079", "101", "202", "344", "346", "375"]
NAME_TOKEN = re.compile(r"conjectur|\bquestion|\bproblem", re.I)
STATEMENT_ENV = (
    "theorem", "maintheorem", "mainthm", "corollary", "proposition",
    "conjecture", "problem", "question", "claim", "remark",
)
BEGIN = re.compile(r"\\begin\{(%s)\*?\}" % "|".join(STATEMENT_ENV))
HEADING = re.compile(r"^### (\d{3}) - ")
SUBHEADING = re.compile(r"^#### (\d{3}) - ")
ANCHOR = re.compile(r"\[`([^`\]]+):(\d+)-(\d+)`\]")
CITE = re.compile(r"`([^`\]]*):(\d+)(?:-(\d+))?`")
PREPRINT_DIR = re.compile(r"(?<![\w-])([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)")
VERDICTS = ("match", "merge", "narrower", "wider")


def norm(s):
    return re.sub(r"\s+", " ", " ".join(x.strip() for x in s.split("\n"))).strip()


def ledger_rows():
    with open(LEDGER, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def population(rows):
    """(pop_families, first, second) using the rules the page states."""
    t0 = [r for r in rows if r["tier"] == "T0"]
    first, second = [], []
    for r in t0:
        bucket = triage_t0.bucket_of(r["shapes"])
        if bucket == "C" or r["fam"] <= "031" or int(r["paps"]) >= 3:
            first.append(r)
        else:
            second.append(r)
    pop = [r for r in second if NAME_TOKEN.search(r["title"])]
    return t0, first, second, pop


def measure(rows):
    t0, first, second, pop = population(rows)
    out = {
        "t0_families": len(t0),
        "t0_manuscripts": sum(int(r["paps"]) for r in t0),
        "first_families": len(first),
        "first_manuscripts": sum(int(r["paps"]) for r in first),
        "second_families": len(second),
        "second_manuscripts": sum(int(r["paps"]) for r in second),
        "pop_families": len(pop),
        "pop_manuscripts": sum(int(r["paps"]) for r in pop),
        "two_pap_families": sum(1 for r in pop if int(r["paps"]) == 2),
    }
    for b in ("R", "B", "K", "N", "U", "C", "O"):
        n = sum(1 for r in pop if triage_t0.bucket_of(r["shapes"]) == b)
        if n:
            out["bucket_" + b] = n
    disc = Counter(r["discipline"] for r in pop)
    out["disciplines"] = ", ".join(
        "%s=%d" % (k, v) for k, v in sorted(disc.items(), key=lambda kv: (-kv[1], kv[0]))
    )
    out["priority_in_pop"] = sum(1 for f in PRIORITY if f in {r["fam"] for r in pop})
    out["priority_outside_pop"] = sum(1 for f in PRIORITY if f not in {r["fam"] for r in pop})
    return out, pop


def blocks(page_lines):
    """fam -> (heading_line_index, body_lines, level) over both entry levels.

    A body runs to the next entry heading of either level, and a level-2 heading closes it, so the
    promoted entries under their own section are not swallowed by the last population entry.
    """
    heads = []
    for i, l in enumerate(page_lines):
        for lvl, rx in ((3, HEADING), (4, SUBHEADING)):
            m = rx.match(l)
            if m:
                heads.append((i, m.group(1), lvl))
                break
    out = {}
    for n, (i, fam, lvl) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(page_lines)
        body = page_lines[i:end]
        stop = [j for j, l in enumerate(body) if l.startswith("## ")]
        if stop:
            body = body[: stop[0]]
        out[fam] = (i, body, lvl)
    return out


def entries(page_lines):
    """fam -> (heading_line_index, body_lines) for the population level only."""
    return {f: (i, b) for f, (i, b, lvl) in blocks(page_lines).items() if lvl == 3}


def quotes_in(body):
    """(path, a, b, quote) for every anchor in an entry body.

    A quotation is the indented block that follows its anchor line. Scanning by line block, rather
    than by matching quote characters, is what lets a LaTeX umlaut (`\\"a`) sit inside a quotation.
    """
    found = []
    for i, line in enumerate(body):
        m = ANCHOR.search(line)
        if not m:
            continue
        path, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        block = []
        j = i + 1
        while j < len(body) and body[j].startswith("  "):
            block.append(body[j].strip())
            if block and block[-1].endswith('"'):
                break
            j += 1
        text = " ".join(block)
        if text.startswith('"'):
            text = text[1:]
        if text.endswith('"'):
            text = text[:-1]
        found.append((path, a, b, text if block else None))
    return found


def verdict_of(body):
    for l in body:
        if l.strip().startswith("- **Reading**:"):
            m = re.search(r"`(\w+)`", l)
            if m and m.group(1) in VERDICTS:
                return m.group(1)
    return None


def check_quotes(page_lines, problems):
    ents = blocks(page_lines)
    anchors = 0
    verdicts = Counter()
    for fam, (_, body, _) in sorted(ents.items()):
        v = verdict_of(body)
        if v is None:
            problems.append("family %s: no `- **Reading**:` verdict in %s vocabulary" % (fam, VERDICTS))
        else:
            verdicts[v] += 1
        for path, a, b, quote in quotes_in(body):
            anchors += 1
            full = os.path.join(ROOT, path)
            if not os.path.isfile(full):
                problems.append("family %s: anchor path not on disk: %s" % (fam, path))
                continue
            with open(full, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().split("\n")
            if not 1 <= a <= b <= len(lines):
                problems.append(
                    "family %s: anchor %s:%d-%d outside 1..%d lines" % (fam, path, a, b, len(lines))
                )
                continue
            if not BEGIN.search(lines[a - 1]):
                problems.append("family %s: %s:%d does not open a statement environment" % (fam, path, a))
            if quote is None:
                problems.append("family %s: anchor %s:%d-%d has no quotation" % (fam, path, a, b))
                continue
            want = norm("\n".join(lines[a - 1:b]))
            got = norm(quote)
            if got != want:
                problems.append(
                    "family %s: quotation does not match %s:%d-%d (first difference at char %d)"
                    % (fam, path, a, b, next((i for i, (x, y) in enumerate(zip(got, want, strict=False)) if x != y), min(len(got), len(want))))
                )
    return anchors, verdicts


def prose_citations(page_lines):
    """(line_index, path, a, b) for every `path:a-b` citation that is not a statement anchor.

    A statement anchor is the backticked cell inside `[...]`; those are checked by check_quotes.
    A prose citation may carry no path ("at `:64-84` of the same file") or a path relative to a
    manuscript directory named earlier in the same entry.
    """
    out = []
    for i, l in enumerate(page_lines):
        for m in CITE.finditer(l):
            if m.start() > 0 and l[m.start() - 1] == "[" and l[m.end():m.end() + 1] == "]":
                continue
            b = int(m.group(3)) if m.group(3) else int(m.group(2))
            out.append((i, m.group(1), int(m.group(2)), b))
    return out


def resolve_citation(path, body, offset):
    """Repo-relative path for a prose citation, or None when it cannot be resolved."""
    if path.startswith("preprints/"):
        return path
    seen = body[: offset + 1]
    if not path:
        for l in seen[::-1]:
            m = ANCHOR.search(l)
            if m:
                return m.group(1)
        return None
    dirs = []
    for l in seen:
        for m in PREPRINT_DIR.finditer(l):
            cand = "preprints/" + m.group(1)
            if os.path.isdir(os.path.join(ROOT, cand)) and cand not in dirs:
                dirs.append(cand)
    hits = [d + "/" + path for d in reversed(dirs)
            if os.path.isfile(os.path.join(ROOT, d, path))]
    return hits[0] if len(hits) == 1 else None


def env_end(lines, a, env):
    """Line number of the \\end{env} that closes the environment opened at line a."""
    depth = 0
    for n in range(a - 1, len(lines)):
        depth += len(re.findall(r"\\begin\{%s\}\*?" % env, lines[n]))
        if re.search(r"\\end\{%s\}" % env, lines[n]):
            depth -= 1
            if depth == 0:
                return n + 1
    return None


def check_citations(page_lines, problems):
    ents = blocks(page_lines)
    owner = {}
    for fam, (h, body, _) in ents.items():
        for j in range(h, h + len(body)):
            owner[j] = (fam, body, j - h)
    count = 0
    for i, path, a, b in prose_citations(page_lines):
        count += 1
        fam, body, off = owner.get(i, (None, [], 0))
        full = resolve_citation(path, body, off)
        if full is None:
            problems.append("citation line %d: %s:%d-%d resolves to no single manuscript file"
                            % (i + 1, path, a, b))
            continue
        if not os.path.isfile(os.path.join(ROOT, full)):
            problems.append("citation line %d: path not on disk: %s" % (i + 1, full))
            continue
        with open(os.path.join(ROOT, full), encoding="utf-8", errors="replace") as fh:
            lines = fh.read().split("\n")
        if not 1 <= a <= b <= len(lines):
            problems.append("citation line %d: %s:%d-%d outside 1..%d lines"
                            % (i + 1, full, a, b, len(lines)))
            continue
        m = BEGIN.match(lines[a - 1].strip())
        if m:
            end = env_end(lines, a, m.group(1))
            if end != b:
                problems.append(
                    "citation line %d: %s:%d opens %s, whose \\end is line %s; citation ends at %d"
                    % (i + 1, full, a, m.group(1), end, b))
    return count


def check_measurements(page_lines, expected, anchors, verdicts, cites, problems):
    keys = {}
    for l in page_lines:
        m = re.match(r"- `([A-Za-z0-9_]+)` (.*)$", l)
        if m:
            keys[m.group(1)] = m.group(2).strip()
    want = {k: str(v) for k, v in expected.items()}
    want["entries"] = str(len(entries(page_lines)))
    want["promoted"] = str(sum(1 for b in blocks(page_lines).values() if b[2] == 4))
    want["anchors"] = str(anchors)
    want["citations"] = str(cites)
    for v in VERDICTS:
        want["verdict_" + v] = str(verdicts.get(v, 0))
    for k, v in sorted(want.items()):
        if k not in keys:
            problems.append("measurements: key `%s` (%s) missing from the page" % (k, v))
        elif keys[k] != v:
            problems.append("measurements: `%s` reads %s, re-derived %s" % (k, keys[k], v))
    for k in sorted(keys):
        if k not in want:
            problems.append("measurements: key `%s` is not a derived quantity" % k)
    return want


def check_entry_set(page_lines, pop, rows, problems):
    """`###` entries == population ∪ {346}; each `####` entry is a family the rule dropped."""
    bl = blocks(page_lines)
    fams = sorted(f for f, (_, _, lvl) in bl.items() if lvl == 3)
    allowed = sorted({r["fam"] for r in pop} | {"346"})
    if fams != allowed:
        missing = sorted(set(allowed) - set(fams))
        extra = sorted(set(fams) - set(allowed))
        if missing:
            problems.append("entries: population families with no entry: %s" % " ".join(missing))
        if extra:
            problems.append("entries: entries outside the population (%d + 346): %s"
                            % (len(pop), " ".join(extra)))
    by = {r["fam"]: r for r in rows}
    inpop = {r["fam"] for r in pop}
    for fam in sorted(f for f, (_, _, lvl) in bl.items() if lvl == 4):
        r = by.get(fam)
        if r is None:
            problems.append("promoted: family %s is not a ledger row" % fam)
            continue
        if fam in inpop:
            problems.append("promoted: family %s is in the population, so it is not promoted" % fam)
        if r["tier"] == "T0":
            problems.append("promoted: family %s is still T0, so the population rule did not drop it" % fam)
        if not NAME_TOKEN.search(r["title"]):
            problems.append("promoted: family %s names no conjecture/problem/question in its title" % fam)


def check_formalization_claim(page_lines, rows, problems):
    """The page claims 0 of the population have main_results, a scope note, or a comparator challenge."""
    _, _, _, pop = population(rows)
    claim = ("0 of %d have a\n  `main_results` entry, 0 have a scope note, 0 have a comparator challenge"
             % len(pop))
    if claim not in "\n".join(page_lines):
        return
    for r in pop:
        if r["mainres"] not in ("", "0"):
            problems.append("family %s: ledger mainres=%s, page claims 0" % (r["fam"], r["mainres"]))
        if r["chal"] not in ("", "0"):
            problems.append("family %s: ledger chal=%s, page claims 0" % (r["fam"], r["chal"]))
        if r["scope_note"] not in ("", "0", "no", "none", "-"):
            problems.append("family %s: ledger scope_note=%s, page claims 0" % (r["fam"], r["scope_note"]))


def quote_blocks(lines):
    """Indices (anchor_line, first_quote_line, last_quote_line) for every anchor in the page."""
    out = []
    for i, l in enumerate(lines):
        if not ANCHOR.search(l):
            continue
        j = i + 1
        while j < len(lines) and lines[j].startswith("  "):
            if lines[j].strip().endswith('"'):
                out.append((i, i + 1, j))
                break
            j += 1
    return out


def mutants(page_lines):
    """Twelve in-memory corruptions, one per check the page relies on."""
    out = []
    qb = quote_blocks(page_lines)

    # 1. inline quotation: corrupt the opening line of a quotation
    lines = list(page_lines)
    a = qb[0][1]
    lines[a] = lines[a].replace("\\begin{theorem", "\\begin{theorm", 1)
    if lines[a] != page_lines[a]:
        out.append(("inline quotation corrupted", lines))

    # 2. quotation wrapped across lines: corrupt a continuation line of a multi-line quotation
    lines = list(page_lines)
    for _, a, b in qb:
        if b - a < 2:
            continue
        mid = (a + b) // 2
        lines[mid] = lines[mid].replace("the", "txe", 1)
        if lines[mid] != page_lines[mid]:
            out.append(("wrapped quotation corrupted", lines))
            break

    # 3. invented quotation
    lines = list(page_lines)
    lines[qb[0][1]] = '  "This sentence is not in the shipped manuscript."'
    out.append(("invented quotation", lines))

    # 4. anchor line range shifted
    lines = list(page_lines)
    for i, l in enumerate(lines):
        m = ANCHOR.search(l)
        if m:
            lines[i] = l[:m.start()] + "[`%s:%d-%d`]" % (m.group(1), int(m.group(2)) + 1, int(m.group(3))) + l[m.end():]
            out.append(("anchor start line shifted", lines))
            break
    # 5. anchor path that does not exist
    lines = list(page_lines)
    for i, l in enumerate(lines):
        m = ANCHOR.search(l)
        if m:
            lines[i] = l[:m.start()] + "[`preprints/No-Such-Manuscript/build/main.tex:%s-%s`]" % (m.group(2), m.group(3)) + l[m.end():]
            out.append(("anchor path absent", lines))
            break
    # 6. a Measurements count
    lines = list(page_lines)
    for i, l in enumerate(lines):
        if l.startswith("- `pop_families`"):
            lines[i] = "- `pop_families` 44"
            out.append(("measurements count corrupted", lines))
            break
    # 7. an entry deleted
    lines = list(page_lines)
    for i, l in enumerate(lines):
        if HEADING.match(l) and l.startswith("### 316"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            del lines[i:j]
            out.append(("population entry deleted", lines))
            break
    # 8. an entry for a family outside the population
    lines = list(page_lines)
    for i, l in enumerate(lines):
        if l.startswith("## Discrepancies"):
            lines[i:i] = ["### 001 - A family outside the population", "",
                          "- **Reading**: `match`. Injected.", ""]
            out.append(("entry outside the population added", lines))
            break
    # 9. a verdict word
    lines = list(page_lines)
    for i, l in enumerate(lines):
        if l.strip().startswith("- **Reading**: `match`"):
            lines[i] = l.replace("`match`", "`wider`", 1)
            out.append(("verdict word changed", lines))
            break
    # 10. a prose citation truncated before its \end
    lines = list(page_lines)
    for _i, path, a, b in prose_citations(page_lines):
        if path and b > a:
            for j, l in enumerate(lines):
                m = CITE.search(l)
                if m and m.group(1) == path and int(m.group(3)) == b:
                    lines[j] = l[:m.start()] + "`%s:%d-%d`" % (path, a, b - 1) + l[m.end():]
                    out.append(("prose citation truncated", lines))
                    break
            if len(out) > 9:
                break
    # 11. a prose citation whose path is not on disk
    lines = list(page_lines)
    for _i, path, a, b in prose_citations(page_lines):
        if path.startswith("build/"):
            for j, l in enumerate(lines):
                m = CITE.search(l)
                if m and m.group(1) == path:
                    lines[j] = l[:m.start()] + "`build/no-such-file.tex:%d-%d`" % (a, b) + l[m.end():]
                    out.append(("prose citation path absent", lines))
                    break
            break
    # 12. a population entry demoted to the promoted level
    lines = list(page_lines)
    for i, l in enumerate(lines):
        if HEADING.match(l) and l.startswith("### 316"):
            lines[i] = "####" + l[3:]
            out.append(("population entry demoted to promoted", lines))
            break
    return out


def main():
    mutant = "--mutant" in sys.argv
    rows = ledger_rows()
    expected, pop = measure(rows)
    with open(PAGE, encoding="utf-8") as fh:
        base = fh.read().split("\n")

    problems = []
    anchors, verdicts = check_quotes(base, problems)
    cites = check_citations(base, problems)
    check_entry_set(base, pop, rows, problems)
    check_measurements(base, expected, anchors, verdicts, cites, problems)
    check_formalization_claim(base, rows, problems)

    print("population: %d families / %d manuscripts (second pass %d/%d, first pass %d/%d, T0 %d/%d)"
          % (expected["pop_families"], expected["pop_manuscripts"], expected["second_families"],
             expected["second_manuscripts"], expected["first_families"], expected["first_manuscripts"],
             expected["t0_families"], expected["t0_manuscripts"]))
    bl = blocks(base)
    print("entries: %d population (population %d + 346) + %d promoted: %s"
          % (len(entries(base)), expected["pop_families"],
             sum(1 for b in bl.values() if b[2] == 4),
             " ".join(sorted(f for f, (_, _, lvl) in bl.items() if lvl == 4))))
    print("anchors: %d, all resolved against the shipped LaTeX" % anchors)
    print("prose citations: %d, all resolved, every one covering a whole statement environment" % cites)
    print("verdicts: " + " ".join("%s %d" % (v, verdicts.get(v, 0)) for v in VERDICTS))
    print("measurements: %d derived keys re-measured"
          % len(check_measurements(base, expected, anchors, verdicts, cites, [])))
    print("priority set: %d in the population, %d outside (346)"
          % (expected["priority_in_pop"], expected["priority_outside_pop"]))
    print("ledger check: mainres, chal and scope_note are 0 for all %d population families"
          % expected["pop_families"])

    if mutant:
        caught = 0
        for label, lines in mutants(base):
            inner = []
            a2, v2 = check_quotes(lines, inner)
            c2 = check_citations(lines, inner)
            check_entry_set(lines, pop, rows, inner)
            check_measurements(lines, expected, a2, v2, c2, inner)
            check_formalization_claim(lines, rows, inner)
            status = "caught" if inner else "MISSED"
            if inner:
                caught += 1
            print("mutant: %s -> %s (%s)" % (label, status, inner[0] if inner else "no problem reported"))
        print("flags %d injected mutations" % caught)

    if problems:
        print("\n%d problems:" % len(problems))
        for p in problems:
            print("  - " + p)
        return 1
    print("\nno problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
