"""Tests for the markdown wish drop."""

from __future__ import annotations

import json
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from harness.beads.__main__ import main
from harness.beads.wishes import (
    WISH_STATUSES,
    build_open_wishes,
    format_wishes_text,
    validate_wish_file,
    validate_wishes_dir,
    wishes_to_json,
)


def wish_content(
    wish_id: str,
    title: str,
    status: str,
    source: str = "human",
) -> str:
    return (
        "---\n"
        f"id: {wish_id}\n"
        f"title: {title}\n"
        f"status: {status}\n"
        f"source: {source}\n"
        "---\n\n"
        f"# {wish_id}: {title}\n"
    )


class WishListTests(unittest.TestCase):
    def write_wish(self, directory: Path, wish_id: str, content: str) -> None:
        (directory / f"{wish_id}.md").write_text(content, encoding="utf-8")

    def test_empty_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp)
            wishes = build_open_wishes(wishes_dir)
            self.assertEqual(wishes, [])
            self.assertIn("(none)", format_wishes_text(wishes))
            payload = json.loads(wishes_to_json(wishes))
            self.assertEqual(payload["count"], 0)
            self.assertEqual(payload["wishes"], [])

    def test_cli_wishes_json_empty_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with patch("sys.stdout", new_callable=StringIO) as stdout:
                code = main(["wishes", tmp, "--json"])
            self.assertEqual(code, 0)
            payload = json.loads(stdout.getvalue())
            self.assertEqual(payload["count"], 0)

    def test_missing_directory_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp) / "missing"
            self.assertEqual(build_open_wishes(wishes_dir), [])
            self.assertTrue(validate_wishes_dir(wishes_dir).ok)

    def test_lists_open_wishes_sorted_by_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp)
            self.write_wish(
                wishes_dir, "WISH-002", wish_content("WISH-002", "Second", "open")
            )
            self.write_wish(
                wishes_dir, "WISH-001", wish_content("WISH-001", "First", "open")
            )
            self.write_wish(
                wishes_dir, "WISH-003", wish_content("WISH-003", "Later", "planned")
            )
            self.write_wish(
                wishes_dir, "WISH-004", wish_content("WISH-004", "Closed", "done")
            )
            wishes = build_open_wishes(wishes_dir)
            self.assertEqual([item["id"] for item in wishes], ["WISH-001", "WISH-002"])
            text = format_wishes_text(wishes)
            self.assertIn("WISH-001: First", text)
            self.assertNotIn("WISH-003", text)

    def test_ignores_non_wish_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp)
            (wishes_dir / "README.md").write_text("# not a wish\n", encoding="utf-8")
            self.assertEqual(build_open_wishes(wishes_dir), [])
            self.assertTrue(validate_wishes_dir(wishes_dir).ok)


class WishValidateTests(unittest.TestCase):
    def write_wish(self, directory: Path, name: str, content: str) -> Path:
        path = directory / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_invalid_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_wish(
                Path(tmp),
                "WISH-001.md",
                wish_content("WISH-001", "Bad", "pending"),
            )
            errors = validate_wish_file(path)
            self.assertTrue(any("invalid status" in str(e) for e in errors))

    def test_missing_source(self) -> None:
        content = """---
id: WISH-001
title: No source
status: open
---
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_wish(Path(tmp), "WISH-001.md", content)
            errors = validate_wish_file(path)
            self.assertTrue(any("missing required field: source" in str(e) for e in errors))

    def test_valid_open_wish(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp)
            self.write_wish(
                wishes_dir,
                "WISH-001.md",
                wish_content("WISH-001", "A torch", "open", "playtest"),
            )
            result = validate_wishes_dir(wishes_dir)
            self.assertTrue(result.ok, "\n".join(str(e) for e in result.errors))

    def test_wish_statuses_are_documented(self) -> None:
        self.assertEqual(WISH_STATUSES, {"open", "planned", "done"})

    def test_planned_wish_requires_beads(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_wish(
                Path(tmp),
                "WISH-001.md",
                wish_content("WISH-001", "Needs beads", "planned"),
            )
            errors = validate_wish_file(path)
            self.assertTrue(any("must list bead ids" in str(e) for e in errors))

    def test_planned_wish_with_beads_is_valid(self) -> None:
        content = (
            "---\n"
            "id: WISH-001\n"
            "title: Nail feel\n"
            "status: planned\n"
            "source: human\n"
            "beads:\n"
            "  - DUNGEON-004\n"
            "  - FACTORY-021\n"
            "---\n\n"
            "# WISH-001: Nail feel\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            wishes_dir = Path(tmp)
            self.write_wish(wishes_dir, "WISH-001.md", content)
            result = validate_wishes_dir(wishes_dir)
            self.assertTrue(result.ok, "\n".join(str(e) for e in result.errors))

    def test_planned_wish_rejects_bad_bead_prefix(self) -> None:
        content = (
            "---\n"
            "id: WISH-001\n"
            "title: Bad prefix\n"
            "status: planned\n"
            "source: human\n"
            "beads:\n"
            "  - ISSUE-001\n"
            "---\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_wish(Path(tmp), "WISH-001.md", content)
            errors = validate_wish_file(path)
            self.assertTrue(any("invalid bead id" in str(e) for e in errors))


class WishPlannerSkillTests(unittest.TestCase):
    def test_skill_stops_on_empty_wish_list(self) -> None:
        root = Path(__file__).resolve().parents[2]
        path = root / ".cursor" / "skills" / "wish-planner" / "SKILL.md"
        self.assertTrue(path.is_file(), f"missing skill: {path}")
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        self.assertIn("empty wish list", lowered)
        self.assertIn("do not invent wishes", lowered)
        self.assertIn("DUNGEON-", text)
        self.assertIn("FACTORY-", text)
        self.assertIn("planned", lowered)


if __name__ == "__main__":
    unittest.main()
