---
id: FACTORY-009
title: Add next CLI command to claim first ready bead
status: in_progress
dependencies:
  - FACTORY-005
assignee: agent
---

# FACTORY-009: Add next CLI command to claim first ready bead

## Context

`claim` requires a bead id. An unattended worker needs to pull the next unit of
work without a human naming it.

## Acceptance Criteria

- [ ] CLI command: `python -m harness.beads next`
- [ ] Claims the first ready-queue bead (stable sort by bead id)
- [ ] Supports `--assignee NAME` (default: `agent`)
- [ ] Prints the claimed bead id (and title) on success
- [ ] Supports `--json` with id, title, and assignee
- [ ] Exit code 1 with a clear error when the ready queue is empty
- [ ] Tests cover: claims first ready bead, empty queue, skips non-ready beads
- [ ] `harness/README.md` documents the command

## Notes

- Reuse `claim_bead` and `build_ready_queue`; do not reimplement claim rules
- If FACTORY-008 is already merged, `next` should inherit backlog sync through `claim`
