---
id: DUNGEON-017
title: Add an outdoor approach with atmospheric depth
status: ready
dependencies:
  - DUNGEON-016
assignee: null
---

# DUNGEON-017: Add an outdoor approach with atmospheric depth

## Context

WISH-003 asks for a clear sense of depth outdoors. Dark Dungeon currently has
only interior rooms, so this pass adds a small reachable exterior approach
that demonstrates the finished outdoor language without expanding combat or
quest scope.

## Acceptance Criteria

- [ ] A reachable outdoor approach connects to the existing first room
- [ ] At least three background depth planes use scale, value, fog, or parallax to separate near/mid/far space
- [ ] Foreground silhouettes and atmospheric motion frame the playable path without blocking it
- [ ] Outdoor lighting is visibly different from interior lighting while retaining the same palette
- [ ] The doorway transition clearly reads as outside versus inside
- [ ] Existing three-room progression remains intact
- [ ] Dark Dungeon tests pass and the project opens without Godot errors

## Notes

- No new enemy, loot, or progression mechanic
- Keep the outdoor slice compact; this is a visual proof, not a new dungeon
- Preserve top-down movement and original dark-fantasy identity
