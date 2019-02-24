"""htc_client.minigames.Phishing"""

import sys

import pygame
from pygame.locals import *

sys.path.append('..')
from common import Background

NAME = 'Phishing'
POINTS = 300
IMG = './minigames/img/phishing.png'


def main(player, surface, font, clock):

    foo = font.render('Is this a Phishing email?', False, (0, 0, 0))
    button = pygame.Rect(100, 100, 100, 100)
    bg = Background('./minigames/img/phishing_background.jpg', [0, 0])

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    flag = 'testflag'
                    player.client.solve(NAME, flag)
                    return

        surface.fill([255, 255, 255])
        surface.blit(bg.image, bg.rect)
        surface.blit(foo, (10, 10))
        pygame.draw.rect(surface, [212, 0, 0], button)

        pygame.display.flip()
