---
id: FACTORY-006
title: Add Cursor hook to validate beads on edit
status: done
dependencies:
  - FACTORY-001
assignee: agent
---

# FACTORY-006: Add Cursor hook to validate beads on edit

## Context

Deterministic checks should run automatically when bead files change — agents should
not need to remember to run the validator. This follows the "crons watch, models act"
principle using Cursor's `afterFileEdit` hook.

## Acceptance Criteria

- [x] `.cursor/hooks.json` configured with `afterFileEdit` hook
- [x] Hook runs bead validator when files under `docs/work-graph/beads/` are edited
- [x] Hook script lives in `.cursor/hooks/` and is cross-platform or documented for Windows
- [x] Validator failures produce visible feedback (stderr or hook response)
- [x] Hook does not run for unrelated file edits (matcher or path check in script)
- [x] `harness/README.md` or project README documents the hook behavior

## Notes

- Use `afterFileEdit` with a matcher if supported, otherwise filter by path in script
- Fail open on hook script errors (don't block edits) unless clearly safe to fail closed
- Keep the hook script minimal — call `python -m harness.beads validate`
