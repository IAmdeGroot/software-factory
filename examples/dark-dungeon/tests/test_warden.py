"""Tests that a slow warden boss is wired into room 3."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Room3BossTests(unittest.TestCase):
    def test_warden_takes_six_hits_and_patrols(self) -> None:
        path = ROOT / "scripts" / "warden.gd"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("HITS := 6", text)
        self.assertIn("SPEED", text)
        self.assertIn("X_MIN", text)
        self.assertIn("X_MAX", text)
        self.assertIn("func _process", text)
        self.assertIn("position.x", text)
        self.assertIn("hits -= amount", text)
        self.assertIn("take_contact_hit", text)
        self.assertNotIn('get_node("Player")', text)
        self.assertNotIn("chase", text.lower())

    def test_warden_scene_is_larger_monitorable_area(self) -> None:
        path = ROOT / "scenes" / "warden.tscn"
        self.assertTrue(path.is_file(), f"missing {path}")
        text = path.read_text(encoding="utf-8")
        self.assertIn("Area2D", text)
        self.assertIn("res://scripts/warden.gd", text)
        self.assertIn("Vector2(40, 32)", text)
        self.assertIn("monitorable = true", text)

    def test_main_places_warden_in_room_three(self) -> None:
        text = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn("res://scenes/warden.tscn", text)
        self.assertIn('[node name="Warden" parent="Room3"', text)
        self.assertIn("res://scenes/seal.tscn", text)


if __name__ == "__main__":
    unittest.main()
