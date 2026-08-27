---
id: DUNGEON-008
title: Add a second enemy type in the east room
status: in_progress
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

- [ ] A second enemy type exists (distinct scene/script from the room-1 insect)
- [ ] That foe is placed in the second room
- [ ] It takes two nail hits to despawn (the first-room insect still takes one)
- [ ] Touching it still damages the player
- [ ] WASD, J-nail, HP, doorway, and the first-room enemy still work
- [ ] Tests check the new type, two-hit wiring, and Room 2 placement
- [ ] README notes two enemy types
- [ ] Tests pass

## Notes

- Do not add chase, loot, a health bar, or a third enemy type
- Keep top-down; do not clone a Hollow Knight enemy
- Visual difference (size/color) is enough to read as a new type
