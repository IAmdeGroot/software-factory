"""Tests that one strikeable enemy is wired into the room."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StrikeableEnemyTests(unittest.TestCase):
    def test_enemy_script_despawns_on_nail_hit(self) -> None:
        path = ROOT / "scripts" / "enemy.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("extends Area2D", text)
        self.assertIn("take_nail_hit", text)
        self.assertIn("queue_free", text)

    def test_enemy_scene_is_monitorable_area(self) -> None:
        path = ROOT / "scenes" / "enemy.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/enemy.gd", text)
        self.assertIn("CollisionShape2D", text)
        self.assertIn("monitorable = true", text)

    def test_main_scene_instances_the_enemy(self) -> None:
        path = ROOT / "scenes" / "main.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("res://scenes/enemy.tscn", text)
        self.assertIn("2_enemy", text)

    def test_player_nail_can_hit_take_nail_hit(self) -> None:
        path = ROOT / "scripts" / "player.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("area_entered", text)
        self.assertIn("take_nail_hit", text)
        self.assertIn("KEY_J", text)


if __name__ == "__main__":
    unittest.main()
