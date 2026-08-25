# Worker loop — Cursor Automation recipe

Commit this recipe. Do **not** invent work. This is not 24/7 multi-agent operation.

## Prompt (paste into the automation)

```text
Implement the next ready bead
```

## Behavior

1. Follow `.cursor/skills/plan-exec-loop/SKILL.md`.
2. Run `python -m harness.beads next` to claim work.
3. If `next` fails because the ready queue is empty: **stop**. Do not create beads, do not start Dark Dungeon or other product work, do not look for extra tasks.
4. If a bead is claimed: implement it, run tests, then `python -m harness.beads complete <id>`.
5. One bead per run.

## How to enable in Cursor

1. Open Cursor Dashboard → Cloud Agents / Automations.
2. Create an automation on this repository.
3. Paste the prompt above.
4. Schedule conservatively (for example after human hours, not a tight loop). Cost-conscious: crons watch, models act only when there is work.

Empty queue is a successful watch cycle. The factory is idle until a planner adds ready beads.
