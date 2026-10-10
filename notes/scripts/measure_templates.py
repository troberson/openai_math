#!/usr/bin/env python3
"""Report-only: measure notes/templates/ — every count notes/templates.md quotes.

Writes nothing, and reads only template text plus the writer's registry. Two trees:
notes/templates/report/*.j2 render the report pages under notes/ through render_reports.py;
notes/templates/*.j2 render the page types under notes/index/ through build_index.py.

Slot rule: a slot is a "{{ " occurrence counted over the WHOLE template file. Each report template
carries a generated header comment whose closing line holds one literal "{{ }}", so the header
contributes exactly 1 to every report template's count; the index templates have no header. Slot
expressions are NOT required to be unique: over the 21 committed templates the measured gap between
"{{ ... }}" expressions and distinct expressions is 10, in 3 templates. The builder's report line
prints a label count (len of the writer's phrases dict), which is a different measure from the
"{{ " occurrences in the file it wrote. Quote a slot count with the rule that yields it.

Run: python3 notes/scripts/measure_templates.py
"""
from __future__ import annotations

import pathlib
import re
import sys
from typing import Any

from catlib import paths as P

TEMPLATES = P.NOTES / "templates"
REPORT_DIR = TEMPLATES / "report"
SLOT = "{{ "
EXPR = re.compile(r"\{\{[^}]*\}\}")
INDEX_TREE = {"discipline.md.j2": "disciplines", "name.md.j2": "names", "topic.md.j2": "topics"}
NON_FAMILY_DIRS = {"disciplines", "names", "topics", "edges"}


def registry() -> Any:
    """The builder module, imported inside the call.

    render_reports.py imports this module to measure the census, and build_report_templates.py
    imports the writer at module level and reads its slot dicts while its own module body runs, so
    a module-level import here closes the cycle at import time: importing render_reports first would
    build the builder's POPULATIONS dict against a half-initialised writer. Same deferred shape as
    catlib/render.py's rendered(); notes/linting.md lists the cycles.
    """
    import build_report_templates
    return build_report_templates


def template_rows(directory: pathlib.Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for t in sorted(directory.glob("*.j2")):
        text = t.read_text(encoding="utf-8")
        exprs = EXPR.findall(text)
        out.append({"name": t.name, "lines": len(text.splitlines()),
                    "bytes": len(text.encode()), "slots": text.count(SLOT),
                    "exprs": len(exprs), "distinct": len(set(exprs))})
    return out


def index_renders() -> dict[str, int]:
    counts = {name: len(list((P.INDEX_DIR / sub).rglob("*.md")))
              for name, sub in INDEX_TREE.items()}
    fam_dirs = [d for d in P.INDEX_DIR.iterdir() if d.is_dir() and d.name not in NON_FAMILY_DIRS]
    counts["family.md.j2"] = sum(len(list(d.rglob("*.md"))) for d in fam_dirs)
    counts["family.md.j2 dirs"] = len(fam_dirs)
    counts["index-readme.md.j2"] = int((P.INDEX_DIR / "README.md").is_file())
    return counts


def coverage() -> dict[str, tuple[str, int]]:
    """page -> (checker, needles the builder can derive from that checker's source)."""
    b = registry()
    return {page: (checker, len(b.checker_needles(P.SCRIPTS / checker)))
            for page, checker in sorted(b.ALL_PAGES.items())}


def registry_gap() -> tuple[list[str], list[str]]:
    """(templates named by the registry with no file on disk, files on disk with no registry entry)."""
    b = registry()
    pages = {pathlib.Path(page).name for page in b.ALL_PAGES}
    templates = {t.name for t in REPORT_DIR.glob("*.j2")}
    missing = sorted(f"{name}.j2" for name in pages if f"{name}.j2" not in templates)
    extra = sorted(t for t in templates if t[: -len(".j2")] not in pages)
    return missing, extra


def header_comment_lines(text: str) -> int:
    """Lines through the closing '#}' of the generated header comment; 0 when the file has none."""
    for i, line in enumerate(text.splitlines(), start=1):
        if "#}" in line:
            return i
    return 0


def all_pages_anchor() -> int:
    """Line in build_report_templates.py where the page<->template registry opens."""
    src = pathlib.Path(registry().__file__).read_text(encoding="utf-8")
    for i, line in enumerate(src.splitlines(), start=1):
        if line.startswith("ALL_PAGES"):
            return i
    return 0


def tree_totals(rows_list: list[dict[str, Any]]) -> dict[str, int]:
    return {"n": len(rows_list), "lines": sum(int(r["lines"]) for r in rows_list),
            "bytes": sum(int(r["bytes"]) for r in rows_list),
            "slots": sum(int(r["slots"]) for r in rows_list),
            "exprs": sum(int(r["exprs"]) for r in rows_list),
            "distinct": sum(int(r["distinct"]) for r in rows_list)}


def population() -> dict[str, Any]:
    """Every measured value notes/templates.md quotes, from the template files and the registry."""
    b = registry()
    rep = template_rows(REPORT_DIR)
    idx = template_rows(TEMPLATES)
    cov = coverage()
    missing, extra = registry_gap()
    renders = index_renders()
    for r in rep:
        page = f"notes/{r['name'][: -len('.j2')]}"
        checker, needles = cov.get(page, ("-", 0))
        r["page"] = page
        r["checker"] = checker
        r["needles"] = needles
    for r in idx:
        r["renders"] = renders.get(r["name"], 0)
    rt, it = tree_totals(rep), tree_totals(idx)
    reuse_rows = [r for r in rep + idx if int(r["exprs"]) > int(r["distinct"])]
    headers = {header_comment_lines(t.read_text(encoding="utf-8"))
               for t in list(REPORT_DIR.glob("*.j2")) + list(TEMPLATES.glob("*.j2"))}
    derived = [p for p, (_c, n) in cov.items() if n]
    return {
        "report_rows": rep,
        "index_rows": idx,
        "report": rt,
        "index": it,
        "all": {"n": rt["n"] + it["n"], "lines": rt["lines"] + it["lines"],
                "bytes": rt["bytes"] + it["bytes"], "slots": rt["slots"] + it["slots"]},
        "reuse": rt["exprs"] + it["exprs"] - rt["distinct"] - it["distinct"],
        "reuse_templates": len(reuse_rows),
        "reuse_detail": "; ".join(
            f"`{r['name']}` ({int(r['exprs']) - int(r['distinct'])} repeat"
            f"{'s' if int(r['exprs']) - int(r['distinct']) > 1 else ''})"
            for r in reuse_rows),
        "header_lines": max(headers),
        "index_header_lines": min(headers),
        "coverage": cov,
        "derived": derived,
        "derived_n": len(derived),
        "not_derived_n": len(cov) - len(derived),
        "registry_n": len(b.ALL_PAGES),
        "all_pages_anchor": all_pages_anchor(),
        "missing": missing,
        "extra": extra,
        "renders": renders,
    }


def report(p: dict[str, Any]) -> None:
    for r in p["report_rows"]:
        print(f"report  {r['name']}  lines {r['lines']}  bytes {r['bytes']}  slots {r['slots']}"
              f"  checker {r['checker']}  needles {r['needles'] or 'NOT DERIVED'}")
    for r in p["index_rows"]:
        print(f"index   {r['name']}  lines {r['lines']}  bytes {r['bytes']}  slots {r['slots']}"
              f"  renders {r['renders']}")
    rt, it, al = p["report"], p["index"], p["all"]
    print(f"report tree  templates {rt['n']}  lines {rt['lines']}  bytes {rt['bytes']}"
          f"  slots {rt['slots']}")
    print(f"index tree   templates {it['n']}  lines {it['lines']}  bytes {it['bytes']}"
          f"  slots {it['slots']}")
    print(f"all          templates {al['n']}  lines {al['lines']}  bytes {al['bytes']}"
          f"  slots {al['slots']}")
    print(f"slot reuse (exprs - distinct) {p['reuse']} in {p['reuse_templates']} templates"
          f"  header comment lines report {p['header_lines']} index {p['index_header_lines']}")
    print(f"needles derived {p['derived_n']} of {p['registry_n']}: {' '.join(p['derived']) or '-'}")
    print(f"registry  ALL_PAGES {p['registry_n']} at build_report_templates.py:{p['all_pages_anchor']}"
          f"  template-without-page {len(p['missing'])}"
          f"  page-without-template {len(p['extra'])}  {' '.join(p['missing'] + p['extra'])}")
    r = p["renders"]
    print(f"index pages on disk  families {r['family.md.j2']}  disciplines {r['discipline.md.j2']}"
          f"  topics {r['topic.md.j2']}  names {r['name.md.j2']}  readme {r['index-readme.md.j2']}")


def main() -> int:
    report(population())
    return 0


if __name__ == "__main__":
    sys.exit(main())
