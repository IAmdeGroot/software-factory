extends Node2D

## The moonken approach: layered scale/value/fog outside, framed by near roots.

const LIGHT_TEXTURE := preload("res://assets/visuals/soft_light.svg")
@export var foreground_only := false


func _ready() -> void:
	if foreground_only:
		queue_redraw()
		return
	_add_moonlight()
	_add_fog()
	queue_redraw()


func _draw() -> void:
	if foreground_only:
		_draw_foreground()
		return
	_draw_far_plane()
	_draw_middle_plane()
	_draw_near_plane()
	_draw_playable_terrace()


func _draw_far_plane() -> void:
	# Plane 1: pale sky and tiny distant teeth.
	draw_rect(Rect2(-1400, -600, 1624, 1800), Color("#111a28"))
	draw_circle(Vector2(-390, -34), 74, Color("#78949a"))
	draw_circle(Vector2(-390, -34), 62, Color("#b1c4b4"))
	var horizon := PackedVector2Array([
		Vector2(-1400, 130), Vector2(-1400, 72), Vector2(-1320, 20),
		Vector2(-1240, 68), Vector2(-1160, 2), Vector2(-1080, 62),
		Vector2(-1000, 27), Vector2(-920, 75), Vector2(-840, 12),
		Vector2(-760, 67), Vector2(-672, 60), Vector2(-610, 22),
		Vector2(-555, 74), Vector2(-490, 8), Vector2(-425, 65),
		Vector2(-350, 28), Vector2(-270, 81), Vector2(-190, 17),
		Vector2(-115, 70), Vector2(-35, 31), Vector2(60, 76),
		Vector2(224, 45), Vector2(224, 130),
	])
	draw_colored_polygon(horizon, Color("#1b2935"))
	for x in range(-1360, 180, 108):
		draw_line(Vector2(x, 78), Vector2(x + 13, -6), Color("#263b45"), 9)
		draw_circle(Vector2(x + 13, -8), 11, Color("#263b45"))


func _draw_middle_plane() -> void:
	# Plane 2: larger ruined arches, softened by a teal fog band.
	for x in range(-1380, 170, 168):
		draw_arc(Vector2(x + 72, 120), 68, PI, TAU, 24, Color("#26383f"), 20, true)
		draw_line(Vector2(x + 4, 118), Vector2(x + 4, 42), Color("#26383f"), 20)
		draw_line(Vector2(x + 140, 118), Vector2(x + 140, 42), Color("#26383f"), 20)
	draw_rect(Rect2(-1400, 76, 1624, 76), Color("#416461", 0.22))


func _draw_near_plane() -> void:
	# Plane 3: high-contrast cliff teeth and broken gold waystones.
	var cliff := PackedVector2Array([
		Vector2(-1400, 174), Vector2(-1320, 122), Vector2(-1230, 158),
		Vector2(-1140, 112), Vector2(-1040, 155), Vector2(-940, 118),
		Vector2(-840, 160), Vector2(-760, 120), Vector2(-672, 174),
		Vector2(-630, 128), Vector2(-565, 153),
		Vector2(-502, 109), Vector2(-430, 158), Vector2(-355, 121),
		Vector2(-276, 163), Vector2(-195, 116), Vector2(-118, 151),
		Vector2(-42, 125), Vector2(45, 161), Vector2(126, 119),
		Vector2(224, 154), Vector2(224, 220), Vector2(-1400, 220),
	])
	draw_colored_polygon(cliff, Color("#17242b"))
	for x in [-570.0, -300.0, -32.0]:
		draw_rect(Rect2(x, 114, 16, 78), Color("#171a24"))
		draw_rect(Rect2(x + 4, 118, 8, 64), Color("#a87b42"))


func _draw_playable_terrace() -> void:
	var terrace := Rect2(-1400, 120, 1608, 900)
	draw_rect(terrace, Color("#152329"))
	for y in range(152, 1020, 64):
		draw_line(Vector2(-1400, y), Vector2(208, y), Color("#294047"), 2)
	for x in range(-1380, 208, 72):
		draw_line(Vector2(x, 120), Vector2(x - 22, 1020), Color("#22363d"), 2)
	var path := PackedVector2Array([
		Vector2(-640, 305), Vector2(-505, 278), Vector2(-370, 316),
		Vector2(-222, 292), Vector2(-80, 326), Vector2(208, 318),
		Vector2(208, 402), Vector2(-70, 405), Vector2(-225, 430),
		Vector2(-380, 397), Vector2(-520, 430), Vector2(-640, 410),
	])
	draw_colored_polygon(path, Color("#26343b"))
	draw_polyline(path, Color("#5b665e"), 3, true)
	for x in range(-580, 150, 126):
		draw_polyline(
			PackedVector2Array([
				Vector2(x, 350), Vector2(x + 19, 341),
				Vector2(x + 31, 357), Vector2(x + 49, 348),
			]),
			Color("#3b5754"),
			2,
			true
		)
	# Warm threshold is the visual handoff to the interior.
	draw_rect(Rect2(208, 296, 32, 128), Color("#0b0d15"))
	draw_line(Vector2(211, 296), Vector2(211, 424), Color("#d49a52"), 4)


func _draw_foreground() -> void:
	var ink := Color("#080b11")
	# Near roots frame edges but leave the central path clear.
	draw_polyline(
		PackedVector2Array([
			Vector2(-660, 610), Vector2(-612, 530), Vector2(-628, 455),
			Vector2(-585, 392), Vector2(-610, 318),
		]),
		ink,
		24,
		true
	)
	draw_polyline(
		PackedVector2Array([
			Vector2(220, 606), Vector2(166, 544), Vector2(186, 474),
			Vector2(145, 430),
		]),
		ink,
		20,
		true
	)
	for x in [-545.0, -118.0]:
		draw_line(Vector2(x, 600), Vector2(x - 18, 535), Color("#101820"), 12)
		draw_circle(Vector2(x - 21, 525), 18, Color("#17272a"))


func _add_moonlight() -> void:
	var moonlight := PointLight2D.new()
	moonlight.position = Vector2(-390, 128)
	moonlight.texture = LIGHT_TEXTURE
	moonlight.texture_scale = 3.4
	moonlight.color = Color("#8fc7c4")
	moonlight.energy = 1.35
	moonlight.shadow_enabled = true
	add_child(moonlight)


func _add_fog() -> void:
	var fog := CPUParticles2D.new()
	fog.position = Vector2(-225, 155)
	fog.amount = 14
	fog.lifetime = 12.0
	fog.preprocess = 12.0
	fog.randomness = 0.85
	fog.texture = LIGHT_TEXTURE
	fog.emission_shape = CPUParticles2D.EMISSION_SHAPE_RECTANGLE
	fog.emission_rect_extents = Vector2(390, 62)
	fog.direction = Vector2(1, 0)
	fog.spread = 12.0
	fog.initial_velocity_min = 4.0
	fog.initial_velocity_max = 11.0
	fog.scale_amount_min = 0.25
	fog.scale_amount_max = 0.55
	fog.color = Color("#6d9894", 0.08)
	fog.z_index = 1
	add_child(fog)
