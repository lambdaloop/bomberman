import explosion
from bomber_constants import *
from bombermap import *
from bomb import *


class Player:
    def __init__(self, position, isComputer = False , num=0, max_bombs = 1, power = 1):
        self.computer = isComputer
        self.start_position = position
        self.position = position
        self.max_bombs = max_bombs
        self.power = power
        self.bombinv = max_bombs
        self.alive = True
        self.num = num
        if self.computer:
            self.repeat_move_delay = computer_move_delay
        else:
            self.repeat_move_delay = 0


    def reset(self):
        self.max_bombs = 1
        self.power = 1
        self.bombinv = self.max_bombs
        self.alive = True
        self.position = self.start_position
        if self.computer:
            self.repeat_move_delay = computer_move_delay
        else:
            self.repeat_move_delay = 0

    def update(self, time):
        obj = get_object(self.position)
        if isinstance(obj, Powerup):
            self.use_powerup(obj)
            set_object(self.powerup, self)
        elif isinstance(obj, explosion.Explosion):
            self.die()

        if self.repeat_move_delay > 0:
            self.repeat_move_delay -= time

    def change_position(self, new_position):
        if self.repeat_move_delay > 0:
            return

        if not can_move(new_position) or new_position == self.position:
            return

        if isinstance(get_object(self.position), Player):
            set_object(self.position, None)

        obj = get_object(new_position)
        if isinstance(obj, Powerup):
            self.use_powerup(obj)
        elif isinstance(obj, explosion.Explosion):
            self.die()

        set_object(new_position, self)
        self.position = new_position

        if self.computer:
            self.repeat_move_delay = computer_move_delay
        else:
            self.repeat_move_delay = player_move_delay


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

        self.change_position(new_position)

    def use_powerup(self, obj):
        if obj.type == 0:
            self.powerup_bomb()
        else:
            self.powerup_power()
        powerups.discard(obj)

    def drop_bomb(self):
        if (self.bombinv > 0):
            b = Bomb(self.power, self.position, self)
            bombs.add(b)

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
        self.alive = False
        global humans, computers

        computers.discard(self)
        humans.discard(self)
