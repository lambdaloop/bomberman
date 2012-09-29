import sys, pygame
import spritesheet
import bombermap

pygame.init()

size = width, height = 800, 600
speed = [4, 4]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

Clock = pygame.time.Clock()
fps = 60

main_player = Player([1,1])

key_to_dir = {pygame.constants.K_UP: Direction.up};

bombs = []

def handle_input(key):
    if not key:
        return

    dir = key_to_dir.get(key, None)
    if dir:
        main_player.move(dir)
    if key == pygame.constants.K_SPACE:
        main_player.drop_bomb()

def handle_AI():
    pass

def update_map():
    pass

def draw_stuff():
    draw_map()
    draw_players()
    draw_explosions()

while 1:
    tickFPS = Clock.tick(fps)
    pressed = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed=event.key

    handle_input(pressed)
    handle_AI()
    update_map()
    draw_stuff()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    # screen.fill(black)
    # screen.blit(ball, ballrect)
    # pygame.display.flip()
