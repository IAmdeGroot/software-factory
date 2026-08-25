# PR review — Cursor Automation recipe

Commit this recipe. Do **not** invent work. Humans still merge pull requests.

## Prompt (paste into the automation)

```text
Review the next bead
```

## Behavior

1. Follow `.cursor/skills/bead-reviewer/SKILL.md`.
2. Run `python -m harness.beads review-queue`.
3. If the review queue is empty: **stop**. Do not invent work. Do not start Dark Dungeon or other product work. Do not merge PRs.
4. If a bead is listed: check the diff against every acceptance criterion.
5. All pass: `python -m harness.beads done <id>`. Any fail: leave `review` and list failing criteria.
6. One bead per run.

## Trigger guidance

Enable this when a pull request opens or when CI on that PR is green. If the dashboard only supports a schedule, run conservatively and no-op when the review queue is empty.

Do not require a paid orchestration service. Cost-conscious: crons watch, models act.

## How to enable in Cursor

1. Open Cursor Dashboard → Cloud Agents / Automations.
2. Create an automation on this repository.
3. Paste the prompt above.
4. Attach it to PR opened / CI success if available; otherwise a sparse schedule.

Enabling the automation is a human dashboard action. This bead only commits the recipe.
