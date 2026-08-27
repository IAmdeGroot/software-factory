"""Tests that a patrolling third enemy type is wired into room 2."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PatrolFoeTests(unittest.TestCase):
    def test_skitter_patrols_and_dies_in_one_hit(self) -> None:
        path = ROOT / "scripts" / "skitter.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("extends Area2D", text)
        self.assertIn("SPEED", text)
        self.assertIn("Y_MIN", text)
        self.assertIn("Y_MAX", text)
        self.assertIn("func _process", text)
        self.assertIn("position.y", text)
        self.assertIn("take_nail_hit", text)
        self.assertIn("queue_free", text)
        self.assertIn("take_contact_hit", text)
        self.assertNotIn("hits -= 1", text)

    def test_skitter_does_not_chase_the_player(self) -> None:
        text = (ROOT / "scripts" / "skitter.gd").read_text(encoding="utf-8")
        lowered = text.lower()
        self.assertNotIn("chase", lowered)
        self.assertNotIn("get_node", lowered)
        self.assertIn("dir", text)

    def test_skitter_scene_is_monitorable_area(self) -> None:
        path = ROOT / "scenes" / "skitter.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/skitter.gd", text)
        self.assertIn("CollisionShape2D", text)
        self.assertIn("monitorable = true", text)
        self.assertIn("monitoring = true", text)

    def test_main_places_skitter_in_room_two(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/skitter.tscn", text)
        self.assertIn('[node name="Skitter" parent="Room2"', text)
        self.assertIn("res://scenes/crawler.tscn", text)
        self.assertIn("res://scenes/enemy.tscn", text)


if __name__ == "__main__":
    unittest.main()
