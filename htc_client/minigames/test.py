"""htc_client.minigames.test"""

import sys

import pygame
from pygame.locals import *


def main(player, surface, font, clock):
    """test minigame"""

    foo = font.render('Test minigame', False, (0, 0, 0))

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        surface.fill((233, 233, 233))

        surface.blit(foo, (10, 10))

        pygame.display.flip()
