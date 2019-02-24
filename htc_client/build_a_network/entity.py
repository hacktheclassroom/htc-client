from pygame.sprite import Sprite
from pygame import Surface
import pygame


class BasicBlock(Sprite):
    def __init__(self, color, startx, starty, width, height, name):
        super(BasicBlock, self).__init__()

        self.image = Surface([width, height])
        self.image.fill(color)
        self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty

        self.name = name


class DraggableBlock(BasicBlock):
    def __init__(self, startx, starty, name, color=(255, 0, 0), img=None):
        super(DraggableBlock, self).__init__(
            color=color,
            startx=startx,
            starty=starty,
            name=name,
            width=80,
            height=80
        )
        # self.image = pygame.image.load("player.png").convert()


class SelectableAndDraggableBlock(DraggableBlock):
    def __init__(self, startx, starty, name, color=(255, 165, 0), img=None):
        super(SelectableAndDraggableBlock, self).__init__(startx, starty, name, color=color, img=img)
        self.joined_to = None

    def join_to(self, other_block):
        self.joined_to = other_block
        other_block.joined_to = self

    def draw_line(self, surface):
        if self.joined_to:
            pygame.draw.line(surface, (0, 0, 0),
                             (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2),
                             (self.joined_to.rect.x + self.joined_to.rect.width / 2, self.joined_to.rect.y + self.joined_to.rect.height / 2), 4)


class ClickableBlock(BasicBlock):
    def __init__(self, startx, starty, width, height, name, on_click, img=None):
        super(ClickableBlock, self).__init__(
            color=(0, 120, 120),
            startx=startx,
            starty=starty,
            width=width,
            height=height,
            name=name
        )
        self.on_click = on_click

    def check_click(self):
        click_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(click_pos):
            self.on_click(click_pos)

