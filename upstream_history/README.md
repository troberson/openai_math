# upstream_history

One page per upstream commit we merge, named `YYYY-MM-DD_<short-hash>.md`: the date of the upstream
commit, its short hash, and a discussion of what it changed.

Upstream is `github.com/openai/math` (`upstream`, read-only). We merge each upstream commit as its
own merge commit on `notes` — one merge per upstream commit, never a rebase — so our reading notes
stay interleaved with their releases in history.

The release ships its own changelog at [`history.md`](../history.md). These pages are our reading of
each commit: what moved in the release surface, what it means for the counts in `notes/`, and what
we have not checked.

| Page | Upstream commit | Our merge |
| --- | --- | --- |
| [2026-10-07_3014888.md](2026-10-07_3014888.md) | `301488868` | `73d94860f` |
| [2026-10-07_fd4aeeb.md](2026-10-07_fd4aeeb.md) | `fd4aeeb2e` | `f23a1b007` |
