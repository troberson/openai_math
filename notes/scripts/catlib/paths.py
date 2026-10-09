"""Repository paths and the path rules every ledger tool shares.

This file sits at notes/scripts/catlib/paths.py, so the repository root is parents[3]:
catlib -> scripts -> notes -> repo root. build_catalog.py, one level up, uses parents[2].
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# Release surface
OVERVIEW_TEX = ROOT / "overview.tex"
CONTENTS_MD = ROOT / "CONTENTS.md"
README_MD = ROOT / "README.md"
PREPRINTS = ROOT / "preprints"
REASONING_TRACES = ROOT / "reasoning_traces"

# Lean surface
LEAN = ROOT / "lean"
FORMALIZATION_YAML = LEAN / "formalization.yaml"
LAKEFILE = LEAN / "lakefile.lean"
LAKE_MANIFEST = LEAN / "lake-manifest.json"
COMPARATOR_DIR = LEAN / "ComparatorChallenges"
OAI_DIR = LEAN / "OAI"
DOCS_DIR = LEAN / "docs"

# Ledger surface
NOTES = ROOT / "notes"
SCRIPTS = NOTES / "scripts"
LEDGER_TSV = NOTES / "catalog.tsv"
SOURCES_TSV = NOTES / "sources.tsv"
LINKS_TSV = NOTES / "links.tsv"
SUBFINDINGS_TSV = NOTES / "subfindings.tsv"
ABSTRACTS_TSV = NOTES / "abstracts.tsv"
DEPS_TSV = NOTES / "formalization-deps.tsv"
STANDING_TSV = NOTES / "conjecture-standing.tsv"
TOPICS_TSV = NOTES / "topics.tsv"
INDEX_DIR = NOTES / "index"
SUMMARIES_DIR = NOTES / "summaries"

# The nine top-level TSVs the proof gate hashes; the gate's snapshot rule is this list
# plus every file under INDEX_DIR.
GATE_TSVS = (
    LEDGER_TSV,
    SOURCES_TSV,
    LINKS_TSV,
    SUBFINDINGS_TSV,
    ABSTRACTS_TSV,
    DEPS_TSV,
    STANDING_TSV,
    TOPICS_TSV,
    NOTES / "named-results.tsv",
)


def rel(path: Path | str) -> str:
    """Repo-relative POSIX path, the form every table cell and citation anchor uses."""
    p = Path(path)
    return p.relative_to(ROOT).as_posix() if p.is_absolute() else Path(p).as_posix()


def owner(path: Path | str) -> str:
    """Manuscript directory name a preprints/ path belongs to.

    The component after `preprints`, never parts[-2]: every one of the 719 resolved main
    files sits under a `build/` directory, so parts[-2] files manuscripts under `build/`
    and `sections/` and silently makes every cross-family join match nothing.
    """
    parts = Path(path).parts
    return parts[parts.index("preprints") + 1]


def read_text(path: Path) -> str:
    """The repo's whole read surface is UTF-8 text; one call site for the encoding."""
    return path.read_text(encoding="utf-8")
