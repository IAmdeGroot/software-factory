"""Markdown wish drop: list and validate wishes."""

from __future__ import annotations

import json
from pathlib import Path

from harness.beads.validate import (
    BeadValidationError,
    ValidationResult,
    parse_frontmatter,
)

WISH_STATUSES = frozenset({"open", "planned", "done"})
REQUIRED_WISH_FIELDS = ("id", "title", "status", "source")


def _wish_files(wishes_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in wishes_dir.glob("*.md")
        if path.stem.startswith("WISH-")
    )


def _read_wishes(wishes_dir: Path) -> list[dict]:
    records: list[dict] = []
    for path in _wish_files(wishes_dir):
        content = path.read_text(encoding="utf-8")
        data, error = parse_frontmatter(content)
        if error:
            raise ValueError(f"{path.name}: {error}")
        records.append(
            {
                "id": data.get("id", path.stem),
                "title": data.get("title", ""),
                "status": data.get("status", ""),
                "source": data.get("source", ""),
                "file": path.name,
            }
        )
    return records


def build_open_wishes(wishes_dir: Path) -> list[dict]:
    """Return open wishes, sorted by id."""
    if not wishes_dir.is_dir():
        return []
    open_wishes = [rec for rec in _read_wishes(wishes_dir) if rec["status"] == "open"]
    return sorted(open_wishes, key=lambda item: str(item["id"]))


def format_wishes_text(wishes: list[dict]) -> str:
    lines = ["Open wishes:"]
    if not wishes:
        lines.append("- (none)")
        return "\n".join(lines)
    for item in wishes:
        lines.append(f"- {item['id']}: {item['title']}")
    return "\n".join(lines)


def wishes_to_json(wishes: list[dict]) -> str:
    payload = {"wishes": wishes, "count": len(wishes)}
    return json.dumps(payload, indent=2)


def validate_wish_file(path: Path) -> list[BeadValidationError]:
    errors: list[BeadValidationError] = []
    rel = path.name

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [BeadValidationError(rel, f"cannot read file: {exc}")]

    data, parse_error = parse_frontmatter(content)
    if parse_error:
        return [BeadValidationError(rel, parse_error)]

    for field_name in REQUIRED_WISH_FIELDS:
        if field_name not in data or data[field_name] in (None, ""):
            errors.append(BeadValidationError(rel, f"missing required field: {field_name}"))

    if errors:
        return errors

    wish_id = data["id"]
    if wish_id != path.stem:
        errors.append(
            BeadValidationError(
                rel,
                f"id {wish_id!r} does not match filename (expected {path.stem!r})",
            )
        )

    status = data["status"]
    if status not in WISH_STATUSES:
        errors.append(
            BeadValidationError(
                rel,
                f"invalid status {status!r}; must be one of: {', '.join(sorted(WISH_STATUSES))}",
            )
        )

    return errors


def validate_wishes_dir(wishes_dir: Path) -> ValidationResult:
    """Validate WISH-*.md files. Missing directory is ok (empty drop)."""
    result = ValidationResult()
    if not wishes_dir.is_dir():
        return result
    for path in _wish_files(wishes_dir):
        result.errors.extend(validate_wish_file(path))
    return result
