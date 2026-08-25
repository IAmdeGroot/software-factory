---
id: FACTORY-016
title: Worker loop opens a pull request
status: done
dependencies:
  - FACTORY-011
assignee: agent
---

# FACTORY-016: Worker loop opens a pull request

## Context

Workers implement and `complete` beads, but the plan-exec skill never tells
them to commit, push, or open a PR. Work piles up on stacked branches and
never reaches the integration branch.

## Acceptance Criteria

- [x] `plan-exec-loop` skill commits with a `FACTORY-NNN:` (or product-id) prefix
- [x] Skill pushes the bead branch and opens one PR for that bead when the environment can
- [x] Skill uses the repository default branch as PR base
- [x] Skill does **not** merge the PR
- [x] AGENTS.md or README documents that one bead = one branch = one PR
- [x] Empty ready queue still means stop; do not invent work

## Notes

- Prefer `bead/FACTORY-NNN-short-title`. If the environment requires another prefix, use that and keep one bead per branch.
- If PR creation is unavailable, still commit and push; report that a human must open the PR
- Do not start Dark Dungeon in this bead
