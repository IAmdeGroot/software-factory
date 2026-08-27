---
id: DUNGEON-013
title: Add a boss in the third room
status: in_progress
dependencies:
  - DUNGEON-012
assignee: agent
---

# DUNGEON-013: Add a boss in the third room

## Context

WISH-001: Hollow Knight–inspired, still top-down. First playable scope includes
one boss. Room 3 is empty after the seal. A larger, slower warden that takes
several honed-nail hits makes the gate pay off. No health bar, no phase 2,
no chase.

## Acceptance Criteria

- [ ] A distinct boss exists in the third room (larger than other foes)
- [ ] It takes multiple honed-nail hits (three swings at damage 2)
- [ ] It patrols slowly and does not chase
- [ ] Contact still damages the player; death still drops a shard
- [ ] Seal, shrine, rooms, and the first three foes still work
- [ ] Tests check boss hits, patrol, and Room 3 placement
- [ ] README notes the warden in room 3
- [ ] Tests pass

## Notes

- Do not add a boss HP bar, phases, or a map
- Keep top-down; do not clone a Hollow Knight boss
- Unhoned nail cannot reach this room (seal already gates it)
