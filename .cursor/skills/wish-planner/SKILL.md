---
name: wish-planner
description: Convert open wishes into beads with acceptance criteria. Use when the user says "Convert open wishes into beads", "Plan the next open wish", or when turning wish drop files into work-graph beads.
---

# Wish Planner

A wish is intent. A bead is executable work. Use this skill to turn `open`
wishes into beads. Do **not** implement the wished feature. Do **not** claim
beads or start workers.

## Unattended prompt

`Convert open wishes into beads`

When no wish id is given:

1. Run `python -m harness.beads wishes`
2. Empty wish list means stop; do not invent wishes. Do not create beads. Do not start product work.
3. Otherwise convert the first open wish (stable id order) below.

## Steps

1. **Select the wish**
   - Named id: use that wish if its status is `open`
   - Otherwise: first id from `python -m harness.beads wishes`

2. **Read context**
   - The wish file in `docs/work-graph/wishes/`
   - `docs/work-graph/backlog.md` and existing beads (avoid duplicates)
   - Relevant `docs/brain/` docs
   - Product code under `examples/` or `products/` only to size the beads

3. **Split into beads**
   - One bead = one PR-sized change with acceptance criteria
   - One wish may become several beads; chain them with `dependencies`
   - Prefix: `DUNGEON-` for Dark Dungeon / game work, `FACTORY-` for harness work
   - Next unused id in that prefix (three digits, matching existing files)
   - Use the bead template in `.cursor/skills/bead-planner/SKILL.md`
   - If the wish needs an architecture decision not in `docs/brain/decisions.md`, stop and escalate to the human instead of inventing a fork

4. **Mark the wish planned**
   - Set `status: planned`
   - Set `beads:` to the new bead ids (YAML list)
   - Run `python -m harness.beads sync-backlog`
   - Run `python -m harness.beads validate`

5. **Stop**
   - Do not `claim` or `next`
   - Do not implement the beads
   - Human still confirms large scope before workers pull

## Output Format

```markdown
## Planned WISH-NNN — [title]

**Beads:** [id list]
**Prefix:** DUNGEON | FACTORY
**Ready now:** [first bead id or none]
**Human needed:** [yes/no — why]
```
