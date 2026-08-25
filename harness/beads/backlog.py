"""Generate docs/work-graph/backlog.md from bead files."""

from __future__ import annotations

from pathlib import Path

from harness.beads.listing import build_status_summary

TABLES_START = "<!-- beads:tables:start -->"
TABLES_END = "<!-- beads:tables:end -->"

DEFAULT_INTRO = (
    "# Work Backlog\n\n"
    "Beads are ordered by dependency. **Ready** beads have all dependencies satisfied.\n\n"
)


def default_backlog_path(beads_dir: Path) -> Path:
    return beads_dir.parent / "backlog.md"


def _link(bead_id: str) -> str:
    return f"[{bead_id}](beads/{bead_id}.md)"


def _status_table(title: str, items: list[dict]) -> str:
    lines = [
        f"## {title}",
        "",
        "| ID | Title | Status |",
        "|----|-------|--------|",
    ]
    if not items:
        lines.append("| _(none)_ | | |")
    else:
        for item in items:
            lines.append(f"| {_link(item['id'])} | {item['title']} | {item['status']} |")
    return "\n".join(lines)


def _blocked_table(items: list[dict]) -> str:
    lines = [
        "## Blocked (waiting on dependencies)",
        "",
        "| ID | Title | Blocked by |",
        "|----|-------|------------|",
    ]
    if not items:
        lines.append("| _(none)_ | | |")
    else:
        for item in items:
            waiting = ", ".join(item["waiting_on"]) if item["waiting_on"] else "blocked"
            lines.append(f"| {_link(item['id'])} | {item['title']} | {waiting} |")
    return "\n".join(lines)


def render_status_tables(summary: dict) -> str:
    beads = summary["beads"]
    ready = summary["ready"]
    in_progress = [item for item in beads if item["status"] == "in_progress"]
    review = [item for item in beads if item["status"] == "review"]
    done = [item for item in beads if item["status"] == "done"]
    blocked: list[dict] = []
    for item in beads:
        if item["status"] == "blocked":
            blocked.append(item)
        elif item["status"] == "ready" and item["waiting_on"]:
            blocked.append(item)

    sections = [
        _status_table("Ready", ready),
        _status_table("In Progress", in_progress),
        _status_table("In Review", review),
        _blocked_table(blocked),
        _status_table("Done", done),
    ]
    return "\n\n".join(sections) + "\n"


def apply_tables(existing: str, tables: str) -> str:
    block = f"{TABLES_START}\n{tables.rstrip()}\n{TABLES_END}"
    if TABLES_START in existing and TABLES_END in existing:
        before, rest = existing.split(TABLES_START, 1)
        _, after = rest.split(TABLES_END, 1)
        return before + block + after
    if existing.strip():
        return DEFAULT_INTRO + block + "\n\n" + existing.lstrip()
    return DEFAULT_INTRO + block + "\n"


def sync_backlog(beads_dir: Path, backlog_path: Path | None = None) -> Path:
    path = backlog_path or default_backlog_path(beads_dir)
    summary = build_status_summary(beads_dir)
    tables = render_status_tables(summary)
    existing = path.read_text(encoding="utf-8") if path.is_file() else ""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(apply_tables(existing, tables), encoding="utf-8")
    return path


def sync_backlog_if_present(beads_dir: Path) -> Path | None:
    path = default_backlog_path(beads_dir)
    if not path.is_file():
        return None
    return sync_backlog(beads_dir, path)
