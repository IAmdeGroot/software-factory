"""Tests that defeating the warden reveals a clear beat."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClearBeatTests(unittest.TestCase):
    def test_room_three_has_a_hidden_cleared_label(self) -> None:
        text = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn('[node name="ClearLabel" type="Label" parent="Room3"]', text)
        self.assertIn('text = "Cleared"', text)
        self.assertIn("visible = false", text)

    def test_warden_reveals_cleared_on_death(self) -> None:
        text = (ROOT / "scripts" / "warden.gd").read_text(encoding="utf-8")
        self.assertIn("_show_cleared", text)
        self.assertIn("ClearLabel", text)
        self.assertIn("visible = true", text)
        death = text.split("func take_nail_hit")[1].split("func ")[0]
        self.assertIn("_show_cleared", death)
        self.assertIn("queue_free", death)


if __name__ == "__main__":
    unittest.main()
