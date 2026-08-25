# Factory Architecture

## Overview

```text
                         HUMAN
                           │
                 vision / decisions
                           │
                           ▼
                    PROJECT BRAIN
                     docs/brain/
                           │
                           ▼
                        PLANNER
                     (Cursor Agent)
                           │
                           ▼
                     WORK GRAPH
                  docs/work-graph/beads/
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             WORKER A             WORKER B
           (Cursor Agent)       (future)
                 │                   │
                 └─────────┬─────────┘
                           ▼
                       REVIEW
                           │
                           ▼
                          QA / TESTS
                           │
                           ▼
                      MERGE / BUILD
                           │
                           ▼
                      MONITORING
                           │
                           ▼
                    NEW WORK / BUGS
                           │
                           └──────────→ WORK GRAPH
```

## Repository Layout

| Path | Purpose |
|------|---------|
| `docs/brain/` | Persistent knowledge (vision, architecture, decisions) |
| `docs/work-graph/beads/` | Structured work items with deps and acceptance criteria |
| `harness/` | Factory orchestration scripts and automation |
| `examples/` | Sample products built to test the factory |
| `products/` | Future: real products the factory builds |
| `.cursor/rules/` | Persistent agent behavior rules |
| `.cursor/skills/` | Reusable workflow playbooks |

## Bead Format

Each bead is a markdown file with YAML frontmatter:

```yaml
---
id: FACTORY-001
title: Short descriptive title
status: ready          # ready | in_progress | review | done | blocked
dependencies: []       # list of bead IDs
assignee: null         # agent or human name
---
```

Followed by: context, acceptance criteria, and notes.

## Technology (v0)

- **Cursor Pro** — AI agents (planner, worker, reviewer)
- **Git** — source control, one bead per branch
- **Markdown** — project brain and work graph
- **Python** — harness scripts (stdlib, `python -m harness.beads`)
- **GitHub** — remote repository (optional, add when ready)

## Evolution Path

1. Manual bead loop in Cursor chat
2. Harness scripts for bead status and ready-queue (FACTORY-003) — done
3. Cursor hooks for post-edit checks (FACTORY-006) — done
4. Status transitions, next-bead pull, CI watch, unattended worker recipe (Milestone 3) — done
5. Review queue, reviewer skill, PR-review and CI-triage recipes (Milestone 4) — done
6. Worker PR + reviewer ready-for-review + human land recipe (Milestone 5)
7. Optional: Cursor SDK for programmatic agent runs

Product examples stay in `examples/` and start only after the land loop exists so work can actually merge. Dark Dungeon remains deferred through Milestone 5.
