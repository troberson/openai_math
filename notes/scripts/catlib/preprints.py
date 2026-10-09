"""The `preprints/` tree: manuscript directories, LaTeX roots, statement environments, `.bib` entries.

Two rules name the same 719-manuscript population and they are not the same read: the manuscript
links in `CONTENTS.md` (`overview.parse_contents`) and the `kind == "manuscript"` rows of
`notes/subfindings.tsv`. A walk of `preprints/` is **749** directories, not 719 manuscripts —
upstream keeps 27 superseded editions and 3 withdrawal notices on disk beside their replacements.

A root is a `.tex` file with `\\documentclass` **at the start of a line**: over the 719 listed dirs,
715 have exactly one, 3 have two, 1 has three. A substring count of the command name reads 714 / 4 / 1
because one dir ships a bundled PGF documentation macro that defines a macro *mentioning* the command.

Main-file resolution prefers `main.tex` **that declares `\\documentclass`**, then `paper.tex`, then the
single root; a multi-root dir with neither is flagged (`None`), never guessed. Every one of the 719
resolved main files sits under a `build/` directory, so `parts[-2]` is not a manuscript location here —
ownership is the component after `preprints` (`catlib.paths.owner`).

Statement environments are counted by the **declared rule**: `\\begin{X}` for X declared by
`\\newtheorem` in the same dir, minus `NON_STATEMENT`. The six-name list
(theorem/lemma/proposition/corollary/claim/conjecture) is kept as a separate measure, not as the
default: the two figures differ by 85 occurrences and a count must name its rule.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from catlib.paths import PREPRINTS, SUBFINDINGS_TSV, owner, read_text
from catlib.tsv import read_rows

DOCCLASS = re.compile(r"^\s*\\documentclass", re.M)
ABSTRACT = re.compile(r"^\s*\\begin\{abstract\}", re.M)
BEGIN = re.compile(r"\\begin\{([A-Za-z*]+)\}")
PROOF = re.compile(r"\\begin\{proof\}")
NEWTHEOREM = re.compile(r"\\newtheorem\*?\{([A-Za-z]+)\}")
SECTION = re.compile(r"\\section\*?\{")
SUBSECTION = re.compile(r"\\subsection\*?\{")
SUBSUBSECTION = re.compile(r"\\subsubsection\*?\{")
BIB_ENTRY = re.compile(r"@[A-Za-z]+\s*\{([^,]*),")

# Environments declared by \newtheorem that state nothing.
NON_STATEMENT = {"definition", "remark", "example", "notation", "convention", "procedure",
                 "construction", "scope", "abstract"}

# The six-name list the release prose quotes, kept as its own measure.
SIX = {"theorem", "lemma", "proposition", "corollary", "claim", "conjecture"}


def tex_files(d: Path) -> list[Path]:
    """Every `.tex` under a manuscript directory."""
    return sorted(d.rglob("*.tex"))


def texts(files: list[Path]) -> list[str]:
    """Text of each file, undecodable bytes replaced — the corpus is not uniformly UTF-8."""
    return [read_text(f) for f in files]


def roots_of(d: Path) -> list[Path]:
    """`.tex` files under `d` that declare `\\documentclass` at the start of a line."""
    out = [f for f in d.rglob("*.tex") if DOCCLASS.search(read_text(f))]
    return sorted(out, key=lambda f: (len(f.relative_to(d).parts), str(f.relative_to(d))))


def main_tex_of(roots: list[Path]) -> tuple[Path | None, str]:
    """Prefer main.tex, then paper.tex, then the single root; flag, never guess, the rest."""
    for name in ("main.tex", "paper.tex"):
        hits = [f for f in roots if f.name == name]
        if hits:
            return hits[0], "name"
    if len(roots) == 1:
        return roots[0], "single-root"
    return None, "flagged"


def declared_envs(texts: list[str]) -> set[str]:
    """Statement environment names declared in the dir, minus the non-statement names."""
    declared: set[str] = set()
    for t in texts:
        declared.update(NEWTHEOREM.findall(t))
    return declared - NON_STATEMENT


def env_counts(texts: list[str], declared: set[str]) -> dict[str, int]:
    """Per-directory counts: proofs, declared-rule statements, sectioning, abstract flag."""
    proofs = thms = sections = subsections = subsub = 0
    abstract = 0
    for t in texts:
        proofs += len(PROOF.findall(t))
        thms += len([m for m in BEGIN.findall(t) if m in declared])
        sections += len(SECTION.findall(t))
        subsections += len(SUBSECTION.findall(t))
        subsub += len(SUBSUBSECTION.findall(t))
        if ABSTRACT.search(t):
            abstract = 1
    return {"proofs": proofs, "thms": thms, "sections": sections, "subsections": subsections,
            "subsubsections": subsub, "abstract": abstract}


def six_count(texts: list[str]) -> int:
    """Occurrences of the six-name list, the measure that sits 85 below the declared rule."""
    return sum(sum(1 for m in BEGIN.findall(t) if m in SIX) for t in texts)


def per_name_counts(texts: list[str], declared: set[str]) -> Counter:
    """Declared-rule statement counts keyed by environment name."""
    per_name: Counter = Counter()
    for t in texts:
        per_name.update(m for m in BEGIN.findall(t) if m in declared)
    return per_name


def listed_dirs_from_contents() -> set[str]:
    """The manuscript directory names CONTENTS.md links — not a walk of `preprints/`."""
    from catlib.overview import parse_contents

    return {Path(p).parts[1] for ps in parse_contents().values() for p in ps}


def listed_dirs_from_subfindings() -> dict[str, dict[str, str]]:
    """{slug: row} for the manuscript rows of notes/subfindings.tsv (719 rows)."""
    return {r["path"].split("/")[1]: r for r in read_rows(SUBFINDINGS_TSV) if r["kind"] == "manuscript"}


def bib_files(scope: set[str] | None = None) -> list[Path]:
    """`.bib` files in the tree; with a scope, only those owned by a listed manuscript dir."""
    files = sorted(PREPRINTS.glob("**/*.bib"))
    if scope is None:
        return files
    return [p for p in files if owner(p) in scope]


def bib_entries(scope: set[str]) -> list[tuple[str, str]]:
    """(owning dir, entry body) for every `@`-entry in a `.bib` owned by a listed manuscript."""
    out: list[tuple[str, str]] = []
    for p in bib_files(scope):
        txt = read_text(p)
        for m in BIB_ENTRY.finditer(txt):
            nxt = txt.find("@", m.end())
            out.append((owner(p), txt[m.start(): nxt if nxt > 0 else len(txt)]))
    return out
