from bomber_constants import *
from bombermap import *
from bomb import *

class Player:
    def __init__(self, position, isComputer = False , max_bombs = 5, power = 1):
        self.computer = isComputer
        self.position = position
        self.max_bombs = max_bombs
        self.power = power
        self.bombinv = max_bombs

    def move(self, dir):
        new_position = list(self.position)
        if dir == Direction.right:
            new_position[0] += 1
        elif dir == Direction.left:
            new_position[0] -= 1
        elif dir == Direction.up:
            new_position[1] -= 1
        elif dir == Direction.down:
            new_position[1] += 1

        if can_move(new_position):
            if isinstance(get_object(self.position), Player):
                set_object(self.position, None)
            self.position = new_position
            set_object(new_position, self)

    def drop_bomb(self):
        if (self.bombinv > 0):
            b = Bomb(self.power, self.position, self)
            bombs.append(b)

            self.bombinv = self.bombinv - 1
            set_object(self.position, b)

    def recharge_bomb(self, num = 1):
        if self.bombinv + num <= self.max_bombs:
            self.bombinv = self.bombinv + num

    def powerup_power(self, num = 1):
        self.power += num

    def powerup_bomb(self, num = 1):
        self.max_bombs += num
        self.bombinv += num

    def die(self):
        global num_humans
        if self in players:
            players.remove(self)
        if not self.computer:
            num_humans -= 1
        if num_humans <= 0:
            game_over()
