import pygame
from pygame.locals import *
from bomber_constants import *
from drawstuff import *


class Menu_screen:
    "Menu is made up of a series of menu screens that are linked together"

    def __init__(self, choices, num_humans = 0):
        self.choices = choices
        self.links = {}
        self.selector = 0
        self.num_humans = num_humans
        self.length = len(choices)

    def link(self, selection, m_s):
        self.links[selection] = m_s
        m_s.links["Back"] = self

    def select(self):
        selected = self.choices[self.selector]
        if selected in self.links:
            link = self.links[selected]
            if isinstance(link, Menu_screen):
                return link
        init_normal_game(self.num_humans, int(selected[0]))
        return None

    def menu_display(self):
        draw_menu(self)

    def incr_selector(self, incr):
        new = self.selector + incr
        while new >= self.length:
            new -= self.length
        while new < 0:
            new += self.length
        self.selector = new

    def take_input(self):
        self.menu_display()
        while True:
            pressed = None
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        pressed=event.key
            if pressed:
                if pressed == pygame.constants.K_DOWN:
                    self.incr_selector(1)
                elif pressed == pygame.constants.K_UP:
                    self.incr_selector(-1)
                elif pressed == pygame.constants.K_RETURN:
                    next_menu = self.select()
                    if next_menu != None:
                        next_menu.take_input()
                    return
                self.menu_display()

def menu():
    root = Menu_screen(["1 Human", "2 Humans"])
    root_1 = Menu_screen(["1 CPU", "2 CPU", "3 CPU", "Back"], num_humans = 1)
    root_2 = Menu_screen(["0 CPU", "1 CPU", "2 CPU", "Back"], num_humans = 2)

    root.link("1 Human", root_1)
    root.link("2 Humans", root_2)

    current = root
    current.take_input()
