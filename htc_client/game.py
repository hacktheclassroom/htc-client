
import sys

import pygame
from pygame.locals import *


def run_game(surface, font, clock):
    """HTC primary game loop, returns a minigame."""

    minigames = {
        'test': {
            'rect': pygame.Rect(100, 100, 100, 100),
            'color': [112, 0, 0]
        }
    }

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for k, v in minigames:
                    if v['rect'].collidepoint(mouse_pos):
                        return k

        surface.fill((233, 233, 233))

        for _, v in minigames.items():
            pygame.draw.rect(surface, v['color'], v['rect'])

        pygame.display.flip()
