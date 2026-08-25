---
id: FACTORY-011
title: Close the unattended worker loop
status: ready
dependencies:
  - FACTORY-007
  - FACTORY-008
  - FACTORY-009
assignee: null
---

# FACTORY-011: Close the unattended worker loop

## Context

Harness commands can claim, complete, and sync status, but the worker skill still
expects a human to name a bead and remember to update it. Closing v0 autonomy
means a worker can start from "do the next work" and leave bead status correct
without extra prompting.

This is not 24/7 multi-agent operation. It is the documented loop a Cursor
Agent or a later Cursor Automation can run unattended.

## Acceptance Criteria

- [ ] `plan-exec-loop` skill pulls work with `python -m harness.beads next` when no bead id is given
- [ ] After verify/review, the skill runs `python -m harness.beads complete <id>` (backlog sync happens via FACTORY-008)
- [ ] Skill documents the unattended prompt: `Implement the next ready bead`
- [ ] A committed automation recipe exists (e.g. `.cursor/automations/worker-loop.md`) with the exact prompt and empty-queue behavior
- [ ] README or AGENTS.md explains how a human enables the scheduled worker in Cursor
- [ ] Recipe says: if `next` fails because the queue is empty, stop; do not invent work

## Notes

- Do not create a Cursor dashboard automation from this bead — commit the recipe only
- Do not start Dark Dungeon or other product work
- Keep the skill change small; do not rewrite factory rules
