---
id: FACTORY-022
title: Add wish-dropper skill
status: done
dependencies:
  - FACTORY-021
assignee: agent
---

# FACTORY-022: Add wish-dropper skill

## Context

WISH-002: the human should not have to hand-write wish YAML. FACTORY-021
turns open wishes into beads, but nothing writes the wish files except a
person. A dropper agent transcribes sourced intent into `WISH-NNN.md`.

This is not idle invention. Workers still stop on an empty ready queue.
The planner still stops on an empty wish list.

## Acceptance Criteria

- [x] `.cursor/skills/wish-dropper/SKILL.md` exists
- [x] Unattended prompt: `Drop wishes from this intent`
- [x] Skill requires a source (human message, playtest note, or named gap)
- [x] Writes the next `WISH-NNN.md` as `open` (`python -m harness.beads next-wish-id`)
- [x] No source / nothing to drop means stop; do not invent wishes
- [x] Does not convert wishes into beads, claim, or start workers
- [x] `docs/work-graph/backlog.md` documents the drop prompt
- [x] Tests pass (harness tests + bead validate)

## Notes

- Do not add Discord/GitHub intake
- Do not invent Dark Dungeon features because the queue is empty
- Keep stdlib-only Python
