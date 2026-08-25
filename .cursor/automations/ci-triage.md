# CI triage — Cursor Automation recipe

Commit this recipe. Do **not** invent work. Green CI means stop.

## Prompt (paste into the automation)

```text
Triage the latest CI failure on this repository
```

## Behavior

1. Find the latest failed GitHub Actions run for this repo (harness tests or bead validation).
2. If CI is green or there is no failure: **stop**. Do not invent work. Do not start Dark Dungeon or other product work.
3. If the failure is clearly caused by the change on that branch, fix it in that bead's scope, run `python3 -m harness.tests` and `python3 -m harness.beads validate`.
4. If the fix is out of scope of the failing change: create a new bead, link it, and stop. Do not fold extra work into an unrelated bead.
5. One failure per run.

## How to enable in Cursor

1. Open Cursor Dashboard → Cloud Agents / Automations.
2. Create an automation on this repository.
3. Paste the prompt above.
4. Trigger on CI failure if the dashboard supports it; otherwise schedule conservatively and no-op when green.

Cost-conscious: crons watch, models act only when a check failed.
