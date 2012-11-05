import pygame
from bomber_constants import *
from bombermap import *

player_image = pygame.image.load('img/player.png')
computer_image = pygame.image.load('img/computer.png')
bomb_image = pygame.image.load('img/squarebomb.png')
explosion_image = pygame.image.load('img/explosion.png')

powerup_images = ['img/powerup_extrabombs.png', 'img/powerup_extrapower.png']
for i in range(len(powerup_images)):
    powerup_images[i] = pygame.image.load(powerup_images[i])

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

def horiz_center_rect(rect):
    rect.left = width/2 - rect.width/2

def vert_center_rect(rect):
    rect.top = height/2 - rect.height/2

def center_rect(rect):
    horiz_center_rect(rect)
    vert_center_rect(rect)

def draw_menu(menu_screen):
    font_path = 'coders_crux/GUBBLABLO.ttf'
    font = pygame.font.Font(font_path, 20)
    font_color = (255, 255, 153)
#    places = ((100, 100), (100, 175), (100, 250), (100, 325))
    y = 100
    item_distance = 50
    width_height = (250, 50)
    background_color = 15,15,15
    screen.fill(background_color)

    #draw title
    title_font = pygame.font.Font(font_path, 40)
    title = title_font.render("BOMBERSQUARE", True, nice_red)
    title_rect = title.get_rect().move((100, 20))
    horiz_center_rect(title_rect)
    screen.blit(title, title_rect)

    for i in range(menu_screen.length):
        if menu_screen.selector == i:
            surface = font.render(menu_screen.choices[i].upper(), True, black, nice_blue)
        else:
            surface = font.render(menu_screen.choices[i].upper(), True, white)
        rect = surface.get_rect()
        rect.top = y
        horiz_center_rect(rect)
        # if menu_screen.selector == i:
        #     highlight = pygame.Surface(surface.get_size())
        #     highlight.fill(light_green)
        #     screen.blit(highlight, rect)
        screen.blit(surface, rect)
        y += rect.height + item_distance
    pygame.display.flip()

def draw_player(p):
    rect = get_rect(p.position)
    screen.blit(player_image, rect)

def draw_computer(p):
    rect = get_rect(p.position)
    screen.blit(computer_image, rect)

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
    rect = get_rect(p.position)
    screen.blit(powerup_images[p.type], rect)

def draw_list_function(func, l):
    def f():
        for x in l:
            func(x)
    return f

draw_bombs = draw_list_function(draw_bomb, bombs)
draw_explosions = draw_list_function(draw_explosion, explosions)
draw_powerups = draw_list_function(draw_powerup, powerups)

def draw_players():
    for h in humans:
        draw_player(h)
    for c in computers:
        draw_computer(c)

white = 255,255,255
black = 0,0,0
red = 255,0,0
green = 0,255,0
blue = 0,0,255
chartreuse = 127,255,0
light_green = 131,255,100
nice_red = 207,45,64
sky_blue = 100,244,255
nice_blue = 0,194,255

def draw_game_over():
    font_path = 'coders_crux/GUBBLO___.ttf'
    font_size = 20
    # white_surface = pygame.Surface((370, 240))
    # white_surface.fill(white)
    # rect = white_surface.get_rect()
    # center_rect(rect)
    # screen.blit(white_surface, rect)

    game_over_font = pygame.font.Font(font_path, font_size*2)
    other_font = pygame.font.Font(font_path, font_size)

    y = height/2 - game_over_font.get_height()/2 - other_font.get_height()/2 * 2

    game_over_text = game_over_font.render("GAME OVER", True, black, white)
    game_over_rect = pygame.Rect((y, 150), game_over_text.get_size())
    horiz_center_rect(game_over_rect)
    screen.blit(game_over_text, game_over_rect)


    space_text = other_font.render("Press <space> to restart.", True, black, white)
    space_rect = space_text.get_rect().move([0, game_over_rect.bottom])
    horiz_center_rect(space_rect)
    screen.blit(space_text, space_rect)

    esc_text = other_font.render("Press <esc> for main menu.", True, black, white)
    esc_rect = esc_text.get_rect().move([0, space_rect.bottom])
    horiz_center_rect(esc_rect)
    screen.blit(esc_text, esc_rect)


def draw_stuff(game_over=False):
    screen.fill(white)
    draw_map()
    draw_powerups()
    draw_bombs()
    draw_players()
    draw_explosions()
    if game_over:
        draw_game_over()
    pygame.display.flip()
