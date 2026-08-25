---
id: FACTORY-012
title: Add review-queue CLI command
status: ready
dependencies:
  - FACTORY-007
assignee: null
---

# FACTORY-012: Add review-queue CLI command

## Context

Workers `complete` beads into `review`. Reviewers and automations need a focused
queue, the same way `ready` is the worker pull-work view. Without it, closing a
bead still waits on a human to name the id.

## Acceptance Criteria

- [ ] CLI command: `python -m harness.beads review-queue`
- [ ] Prints only beads whose status is `review` (stable sort by bead id)
- [ ] Supports `--json` with id, title, and count
- [ ] Exit code 0 when the command succeeds (even if the queue is empty)
- [ ] Tests cover: empty queue, one bead in review, mixed statuses
- [ ] `harness/README.md` documents the command

## Notes

- Reuse `harness/beads/listing.py`; do not change `complete` / `done` behavior
- This is a read-only command — it does not claim or transition status
