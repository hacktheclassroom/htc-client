#!/usr/bin/env python

"""htc_client.main"""

import pygame
import sys
from pygame.locals import *

from importlib import import_module

from menu import run_menu
from game import run_game
from player import Player

WIDTH = 1280
HEIGHT = 720
WINDOW_SIZE = (WIDTH, HEIGHT)

pygame.init()
pygame.font.init()

surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Hack The Classroom')
clock = pygame.time.Clock()
font = pygame.font.Font('./font.ttf', 32)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--debug":
        username, server_code = sys.argv[2].split(":")
        player = Player(username, server_code)
    else:
        player = run_menu(surface, font, clock)

    while True:
        minigame_name = run_game(player, surface, font, clock)

        # run a minigame
        module = import_module('minigames.{}'.format(minigame_name))
        minigame = getattr(module, 'main')
        minigame(player, surface, font, clock)


if __name__ == '__main__':
    main()
