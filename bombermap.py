class Direction:
    up, down, left, right = range(4)

class BlockType:
    blank, wall, brick, powerup = range(4)

class PowerupType:
    extraBomb, speed, bombPower = range(3)

class Block:
    def __init__(self, btype=BlockType.blank, powerup=None, bomb = False):
        self.btype = btype
        self.powerup = powerup
        self.bomb = bomb
    def is_walkable(self):
        return self.btype != BlockType.wall
    def is_destroyable(self):
        return self.btype == BlockType.wall or self.btype == BlockType.powerup
    def is_bomb_passable(self):
        return btype == BlockType.blank
    def powerup(self):
        return self.powerup
    def destroy(self):
        if self.isDestroyable():
            self.btype = BlockType.blank
            self.powerup = None
            return True
        else:
            return False
    def add_bomb(self):
        self.bomb = True
    def remove_bomb(self):
        self.bomb = False
    def contains_bomb(self):
        return self.bomb


mapW, mapH = 20, 20
map = [[Block() for x in range(mapW)] for y in range(mapH)]