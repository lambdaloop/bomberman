import pygame
from bomber_constants import *
from bombermap import *

player_image = pygame.image.load('img/player.png')
bomb_image = pygame.image.load('img/squarebomb.png')
explosion_image = pygame.image.load('img/explosion.png')

block_images = [None, 'img/wall.png', 'img/brick.png']
for i in range(1, len(block_images)):
    block_images[i] = pygame.image.load(block_images[i])



standard_rect = pygame.Rect(0, 0, blockW, blockH)

def pos_to_pixel(pos):
    return [pos[0]*blockW, pos[1]*blockH]

def get_rect(pos):
    rect = standard_rect
    rect.left, rect.top = pos_to_pixel(pos)
    return rect

def draw_player(p):
    rect = get_rect(p.position)
    screen.blit(player_image, rect)

def draw_block(b, pos):
    if b.btype == BlockType.blank:
        return
    rect = get_rect(pos)
    img = block_images[b.btype]
    screen.blit(img, rect)

def draw_bomb(b):
    rect = get_rect(b.position)
    screen.blit(bomb_image, rect)

def draw_map():
    for x in range(mapW):
        for y in range(mapH):
            draw_block(map[x][y], [x,y])

def draw_explosion(e):
    positions = e.exploded_positions
    for p in positions:
        rect = get_rect(p)
        screen.blit(explosion_image, rect)

def draw_powerup(p):
    pass

def draw_list_function(func, l):
    def f():
        for x in l:
            func(x)
    return f

draw_bombs = draw_list_function(draw_bomb, bombs)
draw_players = draw_list_function(draw_player, players)
draw_explosions = draw_list_function(draw_explosion, explosions)
draw_powerups = draw_list_function(draw_powerup, powerups)

white = 255,255,255

def draw_stuff():
    screen.fill(white)
    draw_map()
    draw_players()
    draw_bombs()
    draw_explosions()
    pygame.display.flip()
