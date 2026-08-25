# Conventions

## Beads

- ID format: `FACTORY-NNN` for factory work, `DUNGEON-NNN` (or other product prefix) for product work
- File name matches ID: `FACTORY-001.md`
- Wishes (after FACTORY-020): `WISH-NNN` files under `docs/work-graph/wishes/`. A wish is not claimable work until a planner turns it into beads.
- Status transitions: `ready` → `in_progress` → `review` → `done`
- Use `blocked` when waiting on human decision or external dependency
- One bead = one PR-sized change

## Branches

- Branch name: `bead/FACTORY-001-short-title` (if the environment requires another prefix, keep one bead per branch)
- Integration branch: `main`
- Merge to `main` only after the bead is `done` and CI is green
- Changing GitHub's default branch to `main` is a human repo setting, not an agent action

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
