---
id: DUNGEON-003
title: Add a bounded room the player cannot walk out of
status: ready
dependencies:
  - DUNGEON-002
assignee: null
---

# DUNGEON-003: Add a bounded room the player cannot walk out of

## Context

Movement on an empty plane is not a place. A single bounded room gives
Dark Dungeon a surface that can generate wishes (walls, doors, lighting)
and keeps the harness bonded to the product instead of more factory
markdown.

## Acceptance Criteria

- [ ] The main 2D scene has a visible room (walls or tile bounds)
- [ ] The player cannot walk out of the room
- [ ] The player still moves with WASD and arrow keys inside the room
- [ ] A test checks room/collision wiring exists
- [ ] README notes that play starts in a bounded room
- [ ] Tests pass

## Notes

- No combat, enemies, doors, or camera follow in this bead
- Keep geometry simple (static collision), not a generated dungeon
