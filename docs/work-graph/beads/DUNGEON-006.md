---
id: DUNGEON-006
title: Add enemy contact damage and player hit points
status: done
dependencies:
  - DUNGEON-005
assignee: agent
---

# DUNGEON-006: Add enemy contact damage and player hit points

## Context

WISH-001: Hollow Knight–inspired, not a clone. The nail can already kill the
idle bug for free. Combat needs stakes: touching the foe hurts, you have a
few hits, then the room puts you back. No masks UI, soul, shade, or bench.

## Acceptance Criteria

- [x] Touching the enemy damages the player
- [x] The player has a small hit-point count (three is enough) that is visible
- [x] A brief invulnerability window after a hit so contact is not instant death
- [x] At zero HP the player respawns in the starting room with HP restored
- [x] WASD, J-nail, and walls still work
- [x] Tests check contact-damage and HP/respawn wiring
- [x] README notes that the enemy hurts on contact and that you have a few hits
- [x] Tests pass

## Notes

- Do not add pogo, soul, charms, shade, or a bench
- Keep top-down; do not copy Hollow Knight's mask HUD art
- Enemy can stay idle; chase is out of scope
