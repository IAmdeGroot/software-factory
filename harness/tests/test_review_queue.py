"""Tests for the review-queue command."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.listing import build_review_queue


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


class ReviewQueueTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_empty_queue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.assertEqual(build_review_queue(beads_dir), [])

    def test_one_bead_in_review(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(beads_dir, "FACTORY-002", bead_content("FACTORY-002", "B", "review"))
            review = build_review_queue(beads_dir)
            self.assertEqual([item["id"] for item in review], ["FACTORY-002"])
            self.assertEqual(review[0]["title"], "B")

    def test_mixed_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(beads_dir, "FACTORY-003", bead_content("FACTORY-003", "C", "review"))
            self.write_bead(beads_dir, "FACTORY-002", bead_content("FACTORY-002", "B", "in_progress"))
            self.write_bead(beads_dir, "FACTORY-004", bead_content("FACTORY-004", "D", "review"))
            review = build_review_queue(beads_dir)
            self.assertEqual([item["id"] for item in review], ["FACTORY-003", "FACTORY-004"])


if __name__ == "__main__":
    unittest.main()
