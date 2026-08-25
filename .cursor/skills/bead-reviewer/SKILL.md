---
name: bead-reviewer
description: Review a bead in the review queue against its acceptance criteria. Use when the user says "Review the next bead", "review FACTORY-NNN", or when closing beads that are in review.
---

# Bead Reviewer

Use this skill to accept or reject a bead that a worker has marked `review`.
This skill does **not** merge pull requests.

## Unattended prompt

`Review the next bead`

When no bead id is given:

1. Run `python -m harness.beads review-queue`
2. If the queue is empty, **stop**. Do not invent work, do not create beads, do not start product work.
3. Otherwise review the first bead (stable id order) below.

## Steps

1. **Select the bead**
   - Named id: use that bead if its status is `review`
   - Otherwise: first id from `python -m harness.beads review-queue`

2. **Read the contract**
   - The bead file in `docs/work-graph/beads/`
   - The diff for that bead's change
   - Relevant `docs/brain/` docs only if needed to judge criteria

3. **Check every acceptance criterion**
   - Pass only if the criterion is actually met in the change
   - Tests must have been run (or the criterion does not require tests)

4. **Decide**
   - All criteria pass: `python -m harness.beads done <id>`
   - Any criterion fails: leave status `review` and list the failing criteria
   - After a pass, mark the matching pull request **ready for review** (not draft) when tools allow
   - Matching PR is the branch for that bead id
   - If no PR exists, say so and stop — do not invent a merge
   - Do not merge PRs
   - Do not start Dark Dungeon or other product work

## Output Format

```markdown
## Review FACTORY-NNN — [title]

**Verdict:** done | still review
**PR:** [ready for review | none — human must open PR]
**Failed criteria:** [none | list]
**Notes:** [brief]
```
