---
id: FACTORY-003
title: Add bead status listing script
status: done
dependencies:
  - FACTORY-002
assignee: agent
---

# FACTORY-003: Add bead status listing script

## Context

Agents (and humans) need to see which beads are ready to work on. This script
queries the work graph and prints a status summary.

## Acceptance Criteria

- [x] CLI command (e.g. `python -m harness.beads list` or `npm run beads:list`)
- [x] Lists all beads with their status
- [x] Highlights **ready** beads (all dependencies satisfied and status is `ready`)
- [x] Shows blocked beads and what they are waiting on
- [x] Exit code 0 on success
- [x] Tests cover: all-ready, blocked-by-dep, mixed statuses

## Notes

- This is the "pull work" interface — agents run this to find available tasks
- Output should be agent-readable (plain text or JSON flag)
