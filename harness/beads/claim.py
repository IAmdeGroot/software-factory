"""Claim beads from the ready queue."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from harness.beads.listing import build_ready_queue
from harness.beads.validate import parse_frontmatter


class ClaimError(Exception):
    """Raised when a bead cannot be claimed."""


@dataclass
class ClaimResult:
    bead_id: str
    assignee: str
    path: Path


def _serialize_frontmatter(data: dict) -> str:
    lines = ["---"]
    field_order = ("id", "title", "status", "dependencies", "assignee")
    written: set[str] = set()

    for key in field_order:
        if key not in data:
            continue
        written.add(key)
        value = data[key]
        if key == "dependencies":
            deps = value if isinstance(value, list) else []
            if not deps:
                lines.append("dependencies: []")
            else:
                lines.append("dependencies:")
                for dep in deps:
                    lines.append(f"  - {dep}")
        elif value is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {value}")

    for key, value in data.items():
        if key in written:
            continue
        if value is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {value}")

    lines.append("---")
    return "\n".join(lines)


def _split_bead_content(content: str) -> tuple[str, str]:
    if not content.startswith("---"):
        raise ClaimError("bead file is missing frontmatter")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ClaimError("bead file is missing closing frontmatter delimiter")

    body = parts[2]
    if body.startswith("\n"):
        body = body[1:]
    return parts[0] + "---" + parts[1] + "---", body


def _is_already_claimed(data: dict) -> bool:
    status = data.get("status")
    assignee = data.get("assignee")
    return status == "in_progress" and assignee not in (None, "null", "")


def claim_bead(beads_dir: Path, bead_id: str, assignee: str = "agent") -> ClaimResult:
    bead_path = beads_dir / f"{bead_id}.md"
    if not bead_path.is_file():
        raise ClaimError(f"bead {bead_id!r} not found")

    content = bead_path.read_text(encoding="utf-8")
    _, body = _split_bead_content(content)
    data, parse_error = parse_frontmatter(content)
    if parse_error:
        raise ClaimError(parse_error)

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
    updated = _serialize_frontmatter(data) + "\n" + body
    bead_path.write_text(updated, encoding="utf-8")

    return ClaimResult(bead_id=bead_id, assignee=assignee, path=bead_path)
