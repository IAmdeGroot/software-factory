# Land / merge — human recipe

Agents do **not** merge. This recipe is for the human (or a dashboard reminder). Skip when nothing is ready.

## Prompt (optional dashboard reminder)

```text
List pull requests that are ready to land (bead done, CI green, one bead each). Do not merge.
```

## Merge only when all of these are true

1. The bead for that PR is `done` (`python -m harness.beads list`).
2. CI is green (harness tests + bead validate).
3. The PR is one bead (one branch, one FACTORY-NNN or product id).
4. The PR targets the integration branch (`main` once GitHub's default is renamed; until then, the repository default branch).

## Do not merge when

- The bead is still `review`, `in_progress`, or `ready`
- CI is red or missing
- The PR mixes multiple beads or extra product work
- The agent opened a "push only" branch with no PR — open the PR first

Empty or unready lists mean **skip**. Do not invent merges. Do not start Dark Dungeon as part of landing.

## GitHub default branch

Conventions say merge to `main`. Changing GitHub's default branch from a leftover bead branch to `main` is a **human** repo setting. Agents must not change it from this recipe.

## How to enable a reminder in Cursor

1. Open Cursor Dashboard → Cloud Agents / Automations.
2. Optional: schedule the prompt above on a sparse cadence.
3. You still click merge.

Cost-conscious: crons watch, humans merge.
