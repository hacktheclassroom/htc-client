"""htc_client.minigames.build_a_network"""

import sys

import pygame
from pygame.locals import *
from main import WIDTH, HEIGHT
from build_a_network.util import BlockParser, Puzzle
sys.path.append('..')
from common import Background
from build_a_network.entity import BasicBlock, DraggableBlock, SelectableAndDraggableBlock, ClickableBlock

import random


NAME = 'Network Builder'
POINTS = 300
IMG = './minigames/img/build_a_network/icon.png'

PUZZLES = {
    "puzzle1": {
        "snd_blocks": ["firewall", "router", "database", "server"],
        "draggable_blocks": []
    }
}


class RunTracker(object):
    def __init__(self, parser):
        self.done = False
        self.parser = parser
        self.result = None

    def finish(self):
        self.done = True
        self.result = self.parser.parse()

    def get_result(self):
        if self.result:
            return self.result
        else:
            return []


def main(player, surface, font, clock):


    # title = font.render('Is this a Phishing email?', False, (0, 0, 0))
    # good_button = pygame.Rect(1050, 100, 100, 100)
    # bad_button = pygame.Rect(1050, 500, 100, 100)
    # bg = Background('./minigames/img/phishing_background.jpg', [0, 0])
    # email_pic = pygame.image.load('./minigames/img/email.png')
    #
    # email_number = 0

    # Pick a random puzzle TODO
    puzzle = PUZZLES["puzzle1"]
    blockgroups = Puzzle(**puzzle).make_blockgroups()

    basic_blocks = pygame.sprite.Group()
    clickable_blocks = pygame.sprite.Group()
    draggable_blocks = blockgroups["draggable_blockgroup"]
    snd_blocks = blockgroups["snd_blockgroup"]

    all_blocks = [
        clickable_blocks,
        basic_blocks,
        draggable_blocks,
        snd_blocks

    ]

    picked_up = None
    selected = None

    draw_line = False
    internet = BasicBlock((120, 0, 120), int(WIDTH*2/3) - 20, 20, int(WIDTH/3), 150, "internet")
    dmz = BasicBlock((0, 255, 0), int(WIDTH*2/3) - 20, 350, int(WIDTH/3), 200, "dmz")
    bg = Background('./minigames/img/build_a_network/bground.png', [0, 0])

    basic_blocks.add(dmz)
    basic_blocks.add(internet)

    parser = BlockParser(all_blocks)
    tracker = RunTracker(parser)

    clickable_blocks.add(ClickableBlock(int(WIDTH/2-460), HEIGHT-165, 80, 40, "submit", tracker.finish))

    while not tracker.done:
        clock.tick(60)

        # surface.blit(bg.image, bg.rect)
        surface.fill([255, 255, 255])

        for blockgroup in all_blocks:
            blockgroup.draw(surface)

        if draw_line and selected:
            pygame.draw.line(surface, (0, 0, 0), (selected.rect.x + selected.rect.width/2, selected.rect.y + selected.rect.height/2),
                             pygame.mouse.get_pos(), 4)

        for block in snd_blocks:
            block.draw_line(surface)



        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = False
                for blocks in all_blocks:
                    for sprite in blocks:
                        if sprite.rect.collidepoint(event.pos):
                            if isinstance(sprite, ClickableBlock):
                                sprite.on_click()
                            if isinstance(sprite, DraggableBlock):
                                picked_up = sprite
                            if isinstance(sprite, SelectableAndDraggableBlock):
                                if draw_line and selected:
                                    sprite.join_to(selected)
                                selected = sprite
                                clicked = True
                            break

                if not clicked:
                    selected = None

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                picked_up = None

            if event.type == pygame.MOUSEMOTION:
                if selected:
                    draw_line = True

                if picked_up:
                    selected = None
                    mouse_x, mouse_y = event.pos
                    picked_up.rect.x = mouse_x - picked_up.rect.width/2
                    picked_up.rect.y = mouse_y - picked_up.rect.height/2

        pygame.display.flip()

    flags = tracker.get_result()
    for flag in flags:
        player.client.solve('bnetwork', flag)
    return
