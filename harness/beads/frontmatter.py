"""Read and write bead markdown frontmatter."""

from __future__ import annotations

from pathlib import Path

from harness.beads.validate import parse_frontmatter


class FrontmatterError(Exception):
    """Raised when bead frontmatter cannot be parsed or written."""


def serialize_frontmatter(data: dict) -> str:
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


def split_bead_content(content: str) -> tuple[str, str]:
    if not content.startswith("---"):
        raise FrontmatterError("bead file is missing frontmatter")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise FrontmatterError("bead file is missing closing frontmatter delimiter")

    body = parts[2]
    if body.startswith("\n"):
        body = body[1:]
    return parts[0] + "---" + parts[1] + "---", body


def load_bead(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    _, body = split_bead_content(content)
    data, parse_error = parse_frontmatter(content)
    if parse_error:
        raise FrontmatterError(parse_error)
    return data, body


def write_bead(path: Path, data: dict, body: str) -> None:
    path.write_text(serialize_frontmatter(data) + "\n" + body, encoding="utf-8")
