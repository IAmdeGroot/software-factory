"""Transition bead status after work completes."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from harness.beads.frontmatter import FrontmatterError, load_bead, write_bead


class TransitionError(Exception):
    """Raised when a bead status transition is not allowed."""


@dataclass
class TransitionResult:
    bead_id: str
    from_status: str
    to_status: str
    path: Path


def _load_bead_for_transition(beads_dir: Path, bead_id: str) -> tuple[Path, dict, str]:
    bead_path = beads_dir / f"{bead_id}.md"
    if not bead_path.is_file():
        raise TransitionError(f"bead {bead_id!r} not found")

    try:
        data, body = load_bead(bead_path)
    except FrontmatterError as exc:
        raise TransitionError(str(exc)) from exc

    if data.get("id") != bead_id:
        raise TransitionError(
            f"bead id mismatch: expected {bead_id!r}, found {data.get('id')!r}"
        )
    return bead_path, data, body


def _transition(
    beads_dir: Path, bead_id: str, expected_status: str, next_status: str, action: str
) -> TransitionResult:
    bead_path, data, body = _load_bead_for_transition(beads_dir, bead_id)
    current = data.get("status")
    if current != expected_status:
        raise TransitionError(
            f"bead {bead_id!r} cannot be {action} from status {current!r} "
            f"(expected {expected_status!r})"
        )

    data["status"] = next_status
    write_bead(bead_path, data, body)
    from harness.beads.backlog import sync_backlog_if_present

    sync_backlog_if_present(beads_dir)
    return TransitionResult(
        bead_id=bead_id,
        from_status=expected_status,
        to_status=next_status,
        path=bead_path,
    )


def complete_bead(beads_dir: Path, bead_id: str) -> TransitionResult:
    """Move a claimed bead from in_progress to review."""
    return _transition(beads_dir, bead_id, "in_progress", "review", "completed")


def done_bead(beads_dir: Path, bead_id: str) -> TransitionResult:
    """Move a reviewed bead from review to done."""
    return _transition(beads_dir, bead_id, "review", "done", "marked done")
