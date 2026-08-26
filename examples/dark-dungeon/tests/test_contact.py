"""Tests that enemy contact damages the player and HP/respawn is wired."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContactDamageTests(unittest.TestCase):
    def test_player_has_hp_iframes_and_respawn(self) -> None:
        path = ROOT / "scripts" / "player.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("MAX_HP", text)
        self.assertIn("take_contact_hit", text)
        self.assertIn("IFRAMES", text)
        self.assertIn("_respawn", text)
        self.assertIn("spawn_position", text)
        self.assertIn("move_and_slide", text)
        self.assertIn("KEY_J", text)

    def test_player_scene_shows_hp(self) -> None:
        path = ROOT / "scenes" / "player.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn('[node name="HpLabel" type="Label"', text)

    def test_enemy_reports_contact_on_body_entered(self) -> None:
        path = ROOT / "scripts" / "enemy.gd"
        text = path.read_text(encoding="utf-8")
        self.assertIn("body_entered", text)
        self.assertIn("take_contact_hit", text)
        self.assertIn("take_nail_hit", text)

    def test_enemy_monitors_the_player_body(self) -> None:
        path = ROOT / "scenes" / "enemy.tscn"
        text = path.read_text(encoding="utf-8")
        self.assertIn("monitoring = true", text)
        self.assertIn("monitorable = true", text)


if __name__ == "__main__":
    unittest.main()
