"""Tests that foes drop shards and the player can collect them."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ShardLootTests(unittest.TestCase):
    def test_shard_collects_on_player_overlap(self) -> None:
        path = ROOT / "scripts" / "shard.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("extends Area2D", text)
        self.assertIn("body_entered", text)
        self.assertIn("take_shard", text)
        self.assertIn("queue_free", text)

    def test_shard_scene_is_a_monitorable_area(self) -> None:
        path = ROOT / "scenes" / "shard.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/shard.gd", text)
        self.assertIn("monitoring = true", text)

    def test_player_counts_shards_and_keeps_them_on_respawn(self) -> None:
        path = ROOT / "scripts" / "player.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("func take_shard", text)
        self.assertIn("shards += 1", text)
        self.assertIn("ShardLabel", text)
        respawn = text.split("func _respawn")[1].split("func ")[0]
        self.assertNotIn("shards = 0", respawn)
        self.assertIn("hp = MAX_HP", respawn)

    def test_player_scene_shows_shard_count(self) -> None:
        text = (ROOT / "scenes" / "player.tscn").read_text(encoding="utf-8")
        self.assertIn('[node name="ShardLabel" type="Label"', text)
        self.assertIn('[node name="HpLabel" type="Label"', text)

    def test_foes_drop_a_shard_on_death(self) -> None:
        for name in ("enemy.gd", "crawler.gd", "skitter.gd"):
            text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
            self.assertIn("res://scenes/shard.tscn", text, f"{name} should drop a shard")
            self.assertIn("_drop_shard", text)
            self.assertIn("queue_free", text)


if __name__ == "__main__":
    unittest.main()
