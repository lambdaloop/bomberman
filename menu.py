import pygame
#from pygame.locals import *
from bomber_constants import *
from drawstuff import *


class Menu_screen:
    "Menu is made up of a series of menu screens that are linked together"

    def __init__(self, choices, param_updates, parameters = {}):
        self.choices = choices
        self.links = {}
        self.selector = 0
#        self.num_humans = num_humans
        self.length = len(choices)
        self.parameters = parameters
        self.param_updates = param_updates

    def link(self, selection, m_s):
        self.links[selection] = m_s
        m_s.links["Back"] = self

    def select(self):
#         selected = self.choices[self.selector]
#         if selected in self.links:
#             link = self.links[selected]
# #            if isinstance(link, Menu_screen):
# #                return link
#         #init_normal_game(self.num_humans, int(selected[0]))
#         return selected
        d = self.param_updates[self.selector]
        self.parameters.update(d)

        selected = self.choices[self.selector]
        link = self.links.get(selected, None)
        return (self.parameters, link)

    def menu_display(self):
        draw_menu(self)

    def incr_selector(self, incr):
        new = self.selector + incr
        while new >= self.length:
            new -= self.length
        while new < 0:
            new += self.length
        self.selector = new

def run_menu(m):
    m.menu_display()
    params = {}
    while True:
        pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pressed=event.key
        if pressed:
            if pressed == pygame.constants.K_DOWN:
                m.incr_selector(1)
            elif pressed == pygame.constants.K_UP:
                m.incr_selector(-1)
            elif pressed == pygame.constants.K_ESCAPE:
                if "Back" in m.links:
                    m = m.links["Back"]
                elif "Quit" in m.links:
                    return {'quit', True}
            elif pressed == pygame.constants.K_RETURN:
                ps, link = m.select()
                params.update(ps)
                if isinstance(link, Menu_screen):
                    m = link
                else:
                    return params

            m.menu_display()


def game_menu():
    root = Menu_screen(["0 humans", "1 human", "2 humans", "Quit"],
                       param_updates=[{'num_humans':0}, {'num_humans': 1}, {'num_humans':2}, {'quit': True}])
    root_0 = Menu_screen(["1 computer", "2 computers", "3 computers", "4 computers", "Back"],
                         param_updates=[{'num_computers': 1},{'num_computers': 2},{'num_computers': 3}, {'num_computers': 4},{}])
    root_1 = Menu_screen(["1 computer", "2 computers", "3 computers", "Back"],
                         param_updates=[{'num_computers': 1},{'num_computers': 2},{'num_computers': 3},{}])
    root_2 = Menu_screen(["0 computers", "1 computer", "2 computers", "Back"],
                         param_updates=[{'num_computers': 0}, {'num_computers': 1},{'num_computers': 2},{}])

    root.links["Quit"] = None
    root.link("0 humans", root_0)
    root.link("1 human", root_1)
    root.link("2 humans", root_2)

    return run_menu(root)
