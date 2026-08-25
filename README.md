# Software Factory

A harness for **harnessed agentic engineering** — AI agents that plan, implement, test, and review software with minimal human micromanagement.

## Quick Start

1. Read `context.md` and `AGENTS.md`
2. Pick a ready bead from `docs/work-graph/beads/`
3. In Cursor Agent, say: **"Claim and implement FACTORY-001"**
4. Agent follows the plan → implement → verify → review loop
5. Update the bead status when done

Unattended: say **"Implement the next ready bead"** (commit, push, one PR, do not merge). Review: **"Review the next bead"**. CI failures: `.cursor/automations/ci-triage.md`.

One bead = one branch = one PR. Base is the repository default branch. Humans merge using `.cursor/automations/land.md` (bead `done`, CI green). Integration branch is `main`.

## Structure

```text
software-factory/
├── AGENTS.md              # Agent operating contract
├── context.md             # Factory vision and mental model
├── docs/
│   ├── brain/             # Persistent project knowledge
│   └── work-graph/
│       ├── beads/         # Work items (beads)
│       └── wishes/        # Wish drop (FACTORY-020)

├── harness/               # Factory orchestration code
├── examples/              # Sample products built by the factory
└── .cursor/
    ├── rules/             # Persistent Cursor rules
    └── skills/            # Reusable agent workflows
```

## First Milestone

That loop exists. Next: **Wish Factory** — drop a wish, planner makes beads, workers implement. Dark Dungeon grows in parallel. Do not build Gas Town.

GitHub Actions runs harness tests and bead validation on every push and pull request.

## Sample Product

`examples/dark-dungeon/` — the live product the factory is bonded to. A 2D roguelite used to grow the harness.
