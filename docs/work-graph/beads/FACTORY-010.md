---
id: FACTORY-010
title: Add CI workflow for tests and bead validation
status: in_progress
dependencies:
  - FACTORY-002
assignee: agent
---

# FACTORY-010: Add CI workflow for tests and bead validation

## Context

Nothing watches the repo when nobody is in chat. Deterministic CI should run
harness tests and bead validation on every push and pull request — crons watch,
models act.

## Acceptance Criteria

- [ ] GitHub Actions workflow runs on `push` and `pull_request`
- [ ] Job runs `python3 -m harness.tests` from the repo root
- [ ] Job runs `python3 -m harness.beads validate`
- [ ] Uses Python 3.12 and the stdlib-only harness (no extra install step beyond checkout)
- [ ] Workflow file lives under `.github/workflows/`
- [ ] `harness/README.md` or project README documents that CI watches tests and beads

## Notes

- Keep the workflow minimal — one job, no matrix, no paid services
- Do not add lint/format gates in this bead
