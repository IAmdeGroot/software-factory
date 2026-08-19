# Software Factory

A harness for **harnessed agentic engineering** — AI agents that plan, implement, test, and review software with minimal human micromanagement.

## Quick Start

1. Read `context.md` and `AGENTS.md`
2. Pick a ready bead from `docs/work-graph/beads/`
3. In Cursor Agent, say: **"Claim and implement FACTORY-001"**
4. Agent follows the plan → implement → verify → review loop
5. Update the bead status when done

## Structure

```text
software-factory/
├── AGENTS.md              # Agent operating contract
├── context.md             # Factory vision and mental model
├── docs/
│   ├── brain/             # Persistent project knowledge
│   └── work-graph/beads/  # Work items (beads)
├── harness/               # Factory orchestration code
├── examples/              # Sample products built by the factory
└── .cursor/
    ├── rules/             # Persistent Cursor rules
    └── skills/            # Reusable agent workflows
```

## First Milestone

Planner creates beads → worker claims one → implements → tests → updates bead.

## Sample Product

`examples/dark-dungeon/` — a 2D roguelite used to stress-test the factory. Not the factory itself.
