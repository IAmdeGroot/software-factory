---
id: FACTORY-019
title: Leave Gas Town for the Wish Factory
status: done
dependencies: []
assignee: agent
---

# FACTORY-019: Leave Gas Town for the Wish Factory

## Context

The v0 factory loop is closed. The human chose Yegge's later essay
([The Shape of Things to Come](https://yegge.ai/essays/the-shape-of-things-to-come/))
over Gas Town: no reusable orchestrator, no Mayor/polecat fleet. The
harness grows because Dark Dungeon needs it. Wishes feed the work graph.

## Acceptance Criteria

- [x] `docs/brain/decisions.md` records leaving Gas Town for the Wish Factory
- [x] `docs/brain/vision.md` and `docs/brain/architecture.md` stop treating a reusable Gas Town as the next step
- [x] Next increment beads exist: wish drop, wish-to-bead planner, one Dark Dungeon room
- [x] `python3 -m harness.beads validate` and harness tests pass

## Notes

- Do not implement wish intake or game rooms in this bead
- Do not add Cursor SDK, parallel workers, or a merge thunderdome here
- Empty ready queue still means unattended workers stop
