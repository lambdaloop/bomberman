import sys, pygame
import random #for AI
#import spritesheet
from bomber_constants import *
from player import *
from bombermap import *
from drawstuff import *


pygame.init()

start_positions = [[1,1], [13,11]]
# main_player = Player([1,1], num=0)
# second_player = Player([13, 11], num=1)

for i, pos in enumerate(start_positions):
    all_humans.add(Player(pos, num=i))

all_computers.add(Player([13, 1], num=-1, isComputer=True))

#all_humans.add(main_player)
#all_humans.add(second_player)

for p in all_humans:
    humans.add(p)

for p in all_computers:
    computers.add(p)

def reset_game():
    global bombs, explosions, powerups, humans

#    humans.add(main_player)
#    humans.add(second_player)
    humans.clear()
    for p in all_humans:
        p.reset()
        humans.add(p)

    computers.clear()
    for p in all_computers:
        p.reset()
        computers.add(p)

    # main_player.reset()
    # second_player.reset()

    # main_player.position = [1,1]
    # second_player.position = [13, 11]
    bombs.clear()
    explosions.clear()
    powerups.clear()

    for x in range(mapW):
        for y in range(mapH):
            map[x][y] = Block(startmap[x][y].btype)
            map_objects[x][y] = None


def handle_input(key, keydown=False):
    if key == None:
        return

    if key == pygame.constants.K_SPACE:
        reset_game()

    for h in humans.copy():
        if not h.alive:
            continue

        x = keys[h.num].get(key, None)
        if x == "bomb":
            h.drop_bomb()
        elif x != None:
            if keydown:
                h.player_move_delay = 0
                h.move(x)
                h.player_move_delay = repeat_key_wait
            else:
                h.move(x)

def do_AI(p):
    if p.repeat_move_delay > 0:
        return


    possible = []
    for (axis, inc) in ([0, -1], [0, 1], [1, -1], [1, 1]):
        pos = list(p.position)
        pos[axis] += inc
        if not is_valid_position(pos):
            continue

        b = get_block(pos)
        if b.is_destroyable() and not isinstance(get_object(p.position), Bomb):
            p.drop_bomb()
        if b.is_walkable() and \
             not isinstance(get_object(pos), explosion.Explosion) and \
             not isinstance(get_object(pos), Bomb):
            possible.append(pos)

    if possible != []:
        p.change_position(random.choice(possible))


def update_computers(t):
    for p in computers.copy():
        p.update(t)
        do_AI(p)

def update_bombs(t):
    for bomb in bombs.copy():
        bomb.update(t)

def update_explosions(t):
    for e in explosions.copy():
        e.update(t)

def update_humans(t):
    for p in humans.copy():
        p.update(t)

def update_stuff(t):
    update_bombs(t)
    update_explosions(t)
    update_humans(t)
    update_computers(t)

def is_game_over():
    return len(humans)<=0

def main_loop():
    while not is_game_over():
        tickFPS = Clock.tick(fps)
        pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pressed=event.key

        handle_input(pressed, keydown=True)
        all_pressed = pygame.key.get_pressed()
        for key in direction_keys:
            if all_pressed[key] and pressed != key:
                handle_input(key)

        update_stuff(tickFPS)
        draw_stuff()

while True:
    main_loop()
    #game over here
    pygame.time.delay(2000)
    reset_game()
