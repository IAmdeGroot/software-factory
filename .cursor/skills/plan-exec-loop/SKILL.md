---
name: plan-exec-loop
description: Run the software factory plan-implement-verify-review loop for a bead. Use when claiming a bead, starting factory work, or when the user says "implement FACTORY-NNN".
---

# Plan-Exec Loop

Use this skill when implementing any factory bead.

## Steps

1. **Read context**
   - `AGENTS.md`
   - The bead file in `docs/work-graph/beads/`
   - Relevant files in `docs/brain/`

2. **Plan** (required for multi-file beads)
   - List files to create/modify
   - Outline approach in 3-5 bullets
   - Confirm acceptance criteria are clear; ask human if ambiguous

3. **Claim the bead**
   - Update bead frontmatter: `status: in_progress`, `assignee: agent`
   - Create branch: `bead/FACTORY-NNN-short-title`

4. **Implement**
   - Make the smallest change that satisfies criteria
   - Follow conventions in `docs/brain/conventions.md`

5. **Verify**
   - Run tests
   - Run bead validator if available
   - Fix any failures

6. **Review**
   - Check diff against each acceptance criterion
   - Note anything the human should know

7. **Complete**
   - Update bead: `status: review` (or `done` if no human review needed)
   - Update `docs/work-graph/backlog.md`
   - Summarize what was done and what's now ready

## Output Format

```markdown
## Bead FACTORY-NNN — [title]

**Status:** review | done
**Branch:** bead/FACTORY-NNN-short-title
**Changes:** [brief list]
**Tests:** [pass/fail]
**Next ready beads:** [list]
**Human needed:** [yes/no — why]
```
