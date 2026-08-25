# Dark Dungeon (Example Product)

> This is a **sample product** built by the software factory — not the factory itself.

## Concept

A 2D top-down action RPG / roguelite.

- Explore dungeons
- Fight monsters
- Find weapons and abilities
- Gain power
- Fight bosses

## Run

Requires [Godot 4.3+](https://godotengine.org/download/) (4.x). The Godot binary is not required for the scaffold file tests.

1. Open Godot 4 → Import → select `examples/dark-dungeon/project.godot`
2. Press Play (F5). The main scene is an empty 2D view until player movement lands (DUNGEON-002).

```bash
# Scaffold checks (no Godot binary needed)
python3 -m unittest discover -s examples/dark-dungeon/tests -v
```

## First Playable Scope

- Player movement
- Melee combat
- 3 enemy types
- One dungeon
- Basic loot
- Character progression
- One boss
- Basic UI

## Technology

- **Godot 4** — 2D
- Data-driven enemy/item definitions (later beads)
- Fast iteration over content volume

## Status

Scaffold complete (`DUNGEON-001`). Next: four-way player movement (`DUNGEON-002`).

## Why This Example

Small enough to iterate quickly, fun enough to care about, complex enough to stress-test the factory's agent loop.
