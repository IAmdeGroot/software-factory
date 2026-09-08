---
id: DUNGEON-017
title: Add an outdoor approach with atmospheric depth
status: in_progress
dependencies:
  - DUNGEON-016
assignee: agent
---

# DUNGEON-017: Add an outdoor approach with atmospheric depth

## Context

WISH-003 asks for a clear sense of depth outdoors. Dark Dungeon currently has
only interior rooms, so this pass adds a small reachable exterior approach
that demonstrates the finished outdoor language without expanding combat or
quest scope.

## Acceptance Criteria

- [x] A reachable outdoor approach connects to the existing first room
- [x] At least three background depth planes use scale, value, fog, or parallax to separate near/mid/far space
- [x] Foreground silhouettes and atmospheric motion frame the playable path without blocking it
- [x] Outdoor lighting is visibly different from interior lighting while retaining the same palette
- [x] The doorway transition clearly reads as outside versus inside
- [x] Existing three-room progression remains intact
- [x] Dark Dungeon tests pass and the project opens without Godot errors

## Notes

- No new enemy, loot, or progression mechanic
- Keep the outdoor slice compact; this is a visual proof, not a new dungeon
- Preserve top-down movement and original dark-fantasy identity
