import pygame
import sys

class Direction:
	up, down, left, right = range(4)

class BlockType:
	blank, wall, brick = range(3)

class PowerupType:
	extraBomb, bombPower = range(2)

blockW, blockH = 32, 32
mapW, mapH = 15,13

size = width, height = blockW*mapW, blockH*mapH
speed = [4, 4]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

Clock = pygame.time.Clock()
fps = 60

main_player = None

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

key1_to_dir = key1_us_to_dir

key2_to_dir = {
	pygame.constants.K_UP: Direction.up,
	pygame.constants.K_DOWN: Direction.down,
	pygame.constants.K_LEFT: Direction.left,
	pygame.constants.K_RIGHT: Direction.right,
	pygame.constants.K_RSHIFT: "bomb"
};

keys = [key1_to_dir, key2_to_dir]

bombs = set()
explosions = set()
powerups = set()

humans = set()
computers = set()

def game_over():
	print("game over!")

