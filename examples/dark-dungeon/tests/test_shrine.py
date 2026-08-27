"""Tests that a shrine in room 1 spends shards to hone the nail."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class NailShrineTests(unittest.TestCase):
    def test_shrine_spends_two_shards(self) -> None:
        path = ROOT / "scripts" / "shrine.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("COST := 2", text)
        self.assertIn("hone_nail", text)
        self.assertIn("body_entered", text)

    def test_shrine_scene_monitors_the_player(self) -> None:
        path = ROOT / "scenes" / "shrine.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/shrine.gd", text)
        self.assertIn("monitoring = true", text)

    def test_main_places_shrine_in_room_one(self) -> None:
        text = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn("res://scenes/shrine.tscn", text)
        self.assertIn('[node name="Shrine" parent="Room"', text)

    def test_player_hones_nail_with_shards(self) -> None:
        text = (ROOT / "scripts" / "player.gd").read_text(encoding="utf-8")
        self.assertIn("nail_damage", text)
        self.assertIn("func hone_nail", text)
        self.assertIn("shards -= cost", text)
        self.assertIn("take_nail_hit(nail_damage)", text)
        respawn = text.split("func _respawn")[1].split("func ")[0]
        self.assertNotIn("nail_damage = 1", respawn)
        self.assertNotIn("shards = 0", respawn)

    def test_crawler_uses_nail_damage(self) -> None:
        text = (ROOT / "scripts" / "crawler.gd").read_text(encoding="utf-8")
        self.assertIn("HITS := 2", text)
        self.assertIn("hits -= amount", text)


if __name__ == "__main__":
    unittest.main()
