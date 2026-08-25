---
id: FACTORY-017
title: Reviewer marks the PR ready after done
status: done
dependencies:
  - FACTORY-013
  - FACTORY-016
assignee: agent
---

# FACTORY-017: Reviewer marks the PR ready after done

## Context

Reviewers can `done` a bead without merging. Draft PRs then sit unseen.
After a pass, the reviewer should mark the PR ready for human merge when
tools allow — still without merging.

## Acceptance Criteria

- [x] `bead-reviewer` skill, after `done`, marks the matching PR ready for review when tools allow
- [x] Skill still does **not** merge
- [x] If no PR exists, the skill says so and stops (do not invent a merge)
- [x] AGENTS.md or the reviewer skill documents this step
- [x] Empty review queue still means stop

## Notes

- Matching PR is the branch for that bead id
- Keep the skill small
