---
id: FACTORY-001
title: Validate bead file schema
status: done
dependencies: []
assignee: agent
---

# FACTORY-001: Validate bead file schema

## Context

Every bead is a markdown file with YAML frontmatter. Before building harness scripts,
we need a validator that ensures bead files are well-formed.

## Acceptance Criteria

- [x] A script or test exists that reads all files in `docs/work-graph/beads/`
- [x] Validates required frontmatter fields: `id`, `title`, `status`, `dependencies`
- [x] Validates `status` is one of: `ready`, `in_progress`, `review`, `done`, `blocked`
- [x] Validates `id` matches the filename (e.g. `FACTORY-001.md` → id `FACTORY-001`)
- [x] Validates dependency IDs reference existing bead files
- [x] Reports clear errors for invalid beads
- [x] All existing beads pass validation

## Notes

- Keep it simple: Python or Node, whichever is chosen in harness setup
- This is the first real factory code — set the pattern for testability
