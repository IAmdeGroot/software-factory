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
- **Python or Node** — harness scripts (TBD in FACTORY-002)
- **GitHub** — remote repository (optional, add when ready)

## Evolution Path

1. Manual bead loop in Cursor chat (now)
2. Harness scripts for bead status and ready-queue (FACTORY-003)
3. Cursor hooks for post-edit checks
4. Cursor automations for PR review / CI triage
5. Optional: Cursor SDK for programmatic agent runs
