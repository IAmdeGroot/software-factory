# Software Factory — Agent Operating Contract

This repository is a **software factory**: a harness for harnessed agentic engineering.
The harness is bonded to the products it builds (today: `examples/dark-dungeon/`). Do not build a reusable Gas Town. Next increment is the Wish Factory: wishes become beads; workers still stop on an empty ready queue.

## Core Loop

Every non-trivial task follows:

1. **Plan** — read project brain + bead; produce a short plan before editing.
2. **Implement** — smallest change that satisfies acceptance criteria.
3. **Verify** — run relevant tests/checks; fix failures.
4. **Review** — self-review diff against bead criteria before marking done.
5. **Update state** — update the bead and decision log if needed.

## Context Sources (read in this order)

1. `context.md` — factory purpose and mental model
2. `docs/brain/` — vision, architecture, conventions, decisions
3. `docs/work-graph/beads/` — current work item
4. Source code under `harness/`, `examples/`, or `products/`

## Roles

| Role | Responsibility |
|------|----------------|
| **Human** | Vision, trade-offs, quality bar, exceptional decisions |
| **Planner** | Break goals into beads with dependencies and acceptance criteria |
| **Worker** | Claim ready beads, implement, test, update bead state |
| **Reviewer** | Check diff against acceptance criteria before merge |

## Bead Rules

- One bead = one branch = one PR-sized change.
- Do not start work on blocked beads.
- If you discover new work, create a new bead and link dependencies.
- Mark beads: `ready` → `in_progress` → `review` → `done` (or `blocked`).

## Quality Bar

- Prefer small, reviewable diffs over large rewrites.
- Add or update tests when behavior changes.
- Record non-obvious decisions in `docs/brain/decisions.md`.
- Do not expand scope beyond the current bead without human approval.

## Cost Discipline

- Use Plan Mode for multi-file or architectural work.
- Avoid frontier models for routine tasks.
- Deterministic scripts watch; AI acts when reasoning is required.

## When to Escalate to Human

- Architecture forks with no clear winner in docs
- Security-sensitive changes
- Scope changes that affect project vision
- Repeated test/review failures on the same bead

## Unattended worker

Prompt: **Implement the next ready bead**

When that prompt (or no bead id) is given, run `python -m harness.beads next`. If the ready queue is empty, stop — do not invent work.

After verify, commit with a `FACTORY-NNN:` prefix, push one branch, and open one PR against the repository default branch when the environment can. Do not merge. If PR creation is unavailable, report that a human must open the PR.

To run this on a schedule, create a Cursor Automation from `.cursor/automations/worker-loop.md`. Enabling it in the Cursor dashboard is a human action; the recipe is committed here.

## CI triage

Prompt: **Triage the latest CI failure on this repository**

Recipe: `.cursor/automations/ci-triage.md`. Green CI means stop. Fix in-scope failures; otherwise create a new bead and stop. Enabling the automation is a human dashboard action.

## Unattended reviewer

Prompt: **Review the next bead**

When that prompt (or no bead id) is given, follow `.cursor/skills/bead-reviewer/SKILL.md`. Run `python -m harness.beads review-queue`. Empty queue means stop. On pass, `python -m harness.beads done <id>`, then mark the matching PR ready for review when tools allow. On fail, leave `review` and list failing criteria. If no PR exists, say so and stop. Do not merge PRs.

To run this without a chat message, create a Cursor Automation from `.cursor/automations/pr-review.md` (prompt `Review the next bead`). Trigger on PR opened or CI green when the dashboard allows it. Enabling it is a human dashboard action.

## Land / merge

Humans merge. Recipe: `.cursor/automations/land.md`.

Merge only when the bead is `done`, CI is green, and the PR is one bead. Integration branch is `main` (renaming GitHub's default branch is a human setting). Agents do not merge.





