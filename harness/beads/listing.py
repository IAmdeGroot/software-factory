"""Bead status listing utilities."""

from __future__ import annotations

import json
from pathlib import Path

from harness.beads.validate import parse_frontmatter


def _read_beads(beads_dir: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted(beads_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        data, error = parse_frontmatter(content)
        if error:
            raise ValueError(f"{path.name}: {error}")
        records.append(
            {
                "id": data.get("id", path.stem),
                "title": data.get("title", ""),
                "status": data.get("status", ""),
                "dependencies": data.get("dependencies", []),
                "file": path.name,
            }
        )
    return records


def build_status_summary(beads_dir: Path) -> dict:
    records = _read_beads(beads_dir)
    status_by_id = {rec["id"]: rec["status"] for rec in records}

    ready: list[dict] = []
    blocked: list[dict] = []
    all_items: list[dict] = []

    for rec in records:
        deps = rec["dependencies"] if isinstance(rec["dependencies"], list) else []
        waiting_on = [dep for dep in deps if status_by_id.get(dep) != "done"]
        is_ready = rec["status"] == "ready" and not waiting_on

        item = {
            "id": rec["id"],
            "title": rec["title"],
            "status": rec["status"],
            "dependencies": deps,
            "waiting_on": waiting_on,
            "is_ready": is_ready,
        }
        all_items.append(item)
        if is_ready:
            ready.append(item)
        if rec["status"] == "blocked" or waiting_on:
            blocked.append(item)

    return {"beads": all_items, "ready": ready, "blocked": blocked}


def build_ready_queue(beads_dir: Path) -> list[dict]:
    """Return beads that are ready to be claimed (status ready, deps done)."""
    summary = build_status_summary(beads_dir)
    return summary["ready"]


def format_ready_text(ready: list[dict]) -> str:
    lines = ["Ready queue:"]
    if not ready:
        lines.append("- (none)")
        return "\n".join(lines)
    for item in ready:
        lines.append(f"- {item['id']}: {item['title']}")
    return "\n".join(lines)


def ready_to_json(ready: list[dict]) -> str:
    payload = {"ready": ready, "count": len(ready)}
    return json.dumps(payload, indent=2)


def format_summary_text(summary: dict) -> str:
    lines: list[str] = []
    lines.append("Bead status summary")
    lines.append("")
    lines.append("All beads:")
    for item in summary["beads"]:
        lines.append(f"- {item['id']}: {item['status']} ({item['title']})")

    lines.append("")
    lines.append("Ready beads:")
    if summary["ready"]:
        for item in summary["ready"]:
            lines.append(f"- {item['id']}: ready")
    else:
        lines.append("- (none)")

    lines.append("")
    lines.append("Blocked / waiting:")
    if summary["blocked"]:
        for item in summary["blocked"]:
            if item["waiting_on"]:
                waiting = ", ".join(item["waiting_on"])
                lines.append(f"- {item['id']}: waiting on {waiting}")
            elif item["status"] == "blocked":
                lines.append(f"- {item['id']}: blocked")
    else:
        lines.append("- (none)")
    return "\n".join(lines)


def summary_to_json(summary: dict) -> str:
    return json.dumps(summary, indent=2)
