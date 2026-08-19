# Harness

Factory orchestration code — scripts, validators, and automation that agents and humans use to operate the software factory.

## Planned Contents (v0)

| Component | Bead | Description |
|-----------|------|-------------|
| Bead validator | FACTORY-001 | Validate bead file schema |
| Project scaffold | FACTORY-002 | Runtime, tests, entry point |
| Bead list CLI | FACTORY-003 | Show ready/blocked beads |

## Running (after FACTORY-002)

```bash
# Run tests
npm test          # or: python -m pytest

# List bead status
npm run beads:list   # or: python -m harness.beads list
```

## Design Principles

- **Deterministic where possible** — scripts validate, agents reason
- **Agent-readable output** — plain text or `--json` flag
- **Minimal dependencies** — keep the harness lightweight
