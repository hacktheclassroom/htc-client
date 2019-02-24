"""htc_client.game"""

import sys

import pygame
from pygame.locals import *


def run_game(surface, font, clock):
    """HTC primary game loop, returns a minigame."""

    # later ls the minigames folder and get these names
    i = 0
    minigames = {}
    mg_names = ['test']
    
    for m in mg_names:
        minigames[m] = {
            'rect': pygame.Rect(10, 10+i, 256, 256),
            'color': [112, 0, 0]
        }
        i += 100

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for k, v in minigames.items():
                    if v['rect'].collidepoint(mouse_pos):
                        return k

        surface.fill((233, 233, 233))

        for _, v in minigames.items():
            pygame.draw.rect(surface, v['color'], v['rect'])

        pygame.display.flip()
