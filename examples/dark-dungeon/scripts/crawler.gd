extends Area2D

## Tougher crawler. Two nail hits. Touching the player deals contact damage.

const HITS := 2

var hits := HITS

@onready var body: Sprite2D = $Body


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func take_nail_hit(amount: int = 1) -> void:
	hits -= amount
	if hits <= 0:
		_drop_shard()
		queue_free()
		return
	body.modulate = Color(0.7, 0.35, 0.4, 1)


func _drop_shard() -> void:
	var shard: Node2D = preload("res://scenes/shard.tscn").instantiate()
	get_parent().add_child(shard)
	shard.global_position = global_position


func _on_body_entered(other: Node2D) -> void:
	if other.has_method("take_contact_hit"):
		other.take_contact_hit()
