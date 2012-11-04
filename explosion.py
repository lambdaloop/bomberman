from bomber_constants import *
from powerup import *
import player
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

        if bombermap.get_player(self.position):
            bombermap.get_player(self.position).die()


    def update(self, timelapsed):
        self.timeleft -= timelapsed
        if self.timeleft < 0:
            self.remove()

    def remove(self):
        for pos in self.exploded_positions:
            bombermap.set_object(pos, None)
        explosions.discard(self)

    def explode(self):
        "Returns the array of positions of the explosion in a direction dir from the bomb, in order"
        final = []

        for (axis, increment) in [[0, -1], [0, 1], [1, -1], [1, 1]]:
            new_position = list(self.position)
            for i in range(self.power):
                new_position[axis] += increment
                if not bombermap.is_valid_position(new_position):
                    break
                elif bombermap.can_explosion_pass(new_position):
                    final.append(list(new_position))
                else:
                    obj = bombermap.get_object(new_position)

                    if obj != None:
                        if isinstance(obj, Powerup):
                            powerups.discard(obj)
                        elif isinstance(obj, bomb.Bomb):
                            obj.explode()
                        elif isinstance(obj, player.Player):
                            obj.die()
                            final.append(list(new_position))

                        if not isinstance(obj, Explosion):
                            bombermap.set_object(new_position, None)

                    if bombermap.get_block(new_position).is_destroyable():
                        bombermap.get_block(new_position).destroy()
                        if random.random() < powerup_proportion:
                            p = random_powerup(new_position)
                            powerups.add(p)
                            bombermap.set_object(new_position, p)

                    # need extra check for players because player may not be
                    # on map if placing bomb
                    p = bombermap.get_player(new_position)
                    if p:
                        final.append(list(new_position))
                        p.die()
                    break
        return final
