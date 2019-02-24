"""htc_client.game"""

import sys
import importlib

import pygame
from pygame.locals import *


def run_game(player, surface, font, clock):
    """HTC primary game loop, returns a minigame."""

    # build a minigame list of Rects
    x, y = 0, 120
    minigames = {}
    mg = importlib.import_module('minigames')
    mg_names = mg.__all__

    for m in mg_names:
        mod = importlib.import_module('minigames.{}'.format(m))
        points = mod.POINTS
        m_x, m_y = 10+x, 10+y
        minigames[m] = {
            'x': m_x,
            'y': m_y,
            'rect': pygame.Rect(m_x, m_y, 246, 200), # 256-10 ;)
            'text': font.render('{} - {}'.format(m, points), False, (0, 0, 0)),
            'color': [69, 137, 255]
        }
        x += 252
        if x > 1200:
            y += 256
            x = 0

    # get and load score
    score = player.client.score()['score']
    score_text = font.render('Score: {}'.format(str(score)), False, (0, 0, 0))

    # title
    title_text = font.render('Choose A Minigame', False, (0, 0, 0))

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
        surface.blit(score_text, (10, 10))
        surface.blit(title_text, (490, 10))

        for _, v in minigames.items():
            pygame.draw.rect(surface, v['color'], v['rect'])
            surface.blit(v['text'], (v['x'], v['y']))

        pygame.display.flip()
