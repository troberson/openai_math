#!/usr/bin/env python3
"""Cross-check the counterexample-shaped families outside T0 against main_results; report-only.

Population rule: `counterexample` in the ledger's `shapes` column AND tier != T0 — 28 families,
19 at T3 and 9 at T2. The T0 counterexample-shaped families are read in notes/t0-triage.md, so
this report covers the rest. For each family it prints the abstract sentence that carries the
counterexample language, the comparator configs its scope note links, the main_results entry each
config carries, and the Lean statement that entry's declaration opens with — every line numbered
so notes/counterexample-crosscheck.md can cite it.

Run it twice and diff: the report must be identical. It writes nothing and runs nothing; Lean
files are read as text, per the repo rule that lake, lean, and comparator are never invoked.

A declaration is a source-level claim: formalization.yaml states scope "Partial progress.",
automation methods [agent], review status unchecked. Nothing here says a comparator was run.
"""
import collections
import re

import build_catalog
import extract_subfinding_pairs as ep

from catlib import ledger as L
from catlib import yaml as Y
from catlib.paths import (
    COMPARATOR_DIR as CHALLENGES,
    DOCS_DIR as DOCS,
    LEAN as LEAN_ROOT,
)

ROOT = build_catalog.ROOT


def main_results():
    """config stem -> (declaration, file, yaml file-line), from the package's yaml reader.

    Measured equivalent to the rule this file used to carry: 200 entries, 189 distinct configs,
    and every (declaration, file, file-line) triple identical. The yaml anchor the report prints
    is the entry's `file:` line; a 3-line entry block starts two lines above it.
    """
    ents = Y.main_results_entries()

    def stem(e):
        return e["config"].split("/")[-1].removesuffix(".json")

    return ({stem(e): (e["declaration"], e["file"], e["file_line"]) for e in ents},
            [stem(e) for e in ents])


def scope_note(fam):
    """(path, [(line, config)]) for the family's scope note; ([] when the doc is absent)."""
    p = DOCS / f"{fam}.md"
    if not p.is_file():
        return p, []
    hits = []
    for n, ln in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        hits += [(n, c) for c in re.findall(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean", ln)]
    return p, hits


def counterex_sentences(abstract):
    """Abstract sentences carrying the counterexample phrase, verbatim."""
    return [s for s in re.split(r"(?<=[.!?])\s+", abstract)
            if build_catalog.COUNTEREX_PHRASE.search(s.lower())]


def declaration_statement(decl, rel):
    """(line, signature lines) where a declaration's statement opens in its file."""
    p = LEAN_ROOT / rel
    if not p.is_file():
        return None, []
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    tail = decl.split(".")[-1]
    for i, ln in enumerate(lines, start=1):
        if re.match(rf"^\s*(theorem|lemma|proposition|corollary|def|example)\s+{re.escape(tail)}\b", ln):
            block = [ln.strip()]
            j = i
            while len(block) < 12 and j < len(lines) and not block[-1].rstrip().endswith(":="):
                nxt = lines[j].strip()
                if not nxt:
                    break
                block.append(nxt)
                j += 1
            return i, block
    return None, []


CARRIER_DEF = re.compile(
    r"^\s*(?:private\s+|protected\s+)?(?:def|abbrev|structure)\s+([A-Za-z0-9_.]+)\s*:\s*(?:Prop\s*)?[:=]")
IMPORT = re.compile(r"^\s*import\s+(OAI[\w.]*)\s*$")


def import_closure(rel, cap=400):
    """Files a Lean file can see: itself, then its imports breadth-first, then theirs.

    A carrier named in a statement resolves through imports, not through the directory layout:
    OAI/Analysis/Kaplansky/Main.lean names MainTarget, which is defined in the imported
    OAI/Analysis/Cuntz/Quasitrace.lean, outside Kaplansky/'s own tree. Bounded so a walk over the
    122,458-file tree cannot run away.
    """
    seen, order, queue = set(), [], [rel]
    while queue and len(order) < cap:
        r = queue.pop(0)
        p = LEAN_ROOT / r
        if not p.is_file() or r in seen:
            continue
        seen.add(r)
        order.append(r)
        for ln in p.read_text(encoding="utf-8", errors="replace").splitlines():
            m = IMPORT.match(ln)
            if m:
                queue.append("/".join(m.group(1).split(".")) + ".lean")
    return order


def carrier(name, rel):
    """(file, line, body) for the Prop carrier a statement's type names.

    A statement written `theorem main : MainStatement :=` says nothing about its content until the
    carrier is opened, so the body is quoted beside it. Searched over the declaration file's import
    closure, nearest first; the body is the indented run of lines under the definition.
    """
    for r in import_closure(rel):
        p = LEAN_ROOT / r
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, ln in enumerate(lines, start=1):
            m = CARRIER_DEF.match(ln)
            if not m or m.group(1).split(".")[-1] != name:
                continue
            body = [ln.strip()]
            for nxt in lines[i:]:
                if not nxt.strip() or not nxt.startswith((" ", "\t")):
                    break
                body.append(nxt.strip())
            return p.relative_to(LEAN_ROOT), i, body
    return None, None, []


def main():
    rows = L.ledger_by_fam()
    order, fams = build_catalog.parse_overview()
    entry_lines = ep.resultentry_lines()
    shape = [f for f in order if "counterexample" in build_catalog.shapes_of(fams[f]["abstract"])]
    pop = [f for f in shape if rows[f]["tier"] != "T0"]
    tiers = collections.Counter(rows[f]["tier"] for f in pop)
    with_main = [f for f in pop if int(rows[f]["mainres"]) > 0]
    without = [f for f in pop if int(rows[f]["mainres"]) == 0]

    print("== population")
    print(f"counterexample shape {len(shape)}  outside T0 {len(pop)}  "
          + "  ".join(f"{t} {c}" for t, c in sorted(tiers.items()))
          + f"  T0 shape {len(shape) - len(pop)}")
    print(f"ledger mainres sum {sum(int(rows[f]['mainres']) for f in pop)}  "
          f"ledger chal sum {sum(int(rows[f]['chal']) for f in pop)}  "
          f"ledger paps_form sum {sum(int(rows[f]['paps_form']) for f in pop)}  "
          f"ledger paps sum {sum(int(rows[f]['paps']) for f in pop)}")
    print(f"families with a main_results entry {len(with_main)}  with none {len(without)}  "
          f"no-mainres tiers {dict(collections.Counter(rows[f]['tier'] for f in without))}")

    mr, entries = main_results()
    print(f"main_results entries {len(entries)}  unique configs {len(set(entries))}")

    print("== per family")
    resolved, notfound = 0, []
    carriers, carrier_missing = 0, []
    for f in pop:
        info, r = fams[f], rows[f]
        doc, links = scope_note(f)
        print(f"\nfam {f}  tier {r['tier']}  {info['title']}")
        print(f"   overview.tex:{entry_lines[f]}  scope note "
              f"{doc.relative_to(ROOT) if doc.is_file() else 'ABSENT'}  "
              f"mainres {r['mainres']}  chal {r['chal']}  paps {r['paps']}  paps_form {r['paps_form']}")
        for n, c in links:
            print(f"      link {doc.name}:{n} {c}")
        for n, s in enumerate(counterex_sentences(info["abstract"]), start=1):
            print(f"      claim {n} {s}")
        for c in sorted({c for _, c in links}):
            ent = mr.get(c)
            if ent is None:
                print(f"      config {c}: no main_results entry")
                continue
            decl, rel, yline = ent
            at, block = declaration_statement(decl, rel)
            resolved += 1
            print(f"      config {c}: yaml:{yline} declaration {decl} file {rel}")
            if at is None:
                notfound.append((f, c, decl, rel))
                print(f"         statement NOT FOUND in {rel}")
                continue
            print(f"         statement {rel}:{at}")
            for ln in block:
                print(f"           {ln}")
            t = re.search(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=", " ".join(block))
            if not t:
                continue
            cname = t.group(1).split(".{")[0].split(".")[-1]
            carriers += 1
            cfile, cline, cbody = carrier(cname, rel)
            if cfile is None:
                carrier_missing.append((f, c, cname))
                print(f"         carrier {cname}: definition NOT FOUND")
                continue
            print(f"         carrier {cname} = {cfile}:{cline}")
            for ln in cbody:
                print(f"           {ln}")

    print(f"\ndeclarations resolved {resolved}  statements not found {len(notfound)} {notfound}")
    print(f"carrier-typed statements {carriers}  carriers resolved "
          f"{carriers - len(carrier_missing)}  carrier definitions not found "
          f"{len(carrier_missing)} {carrier_missing}")

    print("== challenge stubs behind the population")
    stubs, files = 0, set()
    for f in pop:
        for _, c in scope_note(f)[1]:
            lp = CHALLENGES / f"{c}.lean"
            if lp.is_file():
                stubs += lp.read_text(encoding="utf-8", errors="replace").count("sorry")
                files.add(c)
    print(f"linked stubs {len(files)}  sorry occurrences {stubs}")


if __name__ == "__main__":
    main()
