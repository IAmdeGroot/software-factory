# Conventions

## Beads

- ID format: `FACTORY-NNN` for factory work, `PRODUCT-NNN` for product work
- File name matches ID: `FACTORY-001.md`
- Status transitions: `ready` → `in_progress` → `review` → `done`
- Use `blocked` when waiting on human decision or external dependency
- One bead = one PR-sized change

## Branches

- Branch name: `bead/FACTORY-001-short-title`
- Merge to `main` only after review passes

## Commits

- Prefix with bead ID: `FACTORY-001: add bead schema validator`
- Keep commits focused on the current bead scope

## Code

- Prefer simple, readable code over clever abstractions
- Add tests when behavior is non-trivial
- No premature architecture — build what the current bead needs

## Documentation

- Record decisions in `docs/brain/decisions.md`
- Update bead file when status or scope changes
- Do not duplicate brain content in chat — reference files instead

## Agent Behavior

- Read `AGENTS.md` and relevant brain docs before starting work
- Use Plan Mode for multi-file changes
- Escalate to human for architecture forks and scope changes
