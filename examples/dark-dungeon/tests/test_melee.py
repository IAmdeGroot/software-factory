"""Tests that nail-like melee is wired into the player."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class NailMeleeTests(unittest.TestCase):
    def test_player_script_faces_and_swings_with_recover(self) -> None:
        path = ROOT / "scripts" / "player.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("var facing", text)
        self.assertIn("KEY_J", text)
        self.assertIn("RECOVER", text)
        self.assertIn("_swing", text)
        self.assertIn("nail.monitoring", text)
        self.assertIn("move_and_slide", text)

    def test_player_scene_has_nail_area(self) -> None:
        path = ROOT / "scenes" / "player.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn('[node name="Nail" type="Area2D"', text)
        self.assertIn("CollisionShape2D", text)
        self.assertIn("monitoring = false", text)


if __name__ == "__main__":
    unittest.main()
