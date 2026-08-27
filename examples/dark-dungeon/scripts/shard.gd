extends Area2D

## Floor shard. Walking over it collects it.


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _on_body_entered(other: Node2D) -> void:
	if other.has_method("take_shard"):
		other.take_shard()
		queue_free()
