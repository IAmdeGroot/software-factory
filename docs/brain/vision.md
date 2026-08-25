# Factory Vision

## What We Are Building

A **software factory** — a reusable harness that lets AI agents autonomously build software products from high-level human intent.

The factory is the product. Games, apps, and tools are outputs.

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

- [ ] Worker commits, pushes, and opens one PR per bead
- [ ] Reviewer marks that PR ready after `done` (still does not merge)
- [ ] Documented human land/merge recipe; integration branch is `main`

Dark Dungeon stays deferred until this land loop exists.

## Later (after v0 factory loop)

- At least one example product increment built through the factory loop (`examples/dark-dungeon/`)

## Non-Goals (v0)

- Fully autonomous 24/7 operation
- Multi-agent parallelism
- External paid orchestration services
- Perfect upfront planning
- Building Dark Dungeon or other products before the factory loop is closed
