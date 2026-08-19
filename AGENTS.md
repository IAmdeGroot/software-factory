# Software Factory — Agent Operating Contract

This repository is a **software factory**: a harness for harnessed agentic engineering.
The factory builds products; products live under `examples/` or future `products/`.

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
