"""The digest-keyed record store.

Cache key: the five git tree digests of the tracked read surface, the sha256 of the consumer's own
source, the sha256 of each L1 file it reads, and its args. The tree digests are exact because the
read surface is fully tracked — `git status --porcelain --ignored=matching` over the five hashed
paths returns 0 lines — so a tree digest and the working tree cannot disagree, and a key computed
from them is a key for the bytes the consumer is about to read.

Records live under `.qwen/cache/records/<key>/`. The `.qwen/*` rule in `.gitignore` keeps the whole
tree untracked, so a cache write never touches the tracked tree and `git status` stays clean.

Records are megabytes, text is not: the store carries derived counts keyed by manuscript directory,
never raw `.tex`. `preprints/` is 632 MB and `lean/OAI/` is 1.8 GB; the eight top-level `notes/*.tsv`
total 630,606 bytes. A record store that carried text would be the corpus with extra steps.

The five hashed paths are the same list `verify_fleet_design.py` carries. The checker keeps its own
copy: a checker that re-derives a count through the code the page uses proves nothing, so the digest
rule is duplicated on the checker side by the same rule that keeps the checkers out of `measure.py`.
"""

from __future__ import annotations

import hashlib
import json
import subprocess

from pathlib import Path
from typing import Any

from catlib import preprints
from catlib.atomic import write_atomic
from catlib.paths import PREPRINTS, ROOT, rel
from catlib.preprints import DOCCLASS

DIGEST_PATHS = ["HEAD:preprints", "HEAD:lean", "HEAD:overview.tex", "HEAD:CONTENTS.md",
                "HEAD:reasoning_traces"]

RECORDS_ROOT = ROOT / ".qwen" / "cache" / "records"


def tree_digests() -> list[str]:
    """The five git tree digests, in DIGEST_PATHS order. One `git rev-parse` call, ~0.002 s."""
    out = subprocess.run(["git", "rev-parse", *DIGEST_PATHS], cwd=ROOT,
                         capture_output=True, text=True, check=True)
    return out.stdout.split()


def sha(text: str) -> str:
    """sha256 of text, the form every key component takes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def key(source: str, l1: tuple[str, ...] = (), args: tuple[str, ...] = ()) -> str:
    """The cache key: tree digests, the consumer's own source, its L1 inputs, its args.

    `source` is the consumer's source text, so editing the consumer invalidates its records.
    `l1` is the text of the tracked files it reads that are not part of the five hashed trees
    (`notes/catalog.tsv` is the common case). `args` is the command line, so a `--tsv` run and a
    plain run do not share a record.
    """
    parts = tree_digests() + [sha(source)] + [sha(t) for t in l1] + list(args)
    return sha("\n".join(parts))[:32]


def store_dir(k: str) -> Path:
    """The keyed record directory, created on demand."""
    d = RECORDS_ROOT / k
    d.mkdir(parents=True, exist_ok=True)
    return d


def cached(k: str, name: str, builder) -> str:
    """The record text under the keyed store; built once and read back on every later call.

    `builder` produces the record text. A cache hit reads the file; a miss builds it, writes it
    through `write_atomic`, and returns the same text, so the first run and the second run of a
    consumer see identical bytes.
    """
    path = RECORDS_ROOT / k / name
    if path.is_file():
        return path.read_text(encoding="utf-8")
    text = builder()
    write_atomic(path, text)
    return text


def record_for(d: Path) -> dict[str, Any]:
    """The per-manuscript record: every derived count a consumer re-derives today, read once.

    Each `.tex` in the dir is read exactly once. `roots_of` used to re-read the whole dir because
    it took a path, not the texts, so a consumer that wanted roots and counts read every file
    twice; the roots here are the same line-start rule applied to the texts already in hand.
    """
    files = preprints.tex_files(d)
    ts = preprints.texts(files)
    declared = preprints.declared_envs(ts)
    roots = [f for f, t in zip(files, ts, strict=True) if DOCCLASS.search(t)]
    roots = sorted(roots, key=lambda f: (len(f.relative_to(d).parts), str(f.relative_to(d))))
    main, rule = preprints.main_tex_of(roots)
    return {
        "dir": d.name,
        "tex": [rel(f) for f in files],
        "tex_bytes": sum(f.stat().st_size for f in files),
        "roots": [rel(f) for f in roots],
        "main": rel(main) if main is not None else "",
        "rule": rule,
        "bib": [rel(f) for f in sorted(d.rglob("*.bib"))],
        "counts": preprints.env_counts(ts, declared),
        "six": preprints.six_count(ts),
        "per_name": dict(sorted(preprints.per_name_counts(ts, declared).items())),
        "declared": sorted(declared),
        "titles": preprints.statement_titles(files, ts),
        "abstracts": preprints.abstract_texts(files, ts),
    }


def manuscript_store(k: str) -> dict[str, dict[str, Any]]:
    """The keyed store as {dir: record}, over every directory under `preprints/`.

    Built once per key, read back on every later call. The population is the 749 dirs on disk,
    not the 719 listed manuscripts: `measure_names.py` scans the whole tree, so a store scoped to
    the listed set cannot reproduce its counts. A consumer that wants the manuscript list filters
    the store by the `overview.tex` slug set, which is the same filter `build_sources.py` uses.
    """
    path = RECORDS_ROOT / k / "manuscripts.jsonl"
    if not path.is_file():
        dirs = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
        write_atomic(path, "\n".join(json.dumps(record_for(d), ensure_ascii=False) for d in dirs))
    rows = (json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
    return {r["dir"]: r for r in rows}
