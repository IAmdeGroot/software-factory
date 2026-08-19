# Work Backlog

Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.

## Ready

| ID | Title | Status |
|----|-------|--------|
| [FACTORY-001](beads/FACTORY-001.md) | Validate bead file schema | ready |

## Blocked (waiting on dependencies)

| ID | Title | Blocked by |
|----|-------|------------|
| [FACTORY-002](beads/FACTORY-002.md) | Create harness project scaffold | FACTORY-001 |
| [FACTORY-003](beads/FACTORY-003.md) | Add bead status listing script | FACTORY-002 |

## Done

_(none yet)_

---

## How to Use

1. Pick the top **ready** bead
2. Tell Cursor Agent: `Claim and implement FACTORY-001`
3. Agent reads the bead, implements, tests, updates status
4. When done, next bead becomes ready
