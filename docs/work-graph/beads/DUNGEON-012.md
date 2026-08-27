---
id: DUNGEON-012
title: Add a seal that only a honed nail can break
status: done
dependencies:
  - DUNGEON-011
assignee: agent
---

# DUNGEON-012: Add a seal that only a honed nail can break

## Context

WISH-001: rooms that ask you to come back with a new move. The hone is that
move. Room 2's east wall is a dead end. A seal that ignores an unhoned nail
and yields to a honed one opens a third room. Not a map, not a boss.

## Acceptance Criteria

- [x] Room 2's east wall has a visible seal blocking a gap
- [x] An unhoned nail does not break the seal
- [x] A honed nail (damage 2) breaks the seal
- [x] A third bounded room exists beyond the seal
- [x] The player can walk into that room after the seal is gone
- [x] WASD, shrine, shards, and existing foes still work
- [x] Tests check seal threshold, room 3 walls, and placement
- [x] README notes the honed-nail seal
- [x] Tests pass

## Notes

- Do not add a boss, map, or key item in this bead
- Keep top-down; do not copy a Hollow Knight gate art
- Unhoned swings should fail quietly (no extra UI)
