"""htc_client.minigames.Phishing"""

import sys

import pygame
from pygame.locals import *

NAME = 'Phishing'
POINTS = 300


def main(player, surface, font, clock):

    foo = font.render('Phishing minigame', False, (0, 0, 0))
    button = pygame.Rect(100, 100, 100, 100)

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

        surface.fill((233, 233, 233))
        surface.blit(foo, (10, 10))
        pygame.draw.rect(surface, [212, 0, 0], button)

        pygame.display.flip()
