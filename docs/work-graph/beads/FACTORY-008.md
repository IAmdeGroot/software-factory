---
id: FACTORY-008
title: Sync backlog.md from bead statuses
status: done
dependencies:
  - FACTORY-007
assignee: agent
---

# FACTORY-008: Sync backlog.md from bead statuses

## Context

`docs/work-graph/backlog.md` is edited by hand and drifts from bead files.
Agents forget to update it. The backlog should be generated from the work graph
whenever a command changes bead status.

## Acceptance Criteria

- [x] CLI command: `python -m harness.beads sync-backlog`
- [x] Regenerates the Ready / In Review / Blocked / Done tables from bead files
- [x] Preserves non-table sections (milestone notes, how-to) via markers or a stable template
- [x] `claim`, `complete`, and `done` call the sync after a successful status change
- [x] Exit code 0 on success
- [x] Tests cover: empty graph, mixed statuses, and that a status-changing command updates the backlog file
- [x] `harness/README.md` documents the command

## Notes

- Single source of truth remains `docs/work-graph/beads/`
- Keep generated output agent-readable markdown tables, matching the current backlog layout
