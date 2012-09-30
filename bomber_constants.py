import pygame

class Direction:
    up, down, left, right = range(4)

class BlockType:
    blank, wall, brick = range(3)

class PowerupType:
    extraBomb, speed, bombPower = range(3)

blockW, blockH = 32, 32
mapW, mapH = 15,13

size = width, height = blockW*mapW, blockH*mapH
speed = [4, 4]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("img/ball.gif")
ballrect = ball.get_rect()

Clock = pygame.time.Clock()
fps = 60

main_player = None

key_to_dir = {
    pygame.constants.K_UP: Direction.up,
    pygame.constants.K_DOWN: Direction.down,
    pygame.constants.K_LEFT: Direction.left,
    pygame.constants.K_RIGHT: Direction.right
};

bombs = []
explosions = []
powerups = []
players = []

num_humans = 0

mainLoop = True

def game_over():
    global mainLoop
    mainLoop = False
    print("game over!")
