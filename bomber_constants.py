import pygame
from bombermap import *

size = width, height = 800, 600
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
players = []
powerups = []
