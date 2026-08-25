"""Claim beads from the ready queue."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from harness.beads.frontmatter import FrontmatterError, load_bead, write_bead
from harness.beads.listing import build_ready_queue


class ClaimError(Exception):
    """Raised when a bead cannot be claimed."""


@dataclass
class ClaimResult:
    bead_id: str
    assignee: str
    path: Path


def _is_already_claimed(data: dict) -> bool:
    status = data.get("status")
    assignee = data.get("assignee")
    return status == "in_progress" and assignee not in (None, "null", "")


def claim_bead(beads_dir: Path, bead_id: str, assignee: str = "agent") -> ClaimResult:
    bead_path = beads_dir / f"{bead_id}.md"
    if not bead_path.is_file():
        raise ClaimError(f"bead {bead_id!r} not found")

    try:
        data, body = load_bead(bead_path)
    except FrontmatterError as exc:
        raise ClaimError(str(exc)) from exc

    if data.get("id") != bead_id:
        raise ClaimError(f"bead id mismatch: expected {bead_id!r}, found {data.get('id')!r}")

    if _is_already_claimed(data):
        current = data.get("assignee")
        raise ClaimError(f"bead {bead_id!r} is already claimed by {current!r}")

    ready_ids = {item["id"] for item in build_ready_queue(beads_dir)}
    if bead_id not in ready_ids:
        raise ClaimError(f"bead {bead_id!r} is not in the ready queue")

    data["status"] = "in_progress"
    data["assignee"] = assignee
    write_bead(bead_path, data, body)

    return ClaimResult(bead_id=bead_id, assignee=assignee, path=bead_path)
