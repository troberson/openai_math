#!/usr/bin/env python3
"""Print the writer's `templates` slot dict, one label per line.

`notes/templates.md` is composed from the bytes `render_reports.templates_phrases()` returns, so
the labels a slot carries are the writer's, not the page's. This prints them with their values,
which is the read you need before adding a census row: a slot label that is a multi-line phrase
stays literal in the template, and only a one-line label is a live count. Report-only; writes
nothing.
"""

import render_reports as R


def main() -> None:
    phrases = R.templates_phrases(R.population_of("templates"))
    for key, value in sorted(phrases.items()):
        print(f"    {key!r}: {value!r},")
    print(f"labels {len(phrases)}")


if __name__ == "__main__":
    main()
