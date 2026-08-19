"""Tests for bead status listing."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.listing import build_ready_queue, build_status_summary


def bead_content(
    bead_id: str, title: str, status: str, dependencies: list[str] | None = None
) -> str:
    deps = dependencies or []
    deps_field = "[]"
    if deps:
        deps_field = "\n" + "\n".join(f"  - {dep}" for dep in deps)
    return (
        "---\n"
        f"id: {bead_id}\n"
        f"title: {title}\n"
        f"status: {status}\n"
        f"dependencies: {deps_field}\n"
        "assignee: null\n"
        "---\n"
    )


class ListingTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_all_ready(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            summary = build_status_summary(beads_dir)
            ready_ids = {item["id"] for item in summary["ready"]}
            self.assertIn("FACTORY-002", ready_ids)

    def test_blocked_by_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "review"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            summary = build_status_summary(beads_dir)
            blocked = {item["id"]: item["waiting_on"] for item in summary["blocked"]}
            self.assertIn("FACTORY-002", blocked)
            self.assertEqual(blocked["FACTORY-002"], ["FACTORY-001"])

    def test_mixed_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "blocked", ["FACTORY-001"]),
            )
            self.write_bead(beads_dir, "FACTORY-003", bead_content("FACTORY-003", "C", "in_progress"))
            summary = build_status_summary(beads_dir)

            statuses = {item["id"]: item["status"] for item in summary["beads"]}
            self.assertEqual(statuses["FACTORY-001"], "done")
            self.assertEqual(statuses["FACTORY-002"], "blocked")
            self.assertEqual(statuses["FACTORY-003"], "in_progress")


class ReadyQueueTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_empty_queue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            ready = build_ready_queue(beads_dir)
            self.assertEqual(ready, [])

    def test_one_ready_bead(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            ready = build_ready_queue(beads_dir)
            self.assertEqual([item["id"] for item in ready], ["FACTORY-002"])

    def test_ready_bead_blocked_by_incomplete_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "review"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            ready = build_ready_queue(beads_dir)
            self.assertEqual(ready, [])


if __name__ == "__main__":
    unittest.main()
