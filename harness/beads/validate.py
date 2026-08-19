"""Validate bead markdown files in the work graph."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

VALID_STATUSES = frozenset({"ready", "in_progress", "review", "done", "blocked"})
REQUIRED_FIELDS = ("id", "title", "status", "dependencies")


@dataclass
class BeadValidationError:
    bead_file: str
    message: str

    def __str__(self) -> str:
        return f"{self.bead_file}: {self.message}"


@dataclass
class ValidationResult:
    errors: list[BeadValidationError] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_frontmatter(content: str) -> tuple[dict, str | None]:
    """Parse YAML-like frontmatter from a bead file. Returns (data, error)."""
    if not content.startswith("---"):
        return {}, "missing opening frontmatter delimiter (---)"

    lines = content.splitlines()
    if len(lines) < 2:
        return {}, "frontmatter is empty"

    data: dict = {}
    current_key: str | None = None
    list_mode = False

    for line in lines[1:]:
        if line.strip() == "---":
            return data, None

        if list_mode and current_key:
            stripped = line.strip()
            if stripped.startswith("- "):
                data.setdefault(current_key, []).append(stripped[2:].strip())
                continue
            list_mode = False
            current_key = None

        if ":" not in line:
            return {}, f"invalid frontmatter line: {line!r}"

        key, _, raw_value = line.partition(":")
        key = key.strip()
        value = raw_value.strip()

        if value == "":
            current_key = key
            list_mode = True
            data[key] = []
            continue

        if value == "null":
            data[key] = None
        elif value == "[]":
            data[key] = []
        else:
            data[key] = value

    return {}, "missing closing frontmatter delimiter (---)"


def validate_bead_file(path: Path, known_ids: set[str]) -> list[BeadValidationError]:
    """Validate a single bead file."""
    errors: list[BeadValidationError] = []
    rel = path.name

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [BeadValidationError(rel, f"cannot read file: {exc}")]

    data, parse_error = parse_frontmatter(content)
    if parse_error:
        return [BeadValidationError(rel, parse_error)]

    for field_name in REQUIRED_FIELDS:
        if field_name not in data:
            errors.append(BeadValidationError(rel, f"missing required field: {field_name}"))

    if errors:
        return errors

    bead_id = data["id"]
    expected_id = path.stem
    if bead_id != expected_id:
        errors.append(
            BeadValidationError(
                rel,
                f"id {bead_id!r} does not match filename (expected {expected_id!r})",
            )
        )

    status = data["status"]
    if status not in VALID_STATUSES:
        errors.append(
            BeadValidationError(
                rel,
                f"invalid status {status!r}; must be one of: {', '.join(sorted(VALID_STATUSES))}",
            )
        )

    dependencies = data["dependencies"]
    if not isinstance(dependencies, list):
        errors.append(BeadValidationError(rel, "dependencies must be a list"))
        return errors

    for dep in dependencies:
        if dep not in known_ids:
            errors.append(
                BeadValidationError(rel, f"dependency {dep!r} references unknown bead")
            )

    return errors


def validate_beads_dir(beads_dir: Path) -> ValidationResult:
    """Validate all bead files in a directory."""
    result = ValidationResult()

    if not beads_dir.is_dir():
        result.errors.append(
            BeadValidationError(str(beads_dir), "beads directory does not exist")
        )
        return result

    bead_files = sorted(beads_dir.glob("*.md"))
    if not bead_files:
        result.errors.append(
            BeadValidationError(str(beads_dir), "no bead files found")
        )
        return result

    known_ids = {path.stem for path in bead_files}

    for path in bead_files:
        result.errors.extend(validate_bead_file(path, known_ids))

    return result
