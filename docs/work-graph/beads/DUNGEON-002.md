---
id: DUNGEON-002
title: Add four-way player movement
status: done
dependencies:
  - DUNGEON-001
assignee: agent
---

# DUNGEON-002: Add four-way player movement

## Context

The first playable increment is a character that moves on a 2D plane.
That is enough to open the project and see the factory producing game
behavior, not just config files.

## Acceptance Criteria

- [x] A player node exists in the main scene (CharacterBody2D or equivalent)
- [x] WASD and arrow keys move the player in four directions
- [x] Movement is visible in the Godot 4 2D main scene
- [x] A test checks the player script and scene wiring exist
- [x] README notes the movement keys
- [x] Tests pass

## Notes

- No combat, enemies, or camera follow in this bead
- Keep speed as a simple exported or constant value
