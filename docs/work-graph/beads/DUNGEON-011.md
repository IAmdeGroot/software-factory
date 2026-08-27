---
id: DUNGEON-011
title: Add a nail shrine that spends shards
status: in_progress
dependencies:
  - DUNGEON-010
assignee: agent
---

# DUNGEON-011: Add a nail shrine that spends shards

## Context

WISH-001: Hollow Knight–inspired, still top-down. Shards currently have nowhere
to go. A shrine in the first room that hones the nail for two shards is both a
spend sink and a reason to walk back through the doorway. Not a bench, not a
shop list, not a map.

## Acceptance Criteria

- [ ] A shrine exists in the first room
- [ ] Walking into it with enough shards spends them and strengthens the nail
- [ ] Without enough shards, or after it has already honed, it does nothing
- [ ] A honed nail defeats the two-hit crawler in one swing
- [ ] Nail upgrade and remaining shards survive respawn
- [ ] Tests check shrine wiring, cost, and nail damage
- [ ] README notes the shrine and the walk-back
- [ ] Tests pass

## Notes

- Do not add a shop UI, charms, or geo naming
- Keep top-down; do not add a bench or soul
- Cost of two shards is enough; do not require a full clear
