# Work Backlog

Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.

<!-- beads:tables:start -->
## Ready

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## In Progress

| ID | Title | Status |
|----|-------|--------|
| [DUNGEON-016](beads/DUNGEON-016.md) | Add dramatic interior lighting and shadows | in_progress |

## In Review

| ID | Title | Status |
|----|-------|--------|
| _(none)_ | | |

## Blocked (waiting on dependencies)

| ID | Title | Blocked by |
|----|-------|------------|
| [DUNGEON-017](beads/DUNGEON-017.md) | Add an outdoor approach with atmospheric depth | DUNGEON-016 |

## Done

| ID | Title | Status |
|----|-------|--------|
| [DUNGEON-001](beads/DUNGEON-001.md) | Add Godot 4 project scaffold | done |
| [DUNGEON-002](beads/DUNGEON-002.md) | Add four-way player movement | done |
| [DUNGEON-003](beads/DUNGEON-003.md) | Add a bounded room the player cannot walk out of | done |
| [DUNGEON-004](beads/DUNGEON-004.md) | Add nail-like melee in the facing direction | done |
| [DUNGEON-005](beads/DUNGEON-005.md) | Add one strikeable enemy in the room | done |
| [DUNGEON-006](beads/DUNGEON-006.md) | Add enemy contact damage and player hit points | done |
| [DUNGEON-007](beads/DUNGEON-007.md) | Add a doorway to a second room | done |
| [DUNGEON-008](beads/DUNGEON-008.md) | Add a second enemy type in the east room | done |
| [DUNGEON-009](beads/DUNGEON-009.md) | Add a patrolling third enemy type | done |
| [DUNGEON-010](beads/DUNGEON-010.md) | Add shard loot when a foe dies | done |
| [DUNGEON-011](beads/DUNGEON-011.md) | Add a nail shrine that spends shards | done |
| [DUNGEON-012](beads/DUNGEON-012.md) | Add a seal that only a honed nail can break | done |
| [DUNGEON-013](beads/DUNGEON-013.md) | Add a boss in the third room | done |
| [DUNGEON-014](beads/DUNGEON-014.md) | Show a clear beat when the warden falls | done |
| [DUNGEON-015](beads/DUNGEON-015.md) | Establish the original dark-fantasy visual language | done |
| [FACTORY-001](beads/FACTORY-001.md) | Validate bead file schema | done |
| [FACTORY-002](beads/FACTORY-002.md) | Create harness project scaffold | done |
| [FACTORY-003](beads/FACTORY-003.md) | Add bead status listing script | done |
| [FACTORY-004](beads/FACTORY-004.md) | Add ready-queue CLI command | done |
| [FACTORY-005](beads/FACTORY-005.md) | Add bead claim CLI command | done |
| [FACTORY-006](beads/FACTORY-006.md) | Add Cursor hook to validate beads on edit | done |
| [FACTORY-007](beads/FACTORY-007.md) | Add complete and done CLI commands | done |
| [FACTORY-008](beads/FACTORY-008.md) | Sync backlog.md from bead statuses | done |
| [FACTORY-009](beads/FACTORY-009.md) | Add next CLI command to claim first ready bead | done |
| [FACTORY-010](beads/FACTORY-010.md) | Add CI workflow for tests and bead validation | done |
| [FACTORY-011](beads/FACTORY-011.md) | Close the unattended worker loop | done |
| [FACTORY-012](beads/FACTORY-012.md) | Add review-queue CLI command | done |
| [FACTORY-013](beads/FACTORY-013.md) | Add bead-reviewer skill | done |
| [FACTORY-014](beads/FACTORY-014.md) | Add PR review automation recipe | done |
| [FACTORY-015](beads/FACTORY-015.md) | Add CI triage automation recipe | done |
| [FACTORY-016](beads/FACTORY-016.md) | Worker loop opens a pull request | done |
| [FACTORY-017](beads/FACTORY-017.md) | Reviewer marks the PR ready after done | done |
| [FACTORY-018](beads/FACTORY-018.md) | Add human land/merge recipe | done |
| [FACTORY-019](beads/FACTORY-019.md) | Leave Gas Town for the Wish Factory | done |
| [FACTORY-020](beads/FACTORY-020.md) | Add markdown wish drop and list command | done |
| [FACTORY-021](beads/FACTORY-021.md) | Convert open wishes into beads | done |
| [FACTORY-022](beads/FACTORY-022.md) | Add wish-dropper skill | done |
<!-- beads:tables:end -->

---

## Milestone 2 — Pull-Work Loop + Guardrails

Goal: agents can discover ready work, claim it, and get automatic validation on bead edits.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-004 | `ready` command — focused pull-work queue | done |
| FACTORY-005 | `claim` command — mark bead in_progress | done |
| FACTORY-006 | Cursor hook — auto-validate bead file edits | done |

---

## Milestone 3 — Close the Factory Loop

Goal: workers can finish beads and pull the next one without a human editing markdown or naming the task. Product work (Dark Dungeon) stays deferred until this loop is closed.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-007 | `complete` / `done` — status transitions | done |
| FACTORY-008 | regenerate `backlog.md` from beads | done |
| FACTORY-009 | `next` — claim first ready bead | done |
| FACTORY-010 | CI watches tests and bead validation | done |
| FACTORY-011 | unattended worker skill + automation recipe | done |

---

## Milestone 4 — Review Loop + CI Triage

Goal: beads in `review` and failed CI can wake an agent without a human naming the work. Humans still merge. Dark Dungeon stays deferred.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-012 | `review-queue` — beads waiting for review | done |
| FACTORY-013 | bead-reviewer skill — accept or reject | done |
| FACTORY-014 | PR review automation recipe | done |
| FACTORY-015 | CI triage automation recipe | done |

---

## Milestone 5 — Land Loop

Goal: each bead becomes a PR that a human can merge. Agents still do not merge. Dark Dungeon stays deferred until work can land.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-016 | worker commits, pushes, opens one PR | done |
| FACTORY-017 | reviewer marks PR ready after `done` | done |
| FACTORY-018 | human land/merge recipe + `main` | done |

---

## Milestone 6 — Wish Factory

Goal: leave Gas Town. Bond the harness to Dark Dungeon. Wishes feed the work graph. Workers still stop on an empty ready queue.

| Bead | Purpose | Status |
|------|---------|--------|
| FACTORY-019 | record Wish Factory direction in the brain | done |
| FACTORY-020 | markdown wish drop + list command | done |
| FACTORY-021 | planner converts wishes into beads | done |
| FACTORY-022 | dropper writes open wishes from sourced intent | done |
| DUNGEON-003 | bounded room (product surface for wishes) | done |

---

## Dark Dungeon — First Playable

Example product under `examples/dark-dungeon/`. Factory PRs may still be unmerged; this work stacks on the current tip.

| Bead | Purpose | Status |
|------|---------|--------|
| DUNGEON-001 | Godot 4 2D project scaffold | done |
| DUNGEON-002 | Four-way player movement | done |
| DUNGEON-003 | Bounded room | done |

---

## Dark Dungeon — Hollow Knight feel (WISH-001)

Inspiration, not a clone. Stay top-down. First verbs:

| Bead | Purpose | Status |
|------|---------|--------|
| DUNGEON-004 | Nail-like melee in facing direction | ready |
| DUNGEON-005 | One strikeable enemy in the room | after 004 |

---

## How to Use

1. Run `python -m harness.beads ready` to see claimable work
2. Run `python -m harness.beads claim FACTORY-00X` to claim a bead
3. Tell Cursor Agent: `Implement the claimed bead`
4. Agent implements, tests, commits, pushes, opens one PR, then `python -m harness.beads complete <id>`
5. Unattended: `Implement the next ready bead` (empty queue means stop)
6. Review: `Review the next bead`; humans merge via `.cursor/automations/land.md`
7. Dropper: prompt `Drop wishes from this intent` — `.cursor/skills/wish-dropper/SKILL.md`. Needs a source. No source means stop; do not invent wishes. Writes `open` wish files. Do not convert to beads or start workers.
8. Planner: prompt `Convert open wishes into beads` — `.cursor/skills/wish-planner/SKILL.md`. Empty wish list means stop; do not invent wishes. Converted wishes become `planned` and list their bead ids. Do not claim or start workers.
