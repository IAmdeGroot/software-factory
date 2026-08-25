---
name: plan-exec-loop
description: Run the software factory plan-implement-verify-review loop for a bead. Use when claiming a bead, starting factory work, when the user says "implement FACTORY-NNN", or "Implement the next ready bead".
---

# Plan-Exec Loop

Use this skill when implementing any factory bead.

## Unattended prompt

`Implement the next ready bead`

When no bead id is given:

1. Run `python -m harness.beads next`
2. If that command fails because the ready queue is empty, **stop**. Do not invent work, do not create beads, do not start product work.
3. Otherwise implement the claimed bead below.

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
   - If a bead id was given: `python -m harness.beads claim FACTORY-NNN`
   - If none was given: `python -m harness.beads next`
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
   - Run `python -m harness.beads complete <id>` (sets `review`; backlog syncs automatically)
   - Do not hand-edit bead status tables in `docs/work-graph/backlog.md`
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
