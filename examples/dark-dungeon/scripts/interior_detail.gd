extends Node2D

## Original ink-and-patina dungeon treatment. Gameplay geometry stays separate.

const INK := Color("#090b13")
const STONE_1 := Color("#151827")
const STONE_2 := Color("#111522")
const STONE_3 := Color("#0e111c")
const GROUT := Color("#272b3d")
const PATINA := Color("#315653")
const GOLD := Color("#a87b42")


func _ready() -> void:
	queue_redraw()


func _draw() -> void:
	_draw_room(Rect2(240, 120, 832, 480), STONE_1, 0)
	_draw_room(Rect2(1072, 120, 440, 480), STONE_2, 1)
	_draw_room(Rect2(1544, 120, 440, 480), STONE_3, 2)
	_draw_walls()
	_draw_room_marks()


func _draw_room(area: Rect2, base: Color, phase: int) -> void:
	draw_rect(area, base)
	var tile := 64
	for y in range(int(area.position.y), int(area.end.y), tile):
		var row := int((y - area.position.y) / tile)
		var shift := 32 if (row + phase) % 2 else 0
		for x in range(int(area.position.x) - shift, int(area.end.x), tile):
			var tile_rect := Rect2(x, y, tile, tile)
			var clipped := tile_rect.intersection(area)
			draw_rect(clipped, GROUT, false, 1.5)
	for i in range(8):
		var px := area.position.x + 45.0 + fmod(i * 113.0 + phase * 41.0, area.size.x - 90.0)
		var py := area.position.y + 38.0 + fmod(i * 71.0 + phase * 53.0, area.size.y - 76.0)
		draw_polyline(
			PackedVector2Array([
				Vector2(px - 15, py - 4),
				Vector2(px - 3, py + 2),
				Vector2(px + 5, py - 7),
				Vector2(px + 17, py + 4),
			]),
			PATINA.darkened(0.22),
			2.0,
			true
		)


func _draw_walls() -> void:
	var wall := Color("#30313d")
	var edge := Color("#555461")
	var walls := [
		Rect2(208, 88, 864, 32), Rect2(208, 600, 864, 32),
		Rect2(208, 88, 32, 544),
		Rect2(1040, 88, 32, 232), Rect2(1040, 400, 32, 232),
		Rect2(1040, 88, 504, 32), Rect2(1040, 600, 504, 32),
		Rect2(1512, 88, 32, 232), Rect2(1512, 400, 32, 232),
		Rect2(1512, 88, 504, 32), Rect2(1512, 600, 504, 32),
		Rect2(1984, 88, 32, 544),
	]
	for wall_rect in walls:
		draw_rect(wall_rect, INK)
		draw_rect(wall_rect.grow(-4), wall)
		draw_line(wall_rect.position + Vector2(4, 5), Vector2(wall_rect.end.x - 4, wall_rect.position.y + 5), edge, 2)

	for x in range(240, 1984, 96):
		draw_line(Vector2(x, 94), Vector2(x - 9, 114), PATINA, 2)
		draw_line(Vector2(x + 31, 606), Vector2(x + 42, 626), PATINA.darkened(0.2), 2)

	# Tarnished thresholds make progression doors readable.
	for x in [1056.0, 1528.0]:
		draw_line(Vector2(x - 17, 319), Vector2(x - 17, 401), GOLD, 3)
		draw_line(Vector2(x + 17, 319), Vector2(x + 17, 401), GOLD.darkened(0.35), 3)


func _draw_room_marks() -> void:
	# Inlaid circles visually anchor shrine, hunt, and warden spaces.
	for mark in [
		[Vector2(360, 240), 62.0, PATINA],
		[Vector2(1292, 360), 72.0, Color("#55333c")],
		[Vector2(1764, 360), 94.0, Color("#493457")],
	]:
		draw_circle(mark[0], mark[1], mark[2].darkened(0.45), false, 3.0, true)
		draw_circle(mark[0], mark[1] - 9.0, mark[2].lightened(0.08), false, 1.5, true)
