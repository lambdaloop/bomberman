from bomber_constants import *
from bombermap import *
from explosion import *

class Bomb:
        def __init__(self, power, position, player):
                self.power = power
                self.position = position
                self.timeleft = 3000
                self.player = player

        def update(self, timelapsed):
                self.timeleft -= timelapsed
                if self.timeleft < 0:
                        self.explode()

        def explode(self):
                explosions.append(Explosion(self.power, self.position))
                self.player.recharge_bomb()
                self.remove()

        def remove(self):
                bombs.remove(self)
                if(get_object(self.position) == self):
                        set_object(self.position, None)
