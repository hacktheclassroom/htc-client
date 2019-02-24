"""htc_client.minigames.build_a_network"""

import sys

import pygame
from pygame.locals import *
from main import WIDTH, HEIGHT
from build_a_network.parser import BlockParser
sys.path.append('..')
from common import Background
from build_a_network.entity import BasicBlock, DraggableBlock, SelectableAndDraggableBlock, ClickableBlock
import random


NAME = 'Network Builder'
POINTS = 300
IMG = './minigames/img/phishing.png'

emails = [
    {
        'img': './minigames/img/email1.png',
        'malicious': False
    }

]


def main(player, surface, font, clock):


    # title = font.render('Is this a Phishing email?', False, (0, 0, 0))
    # good_button = pygame.Rect(1050, 100, 100, 100)
    # bad_button = pygame.Rect(1050, 500, 100, 100)
    # bg = Background('./minigames/img/phishing_background.jpg', [0, 0])
    # email_pic = pygame.image.load('./minigames/img/email.png')
    #
    # email_number = 0

    basic_blocks = pygame.sprite.Group()
    draggable_blocks = pygame.sprite.Group()
    snd_blocks = pygame.sprite.Group()
    clickable_blocks = pygame.sprite.Group()

    all_blocks = [
        basic_blocks,
        draggable_blocks,
        snd_blocks,
        clickable_blocks
    ]

    picked_up = None
    selected = None

    draw_line = False
    internet = BasicBlock((120, 0, 120), int(WIDTH*2/3) - 20, 20, int(WIDTH/3), 150, "internet")
    dmz = BasicBlock((0, 255, 0), int(WIDTH*2/3) - 20, 200, int(WIDTH/3), 200, "dmz")

    basic_blocks.add(dmz)
    basic_blocks.add(internet)

    parser = BlockParser(all_blocks)

    clickable_blocks.add(ClickableBlock(250, 250, 80, 40, "check_block", lambda: parser.parse()))

    for x in range(0, 2):
        for y in range(0, 2):
            block = DraggableBlock(x * 100 + 20, y * 100 + 20, "draggable{}{}".format(x,y))
            draggable_blocks.add(block)

    for x in range(0, 2):
        for y in range(2, 4):
            block = SelectableAndDraggableBlock(x * 100 + 20, y * 100 + 20, "snd{}{}".format(x,y))
            snd_blocks.add(block)
            draggable_blocks.add(block)

    while True:
        clock.tick(60)
        surface.fill([0, 0, 255])

        for block in snd_blocks:
            block.draw_line(surface)

        for blockgroup in all_blocks:
            blockgroup.draw(surface)

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

        if draw_line and selected:
            pygame.draw.line(surface, (0, 0, 0), (selected.rect.x + selected.rect.width/2, selected.rect.y + selected.rect.height/2),
                             pygame.mouse.get_pos(), 4)

        pygame.display.flip()



        #
        # for event in events:
        #     if event.type == pygame.QUIT:
        #         running = False
        #
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #         if event.button == 1:
        #             if rectangle.collidepoint(event.pos):
        #                 rectangle_draging = True
        #                 mouse_x, mouse_y = event.pos
        #                 offset_x = rectangle.x - mouse_x
        #                 offset_y = rectangle.y - mouse_y
        #
        #     elif event.type == pygame.MOUSEBUTTONUP:
        #         if event.button == 1:
        #             rectangle_draging = False
        #
        #     elif event.type == pygame.MOUSEMOTION:
        #         if rectangle_draging:
        #             mouse_x, mouse_y = event.pos
        #             rectangle.x = mouse_x + offset_x
        #             rectangle.y = mouse_y + offset_y
        #
        # surface.fill([255, 255, 255])
        # surface.blit(bg.image, bg.rect)
        # surface.blit(title, (10, 10))
        #
        # email_img = pygame.image.load(emails[email_number]['img'])
        # surface.blit(email_img, (50, 50))
        #
        # pygame.draw.rect(surface, [0, 212, 0], good_button)
        # pygame.draw.rect(surface, [212, 0, 0], bad_button)
