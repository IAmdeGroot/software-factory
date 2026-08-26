extends Area2D

## Idle insect. Nail despawns it. Touching the player deals contact damage.


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func take_nail_hit() -> void:
	queue_free()


func _on_body_entered(body: Node2D) -> void:
	if body.has_method("take_contact_hit"):
		body.take_contact_hit()
