# Dark Dungeon (Example Product)

> This is the **live product** the software factory is bonded to. The harness grows because this game needs it.

## Concept

A 2D top-down action RPG / roguelite, **inspired by Hollow Knight** (nail-like melee, lonely insect-ruin mood) without becoming a side-scrolling clone. See `docs/feel.md`.

- Explore dungeons
- Fight monsters
- Find weapons and abilities
- Gain power
- Fight bosses

## Run

Requires [Godot 4.3+](https://godotengine.org/download/) (4.x). The Godot binary is not required for the scaffold file tests.

1. Open Godot 4 → Import → select `examples/dark-dungeon/project.godot`
2. Press Play (F5). Play starts in a **bounded room** with **one idle insect-like enemy**. Move with **WASD** or the **arrow keys**. Swing a short **nail** with **J** to strike and despawn the enemy.

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

Scaffold, movement, a bounded room, nail-like melee, and one strikeable enemy are in (`DUNGEON-001`–`DUNGEON-005`).

## Why This Example

Small enough to iterate quickly, fun enough to care about, complex enough to grow a Wish Factory around playtest and design wishes.
