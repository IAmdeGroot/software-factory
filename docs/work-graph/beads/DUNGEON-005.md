---
id: DUNGEON-005
title: Add one strikeable enemy in the room
status: ready
dependencies:
  - DUNGEON-004
assignee: null
---

# DUNGEON-005: Add one strikeable enemy in the room

## Context

WISH-001: Hollow Knight–inspired feel. A nail with nothing to hit is still
an empty room. One insect-like foe that dies when the nail connects makes
melee real and gives playtest wishes a target.

## Acceptance Criteria

- [ ] One enemy exists in the main room (simple 2D body + visible shape)
- [ ] The player's melee hitbox can defeat or despawn that enemy
- [ ] The enemy does not need to chase; idle or slow wander is enough
- [ ] The player can still move and attack after the enemy is gone
- [ ] A test checks enemy scene wiring and that the player attack can hit it
- [ ] README notes there is one enemy in the starting room
- [ ] Tests pass

## Notes

- No health bars, no three enemy types, no boss
- Keep the look insect-adjacent (silhouette/color), not a Knight sprite
- No pogo, spells, or geo drops in this bead
