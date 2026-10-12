"""The shared loader for the extracted checker self-tests.

The tests live under `notes/scripts/tests/`, so the checker modules sit in the same tree the loader
walks. The checkers import their siblings by bare name (`import extract_scope_notes as ex`) and import
the `catlib` package, so the script tree has to be on `sys.path` before any checker is imported; each
checker is loaded as a module from its file, which is what makes `ROOT = Path(__file__).resolve().parents[2]`
resolve to the repo root inside it.
"""

import importlib.util
import pathlib
import sys

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parents[1]

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


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
