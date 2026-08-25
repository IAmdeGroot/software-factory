# Factory Vision

## What We Are Building

A **software factory** — a harness that lets AI agents plan, implement, review, and land software from high-level human intent.

The harness is chemically bonded to the products it builds. Dark Dungeon is the live product that grows the factory. Games, apps, and tools are not afterthoughts; a reusable Gas Town is not the goal.

## Principles

1. **Human provides intent, agents execute routine work**
2. **Three layers stay separate**: brain (knowledge), work graph (tasks), source code (artifacts)
3. **Work graph is living**, not a static upfront plan
4. **Small increments**: one bead, one branch, one reviewable change
5. **Playable/testable at every milestone** — for both factory features and example products
6. **Cost-conscious**: Cursor Pro + free tooling; crons watch, models act
7. **Learn by doing**: start minimal, add complexity only when a real bottleneck appears

## Success Criteria (v0)

Factory loop first — no product work until these are checked:

- [x] Planner agent can create beads from a vision doc
- [x] Worker agent can claim a ready bead and implement it without step-by-step human guidance
- [x] Bead status is updated by harness commands after work completes (`complete` / `done`)
- [x] A worker can pull the next ready bead without being told which one (`next`)
- [x] Deterministic CI watches harness tests and bead validity
- [x] Documented unattended loop: skill + Cursor automation recipe, empty queue means stop

## Milestone 4 (after v0 worker loop)

Review and CI triage so work does not stall at `review` waiting for a chat message:

- [x] Reviewer can list beads in `review` (`review-queue`)
- [x] Reviewer skill can accept (`done`) or reject with failing criteria
- [x] Documented PR-review automation recipe
- [x] Documented CI-triage automation recipe

Humans still merge pull requests. Dark Dungeon stays deferred.

## Milestone 5 (land loop)

Work must be able to reach the integration branch without a pile of forgotten drafts:

- [x] Worker commits, pushes, and opens one PR per bead
- [x] Reviewer marks that PR ready after `done` (still does not merge)
- [x] Documented human land/merge recipe; integration branch is `main`

Dark Dungeon stays deferred until this land loop exists.

## Example product (after factory loop)

- [x] First playable Dark Dungeon increment: Godot 4 scaffold + four-way player movement

Humans may merge factory PRs later. New product work continues from the current branch tip so it stacks on those PRs.

## Milestone 6 (Wish Factory)

Leave Gas Town. Bond the harness to Dark Dungeon. Wishes feed the graph:

- [x] Markdown wish drop + list command (FACTORY-020)
- [ ] Planner converts open wishes into beads (FACTORY-021)
- [x] Dark Dungeon has a bounded room that can generate more wishes (DUNGEON-003)

Unattended workers still stop when the ready queue is empty. A wish is not work until a planner turns it into beads.

## Non-Goals (v0)

- Fully autonomous 24/7 operation
- Multi-agent parallelism
- External paid orchestration services
- Perfect upfront planning
- Building Dark Dungeon or other products before the factory loop is closed
- Gas Town: Mayor/polecat fleet, reusable orchestrator, Cursor SDK as the next step
