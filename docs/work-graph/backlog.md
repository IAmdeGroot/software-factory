# Work Backlog

Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.

<!-- beads:tables:start -->
## Ready

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## In Progress

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## In Review

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## Blocked (waiting on dependencies)

| ID | Title | Blocked by |
|----|-------|------------|
| _(none)_ | | |

## Done

| ID | Title | Status |
|----|-------|--------|
| [FACTORY-001](beads/FACTORY-001.md) | Validate bead file schema | done |
| [FACTORY-002](beads/FACTORY-002.md) | Create harness project scaffold | done |
| [FACTORY-003](beads/FACTORY-003.md) | Add bead status listing script | done |
| [FACTORY-004](beads/FACTORY-004.md) | Add ready-queue CLI command | done |
| [FACTORY-005](beads/FACTORY-005.md) | Add bead claim CLI command | done |
| [FACTORY-006](beads/FACTORY-006.md) | Add Cursor hook to validate beads on edit | done |
| [FACTORY-007](beads/FACTORY-007.md) | Add complete and done CLI commands | done |
| [FACTORY-008](beads/FACTORY-008.md) | Sync backlog.md from bead statuses | done |
| [FACTORY-009](beads/FACTORY-009.md) | Add next CLI command to claim first ready bead | done |
| [FACTORY-010](beads/FACTORY-010.md) | Add CI workflow for tests and bead validation | done |
| [FACTORY-011](beads/FACTORY-011.md) | Close the unattended worker loop | done |
| [FACTORY-012](beads/FACTORY-012.md) | Add review-queue CLI command | done |
| [FACTORY-013](beads/FACTORY-013.md) | Add bead-reviewer skill | done |
| [FACTORY-014](beads/FACTORY-014.md) | Add PR review automation recipe | done |
| [FACTORY-015](beads/FACTORY-015.md) | Add CI triage automation recipe | done |
<!-- beads:tables:end -->

---

## Milestone 2 — Pull-Work Loop + Guardrails

Goal: agents can discover ready work, claim it, and get automatic validation on bead edits.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-004 | `ready` command — focused pull-work queue | done |
| FACTORY-005 | `claim` command — mark bead in_progress | done |
| FACTORY-006 | Cursor hook — auto-validate bead file edits | done |

---

## Milestone 3 — Close the Factory Loop

Goal: workers can finish beads and pull the next one without a human editing markdown or naming the task. Product work (Dark Dungeon) stays deferred until this loop is closed.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-007 | `complete` / `done` — status transitions | done |
| FACTORY-008 | regenerate `backlog.md` from beads | done |
| FACTORY-009 | `next` — claim first ready bead | done |
| FACTORY-010 | CI watches tests and bead validation | done |
| FACTORY-011 | unattended worker skill + automation recipe | done |

---

## Milestone 4 — Review Loop + CI Triage

Goal: beads in `review` and failed CI can wake an agent without a human naming the work. Humans still merge. Dark Dungeon stays deferred.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-012 | `review-queue` — beads waiting for review | done |
| FACTORY-013 | bead-reviewer skill — accept or reject | done |
| FACTORY-014 | PR review automation recipe | done |
| FACTORY-015 | CI triage automation recipe | done |

---

## How to Use

1. Run `python -m harness.beads ready` to see claimable work
2. Run `python -m harness.beads claim FACTORY-00X` to claim a bead
3. Tell Cursor Agent: `Implement the claimed bead`
4. Agent implements, tests, then runs `python -m harness.beads complete <id>`
5. Unattended: `Implement the next ready bead` (empty queue means stop)
