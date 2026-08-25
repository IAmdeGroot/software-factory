---
id: FACTORY-007
title: Add complete and done CLI commands
status: in_progress
dependencies:
  - FACTORY-005
assignee: agent
---

# FACTORY-007: Add complete and done CLI commands

## Context

`claim` starts work. Finishing still requires hand-editing bead frontmatter.
Workers should close a bead with a single command so status updates are
deterministic instead of conversational.

## Acceptance Criteria

- [ ] CLI command: `python -m harness.beads complete FACTORY-NNN`
- [ ] `complete` sets status from `in_progress` to `review` and preserves body content
- [ ] CLI command: `python -m harness.beads done FACTORY-NNN`
- [ ] `done` sets status from `review` to `done` and preserves body content
- [ ] Both commands fail with a clear error if the bead is missing or in the wrong status
- [ ] Tests cover: successful complete, successful done, wrong-status failure, missing bead
- [ ] `harness/README.md` documents both commands

## Notes

- Reuse frontmatter parse/write helpers from `claim` rather than duplicating YAML handling
- Do not change `claim` behavior except to share helpers if needed
- Leave backlog.md updates to FACTORY-008
