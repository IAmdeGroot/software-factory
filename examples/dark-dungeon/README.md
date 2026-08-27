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
2. Press Play (F5). Play starts in a **bounded room** with a **nail shrine** (west) and **one idle insect**. An **east doorway** leads to a **second room** with a **two-hit crawler** and a **patrolling skitter**. Room 2's east wall has a **seal**: an unhoned nail does nothing; a **honed nail** breaks it and opens a **third room** with a **warden** (six HP, three honed swings, slow patrol). Move with **WASD** or the **arrow keys**. Swing a short **nail** with **J**. **Touching an enemy costs a hit** (three hits, then you respawn in the first room). Defeated foes drop a **shard**; walk over it to collect. Carry **two shards** back to the shrine to **hone the nail**. Shards and the hone survive respawn.

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

Three rooms, honed-nail seal, shrine, three foe types plus a room-3 warden, shard loot, three HP (`DUNGEON-001`–`DUNGEON-013`). Inspired by Hollow Knight exploration, not a Hallownest map.

## Why This Example

Small enough to iterate quickly, fun enough to care about, complex enough to grow a Wish Factory around playtest and design wishes.
