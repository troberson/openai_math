# upstream_history

One page per upstream **pull request** we merge, named `YYYY-MM-DD_<short-hash>.md`: the date of
the PR merge commit, the PR merge's short hash (which also identifies the content commit it
incorporates), and a discussion of what changed. Content and PR-merge commits are paired — the PR
merge carries no content beyond its parent, so one page covers both.

Upstream is `github.com/openai/math` (`upstream`, read-only). We merge each upstream PR as its own
merge commit on `notes` (never a rebase), so our reading notes stay interleaved with their releases
in history.

The release ships its own changelog at [`history.md`](../../../history.md). These pages are our
reading of each PR: what moved in the release surface, what it means for the counts in `notes/`,
and what we have not checked.

| Page | Upstream PR merge | Content commit | Our merge |
| --- | --- | --- | --- |
| [2026-10-07_3014888.md](2026-10-07_3014888.md) | `fd4aeeb2e` (PR #1) | `301488868` | `73d94860f` + `f23a1b007` |
| [2026-10-12_1581d4c.md](2026-10-12_1581d4c.md) | `1581d4cbd` (PR #2) | `2710f995c` | *(paired merge)* |
| [2026-10-26_7ef5c0c.md](2026-10-26_7ef5c0c.md) | `7ef5c0cc5` (PR #3) | `42907c9e9` | *(paired merge)* |
