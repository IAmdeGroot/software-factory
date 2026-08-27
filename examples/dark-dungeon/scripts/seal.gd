extends Area2D

## Cracked seal. Only a honed nail (damage 2) breaks it.

const NEED := 2


func take_nail_hit(amount: int = 1) -> void:
	if amount < NEED:
		return
	get_parent().queue_free()
