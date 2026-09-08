"""Tests for the authored dark-fantasy visual foundation."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VisualFoundationTests(unittest.TestCase):
    def test_authored_visual_assets_exist(self) -> None:
        assets = ROOT / "assets" / "visuals"
        expected = {
            "player.svg",
            "nail.svg",
            "enemy.svg",
            "crawler.svg",
            "skitter.svg",
            "warden.svg",
            "shrine.svg",
            "seal.svg",
            "shard.svg",
        }
        self.assertTrue(expected.issubset({path.name for path in assets.glob("*.svg")}))

    def test_actor_scenes_use_sprite_visuals(self) -> None:
        for scene_name in (
            "player",
            "enemy",
            "crawler",
            "skitter",
            "warden",
            "shrine",
            "seal",
            "shard",
        ):
            text = (ROOT / "scenes" / f"{scene_name}.tscn").read_text(encoding="utf-8")
            self.assertIn("Sprite2D", text, scene_name)
            self.assertIn("res://assets/visuals/", text, scene_name)

    def test_main_scene_uses_authored_interior_detail(self) -> None:
        text = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn("res://scripts/interior_detail.gd", text)
        detail = (ROOT / "scripts" / "interior_detail.gd").read_text(encoding="utf-8")
        self.assertIn("_draw_room", detail)
        self.assertIn("_draw_walls", detail)

    def test_interior_has_authored_light_shadow_and_motes(self) -> None:
        main = (ROOT / "scenes" / "main.tscn").read_text(encoding="utf-8")
        self.assertIn("res://scripts/interior_lighting.gd", main)
        lighting = (ROOT / "scripts" / "interior_lighting.gd").read_text(
            encoding="utf-8"
        )
        self.assertIn("CanvasModulate", lighting)
        self.assertGreaterEqual(lighting.count("_add_light(Vector2"), 6)
        self.assertIn("LightOccluder2D", lighting)
        self.assertIn("CPUParticles2D", lighting)
        self.assertIn("motes.texture = LIGHT_TEXTURE", lighting)
        self.assertIn("shadow_enabled = true", lighting)


if __name__ == "__main__":
    unittest.main()
