---
id: FACTORY-021
title: Convert open wishes into beads
status: review
dependencies:
  - FACTORY-020
assignee: agent
---

# FACTORY-021: Convert open wishes into beads

## Context

A wish is not work until a planner turns it into one or more beads with
acceptance criteria. That is the producer side of the Beads machine:
ambition in, implementation beads out. Unattended workers still do not
invent work when the ready queue is empty.

## Acceptance Criteria

- [x] Planner skill (or a dedicated wish-planner skill) converts `open` wishes into beads
- [x] Converted wishes move to `planned` and point at the new bead ids
- [x] New beads use the right prefix (`DUNGEON-` for game work, `FACTORY-` for harness)
- [x] Recipe or skill says: empty wish list means stop; do not invent wishes
- [x] `docs/work-graph/backlog.md` documents the wish → bead prompt
- [x] Tests pass (harness tests + bead validate)

## Notes

- Do not implement the wished feature in this bead
- Do not auto-claim or start workers
- Human still confirms large scope; one wish may become several beads
