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

- [x] Planner agent can create beads from a vision doc
- [x] Worker agent can claim a ready bead and implement it without step-by-step human guidance
- [ ] Bead status is updated automatically after work completes
- [ ] At least one example product increment is built through the factory loop

## Non-Goals (v0)

- Fully autonomous 24/7 operation
- Multi-agent parallelism
- External paid orchestration services
- Perfect upfront planning
