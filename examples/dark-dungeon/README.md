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
2. Press Play (F5). Play starts in a **bounded room** with a **nail shrine**
   and **one idle insect**. Go west into a moonlit **outdoor approach** with
   layered ruins, cliff silhouettes, fog, and foreground roots. An **east
   doorway** leads to a **second room** with a **two-hit crawler** and a
   **patrolling skitter**. Room 2's east wall has a **seal**: an unhoned nail
   does nothing; a **honed nail** breaks it and opens a **third room** with a
   **warden** (six HP, three honed swings, slow patrol). Defeat the warden to
   see **Cleared**. Move with **WASD** or the **arrow keys**. Swing a short
   **nail** with **J**. **Touching an enemy costs a hit** (three hits, then you
   respawn in the first room). Defeated foes drop a **shard**; walk over it to
   collect. Carry **two shards** back to the shrine to **hone the nail**.
   Shards and the hone survive respawn.

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
- Original SVG character/prop art with an ink-and-patina dark-fantasy palette
- Data-driven enemy/item definitions (later beads)
- Fast iteration over content volume

## Status

First playable loop is in: three rooms, hone, seal, warden, and a **Cleared**
beat (`DUNGEON-001`–`DUNGEON-014`). The placeholder blocks are replaced by
an original drowned-reliquary visual language (`DUNGEON-015`). Inspired by
Hollow Knight exploration, not a Hallownest map. Interiors now use cool
ambient darkness, warm/cool light pools, cast shadows, pulsing sacred light,
and drifting motes (`DUNGEON-016`). The west exit now opens onto a moonken
terrace with far spires, ruined arches, cliff depth, fog, and foreground
silhouettes (`DUNGEON-017`).

## Why This Example

Small enough to iterate quickly, fun enough to care about, complex enough to grow a Wish Factory around playtest and design wishes.
