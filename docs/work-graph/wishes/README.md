# Wishes

Drop intent here. A wish is not work until a planner turns it into beads.

Prompt: **Drop wishes from this intent** (`.cursor/skills/wish-dropper/SKILL.md`).
Needs a source (human chat, playtest note). No source / nothing to drop means
stop; do not invent wishes.

Then: **Convert open wishes into beads** (`.cursor/skills/wish-planner/SKILL.md`).
Empty wish list means stop; do not invent wishes.

## File format

`WISH-NNN.md` with YAML frontmatter:

```yaml
---
id: WISH-001
title: Short description
status: open          # open | planned | done
source: human         # human | playtest | or any short source label
beads:                # required when status is planned
  - DUNGEON-004
---
```

Game work uses `DUNGEON-` beads; harness work uses `FACTORY-`.

## Commands

```bash
python -m harness.beads wishes
python -m harness.beads wishes --json
python -m harness.beads next-wish-id
python -m harness.beads next-wish-id --json
python -m harness.beads validate   # also validates WISH-*.md
```

Empty drop is fine. Do not invent wishes when listing finds none.
