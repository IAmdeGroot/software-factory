"""Tests that a honed nail breaks a seal into a third room."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HonedSealTests(unittest.TestCase):
    def test_seal_breaks_only_with_damage_two(self) -> None:
        path = ROOT / "scripts" / "seal.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("NEED := 2", text)
        self.assertIn("take_nail_hit", text)
        self.assertIn("amount < NEED", text)
        self.assertIn("queue_free", text)

    def test_seal_scene_blocks_and_is_strikeable(self) -> None:
        path = ROOT / "scenes" / "seal.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("StaticBody2D", text)
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/seal.gd", text)
        self.assertIn("monitorable = true", text)

    def test_main_places_seal_and_third_room(self) -> None:
        text = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn("res://scenes/seal.tscn", text)
        self.assertIn('[node name="Seal" parent="Room2"', text)
        self.assertIn('[node name="Room3"', text)
        self.assertIn("SealedDoorway", text)


if __name__ == "__main__":
    unittest.main()
