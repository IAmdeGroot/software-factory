---
id: DUNGEON-009
title: Add a patrolling third enemy type
status: done
dependencies:
  - DUNGEON-008
assignee: agent
---

# DUNGEON-009: Add a patrolling third enemy type

## Context

WISH-001: Hollow Knight–inspired, still top-down. First playable scope asks for
three enemy types. Room 1 has an idle one-hit insect; room 2 has an idle
two-hit crawler. A third type should move on its own — a short patrol, not a
chase — so combat is not three statues.

## Acceptance Criteria

- [x] A third enemy type exists (distinct scene/script from the insect and crawler)
- [x] It patrols a short line (does not chase the player)
- [x] One nail hit despawns it; contact still damages the player
- [x] It is placed in the second room
- [x] WASD, J-nail, HP, doorway, and the first two foes still work
- [x] Tests check patrol wiring, one-hit, and Room 2 placement
- [x] README notes three enemy types
- [x] Tests pass

## Notes

- Do not add chase, loot, a boss, or a map
- Keep top-down; do not clone a Hollow Knight enemy
- Patrol bounds stay inside room 2 walls
