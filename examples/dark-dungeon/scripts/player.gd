extends CharacterBody2D

const SPEED := 200.0
const RECOVER := 0.28
const NAIL_ACTIVE := 0.12
const MAX_HP := 3
const IFRAMES := 0.55

var facing := Vector2.RIGHT
var recover := 0.0
var nail_active := 0.0
var hp := MAX_HP
var iframes := 0.0
var spawn_position := Vector2.ZERO
var shards := 0
var nail_damage := 1

@onready var nail: Area2D = $Nail
@onready var nail_visible: Sprite2D = $Nail/Visible
@onready var hp_label: Label = $HpLabel
@onready var shard_label: Label = $ShardLabel


func _ready() -> void:
	spawn_position = position
	nail.area_entered.connect(_on_nail_area_entered)
	_refresh_hp_label()
	_refresh_shard_label()


func _physics_process(delta: float) -> void:
	recover = maxf(0.0, recover - delta)
	iframes = maxf(0.0, iframes - delta)
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


func take_contact_hit() -> void:
	if iframes > 0.0:
		return
	hp -= 1
	iframes = IFRAMES
	_refresh_hp_label()
	if hp <= 0:
		_respawn()


func take_shard() -> void:
	shards += 1
	_refresh_shard_label()


func hone_nail(cost: int) -> bool:
	if nail_damage >= 2:
		return false
	if shards < cost:
		return false
	shards -= cost
	nail_damage = 2
	nail_visible.color = Color(0.95, 0.96, 1.0, 0.95)
	_refresh_shard_label()
	return true


func _respawn() -> void:
	hp = MAX_HP
	iframes = 0.0
	position = spawn_position
	_refresh_hp_label()


func _refresh_hp_label() -> void:
	hp_label.text = str(hp)


func _refresh_shard_label() -> void:
	shard_label.text = str(shards)


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
		area.take_nail_hit(nail_damage)
