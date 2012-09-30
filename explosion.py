class Explosion:

	def _init_(self, power, position):
		self.power = power
		self.position = position
		self.timeleft = 1000
		self.exploded_positions = [position].extend(check_left).extend(check_right).extend(check_up).extend(check_down)


	def update(self, timelapsed):
		self.timeleft -= timelapsed
		if self.timeleft < 0:
			self.remove()

	def remove(self):
		explosions.remove(self)

	def check_left(self):
		"Returns the array of positions of the explosion left of bomb, in order"
		final = []
		flame = self.position
		for i in range(power):
			new_position = list[flame]
			new_position[0] -= 1
			if can_move(new_position):
				final.append(new_position)
				flame = new_position
			elif map[new_position[0], new_position[1]].is_destroyable():
				map[new_position[0], new_position[1]].destroy()
				return final
			else
				return final
		return final

	def check_right(self):

	def check_up(self):

	def check_down(self):
