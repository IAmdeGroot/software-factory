extends Area2D

## Nail shrine. Two shards hone the nail. Already honed does nothing.

const COST := 2

@onready var body: ColorRect = $Body


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _on_body_entered(other: Node2D) -> void:
	if not other.has_method("hone_nail"):
		return
	if other.hone_nail(COST):
		body.color = Color(0.22, 0.2, 0.18, 1)
