---
id: FACTORY-018
title: Add human land/merge recipe
status: done
dependencies:
  - FACTORY-016
assignee: agent
---

# FACTORY-018: Add human land/merge recipe

## Context

Architecture has a merge step. Agents must not merge. A committed recipe
tells the human what to merge: green CI, bead `done`, one PR per bead.
Also record that GitHub's integration branch should be `main` (today the
default is a leftover bead branch).

## Acceptance Criteria

- [x] `.cursor/automations/land.md` exists with what to merge and what not to merge
- [x] Recipe: merge only when the bead is `done`, CI is green, and the PR is one bead
- [x] Recipe says agents do not merge; empty or unready PRs mean skip
- [x] `docs/brain/conventions.md` states integration branch is `main` and changing GitHub's default branch is a human action
- [x] README or AGENTS.md points at the land recipe
- [x] Does not change GitHub default branch settings from this bead

## Notes

- Do not add paid merge bots
- Dark Dungeon stays deferred until this land loop exists
