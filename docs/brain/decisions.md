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
