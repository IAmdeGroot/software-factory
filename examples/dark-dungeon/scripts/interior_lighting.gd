extends Node2D

## Authored light pools, wall occlusion, and quiet airborne motes.

const LIGHT_TEXTURE := preload("res://assets/visuals/soft_light.svg")

var pulsing_lights: Array[PointLight2D] = []
var base_energy: Array[float] = []


func _ready() -> void:
	var ambient := CanvasModulate.new()
	ambient.name = "DungeonAmbient"
	ambient.color = Color("#596078")
	add_child(ambient)

	# Sacred teal, threshold gold, seal violet, and boss moonlight.
	_add_light(Vector2(360, 224), Color("#78e5d0"), 1.15, 1.15, true)
	_add_light(Vector2(820, 300), Color("#e2a15a"), 0.82, 0.95, false)
	_add_light(Vector2(1056, 360), Color("#c88a4f"), 0.9, 0.72, false)
	_add_light(Vector2(1292, 235), Color("#6e9fc2"), 0.72, 1.0, false)
	_add_light(Vector2(1528, 360), Color("#9d76d6"), 1.15, 0.8, true)
	_add_light(Vector2(1764, 295), Color("#7fc5c9"), 0.95, 1.35, true)

	_add_wall_occluders()
	_add_motes(Vector2(640, 360), Vector2(760, 390), Color("#8dded1", 0.32), 34)
	_add_motes(Vector2(1292, 360), Vector2(390, 390), Color("#ddb06d", 0.25), 20)
	_add_motes(Vector2(1764, 360), Vector2(390, 390), Color("#a98bd7", 0.3), 24)


func _process(_delta: float) -> void:
	var time := Time.get_ticks_msec() * 0.001
	for i in pulsing_lights.size():
		var drift := sin(time * (1.3 + i * 0.17) + i * 1.7) * 0.055
		pulsing_lights[i].energy = base_energy[i] + drift


func _add_light(
	position_value: Vector2,
	color_value: Color,
	energy_value: float,
	scale_value: float,
	pulses: bool
) -> void:
	var light := PointLight2D.new()
	light.position = position_value
	light.texture = LIGHT_TEXTURE
	light.texture_scale = scale_value
	light.color = color_value
	light.energy = energy_value
	light.shadow_enabled = true
	light.shadow_filter = PointLight2D.SHADOW_FILTER_PCF5
	light.shadow_filter_smooth = 3.0
	add_child(light)
	if pulses:
		pulsing_lights.append(light)
		base_energy.append(energy_value)


func _add_wall_occluders() -> void:
	var walls := [
		Rect2(208, 88, 864, 32), Rect2(208, 600, 864, 32),
		Rect2(208, 88, 32, 208), Rect2(208, 424, 32, 208),
		Rect2(1040, 88, 32, 232), Rect2(1040, 400, 32, 232),
		Rect2(1040, 88, 504, 32), Rect2(1040, 600, 504, 32),
		Rect2(1512, 88, 32, 232), Rect2(1512, 400, 32, 232),
		Rect2(1512, 88, 504, 32), Rect2(1512, 600, 504, 32),
		Rect2(1984, 88, 32, 544),
	]
	for wall_rect in walls:
		var polygon := OccluderPolygon2D.new()
		polygon.polygon = PackedVector2Array([
			wall_rect.position,
			Vector2(wall_rect.end.x, wall_rect.position.y),
			wall_rect.end,
			Vector2(wall_rect.position.x, wall_rect.end.y),
		])
		var occluder := LightOccluder2D.new()
		occluder.occluder = polygon
		add_child(occluder)


func _add_motes(
	position_value: Vector2,
	extents: Vector2,
	color_value: Color,
	count: int
) -> void:
	var motes := CPUParticles2D.new()
	motes.position = position_value
	motes.amount = count
	motes.lifetime = 6.0
	motes.randomness = 0.8
	motes.preprocess = 6.0
	motes.texture = LIGHT_TEXTURE
	motes.emission_shape = CPUParticles2D.EMISSION_SHAPE_RECTANGLE
	motes.emission_rect_extents = extents
	motes.direction = Vector2(0, -1)
	motes.spread = 35.0
	motes.gravity = Vector2(0, -1.8)
	motes.initial_velocity_min = 1.0
	motes.initial_velocity_max = 4.0
	motes.scale_amount_min = 0.018
	motes.scale_amount_max = 0.036
	motes.color = color_value
	motes.z_index = 12
	add_child(motes)
