#!/usr/bin/env python

"""htc_client.main"""

from menu import run_menu

import pygame
from pygame.locals import *

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
    # run game here


if __name__ == '__main__':
    main()
