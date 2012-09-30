class Bomb:

	def _init_(self, power, position):
		self.power = power
		self.position = position
		self.timeleft = 3000

	def update(timelapsed):
		self.timeleft -= timelapsed
		if self.timeleft < 0:
			self.explode()
	
	def explode():
		explosions.append(Explosion(self.power, self.position))
		self.remove()
	
	def remove(self):
		explosions.remove(self)