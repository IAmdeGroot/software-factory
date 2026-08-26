extends CharacterBody2D

const SPEED := 200.0
const RECOVER := 0.28
const NAIL_ACTIVE := 0.12

var facing := Vector2.RIGHT
var recover := 0.0
var nail_active := 0.0

@onready var nail: Area2D = $Nail
@onready var nail_visible: ColorRect = $Nail/Visible


func _ready() -> void:
	nail.area_entered.connect(_on_nail_area_entered)


func _physics_process(delta: float) -> void:
	recover = maxf(0.0, recover - delta)
	if nail_active > 0.0:
		nail_active = maxf(0.0, nail_active - delta)
		if nail_active == 0.0:
			_sheathe()

	var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	if Input.is_physical_key_pressed(KEY_A):
		direction.x -= 1.0
	if Input.is_physical_key_pressed(KEY_D):
		direction.x += 1.0
	if Input.is_physical_key_pressed(KEY_W):
		direction.y -= 1.0
	if Input.is_physical_key_pressed(KEY_S):
		direction.y += 1.0
	direction = direction.limit_length(1.0)
	if direction.length() > 0.05:
		facing = direction.normalized()
	nail.rotation = facing.angle()

	if recover <= 0.0 and Input.is_physical_key_pressed(KEY_J):
		_swing()

	velocity = direction * SPEED
	move_and_slide()


func _swing() -> void:
	recover = RECOVER
	nail_active = NAIL_ACTIVE
	nail.monitoring = true
	nail_visible.visible = true


func _sheathe() -> void:
	nail.monitoring = false
	nail_visible.visible = false


func _on_nail_area_entered(area: Area2D) -> void:
	if area.has_method("take_nail_hit"):
		area.take_nail_hit()
