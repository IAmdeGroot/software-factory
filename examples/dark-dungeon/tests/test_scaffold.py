"""Tests that the Dark Dungeon Godot scaffold files exist."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ScaffoldTests(unittest.TestCase):
    def test_project_godot_exists_and_names_the_game(self) -> None:
        path = ROOT / "project.godot"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("config_version=5", text)
        self.assertIn('config/name="Dark Dungeon"', text)
        self.assertIn('run/main_scene="res://scenes/main.tscn"', text)

    def test_main_scene_is_2d(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Node2D", text)

    def test_godot_cache_is_gitignored(self) -> None:
        path = ROOT / ".gitignore"
        self.assertTrue(path.is_file(), f"missing {path}")
        self.assertIn(".godot/", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
