import pygame
import sys

class Direction:
        up, down, left, right = range(4)

class BlockType:
        blank, wall, brick = range(3)

class PowerupType:
        extraBomb, bombPower = range(2)

scale = 1.5
blockW, blockH = int(32*scale),int(32*scale)
mapW, mapH = 15,13

size = width, height = blockW*mapW, blockH*mapH

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bombersquare")

Clock = pygame.time.Clock()
fps = 60

map_key = {'w' : BlockType.wall, ' ' : BlockType.blank, '-' : BlockType.brick}

repeat_key_wait = 1000
player_move_delay = 150
computer_move_delay = 200 #300

key1_us_to_dir = {
        pygame.constants.K_w: Direction.up,
        pygame.constants.K_s: Direction.down,
        pygame.constants.K_a: Direction.left,
        pygame.constants.K_d: Direction.right,
        pygame.constants.K_LSHIFT: "bomb"
};

key1_dvorak_to_dir = {
        pygame.constants.K_COMMA: Direction.up,
        pygame.constants.K_o: Direction.down,
        pygame.constants.K_a: Direction.left,
        pygame.constants.K_e: Direction.right,
        pygame.constants.K_LSHIFT: "bomb"
};

key1_to_dir = key1_us_to_dir.copy()
key1_to_dir.update(key1_dvorak_to_dir)

key2_to_dir = {
    pygame.constants.K_UP: Direction.up,
    pygame.constants.K_DOWN: Direction.down,
    pygame.constants.K_LEFT: Direction.left,
    pygame.constants.K_RIGHT: Direction.right,
    pygame.constants.K_RSHIFT: "bomb"
};

keys = [key1_to_dir, key2_to_dir]

direction_keys = []

for d in keys:
    for (k, val) in d.items():
        if isinstance(val, int):
            direction_keys.append(k)

bombs = set()
explosions = set()
powerups = set()

humans = set()
computers = set()

all_humans = set()
all_computers = set()

def game_over():
    print("game over!")
