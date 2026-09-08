extends Area2D

## Nail shrine. Two shards hone the nail. Already honed does nothing.

const COST := 2

@onready var body: Sprite2D = $Body


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _on_body_entered(other: Node2D) -> void:
	if not other.has_method("hone_nail"):
		return
	if other.hone_nail(COST):
		body.modulate = Color(0.55, 0.6, 0.62, 1)
