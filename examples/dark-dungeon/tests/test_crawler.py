"""Tests that a tougher second enemy type is wired into room 2."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SecondEnemyTypeTests(unittest.TestCase):
    def test_crawler_takes_two_nail_hits(self) -> None:
        path = ROOT / "scripts" / "crawler.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("extends Area2D", text)
        self.assertIn("HITS := 2", text)
        self.assertIn("take_nail_hit", text)
        self.assertIn("hits -= amount", text)
        self.assertIn("queue_free", text)
        self.assertIn("take_contact_hit", text)

    def test_crawler_scene_is_monitorable_area(self) -> None:
        path = ROOT / "scenes" / "crawler.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/crawler.gd", text)
        self.assertIn("CollisionShape2D", text)
        self.assertIn("monitorable = true", text)
        self.assertIn("monitoring = true", text)

    def test_main_places_crawler_in_room_two(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/crawler.tscn", text)
        self.assertIn('[node name="Crawler" parent="Room2"', text)
        self.assertIn("res://scenes/enemy.tscn", text)

    def test_first_enemy_still_dies_in_one_hit(self) -> None:
        path = ROOT / "scripts" / "enemy.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("func take_nail_hit", text)
        self.assertIn("queue_free()", text)
        self.assertNotIn("hits -=", text)


if __name__ == "__main__":
    unittest.main()
