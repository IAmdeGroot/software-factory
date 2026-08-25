---
id: FACTORY-018
title: Add human land/merge recipe
status: ready
dependencies:
  - FACTORY-016
assignee: null
---

# FACTORY-018: Add human land/merge recipe

## Context

Architecture has a merge step. Agents must not merge. A committed recipe
tells the human what to merge: green CI, bead `done`, one PR per bead.
Also record that GitHub's integration branch should be `main` (today the
default is a leftover bead branch).

## Acceptance Criteria

- [ ] `.cursor/automations/land.md` exists with what to merge and what not to merge
- [ ] Recipe: merge only when the bead is `done`, CI is green, and the PR is one bead
- [ ] Recipe says agents do not merge; empty or unready PRs mean skip
- [ ] `docs/brain/conventions.md` states integration branch is `main` and changing GitHub's default branch is a human action
- [ ] README or AGENTS.md points at the land recipe
- [ ] Does not change GitHub default branch settings from this bead

## Notes

- Do not add paid merge bots
- Dark Dungeon stays deferred until this land loop exists
