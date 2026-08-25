---
id: FACTORY-015
title: Add CI triage automation recipe
status: done
dependencies:
  - FACTORY-010
assignee: agent
---

# FACTORY-015: Add CI triage automation recipe

## Context

CI watches tests and bead validation, but nothing acts when a check fails.
A committed recipe lets a human enable a Cursor automation that reads the
failure and either fixes it in scope or files a bead.

## Acceptance Criteria

- [x] `.cursor/automations/ci-triage.md` exists with the exact prompt to paste
- [x] Recipe: read failed CI, fix if it is clearly in scope of the failing change
- [x] If the fix is out of scope, create a new bead and stop — do not fold extra work into an unrelated bead
- [x] Recipe says: green CI or no failure means stop; do not invent work
- [x] README or AGENTS.md explains how a human enables it
- [x] Does not create the Cursor dashboard automation from this bead

## Notes

- Keep the recipe short
- Do not add new CI jobs in this bead
