"""Tests that two rooms are connected by a doorway and a camera follows."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SecondRoomTests(unittest.TestCase):
    def test_main_scene_has_doorway_and_second_room(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn('[node name="Doorway"', text)
        self.assertIn('[node name="Room2"', text)
        self.assertIn("EastWallNorth", text)
        self.assertIn("EastWallSouth", text)
        self.assertIn("StaticBody2D", text)

    def test_player_has_follow_camera(self) -> None:
        path = ROOT / "scenes" / "player.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn('[node name="Camera2D" type="Camera2D"', text)

    def test_starting_room_and_enemy_remain(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/player.tscn", text)
        self.assertIn("res://scenes/enemy.tscn", text)
        self.assertIn("Vector2(640, 360)", text)


if __name__ == "__main__":
    unittest.main()
