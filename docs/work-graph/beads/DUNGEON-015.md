---
id: DUNGEON-015
title: Establish the original dark-fantasy visual language
status: done
dependencies: []
assignee: agent
---

# DUNGEON-015: Establish the original dark-fantasy visual language

## Context

WISH-003 asks for a fresh, polished look. The first pass replaces flat
placeholder rectangles with a cohesive visual language before lighting and
outdoor depth are layered on top.

The direction is original inked dark fantasy: moonlit blue-black stone,
oxidized teal, warm tarnished gold, and restrained ember accents. Hollow
Knight and Elden Ring are mood references only.

## Acceptance Criteria

- [x] `examples/dark-dungeon/docs/visual-direction.md` defines palette, shape language, hierarchy, and anti-copy constraints
- [x] Player, three regular foes, warden, shrine, seal, shard, and nail use authored visual assets rather than flat placeholder rectangles
- [x] Interior floors and walls gain readable material detail and room-to-room variation
- [x] Existing collision shapes, controls, combat, upgrades, and progression remain unchanged
- [x] Player, enemies, pickups, and exits remain legible against the environment
- [x] Dark Dungeon tests pass

## Notes

- No indoor light/shadow system in this bead (DUNGEON-016)
- No outdoor area in this bead (DUNGEON-017)
- Prefer original vector assets committed as text; do not copy reference-game designs
