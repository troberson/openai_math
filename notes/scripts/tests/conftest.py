"""The shared loader for the extracted checker self-tests.

The tests live under `notes/scripts/tests/`, so the checker modules sit in the same tree the loader
walks. The checkers import their siblings by bare name (`import extract_scope_notes as ex`) and import
the `catlib` package, so the script tree has to be on `sys.path` before any checker is imported; each
checker is loaded as a module from its file, which is what makes `ROOT = Path(__file__).resolve().parents[2]`
resolve to the repo root inside it.
"""

import csv
import importlib.util
import os
import pathlib
import sys

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parents[1]

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# pylint: disable=wrong-import-position
from catlib.layout import (  # noqa: E402  # the script tree is on sys.path only after the insert
    shift,
)

REPO = pathlib.Path(__file__).resolve().parents[3]


@pytest.fixture(scope="module")
def ledger():
    """The ledger rows, for the joins a population is checked against. Read once per module."""
    return list(csv.DictReader((REPO / "notes/gen/tables/catalog.tsv").read_text(
        encoding="utf-8").splitlines(), delimiter="\t"))


@pytest.fixture(autouse=True, scope="module")
def layout_shift(request):
    """When `LAYOUT_SHIFT` is set, the pages the checkers verify are read shifted.

    The patch is the probe: the fixture that hands a test its page and the checker's own page read
    both go through `Path.read_text`, so the page and the population the needle derives from it
    shift together. A needle that re-derives its anchor from the mutated page moves with the page;
    a needle that recorded the anchor as committed fires a message the shifted page never prints.
    The scope is the page tree the checkers verify — `notes/gen/reports/` and `notes/development/` —
    not the index, the summaries, the manuscripts, or the Lean source, so the corpus the
    population is measured from is unchanged. `test_cache_promotion.py` is excluded: its pass
    compares cached bytes with the bytes on the tracked path, so shifting a page makes every page
    differ and the pass reports the first mismatch, which is not a layout finding.
    """
    if not os.environ.get("LAYOUT_SHIFT") or request.node.module.__name__.endswith("cache_promotion"):
        yield
        return
    orig = pathlib.Path.read_text
    pages = (pathlib.Path("notes/gen/reports"), pathlib.Path("notes/development"))

    def read_text(self, *args, **kwargs):
        text = orig(self, *args, **kwargs)
        if self.suffix == ".md" and any(p in self.parents for p in pages):
            return shift(text)
        return text

    # The fixture is the monkeypatch: it swaps Path.read_text for the shifting reader and restores
    # it on teardown. A method assignment is not type-safe, so mypy is right about the shape; the
    # swap is the point of the fixture and cannot be typed, so the code is named on each side.
    pathlib.Path.read_text = read_text  # type: ignore[method-assign]
    yield
    pathlib.Path.read_text = orig  # type: ignore[method-assign]


@pytest.fixture(scope="session")
def load():
    """Return the loader: name -> the checker as a module, loaded once per session.

    The loader memoizes, because a checker's `functools.cache` lives on the module object: a loader
    that re-executed the module per test gave each test a fresh, empty cache, so a `population()`
    under `@cache` was paid once per test, not once per run. The checkers write nothing and the tests
    mutate page text in memory, so sharing one module across tests cannot make a test see a different
    corpus.
    """
    cache: dict[str, object] = {}

    def _load(name: str):
        if name in cache:
            return cache[name]
        spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
        assert spec is not None and spec.loader is not None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        cache[name] = mod
        return mod

    return _load
