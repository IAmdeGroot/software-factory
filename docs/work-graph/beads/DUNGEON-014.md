---
id: DUNGEON-014
title: Show a clear beat when the warden falls
status: in_progress
dependencies:
  - DUNGEON-013
assignee: agent
---

# DUNGEON-014: Show a clear beat when the warden falls

## Context

WISH-001: Hollow Knight–inspired, still top-down. First playable now has a
boss, but killing it is silent. A short on-screen "Cleared" after the warden
falls is the win beat. No credits, no map, no title screen.

## Acceptance Criteria

- [ ] Defeating the warden reveals a visible "Cleared" message in room 3
- [ ] The message is hidden until the warden falls
- [ ] WASD, nail, shrine, seal, shards, and other foes still work
- [ ] Tests check the label and the warden revealing it
- [ ] README notes the clear beat
- [ ] Tests pass

## Notes

- Do not add a title screen, credits, or a save
- Keep top-down; do not copy a Hollow Knight ending
- The player can still walk around after the message
