from bomber_constants import *
from powerup import *
import bomb
import bombermap
import random

class Explosion:
    def __init__(self, power, position):
        self.power = power
        self.position = position
        self.timeleft = 1000

        ps = self.explode()
        ps.append(self.position)
        self.exploded_positions = ps
        for pos in self.exploded_positions:
            bombermap.set_object(pos, self)

    def update(self, timelapsed):
        self.timeleft -= timelapsed
        if self.timeleft < 0:
            self.remove()

    def remove(self):
        for pos in self.exploded_positions:
            bombermap.set_object(pos, None)
        explosions.remove(self)

    def explode(self):
        "Returns the array of positions of the explosion in a direction dir from the bomb, in order"
        final = []

        for axis in [0,1]:
            for increment in [-1, 1]:
                new_position = list(self.position)
                for i in range(self.power):
                    new_position[axis] += increment
                    if bombermap.can_explosion_pass(new_position):
                        final.append(list(new_position))
                    else:
                        obj = bombermap.get_object(new_position)
                        if obj != None:
                            if(isinstance(obj, Powerup)):
                                powerups.remove(obj)
                            elif(isinstance(obj, bomb.Bomb)):
                                obj.explode()

                            bombermap.set_object(new_position, None)

                        if bombermap.get_block(new_position).is_destroyable():
                            bombermap.get_block(new_position).destroy()
                            if random.random() < powerup_proportion:
                                print("powerup at ", new_position)
                                p = random_powerup(new_position)
                                powerups.append(p)
                                bombermap.set_object(new_position, p)

                        if bombermap.get_player(new_position):
                            final.append(list(new_position))
                            bombermap.get_player(new_position).die()
                        break
        print(final)
        return final
