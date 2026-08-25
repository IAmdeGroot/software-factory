---
id: FACTORY-021
title: Convert open wishes into beads
status: ready
dependencies:
  - FACTORY-020
assignee: null
---

# FACTORY-021: Convert open wishes into beads

## Context

A wish is not work until a planner turns it into one or more beads with
acceptance criteria. That is the producer side of the Beads machine:
ambition in, implementation beads out. Unattended workers still do not
invent work when the ready queue is empty.

## Acceptance Criteria

- [ ] Planner skill (or a dedicated wish-planner skill) converts `open` wishes into beads
- [ ] Converted wishes move to `planned` and point at the new bead ids
- [ ] New beads use the right prefix (`DUNGEON-` for game work, `FACTORY-` for harness)
- [ ] Recipe or skill says: empty wish list means stop; do not invent wishes
- [ ] `docs/work-graph/backlog.md` documents the wish → bead prompt
- [ ] Tests pass (harness tests + bead validate)

## Notes

- Do not implement the wished feature in this bead
- Do not auto-claim or start workers
- Human still confirms large scope; one wish may become several beads
