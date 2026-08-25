"""Tests for claiming the next ready bead."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.claim import ClaimError, claim_next
from harness.beads.validate import parse_frontmatter


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


class NextClaimTests(unittest.TestCase):
    def write_bead(self, directory: Path, bead_id: str, content: str) -> None:
        (directory / f"{bead_id}.md").write_text(content, encoding="utf-8")

    def test_claims_first_ready_bead(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))
            self.write_bead(
                beads_dir,
                "FACTORY-003",
                bead_content("FACTORY-003", "C", "ready", ["FACTORY-001"]),
            )
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )

            result = claim_next(beads_dir, assignee="worker")
            self.assertEqual(result.bead_id, "FACTORY-002")
            self.assertEqual(result.title, "B")
            self.assertEqual(result.assignee, "worker")

            claimed = parse_frontmatter((beads_dir / "FACTORY-002.md").read_text(encoding="utf-8"))[0]
            untouched = parse_frontmatter((beads_dir / "FACTORY-003.md").read_text(encoding="utf-8"))[0]
            self.assertEqual(claimed["status"], "in_progress")
            self.assertEqual(untouched["status"], "ready")

    def test_empty_queue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "done"))

            with self.assertRaises(ClaimError) as ctx:
                claim_next(beads_dir)
            self.assertIn("ready queue is empty", str(ctx.exception))

    def test_skips_non_ready_beads(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001", bead_content("FACTORY-001", "A", "review"))
            self.write_bead(
                beads_dir,
                "FACTORY-002",
                bead_content("FACTORY-002", "B", "ready", ["FACTORY-001"]),
            )
            self.write_bead(beads_dir, "FACTORY-003", bead_content("FACTORY-003", "C", "ready"))

            result = claim_next(beads_dir)
            self.assertEqual(result.bead_id, "FACTORY-003")

            skipped = parse_frontmatter((beads_dir / "FACTORY-002.md").read_text(encoding="utf-8"))[0]
            self.assertEqual(skipped["status"], "ready")


if __name__ == "__main__":
    unittest.main()
