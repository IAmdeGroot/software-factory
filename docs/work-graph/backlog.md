# Work Backlog

Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.

## Ready

| ID | Title | Status |
|----|-------|--------|
| _(none — waiting for review decisions)_ | | |

## In Review

| ID | Title | Status |
|----|-------|--------|
| [FACTORY-005](beads/FACTORY-005.md) | Add bead claim CLI command | review |

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
| [FACTORY-006](beads/FACTORY-006.md) | Add Cursor hook to validate beads on edit | done |

---

## Milestone 2 — Pull-Work Loop + Guardrails

Goal: agents can discover ready work, claim it, and get automatic validation on bead edits.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-004 | `ready` command — focused pull-work queue | done |
| FACTORY-005 | `claim` command — mark bead in_progress | review |
| FACTORY-006 | Cursor hook — auto-validate bead file edits | done |

---

## How to Use

1. Run `python -m harness.beads ready` to see claimable work
2. Run `python -m harness.beads claim FACTORY-00X` to claim a bead
3. Tell Cursor Agent: `Implement the claimed bead`
4. Agent implements, tests, updates status
