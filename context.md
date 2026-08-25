# Project Context — Software Factory

## Purpose

This project **is** the software factory: a harness for harnessed agentic engineering.

AI agents plan, implement, test, review, and maintain software. The human provides high-level intent, architectural decisions, and taste. The harness is chemically bonded to the products it builds — today that product is Dark Dungeon under `examples/dark-dungeon/`. We are not building a reusable Gas Town.

See `docs/brain/vision.md` for the current north star (Wish Factory).

---

## Core Concept

**AI-assisted coding**
- Human talks to an AI coding agent.
- Human gives tasks one at a time.
- Human continuously directs the implementation.

**Harnessed agentic engineering**
- Human provides high-level goals and constraints.
- A planning system creates structured work.
- Agents pull available work themselves.
- Agents implement, test, review, and update work state.
- Agents can discover and create new work.
- The work graph evolves as the project evolves.
- Humans intervene mainly when a decision genuinely requires human judgment.

## End State

```text
Human
  ↓
Vision / requirements / decisions
  ↓
Project brain
  ↓
Planner
  ↓
Work graph
  ↓
Worker agents
  ↓
Testing / review / QA
  ↓
Merge / build
  ↓
Monitoring
  ↓
New work discovered
  ↓
Work graph
```

---

## Three Layers (keep separate)

### Project brain — `docs/brain/`

> What does the project know?

Persistent knowledge and guidance for agents.

### Work graph — `docs/work-graph/beads/`

> What needs to be done?

Structured work items with dependencies, status, and acceptance criteria.
Each bead is one executable unit (like an issue, but agent-native).

### Source code — `harness/`, `examples/`, `products/`

> What has actually been built?

---

## Agent Workflow

For a bead such as:

```text
ID: FACTORY-003
Title: Add bead status CLI script
Dependencies: FACTORY-002
Acceptance criteria:
- Script lists all beads and their status
- Script shows which beads are ready (deps satisfied)
- Tests pass
```

A worker agent:

1. Claims the bead
2. Reads relevant brain docs
3. Inspects related code
4. Implements the feature
5. Runs tests
6. Commits work
7. Updates the bead
8. Requests or triggers review
9. Marks complete

The agent should not need the entire conversational history with the human.

---

## Human Role

The human provides:

- Product vision and creative direction
- High-level requirements
- Architecture principles
- Important trade-off decisions
- Quality expectations

The human should **not** normally specify every file, function, or implementation step.

---

## "Crons Watch, Models Act"

Deterministic systems watch for events; AI acts when intelligence is required.

```text
Cron / webhook / monitor → something changed → reasoning required? → wake agent
```

Do not keep expensive AI agents running continuously just waiting.

---

## Cost Philosophy

Target: **Cursor Pro ($20/mo) + free/local tooling** unless a paid service is clearly necessary.

Optimize for **useful work per dollar**. Start with a sequential or small-fleet system.

---

## First Milestone

> A planner creates a few beads, a worker autonomously picks one up, implements it, tests it, and updates the bead.

That loop exists. Next: wishes feed the graph, and Dark Dungeon generates more of them.

## Wish Factory

A **wish** is intent (human, playtest, later intake). A **bead** is executable work with acceptance criteria. Unattended workers pull beads; they do not invent work when the ready queue is empty. A planner turns open wishes into beads.
