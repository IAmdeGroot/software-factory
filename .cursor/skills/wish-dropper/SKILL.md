---
name: wish-dropper
description: Transcribe sourced intent into open wish files. Use when the user says "Drop wishes from this intent", "create a wish", or when turning a chat or playtest note into WISH-NNN.md.
---

# Wish Dropper

A wish is intent on disk. Use this skill to write `open` wish files from a
**source**. Do **not** invent wishes. Do **not** convert them into beads. Do
**not** claim beads or start workers.

## Unattended prompt

`Drop wishes from this intent`

## Steps

1. **Require a source**
   - Human chat that states a want, need, or product/factory gap
   - A playtest note the human pointed at
   - A named gap in `docs/brain/` or `examples/*/docs/` the human asked to capture
   - If there is no source, **stop**. No source / nothing to drop means stop; do not invent wishes.

2. **Allocate an id**
   - Run `python -m harness.beads next-wish-id`
   - Use that id as `WISH-NNN.md` under `docs/work-graph/wishes/`

3. **Write the wish**
   - YAML frontmatter: `id`, `title`, `status: open`, `source` (`human`, `playtest`, or a short label)
   - Body: the intent in the human's words, plus only enough context to plan later
   - One distinct intent per file; if the human named several, write several ids in order

4. **Stop**
   - Do not run the wish-planner
   - Do not `claim` or `next`
   - Do not implement the wished feature
   - An empty ready queue is not a reason to invent a wish

## Output Format

```markdown
## Dropped WISH-NNN — [title]

**Source:** human | playtest | [label]
**Open wishes:** [count]
**Next:** Convert open wishes into beads (human or planner). Not this skill.
```
