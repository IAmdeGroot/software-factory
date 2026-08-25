"""Tests for backlog.md generation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.backlog import TABLES_END, TABLES_START, sync_backlog
from harness.beads.claim import claim_bead
from harness.beads.status import complete_bead


def bead_content(
    bead_id: str,
    title: str,
    status: str,
    dependencies: list[str] | None = None,
    assignee: str | None = None,
) -> str:
    deps = dependencies or []
    deps_field = "[]"
    if deps:
        deps_field = "\n" + "\n".join(f"  - {dep}" for dep in deps)
    assignee_value = "null" if assignee is None else assignee
    return (
        "---\n"
        f"id: {bead_id}\n"
        f"title: {title}\n"
        f"status: {status}\n"
        f"dependencies: {deps_field}\n"
        f"assignee: {assignee_value}\n"
        "---\n\n"
        f"# {bead_id}: {title}\n"
    )


class BacklogSyncTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_empty_graph(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            beads_dir = root / "beads"
            beads_dir.mkdir()
            backlog_path = root / "backlog.md"
            backlog_path.write_text(
                "# Work Backlog\n\n"
                f"{TABLES_START}\nOLD TABLES\n{TABLES_END}\n\n"
                "## Milestone 2\nKeep notes\n",
                encoding="utf-8",
            )

            sync_backlog(beads_dir, backlog_path)
            updated = backlog_path.read_text(encoding="utf-8")
            self.assertIn("| _(none)_ | | |", updated)
            self.assertIn("## Ready", updated)
            self.assertIn("## Done", updated)
            self.assertIn("## Milestone 2\nKeep notes", updated)
            self.assertNotIn("OLD TABLES", updated)

    def test_mixed_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            beads_dir = root / "beads"
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "in_progress", ["FACTORY-001"], assignee="agent"),
            )
            self.write_bead(
                beads_dir,
                "FACTORY-003",
                bead_content("FACTORY-003", "C", "ready", ["FACTORY-002"]),
            )
            self.write_bead(
                beads_dir,
                "FACTORY-004",
                bead_content("FACTORY-004", "D", "review"),
            )
            backlog_path = root / "backlog.md"

            sync_backlog(beads_dir, backlog_path)
            updated = backlog_path.read_text(encoding="utf-8")
            self.assertIn("| [FACTORY-001](beads/FACTORY-001.md) | A | done |", updated)
            self.assertIn("| [FACTORY-002](beads/FACTORY-002.md) | B | in_progress |", updated)
            self.assertIn("| [FACTORY-004](beads/FACTORY-004.md) | D | review |", updated)
            self.assertIn("| [FACTORY-003](beads/FACTORY-003.md) | C | FACTORY-002 |", updated)
            self.assertNotIn("| [FACTORY-003](beads/FACTORY-003.md) | C | ready |", updated)

    def test_claim_updates_backlog(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            beads_dir = root / "beads"
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            backlog_path = root / "backlog.md"
            backlog_path.write_text(
                f"{TABLES_START}\nplaceholder\n{TABLES_END}\n",
                encoding="utf-8",
            )

            claim_bead(beads_dir, "FACTORY-002")
            updated = backlog_path.read_text(encoding="utf-8")
            self.assertIn("| [FACTORY-002](beads/FACTORY-002.md) | B | in_progress |", updated)
            self.assertNotIn("| [FACTORY-002](beads/FACTORY-002.md) | B | ready |", updated)

            complete_bead(beads_dir, "FACTORY-002")
            updated = backlog_path.read_text(encoding="utf-8")
            self.assertIn("| [FACTORY-002](beads/FACTORY-002.md) | B | review |", updated)


if __name__ == "__main__":
    unittest.main()
