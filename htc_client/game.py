"""htc_client.game"""

import sys
import importlib

import pygame
from pygame.locals import *

from common import Background


def run_game(player, surface, font, clock):
    """HTC primary game loop, returns a minigame."""

    # build a minigame list of Rects
    x, y = 50, 120
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
            'text': font.render('{} - {}'.format(m, points), False, (255, 255, 255)),
            'color': [90, 69, 0],
            'img': pygame.image.load(mod.IMG)
        }
        x += 252
        if x > 1200:
            y += 256
            x = 0

    # get and load score
    score = player.client.score()['score']
    score_text = font.render('Score: {}'.format(str(score)), False, (255, 255, 255))

    # title
    title_text = font.render('Choose A Minigame', False, (255, 255, 255))

    bg = Background('./minigames/img/chalkboard.jpg', [0, 0])

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

        surface.fill([255, 255, 255])
        surface.blit(bg.image, bg.rect)
        surface.blit(score_text, (50, 50))
        surface.blit(title_text, (490, 50))

        for _, v in minigames.items():
            pygame.draw.rect(surface, v['color'], v['rect'])
            surface.blit(v['text'], (v['x']+10, v['y']))
            surface.blit(v['img'], (v['x']+60, v['y']+45))

        pygame.display.flip()
