---
id: FACTORY-013
title: Add bead-reviewer skill
status: done
dependencies:
  - FACTORY-012
assignee: agent
---

# FACTORY-013: Add bead-reviewer skill

## Context

The worker loop stops at `review`. Closing a bead still depends on a human
saying "continue". A reviewer skill should pull the review queue, check the
diff against acceptance criteria, and run `done` or leave the bead in review.

This is not automatic merge. Humans still merge PRs.

## Acceptance Criteria

- [x] `.cursor/skills/bead-reviewer/SKILL.md` exists
- [x] When no bead id is given, the skill uses `python -m harness.beads review-queue`
- [x] Empty review queue means stop; do not invent work
- [x] Skill checks the change against each acceptance criterion on the bead
- [x] On pass: `python -m harness.beads done <id>`
- [x] On fail: leave status `review` and list the failing criteria
- [x] Documents the unattended prompt: `Review the next bead`
- [x] AGENTS.md or README mentions the reviewer prompt

## Notes

- Do not start Dark Dungeon or other product work
- Keep the skill small; do not rewrite factory rules
- Do not merge PRs from this skill
