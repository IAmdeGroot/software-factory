"""Tests for bead validation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from harness.beads.validate import (
    VALID_STATUSES,
    parse_frontmatter,
    validate_bead_file,
    validate_beads_dir,
)


VALID_BEAD = """---
id: FACTORY-001
title: Example bead
status: ready
dependencies: []
assignee: null
---

# FACTORY-001: Example bead
"""


class ParseFrontmatterTests(unittest.TestCase):
    def test_parses_scalar_fields(self) -> None:
        data, error = parse_frontmatter(VALID_BEAD)
        self.assertIsNone(error)
        self.assertEqual(data["id"], "FACTORY-001")
        self.assertEqual(data["title"], "Example bead")
        self.assertEqual(data["status"], "ready")
        self.assertEqual(data["dependencies"], [])
        self.assertIsNone(data["assignee"])

    def test_parses_dependency_list(self) -> None:
        content = """---
id: FACTORY-002
title: Depends on one
status: blocked
dependencies:
  - FACTORY-001
assignee: null
---
"""
        data, error = parse_frontmatter(content)
        self.assertIsNone(error)
        self.assertEqual(data["dependencies"], ["FACTORY-001"])

    def test_reports_missing_delimiter(self) -> None:
        _, error = parse_frontmatter("# no frontmatter")
        self.assertIn("missing opening", error or "")


class ValidateBeadFileTests(unittest.TestCase):
    def write_bead(self, directory: Path, name: str, content: str) -> Path:
        path = directory / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_bead_has_no_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            self.write_bead(beads_dir, "FACTORY-001.md", VALID_BEAD)
            errors = validate_bead_file(beads_dir / "FACTORY-001.md", {"FACTORY-001"})
            self.assertEqual(errors, [])

    def test_missing_required_field(self) -> None:
        content = """---
id: FACTORY-001
title: Missing status
dependencies: []
---
"""
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            path = self.write_bead(beads_dir, "FACTORY-001.md", content)
            errors = validate_bead_file(path, {"FACTORY-001"})
            self.assertTrue(any("missing required field: status" in str(e) for e in errors))

    def test_invalid_status(self) -> None:
        content = VALID_BEAD.replace("status: ready", "status: pending")
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            path = self.write_bead(beads_dir, "FACTORY-001.md", content)
            errors = validate_bead_file(path, {"FACTORY-001"})
            self.assertTrue(any("invalid status" in str(e) for e in errors))

    def test_id_filename_mismatch(self) -> None:
        content = VALID_BEAD.replace("id: FACTORY-001", "id: FACTORY-999")
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            path = self.write_bead(beads_dir, "FACTORY-001.md", content)
            errors = validate_bead_file(path, {"FACTORY-999"})
            self.assertTrue(any("does not match filename" in str(e) for e in errors))

    def test_unknown_dependency(self) -> None:
        content = """---
id: FACTORY-002
title: Blocked bead
status: blocked
dependencies:
  - FACTORY-999
assignee: null
---
"""
        with tempfile.TemporaryDirectory() as tmp:
            beads_dir = Path(tmp)
            path = self.write_bead(beads_dir, "FACTORY-002.md", content)
            errors = validate_bead_file(path, {"FACTORY-002"})
            self.assertTrue(any("unknown bead" in str(e) for e in errors))


class ValidateBeadsDirTests(unittest.TestCase):
    def test_repo_beads_are_valid(self) -> None:
        repo_root = Path(__file__).resolve().parents[2]
        beads_dir = repo_root / "docs" / "work-graph" / "beads"
        result = validate_beads_dir(beads_dir)
        self.assertTrue(result.ok, "\n".join(str(e) for e in result.errors))

    def test_all_statuses_are_documented(self) -> None:
        expected = {"ready", "in_progress", "review", "done", "blocked"}
        self.assertEqual(VALID_STATUSES, expected)


if __name__ == "__main__":
    unittest.main()
