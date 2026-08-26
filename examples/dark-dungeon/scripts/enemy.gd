extends Area2D

## One nail hit despawns this foe. Idle; no chase.


func take_nail_hit() -> void:
	queue_free()
