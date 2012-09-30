import pygame

player_image = None
block_images = []
bomb_image = None
explosion_image = None

def pos_to_pixel(pos):
    return [pos[0]*blockW, pos[1]*blockH]

def get_rect(pos):
    rect = standard_rect
    rect.left, rect.top = pos_to_pixel(pos)
    return rect

def draw_player(p):
    rect = get_rect(b.position))
    pygame.blit(player_image, rect)

def draw_block(b, pos):
    if b.btype == BlockType.blank:
        return
    rect = get_rect(pos)
    img = block_images[b.btype]
    pygame.blit(img, rect)

def draw_bomb(b):
    rect = get_rect(b.position)
    pygame.blit(bomb_image, rect)

def draw_map():
    for x in range(mapW):
        for y in range(mapH):
            draw_block(map[x][y])

def draw_explosion(e):
    positions = e.exploded_positions
    for p in positions:
        rect = get_rect(p)
        pygame.blit(explosion_image, rect)

def draw_bombs():
    for b in bombs:
        draw_bomb(b)

def draw_players():
    for p in players:
        draw_player(p)

def draw_explosions():
    for e in explosions:
        draw_explosion(e)

def draw_stuff():
    draw_map()
    draw_players()
    draw_bombs()
    draw_explosions()
    pygame.display.flip()
