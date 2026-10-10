#!/usr/bin/env python3
r"""Build a report template from a committed page and the slot dict its writer supplies.

Writer: notes/templates/report/<page>.j2. It rewrites `git show HEAD:<page>` by replacing every
phrase the writer can produce with a `{{ p['<label>'] }}` slot, so the template's literal text -
quotations, anchors, fenced blocks, numbers the writer does not compute - is byte-exact by
construction, and the slot labels and phrase strings come from the writer's own code, not from a
transcription.

The slot set is the writer's, because the writer's slot dict *is* the template's slot set:
render_reports.py builds one dict per page (`phrases`, `abstracts_phrases`, `named_results_phrases`,
`index_phrases`) and passes it to the template as `p`, and its split tables (`NR_SPLIT`,
`INDEX_SPLIT`) are what give the " a"/" b" labels. A template built from any other list - e.g. the
checker's needle list, which is wider - renders slots the writer never supplies, and Jinja renders an
unknown key as the empty string: the page silently loses text. The page's checker needles are read
too, and reported as coverage (slotted / left literal), never as the slot source.

Each phrase is located with a whitespace-flexible regex over the WHOLE page (the page wraps phrases
across lines), all matches collected, sorted, and rejected on overlap, then replaced from the end so
offsets stay valid. A phrase the page wraps is split at the page's OWN line breaks, keeping each
break's exact whitespace run as the separator so the rendered page wraps identically; split labels
get " a", " b", ... suffixes. render_reports.py keeps the matching prefix table and raises if a
prefix stops matching the measured phrase, so a drifted number fails the render instead of reflowing
the page.

Literal runs are wrapped in `{% raw %}` / `{% endraw %}` when they carry LaTeX. The pages quote
`\newtheorem` and `\char` blocks verbatim; unescaped, a `{` in such a line is a Jinja expression
start and the template fails to compile (`unexpected char '\\'`). Wrapping is safe: with
`trim_blocks` a tag on its own line emits nothing, so the wrapped lines render byte-identically.

Run it from a clean checkout of the page it rebuilds: it reads HEAD, not the working tree. Proof
after any rebuild is the render - `python3 notes/scripts/render_reports.py` twice, pages
byte-identical to HEAD. Prints the label -> phrase-part dict the writer supplies. Touches no page.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys
from collections.abc import Callable
from typing import Any

import render_reports as R

ROOT = pathlib.Path(__file__).resolve().parents[2]
TPL_DIR = ROOT / "notes" / "templates" / "report"
WS_RUN = re.compile(r"[ \t]*\n[ \t]*")
SPLIT_LABEL = re.compile(r"^(.* [a-j])$")

# The measured population per page, taken from the same call render_reports.py makes when it renders.
# The writer's slot dict is built from it, and the page's checker is handed the same object so its
# needle list is derived, not transcribed.
POPULATIONS: dict[str, Callable[[], Any]] = {
    "notes/sources.md": R.measure,
    "notes/abstracts.md": R.CA.measure,
    "notes/named-results.md": R.en.population,
    "notes/index-design.md": R.M.population,
    "notes/names.md": R.names_population,
    "notes/proof-density.md": R.proof_density_population,
    "notes/index-links.md": R.index_links_population,
    "notes/links.md": R.links_population,
    "notes/dependency-drift.md": R.drift_population,
}
# The writer's own slot dict per page. These are the calls render_reports.py makes when it renders,
# so the labels and phrase strings the template gets are the writer's by construction.
LABELS: dict[str, Callable[[], dict[str, str]]] = {
    "notes/sources.md": lambda: R.phrases(POPULATIONS["notes/sources.md"]()),
    "notes/abstracts.md": lambda: R.abstracts_phrases(POPULATIONS["notes/abstracts.md"]()),
    "notes/named-results.md": lambda: R.named_results_phrases(POPULATIONS["notes/named-results.md"]()),
    "notes/index-design.md": lambda: R.index_phrases(POPULATIONS["notes/index-design.md"]()),
    "notes/names.md": lambda: R.names_phrases(POPULATIONS["notes/names.md"]()),
    "notes/proof-density.md": lambda: R.proof_density_phrases(POPULATIONS["notes/proof-density.md"]()),
    "notes/index-links.md": lambda: R.index_links_phrases(POPULATIONS["notes/index-links.md"]()),
    "notes/links.md": lambda: R.links_phrases(POPULATIONS["notes/links.md"]()),
    "notes/dependency-drift.md": lambda: R.drift_phrases(POPULATIONS["notes/dependency-drift.md"]()),
}
PHRASE_FNS = ("count_phrases", "size_phrases")
ALL_PAGES = {
    "notes/abstracts.md": "verify_abstracts.py",
    "notes/index-links.md": "check_index_links.py",
    "notes/index-design.md": "verify_index_design.py",
    # links.md has no page checker: its counts come from the gated writer extract_links.py, which
    # prints its report and writes notes/links.tsv and carries no count_phrases/size_phrases, so
    # the builder reports this coverage as NOT DERIVED.
    "notes/links.md": "extract_links.py",
    # dependency-drift.md's checker takes no count_phrases/size_phrases: its needles are inline
    # want() calls inside check(), so the builder reports this coverage as NOT DERIVED.
    "notes/dependency-drift.md": "verify_dependency_drift.py",
    "notes/named-results.md": "verify_named_results.py",
    "notes/names.md": "measure_names.py",
    "notes/proof-density.md": "measure_proof_density.py",
    "notes/sources.md": "verify_sources.py",
}


def checker_needles(checker: pathlib.Path) -> list[tuple[str, str]]:
    """The page checker's (phrase, label) needles - read for the coverage report, never as slots.

    The checker source is exec'd with the trailing bare `main()` call removed when the module has no
    `if __name__` guard (verify_index_design.py and verify_sources.py run their page check on
    import, which raises SystemExit).
    """
    src = checker.read_text(encoding="utf-8")
    if 'if __name__ == "__main__"' not in src:
        src = src[: src.rindex("\nmain()")]
    ns: dict[str, Any] = {"__name__": "checker_source", "__file__": str(checker)}
    # The needles come from the checker's own source, so the module is loaded by exec.
    exec(compile(src, checker.name, "exec"), ns)  # pylint: disable=exec-used
    out: list[tuple[str, str]] = []
    for fn_name in PHRASE_FNS:
        fn = ns.get(fn_name)
        if callable(fn):
            pop = ns.get("population")
            try:
                out.extend(fn(pop()) if callable(pop) else fn({}))
            except (TypeError, KeyError):
                continue
    return out


def committed_page(page_rel: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{page_rel}"],
                          capture_output=True, text=True, check=True).stdout


def flex(phrase: str) -> re.Pattern[str]:
    """Regex for a phrase whose spaces may be any whitespace run, because the page wraps."""
    return re.compile(r"\s+".join(re.escape(t) for t in phrase.split(" ")))


def split_parts(matched: str, phrase: str) -> tuple[list[str], list[str]]:
    """Split the matched span at the page's line breaks, keeping each break's exact whitespace."""
    runs = list(WS_RUN.finditer(matched))
    if not runs:
        return [matched], [" "]
    parts: list[str] = []
    seps: list[str] = []
    pos = 0
    for r in runs:
        parts.append(matched[pos:r.start()].rstrip(" \t"))
        seps.append(r.group(0))
        pos = r.end()
    parts.append(matched[pos:].lstrip(" \t"))
    if " ".join(parts) != phrase:
        print(f"SPLIT MISMATCH for {phrase!r}\n  parts: {parts}")
        sys.exit(1)
    return parts, seps


def group_labels(labels: dict[str, str]) -> dict[str, list[tuple[str, str]]]:
    """{base label: [(slot label, phrase part), ...]} in the writer's a/b/c order."""
    groups: dict[str, list[tuple[str, str]]] = {}
    for lab, val in labels.items():
        m = SPLIT_LABEL.match(lab)
        base = lab[:-2] if m else lab
        groups.setdefault(base, []).append((lab, val))
    for parts in groups.values():
        parts.sort()
    return groups


def raw_wrap(text: str) -> str:
    """Wrap literal runs that carry LaTeX in a raw block so the template compiles.

    The opening tag is glued to the run's FIRST line — `{% raw %}<line>` — not put on its own line.
    Jinja captures a raw block's body verbatim, `trim_blocks` included, so a tag on its own line emits
    the newline that follows it (a plain `{% raw %}` gains a blank line), and the whitespace-control
    form `{%- raw %}` strips ALL preceding whitespace, which deletes the blank line of a
    "heading, blank, LaTeX paragraph" sequence. Glued, the tag consumes nothing: the newline before it
    is literal text, no newline follows the tag, and `trim_blocks` consumes only the newline after
    `{% endraw %}`. The run then renders byte-identically.
    """
    out: list[str] = []
    run: list[str] = []

    def flush() -> None:
        if run:
            out.append("{% raw %}" + run[0])
            out.extend(run[1:])
            out.append("{% endraw %}")
            run.clear()

    for line in text.split("\n"):
        # Only the markers THIS builder emits are Jinja constructs. A literal page line can carry `{{`
        # or `{%` as LaTeX — sources.md quotes `\item{{{\ttfamily\char`\\documentclass}` and
        # `\def\extractclass#1#2@{%`, and flushing on those leaves the line unescaped, so the template
        # fails to compile with "unexpected char '\\'".
        if ("{{ p['" in line or line.startswith(("{% raw %}", "{% endraw %}", "{#"))):
            flush()
            out.append(line)
        elif "\\" in line or "{" in line or "}" in line:
            run.append(line)
        else:
            flush()
            out.append(line)
    flush()
    return "\n".join(out)


def build(page_rel: str, checker_name: str) -> int:
    label_fn = LABELS.get(page_rel)
    if label_fn is None:
        print(f"no writer slot dict recorded for {page_rel}")
        return 1
    labels = label_fn()
    groups = group_labels(labels)

    text = committed_page(page_rel)
    hits: list[tuple[int, int, str, list[tuple[str, str]]]] = []
    for base, parts in groups.items():
        needle = " ".join(v for _, v in parts)
        found = list(flex(needle).finditer(text))
        if not found:
            print(f"NOT FOUND ({base}): {needle!r}")
            return 1
        hits.extend((m.start(), m.end(), base, parts) for m in found)
    hits.sort()
    kept: list[tuple[int, int, str, list[tuple[str, str]]]] = []
    for h in hits:
        if kept and h[0] < kept[-1][1]:
            # A label whose phrase is a substring of another label's phrase is already slotted by the
            # wider span; only a partial overlap is a real conflict.
            if h[1] <= kept[-1][1]:
                print(f"covered by {kept[-1][2]!r}: {h[2]!r} [{h[0]}:{h[1]}]")
                continue
            print(f"OVERLAP: {kept[-1][2]!r} [{kept[-1][0]}:{kept[-1][1]}] vs {h[2]!r} [{h[0]}:{h[1]}]")
            return 1
        kept.append(h)
    hits = kept

    slots: dict[str, str] = {}
    nslots = 0
    wrapped: list[str] = []
    for start, end, base, parts in reversed(hits):
        matched = text[start:end]
        if len(parts) == 1:
            if "\n" in matched:
                # The writer supplies this phrase as ONE single-line string. Slotting it would drop the
                # page's own line break and reflow the paragraph, so the span stays literal — the
                # template's literal text is byte-exact from the committed page. A phrase the page wraps
                # is slotted only when the writer supplies it as split labels (" a"/" b"), which carry
                # the break as the separator.
                wrapped.append(base)
                continue
            lab, val = parts[0]
            slots[lab] = val
            rendered = "{{ p['" + lab + "'] }}"
            nslots += 1
        else:
            split, seps = split_parts(matched, " ".join(v for _, v in parts))
            if len(split) != len(parts):
                print(f"WRAP MISMATCH ({base}): page splits into {len(split)}, writer has {len(parts)}")
                return 1
            exprs = []
            for (lab, _), part in zip(parts, split, strict=True):
                slots[lab] = part
                exprs.append("{{ p['" + lab + "'] }}")
            rendered = exprs[0]
            for i in range(1, len(exprs)):
                rendered += seps[i - 1] + exprs[i]
            nslots += len(split)
        text = text[:start] + rendered + text[end:]

    text = raw_wrap(text)
    out = TPL_DIR / (pathlib.Path(page_rel).name + ".j2")
    TPL_DIR.mkdir(parents=True, exist_ok=True)
    header = (f"{{# {pathlib.Path(page_rel).name} - generated by notes/scripts/build_report_templates.py\n"
              f"   from git show HEAD:{page_rel} and the slot dict in notes/scripts/render_reports.py.\n"
              f"   Literal text is byte-exact from the committed page; every {{{{ }}}} slot is a label the\n"
              f"   writer supplies. Proof after a rebuild: render_reports.py twice, page byte-identical. #}}\n")
    out.write_text(header + text, encoding="utf-8")
    total = text.count("{{ ")
    needles = checker_needles(ROOT / "notes" / "scripts" / checker_name)
    print(f"template written: {out.relative_to(ROOT)}")
    print(f"labels {len(labels)} groups {len(groups)} hits {len(hits)} slots {nslots} exprs {total}")
    print(f"template lines {len((header + text).splitlines())} bytes {len((header + text).encode())}")
    if wrapped:
        # A phrase the page breaks across lines stays literal unless the writer supplies it as split
        # labels. This list is the work list for the writer's split table (INDEX_SPLIT / NR_SPLIT).
        print(f"left literal {len(wrapped)} (page wraps, writer supplies one string): "
              + " ".join(sorted(wrapped)))
    if needles:
        print(f"checker needles {len(needles)} slotted {sum(1 for ph, _ in needles if ph in labels.values())}"
              f" literal {sum(1 for ph, _ in needles if ph not in labels.values())}")
    else:
        # A checker whose needle list cannot be derived from a call with no population gives no
        # coverage signal at all; printing "0 needles" would read as a clean report that checked nothing.
        print(f"checker needles NOT DERIVED ({checker_name}) - coverage unverified")
    print("\n# writer slots (label -> phrase part)")
    for k, v in sorted(slots.items()):
        print(f"    {k!r}: {v!r},")
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        for page, checker in sorted(ALL_PAGES.items()):
            rc = build(page, checker)
            if rc:
                return rc
        return 0
    if len(argv) != 2:
        print("usage: build_report_templates.py [<notes/page.md> <verify_page.py>]")
        return 2
    return build(argv[0], argv[1])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
