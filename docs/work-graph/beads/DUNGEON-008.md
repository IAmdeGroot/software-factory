---
id: DUNGEON-008
title: Add a second enemy type in the east room
status: done
dependencies:
  - DUNGEON-007
assignee: agent
---

# DUNGEON-008: Add a second enemy type in the east room

## Context

WISH-001: Hollow Knight–inspired exploration, still top-down. Room 2 is an
empty box. The doorway needs a reason: a second insect-like foe, tougher than
the first, waiting east of the gap. No chase AI, no third type, no boss.

## Acceptance Criteria

- [x] A second enemy type exists (distinct scene/script from the room-1 insect)
- [x] That foe is placed in the second room
- [x] It takes two nail hits to despawn (the first-room insect still takes one)
- [x] Touching it still damages the player
- [x] WASD, J-nail, HP, doorway, and the first-room enemy still work
- [x] Tests check the new type, two-hit wiring, and Room 2 placement
- [x] README notes two enemy types
- [x] Tests pass

## Notes

- Do not add chase, loot, a health bar, or a third enemy type
- Keep top-down; do not clone a Hollow Knight enemy
- Visual difference (size/color) is enough to read as a new type
