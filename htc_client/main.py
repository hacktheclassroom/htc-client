#!/usr/bin/env python

"""htc_client.main"""

import pygame
from pygame.locals import *

from importlib import import_module

from menu import run_menu
from game import run_game


WIDTH = 1280
HEIGHT = 720
WINDOW_SIZE = (WIDTH, HEIGHT)

pygame.init()
pygame.font.init()

surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Hack The Classroom')
clock = pygame.time.Clock()

# TODO: Fix font
# myfont = pygame.font.Font('./font.ttf', 36)
font = pygame.font.Font(None, 36)


def main():
    player = run_menu(surface, font, clock)

    while True:
        minigame_name = run_game(surface, font, clock)

        # run a minigame
        module = import_module('minigames.{}'.format(minigame_name))
        minigame = getattr(module, 'main')
        minigame(surface, font, clock)


if __name__ == '__main__':
    main()
