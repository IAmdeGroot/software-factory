---
id: DUNGEON-010
title: Add shard loot when a foe dies
status: in_progress
dependencies:
  - DUNGEON-009
assignee: agent
---

# DUNGEON-010: Add shard loot when a foe dies

## Context

WISH-001: Hollow Knight–inspired, still top-down. First playable scope includes
basic loot. Combat currently leaves nothing on the floor. A shard that drops
when a foe dies, picked up by walking over it, is the collect verb. No shop,
no geo wallet art, no spending.

## Acceptance Criteria

- [ ] Defeating a foe drops a visible shard on the floor
- [ ] Walking over a shard collects it (the shard despawns)
- [ ] The player has a visible shard count
- [ ] Shards persist through respawn (HP still resets)
- [ ] WASD, J-nail, HP, rooms, and all three foe types still work
- [ ] Tests check drop, pickup, and count wiring
- [ ] README notes shards drop from foes
- [ ] Tests pass

## Notes

- Do not add a shop, charms, or a spend sink
- Do not name it geo or copy Hollow Knight HUD art
- Crawler drops only on the killing hit
