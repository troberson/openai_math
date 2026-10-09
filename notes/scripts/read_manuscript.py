#!/usr/bin/env python3
"""Print what a manuscript says, with file:line anchors. Report-only; writes nothing.

Reading a manuscript for a summary page needs three things and the anchors for each:
the abstract, the section skeleton, and the titled statement environments. This prints
those from the LaTeX source, so every sentence a page writes can cite a line.

Rules, and why they are these:
- The main file is the one `build_sources.main_tex_of` resolves (a root named `main.tex`,
  then `paper.tex`, then the single root). A root is a `.tex` declaring `\\documentclass`
  at the start of a line; a substring count of the command reads 717 dirs and 5 roots,
  because a bundled PGF macro *mentions* the command.
- Statements are `\\begin{X}` for X declared by `\\newtheorem` in the same directory, minus
  the non-statement names (`definition`, `remark`, ...). The corpus-wide figure under this
  rule is 21,402; the six-name list is 21,317.
- A statement's title is its **optional** bracket argument, which most environments leave
  empty: 1,498 of 2,270 headline `theorem` begins are titled per line. A title that spans a
  newline is missed by a per-line scan (1,508 over the whole text).
- `\\input`/`\\include` targets are printed, not followed: the section skeleton of a
  multi-file manuscript is per file, and following includes silently reorders a paper.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_sources as S  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
SECTION = re.compile(r"\\(section|subsection|subsubsection)\*?\{([^}]*)\}")
STATEMENT = re.compile(r"\\begin\{([A-Za-z]+)\}(?:\[([^\]]*)\])?")
ABSTRACT = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
INCLUDE = re.compile(r"\\(input|include|subfile)\{([^}]+)\}")
TITLE_WORDS = re.compile(r"\\title\{([^}]*)\}")


def tex_files(d):
    return sorted(d.rglob("*.tex"))


def statements(files, limit):
    declared = set()
    for f in files:
        declared.update(S.NEWTHEOREM.findall(f.read_text(encoding="utf-8", errors="replace")))
    declared -= S.NON_STATEMENT
    out = []
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            for m in STATEMENT.finditer(line):
                if m.group(1) in declared and (m.group(2) or "").strip():
                    out.append((f, n, m.group(1), m.group(2).strip()))
                    if limit and len(out) >= limit:
                        return out, declared
    return out, declared


def main():
    argv, flags = [], []
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        a = args[i]
        if a.startswith("--"):
            flags.append(a)
            if a == "--limit" and i + 1 < len(args) and args[i + 1].isdigit():
                flags.append(f"--limit={args[i + 1]}")
                i += 1
        else:
            argv.append(a)
        i += 1
    if not argv:
        print("usage: read_manuscript.py <preprints-dir> [--limit N] [--all] [--sections-only]")
        return 1
    d = ROOT / "preprints" / argv[0]
    if not d.is_dir():
        print(f"NOT A DIRECTORY: preprints/{argv[0]}")
        return 1
    files = tex_files(d)
    roots = [f for f in files if S.DOCCLASS.search(f.read_text(encoding="utf-8", errors="replace"))]
    main_tex, rule = S.main_tex_of(roots)
    rel = main_tex.relative_to(ROOT) if main_tex else None
    print(f"dir            {argv[0]}")
    print(f"tex files      {len(files)}  roots (line-start documentclass) {len(roots)}")
    print(f"main file      {rel}  (resolved by: {rule})")
    if main_tex:
        t = TITLE_WORDS.search(main_tex.read_text(encoding="utf-8", errors="replace"))
        print(f"\\title        {t.group(1) if t else '(none in main file)'}")
    if "--sections-only" in flags:
        return 0

    if main_tex:
        text = main_tex.read_text(encoding="utf-8", errors="replace")
        ab = ABSTRACT.search(text)
        print("\n== abstract (main file) ==")
        if ab:
            body = re.sub(r"\s+", " ", ab.group(1)).strip()
            print(f"[{main_tex.relative_to(ROOT)}:abstract] {body}")
        else:
            print("(no abstract environment in the main file)")

    print("\n== includes in the main file ==")
    if main_tex:
        for n, line in enumerate(main_tex.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            for m in INCLUDE.finditer(line):
                print(f"  {main_tex.relative_to(ROOT)}:{n} \\{m.group(1)}{{{m.group(2)}}}")

    print("\n== sections ==")
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
            for m in SECTION.finditer(line):
                depth = {"section": 0, "subsection": 1, "subsubsection": 2}[m.group(1)]
                print(f"  {'  ' * depth}{f.relative_to(ROOT)}:{n}  {m.group(2)}")

    limit = 40
    for a in flags:
        if a.startswith("--limit"):
            limit = int(a.split("=")[1]) if "=" in a else 40
    stmts, declared = statements(files, 0 if "--all" in flags else limit)
    print(f"\n== titled statements (declared envs: {', '.join(sorted(declared))}) ==")
    for f, n, kind, title in stmts:
        print(f"  {f.relative_to(ROOT)}:{n}  {kind}  {title}")
    if not "--all" in flags and limit:
        print(f"  (first {limit}; --all for every titled statement)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
