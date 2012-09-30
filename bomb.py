from bomber_constants import *
from bombermap import *
from explosion import *

class Bomb:
        def __init__(self, power, position):
                self.power = power
                self.position = position
                self.timeleft = 3000

        def update(self, timelapsed):
                self.timeleft -= timelapsed
                if self.timeleft < 0:
                        self.explode()

        def explode(self):
                explosions.append(Explosion(self.power, self.position))
                self.remove()

        def remove(self):
                explosions.remove(self)
