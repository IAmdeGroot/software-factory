---
id: FACTORY-004
title: Add ready-queue CLI command
status: done
dependencies:
  - FACTORY-003
assignee: agent
---

# FACTORY-004: Add ready-queue CLI command

## Context

`list` shows everything. Agents pulling work need a focused view: beads that are
`ready` **and** have all dependencies satisfied. This is the primary "what should I
work on next?" interface.

## Acceptance Criteria

- [x] CLI command: `python -m harness.beads ready`
- [x] Prints only beads where status is `ready` and all dependencies are `done`
- [x] Supports `--json` flag for agent-readable output
- [x] Exit code 0 when command succeeds (even if queue is empty)
- [x] Tests cover: empty queue, one ready bead, ready bead blocked by incomplete dep

## Notes

- Reuse logic from `harness/beads/listing.py`
- Keep output minimal — id, title, and id list is enough
