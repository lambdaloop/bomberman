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
        self.length = len(choices)
        self.parameters = parameters
        self.param_updates = param_updates

    def link(self, selection, m_s):
        self.links[selection] = m_s
        m_s.links["Back"] = self

    def select(self):
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


class Text_Menu_screen(Menu_screen):
    def __init__(self, text, choices=["Back"], param_updates=[{}], parameters={}):
        super(Text_Menu_screen, self).__init__(choices, param_updates, parameters)
        self.text = text
    def menu_display(self):
        screen.fill((15,15,15))
        new_top = draw_text(self.text)
        draw_menu(self, background=False, first_item_top = new_top, item_distance = 20)


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



about_text = \
""" ABOUT
Bombersquare 1.0

DEVELOPERS
Pierre Karashchuk
Steven Yang

FONTS USED
Gubblebum by Tjarda Koster
SquareFont by Bou Fonts
"""

controls_text = \
""" CONTROLS

Player 1
Movement: w, a, s, d (for up, left, down, right)
Bomb: Left Shift

Player 2
Movement: Arrow keys
Bomb: Right Shift

Also
[Space] to reset game.
[Esc] to go back to main menu.
"""
def game_menu():

    root = Menu_screen(["0 humans", "1 human", "2 humans", "Back"],
                       param_updates=[{'num_humans':0}, {'num_humans': 1},
                                      {'num_humans':2}, {}])
    root_0 = Menu_screen(["2 computers", "3 computers", "4 computers", "Back"],
                         param_updates=[{'num_computers': 2}, {'num_computers': 3},
                                        {'num_computers': 4},{}])
    root_1 = Menu_screen(["1 computer", "2 computers", "3 computers", "Back"],
                         param_updates=[{'num_computers': 1},{'num_computers': 2},
                                        {'num_computers': 3},{}])
    root_2 = Menu_screen(["0 computers", "1 computer", "2 computers", "Back"],
                         param_updates=[{'num_computers': 0}, {'num_computers': 1},
                                        {'num_computers': 2},{}])


    about = Text_Menu_screen(about_text)
    controls = Text_Menu_screen(controls_text)
    main_menu = Menu_screen(["Play", "Controls", "About", "Quit"],
                            [{}, {}, {}, {'quit':True}])


    main_menu.link("Play", root)
    main_menu.link("Controls", controls)
    main_menu.link("About", about)
    main_menu.links["Quit"] = None

    root.link("0 humans", root_0)
    root.link("1 human", root_1)
    root.link("2 humans", root_2)

    return run_menu(main_menu)
