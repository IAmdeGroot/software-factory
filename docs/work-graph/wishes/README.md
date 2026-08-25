# Wishes

Drop intent here. A wish is not work until a planner turns it into beads
(`FACTORY-021`).

## File format

`WISH-NNN.md` with YAML frontmatter:

```yaml
---
id: WISH-001
title: Short description
status: open          # open | planned | done
source: human         # human | playtest | or any short source label
---
```

## Commands

```bash
python -m harness.beads wishes
python -m harness.beads wishes --json
python -m harness.beads validate   # also validates WISH-*.md
```

Empty drop is fine. Do not invent wishes when listing finds none.
