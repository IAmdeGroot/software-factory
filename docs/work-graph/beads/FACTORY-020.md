---
id: FACTORY-020
title: Add markdown wish drop and list command
status: done
dependencies:
  - FACTORY-019
assignee: agent
---

# FACTORY-020: Add markdown wish drop and list command

## Context

The Wish Factory starts with a drop, not a swarm. Humans (and later
intake) write a wish; agents must be able to list open ones. Same shape
as beads: markdown + YAML, git-tracked, no paid tracker.

## Acceptance Criteria

- [x] Wish files live under `docs/work-graph/wishes/` with YAML frontmatter
- [x] Required fields: `id`, `title`, `status` (`open` | `planned` | `done`), `source`
- [x] CLI: `python -m harness.beads wishes` lists open wishes (stable sort by id)
- [x] `wishes --json` works
- [x] Validator rejects invalid wish files (or a dedicated validate path)
- [x] Tests cover list, empty drop, and invalid status
- [x] Tests pass

## Notes

- Do not convert wishes into beads in this bead (FACTORY-021)
- Do not add Discord/GitHub intake
- Keep stdlib-only Python
