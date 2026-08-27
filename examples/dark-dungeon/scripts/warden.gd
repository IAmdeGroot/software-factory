extends Area2D

## Room-3 warden. Six hit points, slow east-west patrol. Does not pursue.

const HITS := 6
const SPEED := 50.0
const X_MIN := 1600.0
const X_MAX := 1920.0

var hits := HITS
var dir := 1.0

@onready var body: ColorRect = $Body


func _ready() -> void:
	body_entered.connect(_on_body_entered)


func _process(delta: float) -> void:
	position.x += dir * SPEED * delta
	if position.x >= X_MAX:
		position.x = X_MAX
		dir = -1.0
	elif position.x <= X_MIN:
		position.x = X_MIN
		dir = 1.0


func take_nail_hit(amount: int = 1) -> void:
	hits -= amount
	if hits <= 0:
		_show_cleared()
		_drop_shard()
		queue_free()
		return
	body.color = body.color.darkened(0.2)


func _show_cleared() -> void:
	var label := get_parent().get_node_or_null("ClearLabel")
	if label is CanvasItem:
		label.visible = true


func _drop_shard() -> void:
	var shard: Node2D = preload("res://scenes/shard.tscn").instantiate()
	get_parent().add_child(shard)
	shard.global_position = global_position


func _on_body_entered(other: Node2D) -> void:
	if other.has_method("take_contact_hit"):
		other.take_contact_hit()
