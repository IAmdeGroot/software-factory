"""Tests for bead complete and done commands."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.status import TransitionError, complete_bead, done_bead
from harness.beads.validate import parse_frontmatter


def bead_content(
    bead_id: str,
    title: str,
    status: str,
    dependencies: list[str] | None = None,
    assignee: str | None = None,
    body: str | None = None,
) -> str:
    deps = dependencies or []
    deps_field = "[]"
    if deps:
        deps_field = "\n" + "\n".join(f"  - {dep}" for dep in deps)
    assignee_value = "null" if assignee is None else assignee
    extra_body = body if body is not None else f"# {bead_id}: {title}\n"
    return (
        "---\n"
        f"id: {bead_id}\n"
        f"title: {title}\n"
        f"status: {status}\n"
        f"dependencies: {deps_field}\n"
        f"assignee: {assignee_value}\n"
        "---\n\n"
        f"{extra_body}"
    )


class StatusTransitionTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_successful_complete(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(
                beads_dir,
                "FACTORY-007",
                bead_content(
                    "FACTORY-007",
                    "Close loop",
                    "in_progress",
                    assignee="agent",
                    body="# FACTORY-007: Close loop\n\nKeep this body.\n",
                ),
            )

            result = complete_bead(beads_dir, "FACTORY-007")
            self.assertEqual(result.bead_id, "FACTORY-007")
            self.assertEqual(result.from_status, "in_progress")
            self.assertEqual(result.to_status, "review")

            updated = (beads_dir / "FACTORY-007.md").read_text(encoding="utf-8")
            data, error = parse_frontmatter(updated)
            self.assertIsNone(error)
            self.assertEqual(data["status"], "review")
            self.assertEqual(data["assignee"], "agent")
            self.assertIn("Keep this body.", updated)

    def test_successful_done(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(
                beads_dir,
                "FACTORY-007",
                bead_content(
                    "FACTORY-007",
                    "Close loop",
                    "review",
                    assignee="agent",
                    body="# FACTORY-007: Close loop\n\nReviewed body.\n",
                ),
            )

            result = done_bead(beads_dir, "FACTORY-007")
            self.assertEqual(result.to_status, "done")

            updated = (beads_dir / "FACTORY-007.md").read_text(encoding="utf-8")
            data, error = parse_frontmatter(updated)
            self.assertIsNone(error)
            self.assertEqual(data["status"], "done")
            self.assertIn("Reviewed body.", updated)

    def test_complete_wrong_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(
                beads_dir,
                "FACTORY-007",
                bead_content("FACTORY-007", "Close loop", "ready"),
            )

            with self.assertRaises(TransitionError) as ctx:
                complete_bead(beads_dir, "FACTORY-007")
            self.assertIn("expected 'in_progress'", str(ctx.exception))

    def test_done_wrong_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(
                beads_dir,
                "FACTORY-007",
                bead_content("FACTORY-007", "Close loop", "in_progress", assignee="agent"),
            )

            with self.assertRaises(TransitionError) as ctx:
                done_bead(beads_dir, "FACTORY-007")
            self.assertIn("expected 'review'", str(ctx.exception))

    def test_missing_bead(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            with self.assertRaises(TransitionError) as ctx:
                complete_bead(beads_dir, "FACTORY-999")
            self.assertIn("not found", str(ctx.exception))

            with self.assertRaises(TransitionError) as ctx:
                done_bead(beads_dir, "FACTORY-999")
            self.assertIn("not found", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
