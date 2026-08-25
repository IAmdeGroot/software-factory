---
id: FACTORY-020
title: Add markdown wish drop and list command
status: ready
dependencies:
  - FACTORY-019
assignee: null
---

# FACTORY-020: Add markdown wish drop and list command

## Context

The Wish Factory starts with a drop, not a swarm. Humans (and later
intake) write a wish; agents must be able to list open ones. Same shape
as beads: markdown + YAML, git-tracked, no paid tracker.

## Acceptance Criteria

- [ ] Wish files live under `docs/work-graph/wishes/` with YAML frontmatter
- [ ] Required fields: `id`, `title`, `status` (`open` | `planned` | `done`), `source`
- [ ] CLI: `python -m harness.beads wishes` lists open wishes (stable sort by id)
- [ ] `wishes --json` works
- [ ] Validator rejects invalid wish files (or a dedicated validate path)
- [ ] Tests cover list, empty drop, and invalid status
- [ ] Tests pass

## Notes

- Do not convert wishes into beads in this bead (FACTORY-021)
- Do not add Discord/GitHub intake
- Keep stdlib-only Python
