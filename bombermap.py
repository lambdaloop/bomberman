class Direction:
    up, down, left, right = range(4)

class BlockType:
    blank, wall, brick, powerup = range(4)

class PowerupType:
    extraBomb, speed, bombPower = range(3)

class Block:
    def __init__(self, btype=BlockType.blank, powerup=None, bomb = False):
        self.btype = btype
    def is_walkable(self):
        return self.btype != (BlockType.wall and BlockType.brick)
    def is_destroyable(self):
        return self.btype == BlockType.wall
    def is_bomb_passable(self):
        return self.btype == BlockType.blank

    def destroy(self):
        if self.isDestroyable():
            self.btype = BlockType.blank
            return True
        else:
            return False

blockW, blockH = 32, 32
mapW, mapH = 15, 13
test = True

if test:
    map = [[Block() for x in range(mapW)] for y in range(mapH)]
else:
    textfile = open("map.txt", "rt")
    key = {'w' : BlockType.wall, ' ' : BlockType.blank, '-' : BlockType.brick}
    map = [][]
    for i in range(mapH):
        line = textfile.readline()
        for j in range(mapW):
            map[j][i] = Block(line[j])

    text.file.close()

map_objects = [[None for x in range(mapW)] for y in range(mapH)]

def set_object(pos, obj):
    map_objects[pos[0]][pos[1]] = obj

def get_object(pos):
    return map_objects[pos[0]][pos[1]]

def get_block(pos):
    return map[pos[0]][pos[1]]

def get_player(position):
    for player in players:
        if player.position == position:
            return player
    return False

def can_move(new_position):
    if not get_block(new_position).is_walkable():
        return False
    else:
        obj = get_object(new_position)
        if obj and (not isinstance(obj, Powerup)):
            return False
        elif get_player(new_position):
            return False
        else:
            return True
