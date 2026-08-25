---
id: FACTORY-012
title: Add review-queue CLI command
status: done
dependencies:
  - FACTORY-007
assignee: agent
---

# FACTORY-012: Add review-queue CLI command

## Context

Workers `complete` beads into `review`. Reviewers and automations need a focused
queue, the same way `ready` is the worker pull-work view. Without it, closing a
bead still waits on a human to name the id.

## Acceptance Criteria

- [x] CLI command: `python -m harness.beads review-queue`
- [x] Prints only beads whose status is `review` (stable sort by bead id)
- [x] Supports `--json` with id, title, and count
- [x] Exit code 0 when the command succeeds (even if the queue is empty)
- [x] Tests cover: empty queue, one bead in review, mixed statuses
- [x] `harness/README.md` documents the command

## Notes

- Reuse `harness/beads/listing.py`; do not change `complete` / `done` behavior
- This is a read-only command — it does not claim or transition status
