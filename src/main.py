"""htc-client"""

import sys

from htc_api import Client

# all the pygame imports
import pygame
import pygameMenu
from pygame.locals import *
from pygameMenu.locals import *


# globals
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
MENU_BACKGROUND_COLOR = (58, 58, 58)
WIDTH = 1280
HEIGHT = 720
WINDOW_SIZE = (WIDTH, HEIGHT)
MENU_FONT_SIZE = 36
MENU_ALPHA = 100

pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Hack The Classroom')
clock = pygame.time.Clock()


class Player:
    def __init__(self, username, server_code):
        self.username = username
        self.server_code = server_code
        self.client = Client(self.username, self.password)

        self.points = 0

# TODO: from text inputs
# player = Player('vesche', 'fewgf2j4j')
# player.client.validate()


def main_background():
    surface.fill(COLOR_BLACK)


play_menu = pygameMenu.Menu(
    surface,
    bgfun=main_background,
    color_selected=COLOR_WHITE,
    font=pygameMenu.fonts.FONT_BEBAS,
    font_color=COLOR_BLACK,
    font_size=MENU_FONT_SIZE,
    menu_alpha=MENU_ALPHA,
    menu_color=MENU_BACKGROUND_COLOR,
    menu_height=HEIGHT,
    menu_width=WIDTH,
    onclose=PYGAME_MENU_DISABLE_CLOSE,
    option_shadow=False,
    title='Play',
    window_height=WINDOW_SIZE[1],
    window_width=WINDOW_SIZE[0]
)

about_menu = pygameMenu.TextMenu(
    surface,
    bgfun=main_background,
    color_selected=COLOR_WHITE,
    font=pygameMenu.fonts.FONT_BEBAS,
    font_color=COLOR_BLACK,
    font_size_title=MENU_FONT_SIZE,
    menu_color=MENU_BACKGROUND_COLOR,
    menu_color_title=COLOR_WHITE,
    menu_height=HEIGHT,
    menu_width=WIDTH,
    onclose=PYGAME_MENU_DISABLE_CLOSE,
    option_shadow=False,
    text_color=COLOR_BLACK,
    title='About',
    window_height=WINDOW_SIZE[1],
    window_width=WINDOW_SIZE[0]
)

main_menu = pygameMenu.Menu(
    surface,
    bgfun=main_background,
    color_selected=COLOR_WHITE,
    font=pygameMenu.fonts.FONT_BEBAS,
    font_color=COLOR_BLACK,
    font_size=MENU_FONT_SIZE,
    menu_alpha=100,
    menu_color=MENU_BACKGROUND_COLOR,
    menu_height=HEIGHT,
    menu_width=WIDTH,
    onclose=PYGAME_MENU_DISABLE_CLOSE,
    option_shadow=False,
    title='Hack The Classroom',
    window_height=WINDOW_SIZE[1],
    window_width=WINDOW_SIZE[0]
)

main_menu.add_option('Play', play_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)


def main():
    # HTC menu loop
    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                sys.exit(0)

        main_menu.mainloop(events)
        pygame.display.flip()

    # start game loop on successful break of menu loop
    # while True:
    #   do things


if __name__ == '__main__':
    main()
