---
id: DUNGEON-004
title: Add nail-like melee in the facing direction
status: done
dependencies:
  - DUNGEON-003
assignee: agent
---

# DUNGEON-004: Add nail-like melee in the facing direction

## Context

WISH-001: Hollow Knight–inspired feel. The first borrow is the **nail**: a
short, committed melee in the direction the player last moved. Dark Dungeon
stays top-down; this is not a side-view slash.

## Acceptance Criteria

- [x] The player remembers a facing direction from movement (including idle)
- [x] An attack input (keyboard; document the key in the README) swings a
      short-range hitbox in that facing direction
- [x] The swing has a brief recover so it cannot be a hold-to-spam beam
- [x] WASD / arrows still move the player in the bounded room
- [x] A test checks attack/facing wiring in the player script and scene
- [x] README notes the attack key and Hollow Knight–inspired melee
- [x] Tests pass

## Notes

- No enemy, damage numbers, or camera follow in this bead
- Keep the hitbox a simple Area2D or equivalent; no sprite sheet required
- Do not switch the game to a side-scroller
