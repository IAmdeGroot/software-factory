---
id: FACTORY-002
title: Create harness project scaffold
status: done
dependencies:
  - FACTORY-001
assignee: agent
---

# FACTORY-002: Create harness project scaffold

## Context

The `harness/` directory holds factory orchestration code. It needs a proper project
setup with dependency management, test runner, and entry point.

## Acceptance Criteria

- [x] `harness/` has a language runtime project (Python with uv/pip or Node with npm)
- [x] Test runner configured and working
- [x] `harness/README.md` updated with how to run tests and scripts
- [x] Bead validator from FACTORY-001 lives in `harness/`
- [x] `npm test` or equivalent runs all harness tests from repo root

## Notes

- Prefer Python if no strong preference — good for CLI scripts and text processing
- Keep dependencies minimal
