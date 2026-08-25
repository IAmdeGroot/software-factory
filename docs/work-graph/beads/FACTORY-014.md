---
id: FACTORY-014
title: Add PR review automation recipe
status: ready
dependencies:
  - FACTORY-013
assignee: null
---

# FACTORY-014: Add PR review automation recipe

## Context

Architecture calls for Cursor automations for PR review. The reviewer skill
exists after FACTORY-013; this bead commits the recipe a human can enable so
a PR event can wake a reviewer without a chat message.

## Acceptance Criteria

- [ ] `.cursor/automations/pr-review.md` exists with the exact prompt to paste
- [ ] Prompt is `Review the next bead` (or equivalent that uses the reviewer skill)
- [ ] Recipe says: empty review queue means stop; do not invent work
- [ ] Recipe describes trigger guidance (PR opened / CI green) without requiring a specific paid service
- [ ] README or AGENTS.md explains that enabling the automation is a human dashboard action
- [ ] Does not create the Cursor dashboard automation from this bead

## Notes

- Cost-conscious: not a tight loop; crons watch, models act
- Humans still merge
