---
id: DUNGEON-001
title: Add Godot 4 project scaffold
status: ready
dependencies:
  - FACTORY-018
assignee: null
---

# DUNGEON-001: Add Godot 4 project scaffold

## Context

The factory loop is closed. Dark Dungeon is the example product used to
stress-test that loop. It needs a Godot 4 2D project under `examples/dark-dungeon/`
so later beads can add a player and a room.

## Acceptance Criteria

- [ ] `examples/dark-dungeon/project.godot` is a Godot 4 project named Dark Dungeon
- [ ] A main 2D scene is set as the run scene
- [ ] README documents how to open and run the project in Godot 4
- [ ] A test checks the required project files exist
- [ ] `.godot/` is gitignored
- [ ] Decision log records Godot 4 2D for this example

## Notes

- Keep the scaffold empty of gameplay
- Do not add combat, loot, or a dungeon map in this bead
- Godot may not be installed in every environment; the file-existence test must pass without the Godot binary
