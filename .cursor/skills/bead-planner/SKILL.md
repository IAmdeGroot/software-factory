---
name: bead-planner
description: Create new beads from a vision or goal document. Use when planning work, breaking down a feature, or when the user asks to create beads or plan a milestone.
---

# Bead Planner

Use this skill to break a goal into structured beads.

## Input

- A vision doc, feature description, or human goal statement
- Existing beads (read `docs/work-graph/backlog.md` to avoid duplicates)

## Output

One markdown file per bead in `docs/work-graph/beads/`, plus an updated `backlog.md`.

## Bead Template

```markdown
---
id: FACTORY-NNN
title: Short descriptive title
status: ready
dependencies:
  - FACTORY-NNN  # if any
assignee: null
---

# FACTORY-NNN: Title

## Context

Why this work exists and what it enables.

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Tests pass

## Notes

Optional implementation hints or constraints.
```

## Planning Rules

1. Each bead should be completable in one agent session (~1-2 hours of work)
2. Define dependencies explicitly — only mark `ready` if deps are satisfied
3. First bead in a chain should have `dependencies: []`
4. Include test-related criteria in every bead
5. Use `FACTORY-` prefix for factory work, product-specific prefix for product work
6. Update `docs/work-graph/backlog.md` after creating beads

## After Planning

Present a summary:

```markdown
## New Beads Created

| ID | Title | Ready? | Depends on |
|----|-------|--------|------------|
| FACTORY-00X | ... | yes/no | ... |

**Suggested first bead:** FACTORY-00X
```

Ask human to confirm before agents start working.
