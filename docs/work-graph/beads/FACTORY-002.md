---
id: FACTORY-002
title: Create harness project scaffold
status: blocked
dependencies:
  - FACTORY-001
assignee: null
---

# FACTORY-002: Create harness project scaffold

## Context

The `harness/` directory holds factory orchestration code. It needs a proper project
setup with dependency management, test runner, and entry point.

## Acceptance Criteria

- [ ] `harness/` has a language runtime project (Python with uv/pip or Node with npm)
- [ ] Test runner configured and working
- [ ] `harness/README.md` updated with how to run tests and scripts
- [ ] Bead validator from FACTORY-001 lives in `harness/`
- [ ] `npm test` or equivalent runs all harness tests from repo root

## Notes

- Prefer Python if no strong preference — good for CLI scripts and text processing
- Keep dependencies minimal
