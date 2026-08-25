---
id: FACTORY-010
title: Add CI workflow for tests and bead validation
status: done
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

- [x] GitHub Actions workflow runs on `push` and `pull_request`
- [x] Job runs `python3 -m harness.tests` from the repo root
- [x] Job runs `python3 -m harness.beads validate`
- [x] Uses Python 3.12 and the stdlib-only harness (no extra install step beyond checkout)
- [x] Workflow file lives under `.github/workflows/`
- [x] `harness/README.md` or project README documents that CI watches tests and beads

## Notes

- Keep the workflow minimal — one job, no matrix, no paid services
- Do not add lint/format gates in this bead
