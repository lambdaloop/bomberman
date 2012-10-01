import sys, pygame
#import spritesheet
from bomber_constants import *
from bombermap import *
from drawstuff import *
from player import *

pygame.init()

main_player = Player([1,1], num=0)
second_player = Player([13, 11], num=1)

humans.add(main_player)
humans.add(second_player)

def reset_game():
	global bombs, explosions, powerups, humans

	humans.add(main_player)
	humans.add(second_player)

	main_player.reset()
	second_player.reset()

	main_player.position = [1,1]
	second_player.position = [13, 11]
	bombs.clear()
	explosions.clear()
	powerups.clear()

	for x in range(mapW):
		for y in range(mapH):
			map[x][y] = Block(startmap[x][y].btype)
			map_objects[x][y] = None


def handle_input(key):
	if key == None:
		return

	if key == pygame.constants.K_SPACE:
		reset_game()

	for h in humans:
		if not h.alive:
			continue

		x = keys[h.num].get(key, None)
		if x == "bomb":
			h.drop_bomb()
		elif x != None:
			h.move(x)
		

def execute_AI():
	pass

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

		handle_input(pressed)
		execute_AI()
		update_stuff(tickFPS)
		draw_stuff()

while True:
	main_loop()
	#game over here
	pygame.time.delay(2000)
	reset_game()









