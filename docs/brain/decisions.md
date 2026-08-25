# Decision Log

Record non-obvious decisions here. Format:

```markdown
## YYYY-MM-DD — Short title

**Context:** Why this came up
**Decision:** What we chose
**Rationale:** Why
**Alternatives considered:** What we rejected and why
```

---

## 2026-08-19 — Project is the factory, not a game

**Context:** Initial concept used a Dark Dungeon game as the primary framing.
**Decision:** The repository IS the software factory. Dark Dungeon moves to `examples/`.
**Rationale:** The factory must be reusable for any product, not tied to one game.
**Alternatives considered:** Game-first repo with factory as subfolder — rejected because it inverts the priority.

## 2026-08-19 — Markdown beads over external issue tracker (v0)

**Context:** Need a work graph agents can read/write without paid services.
**Decision:** Use markdown files with YAML frontmatter in `docs/work-graph/beads/`.
**Rationale:** Zero cost, git-tracked, agent-friendly, easy to query with scripts.
**Alternatives considered:** GitHub Issues, Jira, Beads CLI — deferred until v0 loop works.

## 2026-08-19 — Cursor-native harness (v0)

**Context:** Need orchestration without adding paid services.
**Decision:** Start with Cursor Agent + rules + skills + manual/semi-auto bead loop.
**Rationale:** Fits $20/mo budget; learn the loop before automating it.
**Alternatives considered:** Cursor SDK headless agents — planned for v1 after manual loop is stable.

## 2026-08-25 — Factory loop before Dark Dungeon

**Context:** Milestone 2 is complete. The remaining v0 checkbox was an example product increment, and FACTORY-005 was waiting in review. The human asked to make the factory autonomous before starting the game.
**Decision:** Accept FACTORY-005 as done. Defer `examples/dark-dungeon/` until Milestone 3 closes the factory loop. v0 success is the unattended worker loop (status commands, next-bead pull, CI, skill + automation recipe), not a playable game.
**Rationale:** The factory is the product. Building a game now would train the loop on the wrong layer and skip the still-manual status and pull steps.
**Alternatives considered:** Start Dark Dungeon beads in parallel — rejected; it splits attention before the loop can run without a human naming work and editing markdown.

## 2026-08-25 — Milestone 4 is review and CI triage, not the game

**Context:** Milestone 3 closed the worker loop. The ready queue is empty. The human asked to continue factory autonomy. Architecture already listed PR review / CI triage as the next evolution step. The remaining stall is beads sitting in `review` until someone types "continue".
**Decision:** Plan Milestone 4 (FACTORY-012–015): review-queue CLI, reviewer skill, PR-review recipe, CI-triage recipe. Keep Dark Dungeon deferred. Humans still merge PRs.
**Rationale:** Autonomy now means a reviewer can act without a chat nudge, and CI failures can wake an agent. Building a game would skip the review side of the factory.
**Alternatives considered:** Start Dark Dungeon now that v0 worker criteria are checked — rejected; review still requires a human message. Cursor SDK fleet — still deferred as v1.

## 2026-08-25 — Milestone 5 is land loop, not the game

**Context:** Milestone 4 closed review and CI triage. The ready queue is empty. Eleven draft PRs are stacked and nothing has merged. Conventions already say merge to `main`, but the GitHub default branch is still a leftover bead branch, and the worker skill never opens a PR.
**Decision:** Plan Milestone 5 (FACTORY-016–018): worker opens a PR, reviewer marks it ready after `done`, human land recipe. Keep Dark Dungeon deferred until work can land.
**Rationale:** Building a game on stacked unmerged branches would not stress-test the factory. The next bottleneck is MERGE, not a product increment.
**Alternatives considered:** Start Dark Dungeon now that the review loop exists — rejected until PRs can land. Auto-merge — rejected; humans still merge. Cursor SDK — still v1.

## 2026-08-25 — Continue from stacked tip; start Dark Dungeon

**Context:** Factory milestones 3–5 are implemented. The human will merge the stacked PRs later and asked how to continue without waiting.
**Decision:** Keep working on the current branch tip (`cursor/factory-018-land-recipe-06d8` / PR #15). Start the example product with `DUNGEON-` beads: Godot 4 scaffold, then four-way player movement. Do not wait for merges.
**Rationale:** The land loop exists. An empty ready queue with no product work stalls the factory. The remaining v0 checkbox is an example increment. Stacking on #15 means a later merge still gets factory + game work in order.
**Alternatives considered:** Idle until merges land — rejected; the human asked to continue. More factory (Cursor SDK) — still v1. Auto-merge the stack — agents still cannot merge.

## 2026-08-25 — Godot 4 2D for Dark Dungeon

**Context:** First product beads need an engine.
**Decision:** Godot 4 (config_version 5), 2D, project under `examples/dark-dungeon/`.
**Rationale:** Matches the example README, is free, and project files are text so agents can edit them without the editor.
**Alternatives considered:** Unity — heavier and less text-friendly. Browser canvas — would skip the intended Godot example. Godot 3 — older; 4 is current.

## 2026-08-25 — Leave Gas Town; grow a Wish Factory around Dark Dungeon

**Context:** Factory v0 through land loop is done. Dark Dungeon has a scaffold and movement. The human asked what was missing versus Yegge, then pointed at [The Shape of Things to Come](https://yegge.ai/essays/the-shape-of-things-to-come/) and said to leave Gas Town.
**Decision:** Stop treating a reusable Gas Town (Mayor, polecats, refinery, 24/7 fleet, Cursor SDK) as the next milestone. Grow the harness because Dark Dungeon needs it. Next increment is a Wish Factory: markdown wishes feed the work graph; a planner turns wishes into beads; workers still stop on an empty ready queue. Product beads (rooms, combat) proceed in parallel so the game can generate wishes.
**Rationale:** Yegge's later essay says reusable harnesses fail; Gas Town burned down building itself. The convergent shape (brain + work graph + watchers) still holds, but it has to be chemically bonded to a live product. A wish drop is the smallest intake that matches "give a requirement and let it spin" without standing up a town.
**Alternatives considered:** Keep building toward Gas Town (SDK, parallel workers, merge thunderdome) — rejected by the human. Adopt Yegge's Beads CLI / Dolt — still deferred; markdown wishes match the v0 bead format. Auto-grant wishes with no planner — rejected; a wish is not a bead until it has acceptance criteria.

## 2026-08-25 — Dark Dungeon is Hollow Knight–inspired, still top-down

**Context:** The human filed a wish: the game should feel or be inspired by Hollow Knight. Dark Dungeon is already a Godot 4 top-down room with WASD movement. Hollow Knight is a side-view Metroidvania.
**Decision:** Treat Hollow Knight as **feel**, not genre. Keep top-down 2D. First borrows: nail-like directional melee (`DUNGEON-004`), then one strikeable enemy (`DUNGEON-005`). Do not clone Hallownest or respec the camera in this increment.
**Rationale:** "Inspired by" is taste and verbs, not a second engine. Switching to side-view would throw away DUNGEON-001–003. A nail plus something to hit is the smallest playable HK echo.
**Alternatives considered:** Full side-view Metroidvania pivot — rejected unless the human asks to abandon top-down. Implement the whole HK kit (pogo, soul, map) in one bead — rejected; too large.
