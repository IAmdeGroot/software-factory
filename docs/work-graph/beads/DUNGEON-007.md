---
id: DUNGEON-007
title: Add a doorway to a second room
status: in_progress
dependencies:
  - DUNGEON-006
assignee: agent
---

# DUNGEON-007: Add a doorway to a second room

## Context

WISH-001: Hollow Knight–inspired exploration, not a Hallownest map. One
room is a box. A doorway into a second bounded room is the next verb:
you walk somewhere. No mini-map, stag, or ability gate.

## Acceptance Criteria

- [x] The starting room has a visible doorway (a gap in a wall)
- [x] A second bounded room exists beyond that doorway
- [x] The player can walk from one room into the other
- [x] A camera follows the player so the second room is on-screen
- [x] WASD, J-nail, HP, and the first-room enemy still work
- [x] Tests check doorway, second-room walls, and camera wiring
- [x] README notes two rooms connected by a doorway
- [x] Tests pass

## Notes

- Do not add a map, loading screen, or locked door
- Keep top-down; two rooms in one scene is enough
- No new enemy type in this bead
