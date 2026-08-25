---
id: FACTORY-017
title: Reviewer marks the PR ready after done
status: ready
dependencies:
  - FACTORY-013
  - FACTORY-016
assignee: null
---

# FACTORY-017: Reviewer marks the PR ready after done

## Context

Reviewers can `done` a bead without merging. Draft PRs then sit unseen.
After a pass, the reviewer should mark the PR ready for human merge when
tools allow — still without merging.

## Acceptance Criteria

- [ ] `bead-reviewer` skill, after `done`, marks the matching PR ready for review when tools allow
- [ ] Skill still does **not** merge
- [ ] If no PR exists, the skill says so and stops (do not invent a merge)
- [ ] AGENTS.md or the reviewer skill documents this step
- [ ] Empty review queue still means stop

## Notes

- Matching PR is the branch for that bead id
- Keep the skill small
