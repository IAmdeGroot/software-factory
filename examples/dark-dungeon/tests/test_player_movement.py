"""Tests that player movement is wired into the Dark Dungeon project."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PlayerMovementTests(unittest.TestCase):
    def test_player_script_moves_with_wasd_and_arrows(self) -> None:
        path = ROOT / "scripts" / "player.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("extends CharacterBody2D", text)
        self.assertIn("move_and_slide", text)
        self.assertIn("ui_left", text)
        self.assertIn("KEY_W", text)
        self.assertIn("KEY_A", text)
        self.assertIn("KEY_S", text)
        self.assertIn("KEY_D", text)

    def test_player_scene_is_character_body(self) -> None:
        path = ROOT / "scenes" / "player.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("CharacterBody2D", text)
        self.assertIn("res://scripts/player.gd", text)

    def test_main_scene_instances_the_player(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/player.tscn", text)
        self.assertIn("instance=ExtResource", text)


if __name__ == "__main__":
    unittest.main()
