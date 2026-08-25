# Work Backlog

Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.

## Ready

| ID | Title | Status |
|----|-------|--------|
| [FACTORY-008](beads/FACTORY-008.md) | Sync backlog.md from bead statuses | ready |
| [FACTORY-009](beads/FACTORY-009.md) | Add next CLI command to claim first ready bead | ready |
| [FACTORY-010](beads/FACTORY-010.md) | Add CI workflow for tests and bead validation | ready |

## In Review

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## Blocked (waiting on dependencies)

| ID | Title | Blocked by |
|----|-------|------------|
| [FACTORY-011](beads/FACTORY-011.md) | Close the unattended worker loop | FACTORY-008, FACTORY-009 |

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
| FACTORY-008 | regenerate `backlog.md` from beads | ready |
| FACTORY-009 | `next` — claim first ready bead | ready |
| FACTORY-010 | CI watches tests and bead validation | ready |
| FACTORY-011 | unattended worker skill + automation recipe | blocked by 008–009 |

---

## How to Use

1. Run `python -m harness.beads ready` to see claimable work
2. Run `python -m harness.beads claim FACTORY-00X` to claim a bead
3. Tell Cursor Agent: `Implement the claimed bead`
4. Agent implements, tests, updates status
