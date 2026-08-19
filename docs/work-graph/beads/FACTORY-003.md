---
id: FACTORY-003
title: Add bead status listing script
status: blocked
dependencies:
  - FACTORY-002
assignee: null
---

# FACTORY-003: Add bead status listing script

## Context

Agents (and humans) need to see which beads are ready to work on. This script
queries the work graph and prints a status summary.

## Acceptance Criteria

- [ ] CLI command (e.g. `python -m harness.beads list` or `npm run beads:list`)
- [ ] Lists all beads with their status
- [ ] Highlights **ready** beads (all dependencies satisfied and status is `ready`)
- [ ] Shows blocked beads and what they are waiting on
- [ ] Exit code 0 on success
- [ ] Tests cover: all-ready, blocked-by-dep, mixed statuses

## Notes

- This is the "pull work" interface — agents run this to find available tasks
- Output should be agent-readable (plain text or JSON flag)
