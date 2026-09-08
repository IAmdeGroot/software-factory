---
id: DUNGEON-016
title: Add dramatic interior lighting and shadows
status: ready
dependencies:
  - DUNGEON-015
assignee: null
---

# DUNGEON-016: Add dramatic interior lighting and shadows

## Context

WISH-003 asks for beautiful effects indoors. With the visual language in
place, the dungeon can use Godot 4's 2D lighting to create pools of warmth,
cool ambient darkness, cast shadows, glow, and subtle environmental motion.

## Acceptance Criteria

- [ ] Interior rooms use a controlled ambient-darkness treatment
- [ ] At least three authored light sources create distinct pools of warm/cool light
- [ ] Walls or props cast visible 2D shadows without hiding collision boundaries
- [ ] Shrine, seal, and warden spaces each have a distinct lighting beat
- [ ] Subtle motes, haze, or glow add motion without obscuring combat
- [ ] Lighting and effects do not change gameplay behavior
- [ ] Dark Dungeon tests pass and the project opens without Godot errors

## Notes

- Keep player and enemy silhouettes readable
- Do not add the outdoor area here
- Prefer a small reusable light texture/effect over per-room duplication
