---
description: Generate single-line Git commit message based on the project's commit style
---

### Purpose

Produce a single Git commit message summary line for the current changes.

Run these commands in parallel to gather context:
- `git log --oneline -5` — style reference
- `git diff --staged --stat` — summary of staged changes
- `git status --short` — overall picture

Infer the commit format from the recent commit history – match whatever style the project uses (Conventional Commits, plain imperative, Jira prefix, etc.).
If `$ARGUMENTS` is non-empty, treat it as an explicit format hint or override.
### Conventional Commits format

This is the preferred default format. If the project uses a different style, match that instead.

`<type>[optional scope]: <description>`
- type: one of `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`
- scope: omit unless it meaningfully narrows the type; one word (two at most), lowercase

### Output rules
1. Print the commit message line only – no explanation, preamble, markdown, or code fences.
2. Line length: ≤ 72 characters; optimal target range 50–65.
3. Imperative mood, lowercase first letter, no trailing period.
