"""Tests that the main scene has a bounded room with collision."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BoundedRoomTests(unittest.TestCase):
    def test_main_scene_has_static_walls_and_collision(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn('[node name="Room"', text)
        self.assertIn("StaticBody2D", text)
        self.assertIn("CollisionShape2D", text)
        self.assertIn("NorthWall", text)
        self.assertIn("SouthWall", text)
        self.assertIn("WestWall", text)
        self.assertIn("EastWall", text)
        self.assertIn("ColorRect", text)

    def test_player_still_instances_inside_the_room(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/player.tscn", text)
        self.assertIn("Vector2(640, 360)", text)


if __name__ == "__main__":
    unittest.main()
