---
id: FACTORY-005
title: Add bead claim CLI command
status: done
dependencies:
  - FACTORY-004
assignee: agent
---

# FACTORY-005: Add bead claim CLI command

## Context

Workers need to atomically mark a bead as claimed before starting implementation.
Today this is done manually by editing the bead file. A CLI command makes the
pull-work loop more autonomous.

## Acceptance Criteria

- [x] CLI command: `python -m harness.beads claim FACTORY-NNN`
- [x] Sets bead status to `in_progress` and assignee to a provided or default value
- [x] Fails with clear error if bead is not in the ready queue
- [x] Fails if bead is already claimed (`in_progress` with assignee set)
- [x] Supports `--assignee NAME` flag (default: `agent`)
- [x] Tests cover: successful claim, not-ready bead, already-claimed bead

## Notes

- Only allow claiming beads that pass the ready-queue check from FACTORY-004
- Update the bead file in place (preserve body content)
