def can_move(new_position):
    return gameboard[new_position[0]][new_position[1]].is_walkable()


class Player:
    def __init__(self, position, isComputer = False , max_bombs = 1, power = 1):
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
            self.position = new_position

    def add_power(self, num):
        self.power += num

    def add_bomb(self, num):
        self.max_bombs += num
        self.bombinv += num

    def drop_bomb(self):
        if (self.bombinv > 0):
            b = Bomb(power, position)
            map[position[0],position[1]].add_bomb()
            bombs.append(b)
            self.bombinv = bombinv - 1
