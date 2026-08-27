extends Area2D

## Amber skitter. Patrols north-south. One nail hit. Contact damages the player.

const SPEED := 70.0
const Y_MIN := 180.0
const Y_MAX := 540.0

var dir := 1.0


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _process(delta: float) -> void:
	position.y += dir * SPEED * delta
	if position.y >= Y_MAX:
		position.y = Y_MAX
		dir = -1.0
	elif position.y <= Y_MIN:
		position.y = Y_MIN
		dir = 1.0


func take_nail_hit() -> void:
	queue_free()


func _on_body_entered(other: Node2D) -> void:
	if other.has_method("take_contact_hit"):
		other.take_contact_hit()
