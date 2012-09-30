import sys, pygame
import spritesheet
from bomber_constants import *
from bombermap import *
from drawstuff import *
from player import *

pygame.init()

main_player = Player([1,1])
players.append(main_player)
second_player = Player([13, 11])
players.append(second_player)

num_humans = 1

def handle_input(key):
    if key == None:
        return

    dir = key1_to_dir.get(key, None)
    if dir != None:
        main_player.move(dir)

    dir = key2_to_dir.get(key, None)
    if dir != None:
        second_player.move(dir)

    if key == pygame.constants.K_LSHIFT:
        main_player.drop_bomb()
    elif key == pygame.constants.K_RSHIFT:
        second_player.drop_bomb()

def execute_AI():
    pass

def update_bombs(t):
    for bomb in bombs:
        bomb.update(t)

def update_explosions(t):
    for e in explosions:
        e.update(t)

def update_stuff(t):
    #update explosions
    update_bombs(t)
    update_explosions(t)

while mainLoop:
    tickFPS = Clock.tick(fps)
    pressed = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed=event.key

    handle_input(pressed)
    execute_AI()
    update_stuff(tickFPS)
    draw_stuff()

    # ballrect = ballrect.move(speed)
        # if ballrect.left < 0 or ballrect.right > width:
        #     speed[0] = -speed[0]
        # if ballrect.top < 0 or ballrect.bottom > height:
        #     speed[1] = -speed[1]

    # screen.fill(black)
        # screen.blit(ball, ballrect)
        # pygame.display.flip()

sys.exit()
