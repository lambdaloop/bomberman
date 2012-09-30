class Explosion:

	def __init__(self, power, position):
		self.power = power
		self.position = position
		self.timeleft = 1000
		self.exploded_positions = [position].extend(explode(Direction.left)).extend(explode(Direction.right))
		.extend(explode(Direction.up)).extend(explode(Direction.down))


	def update(self, timelapsed):
		self.timeleft -= timelapsed
		if self.timeleft < 0:
			self.remove()

	def remove(self):
		explosions.remove(self)

	def explode(self, dir):
		"Returns the array of positions of the explosion in a direction dir from the bomb, in order"
		final = []
		flame = self.position

		if dir == Direction.left:
			axis = 0
			increment = -1
		elif dir == Direction.right:
			axis = 0
			increment = 1
		elif dir == Direction.up:
			axis = 1
			increment = -1
		elif dir == Direction.down:
			axis = 1
			increment = 1

		for i in range(power):
			new_position = list[flame]
			new_position[axis] += increment
			if can_move(new_position):
				final.append(new_position)
				flame = new_position

			else 
				if get_block(new_position).is_destroyable():
					get_block(new_position).destroy()
				elif get_obj(new_position) != None:
					set_object(new_position, None)
				elif get_player(new_position):
					players.remove(get_player(new_position))
				return final

		return final
