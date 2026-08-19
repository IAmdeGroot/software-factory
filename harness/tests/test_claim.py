"""Tests for bead claim command."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.claim import ClaimError, claim_bead
from harness.beads.validate import parse_frontmatter


def bead_content(
    bead_id: str, title: str, status: str, dependencies: list[str] | None = None, assignee: str | None = None
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


class ClaimTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_successful_claim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )

            result = claim_bead(beads_dir, "FACTORY-002", assignee="agent")
            self.assertEqual(result.bead_id, "FACTORY-002")

            updated = (beads_dir / "FACTORY-002.md").read_text(encoding="utf-8")
            data, error = parse_frontmatter(updated)
            self.assertIsNone(error)
            self.assertEqual(data["status"], "in_progress")
            self.assertEqual(data["assignee"], "agent")
            self.assertIn("# FACTORY-002: B", updated)

    def test_not_ready_bead(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "review"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )

            with self.assertRaises(ClaimError) as ctx:
                claim_bead(beads_dir, "FACTORY-002")
            self.assertIn("not in the ready queue", str(ctx.exception))

    def test_already_claimed_bead(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "in_progress", ["FACTORY-001"], assignee="agent"),
            )

            with self.assertRaises(ClaimError) as ctx:
                claim_bead(beads_dir, "FACTORY-002")
            self.assertIn("already claimed", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
