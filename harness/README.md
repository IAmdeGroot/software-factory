# Harness

Factory orchestration code — scripts, validators, and automation that agents and humans use to operate the software factory.

## Planned Contents (v0)

| Component | Bead | Description |
|-----------|------|-------------|
| Bead validator | FACTORY-001 | Validate bead file schema |
| Project scaffold | FACTORY-002 | Runtime, tests, entry point |
| Bead list CLI | FACTORY-003 | Show ready/blocked beads |
| Ready queue CLI | FACTORY-004 | Claimable beads only |
| Claim CLI | FACTORY-005 | Mark a ready bead `in_progress` |
| Complete / done CLI | FACTORY-007 | `in_progress` → `review` → `done` |
| Backlog sync | FACTORY-008 | Regenerate `backlog.md` from beads |
| Next CLI | FACTORY-009 | Claim the first ready bead |
| Review queue CLI | FACTORY-012 | Beads waiting for review |
| Wish drop CLI | FACTORY-020 | List and validate markdown wishes |
| Unattended loop | FACTORY-011 | Skill + Cursor automation recipe |

## Running (FACTORY-002)

From the repository root:

```bash
# Validate all beads
python -m harness.beads

# List bead status (pull-work view)
python -m harness.beads list

# Agent-readable JSON output
python -m harness.beads list --json

# Show only currently claimable beads
python -m harness.beads ready

# Agent-readable ready queue
python -m harness.beads ready --json

# Show beads waiting for review
python -m harness.beads review-queue
python -m harness.beads review-queue --json

# List open wishes (markdown drop)
python -m harness.beads wishes
python -m harness.beads wishes --json

# Claim a ready bead
python -m harness.beads claim FACTORY-007
python -m harness.beads claim FACTORY-007 --assignee agent

# Claim the first ready bead (unattended pull)
python -m harness.beads next
python -m harness.beads next --json
python -m harness.beads next --assignee agent

# Mark an in_progress bead as review
python -m harness.beads complete FACTORY-007

# Mark a review bead as done
python -m harness.beads done FACTORY-007

# Regenerate docs/work-graph/backlog.md from bead files
python -m harness.beads sync-backlog

# Run all harness tests (equivalent to npm test)
python -m harness.tests
```

From `harness/`:

```bash
# Run tests directly from harness project
python -m unittest discover -s tests -v
```

## Project Files

- `harness/pyproject.toml` — Python runtime project metadata
- `harness/tests/__main__.py` — test runner entrypoint
- `harness/beads/` — bead-related CLI and validation

## Cursor Hook: Auto-validate bead edits

Project-level hook config:

- `.cursor/hooks.json` wires `afterFileEdit`
- `.cursor/hooks/validate-beads-on-edit.py` runs `python -m harness.beads validate`

Behavior:

- Runs validation when edited paths include `docs/work-graph/beads/*.md`
- Uses both hook matcher (`Write|TabWrite`) and script-side path checks
- Fails open (it reports errors but does not block edits)

## CI: Tests and bead validation

GitHub Actions (`.github/workflows/harness.yml`) runs on every push and pull request:

- `python3 -m harness.tests`
- `python3 -m harness.beads validate` (beads + `WISH-*.md` in `docs/work-graph/wishes/`)

Python 3.12, stdlib only — no package install step.

## Unattended worker loop

Prompt: `Implement the next ready bead`

Recipe: `.cursor/automations/worker-loop.md` (enable in the Cursor dashboard; do not invent work if `next` finds an empty queue). Worker commits, pushes, and opens one PR per bead; does not merge.

CI failures: `.cursor/automations/ci-triage.md` (prompt `Triage the latest CI failure on this repository`; green CI means stop).

Planner: prompt `Convert open wishes into beads` — `.cursor/skills/wish-planner/SKILL.md` (empty wish list means stop; do not invent wishes; do not claim or start workers).

Review: prompt `Review the next bead` — `.cursor/skills/bead-reviewer/SKILL.md` (empty `review-queue` means stop; do not merge PRs). Recipe: `.cursor/automations/pr-review.md`.

Land: humans merge using `.cursor/automations/land.md` (bead `done`, CI green, one bead). Integration branch is `main`.

## Design Principles

- **Deterministic where possible** — scripts validate, agents reason
- **Agent-readable output** — plain text or `--json` flag
- **Minimal dependencies** — keep the harness lightweight
- **Backlog is generated** — `claim` / `complete` / `done` refresh `docs/work-graph/backlog.md` between `<!-- beads:tables:start -->` and `<!-- beads:tables:end -->`. Milestone notes outside those markers are preserved.
